---
id: "m037"
slug: recognising-sepsis
style: serious
category: nursing
difficulty: advanced
question: "Why is the response to suspected sepsis organised as a time-critical bundle, and what does that design trade away?"
tags: [sepsis, deterioration, bundles, antimicrobial-stewardship, screening]
---

# A bundle exists because the actions must not be done one after another.

The current international consensus definition describes sepsis as life-threatening organ
dysfunction caused by a dysregulated host response to infection, with septic shock as the subset
carrying circulatory and cellular metabolic derangement. *Definitional, and the authority is the
consensus definitions document issued by the collaborating critical care societies.* Two words in
that sentence do the work. **Dysregulated**: a large part of the damage is the response, not the
organism. And **dysfunction**: it is not the infection that defines sepsis, it is what the
response to the infection has done to organs that were not infected.

Markers used below: *mechanism* means checkable by reasoning; *definitional* means it is what the
word means; *consensus* means mainstream agreement across major guidance; *contested* means the
field genuinely disagrees; *country-dependent* means the reader's own guidance decides.

## Why time is in the design at all

Once organ dysfunction is established, the components feed one another. Hypoperfusion drives
anaerobic metabolism and acidosis; endothelial activation and microvascular failure make oxygen
delivery worse at the capillary even where the blood pressure looks adequate; coagulation
activation occludes small vessels; cellular energy failure reduces the ability to recover from any
of it. *Mechanism, from physiology rather than from any guideline.* Each hour's physiology makes
the next hour's harder to reverse, so the cost of a delay is larger than the cost of the same
delay an hour earlier.

The direction of that relationship is not controversial. The **size** of it is — the observational
literature on time-to-antimicrobial and mortality is consistent in direction and much argued over
in magnitude, in whether it is causal across all subgroups, and in whether the mandated time
windows derived from it are the right ones. *Contested, and this is the claim here a reader should
go to the primary literature for rather than accept from any summary, including this one.* A
number is deliberately absent; an invented one would be worse than none.

## What a bundle actually is, structurally

A bundle is not a list of good ideas. It is a **parallelisation device**, and that is the entire
argument for the form:

```
   AS A SEQUENCE — each step waits for the last one to finish
   ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐
   │ notice │──▶│ sample │──▶│ treat  │──▶│ measure│──▶│ review │
   └────────┘   └────────┘   └────────┘   └────────┘   └────────┘
   time elapsed = the SUM of all five, and the physiology runs the whole time

   AS A BUNDLE — the independent actions are launched together
   ┌────────┐   ┌─────────────────────────────────────────────┐
   │ notice │──▶│ sample  ┊  treat  ┊  measure  ┊  escalate   │──▶ reassess
   └────────┘   └─────────────────────────────────────────────┘
   time elapsed = the SLOWEST one, plus the ORDERING CONSTRAINTS that are real

   The ordering constraints that are real, and they are few:
     * microbiological sampling before antimicrobials, because afterwards the result is
       much less interpretable — BUT sampling must not become the reason treatment waits
     * a measurement taken before an intervention, so the intervention has a baseline
   Everything else in a bundle is independent, and anything independent that is done
   in series has been needlessly serialised.

   And the second function: a bundle converts N separate decisions, each of which can be
   deferred by an individual, into ONE decision that cannot.
```

That second function is the human-factors half and is at least as important. The reason escalation
thresholds are written as numbers — the subject of this specialty's handover question — is that a
written mandate removes the need for a junior to justify an action. A bundle does the same thing
for a set of actions: nobody has to argue for the blood cultures separately.

## What the design trades away

This is the substance of the topic, and a candidate who can only recite the elements has missed
it.

**Specificity, deliberately.** A screening trigger built to catch sepsis early must fire on
physiology that is also produced by pain, anxiety, dehydration, alcohol withdrawal, pulmonary
embolism, haemorrhage, pancreatitis and a dozen other things. The tools in use are tuned for
sensitivity because the cost of a miss is high — and the arithmetic of that choice means most
positive screens are not sepsis. *Consensus.* The consequences are not hypothetical:

```
   ERROR DIRECTION 1 — treated as sepsis, was not
   ──────────────────────────────────────────────────────────────────────────────
   broad-spectrum antimicrobials to someone with no bacterial infection
   selection pressure, and resistance that outlives the admission
   antimicrobial-associated colitis, and candidal overgrowth
   intravenous access placed, with its own infection and thrombosis risk
   fluid given to a person whose heart or kidneys cannot accommodate it
   a diagnostic anchor: the real cause looked for less hard once a label exists
   a critical care referral, a transfer, and a bed that someone else needed

   ERROR DIRECTION 2 — was sepsis, not treated as sepsis
   ──────────────────────────────────────────────────────────────────────────────
   organ dysfunction that becomes established and then does not fully reverse
   the whole reason the first column is accepted
   ──────────────────────────────────────────────────────────────────────────────
   The design accepts column one to reduce column two. That is a judgement about
   relative cost, not a fact about biology, and it is revisited as the evidence
   and the resistance picture change.
```

**Fluid is not universally good.** The same volume that restores perfusion in one person
precipitates pulmonary oedema in another with heart failure, dialysis-dependent kidney disease or
cirrhosis. The movement in the field over the last decade has been away from a single fixed volume
for everyone and toward giving fluid in assessed increments with reassessment between them.
*Consensus in direction; the specifics are country-dependent and are among the parts of sepsis
guidance that have changed most.*

**Source control is the half the bundle does not contain.** Antimicrobials without drainage of an
abscess, relief of an obstructed urinary tract, removal of an infected device or surgery for a
necrotising soft tissue infection will not work, and the patient deteriorates while every box on
the form is ticked. *Consensus, and mechanistically obvious once stated.* The question "where is
it" is as time-critical as anything in the bundle and has no box.

**Starting is protocolised; stopping is not.** There is far more guidance on how to begin than on
when to narrow, switch or stop, and the stop is where antimicrobial stewardship lives — reviewing
at the point cultures return, de-escalating to a narrower agent, and stopping when the diagnosis
has changed. A bundle with no review step attached builds a cohort of people on broad-spectrum
agents nobody has revisited. *Consensus.*

**The audit changes the behaviour, not always for the better.** Bundles are measured, and measured
things get documented. Documentation-driven compliance — the box completed, the reassessment
recorded rather than performed — is a recognised failure mode of any mandated bundle, and the
response to finding it is to look at why the work and the form disagree rather than at who filled
the form in.

**And the presentation is not the textbook one in the people most likely to have it.** Fever may
be absent, particularly in older people, in people taking antipyretics or steroids, and in people
with chronic kidney disease; hypothermia is a recognised and worse-prognosis presentation. In a
frail older person the presentation is frequently delirium, a fall, reduced oral intake or simply
"different today" rather than any vital sign. Neutropenia, immunosuppression, pregnancy and the
postpartum period, and children each carry their own distinct pathway and their own thresholds.
*Consensus that these groups differ; the thresholds and pathways are country-dependent.* The
absence of fever is not reassurance, and this single point probably causes more missed sepsis than
any threshold in any tool.

## The human stakes, said plainly

Sepsis kills a great many people every year, and a substantial share of those deaths follow a
recognisable period during which somebody could have acted sooner. Families' accounts of those
cases say the same thing with striking consistency: the concern existed, it was voiced, and it did
not reach a decision in time. Every bundle, trigger and screening tool in this area is a response
to that, and that is why they are mandated rather than suggested.

The other half is real too, and is easier to forget because its victims are diffuse. Treating
everyone who screens positive as though they have sepsis harms some of them, and contributes to a
resistance problem that will outlast every person reading this. Holding both of those at once —
without using either to excuse inaction on the other — is what competence in this topic looks
like.

## What an examiner digs into next

What the local screening tool actually is, what it is tuned for, and what it will fire on that is
not sepsis. Why the first question after starting treatment is "where is the source". What
de-escalation looks like locally and who owns it. Why hypothermia and a normal temperature are
both compatible with sepsis. How the presentation differs in a frail older person, in neutropenia,
and in the postpartum period. And what the local escalation route is when somebody is worried and
the tool has not triggered.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The international consensus definitions of sepsis and septic shock, issued by the collaborating
  critical care societies — the authority for the definitional material in the opening paragraph.
* The international campaign guidelines on the management of sepsis and septic shock, for the
  bundle structure and for the fluid and antimicrobial recommendations, which have been revised
  repeatedly.
* The reader's own national guidance on recognising and responding to sepsis, and the reader's
  institutional sepsis screening tool and pathway — the authority for every trigger, time window
  and named action, none of which appears here.
* The reader's national antimicrobial stewardship guidance, for de-escalation and review.
* A standard critical care or applied physiology textbook, for the organ-dysfunction mechanism,
  which is physiology rather than guideline material.
* The primary literature on time-to-antimicrobial and outcome, which is the single most contested
  claim in this answer and should not be taken from any secondary summary.
* The reader's national guidance on sepsis in pregnancy and the puerperium, in neutropenia, and in
  children, for the three populations whose pathways differ.

## Scope and safety

This explains why a class of protocol is designed the way it is, for someone already training in
or qualified for clinical practice. **It is not a sepsis bundle and deliberately does not contain
one** — no trigger values, no time windows, no fluid volumes, no antimicrobial choices. Those are
set nationally and institutionally, they differ, and they are revised; the reader's own pathway is
the authority and this is not. It has had no clinical review. Nothing here is for use in an
emergency or for a decision about any person's care. If someone is unwell right now, the local
emergency number is the correct response.

## Where this stands, October 2026

The physiology and the definitional framework are stable. Almost everything procedural around them
has moved within living memory and will move again: the screening tools and which physiological
score sits behind them, the time windows and whether they should be mandated at all, the fluid
recommendations, the place of lactate, and the balance struck against antimicrobial stewardship.
This area has been more actively contested than most of nursing practice, and a reader should
expect the version they were taught to have been superseded. The local pathway is the authority
for every number.
