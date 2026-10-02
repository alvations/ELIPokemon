---
id: "m008"
slug: therapeutic-index
style: pokemon
category: pharmacology
difficulty: intermediate
question: "What is the therapeutic index, and what does a narrow one change about how a drug is monitored, substituted and assessed for interactions?"
tags: [therapeutic-index, monitoring, bioequivalence, toxicity, variability]
---

# Take Down pays four to one, Double-Edge three. The printed ratio is not the margin.

A recoil move tells you its index on the tin. **Take Down** does 90 base power and the user takes
a quarter of the damage it dealt: four out to one back. **Double-Edge** does 120 and the user
takes a third: three out to one back. Hit harder, pay proportionally more. The ratio is a property
of the move, it is the same for every Pokémon that uses it, and you can read it off the move data
without battling anything.

Two warnings belong here rather than at the end, because they are what separates understanding the
ratio from reciting it.

**The printed ratio is not the margin.** Three to one says nothing about whether you survive. That
depends on the bar it is attached to, and on what else has already been taken off it. The same
Double-Edge, the same three to one, is comfortable from a full bar and lethal from a worn one. A
ratio describes the move; a margin describes the pairing.

**You cannot find your floor without crossing it.** Nothing in a battle tells you how much recoil
you can afford except arithmetic you do yourself beforehand. **Belly Drum** is the one honest
exception in the games: it states its gate outright and simply refuses when you are below it.

## The arithmetic

```
   THE PRINTED INDEX -- straight off the move data, no inference

   move             power    what the user takes            out : back
   ─────────────────────────────────────────────────────────────────────────────
   Take Down          90     a quarter of damage dealt         4 : 1    wide
   Submission         80     a quarter of damage dealt         4 : 1    wide
   Double-Edge       120     a third of damage dealt           3 : 1    narrower
   Struggle           50     a quarter of damage dealt         4 : 1    and you did
                                                                       not choose it
   Self-Destruct     200     the user faints. Always.          — : —   no ratio
   Explosion         250     the user faints. Always.          — : —   no ratio
   ─────────────────────────────────────────────────────────────────────────────

   The last two rows are not a narrow ratio. They are a different kind of thing:
   the harm is not a risk, it is the mechanism. Nothing about watching the bar
   helps, and the only decision left is whether the trade is worth making at all.
```

```
   SAME MOVE, SAME RATIO, DIFFERENT MARGIN
   A Pokémon with 300 maximum HP uses Double-Edge for 150 damage: recoil of 50.

                                       HP before   recoil   HP after   standing?
   ──────────────────────────────────────────────────────────────────────────────
   full bar                               300         50       250      yes, easily
   worn down                               60         50        10      yes, barely
   worn down, then switched in over
   one layer of Spikes (300/8 = 37)        23         50         0      NO
   ──────────────────────────────────────────────────────────────────────────────

   THE SAME 50. The move did not change, the ratio did not change. What changed is
   how much room there was. This is why 37 points of entry damage are beneath
   notice in one matchup and decide the battle in another, with no difference in
   mechanism at all.
```

```
   LIFE ORB -- a flat tenth of your own maximum HP every time an attack connects,
   in exchange for 1.3× damage on everything.

   300 maximum HP, so 30 a use:

   use           1     2     3     4     5     6     7     8     9    10
   HP left     270   240   210   180   150   120    90    60    30     0  ◄ faints
   damage      +30 % the whole way, and the cost arrives whenever the attack lands,
               whether landing it helped or not
```

```
   BELLY DRUM -- the only move here with its window written into it. It sets Attack
   to +6 (×4.00) and costs HALF OF MAXIMUM HP, and the games refuse it outright
   unless current HP is strictly ABOVE half the maximum.

   Snorlax, which learns Belly Drum at level 15, has base HP 160, so at level 100
   with a perfect HP stat and the full 252 effort points its bar reads

        ( 2 × 160 + 31 + 252/4 ) + 110  =  414 + 110  =  524

   so the cost is 262 and the gate is 262:

   HP before      524     400     263     262     200
   allowed?       yes     yes     yes      no      no
   HP after       262     138       1       —       —
                                    ▲
                                    one point of margin, by arithmetic, not by luck
```

## What a narrow ratio actually changes

**You stop watching the effect and start watching the bar — and you cannot always.** Your own
Pokémon shows its HP as a number. The opponent's shows a bar and nothing else. So for your side
you have a measurement and for theirs you have an impression, and every decision about whether one
more Double-Edge is affordable is made on whichever of the two you happen to have. That asymmetry
is exactly why you measure the thing you can measure rather than the thing you care about, and it
is also why a reading with no context is worthless: HP after Spikes and HP before Spikes are two
different numbers and only one of them is the one your plan was built on.

**The same move in a different Pokémon is not the same move.** **Aggron** learns **Take Down** at
level 25 and **Double-Edge** at level 63, and if its ability is **Rock Head** the recoil from both
is simply skipped — the ratio is no longer four to one or three to one, it is unbounded.
**Rhydon** and **Aerodactyl** also learn Take Down and also carry Rock Head. Nothing about the
move changed; the body it is in changed, and the index went with it. This is the whole of why you
cannot carry a margin from one holder to another and assume it travels.

And an Aggron's ability is **Sturdy** *or* Rock Head, never both, and they protect against
completely different things: in the Game Boy Advance games Sturdy blocks the one-hit knockout
moves — **Fissure**, **Horn Drill**, **Guillotine**, **Sheer Cold** — and nothing else, while Rock
Head blocks recoil and nothing else. Two safeguards, one slot, neither generalising. Reading
*protected* off a sheet without reading *against what* is how a margin gets assumed that was never
there.

And the games put the other exception exactly where it hurts: the recoil script looks for
**Struggle** *before* it looks for Rock Head, so **Rock Head does not protect you from Struggle**.
The one you were forced into is the one nothing shields you from.

**Chip damage is re-weighed.** One layer of **Spikes** removes an eighth of maximum HP on entry.
Against a wide ratio that is a rounding error. Against **Double-Edge** on a worn bar it is the
whole question, as the second block above shows. The amount did not change; the room did.

**And where the cost does not scale with the benefit, it gets worse.** **Take Down** and
**Double-Edge** at least charge in proportion to what they achieved. **Life Orb** charges a flat
tenth whether the hit mattered or not, so ten connecting attacks is the whole bar regardless of
whether any of them were worth making. A cost that does not track the benefit and a thin margin
are much worse together than either is alone.

**Finally, the housekeeping.** A thin margin is why a **Focus Sash** exists at all: from full HP
it leaves you on exactly 1, which is a margin of one point, bought deliberately, and spent once.
It is why the bar gets read before every turn rather than every few. None of that is about the
move. It is all downstream of one ratio being small.

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. The consequence is not a
mechanism, and here the Pokémon framing stops.

A drug with a narrow margin can cause serious harm at a concentration only a little above the one
that helps, and an overdose — whether deliberate or accidental — is a medical emergency. If anyone
may have taken too much of any medicine, the right action is to contact emergency services or the
national poisons service immediately. There is no reset button, no **Pokémon Center**, and nothing
in this answer or its technical twin can be used to judge whether an amount someone has taken is
safe. That judgement needs a person with the records in front of them.

And where a narrow-index drug does harm inside the therapeutic range — a substitution nobody
flagged, a monitoring result nobody chased, a concentration drawn at the wrong time and read as
though it were a trough — that harm was caused by the care rather than by the illness. It is
iatrogenic, and the person it happened to did nothing wrong. Naming it that way is not a
formality: it is what makes it reportable, auditable and preventable for the next person.

## What a Gym Leader is listening for

* Why does the printed ratio tell you less than the bar does?
* The bar reads comfortable and the next recoil faints you. Give three reasons.
* Why can you not carry a margin from **Aggron** across to a Pokémon without **Rock Head**?
* Why is a flat cost per use worse than a proportional one when the margin is thin?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* Your national formulary's monograph for each drug the technical twin of this answer names, and
  its guidance on therapeutic drug monitoring — in the United Kingdom the British National
  Formulary, published by NICE with the pharmaceutical press; elsewhere the equivalent national
  formulary. Authority for every range, interval and sampling time.
* Your national medicines regulator's guidance on bioequivalence, and on generic substitution for
  narrow therapeutic index drugs. Authority for acceptance limits, which this answer's twin
  deliberately does not state, and for which drugs they apply to.
* The medicines regulator's advice on antiepileptic product continuity for your own country — in
  the United Kingdom the Medicines and Healthcare products Regulatory Agency. Country-specific.
* The summary of product characteristics, or the regulator-approved prescribing information, for
  the specific product, for its monitoring requirements.
* Your local laboratory handbook or therapeutic drug monitoring service, for assay-specific
  reference ranges, which differ between laboratories as well as between countries.
* Your national poisons information service for the management of any overdose.

The Pokémon figures are a different matter and were checked: the base powers and recoil fractions
of Take Down, Submission, Double-Edge, Struggle, Self-Destruct and Explosion; Life Orb's 1.3×
multiplier; Belly Drum setting Attack to the maximum stage, costing half of maximum HP and failing
at or below that; the HP formula and Snorlax's base HP of 160; the levels at which Aggron, Rhydon
and Aerodactyl learn Take Down and Aggron learns Double-Edge; Snorlax learning Belly Drum at level
15; one layer of Spikes costing an eighth of maximum HP; Sturdy blocking only the one-hit knockout
moves; the recoil script checking for Struggle before it checks for Rock Head; and the ability
pairs of Aggron, Rhydon and Aerodactyl all come from the public decompilation of the Game Boy
Advance games, read directly. One Pokémon figure here does not: Life Orb's cost of a tenth of the
holder's maximum HP per connecting attack is from general knowledge rather than from code that was
read, and it is the one number above to check before repeating.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in it are the Pokémon ones.** The therapeutic
windows in its technical twin are illustrative figures invented to make arithmetic legible, and no
number in either half is any real drug's range. Practice differs between countries, regulators and
laboratories. Nothing here should be used to make a decision about anyone's treatment, including
your own; the formulary, the product information, the laboratory and local guidance are the
authority. Anyone with a question about a medicine they are taking should raise it with their own
prescriber or pharmacist. In a suspected overdose, contact emergency services.

## Where this stands, October 2026

The ratio and the arithmetic do not date, and the game mechanics cited are fixed in released
software. Everything attached to a particular drug does date: which drugs are formally designated
narrow therapeutic index, what substitution rules apply, which monitoring is expected and how
often. Those are regulatory decisions, they differ between countries, and they change. Check the
current formulary and your own regulator.
