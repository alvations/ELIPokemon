---
id: "m076"
slug: tolerance-dependence-and-withdrawal
style: pokemon
category: pharmacology
difficulty: intermediate
question: "Tolerance, physical dependence and addiction are routinely used as if they were one thing. What is the mechanistic difference between them, and what does each one actually predict?"
tags: [tolerance, dependence, withdrawal, receptor-adaptation, deprescribing]
---

# Protect, Detect and Endure share one counter, and using any of them halves the next one.

Three words get used as one word. The Game Boy Advance code separates them with three different
mechanics, and the separation is exact enough to argue from.

**Tolerance** is `sProtectSuccessRates` — a four-entry table that halves. **Dependence** is
**Belly Drum**, which pays in a currency **Haze** cannot refund. And the third word has no
mechanic at all, which is the correct answer and is where this half stops talking in Pokémon.

```
   static const u16 sProtectSuccessRates[] =
       { USHRT_MAX, USHRT_MAX / 2, USHRT_MAX / 4, USHRT_MAX / 8 };

   uses so far      0         1         2         3
   rate         65535     32767     16383      8191
   chance        1/1       1/2       1/4       1/8
                  ▲
                  USHRT_MAX is compared with a u16 draw, so the FIRST use is
                  certain. Nothing was wrong with the first one. Nothing is
                  wrong with the fourth either -- the printed move data for
                  Protect is identical on both occasions.
```

That last line is the whole of pharmacodynamic tolerance. **Protect** has power 0, accuracy 0 and
10 PP on the fourth use exactly as on the first. The dose did not change, the delivery did not
change, and the effect fell by seven eighths. You cannot find that in the move data, because it is
not in the move data; it is in `gDisableStructs[battler].protectUses`, which nothing displays.

## Cross-tolerance, written into the code as one counter for three moves

`Cmd_setprotectlike` opens with a single test, and the test is the interesting part:

```
   if (lastMove != MOVE_PROTECT && lastMove != MOVE_DETECT && lastMove != MOVE_ENDURE)
       gDisableStructs[attacker].protectUses = 0;

   lastMove is gLastResultingMoves[attacker] -- the last one that actually resolved.

   THREE MOVES, ONE COUNTER:
     Protect   EFFECT_PROTECT,  power 0, accuracy 0, 10 PP, MOVE_TARGET_USER
     Detect    EFFECT_PROTECT,  power 0, accuracy 0,  5 PP, MOVE_TARGET_USER
     Endure    EFFECT_ENDURE,   power 0, accuracy 0, 10 PP, MOVE_TARGET_USER

   Protect and Detect are the SAME effect id with different supply. Endure is a
   DIFFERENT effect id and shares the counter anyway.
```

So **Protect**, **Protect**, **Detect** runs the counter to 1/8 just as three **Protect**s would.
Swapping to **Detect** because the first agent "stopped working" buys nothing at all, and the
reason is visible in one line of C: the counter is keyed to the mechanism, not to the move. That
is cross-tolerance, and it is why it follows the receptor rather than the chemical family.

Now use **Swords Dance** instead, and the next **Protect** is certain again. One intervening
resolution zeroes the counter. A drug-free interval is the one thing that restores the response,
and the code agrees: so does leaving the field. `SwitchInClearSetData` byte-zeroes the whole
`struct DisableStruct`, and **Baton Pass**'s hand-written list of five preserved fields — the
`substituteHP`, the sure-hit battler, the two **Perish Song** timers and the escape-preventer —
does **not** include `protectUses`. Tolerance does not travel. `m070` is the rest of that list.

## The two routes, and why only one of them is findable

`m044` already did the other route. There, what fell was the fraction arriving: **Zap Cannon** at
accuracy 50 delivers all of half its uses, and **Light Screen** takes its cut before the number
reaches you. Measure what arrives and you can see that kind of failure.

Here nothing about arrival changed. **Protect** cost its PP, resolved, and did less. Measuring the
delivered dose would have told you nothing, which is exactly the asymmetry `m041` is built on: a
concentration finds dispositional tolerance and is blind to functional tolerance.

## The same shape with the sign reversed

The games contain the opposite counter in the same struct, which is the best evidence that the
shape is general rather than a quirk of **Protect**.

```
   Cmd_furycuttercalc

     if (furyCutterCounter != 5) furyCutterCounter++;
     gDynamicBasePower = gBattleMoves[gCurrentMove].power;          // Fury Cutter: 10
     for (i = 1; i < furyCutterCounter; i++) gDynamicBasePower *= 2;

   consecutive uses     1     2     3     4     5     6
   delivered power     10    20    40    80   160   160
                                                     ▲
                                                     the cap, at counter 5

   cleared by: a MOVE_RESULT_NO_EFFECT result (the counter goes to 0 in the same
   routine), ClearFuryCutterDestinyBondGrudge, and CancelMultiTurnMoves.
```

One struct, two counters, opposite signs, the same reset rule. **Fury Cutter** sensitises on
repetition and **Protect** tolerates on repetition, and neither touches the printed power of
anything. Repetition changing a response is not a property of the agent. It is a property of what
the repetition is doing to the machinery.

## Escalation runs into a ceiling that is written down

```
   Stockpile:      if (stockpileCounter == 3) -> MOVE_RESULT_MISSED, "can't stockpile any more"
   stat stages:    MIN_STAT_STAGE 0, DEFAULT_STAT_STAGE 6, MAX_STAT_STAGE 12   (so -6 .. +6)
   Swords Dance:   at MAX_STAT_STAGE it does nothing, and says so
```

Three ceilings, all explicit. The reason this belongs beside tolerance is that escalating against
a tolerated effect is the natural response to it, and the game is blunt about where that ends:
**Stockpile** refuses the fourth, **Swords Dance** refuses the seventh stage, and neither refusal
is a failure of the move.

## Dependence: Belly Drum pays in a currency Haze cannot refund

`Cmd_maxattackhalvehp` is four lines and every one of them is load-bearing.

```
   halfHp = maxHP / 2;  (floored to 1 if maxHP / 2 is 0)

   SUCCEEDS only if   statStages[STAT_ATK] < MAX_STAT_STAGE
                AND   hp > halfHp
   then               statStages[STAT_ATK] = MAX_STAT_STAGE   (set, not incremented)
                      and maxHP / 2 is taken

   NOW REMOVE IT:
     Haze (power 0, accuracy 0, 30 PP, MOVE_TARGET_USER) sets every stage back to
       DEFAULT_STAT_STAGE for every battler, and returns not one point of HP.
     Leaving the field does the same: SwitchInClearSetData resets statStages to
       DEFAULT_STAT_STAGE, and HP is in gBattleMons[].hp, which it does not touch.

   Benefit: removable, two ways.          Cost: permanent, both ways.
```

That asymmetry is the whole of what physical dependence is. The adaptation was paid for out of
something that does not come back, so taking the agent away does not return the system to where it
started — it returns it to where it started *minus the adaptation*, which is a different place.
**Blissey** with 255 base HP pays an enormous **Belly Drum** bill and **Shuckle** with 20 pays a
trivial one, and `m006`'s point holds here too: the fraction is the same and the quantities are
nothing alike.

The other half of the mechanism is the refusal condition. **Belly Drum** *fails* when HP is
already at or below half. A system with no reserve cannot build the adaptation in the first place,
and the game checks before it charges rather than after.

## What the counter is not

Two honest limits, because the mapping is exact in one place and silent in another.

**Duration is set somewhere else entirely.** **Disable** writes `disableTimer = (Random() & 3) +
2` — between two and five, drawn at the moment it lands — and the Protect counter has no timer at
all. Nothing in the games makes the recovery of an adapted response depend on how long the agent
takes to clear, which is the one piece of real kinetics this analogy cannot carry. `m006` has it.

**And nothing in Pokémon is a withdrawal syndrome.** There is no mechanic in which removing
something produces a new set of effects pointing the other way. **Haze** clears stages and
**Rest** restores HP at the cost of two turns asleep, and neither of those is a rebound. The
closest the code gets is the ledger asymmetry above, which is where the adaptation *lives*, not
what it feels like. The feeling is a human matter and it is handled below, out of the metaphor.

## Where the metaphor stops

Everything above is mechanism. The third of the three words is not a mechanism, and this is the
part of the topic where the vocabulary has done measurable harm — in both directions.

A substance use disorder is a clinical diagnosis about a pattern of behaviour, assessed against
published criteria, and it cannot be read off a receptor, a counter or a dose. Both of the major
international classification systems state explicitly that tolerance and physical dependence are
not themselves diagnostic criteria in a person taking a prescribed drug as prescribed. That
statement had to be written down because the failure to make it was common and costly.

In one direction, people with pain have had analgesia withheld or reduced because tolerance or a
withdrawal syndrome was read as evidence of addiction. The term coined for the behaviour this
produces — drug-seeking that resolves once the pain is adequately treated — exists because the
misclassification was frequent enough to need a name, and the cost of it falls hardest on people
who are already least likely to be believed.

In the other direction, the reassurance that physical dependence "is not addiction" has been used
to minimise real risk, and that minimisation contributed to a prescribing pattern with severe
consequences in several countries. Both errors come from collapsing three different claims into
one and then arguing about which one it is.

The practical consequence is plain. Stopping a drug the body has adapted to is itself a clinical
event with its own risks, and for some classes those risks are serious. How that is done is a
matter for the person's own prescriber and their national guidance; nothing in this pair describes
how any medicine should be reduced or stopped, for anyone. Anyone worried about a medicine they
are taking should raise it before changing anything, because the change is the risky part and it
is manageable when it is planned.

And a note about words, which is not decoration: "addict", "abuse" and "clean" are being replaced
in professional writing by terms describing the condition rather than the person, and the reason
given is empirical — stigmatising terminology measurably changes how clinicians assess the same
described case.

## What a Gym Leader is listening for

* Why does **Protect**, **Protect**, **Detect** leave the counter at 1/8 rather than resetting it?
* **Protect**'s printed data is identical on the fourth use. So what changed, and where is it
  kept?
* Which kind of tolerance would measuring the delivered dose have found, and which would it miss?
* **Fury Cutter** and **Protect** sit in the same struct with opposite signs. What does that tell
  you about whether repetition-dependence is a property of the agent?
* **Belly Drum**, then **Haze**. What came back and what did not, and why is that the definition?
* Why does **Belly Drum** fail outright below half HP, and what does the check correspond to?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **Both major international classification systems' chapters on substance-related and addictive
  disorders**, for the diagnostic criteria, the current names of the diagnoses, and the explicit
  statements about tolerance and dependence in people taking prescribed drugs as prescribed. The
  two differ, each has been revised, and neither should be quoted from memory.
* **Your national guidance on withdrawing and reducing dependence-forming medicines**, which
  several countries now publish separately. It is the document that answers the practical question
  this pair deliberately does not.
* **Your national formulary's monograph** for any specific drug, for whether dependence is
  expected, what is said about stopping it, and what is said about tolerance to its separate
  effects.
* **A current clinical pharmacology textbook's chapter on tolerance and receptor regulation**, for
  down-regulation, desensitisation, uncoupling and mediator depletion, and for the distinction
  between tachyphylaxis and tolerance.
* **Your national pain guidance**, for the opioid-specific material on how differently the several
  effects of one drug tolerate. Country-dependent and revised.

The Pokémon figures are a different matter and were read directly from the public decompilation of
the Game Boy Advance games rather than recalled: `sProtectSuccessRates` holding `USHRT_MAX,
USHRT_MAX / 2, USHRT_MAX / 4, USHRT_MAX / 8` and being compared with a `u16` draw;
`Cmd_setprotectlike` zeroing `protectUses` unless `gLastResultingMoves` was Protect, Detect or
Endure, incrementing it on success and zeroing it on failure; Protect and Detect both carrying
`EFFECT_PROTECT` with 10 and 5 PP and Endure carrying `EFFECT_ENDURE`; `Cmd_furycuttercalc`
capping its counter at 5 and doubling Fury Cutter's base power of 10 once per step;
`ClearFuryCutterDestinyBondGrudge` and `CancelMultiTurnMoves` clearing that counter;
`Cmd_stockpile` refusing at a counter of 3; `MIN_STAT_STAGE` 0, `DEFAULT_STAT_STAGE` 6 and
`MAX_STAT_STAGE` 12; `Cmd_maxattackhalvehp` requiring Attack below `MAX_STAT_STAGE` and HP
strictly above `maxHP / 2`, then setting the stage to the maximum and charging `maxHP / 2`; Haze's
data and its reset of every stage; `SwitchInClearSetData` byte-zeroing the whole `struct
DisableStruct`, restoring `DEFAULT_STAT_STAGE`, and Baton Pass preserving only `substituteHP`,
`battlerWithSureHit`, the two Perish Song timers and `battlerPreventingEscape`;
`Cmd_disablelastusedattack` setting `(Random() & 3) + 2`; and Blissey's base HP of 255 against
Shuckle's 20. The arithmetic in the blocks above is recomputed from those figures.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** Neither half
contains a dose, a tapering rate, a withdrawal timeline or an incidence figure, deliberately:
those are drug-specific, they differ between countries, and the formulary and your national
withdrawal guidance are the authorities. Nothing here indicates how any medicine should be reduced
or stopped. Stopping a drug the body has adapted to is itself a clinical event and for some
classes it is dangerous; anyone concerned about a medicine they are taking should discuss it with
their own prescriber or pharmacist rather than act on anything read here. The diagnostic material
is described, not reproduced — the classification systems are the only authority for their own
criteria.

## Where this stands, October 2026

The mechanistic content is mechanism and does not date, and the game mechanics quoted are fixed in
released software — though the series has changed several of them between generations, and this
answer pins every figure it uses to the Game Boy Advance games. Three things do date. The
**diagnostic criteria and the names of the diagnoses** have been revised more than once in both
classification systems, and the current wording is theirs. The **national guidance on reducing
dependence-forming medicines** is recent in several countries, is not uniform between them, and is
being revised. And the **terminology** is moving rather than settled. Check the classification
system you work under and your own national guidance.
