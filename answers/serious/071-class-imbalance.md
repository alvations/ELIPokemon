---
id: "071"
slug: class-imbalance
style: serious
category: fundamentals
difficulty: core
question: "How do you handle severe class imbalance?"
tags: [imbalance, smote, class-weights, focal-loss, threshold-tuning]
---

# Class imbalance

At 0.1% positives, a model predicting the majority class always is 99.9% accurate and useless. But
the honest starting point is that **imbalance is often not the real problem** — the real problems are
usually (a) the wrong metric, (b) too few positives in absolute terms, and (c) the loss function not
reflecting the true cost of errors. Reaching for resampling first is the common mistake.

## The interventions, in the order you should try them

**1. Fix the metric.** Stop using accuracy; use PR-AUC, recall at fixed precision, or expected cost.
Many "imbalance problems" evaporate here — the model was fine and the measurement was wrong.

**2. Tune the threshold.** A model trained on imbalanced data usually *ranks* well; it just outputs
low probabilities. Moving the decision threshold from 0.5 to 0.02 costs nothing and often solves the
problem entirely. **Try this before touching the data.**

**3. Class weights / cost-sensitive learning.** Weight the minority class's loss by roughly the
inverse of its frequency. Supported natively by nearly every library
(`class_weight='balanced'`, `scale_pos_weight`), it changes no data, adds no artifacts, and is a
one-line change. This is the right default.

**4. Resampling** — only if the above are insufficient.

```
   UNDERSAMPLING majority          OVERSAMPLING minority        SMOTE
   ──────────────────────          ─────────────────────        ─────
   🐀🐀🐀🐀🐀🐀🐀🐀 → 🐀🐀        ✨ → ✨✨✨✨              interpolate between
   ✨✨                 ✨✨        🐀🐀🐀🐀   🐀🐀🐀🐀       minority neighbours
                                                                to synthesise new
   ✅ fast, less data              ✅ keeps all data              points
   ❌ throws away real info        ❌ exact duplicates →
                                     memorisation                ⚠️ can interpolate
                                                                    across the class
                                                                    boundary
```

**SMOTE deserves scepticism.** It interpolates between minority neighbours, which assumes the
minority class is locally convex in feature space. On high-dimensional or categorical data that
assumption often fails, and recent work finds it frequently fails to beat plain class weighting or
threshold tuning. Use it, if at all, after trying the simpler options, and never fit it outside the
CV loop — SMOTE-before-split is a classic leakage bug that produces spectacular, meaningless scores.

**5. Focal loss** ([Lin et al., 2017](https://arxiv.org/abs/1708.02002)) —
`FL = -(1-p_t)^γ log(p_t)` down-weights easy examples so training focuses on hard ones. Designed for
extreme imbalance in object detection; useful in deep learning, no help for trees.

**6. Reframe the problem.** If positives are extremely rare, **anomaly detection** (one-class SVM,
isolation forest, autoencoder reconstruction error) may fit better than classification. Also
consider whether a coarser positive class — "any suspicious activity" rather than "confirmed fraud" —
gives more signal.

**7. Get more positives.** Often the highest-leverage action and the least glamorous: targeted
labelling of likely positives, active learning, or combining related positive classes.

## Things that break

* **Resampling before splitting.** Duplicated or synthesised minority points end up in both train
  and validation. Always resample **inside** the CV fold, on training data only.
* **Probability calibration.** Resampling and class weighting distort predicted probabilities. If
  you need calibrated probabilities for downstream cost calculations, recalibrate afterwards
  (question 063) or use class weights with a correction rather than resampling.
* **Stratification.** Always stratify splits and folds, or some folds will contain zero positives.

## What an interviewer digs into next

* Why try threshold tuning before resampling?
* Why is SMOTE-before-split a leakage bug?
* What does class weighting do to your predicted probabilities?
* When would you reframe imbalanced classification as anomaly detection?
