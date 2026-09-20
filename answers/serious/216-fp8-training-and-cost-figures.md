---
id: "216"
slug: fp8-training-and-cost-figures
style: serious
category: open-weights
difficulty: intermediate
question: "A lab says it trained its model in FP8 for $5.576M. How do you read that figure?"
tags: [fp8, mixed-precision, training-cost, quantisation, deepseek]
---

# FP8 is an engineering result. $5.576M is an accounting one. Only the first is reproducible.

[DeepSeek-V3](https://arxiv.org/abs/2412.19437) reported the first validated FP8 mixed-precision
pretraining run at frontier scale, and reported the run as **2.788M H800 GPU-hours** — 2.664M
pretraining, 119K context extension, 5K post-training — which "at a rental price of $2 per GPU
hour" comes to **$5.576M**. Both halves of that sentence are true and they are true in completely
different ways. The FP8 recipe is a technical claim you can re-implement. The dollar figure is a
marginal cost of one successful run, at an assumed price, on hardware the lab already owned, with
everything that failed excluded by the report's own admission.

## What FP8 training actually involves

You do not simply cast everything to eight bits. FP8 has about two decimal digits of precision;
a naive run diverges. V3's recipe is three separate mitigations:

```
   ┌─ what is in FP8 ────────────┐   ┌─ what deliberately is NOT ──────────┐
   │  GEMM inputs (fwd + both    │   │  embedding module                    │
   │  backward passes)           │   │  output head                         │
   │  most cached activations    │   │  MoE gating                          │
   │                             │   │  normalisation                       │
   │                             │   │  attention operators                 │
   │                             │   │  master weights      (FP32)          │
   │                             │   │  optimizer moments   (BF16)          │
   └─────────────────────────────┘   └──────────────────────────────────────┘

   fine-grained scaling            accumulate wide
   ┌────────────────────────┐      ┌──────────────────────────────────────┐
   │ activations: 1×128 tile│      │ tensor-core FP8 accumulation on H800 │
   │ weights:   128×128 blk │      │ keeps ~14 bits. Promote the partial  │
   │ → one outlier poisons  │      │ sum to FP32 on the CUDA cores every  │
   │   its tile, not the    │      │ 128 elements, then carry on.         │
   │   whole tensor         │      │ Count small, total big.              │
   └────────────────────────┘      └──────────────────────────────────────┘

   Reported result: relative loss error against a BF16 baseline stays under 0.25%.
```

The pattern to take away is general: **quantise the bulk multiply, keep the accumulation and the
sensitive edges wide.** Every low-precision scheme that works looks like this, and every one that
does not is missing either the fine-grained scaling or the wide accumulator.

## How to read the dollar figure

```
   ┌──────────────── INSIDE the $5.576M ─────────────────┐
   │  2.664M GPU-h  pretraining, 14.8T tokens            │
   │  0.119M GPU-h  context extension                    │
   │  0.005M GPU-h  post-training                        │
   │  × $2/GPU-hour ASSUMED rental price                 │
   └─────────────────────────────────────────────────────┘
   ┌──────────────── OUTSIDE it (the report says so) ────┐
   │  prior research · architecture ablations · data     │
   │  ablations · failed runs · data acquisition and     │
   │  cleaning · salaries · the cluster's capital cost · │
   │  everything after post-training                     │
   └─────────────────────────────────────────────────────┘
        ▲
        └ third-party estimates of DeepSeek's total accumulated
          compute spend have run into the billions. That is a
          different quantity, not a contradiction — but quoting
          $5.6M as "what it costs to build a frontier model" is
          comparing a marginal cost to a total one.
```

Four questions to ask of any such number:

1. **Is it the final run only?** Almost always yes, and almost always unstated in the coverage.
2. **Is the price real or assumed?** $2/GPU-hour was a rental rate, not an invoice. A lab that
   owns its cluster pays amortisation and power, not rent.
3. **What hardware?** H800s were the export-compliant part, with cut interconnect. Some of V3's
   most interesting engineering exists *because* of that constraint, so the number does not
   transfer to an H100 or B200 fleet either up or down in an obvious way.
4. **Does the arithmetic close?** Do the 6ND check out loud: 6 × 37B active × 14.8T tokens
   ≈ 3.3 × 10²⁴ FLOPs. Against 2.66M H800-hours that implies a plausible utilisation. A cost
   claim that fails this check is a claim about something else.

And the one that matters most: **it is not reproducible.** The weights are open; the dataset is
not. Nobody outside the lab can spend $5.576M and get V3.

## The 2026 state of the same argument

Coverage of the V4 series reports FP4+FP8 mixed checkpoints — expert weights in FP4, attention,
normalisation and router in FP8 — trained with the Muon optimizer on more than 32T tokens. **No
GPU-hour or dollar figure for V4 turned up in anything I could reach.** Separately, in September
2026 the lab Magic reported matching V4-Pro base-model quality for around $500K using far fewer
FLOPs; coverage gives the multiplier as both "50 times" and "61 times", which is a useful signal
about how carefully any of it was copied. That is a vendor claim about a base model, on
benchmarks of the vendor's choosing, and should be read as an advertisement until someone
independent reproduces it.

## What an interviewer is listening for

That you separate the engineering claim from the accounting one without being prompted, and that
you can say what makes FP8 work — fine-grained scaling plus a wide accumulator — rather than just
"they used eight bits". On the cost, the tell is whether you ask what the figure excludes before
you repeat it. The strongest answers do the 6ND arithmetic in their head and say what the number
would have to be for the claim to hold.

## Where this stands, September 2026

V3's FP8 recipe and the 2.788M GPU-hour breakdown are from the technical report and are stable.
Everything about V4's precision, optimizer and token count here is **secondary**: arxiv.org,
DeepSeek's documentation host and Hugging Face are blocked by this environment's egress proxy, so
neither the V4 report nor its model cards could be read first-hand. The Magic claim is reported
and unverified. Hardware prices and the precision frontier move every few months; the four
questions do not.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing** — the papers are named because the results are theirs, not because
they were re-read. Resolve every identifier before you cite it.
