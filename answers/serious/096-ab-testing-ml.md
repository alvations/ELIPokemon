---
id: "096"
slug: ab-testing-ml
style: serious
category: mlops
difficulty: intermediate
question: "How do you A/B test a machine learning or LLM feature?"
tags: [ab-testing, experimentation, power-analysis, novelty-effect, guardrails]
---

# A/B testing an ML feature

Offline metrics tell you whether the model is better at its proxy task. An A/B test tells you whether
the *product* is better. Those come apart constantly — a model with higher AUC can reduce revenue,
and a model that "looks worse" offline can win because it is faster.

## The essentials

**Randomise at the right unit.** User, not request — otherwise the same user experiences both arms
and their behaviour contaminates both. If effects spill between users (marketplaces, social feeds),
randomise at the cluster level: geography, seller, community.

**Define metrics before you launch**, in three tiers:

```
   ① PRIMARY (one, chosen in advance)   the decision metric
   ② SECONDARY                          mechanism — helps explain the primary
   ③ GUARDRAILS                          latency, error rate, cost, safety,
                                         complaints — must not regress
```

The guardrail tier is what stops you shipping a model that improves click-through and doubles p99
latency.

**Do the power calculation first.**

$$n \approx \frac{16\sigma^2}{\delta^2} \quad \text{per arm, for 80\% power at } \alpha = 0.05$$

The lesson people take away is that **small effects need enormous samples**: halving the effect size
you want to detect quadruples the sample needed. If you cannot reach that `n`, the honest conclusion
is that you cannot run this test, not that you should run it underpowered and squint at the result.

## The traps

* **Peeking.** Checking daily and stopping when significant inflates the false positive rate
  dramatically. Either fix the duration in advance, or use sequential testing designed for continuous
  monitoring.
* **Novelty and primacy effects.** New things get clicked because they are new; existing users are
  disrupted by change. Both decay over 1–2 weeks. Run at least one full weekly cycle, and check
  whether the effect is stable over time rather than trending toward zero.
* **Multiple comparisons.** Twenty metrics at `p < 0.05` gives one false positive per experiment by
  construction. Pre-register the primary metric.
* **Sample ratio mismatch.** If the 50/50 split is actually 50.4/49.6, your randomisation is broken
  and every result is suspect. Check this **first**, always — it invalidates the whole experiment and
  is easy to miss.
* **Feedback loops.** A recommender in the treatment arm changes what users see, which changes future
  training data. Long-running experiments on recommenders are not measuring a static effect.

## LLM-specific complications

* **High variance in output quality** means larger samples than a typical UI test.
* **Cost and latency are first-class guardrails**, not afterthoughts — an LLM feature can be better
  and unaffordable.
* **Quality is hard to measure automatically.** Combine implicit signals (regeneration rate,
  copy rate, thumbs-down, conversation length, escalation to a human) with sampled human or
  LLM-judge review.
* **Non-determinism** means the same user can get different outputs on the same request; that is
  within-arm variance, not a bug.
* **Prompt and model changes are entangled.** Change one thing per experiment.

## When you cannot A/B test

* **Interleaving** for ranking — show results from both models blended in one list and compare which
  get clicked. Far more sensitive than a split test, so it needs far less traffic.
* **Shadow deployment** — run the new model on live traffic without serving it, comparing predictions
  and latency. Catches operational problems with zero user risk, but measures nothing about user
  behaviour.
* **Switchback tests** for marketplace effects, alternating globally over time windows.
* **Offline replay** against logged decisions, with importance weighting.

## What an interviewer digs into next

* Why randomise on user rather than request?
* What is a sample ratio mismatch and why check it first?
* How do you handle novelty effects?
* You cannot get enough traffic for significance. What now?
