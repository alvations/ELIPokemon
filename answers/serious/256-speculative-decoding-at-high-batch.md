---
id: "256"
slug: speculative-decoding-at-high-batch
style: serious
category: optimization
difficulty: advanced
question: "Speculative decoding is a large win at batch size one. Why can it be a loss at high batch?"
tags: [speculative-decoding, roofline, batching, throughput, serving]
---

# Because it spends compute to save memory traffic, and at high batch you have run out of compute.

At batch 1, decoding streams every weight in the model through the memory system to produce one
token, and the arithmetic units are idle for almost the whole step. Verifying `γ+1` positions in
that same step costs nearly nothing, because it is the same weight-streaming pass with a slightly
bigger token dimension. At batch 256 the arithmetic units are the bottleneck, the step time is
already proportional to how many tokens are in flight, and speculation multiplies that number by
`γ+1` while returning `E[τ] ≤ γ+1` tokens. The ceiling on the high-batch speedup is therefore
`E[τ]/(γ+1)`, which is **less than one for every acceptance rate below 1**. That single inequality
is the whole answer; the rest is working out where the crossover sits.

## The roofline, with the arithmetic

Per decode step a dense model moves `2P` bytes of BF16 weights regardless of batch size, and does
about `2PB` FLOPs. So:

```
   arithmetic intensity  =  2PB FLOPs / 2P bytes  =  B FLOP per byte        (BF16 weights)
                                                  =  2B                     (FP8 weights)

   hardware ridge        =  peak FLOP/s / HBM bandwidth
                         ≈  989e12 / 3.35e12  ≈  295 FLOP/byte  on an H100 SXM   [coverage]

           FLOP/s
             │        ┌──────────────────────── compute roof
             │      ╱
             │    ╱   ← slope = HBM bandwidth
             │  ╱
             │╱          B=1      B=32        B=B*          B=256
             └──────────┴─────────┴────────────┴─────────────┴────── intensity ≈ B
                         memory-bound          ridge        compute-bound
                    spare FLOPs: speculate     ───►      no spare FLOPs: don't
```

The 295 is an upper bound on `B*` and not the number you will measure, because KV-cache traffic
also scales with `B`, attention itself is low-intensity, and nobody reaches peak FLOPs. In
practice the crossover for a dense model lands in the tens. Take `B* = 64` for the worked example
below and substitute your own; the shape does not change.

## Where the speedup goes

Normalise the memory-bound step to 1. With draft cost `c` per drafted token relative to a target
step, and `E[τ] = (1 − α^(γ+1))/(1 − α)`:

```
   step time(B, γ)  =  max( 1 , B·(γ+1)/B* )  +  γ·c
   speedup(B, γ)    =  E[τ] · max(1, B/B*)  /  step time(B, γ)
   as B → ∞         →  E[τ] / (γ + 1)                      ≤ 1, equality only at α = 1
```

At `α = 0.8`, `γ = 3`, `c = 0.1`, so `E[τ] = (1 − 0.8⁴)/0.2 = 2.952`, and `B* = 64`:

```
     batch B     baseline step   spec step    accepted/step   speedup
   ────────────────────────────────────────────────────────────────────
         1          1.00           1.30           2.952        2.27
         8          1.00           1.30           2.952        2.27
        16          1.00           1.30           2.952        2.27
        32          1.00           2.30           2.952        1.28
        64          1.00           4.30           2.952        0.69   ◄ now a LOSS
       128          2.00           8.30           2.952        0.71
       256          4.00          16.30           2.952        0.72
   ────────────────────────────────────────────────────────────────────
                                          asymptote: 2.952 / 4 = 0.738
```

Read the discontinuity at `B = 16 → 32`. The baseline is still memory-bound there — it has not
started slowing down at all — but the speculative path already has `B(γ+1) = 128` tokens in flight
and crossed the ridge two doublings earlier. **Speculation hits the roofline at `B*/(γ+1)`, not at
`B*`.** A system that looks healthy at batch 16 turns into a throughput regression at batch 32
with no change in acceptance rate and no change in the model.

## Two more taxes people forget

* **HBM you spent on the drafter is HBM you did not spend on KV cache.** A separate 1B drafter at
  BF16 is 2 GB of weights plus its own cache. On an 80 GB card serving a 70 B model that is
  several per cent of your KV budget, which is several per cent off your maximum concurrency,
  which costs throughput *before* any of the compute argument applies. An MTP module that shipped
  inside the checkpoint costs you nothing here either — it was paid for during pretraining, by
  somebody else. Self-speculation and n-gram drafting do not pay this tax, which is part of why
  they are the sensible things to try first.
* **Acceptance compounds, so long drafts are worth less than they look.** `P(all γ accepted) =
  α^γ`. At `α = 0.5` and `γ = 6` that is 1.6%; lift `α` to 0.925 and the same six-deep draft lands
  62.6% of the time. A forty-fold swing in the value of the tail of the draft from one change in
  `α`. This is why the optimal `γ` moves with `α` and why fixed `γ` is the wrong default.

## What to do about it

Gate the draft length on the batch size, and let it go to zero. Both major open serving stacks
ship exactly this. SGLang's default adaptive schedule, read from its source, is:

```
   batch  1  →  candidate draft depths  [1, 3, 5, 7]
   batch  8  →                          [0, 1, 3]
   batch 32  →                          [0, 1]
   batch 64  →                          [0]            speculation off entirely
```

vLLM expresses the same idea declaratively as `num_speculative_tokens_per_batch_size`, a list of
`(range_start, range_end, num_speculative_tokens)` triples over inclusive batch ranges. Both
primary, read from the repositories in September 2026.

The deeper framing: speculative decoding is a **latency** optimisation that is free in throughput
terms only while you are under the ridge. Below capacity it gives you lower time-per-output-token
at no cost; at capacity it trades throughput for latency at a fixed exchange rate of `E[τ]/(γ+1)`.
If you are holding a p99 TPOT SLO and running below capacity, that trade can still be the right
one, made deliberately. Made accidentally, by benchmarking at batch 1 and deploying at batch 64,
it is just a regression you cannot see.

## What an interviewer digs into next

* Derive `E[τ]/(γ+1)` as the high-batch ceiling and say when it can equal 1.
* Why does speculation cross the roofline at `B*/(γ+1)` rather than at `B*`?
* When is trading throughput for TPOT the right call, and what metric tells you?

## Where this stands, September 2026

The roofline argument is structural and outlives every part number in it: as long as decode
streams weights and verification is batched over positions, speculation will be a way of spending
idle FLOPs, and it will stop paying when the FLOPs stop being idle. The ceiling `E[τ]/(γ+1)` is
algebra. What rots is the constants — the H100 figures above are coverage, the `B* = 64` is
illustrative rather than measured, and the batch schedules are a September 2026 snapshot of two
fast-moving repositories. Newer accelerators with higher FLOP-to-bandwidth ratios push the ridge
*up*, which makes speculation pay at larger batches, so the specific thresholds will drift in a
predictable direction. Measure `B*` on your own hardware with your own model; it is an afternoon's
work and it is the number the whole decision turns on.
