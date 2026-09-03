---
id: "077"
slug: mixed-precision-training
style: serious
category: systems
difficulty: intermediate
question: "What is mixed-precision training, and why is BF16 preferred over FP16?"
tags: [mixed-precision, fp16, bf16, loss-scaling, fp8, tensor-cores]
---

# Mixed-precision training

Use low precision where it is safe (matmuls, activations) and high precision where it is not
(accumulation, optimizer state, master weights). The payoff: ~2× memory reduction and 2–8× throughput
on tensor cores.

```
   BITS            sign  exponent  mantissa      range          precision
   ────            ────  ────────  ────────      ─────          ─────────
   FP32              1      8         23        ±3e38          ~7 digits
   BF16              1      8          7        ±3e38          ~2-3 digits   ← same range as FP32
   FP16              1      5         10        ±65,504        ~3-4 digits   ← narrow range!
   FP8 E4M3          1      4          3        ±448           ~1-2 digits
```

## Why FP16 is painful

FP16's maximum is 65,504 and its smallest normal is ~6e-5. Gradients routinely fall below that and
**flush to zero**. Activations in large models occasionally exceed the maximum and become `inf`.

The fix is **loss scaling**: multiply the loss by a large constant `S` before the backward pass, so
all gradients scale up by `S` into representable range, then divide by `S` before the optimizer step.
Dynamic loss scaling adjusts `S` automatically — increase it periodically, and on an `inf`/`NaN`
gradient, halve it and **skip that step**.

```
   loss × S ──► backward ──► gradients × S ──► unscale ──► clip ──► step
                   │                              │
              in range now                  check for inf/NaN;
                                            if found: halve S, skip step
```

This works, and it is fragile: skipped steps waste compute, `S` must be tuned, and the failure mode
is a silently diverging run.

## Why BF16 wins

BF16 keeps FP32's **8 exponent bits** — same dynamic range — and sacrifices mantissa bits instead.
Consequences:

* **No loss scaling needed.** Gradients that fit in FP32 fit in BF16.
* **Conversion from FP32 is a truncation** of the low 16 bits, which is trivially cheap.
* **Overflow essentially never happens.**
* The cost is precision: ~3 decimal digits instead of ~4. For gradient descent, which is inherently
  noisy and self-correcting, that turns out not to matter.

The tradeoff — *range matters more than precision for training* — is the key insight, and it is why
BF16 is the default everywhere modern hardware supports it.

## What stays in higher precision

* **Master weights** in FP32 (or the optimizer keeps them). Weight updates are often ~1e-7 relative
  to weights; in BF16 the update rounds to zero and training silently stalls.
* **Optimizer moments** in FP32.
* **Accumulation** inside matmuls in FP32 — tensor cores do this natively.
* **Loss and softmax**, which involve sums over many terms.
* **Normalisation statistics**.

## FP8 and beyond

Hopper/Blackwell support FP8 (E4M3 for forward, E5M2 for backward, trading exponent for mantissa
where each matters more). It requires per-tensor scaling factors updated dynamically, and it is
increasingly used for large-scale pretraining. FP4 exists in research. The general direction —
progressively lower precision with progressively more careful scaling — is stable and likely to
continue.

## What an interviewer digs into next

* Why does BF16 not need loss scaling?
* Why must master weights be FP32 even when compute is BF16?
* What happens during a dynamic loss-scaling overflow?
* Why is the accumulator FP32 even in a BF16 matmul?
