---
id: "171"
slug: human-evaluation-translation
style: serious
category: translation
difficulty: intermediate
question: "How do you run a human evaluation of translation quality properly?"
tags: [mqm, human-evaluation, rater-training, agreement, statistical-power, crowd-vs-expert]
---

# Running a human evaluation that means something

Every automatic metric in question 129 is validated against human judgement. That makes human
evaluation the foundation of the whole edifice — and it is routinely run in ways that produce
numbers with no information in them.

## Who rates matters more than how many

The single most consequential finding in this area: **crowd raters and professional translators do
not agree**, and where they disagree, the crowd is wrong in a specific direction.

```
   given a fluent translation with an ACCURACY error
   (a dropped negation, a swapped number, an omitted clause):

   crowd rater, target-language only ─► reads well. High score.
                                        They cannot see the error — they
                                        never had the source.
   professional, source + target     ─► major accuracy error. Low score.
```

Crowd evaluation without the source measures **fluency**, and calls it quality. Since modern systems
are almost always fluent, that evaluation cannot distinguish the systems you care about
distinguishing. If you take one thing from this: **raters must see the source, and must be able to
read it.**

## MQM rather than a 1-5 scale

Direct Assessment (rate this 0-100) is cheap and noisy. **MQM** (question 129) asks raters to mark
**error spans** with a category and a severity, and derives the score from the marks. It is better
for reasons that are practical rather than theoretical:

* Marking a specific span is a **more reliable judgement** than choosing a number on a scale.
* You get a **diagnosis**, not just a verdict — which error categories dominate, and where.
* **Severity weighting** lets a critical error count as critical (question 132) rather than being
  averaged into mildness.
* Inter-rater agreement is measurable at the span level, so you can tell whether your protocol works.

The cost is real: MQM needs trained annotators and roughly three to five times the time per segment
of a rating scale. Budget for it or do not claim you ran a proper evaluation.

## Protocol details that decide whether the result is usable

* **Train and calibrate raters** on a shared set with a discussed gold standard before the real
  work. Skipping this is the commonest cause of unusable data.
* **Measure agreement** and report it. Low agreement means your instrument is not measuring
  anything, and the result should be discarded rather than published.
* **Randomise and blind system identity**, and interleave systems within a document rather than
  showing one system's whole output — raters anchor hard.
* **Give document context.** Segment-level rating cannot see the phenomena in question 131, so a
  document-level system will not be rewarded for the thing it does better.
* **Include quality controls** — known-bad and known-good items — and report how raters did on them.
* **Power the study.** Twenty segments cannot distinguish two good systems. Run a power calculation
  on your expected effect size, or accept that a null result means nothing.
* **Pay properly.** Underpaid raters rush, and rushing shows up as noise that no analysis removes.

## Reporting

Report the protocol, the number and qualification of raters, agreement statistics, the significance
test, and the confidence interval. A quality claim without those is an assertion. Publish the
per-category MQM breakdown, not just the aggregate — that breakdown is where the actionable
information lives.

## What an interviewer digs into next

* Why does crowd evaluation systematically miss accuracy errors?
* Why is marking a span more reliable than choosing a score?
* What does low inter-rater agreement tell you, and what should you do?
* Why interleave systems within a document rather than rating them separately?
