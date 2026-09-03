---
id: "082"
slug: activation-functions
style: serious
category: deep-learning
difficulty: core
question: "Compare ReLU, GELU, and SwiGLU. Why did LLMs settle on gated activations?"
tags: [relu, gelu, swiglu, activations, gating]
---

# Activation functions

Without a non-linearity, a stack of linear layers collapses to a single linear layer — depth buys
nothing. The activation is what makes depth meaningful. Which one you pick is a smaller decision than
that, but the details matter at scale.

```
   ReLU: max(0,x)          GELU: x·Φ(x)            SiLU/Swish: x·σ(x)
        │    ╱                   │    ╱                   │    ╱
        │   ╱                    │   ╱                    │   ╱
   ─────┼──╱────           ──────┼──╱────           ──────┼──╱────
        │ ╱                   ╲__│╱                    ╲__│╱
        │                        │                        │
   hard kink at 0          smooth, small negative     smooth, self-gated
   derivative 0 or 1       dip near -0.17             similar to GELU
```

## The classic three

**ReLU** — `max(0, x)`. Derivative is exactly 1 for positive input, so it does not attenuate
gradients, which is what made deep networks trainable (question 074). Cheap. Its failure mode is
**dying units**: a unit whose input is always negative has zero gradient forever and never recovers.
LeakyReLU (`max(αx, x)`) and ELU address this.

**GELU** — `x·Φ(x)`, where `Φ` is the standard normal CDF. Interpreted as a stochastic regulariser
made deterministic: scale the input by the probability that it exceeds a random normal draw. Smooth
everywhere, and its small negative dip lets slightly-negative inputs pass a little signal instead of
being hard-zeroed. Used by BERT, GPT-2, GPT-3.

**SiLU / Swish** — `x·σ(x)`. Found by architecture search, essentially equivalent to GELU in practice
and cheaper to compute.

## Gated activations and SwiGLU

The real shift was to **gating**. A GLU-family layer splits the projection in two and multiplies:

$$\text{SwiGLU}(x) = \big(\text{Swish}(xW_1)\big) \odot (xW_3)$$

One branch computes a value, the other computes a **multiplicative gate** deciding how much of it
passes. This is qualitatively different from a pointwise non-linearity: it is a *data-dependent*
interaction between two learned projections, giving the layer a multiplicative operation it otherwise
cannot express.

[Shazeer (2020)](https://arxiv.org/abs/2002.05202) benchmarked the GLU variants and found consistent
small improvements, concluding with the memorable line that he attributes their success to "divine
benevolence" — an honest admission that the theory is thin and the empirical result is solid.

**The parameter accounting matters.** SwiGLU needs three matrices instead of two, so a naïve swap adds
50% to the FFN. Standard practice shrinks `d_ff` from `4d` to `8/3·d ≈ 2.67d`, keeping the parameter
count matched. Comparisons that do not do this are measuring extra parameters, not the activation.

Used by PaLM, Llama, Mistral, Qwen, Gemma — effectively every current LLM.

## Practical guidance

| Context | Choice |
| --- | --- |
| Transformer FFN | **SwiGLU** (with `d_ff = 8/3 d`) |
| BERT-era / simple transformers | GELU |
| CNNs, RL, anything latency-critical | ReLU |
| Output layer | none, or task-specific (softmax, sigmoid) |
| Gates in LSTMs/GRUs | sigmoid, tanh — structurally required |

The honest summary: **the difference between reasonable modern choices is small**, typically under a
percent, and dwarfed by data, scale, and hyperparameters. It is worth getting right at the frontier
and not worth agonising over otherwise. What *is* worth knowing is that gating adds an expressive
capability, not merely a nicer curve.

## What an interviewer digs into next

* Why does a network without a non-linearity collapse to one layer?
* What is a dying ReLU and how do you detect it?
* Why does SwiGLU shrink `d_ff` to `8/3 d`?
* What can a gated activation express that a pointwise one cannot?
