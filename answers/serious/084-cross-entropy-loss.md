---
id: "084"
slug: cross-entropy-loss
style: serious
category: fundamentals
difficulty: core
question: "What is cross-entropy loss and why is it the right loss for language modelling?"
tags: [cross-entropy, kl-divergence, mle, nll, loss-functions]
---

# Cross-entropy loss

$$H(p, q) = -\sum_i p_i \log q_i$$

For a one-hot target this collapses to `-log q_correct` — the negative log-probability the model
assigned to the right answer. Three equivalent readings, and being able to give all three is the mark
of a solid answer:

1. **Information theory.** The expected number of bits (or nats) to encode samples from `p` using a
   code optimised for `q`. Minimising it means making your code match reality.
2. **Maximum likelihood.** Minimising cross-entropy over a dataset **is** maximising the likelihood of
   the data under the model. Identical objectives.
3. **KL divergence.** `H(p,q) = H(p) + D_KL(p‖q)`. Since `H(p)` — the data's own entropy — is a
   constant you cannot change, minimising cross-entropy is exactly minimising KL divergence from the
   true distribution.

## Why not squared error

```
   true label = 1

   prediction  │  MSE loss  │  CE loss   │  ← what the gradient says
   ────────────┼────────────┼────────────┤
      0.9      │   0.01     │   0.105    │  "small correction"
      0.5      │   0.25     │   0.693    │  "you're wrong"
      0.1      │   0.81     │   2.303    │  "you're VERY wrong"
      0.01     │   0.98     │   4.605    │  "catastrophically wrong"
                    ▲            ▲
              saturates      unbounded — confident errors are
              near 1         punished proportionally to confidence
```

Three concrete reasons cross-entropy wins for classification:

* **Unbounded penalty for confident errors.** MSE's penalty tops out near 1 no matter how wrong you
  were; CE goes to infinity. Being confidently wrong *should* hurt more than being uncertainly wrong.
* **Clean gradients.** With a softmax output, `∂L/∂z = q − p`. The gradient is simply the prediction
  error — the softmax derivative cancels exactly. With MSE + softmax you get an extra `q(1−q)` factor
  that vanishes when the model is confidently wrong, precisely when you most need a large update.
* **It is the maximum-likelihood estimator** for a categorical output, so it is not a heuristic
  choice — it is the principled one.

## For language modelling

Next-token prediction is classification over the vocabulary at every position:

$$\mathcal{L} = -\frac{1}{N}\sum_{t=1}^{N} \log P(x_t \mid x_{<t})$$

* The **perplexity** everyone reports is `exp` of this (question 036).
* **Scaling laws** are expressed in it, and it is smooth and dense enough to detect small changes.
* Implementations use `log_softmax` for stability (question 083) and take logits, not probabilities.
* Loss is **masked** on padding and, during SFT, on prompt tokens (question 025).
* **Label smoothing** modifies the target from one-hot to `(1−ε)` on the correct class (question 085).

## Practical failure modes

* **Passing probabilities to a loss expecting logits** — double softmax, silently degraded training.
* **Ignoring class imbalance** — cross-entropy weights every example equally; use class weights or
  focal loss when that is wrong (question 071).
* **`log(0)`** if you hand-roll it without a stable formulation.
* **Mis-set `ignore_index`**, so padding contributes loss and dilutes the real signal.

## What an interviewer digs into next

* Show that minimising cross-entropy equals minimising KL divergence.
* Derive `∂L/∂z = q − p` for softmax + cross-entropy.
* Why does MSE + softmax give vanishing gradients on confident errors?
* Why is loss masked on prompt tokens during SFT?
