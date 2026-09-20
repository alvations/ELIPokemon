---
id: "226"
slug: hosting-long-context-multimodal-weights
style: serious
category: open-weights
difficulty: advanced
question: "An open checkpoint advertises a 1M-token window and native vision. What does self-hosting cost that renting hides?"
tags: [long-context, kv-cache, multimodal, serving, open-weights]
---

# Renting hides the per-request memory. Hosting hands it to you.

Question 206 covers what a million-token window changes and what it does not: the input grew, the
output did not, and prompt caching became the architecture rather than an optimisation. All of
that is true whether you rent or host. This is the half that is only true if you host — **when the
weights are yours, the per-request state is your HBM, and it is not a small number.**

Moonshot's Kimi line makes a clean case study because the window moved several times and the
architecture moved with it. Kimi K2 shipped at 128K. Kimi K2.5 is reported at 256K, as is K2.6
(the K2.6 figures are from coverage; there is no public repository for it and the Hugging Face
card was unreachable from this environment). Kimi K3's model summary gives a context length of
**1,048,576** — read directly from the repository table — alongside native vision.

## The window did not get longer by brute force

K3 is 93 layers, and the composition is the point: **69 Kimi Delta Attention layers and 24 gated
MLA layers**. KDA is a linear-attention formulation that replaces a key–value cache growing with
sequence length with a **fixed-size recurrent state**. The lab's earlier Kimi Linear release — a
48B-A3B model — reports that this cuts the need for large KV caches by **up to 75%** and raises
decoding throughput **up to 6x at 1M tokens** (6.3x faster time-per-output-token against MLA).

Two consequences that matter to whoever runs the service:

* **K3 uses no explicit positional embedding.** Position is carried implicitly by KDA's recurrent
  gating and decay, so the report states it extrapolates to 1M-token contexts with no RoPE
  rescaling or interpolation. Pretraining ran at 8K and was extended to 64K; the million comes
  from the mechanism, plus long-context data synthesised by permuting and concatenating documents
  so the embedded task can only be solved by attending across the whole window.
* **The remaining 24 full-attention layers are where your memory goes.** In a hybrid model the
  long-context per-request cost is set by the layers that still keep a growing cache. "Linear
  attention" does not mean "no KV cache"; it means most of it went away. Count the layers that
  did not.

```
   per request, at 1M tokens

   69 x KDA layer        ┌───┐  fixed-size recurrent state, independent of
                         │ S │  sequence length. Cheap to hold, cheap to
                         └───┘  move, and reusable across requests.

   24 x gated MLA layer  ┌──────────────────────────────────────────┐
                         │ K,V ................................ 1M  │  ◄── grows
                         └──────────────────────────────────────────┘

   weights (MXFP4 experts, higher precision elsewhere)   ~1.5 TB, once
   per-request state                                     x concurrency
                                                          ▲
                                                          └ THIS is the
                                                            number that
                                                            decides your
                                                            batch size
```

## Native vision is not free window

MoonViT-V2 is a 401M-parameter encoder, and K3 is trained natively multimodal — vision and text
jointly optimised from the start of pretraining rather than an encoder grafted on afterwards. That
is a genuine capability difference and it comes with a token bill. The report notes a **2x2
pixel-shuffle downsampling that cuts the number of visual tokens by four**, which is what keeps
inputs of up to 3584x3584 pixels affordable inside a 1M window.

Read that the other way round: without the 4x reduction they would not fit. **Images and text
share one budget.** Question 206's warning that a token is not a stable unit applies with more
force here, because the exchange rate between a pixel and a token is an architecture detail that
changes between versions and is never in the headline number.

## Rent versus host, honestly

```
   ┌──────────────┬──────────────────────────┬─────────────────────────────┐
   │              │  RENT (API)              │  HOST (open weights)        │
   ├──────────────┼──────────────────────────┼─────────────────────────────┤
   │ weights      │  not your problem        │  ~1.5 TB resident, 24/7     │
   │ per-req KV   │  bundled into the price  │  YOUR HBM, x concurrency    │
   │ prefix cache │  vendor built it         │  you build it; K3 needs a   │
   │              │                          │  state-aware variant for    │
   │              │                          │  the KDA layers             │
   │ 1M prefill   │  vendor's latency SLO    │  the recurrence does not    │
   │              │                          │  shorten under tensor       │
   │              │                          │  parallelism — needs        │
   │              │                          │  context parallelism        │
   │ quantisation │  chosen for you          │  chosen by you, and K3's    │
   │              │                          │  MXFP4 came from QAT, not   │
   │              │                          │  from your PTQ script       │
   │ price        │  reported ~$3/$15 per M  │  amortised hardware; only   │
   │              │  in/out, flat by length  │  cheap at high utilisation  │
   └──────────────┴──────────────────────────┴─────────────────────────────┘
```

The pricing figures are from coverage; the vendor's own pricing page was blocked from this
environment, and it is the authority. Everything in the host column is from the K3 technical
report, which describes intra-device context parallelism for long-context prefill precisely
because tensor parallelism partitions heads but never shortens a recurrence, and state-aware
prefix caching to reuse KDA state across requests.

The decision rule is not ideological. **Rent until your utilisation is high and steady, then
model the crossover with per-request state included.** Most people who host a 1M-context model on
bursty traffic are paying for idle HBM and calling it independence.

## What an interviewer is listening for

That you name the per-request state as the thing renting hides, and that you know a hybrid
attention stack has two different memory behaviours in one model. The strongest answers ask how
many full-attention layers there are before quoting any KV-cache saving, and note that images and
text compete for the same window.

## Where this stands, September 2026

Architecture figures are from the Kimi K3 technical report and repository model summary, read
directly; Kimi Linear's KV and throughput figures from its repository README; K2.6's from coverage
only. Pricing was not verifiable from here. The window will keep growing and the hybrid ratio will
keep moving — re-read the layer composition, not the context number, when a new version lands.
