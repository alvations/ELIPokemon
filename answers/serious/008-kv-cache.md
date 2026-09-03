---
id: "008"
slug: kv-cache
style: serious
category: inference
difficulty: core
question: "What is a KV cache and why does it dominate LLM inference memory?"
tags: [kv-cache, inference, decoding, memory-bandwidth]
---

# The KV cache

Autoregressive generation is embarrassingly repetitive. To produce token 501 you run attention
over tokens 1–500 — the same keys and values you already computed when producing token 500.
Because the causal mask means past tokens never see the future, **those keys and values can
never change**. So you store them.

```
  WITHOUT CACHE — O(n²) recompute        WITH CACHE — O(n) append
  ───────────────────────────────        ────────────────────────
  step 1: compute K,V for [1]            step 1: K,V for [1]      → cache
  step 2: compute K,V for [1,2]          step 2: K,V for [2]      → append
  step 3: compute K,V for [1,2,3]        step 3: K,V for [3]      → append
  ...                                    ...
  step n: compute K,V for [1..n]         step n: K,V for [n]      → append

  total: O(n²) projections               total: O(n) projections

  ┌──────────── KV cache, layer ℓ ────────────┐
  │ K: [1][2][3][4][5] … [n-1]  ← new k_n ►   │
  │ V: [1][2][3][4][5] … [n-1]  ← new v_n ►   │
  └───────────────────────────────────────────┘
        only the query for token n is new
```

Two phases fall out of this:

* **Prefill** — process the whole prompt in one parallel pass, filling the cache. Compute-bound,
  great GPU utilisation. Cost ∝ prompt length.
* **Decode** — one token at a time, one query against a growing cache. **Memory-bandwidth
  bound**: you stream the entire cache (and the weights) through the memory system to produce a
  single token. Arithmetic intensity is terrible.

That distinction explains most LLM serving behaviour: time-to-first-token is a prefill problem,
inter-token latency is a bandwidth problem, and they need different optimisations.

## The size problem

$$\text{bytes} = 2 \times n_{\text{layers}} \times n_{\text{kv heads}} \times d_{\text{head}}
\times \text{seq len} \times \text{batch} \times \text{bytes per element}$$

For a 70B-class model (80 layers, 64 heads, `d_head` 128, FP16) at 8k context, a **single**
sequence needs ≈ 21 GB of cache — comparable to the weights themselves, and it is *per user*.
Weights are shared across a batch; the KV cache is not. This is why concurrency, not model
size, is usually what caps a serving deployment.

## How the cost is attacked

| Technique | Mechanism | Saving |
| --- | --- | --- |
| **MQA / GQA** | share K/V across query heads | 8–64× |
| **PagedAttention** ([vLLM](https://arxiv.org/abs/2309.06180)) | store cache in fixed blocks, virtual-memory style | removes 60–80% fragmentation waste |
| **Quantised cache** | store K/V in INT8/FP8 | 2–4× |
| **Sliding window / StreamingLLM** | evict old tokens, keep attention sinks | bounds cache to `O(w)` |
| **Prefix / prompt caching** | reuse the cache for a shared system prompt across requests | skips prefill entirely |
| **MLA** (DeepSeek) | cache a low-rank latent, project up on use | large, with careful design |

Note that PagedAttention's win is not compression at all — it is *allocation*. Naïvely
reserving `max_seq_len` per request wastes most of the memory on sequences that finish early;
paging lets you overcommit and raises achievable batch size several-fold, which directly raises
throughput.

## What an interviewer digs into next

* Why can you cache K and V but not the attention output itself?
* Prefill vs decode: which is compute-bound, which is memory-bound, and how does that change
  your batching strategy?
* Compute the KV cache size for a model you know. (Interviewers love this.)
* What breaks if you evict the first few tokens of the cache? (Attention sinks.)
