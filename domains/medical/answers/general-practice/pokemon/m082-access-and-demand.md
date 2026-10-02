---
id: "m082"
slug: access-and-demand
style: pokemon
category: general-practice
difficulty: advanced
question: "Why does a system that is easy to enter behave differently from one that is hard to enter, and who does each one filter out?"
tags: [access, demand, triage, capacity, queueing]
---

# Nine levers change how many Pokémon come through the door, and not one of them touches the table

Emerald decides whether your step produces an encounter before it decides what the encounter is,
and the two decisions are made by different code reading different data. The table — twelve slots,
a species and a level in each — belongs to the place. The *rate* belongs to a pipeline of
modifiers that the Trainer carries around with them. Everything in this answer is about that
pipeline, because it is the clearest statement in the games of the difference between how much
need exists and how much of it arrives.

m081 is about the two checks that read a *property* of what was rolled. This answer is about the
checks that read nothing at all and simply throttle the door.

## The pipeline, with the integer arithmetic exactly as the engine does it

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE EMERALD WILD-ENCOUNTER ROUTINE. The
   rate test is: multiply the table's rate by 16, apply the modifiers in this order,
   cap at MAX_ENCOUNTER_RATE = 2880, then pass if Random() % 2880 is under it.

   ROUTE 116, table rate 20.   20 × 16 = 320.   320 / 2880 = 11.1% per eligible step.

     modifier                       what the code does        rate      per step
     ────────────────────────────   ──────────────────────   ──────    ─────────
     nothing                        —                           320      11.1 %
     Mach Bike or Acro Bike         × 80 / 100                   256       8.9 %
     White Flute                    + half of itself             480      16.7 %
     Black Flute                    ÷ 2                          160       5.6 %
     Cleanse Tag on the lead        × 2 / 3                      213       7.4 %
     Illuminate in slot one         × 2                          640      22.2 %
     Arena Trap in slot one         × 2                          640      22.2 %
     Stench in slot one             ÷ 2                          160       5.6 %
     White Smoke in slot one        ÷ 2                          160       5.6 %
     Sand Veil, in desert weather   ÷ 2                          160       5.6 %

     stacked, in the engine's own order:
       bike, Black Flute, Cleanse Tag   320 → 256 → 128 → 85      85       3.0 %
       White Flute, Illuminate          320 → 480 → 960          960      33.3 %

   TEN-FOLD, FROM 3.0% TO 33.3%, ON THE SAME PATCH OF GRASS. And the table is
   byte-for-byte identical in every row of that column: Poochyena, Whismur,
   Nincada, Abra, Taillow, Skitty, at the same levels, in the same twelve slots.

   TWO MORE THINGS IN THE SAME ROUTINE

   the door is a property of the place too       step onto a different tile type and
     Hoenn's land rates are 4, 7, 10, 15, 20     the check is skipped outright 40% of
     and 25. Cave of Origin runs at 4, which     the time — Random() % 100 >= 60, with
     is 64/2880 = 2.2% a step; all six Safari    nothing in the game ever saying so.
     Zone areas run at 25, which is 13.9%.       Pure variation in the door, with no
     Six-fold, decided by the map header.        content and no announcement.

   AND THE CEILING NOBODY REACHES
     MAX_ENCOUNTER_RATE is 2880, which is a table rate of 180. The highest rate in
     Hoenn is 25. Flute and ability together reach 1 200. The cap is written down,
     it is real, and no door in the region can get anywhere near it.
```

## Flutes persist, Repels count down, and that difference is the whole design

A **Repel** has a step counter, decrements once per step, and runs a script to announce its own
expiry. The flutes do not. **White Flute** sets one flag and clears the other; **Black Flute**
does the reverse. There is no counter, no expiry and no message: whichever flag is up stays up,
through every route, until the other flute is used. One act, taken once, changing the door
indefinitely and invisibly.

That is the difference between an access rule with a review date on it and an access rule nobody
remembers making. A Trainer three towns later, wondering why the grass is so quiet, is standing in
a perfectly ordinary table behind a filter they set an hour ago and were never reminded of.

## The door that does not filter at all, and its real cost

**Sweet Scent** is the open door. The field routine is called with its flag word set to zero: no
rate roll, no Repel check, no ability check. One encounter, immediately, drawn from the table
exactly as the table is — including the 1% **Skitty** slot and the 10% **Abra** slot that a
threshold would have removed. It costs one turn and 1 PP out of 20.

Three things follow, and the third is the one Trainers skip:

* **Everything comes through, which is the point.** The rare slot is reachable precisely because
  nothing was throttled, and m048 is the argument for why that matters at the opening of an
  encounter rather than at the end of one.
* **The sorting has not disappeared, it has moved.** With the filters off, the decision about what
  to do with a **Poochyena** is made *after* it is on the screen, by a Trainer who can see it,
  rather than before it exists by a rule that could not. That is a strictly better place to make
  it, and it costs a turn each time.
* **Capacity did not change.** PP is 20. The **Safari Zone** states the same thing without any
  politeness: 30 Safari Balls, a step counter set to 500, and the visit ends when the counter
  runs out rather than when the business is finished.

## Which instrument you arrive with decides which slots exist

The fishing tables are the cleanest version of this and they are not about rate at all. One pond,
ten slots, three rods, and the rod decides which part of the table can be reached: the **Old Rod**
can only ever draw slots 1 and 2, the **Good Rod** slots 3 to 5, the **Super Rod** slots 6 to 10.
A Trainer with an Old Rod who concludes the water is dull has sampled two slots out of ten with
perfect diligence. m030 worked the same three rods for sampling; here the point is narrower — the
route in is not a speed, it is a restriction on what is reachable.

## Where the metaphor stops

The person who cannot get in does not appear in the service's data, so the service does not
experience them as a problem. That is the whole difficulty: the failure is invisible from inside,
and from outside it shows up only as a worse presentation somewhere else, later, usually recorded
as something other than a door that would not open. The attributes that an access system sorts
on — confidence, language, flexible working, transport, childcare, data access, and whether being
believed has been your experience before — are not clinical, and they are distributed in the same
direction as need.

In the other direction, opening a door without the capacity to match it degrades the service for
everybody, including exactly the people the opening was meant to reach, and the first thing that
degrades is the time available per person. That is the resource that complexity needs most.
Neither failure is a moral defect in the people working in the system. Both are properties of a
design, which is the reason they are worth designing rather than apologising for. And the sentence
everyone working in such a system already knows: the person who waited longest on the telephone is
not necessarily the person with the most wrong with them.

## What a Gym Leader is listening for

Whether the Trainer separates the rate from the table without being prompted, and can say which
of the two their own instruments actually touch. Then the stacked arithmetic — 320 down to 85 and
up to 960 — and the observation that the twelve slots never moved. Then the flute-against-Repel
point: which filters announce themselves and which just persist. Then where the sorting goes when
the door opens, and what it costs per encounter. Then the rods, and the difference between
sampling less and being unable to reach a slot at all. Then the hard one: how a Trainer would ever
measure the Pokémon that never arrived.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The access standards, contractual requirements and reporting definitions that apply to the
  reader's own practice, which differ substantially between countries and are revised frequently
  *[country-dependent]*.
* The reader's own organisation's access and workforce data, which is the only place the local
  version of this argument can be settled.
* The published literature on total triage, on same-day access models and on telephone or online
  first contact, for the measured effects on workload, continuity and equity — a literature where
  effects differ by setting and the direction is not uniform.
* A current textbook of health services research or operations management in healthcare, for
  queueing behaviour, variation and the relationship between utilisation and waiting.
* Any systematic review of interventions to improve access for underserved groups, for which
  interventions have been shown to change uptake rather than only availability.

The Pokémon figures are a separate matter and are not covered by the line above. The rate test
multiplying a table's encounter rate by 16 and comparing it against a maximum encounter rate of
2 880, the bike multiplier of 80/100, the White Flute adding half and the Black Flute halving, the
Cleanse Tag's two-thirds, the doubling by Illuminate and Arena Trap, the halving by Stench, White
Smoke and by Sand Veil in overworld sandstorm weather, the order those modifiers are applied in,
the forty-per-cent skip when stepping onto a different metatile behaviour, the Hoenn land rates of
4, 7, 10, 15, 20 and 25 with Cave of Origin at the bottom and the six Safari Zone areas at the
top, the Route 116 table, Sweet Scent's field call passing a flag word of zero and its 20 PP, the
Safari Zone's 30 balls and 500-step counter, the flute flags persisting with no counter, the Repel
step counter and its expiry script, and the Old, Good and Super Rod slot groupings of two, three
and five slots, were all read directly from the pret decompilation projects, which this
environment can reach.

## Scope and safety

This is revision material about how an access system behaves, written for someone already
training in or qualified for the field. It is not a clinical reference, not a decision aid, and
not for use in making a decision about any person's care. No access standard, waiting-time target
or triage category is named here on purpose: all of them are local, several are contractual, and
all are revised. The encounter rates above are real and stand in for a mechanism; none of them is
a clinical quantity and no clinical figure should be read out of them. Nothing here describes how
any individual should seek care. If someone is unwell right now, the relevant action is to contact
local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The structural claims — that a barrier changes demand and utilisation but not need, that every
access system filters on some attribute, and that an open door moves the sorting inside where
there is information to do it with — are mainstream and stable. What moves is everything
operational: access standards, contractual targets, the balance between telephone, online and
in-person entry, and the evidence on what opening a door does to total workload. Digital-first
access has been introduced, evaluated and partially reversed in several systems over the last
decade, and the evidence on its equity effects is arriving rather than settled. The Emerald
numbers are stable because the games are finished. Take access standards and definitions from
current local requirements rather than from here, as of October 2026.
