---
id: "027"
slug: lora
style: serious
category: fine-tuning
difficulty: core
question: "Explain LoRA. Why is it parameter efficient?"
tags: [lora, peft, low-rank, adapters, intrinsic-dimension]
---

# LoRA

**Low-Rank Adaptation** ([Hu et al., 2021](https://arxiv.org/abs/2106.09685)) freezes the
pretrained weights `W₀` and learns the update as a product of two thin matrices:

$$W = W_0 + \Delta W = W_0 + \frac{\alpha}{r}BA, \qquad
B \in \mathbb{R}^{d\times r},\; A \in \mathbb{R}^{r\times k},\; r \ll \min(d,k)$$

```
      FULL FINE-TUNING                      LoRA
      ────────────────                      ────

      ┌───────────────┐                ┌───────────────┐
      │               │                │               │
      │      W        │  d×k           │      W₀       │  FROZEN ❄️
      │   TRAINABLE   │  = 4096×4096   │               │
      │   16.8M params│                └───────┬───────┘
      └───────────────┘                        │
                                               ▼   ┌───┐
                                          x ───┼──►│ A │ r×k   4096×8
                                               │   └─┬─┘
                                               │     ▼
                                               │   ┌───┐
                                               │   │ B │ d×r   8×4096
                                               │   └─┬─┘
                                               ▼     │
                                               + ◄───┘  × α/r
                                               │
                                               ▼   trainable: 2·4096·8
                                             output   = 65,536  (0.4%)
```

`A` is initialised Gaussian, `B` is initialised to **zero**, so `ΔW = 0` at step 0 and training
starts exactly at the pretrained model — no warmup shock.

## Why low rank is enough

The premise is the **intrinsic dimensionality** result
([Aghajanyan et al., 2020](https://arxiv.org/abs/2012.13255)): the update needed to adapt a
pretrained model to a downstream task lies in a very low-dimensional subspace. You are not
teaching new knowledge — you are selecting and re-weighting behaviours the model already has, and
that requires far fewer degrees of freedom than the model has parameters. Ranks of 8–64 are
typical; `r = 4` is often enough for style adaptation.

## What you actually gain

* **Memory.** Optimizer state is the real cost of fine-tuning: Adam keeps two FP32 moments per
  trainable parameter, so full fine-tuning of a 7B model needs ~56 GB just for optimizer state
  before gradients or activations. LoRA reduces trainable parameters by ~99%, and with it the
  dominant memory term. This is what puts fine-tuning on one GPU.
* **Storage and serving.** Adapters are megabytes, not gigabytes. You can host one base model and
  hot-swap hundreds of task adapters — even batch requests for *different* adapters together.
* **No inference latency**, if you merge: `W ← W₀ + (α/r)BA` gives back an ordinary weight matrix.
  Unmerged (keeping the branch separate) costs a small overhead but preserves swappability.
* **Structurally limited forgetting**, since `W₀` is never touched.

## Practical details that matter

* **Where to apply it.** Originally just `W_Q` and `W_V`. Current practice applies LoRA to all
  attention projections *and* the MLP, which consistently works better at equal parameter budget.
* **`α` and scaling.** The update is scaled by `α/r`, which decouples the learning rate from the
  rank. A common convention is `α = 2r`. **rsLoRA** argues for `α/√r`, which is better behaved at
  high rank.
* **Learning rate.** LoRA wants a much higher LR than full fine-tuning — typically `1e-4` to
  `3e-4` versus `1e-5`.
* **Limits.** LoRA is worse than full fine-tuning when the task genuinely requires new knowledge
  or a large distribution shift (a new language, a new modality). It excels at style, format,
  domain tone, and task specialisation.

## The variants

**QLoRA** (4-bit frozen base), **DoRA** (decompose into magnitude and direction, tune separately),
**LoRA+** (different learning rates for `A` and `B`), **VeRA** (shared frozen random matrices with
tiny learned scaling vectors), **PiSSA** (initialise from the principal singular components of
`W₀` rather than randomly).

## What an interviewer digs into next

* Why initialise `B` to zero rather than both matrices randomly?
* Why does optimizer state, not parameter count, dominate fine-tuning memory?
* What is the cost of merging vs not merging the adapter?
* When would LoRA definitely lose to full fine-tuning?
