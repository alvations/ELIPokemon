---
id: "100"
slug: fairness-bias-privacy
style: serious
category: responsible-ai
difficulty: intermediate
question: "How do you think about fairness, bias, and privacy in an ML system?"
tags: [fairness, bias, privacy, differential-privacy, impossibility, memorisation]
---

# Fairness, bias, and privacy

## Fairness has no single definition — and cannot

The most important technical fact in this area: the common fairness criteria are **mathematically
incompatible**.

| Criterion | Requires |
| --- | --- |
| **Demographic parity** | equal positive *rates* across groups |
| **Equalised odds** | equal TPR and FPR across groups |
| **Equal opportunity** | equal TPR across groups |
| **Calibration** | a score of 0.7 means 70% for every group |
| **Individual fairness** | similar individuals treated similarly |

[Kleinberg et al. (2016)](https://arxiv.org/abs/1609.05807) and Chouldechova proved that unless base
rates are equal across groups or the classifier is perfect, **you cannot satisfy calibration and
equalised odds simultaneously**. This is not an engineering limitation to be optimised away — it is a
theorem.

The consequence: *"make the model fair"* is not a well-posed request. Someone must choose which
criterion applies, and that is a **normative decision about the domain**, not a technical one. The
COMPAS recidivism debate was exactly this: ProPublica's analysis (unequal false positive rates) and
Northpointe's response (equal calibration) were both correct, about different criteria.

The right answer in an interview is to say this explicitly, then ask what the harm is: a false
positive in hiring means a wrongly rejected candidate; in medical screening it means an unnecessary
test. Different harms, different criteria.

## Where bias enters

```
   ① HISTORICAL   the world is biased, the data records it faithfully
   ② SAMPLING     some groups under-represented in collection
   ③ LABELLING    annotator bias; proxy labels ("arrested" ≠ "committed a crime")
   ④ FEATURES     proxies for protected attributes — postcode, name, school
   ⑤ MODELLING    optimising average accuracy sacrifices minority groups
   ⑥ DEPLOYMENT   thresholds, differential access, feedback loops
```

Removing the protected attribute does **not** work — "fairness through unawareness" fails because
correlated proxies remain, and it removes your ability to *measure* disparity. You generally need the
attribute to audit, even if the model does not use it.

Mitigations sit at three points: **pre-processing** (reweighting, resampling), **in-processing**
(fairness constraints, adversarial debiasing), **post-processing** (group-specific thresholds — often
the most effective and the most legally fraught).

## Privacy

**Memorisation is real.** Models reproduce verbatim training data — the more so for duplicated
sequences, which is why deduplication is the highest-leverage privacy intervention available and also
improves quality. **Membership inference** attacks determine whether a record was in the training set;
**extraction** attacks recover the record itself.

**Differential privacy** is the rigorous defence: the output distribution changes by at most `e^ε`
whether or not any individual's record is included. DP-SGD achieves it by clipping per-example
gradients and adding calibrated noise. It gives a real guarantee and costs real accuracy — the
tradeoff is genuine, and small `ε` (strong privacy) hurts, disproportionately on under-represented
groups, which is an uncomfortable interaction between the two halves of this question.

**Federated learning** keeps raw data on devices and shares updates — useful, but gradients leak
information, so it needs DP or secure aggregation to be a real privacy control rather than a
reassuring architecture.

Practical measures: PII detection and redaction before training, deduplication, data minimisation,
retention limits, canary insertion to *test* for memorisation, and honest documentation.

## Process

Technical fixes are secondary to process. **Disaggregated evaluation** — reporting metrics per group
rather than in aggregate — is the single highest-value practice, because aggregate metrics hide
exactly the failures you are looking for. Add model cards, datasheets, diverse review, and a
documented appeals path.

## What an interviewer digs into next

* Why can't calibration and equalised odds hold simultaneously?
* Why does removing the protected attribute fail?
* What does `ε` mean in differential privacy?
* Why does deduplication help both privacy and quality?
