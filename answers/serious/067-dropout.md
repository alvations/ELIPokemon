---
id: "067"
slug: dropout
style: serious
category: deep-learning
difficulty: core
question: "How does dropout work, and why does it behave differently at train and test time?"
tags: [dropout, regularisation, ensemble, inverted-dropout, co-adaptation]
---

# Dropout

During training, randomly zero each unit's activation with probability `p`, independently per
example and per forward pass. At test time, use all units.

```
   TRAINING (p = 0.5)                    INFERENCE
   ──────────────────                    ─────────
     ●───●───●                            ●───●───●
      ╲ ╱ ╲ ╱                              ╲ ╱ ╲ ╱
     ✗   ●   ✗    ← dropped this batch    ●   ●   ●   ← all active
      ╱ ╲ ╱ ╲                              ╱ ╲ ╱ ╲
     ●   ✗   ●                            ●   ●   ●

   a different random subnetwork          the full network,
   every single forward pass              deterministic
```

## Why it regularises

**Preventing co-adaptation** ([Srivastava et al., 2014](https://jmlr.org/papers/v15/srivastava14a.html)).
Without dropout, units form fragile committees: unit A learns to correct unit B's systematic error,
which only works if B is present and behaving as usual. With dropout, no unit can rely on any other
being there, so each must learn a feature that is independently useful. The result is redundant,
robust representations rather than brittle chains.

**Implicit ensembling.** A network with `n` droppable units defines `2ⁿ` subnetworks sharing weights.
Training samples from that ensemble; inference approximates averaging over all of it. That is a
genuine ensemble at the cost of one model.

## The scaling, and why the two phases differ

A unit's expected input during training is `(1-p)` times its input at test time, since a fraction `p`
of its sources are zero. Leaving this uncorrected means every layer sees a systematically different
input scale at test time than during training, and the network's activations drift out of the range
it was trained for.

**Inverted dropout** — what every framework implements — fixes it at train time by dividing surviving
activations by `(1-p)`:

$$\text{train: } \tilde{h} = \frac{h \odot \text{mask}}{1-p} \qquad\qquad \text{test: } \tilde{h} = h$$

So expectations match and inference is a plain forward pass with no correction. This is why
`model.eval()` matters, and why forgetting it is one of the most common PyTorch bugs — it silently
degrades results rather than raising an error.

## Practical use

* **Typical rates:** 0.5 for wide fully-connected layers, 0.1–0.3 for smaller ones, 0.0–0.1 in
  transformers. Never on the output layer.
* **Dropout and BatchNorm interact badly** ([Li et al., 2018](https://arxiv.org/abs/1801.05134)) —
  dropout changes the variance that BatchNorm estimated during training, so the running statistics
  are wrong at test time. Modern CNNs largely dropped dropout in favour of BatchNorm.
* **In transformers**, dropout sits on attention weights, after the FFN, and on the residual branch —
  but large-model pretraining often uses **zero dropout**, because with enormous datasets and a
  single pass, overfitting is not the binding problem and dropout only slows convergence. It returns
  during fine-tuning on small datasets.
* **Variants:** DropPath/stochastic depth (drop entire residual branches — standard in modern vision
  models), DropConnect (drop weights, not activations), spatial dropout for convolutions.
* **MC Dropout** — keep dropout *on* at inference and sample several passes; the variance is a cheap
  uncertainty estimate, interpretable as approximate Bayesian inference.

## What an interviewer digs into next

* Why divide by `(1-p)` and why at train time rather than test?
* What happens if you forget `model.eval()`?
* Why has dropout largely disappeared from large-scale pretraining?
* Why do dropout and BatchNorm conflict?
