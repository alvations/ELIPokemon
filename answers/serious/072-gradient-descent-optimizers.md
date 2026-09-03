---
id: "072"
slug: gradient-descent-optimizers
style: serious
category: optimization
difficulty: core
question: "Explain gradient descent and its variants: SGD, momentum, Adam, AdamW."
tags: [sgd, momentum, adam, adamw, optimizers, bias-correction]
---

# Gradient descent and its variants

Gradient descent follows the negative gradient downhill: `θ ← θ − η∇L(θ)`. Everything below is a
refinement of *how* to use that gradient.

## Batch vs stochastic vs mini-batch

| | Gradient from | Per step | Noise |
| --- | --- | --- | --- |
| **Batch GD** | all `n` examples | exact, expensive | none |
| **SGD** | 1 example | noisy, cheap | high |
| **Mini-batch SGD** | `B` examples | the practical choice | tunable via `B` |

Mini-batch wins for two reasons: it uses hardware efficiently, and gradient noise is not purely a
cost — it helps escape sharp minima and acts as implicit regularisation. "SGD" in practice means
mini-batch.

## Momentum

$$v_t = \beta v_{t-1} + \nabla L(\theta_t), \qquad \theta_{t+1} = \theta_t - \eta v_t$$

An exponentially weighted average of past gradients. It solves the **ravine** problem: in a loss
surface curving sharply in one direction and gently in another, plain SGD oscillates across the steep
walls while creeping along the valley.

```
   PLAIN SGD in a ravine              WITH MOMENTUM
   ─────────────────────              ─────────────
      ╲    ╱                             ╲    ╱
       ╲ ↗╱                               ╲  ╱
        ╲╱↘                                ╲╱ ──────►
        ╱╲↗                                ╱╲
       ╱  ╲                               ╱  ╲

   oscillates across, crawls          oscillations cancel;
   forward slowly                     consistent direction accumulates
```

Perpendicular components alternate sign and cancel; the consistent along-valley component
accumulates. `β = 0.9` means an effective average over ~10 steps.

**Nesterov momentum** evaluates the gradient at the *look-ahead* position `θ − ηβv`, which corrects
the step before overshooting rather than after.

## Adaptive methods

**AdaGrad** divides the learning rate by the square root of accumulated squared gradients — giving
rarely-updated parameters larger steps. The accumulator only grows, so the learning rate decays to
zero. **RMSProp** replaces the sum with an exponential moving average, fixing that.

**Adam** ([Kingma & Ba, 2014](https://arxiv.org/abs/1412.6980)) combines momentum with RMSProp:

$$m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t \qquad \text{(first moment — direction)}$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2 \qquad \text{(second moment — scale)}$$
$$\hat m_t = \frac{m_t}{1-\beta_1^t}, \quad \hat v_t = \frac{v_t}{1-\beta_2^t} \qquad \text{(bias correction)}$$
$$\theta_{t+1} = \theta_t - \eta \frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}$$

**Bias correction matters and is often glossed over.** Both moments start at zero, so early estimates
are biased toward zero — severely, since `β₂ = 0.999` means `v` needs thousands of steps to warm up.
Without correction the first steps would be enormous. Dividing by `1−β^t` rescales them; the
correction decays to nothing as `t` grows.

Defaults `β₁ = 0.9, β₂ = 0.999, ε = 1e-8` are unusually robust, which is why Adam became the
default. For large-batch LLM training `β₂ = 0.95` is common, for faster adaptation.

## AdamW

Adam with **decoupled weight decay**
([Loshchilov & Hutter, 2017](https://arxiv.org/abs/1711.05101)):

$$\theta_{t+1} = \theta_t - \eta\left(\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon} + \lambda\theta_t\right)$$

Adding L2 to the *loss* means the penalty gradient goes through the adaptive denominator, so
parameters with large historical gradients get decayed less — the opposite of what regularisation
should do. AdamW applies decay directly to the weights, restoring the intended behaviour. This is a
correctness fix, and AdamW is the standard for transformers.

## Choosing

* **AdamW** — the default for transformers and most deep learning.
* **SGD + Nesterov momentum** — still competitive, sometimes better-generalising, for CNNs.
* **Adam's cost:** two extra FP32 states per parameter, so ~8 bytes/parameter of optimizer state —
  the dominant memory term in fine-tuning (question 027).
* **Newer:** Lion (sign-based, less memory), Sophia, Shampoo/Muon (second-order-ish, gaining traction
  in large-scale pretraining).

## What an interviewer digs into next

* Why does momentum help in ravines specifically?
* Explain bias correction and what happens without it.
* Why is Adam + L2 different from AdamW?
* Why does Adam use ~8 bytes per parameter?
