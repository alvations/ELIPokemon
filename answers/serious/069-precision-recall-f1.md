---
id: "069"
slug: precision-recall-f1
style: serious
category: evaluation
difficulty: core
question: "Explain precision, recall and F1, and when to optimise for each."
tags: [precision, recall, f1, confusion-matrix, threshold]
---

# Precision, recall, F1

```
                        PREDICTED
                    positive   negative
                  ┌──────────┬──────────┐
   A    positive  │    TP    │    FN    │  ← recall = TP/(TP+FN)
   C              │          │  (miss)  │    "of the real positives,
   T              ├──────────┼──────────┤     how many did we catch?"
   U    negative  │    FP    │    TN    │
   A              │ (false   │          │
   L              │  alarm)  │          │
                  └──────────┴──────────┘
                        ▲
                 precision = TP/(TP+FP)
                 "of what we flagged, how much was right?"
```

* **Precision** — how trustworthy a positive prediction is. Costs of being wrong fall on the
  *flagged*.
* **Recall** (sensitivity) — how much of the real thing you found. Costs of being wrong fall on the
  *missed*.
* **F1** — harmonic mean, `2PR/(P+R)`. Harmonic, not arithmetic, so it punishes imbalance: 100%
  recall with 5% precision gives F1 = 0.095, not 0.525.

They trade off through the **threshold**, not through model quality. Lower it and you flag more:
recall rises, precision falls. Every model gives you the whole curve; picking a point on it is a
business decision, not a modelling one.

## Which to optimise

| Optimise | When | Example |
| --- | --- | --- |
| **Precision** | false positives are expensive or erode trust | spam filtering (a lost real email is worse than a spam that got through), automated account bans, surfacing content to users |
| **Recall** | false negatives are dangerous | cancer screening, fraud detection, safety-critical defect detection, security alerting |
| **Both (F1)** | roughly symmetric costs, or a single number is needed for model selection | most benchmarks |

Two refinements worth raising:

**Fβ.** F1 assumes precision and recall matter equally. `F_β = (1+β²)PR/(β²P + R)` weights recall `β`
times as much. `F2` for screening, `F0.5` when precision matters more. If you know the cost ratio,
encode it rather than defaulting to F1.

**Precision@k.** When downstream capacity is fixed — a review team can handle 100 cases a day —
recall over the whole population is irrelevant. What matters is precision in the top 100 by score.
This is the right metric for most triage and ranking systems and is under-used.

## The pitfalls

* **Accuracy on imbalanced data is meaningless.** At 0.1% fraud, predicting "never fraud" is 99.9%
  accurate and worthless. Say this before anything else if an interviewer offers you an accuracy
  number on rare events.
* **Macro vs micro averaging** for multiclass. Macro averages per-class scores equally, so rare
  classes count as much as common ones; micro pools all predictions and is dominated by the common
  classes. Report which, and why.
* **Threshold selection must use validation data**, and thresholds drift as the input distribution
  changes — re-tune them, do not set them once.
* **F1 ignores true negatives entirely**, which is appropriate for rare-positive problems and
  misleading otherwise.

## What an interviewer digs into next

* Why is F1 harmonic rather than arithmetic?
* Your fraud model has 99.9% accuracy. What do you ask next?
* When is precision@k the right metric?
* How would you choose a threshold given a known cost ratio?
