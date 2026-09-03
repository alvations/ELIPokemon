---
id: "013"
slug: context-length-limits
style: serious
category: transformers
difficulty: intermediate
question: "Why is context length limited, and what actually breaks when you extend it?"
tags: [context-length, long-context, lost-in-the-middle, needle-in-haystack]
---

# Why context length is limited

Four separate walls, and people usually only name the first.

## 1. Quadratic attention compute

Attention costs `O(n²·d)`. Doubling context quadruples the attention FLOPs and the intermediate
memory. FlashAttention removes the `O(n²)` *memory*, and the FFN's `O(n·d²)` term still dominates
at moderate lengths — but past roughly 32k, attention takes over and grows without bound.

## 2. The KV cache

Linear in `n`, but with a large constant, and **per concurrent request**. This is usually the
binding constraint in production: a 128k-context deployment may serve a tenth of the users of a
8k one on identical hardware.

## 3. Positional generalisation

Learned positional embeddings simply have no vector for position 100 000. RoPE degrades more
gracefully but still puts attention logits out of distribution past its training length — hence
position interpolation, NTK-aware scaling and YaRN, all of which need a fine-tuning phase.

## 4. The training data does not exist

This is the underrated one. Very few natural documents are 200k tokens long and *coherently
dependent* across that span. Long-context training data is largely synthetic or concatenated,
so models are trained on far fewer genuinely long-range dependencies than their advertised
window implies.

## What actually breaks: retrieval ≠ reasoning

The distinction that matters in an interview:

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  NEEDLE IN A HAYSTACK                                            │
  │  "Find this one sentence in 128k tokens."                        │
  │  Modern models: ~99%. Basically solved.                          │
  ├──────────────────────────────────────────────────────────────────┤
  │  MULTI-HOP OVER LONG CONTEXT                                     │
  │  "Combine facts from pages 3, 47 and 190 and draw a conclusion."  │
  │  Accuracy falls off sharply well before the advertised limit.     │
  └──────────────────────────────────────────────────────────────────┘

  performance vs position of the relevant fact — "lost in the middle":

   acc │██                                                      ██
       │███                                                    ███
       │████                                                  ████
       │ ████                                                ████
       │  ████████                                    ████████
       │      ███████████████████████████████████████████
       └────────────────────────────────────────────────────────────►
        start                  middle                          end
```

[Liu et al. (2023)](https://arxiv.org/abs/2307.03172) documented the U-shape: facts at the
beginning and end of a long context are recalled well, facts in the middle much worse — a
primacy/recency effect that plausibly comes from where the training data puts important
information.

Also degrading with length: **instruction adherence** (a system prompt 100k tokens back competes
with everything since), **distractor sensitivity** (more irrelevant text means more ways to be
misled), and **cost/latency**, which are linear in prefill and very much not free.

## Practical guidance

* Treat the advertised window as a *capacity*, not a *recommendation*. Quality and cost both
  favour the smallest context that contains what is needed.
* Put instructions at the beginning **and** repeat critical constraints at the end.
* Retrieval into a short context usually beats dumping a corpus into a long one — cheaper,
  faster, and often more accurate.
* Evaluate on your own multi-hop task, not on needle-in-a-haystack, which saturates and tells
  you nothing.

## What an interviewer digs into next

* At 128k context, is attention or the FFN the bigger FLOP cost? (Do the arithmetic.)
* Why does needle-in-a-haystack saturate while real long-context tasks do not?
* How does position interpolation trade local resolution for range?
* When is RAG strictly better than a long context, and when is it strictly worse?
