---
id: "032"
slug: pruning-and-sparsity
style: serious
category: inference
difficulty: advanced
question: "What are pruning and sparsity, and why is unstructured sparsity hard to exploit?"
tags: [pruning, sparsity, lottery-ticket, structured, wanda, sparsegpt]
---

# Pruning and sparsity

Pruning removes parameters — setting them to zero, or deleting whole structures — to reduce model
size and cost. The perennial catch: **zeros are only free if the hardware can skip them**, and
scattered zeros cannot be skipped.

## The three regimes

```
  UNSTRUCTURED              SEMI-STRUCTURED (2:4)         STRUCTURED
  ────────────              ─────────────────────         ──────────
  ▓ · ▓ · · ▓ · ·           ▓ ▓ · ·  ▓ · ▓ ·              ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓
  · ▓ · ▓ ▓ · · ▓           · ▓ ▓ ·  ▓ ▓ · ·              ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓
  ▓ · · · ▓ · ▓ ·           ▓ · · ▓  · ▓ ▓ ·              ← whole head/
  · · ▓ ▓ · ▓ · ▓           · · ▓ ▓  ▓ · · ▓                 channel/layer
                                                              REMOVED
  best accuracy             exactly 2 of every 4          worst accuracy
  ~zero speedup on GPU      ~1.5–1.9× on Ampere+          real speedup anywhere
  needs sparse formats      hardware-supported            smaller dense model
```

**Unstructured** pruning gives the best accuracy per parameter removed — you delete exactly the
least important weights. But a GPU matmul reads dense tiles; a matrix that is 90% zeros still costs
a full dense matmul unless you switch to a sparse format, and sparse formats have index overhead,
irregular memory access, and poor tensor-core utilisation. Below roughly 95–99% sparsity, sparse
kernels are *slower* than dense ones. This is the whole answer to the question: the win is
theoretical FLOPs, and the loss is memory-access regularity, which is what actually determines
speed.

**2:4 semi-structured** sparsity is the compromise: exactly two of every four contiguous weights
are zero. NVIDIA Ampere and later implement this in the tensor cores with a compressed format and
index metadata, giving a genuine ~2× matmul speedup at 50% sparsity. Constrained enough to be
hardware-friendly, flexible enough to keep decent accuracy.

**Structured** pruning removes whole units — attention heads, FFN channels, entire layers. The
result is just a **smaller dense model**, so every speedup is real on any hardware with no special
kernels. It costs the most accuracy per parameter removed, and it is what people mostly ship.

## Choosing what to remove

* **Magnitude** — prune the smallest `|w|`. Simple, surprisingly strong baseline.
* **Wanda** ([Sun et al., 2023](https://arxiv.org/abs/2306.11695)) — score by `|w| · ‖x‖`, i.e.
  weight magnitude times input activation norm. One forward pass of calibration data, no
  retraining, and it works well at 50% for LLMs. The key insight is the same as AWQ's: what matters
  is a weight's *effect*, not its size.
* **SparseGPT** — layerwise second-order reconstruction (the same machinery as GPTQ), updating
  remaining weights to compensate for pruned ones. Best one-shot results, more expensive.
* **Movement pruning** — prune by how weights move during fine-tuning, better suited to transfer.

## The Lottery Ticket Hypothesis

[Frankle & Carbin (2018)](https://arxiv.org/abs/1803.03635): a dense network contains a sparse
subnetwork ("winning ticket") which, *trained from the original initialisation*, matches the full
network's accuracy. Fascinating, and mostly not practically usable: finding the ticket requires
training the dense network first, and the result is fragile at scale (needing "rewinding" to an
early-training checkpoint rather than initialisation). Cite it as theory, not as a method.

## Where the field actually landed

For LLMs, pruning has been the *least* successful compression technique. Quantization gives 4× with
almost no quality loss and no kernel exotica; 50% unstructured pruning gives no speedup, and
structured pruning at 50% costs real quality. The practical uses today are 2:4 sparsity where
hardware supports it, structured depth/width pruning followed by distillation-based recovery (the
Minitron-style recipe), and MoE — which is arguably sparsity done right, since it is *activation*
sparsity chosen at runtime rather than weight sparsity fixed at compression time.

## What an interviewer digs into next

* Why doesn't 90% unstructured sparsity give a 10× speedup?
* Why does Wanda's activation-aware score beat pure magnitude?
* What is the relationship between MoE and sparsity?
* If you had to compress a 70B model by 4×, would you prune or quantize, and why?
