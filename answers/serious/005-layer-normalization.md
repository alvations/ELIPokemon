---
id: "005"
slug: layer-normalization
style: serious
category: transformers
difficulty: intermediate
question: "What is layer normalization, and why did LLMs move from post-norm to pre-norm?"
tags: [layernorm, rmsnorm, pre-norm, training-stability]
---

# Layer normalization, pre-norm, and RMSNorm

LayerNorm normalises **across the feature dimension of a single example**:

$$\text{LN}(x) = \gamma \odot \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} + \beta,
\qquad \mu, \sigma^2 \text{ computed over the } d \text{ features of that token}$$

No dependence on other examples in the batch — which is exactly why it, and not BatchNorm,
became the transformer's normaliser: it works with variable-length sequences, with batch size
1, and identically at train and inference time.

## Post-norm vs pre-norm

```
 POST-NORM (original 2017)                PRE-NORM (everything since GPT-2)

   x ─┬─────────────────┐                  x ─┬───────────────────────┐
      │                 │                     │                       │
      ▼                 │                     ▼                       │
   Attention            │                   LayerNorm                 │
      │                 │                     │                       │
      ▼                 ▼                     ▼                       │
      └──────► + ◄──────┘                  Attention                  │
               │                              │                       ▼
               ▼                              └────────► + ◄──────────┘
           LayerNorm                                     │
               │                                         ▼
               ▼                                    (next block)
          (next block)

  residual path passes THROUGH a norm      residual path is a clean highway
  → gradient rescaled at every layer       → gradient reaches layer 0 intact
  → needs warmup, tuned carefully          → trains at depth 100+ stably
```

In post-norm the normalisation sits *on* the residual stream, so the identity path is
re-scaled at every one of `L` layers. Gradients get repeatedly squashed on the way down, and
deep post-norm transformers diverge without careful warmup and initialisation
([Xiong et al., 2020](https://arxiv.org/abs/2002.04745) analyse exactly this).

Pre-norm normalises the *input to the sublayer* and leaves the residual stream untouched, so
there is an unbroken additive path from the loss to the embedding. That is what makes
warmup-free, very deep training practical — and it is why essentially every modern LLM is
pre-norm, usually with one final norm before the output head.

The cost of pre-norm is real but manageable: the residual stream's variance grows with depth
(each block adds to it), later blocks contribute proportionally less, and very deep pre-norm
models can show representational collapse in the last layers. Mitigations include scaling
residual branches by `1/√(2L)` at init, and hybrids like sandwich-norm and DeepNorm.

## RMSNorm

[RMSNorm](https://arxiv.org/abs/1910.07467) drops the mean-centring and the bias:

$$\text{RMSNorm}(x) = \gamma \odot \frac{x}{\sqrt{\frac{1}{d}\sum_i x_i^2 + \epsilon}}$$

Empirically the re-centring contributes almost nothing to LayerNorm's benefit; the
re-**scaling** is what matters. Removing it saves a pass over the vector and a reduction,
which is worth something when this op runs twice per layer in a bandwidth-bound regime. Llama,
Mistral, Qwen, Gemma and most current models use RMSNorm.

## What normalization actually buys you

The original "reduces internal covariate shift" story has not held up well. The better-supported
account is that normalisation **smooths the loss landscape** and makes the effective learning
rate scale-invariant: multiply the weights of a normalised layer by `c` and the output is
unchanged, so the optimiser is far less sensitive to the scale of the initialisation and of the
learning rate. That is why removing it usually costs you stability, not accuracy per se.

## What an interviewer digs into next

* Why doesn't BatchNorm work well for sequences?
* Where exactly does the final norm go in a pre-norm stack, and why is it needed?
* Why can dropping the mean subtraction (RMSNorm) be free?
* What is QK-norm and which failure mode does it fix?
