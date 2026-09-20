---
id: "214"
slug: fine-grained-and-shared-experts
style: serious
category: open-weights
difficulty: advanced
question: "Why does DeepSeek use hundreds of small experts plus a shared one, and balance them without an auxiliary loss?"
tags: [mixture-of-experts, routing, load-balancing, deepseekmoe, deepseek]
---

# Narrow experts buy combinatorial specialisation. The shared one stops the duplication.

[DeepSeekMoE](https://arxiv.org/abs/2401.06066) makes two moves at once, and they only make
sense together. **Fine-grained segmentation**: split each FFN expert into several narrower ones
and activate proportionally more of them, holding parameters and FLOPs constant. **Shared expert
isolation**: carve off one expert that processes *every* token, so the knowledge every token
needs is learned once instead of redundantly inside all of the routed experts. DeepSeek-V3 runs
1 shared expert plus 256 routed, top-8 per token, in every layer but the first three, which stay
dense. Coverage of the V4 series reports 1 shared plus **384 routed with top-6**.

## Why narrow beats wide at fixed cost

```
   same parameters, same FLOPs per token, different granularity

   coarse    16 experts, top-2        distinct combinations = C(16,2)   =     120
   fine     256 experts, top-8        distinct combinations = C(256,8)  ≈ 4.1e14
                                                                          ▲
                        the router can express a far richer mixture ──────┘
                        without activating one extra parameter

   ┌─ routed path, one token ────────────────────────────────────────────┐
   │                                                                      │
   │   h ──► router ──► affinity s_i ──► s_i + b_i ──► top-6 selected     │
   │            │                            ▲              │             │
   │            │                            │              ▼             │
   │            │                 bias, TRAINING ONLY   gate uses s_i,    │
   │            │                 nudges WHO is picked   NOT s_i + b_i    │
   │            │                                            │            │
   │            └────────────────────────────────────────────┤            │
   │                                                          ▼            │
   │   h ──────────────► shared expert (every token, always) ─┴──► + ──► y │
   └──────────────────────────────────────────────────────────────────────┘

        overloaded expert  →  b_i decreases by γ  →  picked less next step
        idle expert        →  b_i increases by γ  →  picked more next step
```

The combinatorial argument is the honest reason for fine-graining. Cutting experts narrower and
taking more of them costs nothing at the FLOP level and multiplies the number of distinct expert
*mixtures* the router can express. Each expert then covers less ground, so it can specialise
harder, and less of what it knows is duplicated in its neighbours.

The shared expert exists because that duplication is otherwise unavoidable. Grammar, common
idioms, basic arithmetic — every token needs them, so without a shared path every routed expert
must carry its own copy, and you pay for the same knowledge 256 times. Isolating it frees the
routed experts to be *different* from each other, which is the only thing they are for.

## Why the load-balancing loss had to go

A router left alone collapses: a few experts win early, get more gradient, get better, get
picked more. The classical fix is an **auxiliary loss** penalising imbalance, added to the
language-modelling loss. It works, and it is also a second objective pulling against the first —
you are explicitly telling the model to sometimes route a token to an expert it believes is
worse. [Auxiliary-loss-free load balancing](https://arxiv.org/abs/2408.15664) removes the
gradient conflict by moving the correction out of the loss entirely:

* each expert gets a **bias term added to its affinity score for top-k selection only**;
* the **gating weight** that scales the expert's output is computed from the *unbiased* score;
* after each step, the bias goes down by γ for over-used experts and up by γ for under-used ones.

So the bias changes *who gets chosen* and never changes *how much a chosen expert counts*. It is
a control loop, not a loss term, and it contributes no gradient to the model at all. DeepSeek-V3
keeps a very small sequence-wise balance loss on top, to stop a single sequence degenerating;
reported descriptions of V4 keep the same arrangement, with the affinity function changed from
sigmoid to √softplus and the first few layers using deterministic hash routing.

## What it costs you

* **All-to-all traffic scales with the number of activated experts**, not their size. Top-8 of
  256 means eight destinations per token per layer. Expert parallelism turns that into network
  time, and the interconnect becomes the latency floor.
* **Smaller matmuls, worse arithmetic intensity.** Narrow experts mean narrow GEMMs and lower
  hardware utilisation unless your kernels group tokens per expert well.
* **Balanced in training is not balanced in production.** The bias controller is a training-time
  mechanism. On a skewed traffic mix — all code, or all one language — your served routing can be
  lopsided in a way the pretraining logs never showed, and the hottest expert's GPU becomes
  everyone's clock.
* **Rare experts are fragile.** They see the least data, so they quantise worst, and they are the
  ones handling your unusual inputs (question 207).

## What an interviewer is listening for

The combinatorics, said out loud: more, narrower experts multiply the expressible mixtures at
constant FLOPs. Then that the shared expert is a *deduplication* argument, not a capacity one.
On balancing, the sentence that matters is "the bias affects selection, not the gating weight" —
if you can say why that distinction is the whole point, you have understood it. The strongest
answers raise serving-time imbalance unprompted, because that is the part the papers do not
measure for you.

## Where this stands, September 2026

The DeepSeekMoE and auxiliary-loss-free papers, and V3's 1-plus-256 top-8 configuration, are
from primary sources and are stable. The V4 configuration — 384 routed, top-6, √softplus
affinity, hash routing in the early layers — is **from secondary coverage only**: arxiv.org,
DeepSeek's documentation host and Hugging Face are all blocked by this environment's egress
proxy, so the V4 report and its model cards could not be read first-hand. Expert counts are also
exactly the sort of number that gets garbled in re-reporting, so confirm them against the config
JSON in the model repository before you build anything on them.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing** — the papers are named because the results are theirs, not because
they were re-read. Resolve every identifier before you cite it.
