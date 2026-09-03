---
id: "095"
slug: data-drift
style: serious
category: mlops
difficulty: core
question: "What are data drift and concept drift, and how do you monitor for them?"
tags: [drift, monitoring, psi, kl-divergence, retraining]
---

# Drift

Models are trained on a snapshot and deployed into a moving world. Performance decays. The
distinctions matter because the fixes differ.

| Type | What changes | Example | Fix |
| --- | --- | --- | --- |
| **Covariate / data drift** | `P(X)` | a marketing campaign brings younger users | retrain, or reweight |
| **Concept drift** | `P(Y\|X)` | the *same* user behaviour now means something different post-pandemic | **retrain — mandatory** |
| **Label drift** | `P(Y)` | fraud rate rises from 0.1% to 1% | recalibrate thresholds |
| **Upstream data drift** | the pipeline | a field changes units; nulls become empty strings | fix the pipeline |

Only concept drift necessarily degrades accuracy: `P(X)` can shift while `P(Y|X)` holds, and a
well-generalising model is fine. Reacting to every covariate shift is a common source of unnecessary
retraining.

That last row deserves emphasis: in practice, **most "drift" alerts are broken pipelines**, not
genuine world change. Check the pipeline before theorising about the world.

## Monitoring, in priority order

```
   ① MODEL PERFORMANCE  ← the ground truth, when labels arrive
        accuracy, AUC, business KPI, per segment
        ❌ labels are often delayed by days or months
   ② PREDICTION DRIFT   ← free, immediate, no labels needed
        the distribution of model OUTPUTS over time
        a shift here is the earliest real signal you can get
   ③ INPUT DRIFT        ← per feature, and jointly
        PSI, KL divergence, Kolmogorov-Smirnov, embedding distance
   ④ DATA QUALITY       ← check first when something fires
        null rates, cardinality, ranges, schema, freshness
```

**Population Stability Index** is the industry standard for input drift:

$$\text{PSI} = \sum_i (\text{actual}_i - \text{expected}_i)\ln\frac{\text{actual}_i}{\text{expected}_i}$$

with conventional thresholds `< 0.1` stable, `0.1–0.25` moderate, `> 0.25` significant.

**Prediction drift is the most under-used signal.** It requires no labels, is available immediately,
and directly reflects what the model is doing. If your average predicted probability moved from 0.12
to 0.31 overnight, something is wrong, and you know before any label arrives.

## Practical guidance

* **Segment everything.** Aggregate metrics hide the failure. A model can be stable overall while
  collapsing for new users, one region, or one device type.
* **Beware multiple testing.** Monitoring 500 features at p < 0.05 gives ~25 false alarms per run.
  Use effect-size thresholds (like PSI) rather than raw p-values, which are also over-powered on
  large samples — with a million rows, everything is "significantly" different.
* **Choose a retraining trigger deliberately:** scheduled (simple, predictable, possibly wasteful),
  performance-triggered (correct, needs labels), or drift-triggered (fast, noisy). Most mature teams
  run scheduled retraining plus performance alerting.
* **Keep a reference window** — a frozen training distribution snapshot — and version it alongside
  the model.
* **Log predictions and features at inference time**, or you cannot investigate anything later. This
  is the piece teams most often skip and most regret.

## The LLM-specific version

Prompt/input drift (users ask new things), tool and API changes, model version changes from a
provider, and eval-set staleness. The monitoring analogue is tracking the distribution of request
embeddings, refusal rates, response lengths, and user feedback — the same discipline, different
instruments.

## What an interviewer digs into next

* Which kind of drift necessarily degrades accuracy, and which might not?
* Why is prediction drift more useful than input drift in practice?
* Why are p-values a bad drift threshold at scale?
* How would you design a retraining trigger with 60-day label delay?
