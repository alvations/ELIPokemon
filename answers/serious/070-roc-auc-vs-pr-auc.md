---
id: "070"
slug: roc-auc-vs-pr-auc
style: serious
category: evaluation
difficulty: intermediate
question: "What is the difference between ROC-AUC and PR-AUC?"
tags: [roc-auc, pr-auc, imbalance, ranking-metrics, average-precision]
---

# ROC-AUC vs PR-AUC

Both summarise a classifier across all thresholds. They differ in what they hold constant, and that
difference matters enormously under class imbalance.

```
   ROC CURVE                            PRECISION-RECALL CURVE
   ─────────                            ──────────────────────
   y: TPR = TP/(TP+FN)   recall         y: precision = TP/(TP+FP)
   x: FPR = FP/(FP+TN)                  x: recall

   TPR │        ____----‾‾‾            prec │‾‾‾--___
       │    __--                            │        ‾--__
       │  _-        ← good                  │             ‾‾--___
       │ -                                  │                    ‾‾--
       │-      ╱ ← random (AUC 0.5)         │  baseline = base rate ─────
       └──────────────────►                 └──────────────────────►
                    FPR                                      recall

   BOTH denominators involve only        The x-axis denominator involves
   ONE class each (TP+FN, FP+TN)         only positives; the y-axis
   → invariant to class balance          denominator MIXES classes
                                         → depends on the base rate
```

## Why ROC-AUC misleads on imbalanced data

`FPR = FP / (FP + TN)`. When negatives are overwhelmingly common, `TN` is enormous, so `FPR` stays
tiny even when the absolute number of false positives is large.

Concretely: 1,000,000 negatives, 1,000 positives. A model producing 10,000 false positives to catch
900 true ones has:

* `FPR = 10,000 / 1,000,000 = 0.01` → looks excellent on the ROC curve.
* `Precision = 900 / 10,900 = 8.3%` → **92% of your alerts are wrong.**

The ROC curve hides this because the huge `TN` count dilutes the false positives. The PR curve
exposes it, because precision never mentions `TN` at all.

## Choosing

| | ROC-AUC | PR-AUC |
| --- | --- | --- |
| Baseline (random) | 0.5, always | the positive base rate |
| Sensitive to imbalance | ❌ invariant | ✅ reflects it |
| Comparable across datasets | ✅ | ❌ — only within one base rate |
| Interpretation | P(random positive ranked above random negative) | average precision over recall levels |
| Use when | classes roughly balanced; both errors matter | positives are rare; you care about the positive class |

**Rule of thumb:** if positives are under ~10% of the data and you care about finding them, report
PR-AUC (or average precision). If someone shows you a 0.97 ROC-AUC on a 0.1% fraud problem, ask for
precision at their operating threshold — that number is the one that determines whether anyone can
use the system.

Note that PR-AUC's base-rate dependence cuts both ways: it correctly reflects difficulty, but it
means a PR-AUC of 0.4 on a 1% problem may be far better than 0.6 on a 20% problem. Always report the
base rate alongside it.

## Practical additions

* **Average precision** is the standard estimator of PR-AUC: `Σ (R_n − R_{n−1}) P_n`. Trapezoidal
  interpolation of PR curves is biased — use AP.
* **Partial AUC** when only a region matters (e.g. FPR < 1%, typical in security).
* **Neither is a business metric.** Both aggregate over thresholds you will never use. Once you have
  chosen a model, report the metrics at your actual operating point, with a cost model if you have
  one.

## What an interviewer digs into next

* Work through why FPR stays small when negatives dominate.
* What is PR-AUC's random baseline, and why does that make cross-dataset comparison invalid?
* Why is trapezoidal interpolation wrong for PR curves?
* Your model has 0.97 ROC-AUC on 0.1% fraud. What do you ask for?
