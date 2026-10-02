---
id: "m041"
slug: therapeutic-drug-monitoring
style: serious
category: pharmacology
difficulty: advanced
question: "Which drugs are monitored by plasma concentration rather than by effect, what has to be true before a concentration can be interpreted, and what does a trough actually tell you?"
tags: [therapeutic-drug-monitoring, trough, steady-state, protein-binding, assay]
---

# Concentration monitoring is the third choice, used where the first two are unavailable.

There is a hierarchy, and therapeutic drug monitoring sits at the bottom of it. Where you can
measure the **outcome**, measure the outcome. Where you cannot but can measure the **effect**,
measure the effect — a clotting time for an anticoagulant, a blood pressure for an
antihypertensive, a glucose for insulin. Only where neither is available do you fall back on
measuring the **concentration**, which is a surrogate for a surrogate: it tells you how much drug
is in the plasma, not how much is at the receptor and not whether the person is better.

Saying it that way round fixes the two commonest errors in an exam answer. Concentration
monitoring is not a sign that a drug is important, and its absence is not a sign that a drug is
not. Warfarin is among the most dangerous drugs in common use and nobody measures its
concentration, because the effect is directly measurable and the effect is what matters. *That
contrast is consensus, and it is the whole shape of the topic.*

Claims below are marked **[M]** mechanism, **[D]** definitional, **[C]** consensus, or **[L]**
local — differing by country, institution or laboratory.

## What has to be true before monitoring a concentration is worth doing

Five conditions, and a drug needs essentially all of them **[C]**:

1. **A narrow therapeutic index.** If the margin is wide, the dose can be wrong by a factor and
   nothing happens, so a number adds nothing. See `m008`.
2. **No readily measurable effect.** This is the condition that actually selects the list. An
   antiepileptic's effect is the non-occurrence of seizures, which is unobservable over a short
   interval; an aminoglycoside's effect is bacterial killing at a site you cannot sample.
3. **A reproducible relationship between concentration and effect.** If the same concentration
   produces different effects in the same person on different days, the number is not informative
   **[M]**.
4. **Wide and unpredictable variability in the concentration a given dose produces.** If everyone
   given the same dose lands in the same place, dose by weight and stop. Monitoring earns its cost
   where the dose-to-concentration step is the unpredictable one — which is why renal and hepatic
   impairment, extremes of body composition, interacting drugs and metaboliser phenotype all push
   a drug towards monitoring.
5. **A validated, available assay with a known turnaround.** A result that arrives after the
   decision has been made is not a monitoring programme **[L]**.

The drug classes conventionally named as meeting them — aminoglycosides, glycopeptides, digoxin,
lithium, several antiepileptics, the immunosuppressants, methotrexate in high-dose protocols — are
the standard teaching list **[C]**. Which ones your laboratory actually offers, and at what
sampling times, is local, and the laboratory handbook is the authority.

## What a concentration is a function of

```
   ONE observation.  SEVERAL unknowns.

   C(t)  =  f(  dose , F , interval , time since last dose , CL , Vd ,
                                                    doses actually taken , assay )
                  ▲    ▲       ▲              ▲              ▲    ▲         ▲        ▲
                known  partly  prescribed   OFTEN NOT     unknown  unknown  UNKNOWN  known
                              (not always   RECORDED    (the thing          (the other
                               what was      ACCURATELY   you want)          thing you
                               taken)                                        want)

   ┌──────────────────────────────────────────────────────────────────────────────────┐
   │  To LEARN one unknown you must PIN the others. A sampling protocol is not        │
   │  bureaucracy — it is the only thing that makes the equation solvable. An         │
   │  unlabelled concentration is not a weak measurement. It is not a measurement.    │
   └──────────────────────────────────────────────────────────────────────────────────┘

   And note the two unknowns at the right-hand end. A low trough is equally consistent
   with high clearance and with missed doses, and the number cannot separate them.
   That is a conversation, not an assay. See m043.
```

## Timing, which is the whole discipline

A **trough** is the sample taken immediately before the next dose, at the lowest point of the
dosing interval **[D]**. It is the reference point for three reasons, and they are all mechanical.

* It is **reproducible**. The concentration at the trough changes slowly with time, so being half
  an hour out matters little. Thirty minutes of error near the peak can change the number
  substantially **[M]**.
* **Distribution is complete.** A sample drawn during the distribution phase reads high and means
  nothing, because the drug has not yet equilibrated with the tissue the effect lives in. Digoxin
  is the drug this is always taught on, and the reason it needs hours rather than minutes after a
  dose is its large volume of distribution **[C]**. The required interval is drug-specific and
  belongs to the product information.
* It is the point at which **sub-therapeutic exposure** is most likely, so it bounds the failure
  risk.

```
   ONE DOSING INTERVAL -- shape, not numbers

   C │        ╭─╮  ◄── peak: equilibration incomplete, steep, time-critical
     │       ╱   ╲
     │      ╱     ╲___
     │  ╱──╯  ▒▒▒▒▒▒▒▒ ╲────___
     │ ╱     ▒ DO NOT ▒        ╲────___
     │╱      ▒ SAMPLE ▒                ╲────___
     │       ▒  HERE  ▒                        ╲──── ◄── trough: flat, reproducible
     └──────────────────────────────────────────────────────────► time
      dose                                            next dose

   The shaded band is the distribution phase. A number from inside it is not high
   because the person is over-exposed; it is high because the sample was early.
```

And **steady state**. A concentration drawn before steady state cannot be compared with a
steady-state reference range, because the range was derived at steady state; it under-reads, and
acting on it over-doses. Steady state arrives on a timetable set by half-life and by nothing else
— the arithmetic is in `m006`. The exceptions are the drugs monitored deliberately *before* steady
state because early toxicity is the thing being watched for, and those are protocol-specific
**[L]**.

## What a trough actually tells you, and what it does not

**It tells you:** the exposure at the lowest point of the interval; whether accumulation is
happening, if you have a previous trough to compare it with; and whether the dose, the interval,
the clearance and the doses actually taken are *jointly* consistent with the target.

**It does not tell you:** the peak, the area under the curve, or the free concentration. Those
matter because the three are the exposure measures different drugs' effects actually track **[M]**
— a concentration-dependent killing effect tracks the peak, a time-dependent one tracks how long
the concentration stayed above a threshold, and a cumulative toxicity tracks the area. Monitoring
the wrong one is a real error with a plausible-looking number attached.

Three further caveats, each of which has caused harm:

* **The assay measures total drug, not free drug.** For a highly protein-bound drug,
  hypoalbuminaemia raises the free fraction, so the *total* concentration understates the active
  drug and may read "normal" during toxicity. Phenytoin is the standard example and uraemia
  compounds it **[C]**.
* **An assay for the parent misses active metabolites.** Where the metabolite carries much of the
  effect, the parent concentration is not the exposure that matters **[M]**.
* **Reference ranges and units are laboratory property.** They differ between laboratories as well
  as between countries, and a result transcribed without its units or its range is a recognised
  source of error **[L]**.

Finally, the discipline that makes all of it safe: a concentration is interpreted **with** the
person, not instead of them. A number inside the range in someone showing toxicity does not
exclude toxicity; it says the number was not the right question. Monitoring exists to inform a
clinical judgement that remains the clinician's.

## The human stakes, said plainly

The sections above are an inference problem. The reason the inference is worth getting right is
not.

The drugs on the monitoring list are on it because they hurt people. Aminoglycoside ototoxicity is
often irreversible. Lithium toxicity can cause lasting neurological injury. Immunosuppressant
under-exposure loses transplanted organs and over-exposure causes infection and malignancy. These
are not abstract risks balanced against each other in a textbook; they are outcomes that happen to
individual people, frequently because a sample was drawn at the wrong time, or a result came back
and nobody acted on it, or a range from one laboratory was read against a number from another.

When that happens the harm was caused by the care and not by the illness. The honest word is
iatrogenic, and naming it that way is what makes it reportable, auditable and preventable for the
next person. The person it happened to did nothing wrong, and a monitoring system that depends on
nobody ever being busy is a badly designed system rather than a collection of careless
individuals.

Nothing in this answer can be used to judge whether a particular result is safe, and no number
here is a reference range. Anyone with a question about a blood test or a medicine of their own
should raise it with the clinician or pharmacist who holds their records.

## What an examiner digs into next

* Why is warfarin not concentration-monitored when it is obviously dangerous?
* A trough comes back low. Name three explanations the number cannot distinguish between.
* Why does a sample drawn two hours after a digoxin dose read high, and what is wrong with acting
  on it?
* In hypoalbuminaemia, which way does the total phenytoin concentration mislead you, and why?
* A result sits inside the reference range and the person has signs of toxicity. What now?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md) —
your national formulary, your national guideline body, your own institution's policy, a current
standard textbook, and the primary literature. Specific to this answer:

* **Your local laboratory handbook or therapeutic drug monitoring service.** The authority for
  every reference range, every sampling time and every unit in this topic. It is local on purpose,
  and a range from somewhere else is not a substitute.
* **The summary of product characteristics or regulator-approved prescribing information** for
  each drug on your monitoring list, for the sampling interval after a dose and for whether
  monitoring is part of the licensed approach.
* **Your national formulary's monographs** for the drugs named above, for monitoring requirements
  and for the interaction and impairment adjustments that change the dose-to-concentration step.
* **Your institution's policy on acting on a result out of hours**, which is the part of a
  monitoring programme that most often fails and the part least often written down.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **No reference range, sampling interval or target concentration appears in
this answer**, deliberately: those are laboratory and formulary property, they differ between
institutions and between countries, and a figure remembered from revision material is exactly the
wrong thing to carry to a bedside. Nothing here should be used to make a decision about anyone's
treatment, including your own; the laboratory, the formulary, the product information and local
guidance are the authority. Anyone with a question about a medicine or a blood test of their own
should raise it with their own prescriber or pharmacist.

## Where this stands, October 2026

The inference structure above — one observation, several unknowns, pin the rest to solve for one —
is algebra and does not date. The hierarchy of outcome over effect over concentration is
long-standing consensus and is unlikely to move. What dates, and quickly, is everything attached
to a particular drug or laboratory: which drugs are monitored at all, by trough or by area under
the curve, at what sampling time, against what range, in what units. Area-under-the-curve-guided
dosing has been displacing trough-only approaches for some agents, at different times in different
countries, and assay platforms change ranges when they change. Check the current laboratory
handbook and the current formulary rather than any remembered number.
