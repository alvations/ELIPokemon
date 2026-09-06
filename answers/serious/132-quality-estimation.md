---
id: "132"
slug: quality-estimation
style: serious
category: translation
difficulty: advanced
question: "How do you tell whether a translation is good without a reference?"
tags: [quality-estimation, comet-qe, calibration, routing, critical-errors, mqm]
---

# Quality estimation: judging a translation with no reference

Every metric in question 129 needs a human reference translation. In production you have none —
that is the whole reason you ran the system. **Quality estimation (QE)** predicts how good a
translation is from the source and the output alone, at run time, on the segment you are about to
ship.

## Why it is worth the trouble

QE is not an evaluation nicety; it is a control mechanism.

```
   source ─► MT system ─► candidate ─► QE score
                                          │
                    ┌─────────────────────┼─────────────────────┐
                 high                   middle                 low
                    │                     │                     │
              publish as-is       route to a human       route to a stronger
                                   for post-editing       (costlier) system,
                                                          or refuse to publish
```

That routing is where the money is. Human post-editing is expensive; QE lets you spend it on the
20% of segments that need it instead of the 100%. It also lets you gate genuinely dangerous output
in medical, legal and safety contexts.

## How QE systems work

**Sentence-level.** A regression model over (source, hypothesis) predicting a human quality score.
COMET-QE and CometKiwi are the standard: a cross-lingual encoder embeds both sides, and a head
trained on human judgements (direct assessment or MQM) outputs a score. Trained on the same human
data as reference-based COMET, minus the reference.

**Word-level.** Tag each output token OK/BAD, and often each source token as
contributing-to-an-error. Far more useful for a post-editor, who wants to know *where* to look,
and harder to train.

**LLM-as-judge.** Prompt a strong model with source and hypothesis and ask for an MQM-style error
analysis. GEMBA-MQM and similar do this and are competitive with trained QE models. Inherits every
LLM-judge caveat from question 038 — position bias, self-preference, verbosity bias — plus one
specific to translation: it is weakest exactly on the low-resource languages where you most need
it.

**Uncertainty from the model itself.** Sequence log-probability, entropy, or variance across
sampled/dropout decodes. Free, and much weaker than a trained QE model — a fluent hallucination
has *high* confidence, which is precisely the case you needed to catch.

## Calibration matters more than correlation

A QE model that ranks segments perfectly but whose scores mean nothing absolute cannot drive a
threshold. For routing you need calibration: "score 0.8" must mean the same thing on Monday and on
a new domain on Friday.

Practical consequences:

* **Set thresholds per language pair and per domain**, from a held-out set with human labels. A
  single global threshold will over-trust some pairs and over-review others.
* **Re-validate after any MT system change.** QE scores shift when the thing they are judging
  shifts distribution.
* **Report precision/recall at the operating point**, not just correlation with human scores. The
  business question is "what fraction of the segments I published were actually bad", and
  correlation does not answer it.

## Critical errors are a separate problem

A dropped negation, a reversed dosage, a swapped name, toxic content inserted. These are rare, so
they barely affect a correlation-based evaluation — and they are the entire reason you deployed QE.

Treat critical-error detection as its own **classification** task with its own recall target, not
as the tail of a regression. Build a targeted test set (negation flips, number swaps, entity
substitutions, omission of whole clauses) and measure recall on it directly. A QE model with a
0.85 correlation and 40% recall on dropped negations is not fit for a medical pipeline, and the
0.85 will not tell you that.

## Known weaknesses

* **Fluency bias.** QE models over-reward fluent output; a fluent mistranslation scores better than
  a clumsy correct one. Same failure as human raters skimming.
* **Length and domain sensitivity.** Very short segments (UI strings, single words) are scored
  unreliably.
* **Hallucination detection is weak** without explicit training for it.
* **Low-resource languages** are worst served, again.

## What an interviewer digs into next

* Why is model log-probability a poor QE signal?
* Why is calibration more important than correlation for routing?
* Why must critical-error detection be evaluated separately?
* What is fluency bias and how would you test for it?
