---
id: "099"
slug: ml-system-design
style: serious
category: system-design
difficulty: advanced
question: "Walk me through designing a recommendation system end to end."
tags: [system-design, recommender, retrieval-ranking, two-tower, cold-start]
---

# Designing a recommendation system

The interview is testing whether you **frame** before you build. Spend the first minutes on the
problem, not the model.

## 1. Clarify and scope

* **What are we optimising?** Engagement, revenue, retention, creator health, time well spent? These
  conflict. A system optimised for watch time is not the same product as one optimised for
  satisfaction.
* **Scale?** 10k items or 100M? 1k users or 1B? This decides the entire architecture.
* **Latency budget?** 100 ms end to end changes what is feasible.
* **Cold start?** New users, new items, or both.
* **What signals exist?** Explicit ratings are rare and biased; implicit signals (clicks, dwell,
  completion) are abundant and noisy.

## 2. Metrics, in three layers

| Layer | Examples |
| --- | --- |
| **Online (the decision)** | CTR, conversion, session length, retention, revenue |
| **Offline (the proxy)** | Recall@k, NDCG@k, MAP, calibration |
| **Guardrails** | diversity, novelty, catalogue coverage, p99 latency, creator-side fairness |

Guardrails matter more here than in most systems: a recommender that maximises CTR converges to a
narrow, sensational, homogeneous feed, and the damage shows up in retention months later, long after
the A/B test declared victory.

## 3. The architecture

```
   100,000,000 items
          │
   ┌──────▼──────────────────────────────────┐  ① CANDIDATE GENERATION  ~10 ms
   │  several parallel sources:              │     optimise RECALL
   │   • two-tower ANN retrieval             │     cheap per item
   │   • collaborative filtering / ALS       │
   │   • trending / popular                  │
   │   • recently viewed, followed creators  │
   └──────┬──────────────────────────────────┘
       ~1000 candidates
   ┌──────▼──────────────────────────────────┐  ② RANKING              ~50 ms
   │  heavy model: GBDT or DLRM/DIN          │     optimise PRECISION
   │  rich cross-features, user history,     │     expensive per item
   │  multi-task heads (click, like, share,  │
   │  complete, hide)                        │
   └──────┬──────────────────────────────────┘
        ~100 scored
   ┌──────▼──────────────────────────────────┐  ③ RE-RANKING            ~5 ms
   │  business rules, diversity (MMR),       │
   │  deduplication, freshness, ad blending, │
   │  policy filters                         │
   └──────┬──────────────────────────────────┘
        20 shown
```

The **funnel** is the core idea, and the reason is the same as in RAG (question 046): spend more
compute per item as the candidate set shrinks. Stage 1 must be cheap enough for 100M items; stage 2
can afford a heavy model on 1000.

**Two-tower retrieval:** a user encoder and an item encoder trained so that dot product approximates
relevance. Item embeddings are precomputed and indexed with ANN; the user embedding is computed at
request time. Crucially the towers **cannot interact** before the dot product — which is exactly the
bi-encoder tradeoff, and exactly why you need a ranking stage that *can* cross features.

## 4. Training

* **Negative sampling** is the central design decision. Implicit feedback gives you positives only;
  where negatives come from — random items, in-batch negatives, impressed-but-not-clicked — determines
  what the model learns. Impressed-not-clicked negatives are informative but biased by the current
  system.
* **Position bias.** Item 1 gets clicked because it is first. Correct with a position feature at
  training that is fixed at inference, or with inverse propensity weighting.
* **Multi-task heads** for click, like, share, complete, hide, combined with tuned weights.
  Single-objective recommenders optimise clickbait.
* **Retraining cadence:** ranking daily or hourly; embeddings can be less frequent; near-real-time
  features for session context.

## 5. Cold start

* **New item:** content-based features (text, image embeddings) until interaction data accrues;
  explicit exploration budget.
* **New user:** popularity by segment, onboarding preferences, and rapid adaptation from
  session-level signals.
* **Exploration** generally: some ε-greedy or bandit budget, or the system only ever learns about
  what it already shows — the feedback loop from question 095.

## 6. Serving and operations

Precompute item embeddings, keep the ANN index warm, cache user embeddings with a short TTL, log every
impression with its features (question 098), and monitor per-segment. Kill-switch and instant
rollback for a bad model.

## What an interviewer digs into next

* Why can't you run the ranking model over all 100M items?
* Where do negatives come from, and what bias does each choice introduce?
* How do you correct position bias?
* How do you stop the feedback loop from narrowing the catalogue?
