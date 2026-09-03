---
id: "030"
slug: quantization
style: serious
category: inference
difficulty: core
question: "What is quantization and what are the tradeoffs between INT8, INT4 and FP8?"
tags: [quantization, gptq, awq, int8, fp8, outliers]
---

# Quantization

Quantization stores and computes weights (and sometimes activations) at lower precision than
FP32/BF16. Since LLM decoding is **memory-bandwidth bound**, halving the bytes per weight roughly
halves the time to stream the model per token — quantization is a latency optimisation at least as
much as a memory one.

$$q = \text{round}\!\left(\frac{x}{s}\right) + z, \qquad
\hat{x} = s\,(q - z)$$

`s` is the scale, `z` the zero-point. **Symmetric** quantization sets `z = 0` (fine for
zero-centred weights); **asymmetric** keeps `z` (needed for post-ReLU activations). Granularity —
per-tensor, per-channel, per-group of 64/128 — trades metadata size against accuracy, and
per-group is the usual sweet spot for 4-bit.

## The formats

| Format | Bits | Notes |
| --- | --- | --- |
| **BF16** | 16 | Baseline. Same exponent range as FP32, fewer mantissa bits. |
| **FP8** (E4M3/E5M2) | 8 | Hardware-native on Hopper/Blackwell. Floating point, so it handles dynamic range far better than INT8. Increasingly the default for both training and inference. |
| **INT8** | 8 | Well supported everywhere; needs outlier handling for activations. |
| **INT4** (GPTQ/AWQ/NF4) | 4 | ~3.5× smaller than BF16 with careful methods; the practical floor for quality. |
| **INT2 / ternary** | 2 | Research; large quality loss unless the model is trained for it. |

## PTQ vs QAT

**Post-training quantization** takes a trained model and quantizes it, usually with a small
calibration set (128–1024 samples) to fit scales. Cheap, minutes to hours, and what nearly
everyone uses. **Quantization-aware training** simulates quantization during training with a
straight-through estimator so the model learns robust weights. Better at very low bit-widths, far
more expensive.

## The outlier problem

The central technical obstacle. Transformer activations contain a small number of features with
magnitudes 10–100× the rest, concentrated in specific channels
([LLM.int8(), Dettmers et al., 2022](https://arxiv.org/abs/2208.07339)). A per-tensor scale sized
to fit the outliers leaves everything else crushed into a handful of levels.

```
   activation magnitudes across channels

   |█|                                    outlier channel
   |█|
   |█|
   |█|  ▁▁▂▁▁▂▁▁▁▂▁▁▂▁▁▁▂▁▁▁▂▁▁▂▁▁▁▂     everything else
   └────────────────────────────────────►

   one scale for all of this  →  the ▁▁▂ region gets ~2 distinct values
```

Solutions:

* **Mixed precision decomposition** (LLM.int8) — keep outlier channels in FP16, quantize the rest.
* **SmoothQuant** — migrate activation difficulty into the weights by rescaling channels, since
  weights are much easier to quantize.
* **AWQ** — identify the ~1% of *salient* weight channels (by activation magnitude, not weight
  magnitude) and scale them to protect them. Activation-aware, calibration-light, fast.
* **GPTQ** — layerwise second-order reconstruction: quantize weights one column at a time,
  updating the remaining ones to compensate using approximate Hessian information. Slower to
  produce, very accurate.

## Weight-only vs weight-and-activation

**Weight-only** (GPTQ, AWQ, NF4) dequantizes to BF16 for the matmul. It gives the full memory and
bandwidth win, which is what matters for batch-1 decoding, but no compute speedup. **W8A8 / FP8**
quantizes activations too and uses low-precision tensor cores, giving a genuine compute speedup —
which matters at high batch sizes where you become compute-bound. Choose based on which regime you
serve.

## What degrades

Perplexity is a poor detector: it moves ~1% while multi-step reasoning, long-context recall, and
rare-language performance degrade much more. Evaluate quantized models on your hardest tasks, not
on perplexity. Smaller models are also less robust to quantization than large ones — the redundancy
that makes 4-bit safe at 70B is not there at 1B.

## What an interviewer digs into next

* Why is decoding bandwidth-bound, and why does that make weight-only quantization effective?
* What causes activation outliers, and why do they sit in fixed channels?
* When would you pick FP8 over INT8?
* Why is perplexity a misleading way to evaluate quantization damage?
