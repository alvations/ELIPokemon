---
id: "089"
slug: bagging-vs-boosting
style: serious
category: classical-ml
difficulty: core
question: "What is the difference between bagging and boosting?"
tags: [bagging, boosting, ensembles, variance, bias, stacking]
---

# Bagging vs boosting

Both are ensembles. They attack **opposite terms** of the bias-variance decomposition, and almost
every difference follows from that.

```
   BAGGING — parallel, reduces VARIANCE     BOOSTING — sequential, reduces BIAS

   data ──┬── bootstrap ──► [strong] ──┐    data ──► [weak] ──► errors
          ├── bootstrap ──► [strong] ──┤              │
          ├── bootstrap ──► [strong] ──┼──► avg       └──► [weak] ──► errors
          └── bootstrap ──► [strong] ──┘                      │
                                                              └──► [weak] ──► ...
   base learners: LOW bias, HIGH variance
   (deep trees) — averaging removes the        base learners: HIGH bias, LOW variance
   variance                                    (stumps/shallow trees) — stacking
                                               removes the bias
```

| | Bagging | Boosting |
| --- | --- | --- |
| Training | parallel ✅ | sequential ❌ |
| Base learners | strong, deep, overfit-prone | weak, shallow |
| Reduces | variance | bias |
| Each learner sees | a bootstrap sample | the current residuals/weights |
| More learners | never hurts | **can overfit** |
| Sensitive to noise | robust | sensitive — it chases mislabelled points |
| Sensitive to outliers | robust | sensitive |
| Key hyperparameters | number of trees (just use many) | learning rate, depth, number of rounds |
| Examples | Random Forest, Extra Trees | AdaBoost, XGBoost, LightGBM, CatBoost |

## Why bagging works

Averaging `n` estimators with pairwise correlation `ρ` and variance `σ²` gives variance
`ρσ² + (1−ρ)σ²/n`. As `n → ∞` the second term vanishes and you are left with `ρσ²`. So **reducing
correlation is what matters**, not adding more trees — which is precisely why Random Forest adds
random feature selection on top of bootstrapping. Bias is unchanged, so you want low-bias (deep) base
learners.

Bootstrap sampling also gives ~37% of data out-of-bag per tree (`(1−1/n)ⁿ → e⁻¹`), providing a free
validation estimate.

## Why boosting works

Each round fits the negative gradient of the loss with respect to current predictions — functional
gradient descent, where each step is a tree rather than a parameter update. The ensemble's bias falls
round by round. Since each learner is deliberately weak (depth 3–8), variance stays low and the
**shrinkage** parameter (learning rate, typically 0.01–0.1) controls how much of each correction is
applied.

The noise sensitivity is the direct consequence: boosting explicitly focuses on what it gets wrong,
and a mislabelled example is something it will always get wrong. It will spend increasing capacity
trying to fit it. Bagging simply averages such a point away.

## The third family: stacking

Train **diverse** base models and a meta-learner on their out-of-fold predictions. Reduces both bias
and variance, wins Kaggle competitions, and is a nuisance in production — many models to serve,
complex retraining, hard to debug. Worth naming as the third option.

## The practical summary

* **High variance / overfitting?** → bagging.
* **High bias / underfitting?** → boosting.
* **Noisy labels?** → bagging; boosting will chase the noise.
* **Need the best number and can tune?** → boosting.
* **Need a strong baseline in one line?** → Random Forest.
* **Need parallel training on a big cluster?** → bagging.

## What an interviewer digs into next

* Derive why correlation limits bagging's benefit.
* Why deep trees for bagging and shallow ones for boosting?
* Why is boosting sensitive to label noise?
* What is out-of-bag error and why is it free?
