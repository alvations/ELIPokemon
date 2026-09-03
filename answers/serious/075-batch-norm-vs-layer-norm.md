---
id: "075"
slug: batch-norm-vs-layer-norm
style: serious
category: deep-learning
difficulty: intermediate
question: "How does batch normalization differ from layer normalization?"
tags: [batchnorm, layernorm, groupnorm, normalisation, batch-dependence]
---

# BatchNorm vs LayerNorm

Both normalise activations to zero mean and unit variance, then apply learned scale and shift. They
differ in **which axis the statistics are computed over**, and that single choice determines
everything else.

```
   activations: [batch B, features D]

   BATCHNORM                          LAYERNORM
   ─────────                          ─────────
        features →                         features →
      ┌───┬───┬───┬───┐                ┌───┬───┬───┬───┐
   b  │ ▓ │ ░ │ ▒ │ █ │             b  │ ▓ ▓ ▓ ▓ ▓ ▓ ▓ │ ← stats over
   a  │ ▓ │ ░ │ ▒ │ █ │             a  ├───────────────┤   THIS ROW
   t  │ ▓ │ ░ │ ▒ │ █ │             t  │ ░ ░ ░ ░ ░ ░ ░ │
   c  │ ▓ │ ░ │ ▒ │ █ │             c  ├───────────────┤
   h  └───┴───┴───┴───┘             h  │ ▒ ▒ ▒ ▒ ▒ ▒ ▒ │
        ▲                              └───────────────┘
    stats over THIS COLUMN
    (one feature, all examples)        (one example, all features)

   → an example's output depends       → each example is normalised
     on the other examples in            independently. No coupling.
     the batch
```

## The consequences

| | BatchNorm | LayerNorm |
| --- | --- | --- |
| Statistics over | the batch, per feature | the features, per example |
| Depends on other examples | ✅ (train time) | ❌ |
| Works at batch size 1 | ❌ | ✅ |
| Handles variable-length sequences | ❌ awkward, padding pollutes | ✅ |
| Train/inference behaviour | **different** — running statistics | identical |
| Distributed training | needs syncing across devices | no communication |
| Extra regularisation effect | ✅ from batch noise | ❌ |
| Standard in | CNNs / vision | transformers / NLP |

The train/inference discrepancy is BatchNorm's most operationally painful property. During training
it uses the batch's statistics; at inference there is no batch, so it uses an exponential moving
average accumulated during training. Consequences: results depend on batch size, small batches give
noisy statistics and unstable training, and forgetting `model.eval()` silently corrupts inference.

## Why transformers use LayerNorm

1. **Variable sequence lengths.** Batch statistics computed over padded positions are meaningless.
2. **Small effective batch per device.** Large models shard across devices with few sequences each;
   BatchNorm would need cross-device synchronisation every layer.
3. **Autoregressive inference at batch size 1.** BatchNorm has nothing to normalise over.
4. **Sequence-position coupling.** Batch statistics mix information across examples in ways that
   interact badly with causal masking.

## The rest of the family

* **GroupNorm** — split channels into groups, normalise within each. Batch-independent, standard in
  detection and segmentation where batch sizes are small.
* **InstanceNorm** — GroupNorm with one channel per group; used in style transfer.
* **RMSNorm** — LayerNorm without mean subtraction; the current LLM default (question 005).
* **QK-Norm** — normalise queries and keys before the attention dot product, which stabilises
  attention logits in very large models.

## What normalisation actually does

The original "reduces internal covariate shift" explanation has not held up.
[Santurkar et al. (2018)](https://arxiv.org/abs/1805.11604) showed BatchNorm helps even when
covariate shift is deliberately injected, and argued the real mechanism is **smoothing the loss
landscape** — making gradients more predictable so larger learning rates are safe. There is also a
scale-invariance argument: normalised layers are invariant to weight rescaling, which decouples the
effective learning rate from the weight scale.

## What an interviewer digs into next

* Why does BatchNorm behave differently at train and inference?
* Why is BatchNorm awkward for variable-length sequences?
* What breaks if you use BatchNorm with batch size 2?
* Why has the "internal covariate shift" explanation been questioned?
