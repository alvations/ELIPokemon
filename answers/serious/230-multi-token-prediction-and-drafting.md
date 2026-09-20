---
id: "230"
slug: multi-token-prediction-and-drafting
style: serious
category: open-weights
difficulty: advanced
question: "Multi-token prediction shows up as a training objective and as a decoding trick. Are they the same thing?"
tags: [multi-token-prediction, speculative-decoding, deepseek, inference, throughput]
---

# Same head, two jobs — and only one of them is guaranteed to pay.

They are the same weights used at two different times. As a **training objective**, multi-token
prediction forces the model to represent more than the immediate next token, which is a quality
argument. As an **inference trick**, the extra head is a free draft model you already trained,
which is a throughput argument. DeepSeek-V3 is the clearest case because it is literally the same
module doing both: trained as an auxiliary objective, shipped in the weights, and re-used at
serving time for self-speculation.

Question [033](033-speculative-decoding.md) covers why draft-and-verify is exactly lossless. This
is the part that decides whether you should turn it on.

## The objective

DeepSeek-V3's MTP is not the parallel-independent-heads design of
[Gloeckle et al., 2024](https://arxiv.org/abs/2404.19737). It is a **sequential** chain: one extra
transformer block per prediction depth, sharing the main model's embedding table and output head,
each depth conditioned on the previous depth's representation. V3 ships depth 1 — one extra module
predicting `t+2`.

```
   training                                          serving

   h_t ─┬─► head ─► token t+1   (main loss)          h_t ─┬─► head ─► t+1  (target, kept)
        │                                                 │
        └─► MTP block ─► head ─► token t+2               └─► MTP block ─► t+2  (draft)
             │                                                  │
             └ shared embedding + shared output head             └ same weights, now
               ~1 extra block of params                            a drafter to verify

   the gradient reaches the trunk from BOTH.        the module is optional at inference;
   that is the quality claim.                       dropping it changes nothing.
```

Two things follow. The training signal is denser — every position supervises two predictions — and
the trunk is pushed to pre-plan, because `h_t` now has to be usable for a token it is not directly
emitting. The claim is a quality gain that survives discarding the module. Take that as a claim:
it is an ablation inside one lab's report, not an independently reproduced law.

## The trick, and its cost model

Draft `γ` tokens cheaply, verify all `γ+1` positions in one target forward pass, accept the
longest prefix that survives modified rejection sampling, and take one bonus token from the
corrected distribution. With per-token acceptance `α`:

```
   E[tokens per verify]  =  (1 − α^(γ+1)) / (1 − α)

   round cost  ≈  γ · c + 1        c = draft cost / target cost   (c ≈ 0.1 for an MTP block)
   speedup     ≈  E[tokens] / (γ · c + 1)
```

```
        α       γ=1              γ=2              γ=4              γ=7
   ─────────────────────────────────────────────────────────────────────────
      0.90   E 1.90  ×1.73    E 2.71  ×2.26    E 4.10  ×2.93    E 5.70  ×3.35
      0.80   E 1.80  ×1.64    E 2.44  ×2.03    E 3.36  ×2.40    E 4.16  ×2.45
      0.60   E 1.60  ×1.45    E 1.96  ×1.63    E 2.31  ×1.65    E 2.46  ×1.45
      0.40   E 1.40  ×1.27    E 1.56  ×1.30    E 1.65  ×1.18    E 1.67  ×0.98
   ─────────────────────────────────────────────────────────────────────────
                                                                    ▲
                        at α = 0.4 and γ = 7 you are slower than not speculating
```

Read the bottom-right corner first. `E[tokens]` is monotone in `γ` — it never gets worse — but the
*speedup* is not, because every drafted token you throw away was still paid for. The optimal `γ`
falls as `α` falls, and past some point the answer is to turn it off.

The published DeepSeek numbers sit on this table exactly. V3's report gives an acceptance rate of
**85–90%** for the second token and a **1.8×** improvement in generation TPS. With `γ = 1` the
formula is simply `1 + α`, so `α = 0.85` gives 1.85 tokens per pass, and 1.8× is that minus the
cost of running the extra block. The arithmetic and the announcement agree, which is the check
worth doing on any speculative-decoding claim you are handed.

## Why the speedup is workload-dependent

`α` is not a property of the model. It is a property of **model, drafter, prompt, sampler and
batch size together**, and all five move it:

* **Predictability of the text.** Closing brackets, import blocks, JSON that echoes a schema, and
  verbatim quotation from the context all draft at very high `α`. Novel chain-of-thought, the
  first token after a topic switch, and rare proper nouns draft badly. The same deployment can sit
  at 0.9 on one endpoint and 0.5 on another.
* **Sampling temperature.** Higher temperature flattens the target distribution, `α = E[min(p,q)]`
  falls, and the speedup falls with it. Greedy decoding is the friendliest case.
* **Batch size, and this is the one people miss.** At batch 1, decode is memory-bandwidth bound
  and the arithmetic units are idle, so verifying `γ+1` positions is nearly free. At high batch
  the GPU is already compute-saturated; speculation multiplies the effective batch by `γ+1` and
  starts competing with the real work. Production servers gate it on a batch threshold for this
  reason, and a benchmark run at batch 1 tells you nothing about your fleet.
* **Context length.** Verification attends over the whole KV cache, so the "one forward pass" is
  not constant-cost at 200K tokens the way it is at 2K.
* **Drafter alignment.** A good small model is not automatically a good drafter. What matters is
  agreement with the target's distribution, not the drafter's standalone quality — which is why
  self-speculation from an MTP head, trained on the same data on the same trunk, tends to beat a
  separately trained small model of similar cost.

What never moves is the output distribution. Rejection sampling makes the result exactly the
target's, so a bad `α` costs throughput and can never cost correctness. That asymmetry is why
speculation is safe to ship and easy to A/B: the only risk is that it does not help.

## Where this stands, September 2026

EAGLE-3-style trained drafters are reported to have landed in vLLM, SGLang and TensorRT-LLM
during early 2026, and "ships an MTP module in the weights" has become a normal line on an
open-model card — DeepSeek-V3 and its successors, and the GLM-5.x and Kimi releases, all carry
one. Treat the specific speedup numbers as the perishable part: they are measured at a batch size,
a context length and a temperature that are probably not yours. The durable parts are the two
formulas above and the discipline of asking, of any published speedup, *at what batch size, and at
what acceptance rate*. I could not reach arXiv or the model cards from this environment, so the
acceptance-rate and framework-support figures here are from coverage of the primary reports;
verify them before quoting.

## What an interviewer digs into next

* Why does `E[tokens]` rise with `γ` while the speedup can fall?
* Why does speculative decoding stop helping at high batch size?
* Is a stronger draft model always a better draft model?

**Citation note.** The arXiv identifiers linked above are given from working knowledge and
checked against search results. `arxiv.org` is blocked from the environment this was written
in, so **not one of the papers was opened while writing**. Resolve every identifier before
you cite it.
