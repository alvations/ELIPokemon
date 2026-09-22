---
id: "269"
slug: flashattention-to-flashinfer
style: serious
category: optimization
difficulty: advanced
question: "FlashAttention already fuses attention into one kernel. What does a serving kernel library like FlashInfer have to do that a single fused kernel does not?"
tags: [flashattention, flashinfer, kernels, paged-attention, jit]
---

# One kernel solved one shape. A server never sees the same shape twice.

FlashAttention is a claim about **memory traffic**, not about mathematics: tile the computation so
the N×N score matrix is never written to HBM, and you get the *exact* same output for a fraction
of the bytes. That is a complete answer for training and for a single fixed-shape forward pass. A
serving kernel library — FlashInfer, which vLLM, SGLang, TensorRT-LLM and TGI all call into — has
a different job: **every call has a different batch, a different set of sequence lengths and a
different scatter of KV pages, and the kernel has to be fast anyway.**

## What FlashAttention actually saves, in bytes

Take the prefill from [268](268-roofline-decode-and-prefill.md): 8192 tokens, 64 query heads,
80 layers, BF16. Materialising `QKᵀ` costs

```
   8192 × 8192 × 64 heads × 2 bytes  =  8.59 GB   per layer
   written once, read for softmax, written, read for AV   ≈ 25.8 GB of HBM traffic
   × 80 layers                                            ≈ 2.06 TB

   against 143.8 GB for the entire prefill with the matrix never materialised.
```

Roughly **15× the memory traffic of the whole forward pass**, to store a quantity that is
discarded immediately. That is enough to drag prefill — which sits 29× above the ridge point —
down under it. FlashAttention's answer is to walk K and V in tiles and carry an **online
softmax**: a running row max `m` and a running denominator `l`, rescaled whenever a tile raises
the max.

```
   for each tile of K,V loaded into SRAM:
        s      = Q · Kᵀ(tile)              ← never leaves SRAM
        m_new  = max(m, rowmax(s))
        scale  = exp(m - m_new)
        l      = l · scale + rowsum(exp(s - m_new))
        O      = O · scale + exp(s - m_new) · V(tile)
        m      = m_new
                 ▲                ▲
                 │                └─ the accumulator is O(d) per row, not O(N)
                 └─ the rescale is why this is exact and not an approximation
```

[FlashAttention](https://arxiv.org/abs/2205.14135) (Dao et al., 2022),
[FlashAttention-2](https://tridao.me/publications/flash2/flash2.pdf) (better work partitioning),
and FlashAttention-3 for Hopper. All three produce reference-equivalent output up to
floating-point reassociation — which matters later, and in
[272](272-reading-a-kernel-benchmark.md).

## What a serving library adds on top

### 1. Ragged batches, and the arithmetic of not padding

This is FlashInfer's own decode example, from the docstring of
`BatchDecodeWithPagedKVCacheWrapper` in `flashinfer/decode.py` — seven requests, page size 16:

```
   kv_page_indptr    = [0, 17, 29, 44, 48, 66, 100, 128]     pages per request
   kv_last_page_len  = [1,  7, 14,  4,  3,  1,  16]          fill of the final page

   req   pages   real tokens                   slots taken
   ──────────────────────────────────────────────────────────
    0      17    16·16 +  1 =  257                 272
    1      12    11·16 +  7 =  183                 192
    2      15    14·16 + 14 =  238                 240
    3       4     3·16 +  4 =   52                  64
    4      18    17·16 +  3 =  275                 288
    5      34    33·16 +  1 =  529                 544
    6      28    27·16 + 16 =  448                 448
   ──────────────────────────────────────────────────────────
              128 pages   1,982 tokens         2,048 slots     →  3.2% wasted

   the same batch as a dense padded tensor [7, 529]:  3,703 slots  →  46.5% wasted
   the same batch pre-reserved at max_model_len 8192: 57,344 slots →  96.5% wasted
```

A single fused kernel takes a rectangular tensor. A server never has one. **Every remaining
feature in the list below exists because of that table.**

### 2. Paged and block-sparse are the same data structure

FlashInfer's `BlockSparseAttentionWrapper` (`flashinfer/sparse.py`) takes `indptr` and `indices`
in BSR layout — block compressed sparse row, the identical index structure the paged KV cache
uses. That is the library's central design claim, and you can read it off the two APIs: a **paged
KV cache is a block-sparse attention mask with block size (1, page_size)**. One kernel template
therefore serves paged decode, prefix-shared cascade attention, sliding-window attention and
learned block-sparse patterns, because they differ only in what is in `indices`.

### 3. Specialisation by compile-time trait, and here the common description is wrong

FlashInfer is usually described as compiling per *shape*, with batch size and page size in the
cache key. It does not. From `flashinfer/jit/attention/modules.py`, the decode module's cache key
is exactly:

```
   batch_decode_with_kv_cache_dtype_q_{…}_dtype_kv_{…}_dtype_o_{…}_dtype_idx_{…}
                                _head_dim_qk_{…}_head_dim_vo_{…}
                                _posenc_{…}_use_swa_{…}_use_logits_cap_{…}
```

Dtypes, head dims, positional-encoding mode, sliding window, logit soft cap — **compile-time
traits**. No batch size, no page size, no sequence length. Prefill adds `use_fp16_qk_reduction`
and an `_sm90` suffix for the FA3 backend. So a serving deployment compiles a *small, bounded*
set of modules, once, and batch shape never triggers another compile. That distinction is the
difference between "warm-up costs a minute at boot" and "warm-up never ends".

### 4. plan() and run(), which is where the ragged batch is actually handled

```
   wrapper.plan(indptr, indices, last_page_len, n_qo, n_kv, head_dim, page_size, …)
        │   CPU-side: partitions the ragged work across CTAs, sizes the split-K
        │   reduction, fills a 128 MB workspace buffer
        │   "cannot be used in CUDA Graph or in torch.compile"
        ▼
   for layer in range(80):        ← ONE plan, reused across every layer
        o = wrapper.run(q, kv_cache_at_layer[layer])
```

Per-step scheduling is a CPU cost paid once per forward pass, not once per layer, and the
capturable part is `run()`. That is what makes the CUDA-graph story in
[270](270-serving-stack-around-the-kernel.md) possible at all.

### 5. Backends, and everything that is not attention

`backend="auto"` picks among `fa2`, `fa3`, `trtllm-gen`, `cute-dsl` and `cudnn` by architecture
and feature support — and they do not support the same features. The README notes `cute-dsl`
requires equal `head_dim_qk`/`head_dim_vo` and supports no RoPE, ALiBi or soft-cap; the `cudnn`
path supports CUDA graphs and sinks but not RoPE, soft-cap or FP4 KV. Alongside attention the
library ships **GEMM** (BF16/FP8/FP4, grouped GEMM for LoRA and MoE routing), **communication**
(custom AllReduce, multi-node NVLink, NVSHMEM) and **sampling** (sorting-free top-k/top-p/min-p,
chain speculative sampling). Those four families are the whole decode step, not just its
attention.

### 6. The warm-up is a shipped product, which tells you it hurt

`flashinfer-python` compiles or downloads kernels on first use. There are two extra wheels —
`flashinfer-cubin` (prebuilt binaries for all supported architectures) and `flashinfer-jit-cache`
— plus `flashinfer install-cubin-wheel` and `flashinfer download-kernels`. A project does not
build three distribution channels for a cost that does not matter.

## Where this stands, September 2026

Everything above is primary: I read FlashInfer's README, `decode.py`, `sparse.py` and
`jit/attention/modules.py` directly from the repository. The parts that outlive the library are
the two mechanisms. **Online softmax** is a statement about associativity, not about GPUs — it
will survive every architecture that has a fast small memory and a slow large one. **The ragged
index structure** is the same: as soon as requests have different lengths and arrive at different
times, you are storing them in blocks with an index, and a paged cache and a block-sparse mask
become the same object. The backend list, the wheel names and the FA2/FA3/trtllm split are the
perishable part and will read as archaeology within a year. One caution: FlashInfer's own
`plan()` documents `fixed_split_size` and `disable_split_kv` as switches for **deterministic**
reduction, which is an admission that the default is not — see
[272](272-reading-a-kernel-benchmark.md).

## What an interviewer digs into next

* Why is the online-softmax rescale exact rather than an approximation?
* What is actually in FlashInfer's JIT cache key, and what is deliberately not?
* Why can a paged KV cache and a block-sparse mask share one kernel?

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing**. Resolve every identifier before you cite it.
