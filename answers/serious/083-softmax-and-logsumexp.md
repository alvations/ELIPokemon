---
id: "083"
slug: softmax-and-logsumexp
style: serious
category: fundamentals
difficulty: intermediate
question: "What is softmax, and why do we need the log-sum-exp trick?"
tags: [softmax, logsumexp, numerical-stability, overflow, temperature]
---

# Softmax and log-sum-exp

Softmax maps a vector of real scores to a probability distribution:

$$\sigma(z)_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$$

Properties worth knowing: outputs are positive and sum to 1; it is **monotone**, so it never changes
the ranking; it is **shift-invariant** (`σ(z + c) = σ(z)`), which is exactly what the stability trick
exploits; and it is a soft *argmax*, approaching one-hot as scores spread apart.

## The numerical problem

`exp` overflows fast. In FP32, `exp(x)` is `inf` for `x > 88`; in FP16, for `x > 11`.

```
   z = [1000, 999, 998]

   naïve:  exp(1000) = inf
           inf / (inf + inf + inf) = nan     ← run destroyed

   z = [-1000, -999, -998]

   naïve:  exp(-1000) = 0
           0 / (0 + 0 + 0) = nan             ← underflow, same result
```

Attention logits, pre-softmax classifier outputs on hard examples, and anything divided by a small
temperature all reach these magnitudes routinely. This is not a hypothetical.

## The fix

Subtract the maximum before exponentiating. By shift-invariance the result is mathematically
identical:

$$\sigma(z)_i = \frac{e^{z_i - m}}{\sum_j e^{z_j - m}}, \qquad m = \max_j z_j$$

Now the largest exponent is exactly `e⁰ = 1`, so overflow is impossible, and the denominator is at
least 1, so division is safe. The smallest terms may underflow to zero, which is harmless — they were
negligible anyway.

```
   z = [1000, 999, 998],  m = 1000
   → exp([0, -1, -2]) = [1.0, 0.368, 0.135]
   → sum = 1.503
   → [0.665, 0.245, 0.090]     ✅ correct, stable
```

**Log-sum-exp** is the same idea for the log-partition function:

$$\log\sum_j e^{z_j} = m + \log\sum_j e^{z_j - m}$$

## Why you should not compose `log(softmax(x))`

For cross-entropy you need `log P`. Computing softmax then taking the log loses precision: small
probabilities round to zero and `log(0) = -inf`. **`log_softmax`** computes it directly:

$$\log \sigma(z)_i = z_i - m - \log\sum_j e^{z_j-m}$$

No intermediate probability, no catastrophic cancellation. This is why frameworks provide
`log_softmax` and `cross_entropy` that take **logits**, not probabilities — and why passing softmax
outputs into `nn.CrossEntropyLoss` (which applies log-softmax internally) is such a common bug: it
double-applies the softmax and quietly degrades training.

## Where it shows up

* **Attention** — softmax over `n` scores per row. FlashAttention's online softmax (question 010) is
  a streaming version of exactly this max-tracking trick.
* **Cross-entropy loss** — the standard LM objective.
* **Temperature** — dividing logits by `T` before softmax; small `T` makes overflow *more* likely,
  another reason the stable form is mandatory.
* **Mixture models, log-likelihoods, HMM forward algorithms** — anywhere probabilities are summed in
  log space.

## What an interviewer digs into next

* Prove softmax is shift-invariant and explain why that makes the trick valid.
* Why compute `log_softmax` directly rather than `log(softmax(x))`?
* What happens if you pass probabilities to a loss expecting logits?
* How does online softmax in FlashAttention relate to this?
