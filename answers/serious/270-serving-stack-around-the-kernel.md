---
id: "270"
slug: serving-stack-around-the-kernel
style: serious
category: optimization
difficulty: intermediate
question: "Paged attention, continuous batching, chunked prefill and CUDA graphs are four separate fixes. What does each one fix, and where do they collide?"
tags: [vllm, paged-attention, continuous-batching, chunked-prefill, cuda-graphs]
---

# Four fixes to four different wastes — and then they start fighting each other.

Each of the four solves one specific idleness, and any of them alone leaves most of the throughput
on the floor. The interesting part of this question is not the list. It is that **chunked prefill
and full CUDA graphs want opposite things**, and every production engine has to resolve that
explicitly.

```
   ┌── request arrives ────────────────────────────────────────────────────────┐
   │                                                                           │
   │  admission ──▶ SCHEDULER ──▶ batch is assembled ──▶ MODEL RUNNER          │
   │                   │                                     │                 │
   │       continuous batching: refill                CUDA graphs: replay a    │
   │       a slot the step it frees                   recorded launch sequence │
   │                   │                                     │                 │
   │       chunked prefill: cap the                   paged attention: KV in   │
   │       token budget per step                      fixed blocks + a table   │
   └───────────────────────────────────────────────────────────────────────────┘
```

## 1. Paged attention — fixes reserving for a length you do not know

A request's final length is unknown at admission, so the naive allocator reserves `max_model_len`
of contiguous KV per slot. [269](269-flashattention-to-flashinfer.md) has the arithmetic on a real
seven-request batch: 1,982 live tokens cost 2,048 slots in 16-token pages (**3.2% wasted**), 3,703
slots if you pad every request to the longest one (46.5%), and 57,344 slots if you pre-reserve
`max_model_len` (96.5%). Paging also makes prefix sharing a pointer operation rather than a copy.
Cost: every attention kernel now needs a page table, an indirection per block, and a page size —
and the page size sets your internal fragmentation at roughly half a page per sequence.

## 2. Continuous batching — fixes waiting for the slowest sequence

A static batch is admitted together and returns together, so every slot is held until the longest
generation finishes. Iteration-level scheduling admits a new request the step a slot frees.

```
   eight requests, output lengths 32 64 96 200 350 512 700 900

   static      all 8 slots held for 900 steps          = 7,200 slot-steps
               actually generating                     = 2,854 slot-steps
               ─────────────────────────────────────────────────────────
               utilisation 39.6%

   continuous  a slot is refilled the step it frees    → ~100%, minus scheduling
```

Cost: the batch composition changes every step, which is precisely what the next two fixes find
inconvenient.

## 3. Chunked prefill — fixes one long prompt stalling everybody

An 8,192-token prefill takes about 196 ms of pure compute
([268](268-roofline-decode-and-prefill.md)). Run it as one scheduler step and every decoding
request waits 196 ms for its next token — an inter-token latency spike of roughly eleven missed
decode steps, visible to every user on the server. Chunked prefill caps tokens per step and splits
the prefill across several.

vLLM V1's policy, from its own optimization guide: chunked prefill is **on by default**, decode
requests are scheduled **first**, and the remainder of `max_num_batched_tokens` is filled with
prefill, chunking anything that will not fit. The knob is a genuine trade: smaller values (2048)
give better ITL, larger values give better TTFT, and the docs recommend above 8192 for throughput.

```
   max_num_batched_tokens = 2048, 128 decodes in flight
        128 tokens of decode  +  1,920 tokens of prefill per step
        8,192 ÷ 1,920  →  5 chunks
   TTFT: about the same. ITL spike: one chunk instead of the whole prefill.
```

## 4. CUDA graphs — fixes per-launch CPU overhead

A 70B decode step launches on the order of a thousand kernels. At a few microseconds of CPU launch
and dispatch each, that is milliseconds — against 5.36 ms of actual GPU work at batch 1. A CUDA
graph records the launch sequence once and replays it as a single submission.

vLLM V1 exposes this as `cudagraph_mode`: `NONE`, `PIECEWISE` (everything except
graph-incompatible ops, mainly attention), `FULL`, `FULL_DECODE_ONLY`, and `FULL_AND_PIECEWISE` —
the default. A `CudagraphDispatcher` chooses per batch, keyed on a `BatchDescriptor`. Cost: graphs
are captured per batch size, so real batches are padded up to a captured size; capture takes boot
time and memory; `--enforce-eager` turns it all off.

## Where they collide

**This is the answer the question is fishing for.**

```
   chunked prefill produces MIXED batches (prefill tokens + decode tokens)
                    │
                    ▼
   full CUDA graph capture needs a UNIFORM batch shape
                    │
   vLLM's own design doc: only FlashAttention 3 supports unified full capture;
   FlashInfer, FlashMLA and Mamba support CUDA graphs for PURE DECODE only
                    │
                    ▼
   resolution: run TWO execution modes and dispatch between them every step
               FULL for uniform decode · PIECEWISE for everything else
```

Three more, all real:

* **Paged attention is why `PIECEWISE` exists.** The page table changes every step, so the
  attention op stays eager and the graph is cut around it. Cascade attention is not
  graph-compatible at all and is always dispatched to `PIECEWISE`.
* **Continuous batching fights graph capture.** Batch size changes every step; you pad up to the
  nearest captured size, so a batch of 5 runs as a batch of 8 and you pay for three phantom
  sequences. Capturing more sizes costs more memory and more boot time — `FULL_AND_PIECEWISE` is
  documented as the most performant *and* the most memory-hungry and slowest to capture.
* **Paged attention and continuous batching can deadlock into recompute.** When KV runs out, vLLM
  V1 preempts with `RECOMPUTE` by default; the preempted request comes back as a **new prefill**,
  which chunked prefill must then schedule, which displaces decode. Frequent preemption shows up
  as an ITL problem whose actual cause is capacity.

The practical consequence: **you cannot tune these independently.** Lowering
`max_num_batched_tokens` for ITL makes mixed batches more frequent, which makes full graphs less
reachable, which raises CPU overhead at exactly the small batch sizes where CPU overhead
dominates.

## Where this stands, September 2026

The vLLM specifics above are primary — I read `docs/configuration/optimization.md` and
`docs/design/cuda_graphs.md` directly — and they are the perishable part. Mode names, defaults and
which backend supports what will all have moved within a year; check against the version you have
pinned, not the docs on the website ([232](232-reading-an-open-model-card.md)).

What outlives the implementation is the shape of the problem. **Three of the four fixes exist to
handle variability, and the fourth only works when there is none.** Paging, iteration-level
scheduling and chunking all make the workload more heterogeneous step to step, because
heterogeneity is what lets you keep the machine full. Graph capture, kernel specialisation and
every form of ahead-of-time compilation want the opposite. Any serving stack, on any hardware, in
any year, is a negotiated settlement between those two, and the settlement is usually "detect the
uniform case and have a fast path for it".

## What an interviewer digs into next

* Why does chunked prefill make full CUDA graphs harder?
* What sets your internal fragmentation in a paged KV cache, and what is the right page size?
* You lowered `max_num_batched_tokens` and throughput fell. Give two mechanisms.
