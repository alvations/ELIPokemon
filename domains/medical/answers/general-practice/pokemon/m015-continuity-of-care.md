---
id: "m015"
slug: continuity-of-care
style: pokemon
category: general-practice
difficulty: intermediate
question: "What does continuity of care actually buy, and why is it a clinical intervention rather than a courtesy?"
tags: [continuity, relational-continuity, handover, trust, records]
---

# A Pokémon that someone else raised does not do what it is told, and that is in the code

Start by splitting the word, because three different things get called continuity and they come
apart:

* **The same Trainer.** You are the **Original Trainer**: your name and your **ID No.** are
  printed on the summary screen and they never change.
* **The same record.** Species, level, the four moves, the PP left in each, what it is holding —
  all legible to anybody who opens the screen.
* **The same plan.** The move you chose on the menu is the move that actually gets used.

A party can have a perfect record and no shared history at all. Naming which one is meant is most
of the argument, because the game treats them completely differently — and one of them it enforces
in code.

## The mechanism, which is the mechanism from the encounter tables again

Being the Original Trainer supplies a prior about **one** Pokémon rather than about a table. Any
Trainer can read the slot chances off a route. Only the one who raised a **Charmander** from level
5 knows which of its four moves actually finishes things, what it does when it is nearly out of
HP, and the signal that has no substitute anywhere else — *this is not how it usually goes*.

```
   WHAT THE SUMMARY SCREEN CARRIES, AND WHAT ONLY THE ORIGINAL TRAINER CARRIES

   ┌─────────────────────────────────┬────────────────┬───────────────────────────────┐
   │ information                     │ on the screen? │ needs the same Trainer?       │
   ├─────────────────────────────────┼────────────────┼───────────────────────────────┤
   │ species, level, moves, PP, item │  yes           │  no                           │
   │ OT name and ID No.              │  yes           │  no                           │
   │ what it has already fainted to  │  no            │  no — write it down           │
   │ which move it really wins with  │  no            │  mostly                       │
   │ what it does at low HP          │  no            │  yes                          │
   │ whether this is normal for it   │  no            │  yes                          │
   │ whether it obeys you at all     │  no            │  YES, and the game decides    │
   │                                 │                │  this one in code             │
   └─────────────────────────────────┴────────────────┴───────────────────────────────┘

   The top three rows are a records problem and are fixed by writing things down. The
   bottom four are not, and they are the whole reason the same Trainer is worth something.
```

Everything in the lower half changes what you expect before you press anything, which makes it
information in exactly the sense that a type match-up is information.

## What the game charges for discontinuity

```
   REAL NUMBERS, from Red and Blue. If a Pokémon's Original Trainer ID does not match
   yours, it obeys reliably only up to a level set by your badges — and only four of the
   eight badges are consulted at all.

   badges held                       obeys reliably up to
   ───────────────────────────────   ────────────────────
   none of the four                  level  10
   Cascade Badge   (Misty)           level  30
   Rainbow Badge   (Erika)           level  50
   Marsh Badge     (Sabrina)         level  70
   Earth Badge     (Giovanni)        every level

   The Boulder, Thunder, Soul and Volcano Badges do not enter the check. Above the line
   the Pokémon may loaf around, turn away, ignore the order, fall asleep on the spot,
   hurt itself in confusion — or use a move you did not choose.

   That last failure needs more than one move to be possible, so a Pokémon with a single
   move does nothing at all instead. Discontinuity does not degrade gracefully.
```

That is the clearest statement of the point available anywhere. The plan does not fail because the
Pokémon is weak or because the Trainer gave a bad instruction. It fails because the instruction
came from someone it has no history with, and the fix is not a better instruction.

## What continuity buys, stated honestly

Friendship is the accumulating part, and the engine's arithmetic is specific about it:

* It rises in small increments, and the increments **get smaller as it rises** — the table has
  tiers above 99 and above 199, so the early history is worth more per event than the late
  history.
* Walking together counts: there is a friendship event with a one-in-two chance every 128 steps.
  It accrues from time spent, not from any single impressive act.
* A **Soothe Bell** increases every positive gain by half, a **Luxury Ball** adds one more on top
  of each, and — the detail worth stopping on — a Pokémon gains **one extra point for every good
  thing that happens in the same region where you met it**. Being seen where you were first met is
  mechanically worth something.

And now the part a careful Trainer has to concede. A traded Pokémon earns **1.5× the experience**
of one you caught yourself. So if the measure is how fast it levels, trading wins; if the measure
is whether the move you picked is the move that happens, trading loses. The two measures disagree,
and anyone who quotes only one of them is making an argument rather than a measurement. The honest
position is a consistent direction with a contested size, which is why no single figure is offered
here as the value of continuity.

## Why it is something you build, not something you are

Three tests: it can be designed, it can be measured, and it can be given in different amounts.

* **Designed.** The badge order is the design. **Brock** in **Pewter City**, then **Misty** in
  **Cerulean City**, then **Lt. Surge** in **Vermilion City**, then **Erika** in **Celadon City**,
  **Koga** in **Fuchsia City**, Sabrina in **Saffron City**, **Blaine** on **Cinnabar Island** and
  **Giovanni** in **Viridian City**. Authority is earned in a fixed order and cannot be wished
  for.
* **Measured.** The OT name and the ID No. are printed on the screen, so whether this is your
  Pokémon is a fact you can read rather than a feeling. What the screen does *not* tell you is
  which threshold you are currently under, which is the part people get wrong.
* **Given in amounts.** A traded level-8 Pokémon obeys perfectly well with no badges at all. A
  traded level-55 one with only the Rainbow Badge does not. The mechanism bites hardest exactly
  where the stakes are highest, which is the argument for concentrating it there.

## The tradeoffs, which are real

* **It competes with raw strength.** The **Dragonair** somebody traded you is level 40 and the
  **Ivysaur** you raised is level 24. Sometimes the right call is the one that might not listen.
* **A long history anchors as well as informs.** The Trainer who raised a Charmander from level 5
  is also the one who never noticed that **Charizard** still has **Scratch** in the first slot,
  because it has been there the whole time. Familiarity makes that easier to miss, not harder.
* **One Pokémon holding everything is a single point of failure.** If exactly one of the six knows
  **Surf**, the plan dies the moment it faints.
* **It costs time, in 128-step increments**, and an arrangement that depends on goodwill rather
  than on design does not survive a long route.
* **The rules differ between games.** The thresholds above are Red and Blue's. Later generations
  check differently, so the numbers do not travel even though the mechanism does.

## Where the metaphor stops

The people for whom continuity of care matters most are generally those least able to arrange it:
people who cannot telephone at a fixed time of day, who cannot wait several weeks to see one named
clinician, whose first language is not the system's, or who have previously not been believed. If
continuity is handed out according to who can work a booking system, it reaches the people who
need it least. Treating it as something a service designs, rather than something an individual
clinician offers out of goodwill, is what makes it possible to allocate at all.

## What a Gym Leader is listening for

Whether the Trainer splits the three kinds of continuity without being asked. Then the mechanism —
a prior about this one Pokémon, not an atmosphere. Then the confounding, argued in both
directions, including the 1.5× experience that cuts the other way. Then the trade against raw
strength, and who gets the obedient one. Then the hard case: the battle lost precisely because the
Trainer knew the Pokémon so well that they stopped reading the screen.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The curriculum and professional-standards documents of the reader's own college or training body
  for general practice, for how continuity is defined and what is formally expected.
* Any systematic review of continuity of care and its outcomes, in the primary-care or
  health-services-research literature, for the direction and consistency of the association and
  for the authors' own assessment of confounding.
* The methods section of whichever continuity index a reader intends to quote, issued by the group
  that published it, for how it handles people with very few or very many contacts.
* The reader's own national primary-care policy framework, which determines whether continuity is
  the default to protect or something to construct *[country-dependent]*.
* The reader's own organisation's registration, booking and named-clinician arrangements, which
  are the only authority on what continuity is actually achievable locally.

The Pokémon figures are a separate matter and are not covered by the line above. The obedience
thresholds and the four badges consulted, the named failure behaviours including the substituted
move and the one-move exception, the 1.5× experience for a traded Pokémon, the friendship tiers at
99 and 199, the one-in-two event every 128 steps, the Soothe Bell and Luxury Ball modifiers and
the extra point for being in the region where it was met, were all read directly from the pret
decompilation projects, which this environment can reach.

## Scope and safety

This is revision material about how a service is organised and why that organisation has clinical
effects, written for someone already training in or qualified for the field. It is not a clinical
reference, not a decision aid, and not for use in making a decision about any person's care. No
effect size is quoted, because the evidence is observational and the estimates are contested. The
Pokémon numbers are real and stand in for a mechanism; no clinical figure should be read out of
them. How registration, booking and continuity work differs substantially between health systems,
and local arrangements are the authority on what is possible — this is not. If someone is unwell
right now, the relevant action is to contact local urgent care or the local emergency number, not
to read this.

## Where this stands, October 2026

The three-way split, and the mechanism by which knowing one person over time carries diagnostic
information, are settled and stable. The association with outcomes is consistent in direction and
contested in magnitude, and that has not changed. What is moving quickly is the delivery context:
remote and asynchronous consulting, triage-first access, larger organisational groupings, and
records that follow a person between providers. Several of those improve the record while making
the relationship harder, which is exactly why the three need separating. Re-check local
arrangements rather than assuming them. The Red and Blue obedience numbers are stable because the
games are finished. Correct as a description of consensus in October 2026.
