---
id: "010"
slug: flash-attention
style: serious
category: systems
difficulty: advanced
question: "What is FlashAttention and why is it faster without changing the math?"
tags: [flashattention, io-aware, tiling, online-softmax, hbm-sram]
---

# FlashAttention

FlashAttention ([Dao et al., 2022](https://arxiv.org/abs/2205.14135)) computes **exactly** the
same attention as the naïve implementation — same outputs, bit-for-bit-ish, no approximation —
and is 2–4× faster and uses `O(n)` memory instead of `O(n²)`. The win is entirely in **memory
movement**, which is the thing naïve implementations were quietly wasting.

## The problem: attention is memory-bound, not compute-bound

A GPU has a steep memory hierarchy:

```
   ┌────────────────────────────────────────────────────┐
   │  SRAM / shared memory   ~20 MB    ~19 TB/s         │  ← tiny, blazing
   ├────────────────────────────────────────────────────┤
   │  HBM (the "GPU RAM")    40–80 GB  ~2 TB/s          │  ← big, 10× slower
   └────────────────────────────────────────────────────┘
```

Naïve attention does this:

```
   Q,K ──HBM──► compute S = QKᵀ ──write S to HBM──►  (n × n !)
   S   ──read from HBM──► softmax ──write P to HBM──► (n × n !)
   P,V ──read from HBM──► compute PV ──write O──►

   For n = 8192: each n×n matrix is 128 MB in FP16, per head, per layer.
   You materialise it, write it out, read it back — three times.
```

The matrix multiplies are fast. The round trips to HBM are not. At long sequence lengths, the
kernel spends most of its time waiting on memory, and the `n × n` matrix is also what makes
attention's *memory* quadratic.

## The fix: tile and never materialise

FlashAttention splits Q, K, V into blocks that fit in SRAM and fuses the whole operation into
one kernel:

```
   for each block of Q  (outer loop, stays in SRAM):
       initialise  O_i = 0,  ℓ_i = 0,  m_i = -∞
       for each block of K,V  (inner loop, streamed in):
           S_ij = Q_i K_jᵀ                 ← in SRAM
           m_new = max(m_i, rowmax(S_ij))  ← running max
           P_ij = exp(S_ij - m_new)
           ℓ_i  = ℓ_i · exp(m_i - m_new) + rowsum(P_ij)   ← rescale old, add new
           O_i  = O_i · exp(m_i - m_new) + P_ij V_j       ← rescale old, add new
           m_i  = m_new
       write O_i / ℓ_i to HBM               ← ONE write, size n × d
```

The trick that makes it exact is **online softmax**: you cannot normalise until you have seen
every score, but you *can* keep a running max and running denominator and retroactively rescale
the partial output by `exp(m_old − m_new)` whenever the max changes. Algebraically identical to
computing softmax over the whole row.

Memory traffic drops from `O(n²)` to `O(n²d / M)` where `M` is SRAM size — asymptotically the
same FLOPs, an order of magnitude fewer bytes moved. Peak memory becomes `O(n)`, which is what
actually unlocked long-context training.

For the backward pass, storing the `n × n` probabilities would defeat the purpose, so it
**recomputes** them from the stored `m` and `ℓ` statistics. More FLOPs, far less memory traffic,
still a large net win — a nice illustration that on modern hardware, recompute can be cheaper
than remembering.

## The lineage

* **FlashAttention-2** (2023) — better work partitioning across warps, fewer non-matmul ops
  (which run on the far slower non-tensor-core path), ~2× again.
* **FlashAttention-3** (2024) — Hopper-specific: asynchrony via TMA/WGMMA, FP8 support.
* **PagedAttention** — a different problem (cache *allocation*), often confused with this one.

## The general lesson

This is the canonical example of an **IO-aware algorithm**. The right cost model for a GPU
kernel is usually bytes moved, not FLOPs. If an interviewer asks you to speed something up, the
first question is which side of the roofline you are on.

## What an interviewer digs into next

* Why is FlashAttention exact when other efficient-attention methods approximate?
* Explain online softmax and why the rescaling factor is `exp(m_old − m_new)`.
* Why recompute in the backward pass instead of storing?
* Does FlashAttention help decode (one query token) as much as prefill? (No — why?)
