---
id: "085"
slug: label-smoothing
style: serious
category: training
difficulty: intermediate
question: "What is label smoothing and when does it hurt?"
tags: [label-smoothing, calibration, regularisation, distillation]
---

# Label smoothing

Replace the one-hot target with a slightly softened one
([Szegedy et al., 2015](https://arxiv.org/abs/1512.00567)):

$$y_i^{LS} = (1-\varepsilon)\,y_i + \frac{\varepsilon}{K}$$

With `ε = 0.1` and `K = 1000`, the correct class gets 0.9001 and every other class 0.0001.

## Why it helps

With a one-hot target, cross-entropy is minimised only as `q_correct → 1`, which requires the correct
logit to go to `+∞`. The gradient never reaches zero, so training keeps pushing logits apart forever.
That produces three problems: overconfidence, large logit magnitudes that hurt numerical stability,
and overfitting to label noise (a mislabelled example is pushed toward certainty just as hard as a
correct one).

Label smoothing sets a finite optimum. The loss is minimised at a specific finite logit gap, so the
pressure stops:

```
   ONE-HOT TARGET                    SMOOTHED TARGET (ε = 0.1)
   ──────────────                    ─────────────────────────
   optimum: q_correct = 1.0          optimum: q_correct = 0.9
   → logit gap → ∞                   → logit gap = log(0.9K/0.1) ≈ finite
   → training never stops pushing    → gradient reaches zero. Done.

   representation effect: classes form tight equidistant clusters
```

[Müller et al. (2019)](https://arxiv.org/abs/1906.02629) showed it also reshapes the penultimate
layer: examples cluster tightly around their class centroid and equidistantly from other classes,
rather than spreading out. Better calibration and cleaner class separation follow from that geometry.

## Where it wins

* **Image classification** — near-universal in modern recipes; small but consistent accuracy gains.
* **Machine translation** — `ε = 0.1` is standard, and was in the original Transformer paper. Note
  the paper's own observation: it *hurts* perplexity while *improving* BLEU, since the model is
  deliberately less certain but makes better choices.
* **Calibration** — usually improves ECE (question 063).
* **Noisy labels** — reduces the damage from mislabelled examples.

## Where it hurts

This is what the question is really asking.

**1. Distillation.** The important case. Label smoothing **erases the dark knowledge** (question 031)
that makes a teacher useful. It forces all wrong classes toward the *same* small value, destroying
the relative structure — the information that "Charmander is more confusable with Charmeleon than with
Squirtle" — which is precisely what a student learns from. Müller et al. measured this: a
smoothing-trained teacher makes a *worse* teacher despite being a better classifier.

**2. When you need well-separated logits** for downstream use — retrieval, thresholding on raw scores,
or anything reading logit margins.

**3. Fine-grained tasks with genuine hierarchy.** Uniform smoothing asserts all wrong classes are
equally wrong, which is false when some are near-synonyms.

**4. LLM pretraining.** Rarely used. The target distribution over next tokens is already genuinely
uncertain, the vocabulary is enormous (so `ε/K` is negligible), and it distorts the likelihood the
model is meant to estimate.

**5. Where calibrated probabilities matter downstream.** It deliberately biases probabilities away
from confidence, which is a distortion if you feed them into a cost calculation.

## What an interviewer digs into next

* Why does one-hot cross-entropy push logits toward infinity?
* Explain concretely why label smoothing hurts distillation.
* Why does it improve BLEU while worsening perplexity?
* Why is it rare in LLM pretraining?
