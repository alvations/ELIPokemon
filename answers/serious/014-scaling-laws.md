---
id: "014"
slug: scaling-laws
style: serious
category: training
difficulty: intermediate
question: "Explain neural scaling laws and the Chinchilla compute-optimal result."
tags: [scaling-laws, chinchilla, compute-optimal, kaplan, inference-cost]
---

# Scaling laws and Chinchilla

**Scaling laws** are the empirical observation that language-model loss falls as a smooth power
law in model parameters `N`, dataset size `D`, and compute `C` — over many orders of magnitude,
with no visible discontinuity:

$$L(N, D) = E + \frac{A}{N^{\alpha}} + \frac{B}{D^{\beta}}$$

`E` is the irreducible entropy of language; the other two terms are what you can buy. The
practical value is **prediction**: fit the curve on small runs and forecast the loss of a run
that costs ten million dollars, before spending it.

## Kaplan vs Chinchilla

[Kaplan et al. (2020)](https://arxiv.org/abs/2001.08361) concluded that given more compute you
should mostly grow the *model*, scaling parameters much faster than data. The field built GPT-3
(175B parameters, 300B tokens) on that basis.

[Hoffmann et al. (2022)](https://arxiv.org/abs/2203.15556) — Chinchilla — re-ran the experiment
over 400 models with properly tuned learning-rate schedules for each and found the opposite:
**parameters and data should scale roughly equally**, about **20 tokens per parameter** at the
compute-optimal point. Kaplan's runs had used a fixed schedule not adapted to each budget,
which systematically penalised the small-model/large-data corner.

```
  For a FIXED compute budget C ≈ 6ND, where do you spend it?

   loss │
        │  ╲                                    ╱
        │   ╲        Kaplan says here ─┐       ╱
        │    ╲                         ▼      ╱
        │     ╲___                  ╱‾‾╲    ╱
        │         ‾‾‾───────────────    ────
        │              ▲
        │              └── Chinchilla optimum: D ≈ 20N
        └──────────────────────────────────────────────►
         all params                          all data
         (huge model,                     (small model,
          few tokens)                     many tokens)

   Chinchilla 70B  beat  Gopher 280B  at the SAME compute.
   4× smaller, 4× more data, better on nearly every benchmark.
```

## The twist: compute-optimal is not deployment-optimal

Chinchilla optimises **training** compute. Nobody trains a model to admire it — you serve it,
often for billions of tokens. Inference cost scales with `N`, not with `D`, so if the model will
be served heavily it is rational to **overtrain a smaller model far past its Chinchilla point**:
you spend more once to save forever.

This is why Llama-class models are trained on 15–20 *trillion* tokens for 7–70B parameters —
ratios of 300:1 or more, wildly "compute-suboptimal" by Chinchilla and obviously correct in
practice. [Sardana et al. (2023)](https://arxiv.org/abs/2401.00448) formalised this by folding
expected inference volume into the objective.

## Caveats worth raising

* **Loss is not capability.** Scaling laws predict cross-entropy beautifully and downstream task
  performance only loosely.
* **Data quality changes the constants.** Curation, dedup and filtering shift the curve; the
  exponents are more stable than the offsets.
* **Data is finite.** High-quality public text is a bounded resource, which is why repetition
  (up to ~4 epochs is roughly as good as fresh data), synthetic data, and multimodal sources
  matter.
* **Post-training changes everything.** Modern capability owes as much to instruction tuning and
  RL as to raw pretraining scale, and those are not covered by these laws.

## What an interviewer digs into next

* Where does `C ≈ 6ND` come from? (Forward + backward FLOPs per token per parameter.)
* Why did Kaplan and Chinchilla disagree, methodologically?
* When should you deliberately train past the compute-optimal point?
* If loss keeps falling smoothly, what explains apparently abrupt capability jumps?
