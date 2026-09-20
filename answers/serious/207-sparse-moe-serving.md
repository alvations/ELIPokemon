---
id: "207"
slug: sparse-moe-serving
style: serious
category: frontier
difficulty: advanced
question: "An open model advertises 250B total parameters with 15B active. What does that buy you when you go to serve it?"
tags: [mixture-of-experts, serving, memory, routing, quantisation]
---

# Active parameters buy FLOPs. Total parameters still cost memory.

Upstage's Solar Open 2, released openly in 2026, is the cleanest example to reason about: a
mixture-of-experts model reported at **250B total parameters with about 15B activated per
token**, a context window up to 1M, and a claim that it runs on **two NVIDIA H200s**. The same
lab's earlier SOLAR 10.7B was built by depth up-scaling — duplicating and re-stacking the layers
of a 7B and continuing pretraining — so the house style is getting more capacity out of a fixed
budget.

The single sentence that matters: **the router decides how much compute you spend, and nothing
decides how much memory you spend.** Every one of the 250B weights must be somewhere the GPU can
reach, because any token might route to any expert.

## Why the two-H200 figure is exactly the arithmetic you should do

```
   250B parameters
      × 1 byte/param (FP8)            = 250 GB of weights
      × 2 bytes/param (BF16)          = 500 GB of weights

   H200 ≈ 141 GB HBM each
      2 × H200                        = 282 GB   ◄── fits FP8, with ~32 GB
                                                     left for everything else
      4 × H200                        = 564 GB   ◄── what BF16 needs

   ┌─────────────── what the 32 GB has to cover ────────────────┐
   │  KV cache  │  activations  │  fragmentation  │  headroom   │
   └─────────────────────────────────────────────────────────────┘
        ▲
        └ a 1M-token context is not free here. "Runs on two H200s"
          and "serves 1M context at useful batch size" are different
          claims and should be tested separately.

   Compute per token ∝ 15B.   Memory ∝ 250B.   These do not move together.
```

So the honest framing of a 250B-A15B model is: **the inference cost of a 15B model and the
hardware footprint of a 250B one**. That is an excellent trade if you are GPU-rich and a
non-trade if you are not — which is why an MoE gives a consumer card nothing. A widely repeated
community result on Gemma 4's 26B-A4B checkpoint has it running at roughly 11 tokens/second on an
RTX 4090, *slower* than a comparable dense 4B: the routing overhead is real, and with only ~4B
active there is not enough compute saving to pay for it at batch size one.

## The four serving problems nobody mentions in the announcement

1. **Batching gets worse, not better.** Tokens in a batch scatter across different experts, so a
   batch no longer maps to one dense matmul. Throughput depends on how well your server groups
   tokens by expert, and a bad grouping erases the FLOP advantage.
2. **Expert parallelism means network traffic.** Split experts across GPUs and every token's
   routing decision becomes an all-to-all. That is a latency floor set by your interconnect, not
   by your model.
3. **Load imbalance.** Routers collapse toward popular experts unless trained against it, and a
   hot expert is a straggler that every other GPU waits on.
4. **Quantisation is not uniform across experts.** Rarely-activated experts have less calibration
   data, so aggressive post-training quantisation degrades them first — and they are exactly the
   ones serving your unusual inputs.

## What an interviewer is listening for

That you separate the two parameter counts and attach each to the right resource. Then the
arithmetic above, done out loud — parameters times bytes per parameter against HBM per card is a
thirty-second calculation that decides whether a deployment is possible at all. The strongest
answers add that a vendor's "runs on N GPUs" number is almost always weights-only at low
precision, short context and batch size one, and say what they would measure instead:
tokens/second at the batch size and context length they actually need.

## Where this stands, September 2026

The Solar Open 2 figures above are as reported in coverage of the release; the model card is the
authority and should be read directly before anyone provisions hardware. The reasoning — active
for compute, total for memory — is architecture-level and outlives any particular checkpoint.
