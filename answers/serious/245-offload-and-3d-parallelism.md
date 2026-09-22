---
id: "245"
slug: offload-and-3d-parallelism
style: serious
category: open-weights
difficulty: advanced
question: "ZeRO-Offload moves optimizer state to CPU and ZeRO-Infinity to NVMe. When does that pay, and when is 3D parallelism the better answer?"
tags: [zero-offload, nvme, 3d-parallelism, pipeline, deepspeed]
---

# Offload buys capacity you do not have. Parallelism buys use of capacity you do.

Offloading turns an out-of-memory error into a slow job. That is a genuinely good trade when the
alternative is no job at all, and a bad one the moment you had the hardware to do it properly.
The decision is arithmetic, not taste: **compare the bytes you must move per step against the
work the GPU has to do in that step.** If the transfer hides inside the compute, offload is free.
If it does not, you have bought capacity with throughput at a rate you should quote out loud
before you enable it.

## The tiers, and what each one actually is

```
   ┌─────────────┬──────────────────┬───────────────────────────────────────────┐
   │ tier        │ rough bandwidth  │ what DeepSpeed puts there                 │
   ├─────────────┼──────────────────┼───────────────────────────────────────────┤
   │ HBM (GPU)   │ ~1–3 TB/s        │ params, activations, the live shard       │
   │ host DRAM   │ ~200–500 GB/s    │ ZeRO-Offload: optimizer state AND the     │
   │  via PCIe   │  link ~25 GB/s   │   optimizer STEP itself (DeepSpeedCPUAdam)│
   │ NVMe        │ ~3–7 GB/s/drive  │ ZeRO-Infinity: optimizer state, params    │
   │             │                  │   `nvme_path`, `buffer_count`, `ratio`    │
   └─────────────┴──────────────────┴───────────────────────────────────────────┘

   Note the second row carefully. ZeRO-Offload does not merely park bytes on the
   host; it MOVES THE ADAM UPDATE to the CPU, which is why DeepSpeed ships its own
   DeepSpeedCPUAdam (documented as 5–7× the throughput of PyTorch's CPU Adam).
   Otherwise the optimizer step becomes the whole step.
```

ZeRO-Offload is available from stage 1 up and its documented headline is a **10B GPT-2 trained
on one 32 GB V100**, with up to 13B on a single GPU. ZeRO-Infinity is the stage-3 successor: it
adds NVMe, `deepspeed.zero.Init(remote_device="nvme")` so a model larger than host memory can be
*constructed*, and memory-centric tiling (`deepspeed.zero.TiledLinear`) to cut the working set of
one huge layer.

## The arithmetic you should do before enabling it

13B model, 8 ranks, ZeRO-2 plus optimizer offload. Each rank owns `13e9/8 = 1.625e9` parameters'
worth of optimizer state.

```
   PER RANK, PER STEP, ACROSS PCIe
     gradients down to host   1.625e9 × 2 B = 3.25 GB
     updated params back up   1.625e9 × 2 B = 3.25 GB
                                     total   6.50 GB
     at ~25 GB/s achieved                  ≈ 0.26 s   ← and eight ranks share
                                                        the host's root complexes

   PER RANK, PER STEP, INSIDE THE HOST
     Adam must stream its state: 16 B/param × 1.625e9 ≈ 26 GB of DRAM traffic
     × 8 ranks                                        ≈ 208 GB per node per step
     at ~400 GB/s of host memory bandwidth            ≥ 0.5 s, as a FLOOR

   VERDICT
     GPU step was 3.0 s  →  you lose ~20–30%.        Take the deal.
     GPU step was 0.3 s  →  you lose 3×.             Do not take the deal.
```

The lever that makes offload work is therefore **longer steps**: bigger micro-batches, longer
sequences, more gradient accumulation. Offload and gradient accumulation are the same trick
pointed at different resources, and they compose.

NVMe changes the numbers by an order of magnitude the wrong way. 12 B/param × 13e9 = **156 GB**
of optimizer state; one drive at 5 GB/s streams that in ~31 s. ZeRO-Infinity is therefore built
around `ratio` (what fraction of the state goes to NVMe rather than DRAM), `buffer_count`, and
striping across drives — and it is for the case where the honest alternative is "cannot train
this at all".

**One operational trap, straight from the config docs:** `pin_memory` now defaults to `true` for
both `offload_param` and `offload_optimizer`, where it used to default to `false`. On a host
with a low `ulimit -l` that turns into an out-of-memory on upgrade, with nothing in your diff to
explain it. Pinned memory is what makes the DMA fast; it is also not swappable.

## When 3D parallelism is the right answer instead

3D parallelism splits the *work*, not the storage, along three orthogonal axes:

```
   ┌ data ────────────┐  N replicas on different batches. ZeRO lives here.
   │                  │  Communication: gradients, once per step.
   ├ pipeline ────────┤  Layers split into p stages. Only activations cross
   │                  │  stage boundaries — the CHEAPEST axis by volume.
   │                  │  Cost: the bubble.  bubble = (p−1)/(m+p−1)
   │                  │     p=4, m=1  micro-batch  → 75% of the time idle
   │                  │     p=4, m=12 micro-batches → 20% idle
   ├ tensor ──────────┤  One matmul split across ranks. All-reduce INSIDE
   │                  │  every layer — the most communication of the three.
   └──────────────────┘  Keep it inside one node, on NVLink. Never across nodes.

   DeepSpeed-Ulysses adds sequence parallelism as a fourth axis, for when the
   sequence itself, not the weights, is what does not fit.
```

The rule of thumb that survives contact: **tensor parallel within a node, pipeline across nodes,
data parallel on top, ZeRO to mop up whatever optimizer state remains.** And the choice against
offload is simply: do you have the GPUs? 3D parallelism converts idle GPUs into capacity.
Offload converts a shortage of GPUs into time. If you have 64 GPUs and a model that will not fit
on 8, you have a parallelism problem. If you have one GPU and a deadline, you have an offload
problem.

## What an interviewer digs into next

* Your step time went up 40% after enabling offload. Which counter tells you whether it is PCIe
  or host DRAM?
* Why does pipeline parallelism's bubble shrink with micro-batches but not with more stages?
* What breaks when you put tensor parallelism across an InfiniBand hop?
* ZeRO-3 plus pipeline parallelism: which of the two owns the parameters, and what does that do
  to the all-gather?
* Coherent CPU–GPU links on superchip-class hardware change the first table. Which line, and by
  how much?

## Where this stands, September 2026

The DeepSpeed specifics are **primary**, from a clone of `deepspeedai/DeepSpeed` at commit
`1eb56d2`: `docs/_tutorials/zero-offload.md` (the 10B-on-one-V100 result, the 5–7× CPU Adam
claim), `docs/_tutorials/zero.md` (ZeRO-Infinity, tiling, `zero.Init`),
`docs/_pages/config-json.md` (`nvme_path`, `ratio`, `buffer_count`, and the `pin_memory` default
change) and `docs/_tutorials/pipeline.md`. The tree is at **0.19.8**, PyPI at **0.19.7**. The
bandwidth figures are order-of-magnitude and hardware-dependent; the worked step arithmetic is
mine, not a benchmark. The project's own news page lists ZenFlow and SuperOffload as the current
work on hiding exactly these stalls — read those before assuming the numbers above are the
ceiling. The tier ladder and the compare-bytes-to-compute rule outlast any of it.
