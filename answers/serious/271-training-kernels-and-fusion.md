---
id: "271"
slug: training-kernels-and-fusion
style: serious
category: optimization
difficulty: advanced
question: "A fine-tuning library claims 2x faster training and 70 percent less VRAM from custom kernels. Where does that actually come from?"
tags: [triton, fusion, lora, gradient-checkpointing, moe]
---

# Almost none of it is arithmetic. It is round trips to HBM that never happen.

LoRA already removed most of the FLOPs from fine-tuning. What is left in a step is a long tail of
elementwise work — RoPE, SwiGLU, normalisation, the optimiser update — each op of which reads a
big tensor out of HBM, does one multiply, and writes it back. Every one of those sits at an
arithmetic intensity near 1 ([268](268-roofline-decode-and-prefill.md)), so it runs at bandwidth.
**Fusing them is a bytes optimisation, and that is the entire trick.** Unsloth is the clearest
worked example because its kernels are readable; everything below I read from `unsloth/kernels/`
directly.

Configuration throughout: Llama-3.1-8B shape — 32 layers, hidden 4096, 32 query heads, 8 KV heads,
head_dim 128, intermediate 14336 — with 8,192 tokens in a step, BF16, on one H100 (3.35 TB/s).

## 1. Fused RoPE: one launch for Q and K, in place

`unsloth/kernels/rope_embedding.py` runs a single Triton kernel over Q **and** K, loads each
`cos`/`sin` row once for both, and `tl.store`s the rotated values back into the same pointers.

```
   the ordinary PyTorch path, per layer, forward
        rotate_half(q)       R 67.1 + W 67.1 MB
        q * cos              R 67.1 + W 67.1
        rotate * sin         R 67.1 + W 67.1
        add                  R 134.2 + W 67.1
                             ───────────────── ≈ 8 traversals of Q  =  537 MB
        the same for K                        ≈ 8 traversals        =  134 MB
                                                                       671 MB

   the fused kernel
        read Q, write Q, read K, write K      =  2 traversals       =  168 MB
                                                        ───────────────────────
   saved: 503 MB per layer forward × 32 layers × (fwd + bwd)  ≈  32 GB per step
          at 3.35 TB/s that is about 9.6 ms of every step, doing nothing
```

## 2. Fused SwiGLU backward: three loads, three stores, seven operations

`swiglu.py`'s `_DWf_DW_dfg_kernel` reads `DW`, `e` and `g`, computes `h`, `df` and `de`, and
stores all three **back into those same three buffers**. The naive version is seven elementwise
kernels each round-tripping a `[8192 × 14336]` tensor — 234.9 MB apiece.

```
   naive   sigmoid, se·e, f·g, DW·f, DW·g, and the de expression
           ≈ 13 reads + 6 writes  =  19 traversals × 234.9 MB  =  4.46 GB per layer
   fused   3 reads + 3 writes     =   6 traversals              =  1.41 GB per layer
           and zero new allocations — the outputs overwrite the inputs

   3.05 GB × 32 layers  ≈  97 GB per step, ≈ 29 ms at 3.35 TB/s
```

## 3. Do not save what you can recompute — the same move at two scales

**Small scale.** `fast_lora.py`'s `LoRA_MLP.forward` calls `ctx.save_for_backward(gateA, gateB,
upA, upB, downA, downB, X, e, g)`. Look at what is *not* there: `f` and `h`, the SwiGLU
intermediates. They are regenerated in the backward from `e` and `g` by the fused kernel above,
for free, because that kernel was going to touch those buffers anyway. Two `[8192 × 14336]`
tensors per layer at 234.9 MB — **15.0 GB across 32 layers** that is never held.

**Large scale.** Gradient checkpointing is the same bargain with the dial turned up: store
activations only at segment boundaries and re-run the forward inside the backward. With `L` layers
and a checkpoint every `√L` — about every 6 layers here — activation memory falls from `O(L)` to
`O(√L)` for one extra forward pass, roughly **+33% compute for a large multiple less memory**. It
is not free and it is not a kernel; it is the oldest compute-for-memory trade in the book, and it
is doing a large share of any "70% less VRAM" headline.

## 4. The LoRA gradient that is never materialised

The interesting line in `fast_lora.py` is the association order:

```
   d_downA.addmm_(h.t(), dY @ downB.t(), alpha=downS, beta=0)
   d_downB.addmm_(downA.t() @ h.t(), dY, alpha=downS, beta=0)
                  ▲
                  └── dY @ Bᵀ first: the intermediate is [tokens × r], never [K × N]

   the full down_proj weight gradient would be 14336 × 4096 = 58.7M elements
   the two LoRA gradients are  14336·16 + 16·4096 = 294,912 elements
                                                     ───────────────────
                                                     199× smaller
```

`beta=0` with a preallocated `torch.empty_like` means no allocation, and `dX` is written into the
saved `X`'s storage when `inplace=True`. Base weights stay quantised on the device: `fast_lora.py`
calls `fast_dequantize(upW.t(), upW_quant)`, uses it for exactly one matmul and then `del upW`.
The dequantised copy exists for microseconds. That is how 8B parameters live in 5–6 GB — dynamic
4-bit quantisation leaves selected tensors at higher precision — rather than 16.1 GB.

## 5. MoE: grouped GEMM, and why the loop is so bad

Hugging Face's `Qwen3MoeExperts.forward` still contains `for expert_idx in expert_hit:`, and
inside the loop, a gather, two `nn.functional.linear` calls, an activation, a scale and an
`index_add_`. Unsloth's `kernels/moe/README.md` says exactly what it replaces that with:
"eliminates the loop over experts by performing gemms as a grouped GEMM", with the permutation
into expert order fused into the **prologue** of the first GEMM and the unpermutation into the
**epilogue** of the second.

Take a 128-expert, top-8 layer with hidden 2048 and expert intermediate 768, at 1,024 tokens:

```
   8,192 (token, expert) assignments ÷ 128 experts  =  64 tokens per expert

   looped:   per expert, gate_up is [64 × 2048] @ [2048 × 1536]
             output tiles at 128×128  =  1 × 12  =  12 CTAs
             on 132 SMs that is 9.1% of the GPU — 128 times in a row
             ≈ 768 kernel launches per MoE block

   grouped:  all 128 groups in ONE kernel = 1,536 CTAs, ~12 full waves
```

And here is the part worth keeping. Weights are read once and used for every token routed to them,
so **the arithmetic intensity of a grouped MoE GEMM is exactly the average tokens per expert.**

```
   FLOPs  = 2 · P_expert · tokens_per_expert · E
   bytes  = 2 · P_expert · E                        (BF16 weights, read once)
   ratio  = tokens_per_expert                       exactly
```

At 1,024 tokens that is 64 — deep in the memory-bound region, where fusion wins enormously. At a
realistic training sequence of 8,192 it is 512, which is *above* the ridge point of 295, and the
same kernel wins far less. **Remember that the next time you read a MoE speedup number**
([272](272-reading-a-kernel-benchmark.md)).

## Where this stands, September 2026

The kernels above are primary — read from the repository. The **numbers in the marketing are
not**, and they are not all measuring the same thing. From Unsloth's own README: "2× faster with
70% less VRAM" for fine-tuning generally; "**New RoPE & MLP Triton Kernels & Padding Free +
Packing**: 3× faster training & 30% less VRAM" — note that this bundles a kernel change with a
*data* change, and removing padded tokens is not a kernel win; and "Train MoE LLMs 12× faster with
35% less VRAM", whose benchmark script in the repo compares against Hugging Face's
`Qwen3MoeSparseMoeBlock` at `seqlen 1024` on an H100. Every one of those is a ratio against a
specific unoptimised baseline at a specific shape.

What outlives all of it is the three mechanisms, none of which are library-specific: **fuse
elementwise chains because they are bandwidth-bound**, **recompute rather than store whenever the
recompute is cheaper than the traffic**, and **keep the association order that never materialises
a full-rank intermediate**. Those were true before Triton existed and will be true after it.

## What an interviewer digs into next

* Why does fusing RoPE help, when RoPE is a rounding error in the FLOP count?
* Which of the claimed VRAM saving is kernels and which is gradient checkpointing?
* What is the arithmetic intensity of a grouped MoE GEMM, and what does that imply about batch?
