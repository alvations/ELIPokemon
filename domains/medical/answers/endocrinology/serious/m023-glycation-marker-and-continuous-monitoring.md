---
id: "m023"
slug: glycation-marker-and-continuous-monitoring
style: serious
category: endocrinology
difficulty: intermediate
question: "What does glycated haemoglobin measure that a spot glucose cannot, and where does it mislead?"
tags: [hba1c, monitoring, continuous-glucose, variability, red-cell-turnover]
---

# A spot glucose is a sample. A glycation marker is an integral. Neither is the trace.

Glucose reacts non-enzymatically with haemoglobin inside the red cell, and because the reaction is
slow and effectively irreversible over the cell's life, the glycated fraction accumulates in
proportion to how much glucose the cell has been exposed to and for how long *(mechanism)*. That
is the whole basis of the measurement: the red cell is a passive integrator, carrying a record
nobody had to write down. A spot glucose cannot do that, because a single sample of a variable
that swings through the day carries almost no information about the mean. The glycation marker
also cannot do something a spot glucose can, which is tell you what is happening now.

Claims below are marked *(mechanism)*, *(consensus)* or *(guideline-dependent)* where the basis is
load-bearing.

## Why the integral is weighted, and what that weighting costs

The red cell population is a mixture of ages, continually replaced. The oldest cells carry the
most glycation but there are fewer of them left; the youngest carry the least. The resulting
average is therefore weighted toward recent exposure rather than being a flat mean over the cell's
whole lifespan *(mechanism)*. The practical consequence is that the marker moves, but slowly, and
lags a genuine change in control by weeks — so repeating it too soon measures mostly the period
you have already measured *(consensus)*; how soon is too soon is set by local guidance
*(guideline-dependent)*.

```
   WHAT EACH ONE SEES
   ──────────────────
   true glucose      ╭─╮      ╭──╮          ╭─╮        ╭──╮
   through the day  ─╯ ╰─╮  ╭─╯  ╰╮   ╭────╯ ╰─╮   ╭──╯  ╰──
                         ╰──╯     ╰───╯        ╰───╯
                      ▲        ▲                        ▲
   spot checks        │        │                        │   three values. three
                      ●        ●                        ●   different conclusions.

   glycation marker  ════════════════════════════════════   one number for the
                     weighted to the recent end            whole window

   continuous trace  ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿   the shape, the rate,
                     ░░ time low ░░        ░░ time low ░░   and the direction


   THE FAILURE THE INTEGRAL CANNOT SEE
   ───────────────────────────────────
   person A    ─────────────────────────────────   steady, inside range
   person B    ╱╲    ╱╲      ╱╲    ╱╲    ╱╲        swinging high and low
               ╲╱▂▂▂▂╲╱▂▂▂▂▂▂╲╱▂▂▂▂╲╱▂▂▂▂╲╱▂▂▂    with hypoglycaemia in
                                                   every trough
               ╰── identical glycation marker ──╯
```

## What it misses

**Variability, and therefore hypoglycaemia.** The marker is an average, and an average is blind to
the distribution that produced it. A record with large swings and one that is steady can integrate
to the same value, and the swinging one contains lows the number does not report *(mechanism)*.
This is the single most important limitation, because the harm from a low is immediate and the
marker that looks reassuring is averaging it away.

**Pattern and timing.** Overnight drift, post-meal spikes, the effect of exercise and the shape of
a dawn rise are all invisible in an integral. The clinical question is usually *when* and *why*,
and the integral answers neither.

**The recent few days.** By construction it is weighted but slow, so a change made last week is
largely not in it yet *(mechanism)*.

## Where it misleads

Everything above assumes the integrator behaves normally. The marker is a property of haemoglobin
inside red cells, so anything that changes red-cell lifespan, red-cell production, or the
haemoglobin molecule itself alters the result without any change in glucose at all *(mechanism)*.
The categories, rather than a list to memorise:

* **Shortened red-cell survival or increased production** gives a population skewed young, with
  less accumulated glycation, and reads low relative to the true mean — haemolysis, recent blood
  loss, states of brisk reticulocytosis, some drug-induced haemolysis, and the later stages of
  pregnancy *(consensus)*.
* **Lengthened survival or reduced production** gives an older population and reads high — iron
  deficiency and other deficiency anaemias before treatment, and absence of the spleen
  *(consensus)*.
* **Recent transfusion** replaces part of the population with cells carrying somebody else's
  exposure history. The record is no longer a record of this person *(mechanism)*.
* **Haemoglobin variants and raised fetal haemoglobin** interfere in a way that depends on the
  assay method — some are affected, some are not — so the correct question is which method the
  laboratory runs *(guideline-dependent)*.
* **Kidney disease, and dialysis in particular**, affects both red-cell turnover and, with some
  methods, the assay itself *(consensus)*.

There is also a quieter issue: at the same mean glucose, measured glycation differs between
individuals and between populations more than measurement error explains, and the mechanism and
clinical significance of that difference remain contested *(consensus, with genuine
disagreement)*. Treat a single value near a decision point as a measurement with a confidence
interval, not as a fact.

## The decisions taken on it are thresholds, and thresholds are not properties of the molecule

A continuous quantity gets hard lines drawn across it, and crossing one changes what happens next:
a diagnosis is made, a therapy is started or intensified, a surveillance interval changes. Three
things follow and they are routinely conflated. The **value** of each line is a consensus decision
that differs between guideline bodies and is revised *(guideline-dependent)*. The **direction of
interpretation** is contextual — the same measurement is weighed differently in a young person
with decades of exposure ahead, in frailty, in advanced kidney disease and in pregnancy, where
separate criteria and separate measurements apply *(consensus)*. And the **measurement itself**
carries a spread, so a result sitting on a line is not evidence that the person is on the line.
None of that is a property of glycated haemoglobin. It is a property of the decisions people have
agreed to attach to it, which is why the threshold is looked up rather than remembered.

## Why continuous monitoring changed the questions

A sensor in the subcutaneous tissue reports interstitial glucose continuously. The convenience is
obvious and is the least interesting part. What changed is that a continuous record makes
previously unaskable questions answerable: what fraction of the day is spent inside the intended
range, what fraction below it, how variable the trace is, and — uniquely — *which direction it is
moving right now* *(consensus)*. A rate of change is information no spot measurement contains at
all, and it is what allows a decision to be made before the problem arrives rather than after
*(mechanism)*.

The consequences run further than the clinic. Overnight lows that nobody was awake to measure
became visible. Variability became a described quantity rather than an impression. And review
shifted from a single number discussed at an appointment to a shape discussed with the person who
lived it.

The limitations are real and follow from the same mechanism. Interstitial glucose trails plasma
glucose during rapid change, so the sensor is least accurate exactly when the trace is most
interesting *(mechanism)*. Pressure on a sensor can produce an artefactual low. Some substances
interfere with some sensors, which is a per-device question answered by the manufacturer's
instructions *(guideline-dependent)*. Alarms fatigue. And a continuous record generates far more
data than a consultation can absorb, so the summary metrics are only useful if everyone agrees
what they mean. Published consensus targets for those metrics exist and differ by population and
by document; local guidance is the authority and **no target values appear here**
*(guideline-dependent)*.

Used together the division of labour is clean: the integral for the long view, the trace for the
pattern and the direction, and a confirmatory blood glucose where the device's instructions or
local policy require one.

## The human stakes, said plainly

Two measurements, and both of them get used as something other than measurements.

A single glycation value has become, in a great many consultations, a proxy for whether someone
has been good. That is a misuse of a number with a confidence interval, an interference profile
and a dependence on red-cell biology that has nothing to do with anybody's effort. The same misuse
runs in the other direction and is more dangerous: a value that looks reassuring can be the
average of a trace that goes dangerously low every night, and the harm from those lows is
immediate while the number that concealed them is not.

Continuous monitoring makes self-management visible, which helps, and also makes it surveillable,
which can be used to judge. A trace shared in a consultation is a record of somebody's nights,
meals, illnesses, work shifts and mistakes. It deserves to be read as information about a
condition rather than as evidence about a person, and the reason to say so is that it is
frequently not.

A note about who is reading. Someone reading about glucose monitoring is more likely to be living
with it than revising it. If that is you: there are deliberately no target values on this page,
because the published ones are population agreements that differ between documents, and what
applies to you is set with your own clinical team. A reading that worries you is a reason to
contact them, not a reason to act on anything written here.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* Your national diabetes guideline's sections on monitoring and on glycaemic targets, from the
  body that issues it, which is the authority on any target value and on how often to measure.
* The American Diabetes Association's annual standards of care document, for its chapter on
  glycaemic assessment and monitoring technology.
* The consensus statements of the Advanced Technologies and Treatments for Diabetes meetings, for
  the agreed continuous-glucose metrics and how they are defined.
* The International Federation of Clinical Chemistry's reference material on standardising the
  glycated haemoglobin measurement, and the question of which reporting units your laboratory
  uses.
* Your own laboratory's handbook: which assay method it runs, which haemoglobin variants that
  method is affected by, and what it says about results in kidney disease.
* The manufacturer's instructions for the specific continuous sensor in use, for its accuracy
  claims, interfering substances and confirmatory-testing requirements.

## Scope and safety

This explains what two kinds of measurement can and cannot show. It is not a monitoring protocol
and not about any individual's care. **No thresholds, target ranges or reporting values appear
here**, because they differ between guidelines, between reporting units and between populations,
and they are revised. Local guidance and the laboratory handbook are the authorities. Nothing here
has had clinical review. If someone is unwell now, contact local emergency services.

## What an examiner digs into next

* Why is the glycation marker weighted toward recent exposure rather than flat across the red
  cell's life?
* Which direction does the marker move in iron deficiency, and why?
* What can a rate of change tell you that no single value can?

## Where this stands, October 2026

The mechanism — glucose integrated by a cell population with a lifespan — is settled and will not
change. The reporting units, the assay interference profiles, the consensus metrics for continuous
monitoring and every target value attached to any of it are current agreements, and they move.
Check the document, not a remembered figure.
