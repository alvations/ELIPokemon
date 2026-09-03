---
id: "080"
slug: zero-and-fsdp
style: serious
category: systems
difficulty: advanced
question: "What is ZeRO/FSDP sharding and what are the stages?"
tags: [zero, fsdp, sharding, deepspeed, memory-optimisation]
---

# ZeRO and FSDP

Plain data parallelism replicates everything on every GPU: parameters, gradients, and optimizer
state. That replication is pure waste — every device holds an identical copy of data it only needs a
slice of at any moment.

**ZeRO** ([Rajbhandari et al., 2019](https://arxiv.org/abs/1910.02054)) shards those three, gathering
what is needed just in time. **FSDP** is PyTorch's native implementation of the same idea.

## The memory being attacked

For a model with `Ψ` parameters trained in mixed precision with Adam:

| Component | Bytes per parameter |
| --- | --- |
| BF16 parameters | 2 |
| BF16 gradients | 2 |
| FP32 master weights | 4 |
| Adam first moment (FP32) | 4 |
| Adam second moment (FP32) | 4 |
| **Total** | **16 Ψ** |

A 7B model needs ~112 GB before a single activation — which is why it does not fit on one 80 GB GPU,
despite the weights being only 14 GB. **Optimizer state, not weights, is the problem.**

## The stages

```
   N GPUs.  Per-GPU memory for the 16Ψ above:

   ┌──────────────────────────────────────────────────────────────┐
   │ BASELINE (DDP)   params ▓▓▓▓  grads ▓▓▓▓  optim ▓▓▓▓▓▓▓▓     │
   │                  every GPU holds ALL of it        = 16Ψ      │
   ├──────────────────────────────────────────────────────────────┤
   │ ZeRO-1  shard OPTIMIZER STATE                                │
   │   params ▓▓▓▓  grads ▓▓▓▓  optim ▓░░░       = 4Ψ + 12Ψ/N     │
   │   ✅ 4× saving, SAME communication as DDP. Free. Always on.  │
   ├──────────────────────────────────────────────────────────────┤
   │ ZeRO-2  + shard GRADIENTS                                    │
   │   params ▓▓▓▓  grads ▓░░░  optim ▓░░░       = 2Ψ + 14Ψ/N     │
   │   ✅ 8× saving, still ~same communication volume             │
   ├──────────────────────────────────────────────────────────────┤
   │ ZeRO-3  + shard PARAMETERS         (= FSDP)                  │
   │   params ▓░░░  grads ▓░░░  optim ▓░░░       = 16Ψ/N          │
   │   ✅ linear scaling — memory → 0 as N grows                  │
   │   ❌ ~1.5× communication: must all-gather params per layer   │
   └──────────────────────────────────────────────────────────────┘
```

**ZeRO-3 / FSDP mechanics:** before a layer's forward pass, all-gather its parameters from every
rank; compute; **immediately discard** the non-local shards. Repeat on the backward pass, then
reduce-scatter the gradients so each rank keeps only its slice. Peak memory holds one layer's full
parameters rather than the whole model.

The communication can be largely hidden: prefetch layer `i+1`'s parameters while computing layer `i`.
Done well, ZeRO-3 costs closer to 10–20% throughput than the naïve 50%.

**ZeRO-Offload / Infinity** push optimizer state (and optionally parameters) to CPU RAM or NVMe.
Enormous memory relief, large throughput cost — a last resort that turns "impossible" into "slow".

## ZeRO vs tensor parallelism

Both reduce per-GPU memory, but differently:

* **Tensor parallel** splits *the computation* of each layer; every step needs two all-reduces per
  layer. Must stay on a fast intra-node interconnect.
* **ZeRO-3** splits *the storage*; computation is replicated after gathering. Communication is
  gather/scatter, more tolerant of slower links.

They compose: tensor parallel inside a node, ZeRO across nodes.

## Practical notes

* **Start with ZeRO-1.** It is essentially free — same communication, 4× less memory — and there is
  no reason not to enable it.
* **Wrap at a sensible granularity** (per transformer block). Wrapping too finely means many small
  all-gathers; too coarsely means large memory spikes.
* **Combine with activation checkpointing** — they address different terms (question 078).
* **Mixed precision interacts**: keep FP32 master weights sharded, not replicated, or you lose much of
  the benefit.

## What an interviewer digs into next

* Why is ZeRO-1 free but ZeRO-3 not?
* Compute per-GPU memory for a 7B model with ZeRO-3 on 8 GPUs.
* When would you choose tensor parallelism over ZeRO-3?
* How is ZeRO-3's communication overlapped with compute?
