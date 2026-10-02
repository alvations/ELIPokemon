---
id: "m031"
slug: primary-survey-ordering
style: serious
category: emergency
difficulty: intermediate
question: "Why is the primary survey ordered airway, breathing, circulation, and what is that ordering actually sorting on?"
tags: [primary-survey, abcde, prioritisation, protocol-design, revision]
---

# The letters are a sort, and the key is time-to-irreversible-harm

The primary survey is not a list of the five most important things. It is a **sort**, and the key
it sorts on is how quickly an unaddressed failure in each system causes harm that cannot be
undone. A completely obstructed airway stops oxygen entering at all, and the clock on that is the
shortest clock in the body. Ventilatory failure runs a little slower. Loss of circulating volume
runs slower again, and how much slower depends on the rate of loss. Rising intracranial pressure
and unrecognised hypothermia are slower still. Put the shortest deadline first and the scarcest
resource in the room — the first few minutes, and the attention of whoever is leading — is spent
where the deadline is nearest. The letters are the output of that sort. The sort key is the
reasoning, and it is the only part worth memorising, because it regenerates the letters.

That is why *which of these is the sickest-looking problem* is the wrong question. Severity,
visibility and treatability are all different keys, and sorting on any of them produces a
different and worse order. A dramatic open fracture is visible, severe and treatable, and it is
not in the primary survey's first four letters, because its clock is long. **(Mechanism** — this
follows from the physiology of oxygen delivery and from nothing else, and it is checkable by
reasoning rather than by citation.**)**

## What the sort looks like

```
  deadline, to an order of magnitude   the question being asked        where it sits
  ────────────────────────────────────────────────────────────────────────────────────
  seconds to a couple of minutes       is the airway open?                   A
  a few minutes                        is air actually moving, enough?       B
  minutes to tens of minutes           is blood actually moving, enough?     C
  tens of minutes to hours             is the brain being injured now?       D
  hours                                what has been missed so far?          E
  ────────────────────────────────────────────────────────────────────────────────────
        ▲
        └── the sort key: time to irreversible harm.
            Not severity. Not visibility. Not how fixable it is.
```

## Three properties that make the ordering forced rather than conventional

**It is also a dependency order, and the two agree.** Lower letters are conditional on higher ones
in a way that makes work on them literally unproductive. Moving air into lungs that nothing
reaches is wasted work; moving blood that carries no oxygen is wasted work. So the sequence is
simultaneously a sort on urgency and a topological sort of a dependency graph. Those two orders
coinciding is a fact about respiratory and circulatory physiology, not a design choice, and it is
the single thing that makes the survey teachable as a mnemonic instead of as a derivation.

**The clocks belong to the physiology, not to the operator.** This is the consequence people argue
with, and it is the one that matters. Being very experienced changes how *fast* each step is
completed and how *well*; it does not move any deadline. So experience is not a licence to start
further down the list. A protocol whose ordering depended on who was running it would not be an
ordering at all — it would be a suggestion, and it would stop being comparable between two people
or two shifts. The ordering is deliberately indifferent to how good the person using it is.

**The famous exceptions are the same key applied to a different situation, which is the proof.**
Where the presenting problem is a non-perfusing cardiac rhythm, circulation's clock becomes the
shortest clock, and the sequence re-sorts to put it first. Where there is catastrophic external
haemorrhage, that specific bleed's clock is shorter than the airway's, and it goes in front of
everything. Neither is a carve-out bolted onto a tradition. Both fall out of running the same sort
on a different set of inputs — and the fact that they do is the cleanest available evidence that
the ordering was derived rather than inherited. **(Consensus** that both re-sorts exist;
**council-dependent** in how each is worded, where its boundaries are drawn, and what it is
called.**)**

```
   what dominates the presentation      the order the key produces
   ──────────────────────────────────────────────────────────────────
   nothing in particular                A    B    C    D    E
   a non-perfusing rhythm               C    A    B
   catastrophic external bleeding       the bleed, then A, B, C
   ──────────────────────────────────────────────────────────────────
   one sort key, three input vectors, three orders
```

## What the ordering gives up

* **It is coarse.** Five bins over a continuum of deadlines. Within a letter it says nothing about
  what to do first, and it cannot express "these two are equally urgent".
* **It reads as sequential when the work is parallel.** A team addresses several letters at once.
  The ordering is a statement about **what wins when two demands collide** — whose turn it is when
  there are not enough hands — not a prohibition on concurrency. Read as a queue by one person
  working alone, it is close to right; read as a queue by a team of six, it wastes five of them.
* **It is wrong whenever the key is wrong for the situation.** A sort is only as good as its key,
  and the key encodes an assumption about which clocks are running. The structured survey is
  excellent at stopping a frightened person from fixing the visible thing, and it is poor at
  noticing that the situation is not the one it was designed for.
* **It can manufacture a feeling of completion.** Reaching E is not the same as having understood
  the problem, and the survey is explicitly built to be repeated rather than finished.

## Why it is taught as letters at all

Because the recall has to survive a stressed, sleep-deprived, frightened human being who does this
rarely. A derivation does not survive that; five letters in a fixed order do. The mnemonic is a
compression of the reasoning chosen for robustness rather than for elegance, and the cost of that
compression — coarseness, and a false air of sequence — is accepted on purpose. Question m032 is
about that trade in general.

## The human stakes, said plainly

Everything above is a sort. What is being sorted is how much time a person has left.

An airway that is completely obstructed stops oxygen entering the body at all, and the tissue that
runs out first is brain, which holds almost no reserve of its own. Ventilatory failure arrives at
the same place more slowly. Loss of circulating volume is slower again, and the rate of loss
decides how much slower — the same volume lost over an hour and lost over four minutes are not the
same problem. Rising pressure inside a closed skull, and a core temperature falling while nobody
is looking, are slower still and stay reversible for longer. That last point is the one most often
misread: the later letters sit late because their clocks are long, not because what happens there
matters less to the person it is happening to. **(Mechanism.)**

Two things follow that are worth saying with no machinery around them. The ordering is not a
ranking of people and it is not a ranking of how much anything matters; nobody further down the
sort is being valued less. And reaching the last letter is not the same as the person being safe —
which is why a structured survey is built to be run again rather than finished, and why the
commonest serious failure it exists to prevent is a competent, frightened person giving all of
their attention to the injury they can see.

## What an examiner digs into next

* What is the sort key, in one sentence, without naming the letters?
* Why do the dependency order and the urgency order agree, and what would follow if they did not?
* Why is seniority not a reason to reorder, and what *is* a legitimate reason?
* Why do the re-sorted sequences support the principle rather than undermine it?
* What does the ordering fail to express, and what compensates for that in practice?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md).
Specific to this answer:

* The current adult basic and advanced life support guidelines issued by **the national
  resuscitation council for the country the reader practises in**. There is no single global
  document, the councils differ from one another, and each revises on its own cycle.
* The current consensus on science with treatment recommendations issued by **the International
  Liaison Committee on Resuscitation**, which is the evidence synthesis the national councils
  write their own guidelines from.
* The current primary survey and catastrophic-haemorrhage guidance issued by **the reader's
  regional or national trauma network**.
* **The reader's own employing organisation's** resuscitation and trauma policy, which is the
  document that actually governs practice where they work and which outranks every general account
  including this one.

Every claim above is marked **mechanism** (it follows from physiology and is checkable by
reasoning), **consensus** (agreed across the major councils as of writing), or
**council-dependent** (it genuinely differs between councils). Nothing here is quoted from any of
these documents, and no guideline number, document title or identifier is given, because none was
opened.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why a protocol has the shape it has*, written for someone already
trained. It is deliberately not a protocol: it contains no sequence of actions, no rates, no
depths, no ratios, no doses and no settings, and it is not a reference to be consulted while
acting. Resuscitation and trauma guidance **differs between national councils and is revised on a
cycle**, and the differences reach exactly the material this answer avoids stating. The reader's
own national council and local protocol are the authority; this is not, and it has had no clinical
review. Nothing here describes any real person or any real case.

## Where this stands, October 2026

The sort-key argument is stable and is not controversial: the ordering of the structured primary
survey has been justified this way in teaching for decades, and the re-sorted sequences for
non-perfusing rhythms and for catastrophic haemorrhage are mainstream across the major national
councils. What is not stable is anything more specific — the exact wording of the letters, which
assessments sit under each, the thresholds for escalation, and how the re-sorts are described all
vary between councils and move with each revision cycle. Treat this answer as an explanation of a
principle dated October 2026, and read the current document from the council that governs where
the reader actually works for anything beyond the principle.
