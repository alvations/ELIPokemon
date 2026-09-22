---
id: "253"
slug: speculative-decoding-exactness
style: serious
category: optimization
difficulty: advanced
question: "Speculative decoding claims to be exact, not approximate. Why is that true?"
tags: [speculative-decoding, rejection-sampling, exactness, inference, sampling]
---

# Because the correction step puts back exactly the probability mass the draft took.

Speculative decoding accepts a drafted token with probability `min(1, p(x)/q(x))`, and on
rejection resamples from the **residual** distribution `norm(max(0, p − q))`. Those two branches
are constructed so that their probabilities sum, token by token, to `p(x)`. Not approximately —
the output of the accept-or-correct step is a sample from `p`, the target model's distribution,
for any draft distribution `q` whatsoever, including a deliberately terrible one. A bad drafter
lowers the acceptance rate and therefore the speedup. It cannot move the output distribution,
because the correction is not a repair for a good guess; it is an accounting identity.

Question [033](033-speculative-decoding.md) introduces the algorithm and
[230](230-multi-token-prediction-and-drafting.md) does the throughput arithmetic. This answer is
the proof and the fine print.

## The one-token proof

Let `q` be the draft distribution at this position and `p` the target's. Draw `x ~ q`, draw `u ~
U[0,1)`, accept if `u < p(x)/q(x)`. Write `r(y) = max(0, p(y) − q(y))` and `Z = Σ_y r(y)`. There
are two ways the emitted token can be `y`:

```
  P(emit y)  =  P(draft y) · P(accept y)          +  P(reject anything) · residual(y)
             =  q(y) · min(1, p(y)/q(y))          +  Z · r(y)/Z

  case  p(y) ≥ q(y):   q(y)·1            + (p(y) − q(y))   =  p(y)      ✔
  case  p(y) <  q(y):  q(y)·(p(y)/q(y))  + 0               =  p(y)      ✔
```

The only thing that has to check out is that the rejection probability really is `Z`, and it is:

```
  P(accept)  =  Σ_y q(y)·min(1, p(y)/q(y))  =  Σ_y min(p(y), q(y))  =  α
  P(reject)  =  1 − Σ_y min(p,q)            =  Σ_y max(0, p−q)      =  Z   ✔
```

That second line is the identity worth memorising, because it is also the whole theory of drafter
quality:

```
  α  =  Σ min(p, q)  =  1 − TV(p, q)          TV = ½ Σ |p − q|
```

**The per-token acceptance rate is one minus the total variation distance between drafter and
target.** Nothing else about the drafter matters — not its benchmark scores, not its size, not
whether it is a good model. Only how far its distribution sits from the target's, at the positions
you are actually decoding.

## Worked numbers

Three candidate tokens, a drafter that has never seen the third one:

```
  token        A       B       C          α = Σ min(p,q) = 0.60 + 0.20 + 0 = 0.80
  ───────────────────────────────────────  TV(p,q) = ½(0.10+0.10+0.20) = 0.20
  q (draft)   0.70    0.30    0.00        α = 1 − TV   ✔
  p (target)  0.60    0.20    0.20
  ───────────────────────────────────────
  accept w.p.  6/7     2/3      —         min(1, p/q)
  reject mass 0.10    0.10     0.00       q·(1 − p/q) = q − p where q > p
  residual     0       0       1.00       norm(max(0, p−q)) = 0.20/0.20

  emitted A:  0.70 × 6/7           = 0.60   ✔ = p(A)
  emitted B:  0.30 × 2/3           = 0.20   ✔ = p(B)
  emitted C:  0.20 (reject) × 1.00 = 0.20   ✔ = p(C)
```

Now hand it a drafter with almost no overlap — `q = (0.60, 0.20, 0.20)` against `p = (0, 0.40,
0.60)` on tokens A/B/C:

```
  α = 0 + 0.20 + 0.20 = 0.40 ... and the emitted distribution is still exactly p.
  reject mass 0.60;  residual = norm(0, 0.20, 0.40) = (0, 1/3, 2/3)
  emitted B: 0.20 + 0.60×(1/3) = 0.40 ✔     emitted C: 0.20 + 0.60×(2/3) = 0.60 ✔
```

Same guarantee, worse throughput. That asymmetry is the licence to ship speculation without a
quality eval, and it is the single most useful property of the technique.

## Extending to γ positions

Verify the drafted prefix left to right. Position `i` is only reached if positions `1..i−1` were
all accepted, so the chain rule applies unchanged: each position samples from the target's
conditional given an *already exact* prefix. The moment a position rejects, everything after it is
discarded — those drafts were conditioned on a token that did not happen. Because the verification
pass computed the target's distribution at position `i` anyway, the resample is free, which is why
a rejection still yields one good token.

If **all** `γ` are accepted, the verification pass has also produced the target's distribution at
position `γ+1`, conditioned on a fully accepted prefix. Sampling it costs nothing and is exact,
and that is the **bonus token** — the reason expected accepted length is `(1 − α^(γ+1))/(1 − α)`
rather than a `γ`-capped quantity. vLLM's `RejectionSampler` names these three categories
directly: *accepted*, *recovered* (the residual draw) and *bonus* tokens, and states in its own
docstring that the implementation follows [Leviathan et al.](https://arxiv.org/abs/2211.17192) —
primary, read from the repository.

Under greedy decoding `p` is a point mass on the argmax, so `min(1, p/q)` is 1 exactly when the
draft token *is* the argmax and 0 otherwise. The rule degenerates to string equality, which is why
greedy speculative decoding is often implemented as a `==` and still deserves the word exact.

## What exactness does not give you

This is where good candidates separate themselves, because every item below has shipped as a bug.

* **It is distributional, not sample-wise.** Same distribution, different random draws. A seeded
  run with speculation on will not emit the same string as a seeded run with it off, because the
  random numbers are consumed in a different order. Equality tests must compare distributions or
  fix both the draft and the correction stream.
* **The truncation samplers must be applied to the target *before* the correction.** If you serve
  with `top_p = 0.9`, the distribution you promised the user is the truncated one, so `p` in the
  accept rule must be the truncated `p`. vLLM does this — `apply_sampling_constraints` divides the
  target logits for the drafted positions by temperature and then applies top-k/top-p before the
  sampler runs (primary). An implementation that corrects against the raw softmax while the
  non-speculative path truncates is silently serving a different distribution.
* **A constrained-decoding mask is part of `p` too.** Grammar-constrained or schema-constrained
  decoding replaces the target distribution. Correct against the masked one.
* **Floating point is not exact.** `p` is computed in a forward pass whose kernels, tile shapes
  and reduction order depend on how many tokens are in the batch — and speculation changes that
  number. Bitwise-identical logits across the two paths are not on offer without batch-invariant
  kernels.
* **Several popular variants deliberately abandon the guarantee.** Medusa's *typical acceptance*
  keeps any draft above a probability floor. vLLM exposes `rejection_sample_method` values
  `"synthetic"` and `"block"` alongside `"standard"` (primary, from the config). These are fine
  choices; they are not the lossless algorithm, and a stack that quietly uses one while citing the
  exactness result is mis-selling. Ask which mode is on.

## What an interviewer digs into next

* Show that `Σ min(p,q) = 1 − TV(p,q)`, and say what follows for choosing a drafter.
* Why can a rejected position's successors not be reused?
* Where should top-k be applied, and what breaks if it is applied only to the draft?

## Where this stands, September 2026

The proof is permanent. It is four lines of algebra over two distributions and it will be true for
every architecture and every accelerator that comes after this one; the identity `α = 1 − TV(p,q)`
will still be how you reason about any drafter in ten years. The perishable half is everything in
the fine print: which framework applies truncation where, what the lossy acceptance modes are
called, and whether the default is `"standard"`. Those were read first-hand from the vLLM tree in
September 2026 and will move. Re-read the sampler in the version you deploy; the guarantee lives
in that file, not in the paper.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was resolved
while writing**. Resolve every identifier before you cite it.
