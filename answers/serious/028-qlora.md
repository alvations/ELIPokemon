---
id: "028"
slug: qlora
style: serious
category: fine-tuning
difficulty: intermediate
question: "What is QLoRA and how does it combine 4-bit quantization with LoRA?"
tags: [qlora, nf4, double-quantization, paged-optimizers, peft]
---

# QLoRA

[QLoRA](https://arxiv.org/abs/2305.14314) fine-tunes a **4-bit quantized frozen base model** with
LoRA adapters kept in 16-bit. The headline result was fine-tuning a 65B model on a single 48 GB
GPU with no measurable quality loss versus 16-bit LoRA.

```
   ┌──────────────────────────────────────────────────────────────┐
   │  BASE MODEL: 4-bit NF4, frozen ❄️        65B → ~33 GB        │
   │                                                              │
   │  forward pass:                                               │
   │     stored 4-bit ──dequantize──► BF16 ──matmul──► activations│
   │            (per block, on the fly, never stored in BF16)     │
   │                              +                               │
   │  ┌────────────────────────────────────────────────────────┐  │
   │  │  LoRA A, B: BF16, trainable ✅        ~0.2 GB          │  │
   │  │  gradients flow THROUGH the frozen 4-bit weights       │  │
   │  │  but are only APPLIED to A and B                       │  │
   │  └────────────────────────────────────────────────────────┘  │
   └──────────────────────────────────────────────────────────────┘
```

The key structural point: gradients must be *back-propagated through* the quantized weights
(you need `∂L/∂x` to reach the adapter), but they are never *stored for* them. No optimizer state,
no gradient buffers, no master copy for 99.6% of the parameters.

## The three technical contributions

**1. NF4 — 4-bit NormalFloat.** Pretrained weights are approximately zero-centred and normally
distributed. NF4 places its 16 quantization levels at the quantiles of a standard normal, so each
level is used with roughly equal probability. This is information-theoretically optimal for
normally distributed data and beats uniform INT4 and FP4 measurably. Quantization is
**blockwise** (blocks of 64), each block with its own scale, so outliers only damage their block.

**2. Double quantization.** Each block needs a 32-bit scale constant. At block size 64 that is
`32/64 = 0.5` bits per weight — significant when the weights themselves are 4 bits. So quantize
the constants too (8-bit, blocks of 256), saving ~0.37 bits/parameter, about 3 GB on a 65B model.

**3. Paged optimizers.** Use NVIDIA unified memory so optimizer state pages out to CPU RAM on a
gradient-checkpointing memory spike instead of OOM-ing. Prevents the crash that would otherwise
end a long run.

## Where the memory actually goes

| Component (7B model) | Full FT (BF16) | LoRA (BF16) | QLoRA (NF4) |
| --- | --- | --- | --- |
| Weights | 14 GB | 14 GB | **~4 GB** |
| Gradients | 14 GB | ~0.05 GB | ~0.05 GB |
| Adam state | 56 GB | ~0.2 GB | ~0.2 GB |
| **Total (approx.)** | **~84 GB** | **~15 GB** | **~5 GB** |

LoRA removes the optimizer state; QLoRA additionally removes most of the weight memory. They
attack different terms, which is why they compose so well.

## Tradeoffs

* **Slower**, by roughly 20–40%, because every matmul dequantizes on the fly. You are trading
  compute for memory — the right trade when the alternative is not fitting at all.
* **Base quality is slightly degraded** by 4-bit quantization; the adapter largely compensates
  during fine-tuning, which is why fine-tuned quality matches but the *starting point* is worse.
* **Merging is awkward.** You cannot cleanly merge a BF16 adapter into 4-bit weights without
  re-quantizing and losing some of the adapter's precision. Common practice is to serve the
  adapter unmerged, or merge into a 16-bit copy of the base.
* **QLoRA is for training memory**, not primarily for inference speed. For serving, you would
  typically use a different quantization scheme (AWQ, GPTQ) tuned for throughput.

## What an interviewer digs into next

* Why quantile-spaced levels (NF4) rather than uniform?
* Why must gradients flow through the frozen weights even though they are not updated?
* Why is double quantization worth 0.37 bits, and when does it not matter?
* What breaks when you merge a 16-bit adapter into a 4-bit base?
