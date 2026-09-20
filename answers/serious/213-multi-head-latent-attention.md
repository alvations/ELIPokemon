---
id: "213"
slug: multi-head-latent-attention
style: serious
category: open-weights
difficulty: advanced
question: "What does Multi-head Latent Attention actually cost, and what does it buy against GQA and MQA?"
tags: [attention, kv-cache, mla, gqa, deepseek]
---

# It buys you a 57× smaller cache and charges you matmuls, kernels and a fork in the ecosystem.

Multi-head Latent Attention was introduced in [DeepSeek-V2](https://arxiv.org/abs/2405.04434)
and carried through [DeepSeek-V3](https://arxiv.org/abs/2412.19437). Instead of caching a key
and a value per head per token, it caches **one low-rank latent per token** and re-projects it
back up to per-head keys and values when attention actually runs. In V3's configuration that is
a 512-dimensional latent plus a 64-dimensional decoupled RoPE key — **576 values per token per
layer**, against 128 heads × 128 dims × 2 = 32,768 for full multi-head attention. The trade is
explicit: you spend FLOPs and implementation complexity to stop spending HBM.

## What is actually in the cache

```
   per token, per layer — values held in the KV cache

   MHA    K: 128 heads × 128 dims  ┐
          V: 128 heads × 128 dims  ┘ = 32,768   ████████████████████████  1.0×
   GQA    8 KV heads × 128 × 2       =  2,048   █▌                       16×  smaller
   MQA    1 KV head  × 128 × 2       =    256   ▏                       128×  smaller
   MLA    latent 512 + RoPE key 64   =    576   ▍                        57×  smaller
                       │        │
                       │        └ carries position; cannot be folded away
                       └ re-projected to all 128 heads' K and V at read time

   DeepSeek-V3, 61 layers, BF16:  576 × 61 × 2 B  ≈ 70 KB per token
   Reported comparisons:          Llama-3.1 405B ≈ 516 KB · Qwen-2.5 72B ≈ 327 KB

   ┌──────────────── where each design gives something up ─────────────────┐
   │ GQA/MQA  throw away head diversity: fewer distinct K/V subspaces      │
   │ MLA      keeps 128 distinct heads, throws away rank instead           │
   └───────────────────────────────────────────────────────────────────────┘
```

That last box is the whole argument. [GQA](https://arxiv.org/abs/2305.13245) and MQA reduce the
cache by making heads *share* keys and values — you genuinely have fewer distinct K/V subspaces
afterwards. MLA keeps all 128 heads distinct and instead constrains the K/V projection to a
low-rank bottleneck. Note that MQA still caches *less* than MLA (256 values against 576); the
DeepSeek claim is not that MLA is the smallest cache available, it is that MLA gets a
GQA-or-better footprint at MHA-or-better quality. The V2 paper reports MLA outperforming MHA
while caching a fraction as much — that is the result the architecture lives or dies on, and it
is a single-lab result you should want replicated before you build on it.

## The part that refuses to compress: position

RoPE is applied to keys before the dot product, and it is position-dependent, so the
up-projection matrix cannot be pre-absorbed into the query weights — the rotation sits in
between. DeepSeek's answer is the **decoupled RoPE key**: 64 dimensions per token carry
position and are cached uncompressed, alongside the 512-dimensional content latent. 512 for
*what*, 64 for *when*. It is a small tax and the tidiest illustration of the general rule that
compressing a cache is easy until something in the middle of the computation is not linear.

## What it costs

1. **FLOPs at read time.** Every attention call re-expands the latent. In decode you usually
   absorb the up-projections into the query and output weights and never materialise the full
   K/V; in prefill you often want the opposite. That means two code paths, not one.
2. **Tensor parallelism gets awkward.** GQA shards cleanly — give each rank some KV heads. MLA
   has a single shared latent, so a naive TP split duplicates it on every rank and the memory
   win partially evaporates. There is an active literature on fixing this
   ([TPLA](https://arxiv.org/abs/2508.15881) among others), which tells you it is a real problem.
3. **Kernels and ecosystem.** FlashAttention and every serving stack's paged-attention
   implementation assume a K/V layout MLA does not have. Support arrived, but months after the
   weights did, and it is still a narrower road than GQA.
4. **You cannot convert an existing GQA model into one for free.** MLA is a pretraining
   decision.

## What it buys

Memory per token is what sets your maximum batch size at a given context length, and batch size
is what sets your cost per token. A 7× smaller cache than a comparable GQA model is not a 7%
serving improvement, it is the difference between a deployment that pencils out and one that
does not. DeepSeek's repeated API price cuts through 2025 are downstream of exactly this.

## And then the same lab dropped it

The V4 series, previewed in April 2026, **replaced MLA** with a hybrid of *Compressed Sparse
Attention* and *Heavily Compressed Attention*. Reported descriptions have CSA compressing the KV
cache along the **sequence** dimension and then running sparse attention over the survivors,
while HCA compresses harder but stays dense, the two alternating across depth. MLA shrank each
token's entry; CSA and HCA shrink the *number* of entries — a different axis, and the one that
matters when the context is a million tokens rather than a hundred thousand. Coverage of the V4
report quotes roughly **27% of V3.2's single-token inference FLOPs and 10% of its KV cache at
1M context**. I could not reach the report itself (see below), so treat both figures as reported
rather than read.

The lesson generalises past DeepSeek: a KV-cache technique is good against the context length it
was designed for. Per-token compression saturates; sequence-length compression is what is left.

## What an interviewer is listening for

That you can state what is in the cache, in numbers, for all four designs — and that you notice
MQA caches less than MLA, which most candidates miss because they have absorbed "MLA is the
efficient one". Then the decoupled RoPE key, because it shows you know *why* the compression is
not free. The strongest answers finish with the serving consequences — TP sharding, kernel
support, two code paths — rather than stopping at the memory arithmetic.

## Where this stands, September 2026

The V2 and V3 numbers are from the technical reports and are stable. Everything about V4's
CSA/HCA here comes from **secondary coverage**: arxiv.org, DeepSeek's own documentation and
model card host, and the Hugging Face model repositories are all blocked by this environment's
egress proxy, so the V4 technical report could not be read first-hand. The authority is
`DeepSeek-V4` on arXiv and the model cards in the `deepseek-ai` Hugging Face org; read them
before quoting a figure. The MLA-versus-GQA reasoning outlives all of it.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing** — the papers are named because the results are theirs, not because
they were re-read. Resolve every identifier before you cite it.
