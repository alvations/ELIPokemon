---
id: "m041"
slug: therapeutic-drug-monitoring
style: pokemon
category: pharmacology
difficulty: advanced
question: "Which drugs are monitored by plasma concentration rather than by effect, what has to be true before a concentration can be interpreted, and what does a trough actually tell you?"
tags: [therapeutic-drug-monitoring, trough, steady-state, protein-binding, assay]
---

# You can read the damage. You cannot read the Speed — so you work the Speed out before the turn.

Nobody computes **Attack**. You use the move and the damage is printed on the screen, and the
printed damage is the effect you actually wanted. Nobody computes **Speed** either, and that is a
mistake, because Speed is the one stat whose effect you can never read: the only readout the games
give you is a single bit per turn — who moved first — and that bit is corrupted by five separate
things before it reaches you.

That gap is the whole of therapeutic drug monitoring. You measure the effect where the effect is
legible. You fall back on measuring the **number** only where the effect is one bit of confounded
information per turn.

## Why the damage is legible and the turn order is not

The damage is nearly legible, and the "nearly" matters. The standard damage path in the Game Boy
Advance games multiplies the result by a random factor of **85 % to 100 % inclusive** — the code
takes `100 - (Random() % 16)`, so sixteen values, every one equally likely. One observed damage
number therefore brackets the Attack rather than pinning it.

Two moves escape that entirely. **Seismic Toss** runs `dmgtolevel` and then `adjustsetdamage`, so
it never touches the random multiplier at all: at level 100 it removes exactly 100, every time.
**Super Fang** takes exactly half of current HP and likewise skips it. Those are the measurements
with no spread on them, and they are the ones you can invert from a single observation.

Turn order is a different animal. Here is what sits between the Speed stat and the bit you
observe, all of it read off the turn-order routine:

```
   WHAT YOU OBSERVE:  one bit.  "they moved first."
   WHAT IS BETWEEN THAT BIT AND THE SPEED STAT:

   1  priority is compared BEFORE speed is looked at at all
         Quick Attack  +1        Protect  +3
         so a slower Pokémon moving first tells you nothing about either Speed

   2  a Macho Brace on the holder     →  Speed / 2

   3  paralysis on the holder         →  Speed / 4
         and paralysis arrives from Thunder Wave, from Glare, from Stun Spore, from
         Body Slam's secondary, or from Zap Cannon -- five sources, one effect, and
         a Cheri Berry or a Lum Berry takes it straight back off again

   4  a Quick Claw that triggers      →  effective Speed set to the MAXIMUM, at random

   5  stat stages, applied as a ratio before any of the above -- an Agility is +2

   6  and on an exact tie             →  Random() & 1.   A coin.

   ┌──────────────────────────────────────────────────────────────────────────────────┐
   │  Six interveners between the quantity and the observable. This is exactly why    │
   │  a seizure not happening is not a measurement of an antiepileptic, and why a     │
   │  blood pressure IS a measurement of an antihypertensive. One of those effects    │
   │  is a printed number and the other is a coin flip with five modifiers on it.     │
   └──────────────────────────────────────────────────────────────────────────────────┘
```

## The laboratory, hiding in the badge case

The sharpest fact in this answer is one most players never notice. In the turn-order routine there
is a badge check: if the player holds the **third Gym badge** — the **Dynamo Badge**, which
**Wattson** hands over in **Mauville City** — the *player's* Speed is multiplied by 110 and
divided by 100. Ten per cent, free. The damage routine carries three siblings of it: the first
badge boosts Attack, the fifth boosts Defence, the seventh boosts both Special stats.

And then the conditions, which are the point:

* it applies **only to the player's side**, never the opponent's;
* it is **switched off entirely** in link battles, recorded link battles, E-Reader battles and
  every **Battle Frontier** facility;
* and it does not apply against a Secret Base trainer.

So the same Pokémon, unchanged, reads one Speed on **Route 118** and a different Speed in the
**Battle Tower**. Nothing about the Pokémon moved. The measuring apparatus moved.

That is a reference range. A number from one laboratory read against a range from another is not a
slightly worse number; it is a different quantity wearing the same units, and the badge boost is
the cleanest demonstration of it anywhere in the games.

## One reading, three answers: the inference problem

The summary screen gives you one number per stat. The formula behind it, for every stat except HP,
is:

```
   stat  =  ( ( 2 × base  +  IV  +  EV / 4 ) × level ) / 100  +  5
   then   × 110/100  for a raising nature,  × 90/100  for a lowering one
   (nature never touches HP, accuracy or evasion -- the code returns early for those)

   SMEARGLE, base Speed 75, level 100.  So:  stat = 155 + IV + EV/4, before nature.

   reading   consistent with                                    IV      EVs    nature
   ─────────────────────────────────────────────────────────────────────────────────────
     186     a perfect Speed IV and no training                  31       0     neutral
     186     a middling IV with 64 points of training            15      64     neutral
     186     a poor IV with 96 points of training                 7      96     neutral
     186     a decent IV, 128 points, and a nature DRAGGING
             it down   (207 × 90/100 = 186)                      20     128     lowering
   ─────────────────────────────────────────────────────────────────────────────────────

   FOUR different Pokémon. ONE reading. The number is not wrong and the arithmetic is
   not hard -- the equation simply has more unknowns than observations, and no amount
   of staring at 186 fixes that.

   Pin the nature and pin the EVs and the IV falls out. Pin nothing and you have a
   number and a shrug.

   And the nature is itself derived, not stored: the code reads it out of the
   Personality Value, fixed when the Pokémon was generated and never printed. The
   one in-game tell is which Pokéblock flavour it likes, because the flavour-gain
   table is indexed by nature.
```

Smeargle is a deliberate choice here: its base stats are 55 / 20 / 35 / 75 / 20 / 45, unremarkable
in every slot, so nothing about the species distracts from the arithmetic.

And there is a case where the reading moves while the thing it measures does not. In the later
generations, **Hyper Training** with a **Bottle Cap** or a **Gold Bottle Cap** makes a stat
*calculate* as though the IV were perfect while leaving the stored IV exactly as it was — so the
summary screen and the underlying value now disagree, permanently, and only one of them is the
number that breeds true. That is the total-versus-free problem in one mechanic: the quantity the
instrument reports and the quantity that acts are two different quantities, and nothing on the
screen flags the divergence. (Hyper Training is from general knowledge of the later games; it does
not exist in the Game Boy Advance code read for the rest of this answer, and it is the one Pokémon
claim here to check before repeating.)

## Which readings are worth taking at all

You do not sit down and work out **Shuckle**'s Speed. Its base Speed is **5** — against base
Defence and base Special Defence of **230** each — and no plausible combination of training,
nature and level puts it near anything you care about outrunning. Nor **Snorlax**'s, at base 30,
nor **Rhydon**'s, at base 40. The answer is "slow", the margin is enormous, and a precise number
buys you nothing. The same goes the other way for **Ninjask** at base 160 and **Deoxys** at 150:
the answer is "first", and arithmetic adds no information to it.

Where you do the arithmetic is where the base stats are **equal**, and the games hand you those
collisions:

```
   EXACT TIES IN THE GEN III BASE-SPEED TABLE -- the thin margins

   base 130   Jolteon        Aerodactyl        Crobat
   base 120   Alakazam       Dugtrio           Sceptile
   base 110   Gengar         Latios            Latias
   base 100   Salamence      Slaking

   Three species on the same rung. Nothing about the species decides the turn.
   What decides it is the IV, the EVs and the nature -- and NONE of those three
   is printed anywhere.

   And the rungs are not safe either. Level 100, the stat formula from above:

                       base   IV   EVs   nature     Speed
   ───────────────────────────────────────────────────────────
   untrained Jolteon    130     0     0   neutral      265
   trained Dugtrio      120    31   252   neutral      339   ◄── and 120 < 130
   ───────────────────────────────────────────────────────────

   A ten-point base deficit overturned, comfortably, by the invisible numbers.
   This is exactly why a dose is not an exposure: the thing you prescribed and
   the thing that arrived are separated by quantities nobody showed you.
```

So the selection rule is the one the clinic uses. You measure the number where the decision is
close and the effect is illegible, and nowhere else. A measurement taken because the assay exists
rather than because a decision turns on it is not caution; it is noise with a laboratory bill
attached.

## Reading at a defined instant

The turn-order routine reads Speed at one fixed moment: after the stat stages have been applied as
a ratio, after the held item has been looked up, after paralysis has divided by four, at the
instant of comparison. A Speed you computed before the **Macho Brace** came off is not the Speed
in force. A Speed you computed before the paralysis landed is not either.

Nothing in the game stops you doing the arithmetic at the wrong moment and then trusting it. The
protocol — read it *here*, at *this* point in the turn, every time — is the only thing that makes
two readings comparable with each other. That is a trough: not a better number, a **reproducible**
one.

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. The reason the mechanism
is worth getting right is not, and here the Pokémon framing stops.

The drugs that get concentration monitoring are on that list because they injure people.
Aminoglycoside damage to hearing and balance is often permanent. Lithium toxicity can leave
lasting neurological injury. Immunosuppressant under-exposure loses transplanted organs;
over-exposure causes infection and cancer. Those are not trade-offs on a page. They happen to
individual people, and they happen disproportionately because a sample was taken at the wrong
time, or a result came back and nobody chased it, or a range from one laboratory was read against
a number from another.

A stat you mis-compute costs you a turn and the turn comes round again. When monitoring fails, the
harm was caused by the care rather than by the illness, and the honest word for that is
iatrogenic. Naming it that way is what makes it reportable, auditable and preventable for the next
person; the person it happened to did nothing wrong; and a system that works only when nobody is
busy is a badly designed system, not a collection of careless individuals.

Nothing in this answer or its technical twin can be used to judge whether a particular blood
result is safe, and there is no reference range in either half. Anyone with a question about a
test or a medicine of their own should raise it with the clinician or pharmacist holding their
records.

## What a Gym Leader is listening for

* Why is one damage number not enough to pin an Attack stat, and which two moves are the
  exception?
* The opponent moved first. List the things that bit of information is consistent with.
* Why is a Speed computed on **Route 118** not comparable with one computed in the **Battle
  Tower**?
* A reading of 186 on a level-100 **Smeargle**. Give three different Pokémon that produce it.
* Why does nobody compute **Shuckle**'s Speed, and what is the general rule hiding in that?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../for-agents/SOURCES-pharmacology.md`](../../for-agents/SOURCES-pharmacology.md). Specific
to this answer, and to its technical twin:

* **Your local laboratory handbook or therapeutic drug monitoring service**, the authority for
  every reference range, sampling time and unit in this topic.
* **The summary of product characteristics or regulator-approved prescribing information** for
  each monitored drug, for how long after a dose a sample may be taken.
* **Your national formulary's monographs** for the drugs the twin of this answer names.
* **Your institution's policy for acting on a result out of hours.**

The Pokémon figures are a different matter and were checked against the public decompilation of
the Game Boy Advance games, read directly: the random damage multiplier of 85–100 % inclusive
computed as `100 - (Random() % 16)`; Seismic Toss using `dmgtolevel` and `adjustsetdamage` and so
bypassing that multiplier; Super Fang taking half of current HP by the same route; the turn-order
routine's order of operations, including priority being compared first, the Macho Brace halving
Speed, paralysis dividing it by four, the Quick Claw setting it to the maximum, and the coin flip
on an exact tie; Quick Attack at priority +1 and Protect at +3; the badge Speed boost of 110/100
gated on the third badge flag, the player's side, and exclusion of link, recorded-link, E-Reader
and Frontier battles; the Mauville City Gym script setting that same third badge flag and naming
it the Dynamo Badge; the non-HP stat formula and the nature multipliers of 110/100 and 90/100 with
HP, accuracy and evasion exempted; the nature being derived from the Personality Value and
indexing the Pokéblock flavour-gain table; Thunder Wave, Glare and Stun Spore all carrying the
paralysis effect, Body Slam carrying it as a thirty-per-cent secondary and Zap Cannon as a
paralysing hit; the Cheri Berry and Lum Berry hold effects; Agility raising Speed by two stages;
and the base stats of Smeargle, Shuckle, Snorlax, Rhydon, Ninjask, Deoxys, Jolteon, Aerodactyl,
Crobat, Alakazam, Dugtrio, Sceptile, Gengar, Latios, Latias, Salamence and Slaking. Every
arithmetic result in the tables above is recomputed from that formula rather than recalled.

**One Pokémon claim here is not from code** and is flagged where it appears: Hyper Training and
the Bottle Caps belong to the later generations, whose source was not read, and that is the single
figure above to check before repeating.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only numbers in either half of this pair are the Pokémon ones.** No
reference range, sampling interval or target concentration appears anywhere in this pair,
deliberately: those are laboratory and formulary property, they differ between institutions and
between countries, and a figure remembered from revision material is exactly the wrong thing to
carry to a bedside. Nothing here should be used to make a decision about anyone's treatment,
including your own; the laboratory, the formulary, the product information and local guidance are
the authority. Anyone with a question about a medicine or a blood test of their own should raise
it with their own prescriber or pharmacist. A stat you can recompute is not a person you have
measured.

## Where this stands, October 2026

The inference structure above is algebra and does not date, and the game mechanics cited are fixed
in released software. What dates is everything attached to a particular drug or laboratory: which
drugs are monitored, by trough or by area under the curve, at what time after a dose, against what
range, in what units. Area-under-the-curve-guided dosing has been displacing trough-only
approaches for some agents, at different times in different countries, and an assay platform
change moves a range without anything clinical having changed. Check the current laboratory
handbook and the current formulary.
