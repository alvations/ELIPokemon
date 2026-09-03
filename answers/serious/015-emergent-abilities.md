---
id: "015"
slug: emergent-abilities
style: serious
category: research
difficulty: intermediate
question: "What are emergent abilities of LLMs, and are they real?"
tags: [emergence, phase-transitions, metrics, grokking, induction-heads]
---

# Emergent abilities

The claim ([Wei et al., 2022](https://arxiv.org/abs/2206.07682)): some capabilities are absent
in small models, absent, absent — and then appear abruptly past a scale threshold. Multi-step
arithmetic, some multi-task benchmarks, and instruction following were the headline examples.
The implication was unsettling: if capabilities appear discontinuously, you cannot forecast what
the next model will be able to do.

## The rebuttal

[Schaeffer et al. (2023)](https://arxiv.org/abs/2304.15004) argued much of this is a **measurement
artifact**. Consider 5-digit addition scored by exact match. Per-digit accuracy improves smoothly
with scale; exact-match accuracy is that raised to the fifth power, so it hugs zero and then
lurches upward. The underlying capability was improving continuously the whole time — the metric
was discontinuous.

```
  SAME MODELS, TWO METRICS

  per-token log-prob of the correct answer     exact-match accuracy
  (smooth, continuous)                         (nonlinear, "emergent")

   │            ....••••                        │              ████
   │      ...•••                                │              █
   │  ..•••                                     │              █
   │.•                                          │______________█
   └──────────────────────────────►             └──────────────────────►
      model scale                                   model scale
```

Swap exact-match for a continuous metric — token edit distance, Brier score, log-likelihood of
the target — and most "emergent" curves straighten out. The general rule: **discontinuous metrics
manufacture discontinuities.**

## Where the nuance lands

Neither extreme is right, and saying so is what a good answer looks like:

* Many claimed emergences are metric artifacts. That is well supported.
* But some genuine **phase transitions** in internal structure are documented. The clearest is
  **induction heads** ([Olsson et al., 2022](https://arxiv.org/abs/2209.11895)): a specific
  circuit forms over a narrow window of training, visible as a bump in the loss curve, and
  in-context learning ability jumps at exactly that point. That is a real discontinuity in
  mechanism, not in scoring.
* **Grokking** ([Power et al., 2022](https://arxiv.org/abs/2201.02177)) shows sudden
  generalisation long after training accuracy saturates — again a real transition, driven by
  representation reorganisation rather than by a metric.
* From a **product** standpoint the distinction can be moot. If your application needs 95%
  exact-match, "the underlying log-likelihood was improving smoothly" is cold comfort: the
  feature does not work, then it works.

## How to talk about it in an interview

1. State the original claim precisely.
2. Give the metric critique and the arithmetic example.
3. Distinguish *metric* discontinuity from *mechanistic* discontinuity, and cite induction heads
   as a case of the latter.
4. Note the practical implication: measure with continuous metrics if you want to **forecast**,
   with thresholded metrics if you want to know whether you can **ship**.

The honest summary: capability generally improves smoothly; our measurements and our product
thresholds are what tend to be sharp; and there exist a small number of genuine structural phase
transitions during training.

## What an interviewer digs into next

* Design an experiment to distinguish a metric artifact from a real phase transition.
* Why does exact-match on `k` tokens compress smooth improvement into an apparent jump?
* What are induction heads and why is their formation visible in the loss curve?
* If capability is smooth, why can't we predict downstream benchmark scores well?
