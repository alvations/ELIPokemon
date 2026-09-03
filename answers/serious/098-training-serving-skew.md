---
id: "098"
slug: training-serving-skew
style: serious
category: mlops
difficulty: intermediate
question: "What is training-serving skew and how does a feature store help?"
tags: [training-serving-skew, feature-store, point-in-time, leakage, mlops]
---

# Training-serving skew

Any difference between how features are computed at training time and at serving time. The model was
fit on one distribution and is asked to predict on another, and the failure is **silent** — no error,
no exception, just quietly degraded predictions.

## The four flavours

**1. Implementation skew.** Training features are computed in a Python/Spark batch job; serving
features in a Java/Go online service. Two implementations of "average order value over 30 days" that
disagree on timezone handling, null semantics, or rounding.

**2. Data skew.** The offline warehouse has late-arriving, corrected, deduplicated data. The online
store has whatever arrived in the last second. Same query, different answer.

**3. Time-travel skew (the worst).** Training accidentally uses information that would not have been
available at prediction time.

```
   ❌ WRONG — computed with today's data
   prediction date: 2026-01-15
   feature "lifetime_order_count" computed: 2026-09-01  ← includes 8 months
                                                           of the FUTURE
   The model learns to rely on a number it will never see in production.

   ✅ RIGHT — point-in-time correct
   for each training row, compute every feature using ONLY data with
   timestamp ≤ that row's prediction timestamp.
```

This is the most damaging and the hardest to detect, because it produces **excellent offline metrics**
and a model that fails in production. Suspiciously good validation scores are the symptom (question
065).

**4. Feedback-loop skew.** The model's own predictions change future data. A fraud model that blocks
transactions never observes their outcomes, so the next training set is biased by the current model's
decisions.

## What a feature store provides

```
   ┌────────────────── FEATURE DEFINITION (written ONCE) ─────────────────┐
   │   avg_order_value_30d = mean(orders.amount) over 30-day window       │
   └───────────────┬──────────────────────────────┬───────────────────────┘
                   ▼                              ▼
     ┌─────────────────────────┐      ┌─────────────────────────┐
     │ OFFLINE STORE           │      │ ONLINE STORE            │
     │ warehouse / parquet     │      │ Redis / DynamoDB        │
     │ point-in-time joins     │      │ low-latency key lookup  │
     │ → training data         │      │ → serving               │
     └─────────────────────────┘      └─────────────────────────┘
              same definition, same code path, two access patterns
```

The central guarantee is **one definition, two access patterns**. Concretely it supplies:

* **Point-in-time correct joins** — the core feature, and the thing that is genuinely hard to build
  yourself. Given a set of (entity, timestamp) rows, return the feature values as they were at each
  timestamp.
* **A shared registry** so features are discoverable and reusable across teams.
* **Consistency guarantees** between offline and online paths.
* **Monitoring** of freshness and distribution per feature.

## When you do not need one

Feature stores are heavy infrastructure. You can get most of the benefit without one by:

* Putting all transformations **inside the model artifact** (an sklearn Pipeline, a TF transform
  graph) so training and serving physically share code.
* **Logging features at serving time** and training on those logged features — which makes skew
  structurally impossible, because the training data *is* the serving data. This is the single most
  effective and most under-used technique available.
* Computing features from a single source of truth with one implementation.

The logging approach deserves emphasis: it eliminates flavours 1, 2 and 3 at once, requires no new
infrastructure, and costs only storage.

## Detecting skew

* Compare feature distributions offline vs online for the same entities — the direct test.
* Shadow-score production traffic with the training pipeline and diff the outputs.
* Assert on feature freshness and null rates in serving.
* Treat an unexplained offline/online performance gap as skew until proven otherwise. It usually is.

## What an interviewer digs into next

* What is a point-in-time correct join and why is it hard?
* Why does time-travel skew produce excellent offline metrics?
* How does logging serving features eliminate skew?
* When is a feature store not worth the operational cost?
