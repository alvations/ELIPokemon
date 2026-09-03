---
id: "088"
slug: trees-forests-boosting
style: serious
category: classical-ml
difficulty: core
question: "Compare decision trees, random forests, and gradient boosting."
tags: [decision-trees, random-forest, xgboost, gbdt, tabular]
---

# Trees, forests, and boosting

## Decision trees

Recursively split the feature space on the single feature/threshold that most reduces impurity —
Gini or entropy for classification, variance for regression.

```
                    Speed > 100?
                   ╱            ╲
                 yes             no
                ╱                  ╲
        Attack > 80?            Defence > 90?
        ╱        ╲               ╱        ╲
    sweeper    fast wall     tank      pivot
```

✅ Interpretable, no scaling needed, handles mixed types and non-linear interactions natively,
invariant to monotone feature transforms.
❌ **High variance** — a slightly different training sample yields a completely different tree.
Axis-aligned splits handle diagonal boundaries poorly. Unpruned trees memorise.

That instability is not a flaw to be fixed; it is the property both ensembles below are built on.

## Random Forest — bagging

Train many deep trees on bootstrap samples, and at each split consider only a random subset of
features (`√p` for classification). Average their predictions.

The double randomisation is the point: bootstrapping alone leaves trees correlated because the same
strong feature dominates the root split in all of them. Restricting features per split **decorrelates**
them, and since averaging `n` correlated variables reduces variance by `ρ + (1−ρ)/n`, lowering `ρ` is
what makes the ensemble work.

Trees are grown deep — low bias, high variance — because averaging removes the variance.

✅ Hard to overfit with more trees (more trees never hurts), parallel, few hyperparameters, free
out-of-bag validation.
❌ Large models, slower inference, usually a point or two behind boosting.

## Gradient boosting — sequential

Fit trees **sequentially**, each on the residual errors of the ensemble so far. Formally, each tree
approximates the negative gradient of the loss with respect to the current predictions.

```
   BAGGING (parallel, variance reduction)     BOOSTING (sequential, bias reduction)

   ┌──┐ ┌──┐ ┌──┐ ┌──┐                        ┌──┐    ┌──┐    ┌──┐    ┌──┐
   │T1│ │T2│ │T3│ │T4│  all independent       │T1│──► │T2│──► │T3│──► │T4│
   └──┘ └──┘ └──┘ └──┘                        └──┘    └──┘    └──┘    └──┘
        ╲  │  │  ╱                             fits    fits    fits    fits
         average                              data   T1's    T2's    T3's
                                                     errors  errors  errors
   deep trees, low bias, high variance        shallow trees (depth 3-8),
   → averaging kills the variance             high bias → boosting kills the bias

   ✅ more trees never hurts                   ❌ more trees CAN overfit — needs
                                                  early stopping
```

XGBoost, LightGBM and CatBoost add: second-order (Newton) optimisation, L1/L2 regularisation on leaf
weights, shrinkage (learning rate), column and row subsampling, and efficient histogram-based split
finding. LightGBM grows leaf-wise (faster, more overfit-prone); CatBoost handles categorical features
natively with ordered target statistics.

## Choosing

| | Tree | Random Forest | Boosting |
| --- | --- | --- | --- |
| Accuracy | low | good | **best on tabular** |
| Overfits with more trees | n/a | ❌ no | ✅ yes |
| Tuning burden | low | low | **high** |
| Parallel training | n/a | ✅ | ⚠️ within trees only |
| Interpretability | ✅ excellent | ❌ | ❌ (use SHAP) |
| Robust to outliers | ✅ | ✅ | ⚠️ less so with squared loss |
| Sensible default | rarely | strong baseline | when accuracy matters |

**The bigger point for an interview:** gradient-boosted trees remain the state of the art for tabular
data, and repeated benchmarks find they still beat deep learning there
([Grinsztajn et al., 2022](https://arxiv.org/abs/2207.08815)). The reasons are structural — tabular
features are heterogeneous and often uninformative, and trees handle irregular, non-smooth target
functions that neural networks bias against. Reaching for a neural network on a tabular problem
usually costs accuracy *and* effort.

## What an interviewer digs into next

* Why does random feature selection at each split matter beyond bootstrapping?
* Why do forests use deep trees and boosting use shallow ones?
* Why can boosting overfit with more trees while bagging cannot?
* Why do trees still beat deep learning on tabular data?
