---
id: "m047"
slug: multimorbidity-and-guidelines
style: serious
category: general-practice
difficulty: advanced
question: "Why do single-disease guidelines stop composing once a person has four conditions, and what has to replace them?"
tags: [multimorbidity, guidelines, treatment-burden, competing-risk, prioritisation]
---

# A guideline is a conditional statement, and the condition stops holding

Every recommendation in a single-disease guideline is implicitly of the form: *in a population
resembling the one this was derived from, doing X produces more benefit than harm, over this
horizon.* The disease is the part that gets written down. The resembling, and the horizon, are the
parts that do the work, and both fail silently when the person in front of you has four conditions
rather than one *[mechanism, not guideline]*.

So the failure is not that four guidelines are too much to read. It is that each one is a
*conditional* recommendation whose condition is no longer satisfied, and nothing in the document
says so. A guideline cannot warn you that you are outside it, because being outside it is exactly
the circumstance it does not model.

## Four mechanisms, and they are different from each other

Treating them as one thing — "polypharmacy" — loses the distinctions that determine what to do.

1. **Direct conflict between indications.** The intervention indicated for one condition is
   contraindicated, or harmful, in another. This is not a drug interaction; it is an interaction
   between *recommendations*, and it appears in neither document because neither document
   considers the other condition.
2. **Time-to-benefit against competing risk.** A recommendation whose benefit accrues over years
   has a different expected value in someone whose horizon is shortened by their other conditions.
   The evidence has not changed; the integral over it has. This is the single most under-taught
   piece of reasoning in the area *[mechanism, not guideline]*.
3. **Treatment burden is a shared and finite budget, and no guideline debits it.** Appointments,
   monitoring, blood tests, dose timings, the cost where there is one, the cognitive load. Each
   guideline assumes it is drawing on an empty account. Four of them overdraw it, and the
   overdraft shows up as non-attendance and non-adherence, which are then recorded as properties
   of the person.
4. **The evidence is thinnest exactly where the decisions are hardest.** Trials have historically
   excluded participants with several conditions, or with the organ impairment those conditions
   produce, so applicability is worst for the people in whom the stakes are highest. That the
   exclusions existed is a matter of record; how much they bias any specific estimate is
   contested *[consensus, magnitude contested]*.

## Why composition is the mathematical problem it looks like

```
   TWO DOCUMENTED TERMS, AND A PRODUCT THAT APPEARS IN NEITHER DOCUMENT.
   The numbers are illustrative multipliers, chosen to show the shape.

   guideline A says, for condition A alone:   effect on risk  ×0.5
   guideline B says, for condition B alone:   effect on risk  ×2.0

   ┌──────────────────────────┬──────────────┬──────────────┬──────────────────────────┐
   │ the person in front of   │ term from A  │ term from B  │ composed                 │
   │ you has                  │              │              │                          │
   ├──────────────────────────┼──────────────┼──────────────┼──────────────────────────┤
   │ condition A only         │    ×0.5      │      —       │  ×0.5   in guideline A   │
   │ condition B only         │      —       │    ×2.0      │  ×2.0   in guideline B   │
   │ both A and B             │    ×0.5      │    ×2.0      │  ×1.0   in NEITHER       │
   └──────────────────────────┴──────────────┴──────────────┴──────────────────────────┘

   The composed answer looks ordinary. Nothing about it is ordinary: it is the product
   of two abnormal terms that happen to cancel, and a clinician reading either document
   alone would act, correctly by that document, and wrongly here.

   Now the other direction, same arithmetic:

   both terms pointing the same way      ×2.0 × ×2.0  =  ×4.0
   both terms pointing the other way     ×0.5 × ×0.5  =  ×0.25

   One composition, a sixteen-fold spread between its extremes, and not one of the four
   products is printed in either single-condition table.
```

The clinical content of that diagram is the asymmetry it exposes. A composed estimate that looks
unremarkable is not evidence that the composition is unremarkable, and the four-condition case is
where the products get far enough from one that the single-disease recommendation can be the wrong
sign rather than merely the wrong size.

## What replaces the four guidelines

Not nothing, and not clinical intuition. A different object: **one plan with a stated priority
order**, which is a harder document to write and the only one that can exist.

* **Elicit what the person is trying to achieve, before ranking anything.** This is not a
  courtesy. Without it there is no ordering relation, and without an ordering relation
  prioritisation is arbitrary. Different people with identical conditions rank function, symptom
  relief, longevity and freedom from monitoring differently, and the ranking is theirs to supply.
* **Say which recommendations are being set aside, and why, in the record.** A guideline not
  followed is a decision; a guideline not mentioned is a gap. The difference is legible only if
  somebody wrote it down.
* **Count treatment burden explicitly as a cost on the same page as the benefits.** Including the
  appointments the plan itself generates.
* **Prefer the mechanism to the recommendation where they diverge.** Physiology composes;
  recommendations do not. Reasoning from how the conditions interact is the only thing available
  when no document covers the combination.
* **One review rather than four.** Combining reviews is the structural counterpart of combining
  guidelines, and it is the part a service can implement rather than an individual clinician.
* **Name the horizon.** For each recommendation kept, roughly how long until the benefit arrives,
  set beside what else is likely to happen in that time.

## The counterweight, which is not optional

Multimorbidity is not a licence to do less, and the argument above can be misused that way with
very little effort. The phrases *treatment burden* and *limited horizon* are available to justify
withholding effective treatment from people who are old, poor, cognitively impaired, or carry a
psychiatric diagnosis — and under-treatment of exactly those groups is a documented pattern, not
a hypothetical risk *[consensus]*. The test that does some work is whether the same reasoning
would have been applied to a person with identical conditions and a different life.

And the guidelines remain the best available statement about each condition taken alone. Composing
them badly is a real problem; discarding them is a worse one.

## The human stakes, said plainly

Four conditions is one life. The person is doing the integration already — across appointments, in
the gaps between letters, with no clinical training and no access to the reasoning that produced
any of the four plans. When a service says it is hard to combine four guidelines, it is describing
work it has handed to the least-equipped person in the system.

The experience of multimorbidity, as people describe it, is less about any single condition than
about the volume of the apparatus: the letters, the differing instructions, the having to explain
the whole history again to each new clinician, the appointments that conflict, the sense that
every clinician is confident about their slice and nobody is responsible for the whole. That
burden is not an inconvenience around the edge of care. For many people it is the dominant part of
living with illness, and it is almost entirely invisible in the record.

Two things follow that are worth saying directly. Asking what matters most to someone is not a
soft skill bolted onto a technical decision — in this situation it is the technical step without
which the decision cannot be made at all. And a conversation about a shortened horizon has to be
offered when there is time for it, not discovered inside a medication review, and the person
decides how far it goes.

## What an examiner digs into next

Whether the candidate names *conditionality* rather than *quantity* as the reason composition
fails. Then time-to-benefit against competing risk, argued with an example. Then treatment burden
as a budget nobody debits. Then the priority-setting step, and who supplies the ordering. Then the
uncomfortable one: how to tell a properly prioritised plan from rationing dressed as
prioritisation, and what would have to be in the record to distinguish them.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The national guideline on multimorbidity or on the care of people with several long-term
  conditions, issued by the body that governs the reader's practice, which is the document that
  states the prioritisation approach expected locally *[country-dependent]*.
* The eligibility criteria sections of the pivotal trials behind any specific recommendation being
  applied, which is where the applicability question is actually settled.
* Any systematic review of the representation of multimorbidity in randomised trials, in the
  clinical-epidemiology literature, for the scale of the exclusions.
* The published literature on treatment burden and on the cumulative complexity of care, for the
  vocabulary and for the instruments that attempt to measure it.
* Any analysis of time-to-benefit for the specific intervention in question, which is the number
  that makes the competing-risk argument concrete rather than rhetorical.
* The reader's own organisation's structured medication review and care-planning templates, for
  what is locally expected to be recorded about recommendations deliberately not followed.

## Scope and safety

This is revision material about how clinical recommendations are combined, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here should inform what any individual takes, stops or attends — that belongs
with the clinicians and the pharmacist who hold the person's full list and know their
circumstances. No medicine, class, condition pairing, target or threshold is named here on
purpose. The multipliers in the worked example are illustrative integers chosen to make the
arithmetic legible; none is the measured effect of anything. Formularies and guidelines differ by
country and are revised, and the local versions are the authority — this is not. If someone is
unwell right now, the relevant action is to contact local urgent care or the local emergency
number, not to read this.

## Where this stands, October 2026

The structural argument — that a guideline is a conditional recommendation and that the condition
fails under multimorbidity — is mainstream and stable, and has been for long enough that national
guidance on the topic now exists in several countries. What continues to move is the practical
apparatus: how combined reviews are specified and funded, whether incentive frameworks reward a
single prioritised plan or a set of disease-specific indicators, and how time-to-benefit estimates
are published for individual interventions. Risk-prediction tools built for people with several
conditions are arriving and are not yet well validated across populations. Take the local
prioritisation framework, and any specific time-to-benefit figure, from current sources rather
than from here, as of October 2026.
