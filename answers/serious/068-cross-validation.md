---
id: "068"
slug: cross-validation
style: serious
category: fundamentals
difficulty: core
question: "Explain cross-validation and describe cases where it silently fails."
tags: [cross-validation, k-fold, leakage, time-series, nested-cv]
---

# Cross-validation

Split the data into `k` folds; train on `k-1` and validate on the held-out one; rotate; average. You
get an estimate that uses all the data for both training and validation, plus a **variance** estimate
across folds that a single split cannot give you.

```
   5-fold CV

   fold 1  [VAL][ tr ][ tr ][ tr ][ tr ]  → score₁
   fold 2  [ tr ][VAL][ tr ][ tr ][ tr ]  → score₂
   fold 3  [ tr ][ tr ][VAL][ tr ][ tr ]  → score₃
   fold 4  [ tr ][ tr ][ tr ][VAL][ tr ]  → score₄
   fold 5  [ tr ][ tr ][ tr ][ tr ][VAL]  → score₅

   report mean ± std.  The std is not decoration — it tells you whether
   a 2-point difference between two models means anything.
```

`k = 5` or `10` is standard. Leave-one-out (`k = n`) has low bias and high variance and is usually not
worth the cost.

## The silent failures

Cross-validation's danger is that it **returns a number regardless**. Every failure below yields a
confident, optimistic score.

**1. Temporal data with random folds.** Random splitting trains on the future and validates on the
past. Use **forward-chaining**: train on `[1..t]`, validate on `t+1`, roll forward.

```
   ✅ TIME-SERIES CV
   [tr]                    [VAL]
   [tr][tr]                     [VAL]
   [tr][tr][tr]                      [VAL]
   ─────────────────────────────────────────► time
```

**2. Grouped data split randomly.** The same patient, user, or document appearing in train and
validation means you are testing memorisation. Use `GroupKFold` on the entity id. This is the most
common leakage in real projects.

**3. Preprocessing fitted before splitting.** Scalers, imputers, feature selectors, target encoders,
and SMOTE fitted on the full dataset leak validation statistics into training. **Everything must be
inside the pipeline**, refit per fold. Target encoding without nested CV is a particularly severe
case — it can produce near-perfect CV scores and useless models.

**4. Duplicates and near-duplicates** across folds. Deduplicate first.

**5. Hyperparameter selection on the same CV.** Picking the best of 200 configurations by CV score
means the winning score is optimistically biased — you have selected for fold-specific noise. Fix
with **nested CV**: an inner loop for tuning, an outer loop for estimating.

**6. Ignoring class imbalance.** With rare classes, some folds may contain none. Use stratified
folds.

**7. Distribution shift.** CV estimates performance on data *like the training data*. If deployment
differs — new users, a new season, a different population — CV is measuring the wrong thing entirely,
and no amount of correct CV methodology detects it.

## When not to use it

* **Deep learning at scale.** `k` full training runs is usually prohibitive; a single large held-out
  set is standard.
* **Very large datasets** where a single split already has negligible variance.
* **Genuine time series**, where forward-chaining is the only valid form.

## The rule

> If the CV score is much better than you expected, look for the leak before you celebrate.

Every leakage mode above produces exactly the symptom of a great score, and a great score is the
least alarming thing a dashboard can show you.

## What an interviewer digs into next

* Why must preprocessing be inside the CV loop?
* Design a CV scheme for hospital data with repeated patient visits.
* What is nested CV and when do you need it?
* Why does the fold-to-fold standard deviation matter for model selection?
