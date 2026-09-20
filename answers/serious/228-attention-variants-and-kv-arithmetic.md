---
id: "228"
slug: attention-variants-and-kv-arithmetic
style: serious
category: open-weights
difficulty: advanced
question: "Walk me through MHA, MQA, GQA and multi-head latent attention with real shapes. What does each one actually divide?"
tags: [attention, kv-cache, gqa, mla, deepseek]
---

# Four variants, one number, and it is a straight divisor on your KV cache.

Every variant of attention in the open-weight field differs in exactly one quantity: **how many
distinct key/value vectors you keep per token per layer.** Queries stay at full head count in all
four, because query diversity is what the heads are *for*. So the whole family reduces to one
line of arithmetic, and the fastest way to answer this question is to do that arithmetic out loud
on a real configuration rather than draw four boxes.

```
   KV bytes per token per layer  =  2  ×  n_kv_heads  ×  head_dim  ×  bytes_per_element
                                    ▲        ▲             ▲              ▲
                                  K and V   the only    fixed by      2 for BF16,
                                            thing that  the model     1 for FP8
                                            varies
```

Questions [008](008-kv-cache.md) and [009](009-mqa-and-gqa.md) cover the cache and the MQA/GQA
idea at interview level. This is the version with the shapes in it.

## One concrete configuration, four ways

Take Llama-3.1-405B's shape, because it is public and because DeepSeek published a KV-cache table
that this arithmetic has to reproduce: **126 layers, 128 query heads, head_dim 128, 8 KV heads,
BF16**. Hold everything fixed except `n_kv_heads`.

```
                      n_kv    per layer/token           × 126 layers          ratio
   ─────────────────────────────────────────────────────────────────────────────────
   MHA                 128    2·128·128·2 = 65,536 B    8,257,536 B = 8.26 MB    1×
   GQA  (g = 8)          8    2·  8·128·2 =  4,096 B      516,096 B =  516 KB   16×
   MQA                   1    2·  1·128·2 =    512 B       64,512 B = 64.5 KB  128×
   ─────────────────────────────────────────────────────────────────────────────────

   MLA (DeepSeek-V3: 61 layers, kv_lora_rank 512, qk_rope_head_dim 64)

                       cache = 512 (latent) + 64 (decoupled RoPE key) = 576 values
                       2 bytes each  →   1,152 B per layer per token
                       × 61 layers   →      70,272 B = 70 KB
```

Two of those numbers are checkable against the source. DeepSeek's hardware-architecture paper
reports 516 KB per token for Llama-3.1-405B, 327 KB for Qwen-2.5-72B and 70 KB for DeepSeek-V3 —
and 516,096 bytes and 70,272 bytes are exactly what the formula gives. Qwen-2.5-72B falls out too:
80 layers × 4,096 B = 327,680 B. When your arithmetic reproduces a published table to the byte,
you have understood the mechanism rather than memorised a slogan about it.

## What each variant is actually doing

**MHA** gives every query head a private K and V. Nothing is shared, so the cache carries a
factor of `n_heads`, and at 128 heads that is the difference between a deployable model and one
that spends its whole HBM budget on history.

**MQA** ([Shazeer, 2019](https://arxiv.org/abs/1911.02150)) collapses to a single KV head. It
divides by `n_heads` and it is the only one of the four that measurably hurts, with reported
training instability at scale.

**GQA** ([Ainslie et al., 2023](https://arxiv.org/abs/2305.13245)) partitions query heads into
`g` groups sharing one KV head each. `g = n_heads` is MHA, `g = 1` is MQA, and `g = 8` is what
nearly every open dense model ships, because it buys 16× here for a quality loss that uptraining
on roughly 5% of the original compute mostly closes.

**MLA** (DeepSeek-V2, [arXiv 2405.04434](https://arxiv.org/abs/2405.04434), carried into V3) is a
different move. Instead of sharing heads, it caches a **low-rank latent** of width 512 and
up-projects to per-head K and V at use time. That up-projection would cost compute on every
decode step, except that `W_UK` folds into `W_Q` and `W_UV` folds into `W_O` — so at decode you
never materialise per-head K and V at all.

The detail that trips people up is the **64 extra dimensions**. RoPE is position-dependent, so it
does not commute with the absorption trick: you cannot fold a rotation that differs per token
into a fixed weight matrix. DeepSeek's answer is a *decoupled* RoPE key — 64 dimensions carrying
position, shared across all heads, cached beside the latent. That is why the number is 576 and
not 512, and it is the single best question to ask someone who claims to have read the paper.

```
   decode-time shape, MLA (DeepSeek-V3)

        cached per token:  [ c_KV : 512 ]  [ k_rope : 64 ]    ← shared by all 128 heads
                                  │                │
             absorbed into W_Q ───┘                └─── concatenated, never absorbed
                                  ▼
        effective kernel:  MQA with head_dim 576, not MHA with head_dim 128

        cache  ↓ 57× against MHA on the same model     compute per token ↑
        (65,536 B → 1,152 B per layer per token)       (one much wider head)
```

MLA therefore trades arithmetic for bandwidth, which is the right direction during decode, where
the GPU is bandwidth-bound and its arithmetic units sit idle. It is also why MLA needs its own
kernels: it is not a drop-in for a FlashAttention path shaped around 128-wide heads.

## What the divisor actually buys

Cache size is not the deliverable. Concurrency is.

```
   8 × H100 (80 GB) = 640 GB.  Llama-3.1-405B at FP8 ≈ 405 GB of weights.
   Left for KV, activations and fragmentation: ~235 GB.

                per token      tokens that fit      at 32K context
   ──────────────────────────────────────────────────────────────────
   MHA           8.26 MB          ~28,400            0.9 requests   ← not a server
   GQA (g=8)      516 KB         ~455,000           13.9 requests
   MQA           64.5 KB       ~3,640,000            111 requests
   ──────────────────────────────────────────────────────────────────

   The same 235 GB. The only thing that changed was n_kv_heads.
```

Note what does *not* change: **prefill FLOPs**. Attention compute during prefill is set by the
query head count, which is 128 in all four variants. GQA and MLA are decode-side wins. If your
workload is long prompts and short answers, they buy you batch size and almost no latency.

## Where this stands, September 2026

The configurations will rot; the formula will not. DeepSeek-V3's shape is fixed in the lab's own
repository (`inference/configs/config_671B.json`, which I read directly), while the 70 KB and
516 KB figures come from DeepSeek's papers — arXiv and the Hugging Face model cards were both
unreachable from this environment, so treat those two as read through coverage and check the PDFs
before citing them. What is durable is the divisor: count K and V, count KV heads, multiply by
head_dim, by bytes, by layers. Every architecture shipped since — sparse attention in
DeepSeek-V3.2 and MiniMax M3, hybrid linear stacks in Qwen and Kimi
([231](231-linear-and-hybrid-attention.md)) — changes *which tokens* you attend to, not this line
of arithmetic for the ones you keep.

## What an interviewer digs into next

* Why can RoPE not be absorbed into the query projection, and what are the 64 dimensions for?
* Does GQA help prefill? (No. Say why.)
* When would you still choose MQA in 2026?

**Citation note.** The arXiv identifiers linked above are given from working knowledge and
checked against search results. `arxiv.org` is blocked from the environment this was written
in, so **not one of the papers was opened while writing**. Resolve every identifier before
you cite it.
