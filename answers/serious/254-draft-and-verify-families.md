---
id: "254"
slug: draft-and-verify-families
style: serious
category: optimization
difficulty: intermediate
question: "A separate draft model, Medusa heads, EAGLE, lookahead, n-gram lookup — how do the drafting families differ?"
tags: [speculative-decoding, eagle, medusa, lookahead, prompt-lookup]
---

# They differ in one thing: what the drafter is allowed to look at.

Every draft-and-verify method runs the same verification step, so they are interchangeable from
the correctness side — [253](253-speculative-decoding-exactness.md) applies to all of them
equally. What separates them is the drafter's **information set**. An n-gram matcher sees only the
token string. A separate small model sees the string through its own weights. Medusa heads see the
target's final hidden state. EAGLE sees the target's hidden states and rolls them forward
autoregressively. Jacobi sees the target itself. Acceptance rate climbs roughly in that order, and
so does the cost of getting the drafter in the first place — parameters, a training run, or both.

Since `α = 1 − TV(draft, target)`, the ranking is not mysterious. Every step up that list gives
the drafter more of what the target conditioned on, so its distribution sits closer to the
target's.

## The families

```
  family            extra weights   needs training?   conditions on              draft cost
  ───────────────────────────────────────────────────────────────────────────────────────────
  n-gram / prompt      none            no             the token string alone      ~0
  lookup                                              (match, then copy)
  suffix decoding      none            no             string + a cache of past    ~0
                                                      responses
  Jacobi /             none            no             the target model itself     1 target pass
  lookahead                                           (fixed-point iteration)       per iteration
  ───────────────────────────────────────────────────────────────────────────────────────────
  layer-skip /         none            usually yes    a truncated prefix of the   ~0.2 × target
  self-speculation                     (to be good)   target's own layers
  Medusa heads         K small heads   yes (cheap;    the target's FINAL hidden   ~0.01 × target
                                       trunk frozen   state, K heads independent    per head
                                       in Medusa-1)
  EAGLE / EAGLE-3      1 decoder       yes            target hidden states,       ~0.05 × target
                       layer                          rolled forward one step       per step
                                                      at a time, own LM head or
                                                      the target's
  MTP module in        ships in the    already done   like EAGLE: a real block    ~0.1 × target
  the weights          checkpoint                     on the target's trunk
  ───────────────────────────────────────────────────────────────────────────────────────────
  separate draft       a whole model   no (if one     its own weights only        0.02–0.1 ×
  model                                exists)                                      target
```

**n-gram / prompt lookup.** Take the last `n` emitted tokens, find that n-gram earlier in the
prompt, propose whatever followed it. No model, no training, no parameters. vLLM exposes it as
`method="ngram"` with `prompt_lookup_min` and `prompt_lookup_max` bounding the match length
(primary, read from the repository). It is astonishingly good on the workloads where the output
quotes the input — code editing, diff application, summarisation, RAG answers that cite — and it
contributes nothing at all on free prose, where the continuation has never appeared before.
**Suffix decoding** is the grown-up version: vLLM keeps a suffix tree over the prompt plus a
global cache of past responses (`suffix_decoding_max_cached_requests` defaults to 10,000, tree
depth 24, and it only speculates tokens whose frequency-estimated probability clears
`suffix_decoding_min_token_prob`, default 0.1 — all primary).

**Jacobi and lookahead decoding.** Guess a window of `n` future tokens, run the target over all of
them in parallel, and each position gets replaced by what the target actually says there. Iterate.
It is Jacobi iteration on the decoding fixed point, it provably converges to the same sequence
greedy decoding would produce in at most `n` steps, and it needs no second model and no training
at all. [Lookahead decoding](https://arxiv.org/abs/2402.02057) makes it pay by harvesting n-grams
out of the Jacobi trajectory into a pool and verifying them as drafts. The cost is that each
iteration is a full target pass over a window, so the win depends on converging in well under `n`
steps.

**Layer-skip self-speculation.** Draft with a prefix of the target's own layers, verify with all
of them. Zero extra weights and the KV cache is shared, which is the real attraction. Off the
shelf the early-exit distribution is poor; [LayerSkip](https://arxiv.org/abs/2404.16710) trains
for it explicitly with layer dropout and an early-exit loss, which is a training run you have to
want.

**Medusa.** Bolt `K` small heads onto the frozen trunk; head `k` predicts token `t+k` from the
same final hidden state ([Cai et al.](https://arxiv.org/abs/2401.10774)). Training is cheap
because the backbone does not move (Medusa-1; Medusa-2 unfreezes it and does better). The
structural weakness is that the heads are **conditionally independent** — head 2 does not know
what head 1 chose — so the joint they define is a product of marginals and drifts from the target
fast with depth. Medusa answers that with a candidate tree and, separately, with *typical
acceptance*, which trades the exactness guarantee for a higher accept rate. The first fix is free;
the second is not ([255](255-tree-drafting-and-verification.md)).

**EAGLE.** Drop the independence. Draft in **feature space**: a single decoder layer takes the
target's penultimate-layer hidden states, shifted and concatenated with the embedding of the token
actually sampled, and predicts the *next hidden state*; the token distribution comes from the LM
head. Because it is autoregressive over features, depth-2 drafting knows what depth 1 chose, and
acceptance holds up far longer. EAGLE-2 makes the candidate tree context-dependent by using the
drafter's own confidence as a proxy for acceptance; EAGLE-3 reportedly drops the
feature-regression loss in favour of direct token training with multi-step ("training-time test")
supervision and fuses low, middle and high layer features from the target. EAGLE is the default
recommendation in both vLLM and SGLang as of this writing, and both ship `eagle` and `eagle3` as
first-class methods (primary). EAGLE-2 and EAGLE-3 design details here are **coverage**, not a
reading of the papers.

**A separate draft model.** The original formulation. A 1B drafting for a 70B of the same family
works because they were trained on similar data, and `α` tracks that similarity, not the drafter's
standalone quality. Costs: a second set of weights resident in HBM, a second KV cache, a second
tensor-parallel layout to get right, and a hard requirement that the tokenizers agree — vLLM now
offers `use_heterogeneous_vocab`, which builds a token-level intersection at init and constrains
the draft logits to the shared tokens, but that is a workaround with its own acceptance cost
(primary).

**MTP modules shipped in the checkpoint** sit between EAGLE and a draft model and cost you nothing
to obtain, because the lab trained them. See [215](215-multi-token-prediction-and-speculation.md)
and [230](230-multi-token-prediction-and-drafting.md); vLLM's method list carries more than twenty
vendor-specific `*_mtp` entries, which tells you how normal this has become.

## How to choose

Run n-gram first if any part of your traffic quotes its input — it is free, it composes with a
batch-size gate, and it answers the question of whether draft-and-verify helps you at all before
you pay for anything. If the checkpoint ships an MTP module, that is the next cheapest real
drafter. Reach for EAGLE when you can afford to train a head on traffic that looks like yours,
which is precisely when it beats a generic small model: a drafter tuned on your distribution has
lower TV against your target on your prompts, and that is the only number that matters. Reach for
a separate draft model last, when a good one already exists in the family and you have the memory
to spare.

## What an interviewer digs into next

* Why do Medusa's independent heads lose acceptance with depth, and how does EAGLE avoid it?
* When is a zero-parameter n-gram drafter better than a trained one?
* What breaks if the draft and target tokenizers differ?

## Where this stands, September 2026

The taxonomy is durable: drafters will keep being ranked by what they get to condition on and what
they cost to obtain, and that ordering predates every name in the table. The names are the
perishable part. The method list, the config defaults and the suffix-decoding numbers above were
read directly from the vLLM and SGLang trees in September 2026 and are primary for that snapshot;
the EAGLE-2 and EAGLE-3 mechanism descriptions are coverage. Whichever three names are fashionable
when you read this, ask the same two questions of each: what does the drafter see, and who paid to
train it.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was resolved
while writing**. Resolve every identifier before you cite it.
