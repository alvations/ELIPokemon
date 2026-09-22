---
id: "266"
slug: kv-cache-quantisation
style: serious
category: optimization
difficulty: advanced
question: "At what context length does the KV cache cost more than the weights, and what does quantising the cache cost you?"
tags: [kv-cache, quantisation, long-context, serving, memory]
---

# The weights are a fixed cost. The cache is a bill that grows, and nobody reads it.

Weight quantisation gets all the attention because it is what you download. But weights are paid
once and the KV cache is paid per token per sequence, so there is always a context length beyond
which the cache is the larger line item — and on a modern GQA model at modern context lengths, you
are usually already past it. Do the arithmetic out loud; it is the whole answer.

## The arithmetic, on two real configurations

The per-token cache formula is from [228](228-attention-variants-and-kv-arithmetic.md): `2 ×
n_kv_heads × head_dim × bytes × n_layers`.

```
   Llama-3.1-8B  —  32 layers, 8 KV heads, head_dim 128, BF16
   ──────────────────────────────────────────────────────────────────────
   per token   2 × 8 × 128 × 2 × 32   =  131,072 B  =  128 KiB
   weights     8.03B × 2 B            =   16.06 GB

   crossover   16.06e9 / 131,072      =  122,500 tokens IN FLIGHT
   ──────────────────────────────────────────────────────────────────────
   at   8K context:  1.07 GB/seq  →  15 concurrent seqs to match the model
   at 128K context: 17.18 GB/seq  →  ONE sequence outweighs the whole model

   On one 80 GB card: 64 GB left after weights.
        BF16 cache  → 488K tokens →  3.7 sequences at 128K
        FP8  cache  → 977K tokens →  7.4 sequences    ← same card, one flag
        4-bit cache → 1.95M tokens → 14.9 sequences
```

```
   Llama-3.1-405B  —  126 layers, 8 KV heads, head_dim 128, BF16 cache
   ──────────────────────────────────────────────────────────────────────
   per token   2 × 8 × 128 × 2 × 126  =  516,096 B  =  504 KiB
   weights at FP8                     =  ~405 GB

   8 × H100 = 640 GB.  640 − 405 = ~235 GB for cache and activations.
   ──────────────────────────────────────────────────────────────────────
   BF16 cache  235e9 / 516,096 = 455K tokens = 13.9 requests at 32K
   FP8  cache  235e9 / 258,048 = 911K tokens = 27.8 requests at 32K
   ──────────────────────────────────────────────────────────────────────
   Doubling the concurrency of a $250K node, for one configuration flag.
```

Two things fall out that people find surprising. **A single 128K request on an 8B model holds more
bytes of cache than the model has of weights** — and 8B is the size everybody thinks of as "the
small one". And on a large node you hit the *memory wall* long before you hit the crossover, so
the practical question is never "is the cache bigger than the weights" but "how many requests
fit", to which the cache is the only answer that moves.

## Three ways to make the cache smaller, in increasing order of loss

```
   1. BY CONSTRUCTION — GQA, MQA, MLA                        lossless
      change n_kv_heads, or cache a latent and recompute.
      Decided at training time. 8× to 57×.  → 228

   2. QUANTISE — store every token, at fewer bits            lossy, uniform
      FP8: 2×, free in practice.  4-bit: 4×, needs care.
      Decided at serving time. Composes with everything.

   3. EVICT — keep fewer tokens                              lossy, selective
      sliding window, attention sinks, H2O-style scoring.
      Changes what the model can see. Breaks prefix reuse:
      two requests that shared a prefix no longer share a cache
      if eviction chose differently for each.
```

The ordering matters in an interview because candidates jump to (2) and never mention that (1) was
already applied by whoever trained the thing, or that (3) is a different kind of promise — (2)
degrades every token slightly, (3) removes some tokens entirely.

## K is harder than V, and the asymmetry is exploitable

This is the part that separates people who have shipped it from people who have read about it.

```
                    KEYS                          VALUES
   ───────────────────────────────────────────────────────────────────
   consumed by      QKᵀ, then SOFTMAX             a weighted AVERAGE
   error behaves    exponentiated — a small       averaged — errors across
                    logit error becomes a large   tokens partly cancel
                    probability error
   structure        persistent outlier CHANNELS,  no strong channel
                    the same dims every token     structure; per-token is fine
                    (the same fact as 264)
   so quantise      per-CHANNEL, which fights     per-TOKEN, which is the
                    against streaming (the        natural layout, trivially
                    channel isn't complete        done as tokens arrive
                    until the sequence ends)
   ───────────────────────────────────────────────────────────────────
   practical budget:  K at 8 bits, V at 4.  Not K4V4.
```

KIVI and KVQuant are the two names to know for this, and the asymmetry has since become
configuration you can just set. llama.cpp exposes `--cache-type-k` and `--cache-type-v`
**separately**, over `f16`, `bf16`, `q8_0`, `q5_0`, `q5_1`, `q4_0`, `q4_1` and `iq4_nl`. vLLM's
`kv_cache_dtype` includes `fp8_e4m3`, `fp8_e5m2`, `int8_per_token_head`, `int4_per_token_head`,
`nvfp4`, a DeepSeek-MLA-specific `fp8_ds_mla`, and — the asymmetry made explicit in a product — a
mode that stores **K at 8 bits and V at 4**. There is also a flag to *skip* named layers, because
sliding-window layers in a hybrid stack often should not be quantised at all.

Two implementation details that bite. **Per-token scales are not free**: a scale and zero-point
per token per head is itself cache, and at 4 bits on a small head dimension the metadata is a
meaningful fraction of what you saved. And **the first few tokens are not like the others** — they
carry enormous attention mass as sinks, so the standard recipe keeps a full-precision window at
both ends (the first handful of tokens, and the most recent block that is still being written) and
quantises only the settled middle.

## What breaks, and why your eval will not see it

Cache quantisation damage is **concentrated in exactly the capabilities that need long context**:
verbatim retrieval from far back in the prompt, needle-in-a-haystack recall, long multi-step
arithmetic where an early intermediate has to survive, and any task where the model must quote
rather than paraphrase. It also **grows with context length** — the errors accumulate over more
cached tokens and more attention mass is spread over degraded keys.

Which produces the trap: you evaluate the FP8 cache at 4K, see nothing, ship it, and the
regression lives at 100K where your benchmark never goes. **Evaluate a quantised cache at the
context length you actually serve, not at the context length your harness defaults to**
([267](267-evaluating-a-quantised-model.md)).

## What an interviewer digs into next

* At what batch and context does cache quantisation beat weight quantisation? (Do the division.)
* Why is K harder than V — give both the softmax reason and the outlier-channel reason.
* Why does per-channel K quantisation fight against streaming decode?
* When would you evict instead of quantise, and what do you give up in the prefix cache?

## Where this stands, September 2026

The engine-side facts are **primary**: the llama.cpp cache-type list and its separate K and V
flags, and vLLM's `kv_cache_dtype` options including the K8/V4 mode and the per-layer skip list,
were read directly from those projects' sources. The 504 KiB and 128 KiB per-token figures follow
from the published shapes by the arithmetic in [228](228-attention-variants-and-kv-arithmetic.md),
where the 405B figure reproduces a published table exactly. The H100 capacities and the FP8 weight
size for 405B are **coverage**, and the "$250K node" is an order-of-magnitude aside, not a quote.
KIVI and KVQuant are named from working knowledge; their papers were not opened, because arxiv.org
is blocked from here. The specific dtype names will churn. The division will not: weights over
bytes-per-token gives you the number of tokens at which the bill flips, and that number has been
falling every year as context windows grow.
