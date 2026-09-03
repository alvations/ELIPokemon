---
id: "065"
slug: overfitting
style: serious
category: fundamentals
difficulty: core
question: "What is overfitting, how do you detect it, and how do you prevent it?"
tags: [overfitting, regularisation, early-stopping, leakage, validation]
---

# Overfitting

The model learns patterns specific to the training sample — including noise — that do not hold in the
population. Training error keeps falling while test error rises.

```
   error │
         │ ╲                                    ╱ validation
         │  ╲                            ____╱
         │   ╲___                   ___╱
         │       ‾‾‾───────────────╱
         │            ▲
         │            │ early stopping point
         │  ╲         │
         │   ╲________│________________________ training
         └────────────────────────────────────────► epochs
```

## Detection

* **The train/validation gap.** The primary signal. Watch both curves; the epoch where validation
  turns is where overfitting begins.
* **Learning curves vs training-set size.** If validation error is still falling as you add data,
  more data will help. If both curves have plateaued together at a high error, you have a bias
  problem instead, and more data will not help.
* **Cross-validation variance.** Wildly different scores across folds indicate high variance.
* **Sanity check: shuffle the labels.** If the model can fit random labels to zero training error —
  which any sufficiently large network can — you have confirmed it has the capacity to memorise, so
  your regularisation, not your architecture, is what stands between you and memorisation.

## Prevention

**Data:**
* **More data.** The only intervention that reduces variance without adding bias.
* **Augmentation** — realistic transformations that preserve the label. Cheap synthetic data.
* **Better splits** — the fix for the most common cause, below.

**Model:**
* Fewer parameters / lower capacity; shallower trees; fewer features.
* **Regularisation** — L2 (weight decay), L1 (sparsity), dropout, label smoothing.
* **Early stopping** — cheap, effective, and equivalent to a form of regularisation.
* **Ensembling and bagging** — averaging decorrelated errors reduces variance directly.

**Process:**
* A **held-out test set touched once**. Every decision made against a set converts it from a
  measurement into a training signal.
* **Nested cross-validation** when tuning hyperparameters, otherwise your validation score is
  optimistic.

## The most common real cause is not model capacity

In practice, most "overfitting" in production is **data leakage** — the model is not memorising, it
is cheating, and no amount of regularisation fixes it:

* **Target leakage** — a feature that encodes the label. `account_closed_date` predicts churn
  perfectly and does not exist at prediction time.
* **Temporal leakage** — random splits on time-series data let the model see the future. For
  anything temporal, split by time.
* **Group leakage** — the same patient, user, or document in both train and test. Split by group.
* **Preprocessing leakage** — fitting the scaler, imputer, or vectoriser on the full dataset before
  splitting. Fit on train only, inside the pipeline.
* **Duplicate rows** across splits.

The diagnostic that catches most of these: a validation score that is *too good*. Suspicious
performance deserves investigation before celebration, and a feature-importance list where one
feature dominates implausibly is the usual smoking gun.

## What an interviewer digs into next

* How do you distinguish overfitting from leakage?
* Why does early stopping act as regularisation?
* You get 99% AUC on a churn model. What do you check first?
* When would you split by time, and when by group?
