---
id: "m012"
slug: red-flags-and-safety-netting
style: pokemon
category: general-practice
difficulty: advanced
question: "What is safety-netting actually for, and what separates a safety-net that works from reassurance that only sounds like one?"
tags: [safety-netting, red-flags, uncertainty, documentation, diagnostic-delay]
---

# You do not clear Mt. Moon of Clefairy by meeting ten Zubat

Walk into **Mt. Moon** looking for a **Clefairy** and the ordinary outcome is that you do not find
one. The table on the first floor is 202/256 **Zubat**, 38/256 **Geodude**, 13/256 **Paras** and
3/256 Clefairy, and the per-step encounter rate is 10/256, so a lap of the floor that produces ten
encounters and no Clefairy is not evidence of anything. It is the expected result. Ending a visit
without the thing you came for is the normal case, not a failure.

What a good Trainer does with that is the subject here. The plan is not "there is no Clefairy" and
it is not "I will keep wandering until something happens". It is a **Max Repel** with 250 counted
steps on it, an **Escape Rope** in a known bag slot, a named trigger, and an entry in the
**Pokédex** under SEEN that says the thing is still open. That is a net. It substitutes for
certainty it cannot get, and it has a mechanism.

## The rare slot: what it tells you and what it does not

A rare slot is a slot you act on the moment it appears — slot 10 on Mt. Moon 1F is Clefairy at
3/256 and it is worth a **Poké Ball** every time. Two consequences matter more than any list of
which slot is where:

* **A rare slot is tuned for being unmistakable, which makes it a terrible way to exclude
  anything.** Most of what you are hunting does not announce itself. On Mt. Moon B2F, Clefairy
  sits in *two* slots at two different levels, and whichever one you learn to look for, the other
  one walks past you.
* **Which slot is rare is a local fact.** Clefairy is 3/256 on 1F, 11/256 on B1F and 16/256 on
  B2F. One cave. Three floors. Nobody should carry a slot list between them.

Here is what a reading that is unmistakable-but-narrow actually leaves behind. Take Mt. Moon B2F,
where Clefairy holds slot 8 at level 10 and slot 10 at level 12, and use the narrow reading — *the
number on the screen is 12*.

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE MT. MOON B2F ENCOUNTER TABLE. The slot
   chances are 51 51 39 25 25 25 13 13 11 3 out of 256 in slot order, as on every land table.

   256 rolls of the B2F table.   Clefairy: slot 8 (13/256, lvl 10) + slot 10 (3/256, lvl 12)

   ┌───────────────────┬───────────────┬───────────────┬───────────────┐
   │                   │  Clefairy     │  not it       │  total        │
   ├───────────────────┼───────────────┼───────────────┼───────────────┤
   │  screen reads 12  │            3  │           24  │           27  │
   │  reads anything   │           13  │          216  │          229  │
   │  else             │               │               │               │
   ├───────────────────┼───────────────┼───────────────┼───────────────┤
   │  total            │           16  │          240  │          256  │
   └───────────────────┴───────────────┴───────────────┴───────────────┘

   catches only          3 / 16  = 18.8 %      clears      216 / 240 = 90.0 %
   before the reading   16 / 256 =  6.25 %
   after it comes back  13 / 229 =  5.68 %     negative

   A reading that is right nine times in ten when it says no, and still moved the number
   from 6.25 % to 5.68 %. Thirteen of the sixteen Clefairy are sitting inside the group it
   just cleared — about one in every eighteen rolls it waved through.
```

And the other arithmetic, the one every Trainer feels and nobody does. On 1F, Clefairy is 3/256 of
a 10/256 step, so the chance per step is 30/65 536 — one Clefairy every **2 185 steps** on
average, and about **6 540 steps** before a Trainer could honestly say that meeting none was
surprising. Ten encounters leave (253/256)¹⁰ = **88.9%** of the original doubt standing.

That is the design constraint. The net gets cast over an enormous amount of ordinary grass, so it
has to be cheap, specific, and not frightening — and it still has to work.

## The anatomy of a net that works

```
   ┌────────────────────┬──────────────────────────────────┬────────────────────────────┐
   │ component          │ a net                            │ reassuring noise           │
   ├────────────────────┼──────────────────────────────────┼────────────────────────────┤
   │ what is being      │ Clefairy, named, slot 10, still  │ nothing named              │
   │ watched for        │ open in the Pokédex under SEEN   │                            │
   │ trigger            │ a number on the screen that can  │ "watch out in there"       │
   │                    │ actually be read off it          │                            │
   │ timeframe          │ Max Repel, 250 steps, and the    │ open-ended                 │
   │                    │ game tells you when it wore off  │                            │
   │ action             │ Escape Rope, bag slot known, and │ "head back if it goes bad" │
   │                    │ it only works in a cavern        │                            │
   │ who holds it       │ the step counter and the save,   │ the Trainer's memory       │
   │                    │ not the Trainer's memory         │                            │
   │ recorded           │ SEEN and OWN are separate        │ in one Trainer's head      │
   │                    │ counters, so the gap is visible  │                            │
   │ checked            │ the Pewter City Pokemon Center   │ assumed                    │
   │                    │ was confirmed to be behind you   │                            │
   │                    │ before you went in               │                            │
   └────────────────────┴──────────────────────────────────┴────────────────────────────┘
```

Four of those deserve their reasons stated.

**The trigger has to be something readable.** "If it looks dangerous" is not a trigger. The level
is, because it is printed on the screen. And it matters that the printed number means what you
think: Zubat learns Supersonic at level 10 and Confuse Ray only at level 21, so nothing in Mt.
Moon's table has Confuse Ray yet. The thing that will eventually be a problem is not yet showing
the feature that makes it recognisable.

**The step count is what turns doubt into a decision.** A **Super Repel** is 200 steps and a Max
Repel is 250, and the engine counts them down and prints a message when the last one is spent. "It
seems fine in here" and "250 steps, and after that the plan changes" are different statements, and
only the second one has a mechanism. A net with no counter on it is a deferral.

**Recording it is part of the plan, not the tidying up afterwards.** SEEN and OWN are separate
numbers in the Pokédex for a reason: the first is what you have met and the second is what you
have confirmed, and the gap between them is the list of things still open. A Trainer who keeps
that list in their head loses it exactly when it is needed — on the next visit, which may not be
theirs.

**Netting everything is netting nothing.** The reading above waves through about seventeen
ordinary rolls for every Clefairy it misses. Burning a Max Repel on every patch of grass in Kanto
empties the bag, costs the money that buys **Potion**s, and teaches you to ignore the message when
it finally matters.

## Where the metaphor stops

Diagnostic delay is the mechanism behind a large share of serious harm in first-contact care, and
the two named most often are delayed cancer diagnosis and the deterioration of an infection that
looked unremarkable at first presentation. In a substantial proportion of those cases the
contributory factor is not a missed clue: it is a plan that had no trigger, no date and no record.
That is also the hopeful part, because it is the kind of failure a designed process reduces.

And a second thing that belongs here rather than in a metaphor. The people for whom a safety-net
is most likely to fail are the ones least able to come back — language, work, caring
responsibilities, cost, transport, confidence, or having previously not been believed. A net built
around an articulate, available, confident person is not a net for them. Active recall, instead of
relying on someone returning, is the part of this that is genuinely difficult and genuinely
matters.

## What a Gym Leader is listening for

Whether the Trainer can say what the chance still was when they walked out, and whether the net
was sized for it. Then the exact wording of the trigger, out loud. Then whether the way out was
checked — an Escape Rope does nothing on a route, because it only works in the forest, cemetery,
cavern, facility and interior tilesets. Then the awkward one: what happens when the net is set and
nobody comes back, and how you tell a floor that was genuinely empty from a Trainer who could not
return to it.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The suspected-cancer and urgent-referral criteria issued by the national or regional body
  governing the reader's practice, for the red-flag thresholds themselves (**country-dependent**).
* The curriculum and assessment guidance of the reader's own college or training body for general
  practice, for what safety-netting is formally expected to contain.
* The reader's own organisation's significant-event and serious-incident framework, which is where
  the local evidence about how nets fail actually lives.
* Any systematic review of diagnostic error and diagnostic delay in primary care, in the
  patient-safety literature, for the recurring contributory factors.
* The national patient-safety or healthcare-inspection body's published reports on diagnostic
  delay for the reader's country (**country-dependent**).

The Pokémon figures are a separate matter and are not covered by the line above. The encounter
tables and rates for Mt. Moon 1F, B1F and B2F, the ten slot chances, the Repel step counts and the
message printed when one expires, Zubat's level-10 Supersonic and level-21 Confuse Ray, and the
five tilesets an Escape Rope works in, were all read directly from the pret decompilation
projects, which this environment can reach.

## Scope and safety

This is revision material about how a clinical process is designed, written for someone already
training in or qualified for the field. It is not a clinical reference, not a decision aid, and
not for use in making a decision about any person's care. It contains no red-flag list on purpose:
those lists are local, they are revised, and the authoritative version is the one issued for the
reader's own setting. The encounter numbers are real and are standing in for a mechanism; no
clinical figure should be read out of them. If someone is unwell right now, the relevant action is
to contact local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The reasoning — that a net substitutes for certainty and should therefore be specified like any
other intervention — is mainstream and stable. The thresholds it refers to are not: they are
revised regularly and differ between countries, so none is reproduced here. Access routes,
out-of-hours arrangements and recall mechanisms also change at short notice, so the route named in
any net needs confirming at the time rather than remembered. The Mt. Moon numbers are from Red and
Blue and are stable because the games are finished. Correct as a description of consensus in
October 2026.
