---
id: "066"
slug: l1-vs-l2-regularization
style: serious
category: fundamentals
difficulty: core
question: "What is the difference between L1 and L2 regularization?"
tags: [l1, l2, lasso, ridge, sparsity, weight-decay]
---

# L1 vs L2 regularization

Both add a penalty on weight magnitude to the loss; they differ in what the penalty's geometry
rewards.

$$L_1:\; \mathcal{L} + \lambda\sum_i |w_i| \qquad\qquad L_2:\; \mathcal{L} + \lambda\sum_i w_i^2$$

## Why L1 produces exact zeros

The gradient tells the whole story:

$$\frac{\partial}{\partial w_i}\lambda|w_i| = \lambda\,\text{sign}(w_i)
\qquad
\frac{\partial}{\partial w_i}\lambda w_i^2 = 2\lambda w_i$$

L1's pull toward zero is **constant** regardless of how small the weight is, so a weight with weak
gradient support gets pushed to exactly zero and stays there. L2's pull is **proportional** to the
weight, so it shrinks toward zero asymptotically and never arrives.

Geometrically, the constraint region for L1 is a diamond with corners on the axes; for L2 it is a
sphere. The optimum lands where the loss contours first touch the region, and a diamond's corners —
which lie on the axes, i.e. have coordinates exactly zero — are far more likely contact points.

```
        L1 (diamond)                    L2 (circle)

     w₂ │      ╱╲                    w₂ │      ___
        │     ╱  ╲                      │    ╱     ╲
        │    ╱ ●──╲── contours          │   │   ●───│── contours
        │   ╱      ╲                    │    ╲ ___ ╱
    ────┼──◆────────◆──── w₁        ────┼──────●──────── w₁
        │   ╲      ╱                    │
        │    ╲    ╱                     │  touches at a generic point:
        │     ╲__╱                      │  both weights small, neither zero
        │                               │
   touches at a CORNER: w₂ = 0 exactly
```

## Comparison

| | L1 (Lasso) | L2 (Ridge / weight decay) |
| --- | --- | --- |
| Solution | sparse — exact zeros | dense — all small |
| Feature selection | ✅ built in | ❌ |
| Correlated features | picks one arbitrarily, zeroes the rest | shares weight among them |
| Differentiable at 0 | ❌ (needs subgradient/proximal methods) | ✅ |
| Closed form (linear) | ❌ | ✅ `(XᵀX + λI)⁻¹Xᵀy` |
| Bayesian prior | Laplace | Gaussian |
| Stability under resampling | lower | higher |

**Elastic Net** combines them: `λ₁‖w‖₁ + λ₂‖w‖₂²`. It keeps sparsity while handling correlated
features gracefully — with pure L1, a group of correlated predictors gets one survivor chosen by
noise, which is bad for interpretation and unstable across resamples.

## Deep learning specifics

* **L2 is the default**, as `weight_decay`. L1 is rare in deep nets, because sparsity there is
  usually pursued through explicit pruning instead (question 032).
* **AdamW matters.** With adaptive optimizers, adding L2 to the loss is *not* the same as weight
  decay: the penalty gradient gets divided by the same adaptive denominator as everything else, so
  parameters with large historical gradients get decayed less. AdamW
  ([Loshchilov & Hutter](https://arxiv.org/abs/1711.05101)) decouples it, applying decay directly to
  the weights. This is a genuine bug fix, not a tweak, and it is why AdamW replaced Adam.
* **Do not decay biases, LayerNorm gains, or embeddings.** Standard practice excludes them; decaying
  a normalisation scale is meaningless and decaying biases hurts.
* **Interaction with normalisation.** In a normalised network, weight scale does not affect the
  function, so weight decay mostly changes the *effective learning rate* rather than acting as a
  classical complexity penalty.

## What an interviewer digs into next

* Derive why L1 gives exact zeros from the gradient.
* What happens with L1 and two perfectly correlated features?
* Why does AdamW differ from Adam + L2, concretely?
* Why exclude LayerNorm parameters from weight decay?
