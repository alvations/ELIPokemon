---
id: "m006"
slug: pharmacokinetics-four-processes
style: pokemon
category: pharmacology
difficulty: advanced
question: "What do absorption, distribution, metabolism and excretion each contribute, and why are clearance, volume of distribution and half-life the three numbers that actually predict a drug's behaviour?"
tags: [pharmacokinetics, half-life, clearance, loading-dose, adme]
---

# Super Fang always takes half, so the size of the bar and the clock on it are two numbers.

Blissey has the highest base HP in the games, 255, and at level 100 with a perfect HP stat and the
full 252 effort points in it the bar reads **714**. Shedinja's bar reads **1**, at every level,
for ever, because the games hard-code it rather than calculating it. Those two Pokémon are the
whole of volume of distribution, and the next paragraph is the whole of why half-life is a
separate idea.

**Super Fang** takes half of whatever is on the bar right now. Not a fixed amount — a fixed
*fraction*. So Super Fang empties Blissey's 714 and Shedinja's 1 in **exactly the same number of
hits**, because halving does not care how much there was. Meanwhile **Seismic Toss** at level 100
takes exactly 100 HP from anything it touches, so it empties Shedinja in one and Blissey in eight.
Two kinds of removal, two completely different relationships with the size of the bar.

That is the lesson, before any of the four processes: the size of the bar and the rule the bar
empties by are separate facts, and the clock you care about is produced by both of them together.

## The four processes, each pinned to a mechanic

| In the clinic | In the games | Why it is the same shape |
| --- | --- | --- |
| Absorption, bioavailability | A **Potion** used from the bag versus a held **Oran Berry** | The Potion's 20 HP arrives immediately and in full. The Oran Berry's 10 HP sits in the hand doing nothing until the bar is at half or below. Same chemical, different route, different arrival |
| Distribution, volume | The maximum on the bar — Blissey 714, Shedinja 1 | The same 20 HP is 2.8 % of Blissey and twenty times Shedinja's entire bar |
| Metabolism | **Magikarp** at level 20, and **Eevee** with a **Thunder Stone** | The thing administered is not always the thing that acts |
| Excretion | **Super Fang** and **Seismic Toss** | Both take HP off the bar for good; they differ only in the rule |
| Metabolism + excretion = clearance | Both of the above feeding one emptying rate | Different mechanics, one number |

**Absorption.** A **Hyper Potion** used from the bag is the complete, immediate route. A held
**Oran Berry** restores 10 HP, and only when HP has fallen to half the maximum or lower — it is
sitting there the whole time, unavailable, waiting for a condition. A **Sitrus Berry** is the same
shape with a bigger number, and the games changed that number in a way worth noticing: in Ruby,
Sapphire and Emerald it restores a flat 30 HP, and from Diamond and Pearl onwards it restores a
quarter of maximum HP instead. The series switched a fixed amount for an amount scaled to the
holder, which is exactly the difference between a flat dose and a weight-based one.

**Distribution.** Blissey's bar is checkable arithmetic rather than lore:

```
   maximum HP  =  ( 2 × baseHP  +  HP IV  +  HP EV / 4 ) × level / 100  +  level + 10

   Blissey, level 100, perfect HP IV, 252 HP EV:
        ( 2 × 255 + 31 + 252/4 ) × 100/100 + 100 + 10
      = ( 510   + 31 + 63     ) +  110
      =   604                   +  110        =  714

   Shedinja, any level:  the games skip the formula entirely and write 1.
```

**Metabolism.** **Magikarp** knows **Splash**, and Splash does nothing whatsoever. What you put in
is inert; at level 20 it becomes **Gyarados**, and *that* is the thing with the effect. Block the
conversion with an **Everstone** and you do not get a stronger Magikarp — you get no Gyarados and
no effect at all. **Eevee** with a **Thunder Stone** is the other case: **Jolteon** is a real
product with its own properties, and it is no longer the thing you handed over.

**Excretion.** **Super Fang** removes a fraction. **Seismic Toss** and **Night Shade** remove the
user's level in HP, flat, whatever the target. The first has a stable halving time. The second
does not have one at all.

## The arithmetic that makes the clock useful

```
   Blissey's bar: 714.  Super Fang, repeatedly (the games round down each time):

   hits        HP left              fraction of the bar       distance to EMPTY halves too
   ─────────────────────────────────────────────────────────────────────────────────────────
     0           714                   100.0  %                       —
     1           357                    50.0  %                    half way
     2           178                    25.0  %                    three quarters
     3            89                    12.5  %                    seven eighths
     4            44                     6.2  %                    fifteen sixteenths
     5            22                     3.1  %   ◄── the "five"   thirty-one thirty-seconds
     7             5                     0.7  %                    one hundred twenty-seventh
   ─────────────────────────────────────────────────────────────────────────────────────────

   Shedinja's bar is 1, and Super Fang clears it in the same arithmetic, not fewer hits.
   Halving does not know the size of the bar. That is the entire point.

   ONE table, read two ways. Filling a bar back up by closing half the remaining gap each
   turn gives 50, 75, 87.5, 93.75, 96.9 % — the same column, read as progress instead of
   as loss, because one rate constant governs both directions.
```

Five is not a sacred number. It is where the right-hand column passes about 97 %, and three hits
(87.5 %) is often near enough to act on while seven (0.7 % left) is as near as anyone needs. Which
you want depends entirely on how badly 10 % short would hurt — a different question, taken up in
**m008**.

## Why you reach for a Max Potion, and when you do not

```
   FILLING the bar from empty          =  the size of the bar
        Blissey                        =  714 HP of healing
        Shedinja                       =  1 HP of healing
        a Max Potion                   =  fills whatever the bar is, in one go
        a Potion                       =  20 HP, whatever the bar is

   HOLDING the bar once filled         =  the size of the leak
        Seismic Toss, level 100        =  100 HP out per turn
        Leftovers on Blissey           =  714 / 16  =  44 HP in per turn
        net                            =  56 HP out per turn
        Blissey from full to empty     =  714 / 56  ≈  13 turns

   ┌──────────────────────────────────────────────────────────────────────────────┐
   │  no Max Potion : Leftovers alone fills 714 at 44 a turn  →  17 turns         │
   │  Max Potion    : full on the turn you use it, then hold the 44-a-turn line   │
   └──────────────────────────────────────────────────────────────────────────────┘

   The two sums use DIFFERENT facts. Halve the leak and the amount needed to FILL the bar
   does not change at all; only the amount needed to HOLD it does. Swapping those round is
   the classic error.
```

You reach for the **Max Potion** because filling by Leftovers happens on a timetable set by the
bar and the trickle, and sometimes seventeen turns is longer than the battle. You do not reach for
it when the bar is small enough to fill by trickle anyway, when overshooting is itself the danger,
when you do not actually know how big the bar is, or when the effect you want is not on the bar —
a Pokémon locked into **Struggle** because every move is out of PP does not need HP, it needs an
**Elixir**, and the bar is the wrong number to be watching.

## What moves the numbers

* **A weaker remover.** Drop the level of the Pokémon using **Seismic Toss** and the flat 100
  becomes a flat 50; the bar lasts twice as long and the amount needed to hold it halves. The
  amount needed to fill it is untouched.
* **A different bar.** **Effort Values** and a **Rare Candy** climb change the maximum without
  touching the leak. Same leak, different bar, different clock.
* **Which rule is in force.** **Super Fang** has a constant halving time. **Seismic Toss** has
  none, because a flat amount against a shrinking bar is a straight line, not a curve. When the
  remover is working flat out at a fixed ceiling, halving times stop being a meaningful thing to
  quote — and that is the shape of the saturable case in this answer's technical twin.
* **The mapping's one leak, named honestly.** Almost every drain in the games — **Leech Seed** at
  an eighth, **Leftovers** at a sixteenth, a burn at an eighth — is written as a fraction of the
  bar, so in the games the leak is tied to the bar in a way it is not in a person. **Seismic
  Toss** and **Night Shade** are used above precisely because they are not.

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. Here it stops.

Pharmacokinetics is where a great deal of avoidable harm in medicine actually happens. The people
in whom elimination is slower or body composition is unusual — those with reduced kidney or liver
function, the very old, the very young, the very underweight, the critically ill — are the same
people least able to absorb a dosing error, and the error is usually a correct calculation applied
to a wrong assumption rather than a slip in the multiplication. Loading doses are a recognised
source of serious harm for exactly that reason: they are large by design and they are computed
from a volume nobody measured.

A bar emptying on a screen refills when you walk into the nearest building. A dosing error is
something done to a person by a system, and the honest name for it is iatrogenic harm. Nothing in
this answer or its technical twin should be used to work out an amount for anyone. Anyone with a
question about a medicine they are taking should raise it with their own prescriber or pharmacist.

## What a Gym Leader is listening for

* Why does a huge bar make skimming off the top useless?
* The leak halves. How much healing does it now take to fill the bar? (The same.)
* Why is a halving time the wrong number to quote for **Seismic Toss**?
* Given two readings of the bar, how would you tell a flat leak from a missed **Leftovers** turn?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* Your national formulary's monograph for any drug the technical twin of this answer names — in
  the United Kingdom the British National Formulary, published by NICE with the pharmaceutical
  press; elsewhere the equivalent national formulary. Authority for every dose, interval and
  target concentration.
* The summary of product characteristics (European Union and United Kingdom) or the regulator-
  approved prescribing information (for example the label approved by the United States Food and
  Drug Administration) for the specific formulation. Authority for bioavailability, half-life and
  whether loading is part of the licensed approach.
* Your national formulary's guidance on prescribing in renal impairment and in hepatic impairment.
* A standard clinical pharmacology textbook for the first-order equations this answer dramatises.
* Your local therapeutic drug monitoring service or laboratory handbook, for reference ranges and
  sampling times, which differ between laboratories and between countries.

The Pokémon figures are a different matter and were checked: the HP formula, Blissey's base 255,
Shedinja's hard-coded 1, Super Fang halving current HP, Seismic Toss and Night Shade dealing the
user's level in damage, Leftovers at a sixteenth of maximum, and the Oran and Sitrus Berries at a
flat 10 and 30 HP on half or less all come from the public decompilation of the Game Boy Advance
games, read directly. One Pokémon claim here does not: that the Sitrus Berry became a quarter of
maximum HP from Diamond and Pearl onwards is from general knowledge of the later games, whose code
was not read, and it is the one figure above to check before repeating.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in it are the Pokémon ones.** Every clinical
figure in its technical twin is either an illustrative round figure or a general principle, and
none is a dose, a target or a threshold for any person. Practice differs between countries and
between formularies. Nothing here should be used to make a decision about anyone's treatment,
including your own; the formulary, the product information and local guidance are the authority.
Anyone with a question about a medicine they are taking should raise it with their own prescriber
or pharmacist. A bar emptying on screen is a mechanism made visible. It is not a person.

## Where this stands, October 2026

The arithmetic above is definition and algebra, and it does not date. The game mechanics cited are
fixed in released software and do not date either, though the series has changed some of them
between generations and this answer says which. What dates is everything attached to a particular
drug — targets, renal dosing, whether loading is recommended at all — and that moves at different
times in different countries. Check the current formulary.
