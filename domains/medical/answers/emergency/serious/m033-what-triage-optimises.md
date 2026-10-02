---
id: "m033"
slug: what-triage-optimises
style: serious
category: emergency
difficulty: advanced
question: "What is a triage system optimising, and why is the sickest patient not first in a mass-casualty setting?"
tags: [triage, mass-casualty, prioritisation, marginal-benefit, training]
---

# The objective never changes. The constraint does, and that is what inverts the order.

A triage system is a sorting rule that only exists when demand exceeds the resource available
inside the window in which treatment still changes the outcome. What it optimises is the number of
people who survive **across everyone who presented**, subject to a fixed resource over a fixed
window. **(Mechanism** — this is a constrained-optimisation argument and it is checkable by
reasoning.**)**

In routine practice the resource is not the binding constraint. There are enough hands, enough
time, enough blood, enough theatres. When a constraint is slack, two objectives that are different
in principle — *the best achievable outcome for the person in front of me* and *the most survivors
overall* — give the same answer, and the reflex of going to the most unwell person first is simply
correct. In a mass-casualty incident the resource becomes the binding constraint, the two
objectives come apart, and the population objective is the one the system follows.

So the inversion is not a change of values. It is the same value — fewest deaths — evaluated under
a constraint that used to be slack and no longer is. That distinction is the whole answer, and it
is the reason the inversion can be defended rather than merely obeyed.

## Why the ordering inverts, as arithmetic

Rank people by the **expected lives gained per unit of resource spent**: the probability of
survival with treatment minus the probability without, divided by the resource that treatment
consumes.

```
   group                            benefit if treated   resource needed   benefit per unit
   ────────────────────────────────────────────────────────────────────────────────────────────
   will survive without help        very small           small             low
   will die without help, and       large                moderate          HIGHEST
     likely to survive with it
   unlikely to survive whatever     small                very large        lowest
     is done with what is available
   ────────────────────────────────────────────────────────────────────────────────────────────
   routine practice : the denominator does not bind, so this ranking == severity ranking
   mass casualty    : the denominator binds, so this ranking != severity ranking
```

The third row is where the inversion bites, and it is the row that is counterintuitive, because in
routine practice that group receives the most of everything. Under a binding constraint it has
both a small numerator and a very large denominator, so it ranks last on the quantity being
optimised. The second row — severely injured but salvageable — ranks first.

This also explains why *sickest first* felt like a principle rather than a heuristic. It is a
**proxy** for the benefit-per-unit ratio, and it is an excellent proxy exactly while the
denominator can be ignored. Proxies that are accurate for a decade feel like definitions. This one
is not one.

## Why it is a sieve, not an assessment

Three structural consequences follow from the resource being the binding constraint, and all three
look like sloppiness until the constraint is taken seriously.

* **Sorting consumes the resource it is allocating.** A slow, accurate sort can cost more than the
  accuracy is worth. So the categories are few, the observations are few, and the decision is
  mechanical. Precision is deliberately traded for speed, at a rate chosen in advance by people
  who were not under pressure.
* **The sort key moves, so the sort repeats.** Probability of benefit changes as time passes and
  as resource arrives. A triage decision is a snapshot of a ranking, not a verdict, and every
  system of this kind builds in re-sorting for that reason.
* **The constraint itself has to be assessed, and that assessment can be wrong.** The whole
  inversion is conditional on the resource genuinely binding. Switching into this mode when it
  does not causes harm with no compensating benefit, which is why the decision to declare the mode
  is separated from the decision about any individual.

## The hardest part, stated plainly

Every system of this kind contains a category for people whose injuries are not survivable with
the resource available.

That is not a technical detail and it will not be dressed up here. It is a decision forced by a
constraint nobody chose, it carries a genuine moral cost that the arithmetic above does not
discharge, and it is distressing for everyone involved — including, and often especially, the
person who had to make it. Services that use these systems also run debriefing, peer support and
occupational health provision for the people who apply them, and that provision is part of the
system rather than an afterthought to it. Those routes exist precisely for this, and they are the
right place to take it — which is worth knowing before anyone needs them.

## Why the inversion has to be trained rather than explained

* **It is not a knowledge gap. It is a reflex override.** The reflex — the worst-off person
  receives everything available — is correct in every other setting and is reinforced thousands of
  times across a career. Overrides of a well-practised reflex fail under stress unless the
  override itself has been rehearsed under something like stress. Explaining it once does not
  install it.
* **The role is deliberately separated from the treating role.** One person cannot hold a
  population objective and an individual objective simultaneously; the individual one wins,
  because it is the one looking back. Assigning the sort to someone who is not treating is a
  structural fix for a predictable human failure, not a comment on anyone's character.
* **The criteria are deliberately mechanical.** The less the decision depends on the state of the
  person making it, the better it survives the conditions it is made in. That is question m032's
  argument applied to the single decision where it matters most.
* **The counterintuitiveness is evidence the system is doing work.** A sorting rule that agreed
  with everyone's instinct in every setting would be redundant. The discomfort is the signal that
  the constraint is real.

## What it gives up

It is wrong about individuals by construction — that is what optimising a population total means.
It rests on prognostic judgements made in seconds, from few observations, by people under extreme
pressure, and those judgements are known to be imprecise in both directions. And it produces a
documented trail of decisions that will be reviewed later, calmly, by people with information that
nobody had at the time. A system that could not survive that review honestly would not be usable;
saying out loud in advance what it is optimising is how it survives it.

## What an examiner digs into next

* State the objective function, and state what changed between routine practice and a
  mass-casualty incident. Which one was it?
* Why does the ranking by benefit-per-unit-resource coincide with severity in routine practice?
* Why is *sickest first* a proxy rather than a principle, and when exactly does the proxy fail?
* Why is the sorting role separated from the treating role?
* Why is re-triage structural rather than a safety net?
* What harm follows from declaring the constrained mode when the resource was in fact adequate?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* **The reader's own service or employing organisation's** major-incident and mass-casualty triage
  policy, which names the triage tool actually in use where they work, its categories and its
  criteria. This is the document that governs, and it is the one this answer deliberately does not
  reproduce.
* **The reader's regional or national trauma network's** major-incident guidance, which sets out
  how the mode is declared and by whom.
* The current life support and major-incident guidance issued by **the national resuscitation
  council for the country the reader practises in**. The councils differ from one another and each
  revises on its own cycle.
* The current consensus on science with treatment recommendations issued by **the International
  Liaison Committee on Resuscitation**, for the evidence synthesis the national councils write
  from.
* **The reader's own organisation's** staff support, debriefing and occupational health provision,
  which is a named service in almost every such organisation and is the right route for the part
  of this subject that is not academic.

Claims here are marked **mechanism** (constrained optimisation and human-factors reasoning,
checkable by thinking), **consensus** (agreed across mainstream practice as of writing), or
**council-dependent** / **service-dependent** (genuinely different between organisations). No
triage tool is named, no category labels are given, no criteria or thresholds are stated, nothing
is quoted, and no guideline number or document title is given, because none was opened.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *what a triage system is optimising and why*, written for someone
already trained. It is deliberately not a protocol and is not usable as one: it names no triage
tool, lists no categories, states no criteria or thresholds, and contains no sequence of actions,
rates, depths, ratios, doses or settings. Triage tools and major-incident policies **differ
between countries, services and institutions**, and resuscitation guidance likewise **differs
between national councils and is revised on a cycle**. The reader's own service policy and
national council are the authority; this is not, and it has had no clinical review. Nothing here
describes any real person, case, incident or institution.

## Where this stands, October 2026

The constrained-optimisation account of triage, the benefit-per-unit-resource ranking, the
separation of the sorting role from the treating role and the requirement to re-sort are
mainstream and are **mechanism** — a reader can check the reasoning without opening anything.
Everything specific is **service-dependent**: which triage tool is in use, how many categories it
has, what they are called, what observations feed it, who may declare a major incident, and how
decisions are reviewed afterwards all differ between countries and between neighbouring services
in the same country, and all of them are revised. Several national councils publish on multi-year
cycles that are not synchronised with each other. Dated October 2026; the governing document is
the one issued by the service the reader actually works for.
