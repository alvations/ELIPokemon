---
id: "m044"
slug: formulation-and-route
style: pokemon
category: pharmacology
difficulty: intermediate
question: "Why does the same drug behave differently by route, and what does a modified-release preparation actually modify?"
tags: [route-of-administration, bioavailability, modified-release, first-pass, dose-dumping]
---

# Accuracy is the fraction that arrives. Fire Spin is a modified-release tablet.

Every move in the games prints two numbers, and they are the only two numbers this answer needs.
**Base power** is the dose. **Accuracy** is the fraction that arrives. Multiply them and you have
what the move actually delivers, which is almost never the number on the tin.

```
   STRAIGHT OFF THE GEN III MOVE DATA -- no inference anywhere in this table

   move              power    accuracy      power × accuracy
   ───────────────────────────────────────────────────────────────────────────
   Flamethrower        95        100              95.0
   Fire Blast         120         85             102.0
   Megahorn           120         85             102.0
   Hydro Pump         120         80              96.0
   Cross Chop         100         80              80.0
   Thunder            120         70              84.0
   Blizzard           120         70              84.0
   Zap Cannon         100         50              50.0
   Fissure              —         30               —    (a different kind of thing)
   ───────────────────────────────────────────────────────────────────────────

   Read the first two rows together. Fire Blast's printed power beats
   Flamethrower's by 25 and its delivered power beats it by 7. The dose went up
   by about a quarter and the exposure went up by about seven per cent, and the
   whole of the difference is a barrier taking a cut of every use.
```

**The honest limit of that mapping, before it does any work.** A bioavailability of 0.5 delivers
half of every dose. **Zap Cannon** at 50 delivers *all* of half the doses. The means agree and the
variances do not, and a move that works once in two is a worse thing to build a plan on than a
move that always works at half strength. Naming that is better than pretending the analogy is
exact, and `m043` is where the arithmetic of a plan with several uncertain steps lives.

## The intravenous route: F = 1 by definition, not by improvement

**Lock-On** and **Mind Reader** do not make the next move better. They set `STATUS3_ALWAYS_HITS`
for two turns and record *which* Pokémon is owed the guarantee, and the accuracy routine then
honours it and skips the roll entirely.

So **Zap Cannon** behind a **Lock-On** is a 50-accuracy move that lands. The move data did not
change — the printed 50 is still printed 50 — and nothing about the move was upgraded. The
**route** changed, and the route is the thing the guarantee is attached to. That is precisely why
intravenous bioavailability is 1 *by definition* rather than by measurement: it is not a drug that
absorbs well, it is a drug that skipped absorption.

## First pass: Light Screen, and the three ways round it

`m042` used **Light Screen** for the barrier, and the same mechanic does the route half of the job
because the damage routine spells out exactly what the barrier does and does not cover.

```
   A special hit computes to 160 before the screen is consulted.

   route                                   arrives     the rule in the code
   ───────────────────────────────────────────────────────────────────────────────────
   through the screen, single battle          80       damage / 2
   through the screen, double battle,        106       2 × (damage / 3)
      two defenders alive
   as a CRITICAL HIT                     160 × crit    the screen applies only when
                                                        the crit multiplier is 1
   as a PHYSICAL move                        160       Reflect is the screen for that
                                                        route; Light Screen is not
   after Brick Break (75 power, 100 acc)     160       the screen is removed, then the
                                                        hit lands, in one action
   ───────────────────────────────────────────────────────────────────────────────────

   FOUR routes to the same target and three of them are not subject to the barrier.
   Nothing in that column is a better move. Raising Special Attack does not change
   the FRACTION the screen takes, because the fraction belongs to the screen.
```

That is the whole of why a sublingual tablet of a heavily extracted drug is not a stronger tablet.
It is the same drug arriving by a route the barrier does not sit on.

## Modified release: the partial-trapping moves

This is the mapping the games already contain, and the numbers are exact.

```
   THE TRAPPING FAMILY, from the move data, all EFFECT_TRAP

   move           power   accuracy
   ─────────────────────────────────
   Clamp            35       75
   Wrap             15       85
   Bind             15       75
   Fire Spin        15       70
   Sand Tomb        15       70
   Whirlpool        15       70
   ─────────────────────────────────

   AND THEN THE DELIVERY, which has nothing to do with those numbers:

     on landing:  a counter is set to  (Random() & 3) + 3   →  3 to 6
     each end of turn:  counter decrements; while it is still non-zero the
                        trapped Pokémon loses  maxHP / 16  (minimum 1)
     so:  TWO to FIVE ticks of a SIXTEENTH, from one application

   Blissey, whose bar at level 100 with the full investment is 714 (see m006):

   ticks        1      2      3      4      5
   delivered   44     88    132    176    220
                                            ▲
   ONE administration. A fixed fraction of the HOLDER per turn -- not a fixed
   amount, so it scales to the body it is in. A duration the attacker does not
   choose. And no way whatsoever to make it arrive faster.
```

That last clause is the honest boundary of the analogy, and it is worth stating rather than
hiding: a crushed modified-release tablet dumps its whole content at once, and **the games have no
mechanic for that**. Nothing shortens a trap into a single hit. You can only end it — **Rapid
Spin** clears it, and instructively clears exactly *one* thing per use, trapping first, then
**Leech Seed**, then **Spikes**, in that fixed order. Where the mapping runs out, say so.

## Delayed release: the dose is fixed when it is given

**Future Sight** (80 power, 90 accuracy) and **Doom Desire** (120, 85) are the delayed ones, and
the code does something sharper than simply waiting. It sets a counter to 3 **and computes the
damage immediately**, at the moment the move is used, then stores it and applies the stored number
when the counter runs out.

So whatever happens in the intervening turns — a boost, a screen going up, the target switching
for something bulkier — the amount that lands was decided when the move was used. The dose is
fixed at administration, not at absorption. And nothing accelerates it: there is no action in the
games that brings a **Future Sight** forward.

## Withheld until a condition: the Berries

`m006` used this one for absorption and it is the enteric coat exactly. A held **Oran Berry**
restores 10 HP and a held **Sitrus Berry** a flat 30 in the Game Boy Advance games, and **neither
does anything at all** until HP has fallen to half of maximum or below. The amount is unchanged.
The *trigger* is a condition met somewhere further along, and until it is met the item is sitting
in the hand doing nothing.

## Local and systemic, and what covering more ground costs

**Light Screen** and **Reflect** are both `MOVE_TARGET_USER` and both set a side status: they
apply to your half of the field and nowhere else. **Sandstorm** does not work that way. The
end-of-turn routine loops over **every battler on the field** and takes `maxHP / 16` off each one
— both sides, your own team included — unless the Pokémon is Rock, Steel or Ground type, or has
**Sand Veil**, or is underground or underwater.

One confined to a side, one that reaches everything present. That is topical against systemic, and
the exemption list is the reason a systemic agent's effects are hard to predict in advance.

And covering more ground is charged for. In a double battle, a move whose target is both opponents
does **half** damage — that is a separate line in the damage routine, checked after the screen.
**Surf** is one of those, at 95 power and 100 accuracy; **Blizzard** is another. **Earthquake**
goes further and is targeted at foes *and ally*, so it reaches your own partner. `m045` is where
that collateral becomes the whole argument.

## Two turns, committed on the first

**Dig** (60 power, 100 accuracy) and **Fly** (70, 95) are `EFFECT_SEMI_INVULNERABLE`: you choose
on turn one and it lands on turn two, and you cannot change your mind in between. Average the
delivery over the two turns and Dig's 60 is 30 a turn and Fly's 66.5 is 33. The same total, at
half the rate, with a turn of exposure bought in exchange — and being underground during **Dig**
is, per the weather routine above, one of the things that exempts you from a **Sandstorm**. Even
in the games, which route you took changes what reaches you.

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. Two of the errors it
dramatises are among the most serious in medicine, and here the Pokémon framing stops.

A **wrong-route administration** — something intended for a vein given into the spinal fluid, or
the reverse — has killed people, repeatedly, in several countries. The response was not to ask
anyone to be more careful. It was to change the physical design: distinct connectors that will not
join, distinct labelling, distinct storage, mandatory independent checks, and in some systems
arranging that the two can never be in the same room. That is the right answer to an error that is
rare and catastrophic: engineer it out rather than exhort against it.

**Dose dumping** from a crushed modified-release tablet is the quieter one, and it happens for
sympathetic reasons — someone cannot swallow, a feeding tube has to be used, a tablet is halved to
get a smaller amount. The person doing it is almost always trying to help, and that is exactly why
the answer is a different preparation rather than a reprimand.

In both cases the harm was caused by the care rather than by the illness, and the honest word is
iatrogenic. Naming it that way is what makes it reportable, auditable and preventable, and it puts
the fault in a system that allowed the substitution rather than in whoever was holding the pot.

Nothing in this answer or its technical twin indicates whether any particular preparation can be
crushed, split, dispersed or given by a different route. That is product-specific, it is in the
product's own documentation, and a pharmacist can answer it in a sentence. Anyone who cannot
swallow a medicine they have been given should ask their prescriber or pharmacist rather than
alter it.

## What a Gym Leader is listening for

* **Fire Blast** has 25 more power than **Flamethrower** and delivers 7 more. Where did the rest
  go?
* Why is **Zap Cannon** behind a **Lock-On** not a better move?
* Name three routes past a **Light Screen**. Which of them improves the attack? (None.)
* **Fire Spin** on **Blissey**. How much is delivered, over how many turns, and who chose the
  duration?
* Why can nothing in the games make a **Future Sight** arrive early, and what does that fail to
  model?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../for-agents/SOURCES-pharmacology.md`](../../for-agents/SOURCES-pharmacology.md). Specific
to this answer, and to its technical twin:

* **The summary of product characteristics or regulator-approved prescribing information** for the
  specific product — the only authority for its bioavailability, its release mechanism, whether it
  may be crushed or halved, and which routes it is licensed for. A general rule about
  modified-release tablets is not a statement about the one in anybody's hand.
* **A specialist reference on giving medicines to patients who cannot swallow**, or your
  institution's equivalent. That is the document which answers the crushing question properly.
* **Your national medicines regulator's bioequivalence guidance**, for acceptance criteria, for
  the tighter criteria applied to narrow therapeutic index products, and for which products must
  be prescribed by brand. Country-specific.
* **Your institution's injectable medicines policy and its intrathecal administration policy**,
  the latter typically mandatory and separately audited.
* **Your national patient-safety body's alerts** on wrong-route administration.

The Pokémon figures are a different matter and were checked against the public decompilation of
the Game Boy Advance games, read directly: the power and accuracy of Flamethrower, Fire Blast,
Megahorn, Hydro Pump, Cross Chop, Thunder, Blizzard, Zap Cannon, Fissure, Surf, Brick Break, Dig,
Fly, Future Sight and Doom Desire; Clamp, Wrap, Bind, Fire Spin, Sand Tomb and Whirlpool all
carrying `EFFECT_TRAP`, the trap counter being set to `(Random() & 3) + 3` and decremented at the
end of each turn with `maxHP / 16` taken while it remains non-zero; Lock-On and Mind Reader
setting `STATUS3_ALWAYS_HITS` for two turns with the guaranteeing battler recorded, and the
accuracy routine honouring it; Light Screen halving special damage, reducing it to two-thirds in a
double battle with two live defenders, and applying only when the critical multiplier is 1, with
Reflect covering the physical route; Brick Break removing a screen before hitting; Future Sight
and Doom Desire setting a counter of 3 and having their damage computed at the moment of use and
stored; the Oran Berry's 10 HP and the Sitrus Berry's flat 30 in these games, both gated on HP at
or below half; Light Screen and Reflect being `MOVE_TARGET_USER` side statuses; the sandstorm
end-of-turn routine taking `maxHP / 16` from every battler present except Rock, Steel and Ground
types, Sand Veil holders, and Pokémon underground or underwater; the halving of a both-opponents
move's damage in a double battle; Earthquake's target being foes and ally; Dig and Fly carrying
`EFFECT_SEMI_INVULNERABLE`; and Rapid Spin clearing exactly one of trapping, Leech Seed or Spikes
per use, in that order. The arithmetic in the blocks above is recomputed from those figures rather
than recalled.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** Every figure
in the technical twin is an illustrative round number chosen to make the extraction-ratio and
release-profile arithmetic legible, and none is a real product's bioavailability, dose or
bioequivalence limit. In particular, nothing in either half indicates whether any specific
preparation can be crushed, split, dispersed or given by a different route — that is
product-specific information held in the product's own documentation, and a pharmacist is the
fastest route to it. Nothing here should be used to make a decision about anyone's treatment,
including your own. Anyone who cannot swallow a medicine should ask their prescriber or pharmacist
rather than alter it.

## Where this stands, October 2026

The three-variable framing — fraction, rate, barrier — is mechanism and does not date, and the
game mechanics cited are fixed in released software, though the series has changed several of them
between generations and this answer pins the ones it uses to the Game Boy Advance games. What
dates is everything product-specific and everything regulatory: which products exist in which
release forms, which must be prescribed by brand, what the bioequivalence acceptance criteria are
and which products attract the tighter ones, and the device-standard changes introduced in several
countries to engineer out wrong-route connections. Those are regulator and national-safety-body
decisions, they differ between countries, and they change. Check the current product information
and your own regulator.
