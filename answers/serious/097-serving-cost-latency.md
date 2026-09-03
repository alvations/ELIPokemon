---
id: "097"
slug: serving-cost-latency
style: serious
category: mlops
difficulty: intermediate
question: "How do you reduce LLM serving cost and latency in production?"
tags: [serving, latency, throughput, batching, caching, routing]
---

# Reducing LLM cost and latency

First, separate the two phases, because they have different bottlenecks and different fixes:

```
   PREFILL (process the prompt)          DECODE (generate tokens)
   ─────────────────────────             ────────────────────────
   all tokens in parallel                one token at a time
   COMPUTE-bound                          MEMORY-BANDWIDTH-bound
   → drives time-to-first-token           → drives inter-token latency
   → cost ∝ input length                  → cost ∝ output length
```

Output tokens cost several times more than input tokens on most APIs for exactly this reason.

## The levers, roughly by return on effort

**1. Generate fewer tokens.** The most under-used optimisation. Decode dominates latency, so
constraining output length, avoiding verbose formats, and asking for structured rather than
conversational answers cuts cost proportionally. Prompting for brevity is free.

**2. Prompt caching.** If a long system prompt or document prefix is shared across requests, cache
its KV state. Skips prefill entirely for the shared part — often a 50–90% reduction in
time-to-first-token and a large discount on input cost. Requires putting the stable content **first**,
which constrains your prompt layout (question 052).

**3. Route by difficulty.** Most traffic does not need your largest model. A cheap classifier or a
small model with an escalation path handles the bulk; the frontier model handles the rest. This is
frequently the single largest cost reduction available, and it is an architecture decision, not a
tuning one.

**4. Continuous batching.** Static batching wastes GPU time waiting for the longest sequence in the
batch. Continuous (in-flight) batching admits new requests as others finish, raising throughput
several-fold. This is what vLLM, TGI and TensorRT-LLM do, and it is table stakes for self-hosting.

**5. Quantization** (question 030). FP8/INT8 weights roughly halve the bytes moved per token, which
halves decode time in a bandwidth-bound regime.

**6. PagedAttention** — eliminates KV cache fragmentation, raising achievable concurrency
substantially (question 008).

**7. Speculative decoding** (question 033) — 2–3× latency reduction at low concurrency. Note it can
*reduce* throughput at high batch sizes, so it is a latency tool, not a cost tool.

**8. Distillation** — fine-tune a small model on your traffic. 10× cheaper at comparable quality on
*your* task, though it costs engineering effort and an eval set.

**9. Semantic caching** — cache responses keyed by embedding similarity. Excellent hit rates on FAQ
traffic, and dangerous for anything personalised or time-sensitive. Needs a conservative similarity
threshold and a clear TTL.

**10. Streaming.** Does not reduce cost or true latency, but it transforms *perceived* latency —
time-to-first-token is what users experience. Cheap, and it should be the default.

## What to measure

| Metric | Meaning |
| --- | --- |
| **TTFT** | time to first token — prefill + queueing. The perceived responsiveness. |
| **TPOT/ITL** | time per output token — the decode rate. |
| **E2E latency** | `TTFT + TPOT × output_tokens` |
| **Throughput** | tokens/sec across all concurrent requests |
| **Cost per request** | the number that matters to the business |
| **Goodput** | requests/sec *meeting your latency SLO* — the honest capacity number |

The fundamental tension: **larger batches raise throughput and raise per-request latency.** You are
picking a point on that curve, and the right point depends on whether you are serving an interactive
chat or a batch pipeline. Report goodput rather than raw throughput, because throughput at
unacceptable latency is not capacity.

## What an interviewer digs into next

* Why do output tokens cost more than input tokens?
* How does continuous batching differ from static batching?
* Why does speculative decoding help latency but not throughput?
* What are the risks of semantic caching?
