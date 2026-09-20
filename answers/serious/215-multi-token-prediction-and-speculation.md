---
id: "215"
slug: multi-token-prediction-and-speculation
style: serious
category: open-weights
difficulty: advanced
question: "Is multi-token prediction the same thing as speculative decoding?"
tags: [multi-token-prediction, speculative-decoding, training-objective, throughput, deepseek]
---

# No. One changes the model, the other changes the clock. DeepSeek ships one module as both.

Multi-token prediction is a **training objective**: at every position the model is asked to
predict the next token *and* the one after it, so gradients arrive from a denser signal and the
representation at position t has to carry information about t+2. Speculative decoding is a
**serving technique**: something cheap proposes several tokens, the real model verifies them in
one forward pass, and under the correct acceptance rule the output distribution is unchanged.
They are independent. DeepSeek-V3 makes them look like one thing because it reuses the MTP
module — trained for the first purpose — as the draft head for the second.

## Two different pictures

```
  TRAINING — the objective changes the weights
  ┌──────────────────────────────────────────────────────────────────────┐
  │  h_t ──► main head ─────────────► token t+1      loss_1              │
  │   │                                                                   │
  │   └────► MTP module (own transformer block, shares embedding &        │
  │          output head; conditioned on the TRUE t+1) ──► t+2  loss_2 ×λ │
  │                                                                       │
  │  DeepSeek-V3 uses depth 1 — two tokens total, predicted sequentially, │
  │  keeping the full causal chain. Not the parallel independent heads of │
  │  Gloeckle et al. The MTP module can be DISCARDED at inference and the │
  │  main model is unaffected.                                            │
  └──────────────────────────────────────────────────────────────────────┘

  INFERENCE — the technique changes throughput, not the weights
  ┌──────────────────────────────────────────────────────────────────────┐
  │  draft:  t+1, t+2  ──►  verify BOTH in one forward pass               │
  │                              │                                         │
  │              ┌───────────────┴───────────────┐                        │
  │              ▼                               ▼                        │
  │        accepted: keep both            rejected: keep t+1, discard      │
  │        → 2 tokens, 1 pass               → 1 token, 1 pass, wasted FLOPs│
  │                                                                        │
  │  Reported for V3: second token accepted 85–90% of the time → ~1.8× TPS │
  │  Correctness is NOT probabilistic. A rejected draft costs compute; it  │
  │  can never change the text you get out.                                │
  └──────────────────────────────────────────────────────────────────────┘
```

## Why the objective helps at all

Next-token prediction gives one supervision signal per position. Asking for t+2 as well gives
two, and more usefully it **penalises representations that only work one step out**. A model
that has committed to a token which makes the following token impossible pays for it
immediately rather than several steps later. [Gloeckle et al.](https://arxiv.org/abs/2404.19737)
report the gains concentrating in code and reasoning — domains where local choices have
non-local consequences — and growing with model size, which is why small-scale ablations of MTP
have historically looked unconvincing.

DeepSeek's variant differs from that paper in an important way: the MTP module is **sequential**,
a real transformer block that consumes the actual t+1 token before predicting t+2, rather than an
extra independent head hanging off the trunk. It therefore keeps the causal chain intact, which
is also what makes it usable as a draft model afterwards.

## Why they get confused, and what the confusion costs

The MTP module is dropped at inference, *or* kept and used to draft. That is a genuinely elegant
piece of engineering and it is also the source of the muddle. Two failure modes follow:

* **Reading a throughput number as a quality number.** "1.8× TPS from MTP" is a speculative
  decoding result. It says nothing about benchmark scores. The benchmark effect of the MTP
  objective is a separate, much smaller, much harder-to-attribute number.
* **Reading a quality number as a throughput number.** A lab that trains with MTP and does not
  ship a draft head gives you none of the speed.

## What the speedup actually depends on

1. **Batch size.** Speculative decoding pays when decode is memory-bandwidth-bound and the
   compute units are idle. At batch size 1 that is most of the time; at a large serving batch the
   GPU is already compute-bound and drafting spends FLOPs you needed. Vendor speedups are almost
   always quoted at low batch.
2. **Acceptance rate, which is workload-dependent.** 85–90% is reported across "various
   generation topics". On text unlike anything in pretraining — an unusual schema, a rare
   language, adversarial input — acceptance falls, and past roughly 50% the verification overhead
   eats the gain.
3. **Draft depth.** Depth 1 is conservative on purpose. Longer speculation multiplies the upside
   and multiplies the waste on rejection.
4. **The acceptance rule.** Greedy "accept if it matches argmax" is not the same algorithm as the
   [rejection-sampling scheme](https://arxiv.org/abs/2211.17192) that provably preserves the
   sampling distribution. If a serving stack is quietly doing the former at temperature > 0, its
   outputs are not the model's outputs. Ask.

## What an interviewer is listening for

That you separate objective from technique in the first sentence, and that you can say what each
one actually buys — denser supervision versus idle-silicon reclamation. Then the correctness
property: speculation is exact, not approximate, and a rejected draft costs only FLOPs. The
strongest answers volunteer the batch-size caveat, because it is the reason a published 1.8×
often becomes 1.1× on a busy production server.

## Where this stands, September 2026

V3's MTP design, the depth-1 configuration, the 85–90% acceptance rate and the 1.8× TPS figure
are from the V3 technical report. Coverage of the V4 series says its MTP configuration is
**unchanged from V3**, which is a secondary claim: arxiv.org, DeepSeek's documentation host and
Hugging Face are blocked by this environment's egress proxy, so the V4 report was not read
first-hand. The separation between a training objective and a serving technique is not a
DeepSeek fact at all and will still be true when all of these checkpoints are retired.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing** — the papers are named because the results are theirs, not because
they were re-read. Resolve every identifier before you cite it.
