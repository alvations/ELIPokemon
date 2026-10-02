---
id: "m042"
slug: renal-and-hepatic-impairment
style: pokemon
category: pharmacology
difficulty: advanced
question: "Why do renal and hepatic impairment change prescribing in different ways, and why is there a usable number for one of them and not for the other?"
tags: [renal-impairment, hepatic-impairment, first-pass, protein-binding, clearance]
---

# A weaker Seismic Toss is one number. Losing Blissey is four problems at once.

**Seismic Toss** removes exactly the user's level in HP. The battle script runs `dmgtolevel` and
then `adjustsetdamage`, so it never touches the 85-to-100-per-cent random multiplier that every
ordinary attack goes through: at level 100 it takes 100, at level 50 it takes 50, every single
time, from anything it can hit. One mechanic, one number, and the number is printed on the
Pokémon.

**Blissey** is the opposite kind of fact. Base HP 255 and base Special Defence 135, against base
Attack 10 and base Defence 10 — and from its own level-up learnset, **Soft-Boiled** at level 10
and **Light Screen** at level 40, with **Natural Cure** or **Serene Grace** in the ability slot.
That is one party member doing four separate jobs, and there is no single number that tells you
how much of it is left.

`m006` established the leak as clearance. This answer is about the difference between a leak
getting weaker and a *role* disappearing.

## The gradable one

```
   SEISMIC TOSS as the only route off the bar.  Blissey's own bar, level 100,
   perfect HP stat and the full 252 effort points, is 714 (the formula is in m006).

   user's level   HP removed per turn   turns to empty 714   healing needed to FILL it
   ───────────────────────────────────────────────────────────────────────────────────
       100               100                     8                      714
        50                50                    15                      714
        25                25                    29                      714
   ───────────────────────────────────────────────────────────────────────────────────
                          ▲                      ▲                        ▲
                   HALVES exactly        DOUBLES exactly          DOES NOT MOVE

   Three things follow and all three are arithmetic, not judgement:
     · the leak is a single quantity you can read off the level;
     · halving it exactly doubles the time, because there is no roll on it;
     · and it has NOTHING to do with how much it takes to fill the bar.
   Getting that last one backwards is the standard error, and m006 says so too.
```

**And the one place the number lies.** **Spikes** does not work like that. In the Game Boy Advance
games the entry damage is `maxHP / ((5 − layers) × 2)` — an eighth for one layer, a sixth for two,
a quarter for three. That is a **fraction of the holder**, so one layer takes 89 off Blissey's 714
and 2 off **Shedinja**'s hard-coded 1. **Seismic Toss** is flat and does not scale at all.

So a quantity expressed as a fraction of a standard body does the wrong thing on an unusual body,
and a flat quantity does the wrong thing on every body but one. Knowing which of the two you are
holding is the whole of why a routinely reported estimate and a narrow-margin decision want
different numbers.

## The ungradable one

Take Blissey out and count what left with it:

| The job | The mechanic, from the games | What replacing it costs |
| --- | --- | --- |
| Restoration | **Soft-Boiled**, learnt at level 10 | A move slot on something else, at worse HP |
| The barrier | **Light Screen**, learnt at level 40, halves incoming special damage for your whole side | A move slot, and five turns of upkeep |
| The wall itself | Base HP 255 and base Special Defence 135 | Nothing in the Kanto or Hoenn dex matches it |
| Clearing status | **Natural Cure** wipes `status1` to zero on switch-out | An ability slot, which is not transferable |

Four jobs, four different replacements, and they are not even the same *kind* of thing — two
moves, a stat line and an ability. **Chansey** carries the same ability pair and learns
Soft-Boiled at 13 and Light Screen at 49, so the shape survives the evolution; what changes is the
magnitude, and the magnitude is the part a level would have told you.

There is no reading for "how much Blissey". A level is a number. A role is a list.

## The barrier, which is the sharp one

**Light Screen** is first-pass extraction, and the damage routine is precise enough to make the
analogy exact.

```
   An incoming SPECIAL hit computes to 160 before the screen is consulted.

   situation                                        what ARRIVES     why
   ────────────────────────────────────────────────────────────────────────────────────
   Light Screen up, single battle                        80          damage / 2
   Light Screen up, double battle, two defenders alive  106          2 × (damage / 3)
   Light Screen up, but the hit CRITS                   160 ×crit    the code requires
                                                                     the crit multiplier
                                                                     to be 1 -- a crit
                                                                     skips the screen
   Light Screen up, hit is PHYSICAL                     160          Reflect covers that
                                                                     route; Light Screen
                                                                     does not cover it
   Light Screen gone                                    160          nothing taken
   ────────────────────────────────────────────────────────────────────────────────────

   ┌──────────────────────────────────────────────────────────────────────────────────┐
   │  Read the first and last rows together. The attacker did not change move, did   │
   │  not train, did not switch. The SAME 160 left, and TWICE as much arrived,       │
   │  because the thing taking a cut stopped taking one.                             │
   └──────────────────────────────────────────────────────────────────────────────────┘

   And raising the attacker's Special Attack does not change the FRACTION taken.
   The barrier's cut is a property of the barrier. That is why the oral dose of a
   high-extraction drug is the one that moves in liver failure and the injected
   dose is not -- see m044 for the route half of this.
```

The three bypasses are the three routes. A **critical hit** ignores the screen outright. A
physical move was never subject to it. And **Brick Break** — 75 power, 100 accuracy — removes the
screen and *then* hits, in one action. Three different ways round a barrier, each exact, and none
of them an improvement to the move.

## Three more consequences, each pointing a different way

**The held item is the binding.** **Knock Off** is 20 base power and its real effect is that the
target's held item is gone for the rest of the battle. Take the **Leftovers** off Blissey and the
sixteenth-of-maximum trickle stops; take a type-boosting item off an attacker and its output drops
with no change to anything else. One action, several numbers moved, and `m009` is where the
irreversibility of that is worked through.

**The same hit, a different effect.** A **burn** does two things in the Game Boy Advance code: it
removes an eighth of maximum HP at the end of each turn, and — separately, in the damage routine —
it **halves the user's Attack** unless the ability is **Guts**. **Machamp** has Guts as its only
ability and **Heracross** has **Swarm** or Guts, and for either of them the halving simply does
not happen. So the identical move, from the identical Pokémon, at the identical stats, lands for
half or for full depending on a condition that is nowhere in the move data. Nothing about the
amount changed. The *sensitivity* changed, and that is the half of liver disease that is not
kinetics at all.

**And the direction reverses for a conversion step.** `m006` set this one: **Magikarp** knows
**Splash**, which does nothing, and the thing with the effect is the **Gyarados** it becomes at
level
20. Put an **Everstone** on it and you do not get a stronger Magikarp — you get no Gyarados and no
    effect whatsoever. Every other failure in this answer makes more of something arrive. A broken
    conversion makes less.

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. Here it stops.

The two groups of people this pair of answers is about are among the most reliably harmed by
prescribing. Someone with reduced kidney or liver function is taking more medicines than average,
is more likely to be old, is more likely to be in hospital, and is less able to absorb an error
when one is made. The error is rarely arithmetic. It is a correct calculation applied to an
assumption that was true of somebody else — a filtration estimate normalised to a standard body
used for a narrow-margin drug in a very small person, an oral dose reasoned from an injected one
in liver failure, a total drug concentration read as reassuring when the binding protein was low.

A Pokémon with a weaker leak is a sum. A person harmed by a dose is a person harmed by a system,
and the honest word for that is iatrogenic. Naming it that way is what makes an event reportable,
auditable and preventable for the next person, and it puts the fault where it belongs — in the
design that let the assumption through, not in whoever happened to be holding the chart. The
person it happened to did nothing wrong.

Nothing in this answer or its technical twin is a dose, an adjustment or a threshold, and nothing
in either should be used to work out an amount for anyone. Anyone with a question about their own
kidneys, liver or medicines should raise it with their own prescriber or pharmacist, who can see
results that neither half of this pair can.

## What a Gym Leader is listening for

* Why does halving the level of a **Seismic Toss** user exactly double the time to empty, when
  halving an ordinary attacker's output does not?
* One layer of **Spikes** against Blissey and against **Shedinja**. Why is that the whole argument
  about normalised estimates?
* Name the four things that leave the team when Blissey does, and what each costs to replace.
* **Light Screen** drops. The attacker changed nothing. Why did twice as much arrive?
* Three ways past a **Light Screen**. Which of them is an improvement to the attacking move?
  (None.)

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **Your national formulary's prescribing-in-renal-impairment and
  prescribing-in-hepatic-impairment guidance**, and the monograph for every drug the twin names.
  The authority for every adjustment, and it differs between countries.
* **Your laboratory's reported filtration estimate** — which equation, and whether it is
  normalised to body surface area. That is a fact about the laboratory, not about the patient.
* **The summary of product characteristics or regulator-approved prescribing information** for
  each product, for its impairment sections and for the bioavailability figure that makes the
  barrier argument above quantitative.
* **A current standard clinical pharmacology or hepatology textbook**, for the extraction-ratio
  derivation and for what the composite severity scores were built to predict.

The Pokémon figures are a different matter and were checked against the public decompilation of
the Game Boy Advance games, read directly: Seismic Toss running `dmgtolevel` and `adjustsetdamage`
and so bypassing the random damage multiplier of 85–100 per cent; that multiplier being `100 -
(Random() % 16)` on the ordinary damage path; the HP formula and Blissey's base stat line of 255 /
10 / 10 / 55 / 75 / 135; Chansey's of 250 / 5 / 5 / 50 / 35 / 105; Shedinja's hard-coded maximum
HP of 1; Blissey learning Soft-Boiled at level 10 and Light Screen at level 40, and Chansey at 13
and 49; the ability pair Natural Cure and Serene Grace on both, and Natural Cure clearing
`status1` to zero; Spikes damage of `maxHP / ((5 − layers) × 2)` with a maximum of three layers;
Light Screen halving special damage, reducing it to two-thirds in a double battle with two live
defenders, and being skipped entirely unless the critical multiplier is 1; Reflect covering the
physical route instead; Brick Break at 75 power and 100 accuracy removing a screen; Knock Off at
20 base power removing the held item; Leftovers restoring a sixteenth of maximum HP; burn removing
an eighth of maximum HP per turn and halving Attack in the damage routine unless the ability is
Guts; Machamp having Guts as its only ability and Heracross having Swarm or Guts; and Magikarp
evolving into Gyarados at level 20 with Splash having no effect. Every arithmetic result in the
blocks above is recomputed from those rules rather than recalled.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** Every figure
in the technical twin is an illustrative round number chosen to make the extraction-ratio
arithmetic legible; no renal or hepatic dosing band appears in either half, deliberately, because
those are formulary and local property and they differ between countries. Nothing here should be
used to make a decision about anyone's treatment, including your own; the formulary, the product
information, the laboratory and local guidance are the authority. Anyone with a question about a
medicine they are taking should raise it with their own prescriber or pharmacist. A Pokémon whose
leak got smaller is a sum. A person is not.

## Where this stands, October 2026

The structural argument — one gradable function against four that fail separately — is mechanism
and does not date, and the game mechanics cited are fixed in released software, though the series
has changed several of them between generations and this answer pins the ones it uses to the Game
Boy Advance games. What dates is everything downstream: which estimating equation a laboratory
reports and whether it is normalised, which drugs carry an absolute-clearance caveat, the renal
dosing bands, and the per-drug hepatic advice. Renal function reporting has been revised in
several countries in recent years, including over whether to apply a race coefficient, and the
answer differs by country. Check current laboratory practice and the current formulary rather than
any remembered band.
