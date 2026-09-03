---
id: "063"
slug: model-calibration
style: serious
category: evaluation
difficulty: advanced
question: "What is model calibration and why does it matter?"
tags: [calibration, ece, reliability-diagram, temperature-scaling, confidence]
---

# Calibration

A model is **calibrated** if its stated confidence matches its accuracy: of everything it says with
70% confidence, about 70% should be correct. This is a distinct property from accuracy — a model can
be highly accurate and badly calibrated, or poorly accurate and perfectly calibrated.

It matters wherever a downstream decision depends on the confidence rather than only the answer:
routing to a human, abstaining, triaging, or combining with other evidence. A 90%-accurate model
that says "99% sure" on everything is unusable for triage, because you cannot tell its good answers
from its bad ones.

## Measuring it

**Reliability diagram** — bin predictions by confidence and plot accuracy per bin:

```
   accuracy
     1.0 │                                    ╱ perfect calibration
         │                                 ╱
     0.8 │                              ╱  ●
         │                           ╱    ●
     0.6 │                        ╱     ●
         │                     ╱      ●        ← below the diagonal:
     0.4 │                  ╱       ●             OVERCONFIDENT
         │               ╱        ●               (the usual case)
     0.2 │            ╱         ●
         │         ╱
         └─────────────────────────────────────►
          0.2   0.4   0.6   0.8   1.0   confidence
```

**Expected Calibration Error** — the weighted average gap between confidence and accuracy across
bins:

$$\text{ECE} = \sum_{m=1}^{M}\frac{|B_m|}{n}\Big|\text{acc}(B_m)-\text{conf}(B_m)\Big|$$

ECE is bin-count-sensitive and can hide compensating errors; report a reliability diagram alongside
it. **Brier score** (mean squared error on probabilities) is a proper scoring rule that captures both
calibration and accuracy in one number.

## Why neural networks are miscalibrated

[Guo et al. (2017)](https://arxiv.org/abs/1706.04599) documented that modern deep networks are
systematically **overconfident**, and that this got worse as networks got larger and better —
accuracy improved while calibration degraded. The causes: cross-entropy training pushes toward
one-hot targets indefinitely, so a model that already classifies correctly keeps being pushed to be
*more* certain; capacity permits near-perfect fit of the training set; and standard regularisation
choices trade calibration for accuracy.

## The LLM-specific picture

The finding that matters here: **base models are reasonably well calibrated on multiple-choice
tasks, and RLHF destroys it.** The GPT-4 technical report showed exactly this — the pretrained model's
confidence tracked accuracy well; the post-trained model was sharply overconfident. The mechanism is
straightforward: preference training rewards decisive, confident answers, so it optimises away the
hedging that calibration requires.

Two distinct notions of confidence for an LLM, worth separating:

* **Token-level probability** of the answer tokens. Cheap, but conflates uncertainty about the fact
  with uncertainty about phrasing.
* **Verbalised confidence** — asking the model to state a percentage. More usable, and typically
  poorly calibrated, clustering at round numbers like 80% and 90%.

Better estimators: **semantic entropy** (sample `k` answers, cluster by meaning, measure entropy over
clusters — high disagreement means high uncertainty), and **self-consistency agreement rate**, which
is a decent practical proxy.

## Fixing it

* **Temperature scaling** — fit a single scalar `T` on a validation set to divide logits before
  softmax. Post-hoc, does not change the ranking of predictions (so accuracy is unchanged), and
  fixes most of the miscalibration. The standard first move.
* **Platt scaling / isotonic regression** — more flexible post-hoc mappings.
* **Conformal prediction** — instead of a calibrated probability, output a *set* of answers with a
  guaranteed coverage rate. Distribution-free and gives an actual guarantee, which is why it is
  gaining ground for high-stakes use.
* **Ensembles** — averaging several models improves calibration substantially.

## What an interviewer digs into next

* Give an example of an accurate but miscalibrated model.
* Why does RLHF degrade calibration?
* Why does temperature scaling leave accuracy unchanged?
* What guarantee does conformal prediction actually provide?
