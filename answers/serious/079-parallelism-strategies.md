---
id: "079"
slug: parallelism-strategies
style: serious
category: systems
difficulty: advanced
question: "Explain data, tensor, pipeline, and expert parallelism."
tags: [data-parallel, tensor-parallel, pipeline-parallel, 3d-parallelism, megatron]
---

# Parallelism strategies

Four ways to split a training job across devices. They are composable, and large runs use several at
once ("3D parallelism").

```
 ┌─ DATA PARALLEL ────────────────────────────────────────────────────┐
 │  Every GPU: full model copy, different data shard.                 │
 │  Sync: all-reduce gradients each step.                             │
 │  ✅ simple, scales far   ❌ model must fit on one GPU               │
 │  GPU0 [MODEL] ← batch 0-7      GPU1 [MODEL] ← batch 8-15           │
 │            └──── all-reduce gradients ────┘                        │
 ├─ TENSOR PARALLEL (intra-layer) ────────────────────────────────────┤
 │  Split individual matrices across GPUs.                            │
 │  Attention: heads split across GPUs. FFN: W₁ column-split,         │
 │  W₂ row-split, so only ONE all-reduce per block.                   │
 │  ✅ shrinks per-GPU memory and per-layer latency                    │
 │  ❌ 2 all-reduces per layer → needs NVLink; keep WITHIN a node      │
 │  GPU0 [heads 0-15][W₁ cols 0-k]   GPU1 [heads 16-31][W₁ cols k-n]  │
 ├─ PIPELINE PARALLEL (inter-layer) ──────────────────────────────────┤
 │  Split by LAYER across GPUs; activations flow between stages.      │
 │  GPU0 [layers 0-19] → GPU1 [layers 20-39] → GPU2 [40-59]           │
 │  ✅ low communication (only stage boundaries) → works across nodes  │
 │  ❌ the BUBBLE: idle time while the pipeline fills and drains       │
 ├─ EXPERT PARALLEL (MoE only) ───────────────────────────────────────┤
 │  Different experts on different GPUs; tokens all-to-all routed.    │
 │  ✅ the only way to fit very large MoE models                       │
 │  ❌ all-to-all is bandwidth-hungry and load-imbalance-sensitive     │
 └────────────────────────────────────────────────────────────────────┘
```

## The pipeline bubble

The defining cost of pipeline parallelism:

```
   naïve, 4 stages:                    with 4 micro-batches:
   GPU0 ████░░░░░░░░                   GPU0 ████████░░░░
   GPU1 ░░░░████░░░░                   GPU1 ░░████████░░
   GPU2 ░░░░░░░░████                   GPU2 ░░░░████████
   GPU3 ░░░░░░░░░░░░████               GPU3 ░░░░░░████████
        ░ = idle. 75% wasted.               bubble ≈ (p-1)/(m+p-1)
```

Splitting the batch into `m` micro-batches shrinks the bubble to roughly `(p−1)/(m+p−1)`. GPipe
processes all forward then all backward; **1F1B** interleaves them, which reduces peak activation
memory substantially and is what modern frameworks use.

## Composing them

The standard recipe for a large run:

* **Tensor parallel within a node** (8 GPUs on NVLink) — highest communication, needs the fastest
  interconnect.
* **Pipeline parallel across nodes** — lowest communication per unit of work.
* **Data parallel across replicas of the whole thing** — outermost.
* **ZeRO/FSDP sharding** layered on data parallelism to cut redundant optimizer state (question 080).
* **Sequence/context parallel** for very long sequences, splitting the sequence dimension.

The organising principle is: **match the communication intensity of each strategy to the bandwidth of
the level it runs at.** Getting this backwards — tensor parallelism across a slow network — is the
classic way to build a cluster that scales badly.

## What an interviewer digs into next

* Why does Megatron split `W₁` by column and `W₂` by row?
* Compute the pipeline bubble for 8 stages and 32 micro-batches.
* Why must tensor parallelism stay within a node?
* Which strategy would you add first when a model stops fitting?
