---
id: "165"
slug: vlm-inference-efficiency
style: serious
category: multimodal
difficulty: advanced
question: "What makes vision-language model inference expensive, and how do you fix it?"
tags: [inference, prefill, kv-cache, token-pruning, prefix-caching, batching]
---

# Serving a VLM cheaply

Text LLM serving economics (questions 032, 033) assume prompts of a few hundred to a few thousand
tokens. A single high-resolution image is 2,000-5,000 tokens (question 121). That changes which
part of the system is the bottleneck.

## Where the cost actually is

```
   TEXT LLM                          VLM
   ────────                          ───
   prefill:  short                   prefill: DOMINATES — thousands of image tokens
   decode:   long, memory-bound      decode:  often short ("what is this?" → 20 tokens)

   so: text serving is decode-bound and batches well.
       VLM serving is PREFILL-bound and is compute-bound instead.
```

Three separate costs, frequently conflated:

1. **Vision encoder forward pass** — quadratic in patch count, run once per image.
2. **Prefill over image tokens** in the LLM — the usual culprit, and it scales with the *language
   model's* size, not the encoder's.
3. **KV cache for image tokens** — 4,000 image tokens occupy KV cache for the whole generation, so
   a VLM serves far fewer concurrent requests per GPU than a text model of the same size.

## The levers, best first

* **Prefix caching.** If the same image is asked several questions — a document QA session, an
  agent looking at one screenshot repeatedly — cache the KV for the image prefix and reuse it. This
  is the single biggest win in real workloads and it is often not implemented because the image is
  assumed to change every request. Measure how often it does.
* **Token reduction before the LLM.** Pixel shuffle (question 121) is free 4x. Token merging and
  pruning cut further, with the caveat that they are dangerous on documents. A resampler bounds it
  absolutely (question 119).
* **Right-size the resolution per request.** Most requests do not need maximum tiling. Route: cheap
  low-resolution pass first, escalate only if the model or a classifier says the answer needs detail.
  This is question 132's routing idea applied to compute.
* **Quantise the vision tower.** It is usually a small fraction of parameters but runs in full
  precision by default in many stacks. Check.
* **Batch by image count.** Requests with wildly different numbers of image tokens batch badly;
  bucketing by token count improves throughput materially.

## What does not help as much as expected

* **Speculative decoding** (question 034) targets decode. If your workload is short answers about
  images, decode is not your problem.
* **A smaller language model** with the same vision tower keeps the encoder cost and keeps the
  image token count; savings are smaller than the parameter ratio suggests.
* **Flash attention** helps, and does not change the quadratic token-count scaling that made the
  prefill expensive in the first place.

## Measuring it properly

Report **time to first token** and **tokens per second** separately, and report them **as a function
of image resolution and count** — a VLM benchmarked on one 336px image tells you nothing about its
behaviour on a four-tile document. Also report **concurrent requests per GPU at a latency target**,
because that is what determines cost per query and it is dominated by KV cache pressure, not by
compute.

## What an interviewer digs into next

* Why is VLM serving prefill-bound where text serving is decode-bound?
* When does prefix caching apply, and why is it under-used?
* Why does swapping in a smaller LLM save less than you would expect?
* What does concurrent-requests-per-GPU measure that latency alone does not?
