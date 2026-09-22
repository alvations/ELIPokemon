---
id: "244"
slug: zero-stages-and-memory-arithmetic
style: serious
category: open-weights
difficulty: advanced
question: "Walk me through DeepSpeed's ZeRO stages 1, 2 and 3 with real memory arithmetic. What does each one shard?"
tags: [zero, deepspeed, distributed-training, memory, data-parallelism]
---

# Each stage deletes one kind of redundant copy. Stage 3 also deletes your access to a weight.

Plain data parallelism keeps a **complete** set of training state on every rank: parameters,
gradients and optimizer state, all identical, all N times over. ZeRO — the Zero Redundancy
Optimizer, [Rajbhandari et al.](https://arxiv.org/abs/1910.02054) — observes that at any instant
each rank only *needs* its own slice, and partitions the state across the data-parallel group in
three cumulative stages. Stage 1 partitions optimizer state. Stage 2 adds gradients. Stage 3 adds
the parameters themselves. The memory falls roughly as `1/N`; the communication rises, and at
stage 3 the programming model changes underneath you.

## The arithmetic, on a model you can picture

Take a **13B dense model**, hidden size 5120, 40 layers, 128K vocabulary, trained in bf16 with
Adam on **8 GPUs of 80 GB**. Per parameter, mixed-precision Adam costs:

```
   2 B   bf16 parameter          ┐
   2 B   bf16 gradient           ┘ needed on the critical path
   4 B   fp32 master weight      ┐
   4 B   Adam momentum (fp32)    │ only touched inside optimizer.step()
   4 B   Adam variance  (fp32)   ┘
  ────
  16 B   per parameter
```

```
   Ψ = 13e9 parameters, N = 8 ranks.        per-GPU model-state memory

   DDP        2Ψ  +  2Ψ  +  12Ψ            = 208.00 GB   ████████████████  OOM
   ZeRO-1     2Ψ  +  2Ψ  +  12Ψ/N          =  71.50 GB   █████▌            fits, barely
   ZeRO-2     2Ψ  +  (2+12)Ψ/N             =  48.75 GB   ███▊
   ZeRO-3     (2+2+12)Ψ/N                  =  26.00 GB   ██
              │      │        │
              │      │        └ optimizer state: sharded from stage 1 on
              │      └ gradients: sharded from stage 2 on
              └ parameters: replicated until stage 3

   ZeRO-1:  4×13 = 52.00  +  12×13/8 = 19.50   →  71.50 GB
   ZeRO-2:  2×13 = 26.00  +  14×13/8 = 22.75   →  48.75 GB
   ZeRO-3:                  16×13/8  = 26.00   →  26.00 GB
```

Read the middle column rather than the total. Stage 1 alone takes 208 GB to 71.5 and that is the
difference between "will not start" and "starts". Stage 2 buys another 23 GB. Stage 3 buys 23
more *and* makes the number scale with N, which stages 1 and 2 do not: at N = 64, stage 2 is
still stuck above the 26 GB of replicated parameters while stage 3 is down near 3 GB.

## Do not trust that table; run the estimator

DeepSpeed ships its own memory estimators, and they do not agree with the textbook count. From
`deepspeed/runtime/zero/stage_1_and_2.py`, verbatim:

```
   # GPU's total_params multipliers: 2 = params_16bit,
   # 18 = 2_grads_16bit + 4_grads_32bit + 4_params_32bit + 8_optimizer_states_32bit
   gpu_mem = 2 * total_params + int(18 * total_params / total_gpus)
```

Eighteen, not fourteen — because the implementation also keeps an **fp32 gradient** buffer that
the tidy 16-byte story leaves out. For our case that is `26.00 + 18×13/8 = 55.25 GB`, not 48.75.
The stage-3 estimator is `4 × largest_layer_params + 18Ψ/N`: the second term is the shard, the
first is the transient buffer for the largest single parameter tensor you must **gather whole**.
With a 128K × 5120 embedding, that is 0.66B params × 4 B ≈ 2.6 GB of headroom you have to leave
free, giving ≈ 31.9 GB. Nobody in an interview is going to hold you to 18 against 16. Knowing
that the gap exists, and that there is a function in the library that answers it, is the point.

## What none of this covers: activations

ZeRO shards **model states**. Activation memory is untouched and is frequently the larger number:

```
   activations ≈ batch × seq_len × hidden × layers × (bytes) × (a factor for
                 how many tensors the backward pass needs kept alive)

   13B, batch 4, seq 8192, hidden 5120, 40 layers, bf16, no checkpointing:
       4 × 8192 × 5120 × 40 × 2 B ≈ 13.4 GB for ONE saved tensor per layer;
       a real block saves several, so the true figure is multiples of that.

   Fixes are orthogonal to ZeRO: activation checkpointing (recompute instead
   of store), sequence parallelism (DeepSpeed-Ulysses), activation offload.
```

A candidate who quotes 26 GB for ZeRO-3 and then cannot say why the job still OOMs has learned
the table and not the system.

## What each stage costs

**Communication.** DDP does one all-reduce of gradients: `2Ψ` of traffic. ZeRO-1 and ZeRO-2
replace it with reduce-scatter plus all-gather — the same `2Ψ`, rearranged. **ZeRO-3 adds an
all-gather of parameters in the forward pass and again in the backward pass**, taking the total
to roughly `3Ψ`, about **1.5× DDP**. That is the real price of stage 3, and it is why
[ZeRO++](https://www.deepspeed.ai/) exists — quantised weights, hierarchical partitioning and
quantised gradients, reported as a 4× communication reduction.

**The programming model.** Under stage 3 a parameter is not resident. Reading `p.data` outside a
forward pass gives you a slice, or nothing. You construct huge models inside
`deepspeed.zero.Init(...)` so they are partitioned as they are allocated rather than after, and
you wrap any direct access in `deepspeed.zero.GatheredParameters(...)` with a `modifier_rank`.
Every custom initialiser, weight-tying trick and `state_dict` hack in your codebase meets this.

**Precision knobs interact.** DeepSpeed's config documents `bf16_optimizer_states`: keeping the
master weights and both Adam moments in bf16 brings the offloaded state to **~6 bytes/param**
against **~10** with fp32 moments. That is a bigger lever than a stage bump and it is a
convergence risk, not a free win.

## Choosing

Stage 2 if the parameters fit and you want the cheapest correct thing. Stage 3 when `2Ψ` alone
does not fit, when you want per-GPU memory to keep falling as you add ranks, or when you need
the headroom for a longer sequence. Do not start at stage 3 out of ambition: you are paying 1.5×
communication and a debugging tax for memory you may not need.

## What an interviewer digs into next

* Why is stage 2's per-GPU memory floored at `2Ψ` no matter how many ranks you add?
* Where does the fp32 master weight actually live under stage 2 with CPU offload?
* You enabled stage 3 and throughput halved. What do you measure first?
* Why does gradient accumulation change ZeRO-2's communication pattern but not its memory?
* Which of ZeRO's savings survive if you swap Adam for a stateless optimizer?

## Where this stands, September 2026

The ZeRO stage semantics, the estimator constants, the `18` comment and the
`bf16_optimizer_states` byte counts are **primary**: read from a clone of
`deepspeedai/DeepSpeed` at commit `1eb56d2`
(`deepspeed/runtime/zero/stage_1_and_2.py`, `stage3.py`, `docs/_tutorials/zero.md`,
`docs/_pages/config-json.md`). The version in the tree is **0.19.8**, the latest on PyPI
**0.19.7**. The 13B worked example is mine and the activation figure is an order-of-magnitude
sketch, not a measurement. Byte counts move with optimizer and precision fashions; `1/N` does not.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing**. Resolve every identifier before you cite it.
