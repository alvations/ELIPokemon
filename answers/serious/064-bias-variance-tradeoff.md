---
id: "064"
slug: bias-variance-tradeoff
style: serious
category: fundamentals
difficulty: core
question: "Explain the bias-variance tradeoff."
tags: [bias-variance, overfitting, double-descent, generalisation]
---

# The bias-variance tradeoff

For squared error, expected test error decomposes exactly:

$$\mathbb{E}\big[(y-\hat f(x))^2\big] = \underbrace{\big(\mathbb{E}[\hat f(x)]-f(x)\big)^2}_{\text{bias}^2}
+ \underbrace{\mathbb{E}\big[(\hat f(x)-\mathbb{E}[\hat f(x)])^2\big]}_{\text{variance}}
+ \underbrace{\sigma^2}_{\text{irreducible}}$$

* **Bias** — error from wrong assumptions. The model is too simple to represent the truth. Averaged
  over many training sets, it is still wrong in the same direction.
* **Variance** — sensitivity to the particular training set. Retrain on a different sample and you
  get a very different function.
* **Irreducible error** — noise in the labels. No model removes it, and thinking you have is a sign
  of leakage.

```
   error │  ╲                                        ╱
         │   ╲          total error                ╱
         │    ╲___                            ___╱
         │        ‾‾‾‾───────────────────────╱
         │   ╲                             ╱
         │    ╲  bias²                   ╱  variance
         │     ╲___                    ╱
         │         ‾‾‾───────────────╱
         └────────────────────────────────────────────────►
          simple            ▲                      complex
          UNDERFIT          │                      OVERFIT
                     sweet spot
```

The classic diagnostic:

| Train error | Test error | Diagnosis | Fix |
| --- | --- | --- | --- |
| High | High | high bias (underfit) | bigger model, better features, train longer |
| Low | High | high variance (overfit) | more data, regularisation, simpler model |
| Low | Low | good | ship it |
| High | Low | bug | check for leakage, or a mis-split |

## Levers

**Reduces variance:** more data (the only free lunch — it lowers variance without raising bias),
regularisation, bagging/ensembling, early stopping, dropout, data augmentation, feature selection.

**Reduces bias:** more capacity, better features, less regularisation, longer training, a model class
that matches the structure of the problem.

## The modern caveat: double descent

The classical U-curve is not the whole story. Past the interpolation threshold — where the model has
just enough capacity to fit the training data exactly — test error rises to a peak, and then
**decreases again** as capacity grows further
([Belkin et al., 2019](https://arxiv.org/abs/1812.11118); [Nakkiran et al., 2019](https://arxiv.org/abs/1912.02292)).

```
   test │    ╲       ╱‾╲
   error│     ╲    ╱    ╲
        │      ╲__╱      ╲___
        │                     ‾‾‾‾───────────
        └──────────────┬──────────────────────►  capacity
              classical U    ▲            modern regime
                    interpolation threshold
```

The explanation is that among the many functions that fit the data exactly, SGD with weight decay
finds *smooth* ones, and increasing capacity increases the supply of smooth interpolating solutions.
This is why massively overparameterised networks generalise despite having enough capacity to
memorise random labels — a fact the classical framing alone cannot explain.

The tradeoff is still the right mental model for classical models and for reasoning about
regularisation. It is not a complete account of deep learning, and saying so is what distinguishes a
strong answer.

## What an interviewer digs into next

* Which of your interventions reduces variance without increasing bias?
* Why is train error > test error a bug rather than a result?
* What is double descent, and what does it imply about model selection?
* How would you tell underfitting from a data-quality problem?
