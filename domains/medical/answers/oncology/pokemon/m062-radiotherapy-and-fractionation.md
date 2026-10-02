---
id: "m062"
slug: radiotherapy-and-fractionation
style: pokemon
category: oncology
difficulty: advanced
question: "What does ionising radiation actually do to a cell, and why is a course of radiotherapy divided into many small fractions instead of being given all at once?"
tags: [radiotherapy, fractionation, dna-damage, therapeutic-ratio, radiobiology]
---

# Rock Blast lands five times in one turn. Ingrain pays out once per turn.

Two mechanics from Emerald's own code, and between them they are fractionation.

**Multi-hit moves resolve inside a single turn.** `Cmd_setmultihitcounter` draws the count:
`Random() & 3`, and if that comes out above 1 it redraws as `(Random() & 3) + 2`, otherwise it
adds 2 to what it had. The distribution falls out as two and three hits at three-eighths each,
four and five at one-eighth each. **Rock Blast** is 25 base power a hit, **Bullet Seed** 10,
**Fury Swipes**
18. Five hits, one turn, and nothing happens in between them.

**Ingrain pays out at the end of a turn.** Read `ENDTURN_INGRAIN`: a sixteenth of maximum HP,
floored to a minimum of 1, once per turn, and only if HP is below maximum. **Leftovers** is the
same arithmetic in `HOLD_EFFECT_LEFTOVERS`.

So: deliver a total inside one turn and the recovery mechanic fires once. Deliver the same total
across five turns and it fires five times. **Nothing about the total changed. The schedule
changed, and the schedule is worth something only to whoever has the recovery mechanic.** That is
fractionation, exactly: it does not work because small doses are gentler, it works because the gap
between them is worth more to one tissue than to another.

As elsewhere in this specialty: **the objects of study are move data, end-of-turn routines,
weather flags and targeting rules.** No Pokémon in this answer stands in for a person with cancer,
and the analogy is dropped entirely at the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
(**consensus**, **country-dependent**).

## The two schedules, drawn

```
   THE SAME TOTAL, TWO SCHEDULES

   one turn, five hits        │  five turns, one hit each
   ───────────────────────────┼──────────────────────────────────────────────
   ▓▓▓▓▓  →  end of turn      │  ▓ ·recover· ▓ ·recover· ▓ ·recover· ▓ ·…· ▓
             ONE payout of    │
             maxHP/16         │  FIVE payouts of maxHP/16 — but only to
                              │  whoever is holding Leftovers or is Rooted
   ───────────────────────────┴──────────────────────────────────────────────

   AND THAT IS THE ENTIRE ARGUMENT.  Split the dose and the side with the
   better repair between fractions keeps more of itself.  The tumour repairs
   sublethal damage LESS WELL than the late-responding normal tissue does, and
   that tissue is also disproportionately sensitive to FRACTION SIZE — so
   smaller fractions cost control little and spare it a lot.

   Where both sides hold Leftovers, splitting buys NOTHING.  Fractionation
   exploits a DIFFERENCE; no difference, no gain.

   ────────────────────────────────────────────────────────────────────────────

   AND FOUR THINGS HAPPEN IN THE GAP, ON FOUR TIMESCALES:

     REPAIR           hours       the end-of-turn payout.  Sublethal damage
                                  repaired, better by the dose-limiting
                                  tissue than by the tumour
     REDISTRIBUTION   hours       Fly and Dig.  See below — at any instant
                                  part of the population is in a state your
                                  move cannot reach, and the state is
                                  TRANSIENT
     REOXYGENATION    days        the weather multiplier.  Same move, same
                                  target, different achieved damage because
                                  the FIELD changed
     REPOPULATION     days–weeks  the payout keeps firing for the tumour too.
                                  Stretch the schedule far enough and you are
                                  funding the thing you are treating, which is
                                  why OVERALL TIME is a variable and an
                                  unplanned gap is a problem
```

## One more thing about the count, and it is the difference from a prescription

The honest disanalogy, before anything else is built on it. In Emerald the **number** of hits is
*drawn*. A prescription is not. From the fourth generation on, **Cloyster**'s ability list
includes **Skill Link**, which fixes a two-to-five-hit move at its maximum every time, and that —
not the random draw — is the shape of a radiotherapy schedule: a declared number of fractions, of
a declared size, delivered on declared days, with the plan built on the assumption that all of
them arrive.

Which is precisely why an unplanned gap is a problem rather than an inconvenience (**consensus**).
It is not that the course got shorter. It is that the schedule the plan was computed against is no
longer the schedule that was delivered, and the repopulation term is the one that moves. Cloyster,
incidentally, has base Defense 180 against base HP 50 in its species data — a reminder that the
thing a plan is built around is a specific set of numbers, not a tendency.

## What the radiation actually does, and why the kill is a fraction

Energy deposited in tissue ionises along the track, and DNA damage follows two ways
(**mechanism**): directly, within the DNA, and indirectly, through reactive species made from
water — the larger route for the photon beams in widest clinical use, and an **oxygen-dependent**
one. Single-strand breaks and base damage are repaired efficiently. The lesion that matters is the
**double-strand break** left unrepaired or repaired wrongly, and a cell carrying it usually dies
at its next attempted division rather than on the spot, which is why effects arrive on the
timescale of each tissue's own turnover. Misrepair producing chromosomal rearrangement is also the
mechanistic basis of radiation-associated second malignancy, a stochastic late effect rather than
a threshold one (**consensus**).

Now the part the games state better than any survival curve, and it is three lines of code.

**Super Fang** takes half of what is on the bar. `Cmd_damagetohalftargethp` is literally
`gBattleMons[gBattlerTarget].hp / 2` — current HP, not maximum — **and then, if that came out as
zero, the code sets it to 1.** Halving is a *fraction*, so Super Fang approaches the bottom of the
bar and never arrives there by halving alone; the floor is what finishes it, and the floor is a
separate instruction. Compare **Seismic Toss** and **Night Shade**, both `EFFECT_LEVEL_DAMAGE`,
both taking a fixed absolute amount equal to the user's level. Two completely different
relationships with how much is there. The limiting case is **Shedinja**, whose base HP in the
species data is **1**: half of 1 is 0, so the halving contributes nothing at all and only the
floor instruction does any work.

Radiation is Super Fang (**mechanism**). A dose increment removes a *proportion* of the surviving
population, so survival falls multiplicatively, the curve approaches zero and does not reach it,
and a radical prescription is chosen to achieve a high **probability** of control rather than a
certainty of it. The honest statement of what a dose does is probabilistic, and anyone who tells
you otherwise has mistaken the floor for the function.

And the targeting field says the other structural thing. Radiotherapy is `MOVE_TARGET_SELECTED`: a
declared target, dose deposited where the beam is and nowhere else. Systemic therapy, as the
earlier answer in this specialty laid out, is **weather** — a field condition with no declared
target at all. That is the cleanest contrast available between the two, and it is why a target
volume gets drawn, argued over and recorded.

## Redistribution: Fly and Dig, and the state your move cannot reach

Read `Cmd_accuracycheck` and the rule is explicit. A target carrying `STATUS3_ON_AIR`, from
**Fly**, or `STATUS3_UNDERGROUND`, from **Dig**, produces `MOVE_RESULT_MISSED` outright — *unless*
the incoming move carries the matching ignore flag, which only a handful of moves do.
**Earthquake** reaches a target that is underground — send a **Dugtrio** below ground and that is
very nearly the only thing that will find it. **Lock-On** overrides the whole check, which is the
exception that proves it is a check.

Two properties of that state are the ones that matter, and both are real:

* **It is a property of the target's current state, not of its identity.** The same Pokémon is
  reachable this turn and unreachable the next.
* **It is transient.** Fly and Dig resolve on the following turn and the state clears by itself.

Which is redistribution (**mechanism**). At the moment any one fraction is delivered, part of the
surviving population is in a phase of the cell cycle in which that fraction achieves relatively
little. The population then moves on. So a second fraction, later, meets a differently distributed
population, and over a course each sub-population is caught at a point where it is reachable. One
enormous exposure gets one draw on that distribution. Many fractions get many.

## Reoxygenation: the field changes what a hit achieves

The clinical fact is that the indirect damage route needs oxygen, so a hypoxic region of a tumour
is relatively radioresistant, and as the tumour shrinks previously hypoxic regions regain a blood
supply and stop being protected (**mechanism**, **consensus**).

The games have this as weather, and the numbers are in Emerald's damage calculation. In rain, Fire
damage is halved and Water damage is multiplied by fifteen tenths. In harsh sunlight it is the
reverse. **Solar Beam** is the sharpest instance and it is read off the field twice: it is halved
by rain, by sandstorm and by hail alike — by *any* weather except sun — and in sun it fires
without its charge turn at all, because `AttacksThisTurn` returns the not-charging value for it
the moment the sun flag is set. So a **Venusaur** holding Solar Beam is a different proposition in
every weather, with nothing about Venusaur or the move having changed.

And who set the field is a separate question from what the field does. **Groudon**'s **Drought**
brings the sun and **Kyogre**'s **Drizzle** brings the rain, and once either is up the multipliers
apply to everything in scope regardless of what is still on the field.

The strongest version of the point is **Castform**, and it is exact. With **Forecast**, the
routine rewrites Castform's own **type** from the weather flags: Fire in sun, Water in rain, Ice
in hail, Normal when there is no weather with an effect. The environment does not merely scale
what a hit achieves — it can change what the thing being hit *is*. That is the hypoxic fraction in
one mechanic: the same tissue, differently radiosensitive, because of the state of its
surroundings.

Weather in Emerald is also set as a *temporary* condition and reverts, which is the shape of the
clinical point: the protection is a property of the environment, and when the environment changes
the protection goes with it.

**And be exact about what is carried across, because it would be easy to read it wrongly.** What
is mapped is *an environmental multiplier on a delivered effect*. Nothing in the weather stands in
for a person, for a tumour's seriousness or for anybody's chances. The point is a property of the
field.

## Acute against late, and why it is not a matter of degree

This distinction does more clinical work than anything else here, and it maps onto the two kinds
of cost this specialty has already separated (**mechanism**).

**Acute reactions** are the dividing-tissue effect in the treated field — mucosa, skin, marrow
where it is in the beam. The dividing compartment is hit, the surface it supplies is not replaced,
the effect appears during or shortly after the course, it tracks intensity and volume, and it
**recovers**, because the progenitor pool regenerates. That is the proportional, recoverable cost
— the recoil computed from the damage actually dealt, in this specialty's established vocabulary,
and the end-of-turn payout is what makes recovery possible.

**Late reactions** are the other kind entirely: fibrosis, vascular and microvascular injury,
neural injury, appearing months to years later, governed strongly by **fraction size** rather than
by overall intensity, and largely **not** recovering (**consensus**). This is the flat charge that
accumulates and is never refunded, and it is what actually limits a radical dose. Hence: an acute
reaction is managed and waited out; a late reaction is prevented at the planning stage or not at
all.

## The therapeutic ratio, and the two levers

Everything in radiotherapy is the ratio of effect on the target to effect on normal tissue, and
there are exactly two ways to move it (**mechanism**):

* **Physically.** Less dose in normal tissue for the same dose in the target — planning,
  immobilisation, image guidance, conformal and modulated delivery, brachytherapy,
  charged-particle beams. And the dose–volume relationship matters as much as the dose: the same
  dose to part of an organ is a different proposition from the same dose to all of it.
* **Biologically.** Exploit a difference between the target and the normal tissue. Fractionation
  is the oldest and most reliable such lever, and concurrent radiosensitising systemic therapy is
  another that works by widening the difference at the cost of adding toxicity (**consensus**,
  with (**country-dependent**) regimens).

So "more dose" is never the whole answer and "less dose" is never a safe default. And the honest
limit, which the multi-hit code supplies itself: **splitting a total is only ever worth what the
difference in recovery is worth.** Where the tumour's fractionation sensitivity resembles that of
the dose-limiting tissue, fewer and larger fractions can give equivalent control with acceptable
late effects — which diseases those are, and what is actually offered, is (**consensus**) in
principle and firmly (**country-dependent**) in practice.

## Where the metaphor stops

Everything above is physics, repair kinetics and scheduling, and code with a readable end-of-turn
routine is a good place to see why a schedule has the shape it has. What follows is about people,
so it is said plainly and without the analogy.

A radical course means attending for treatment repeatedly over weeks, often while already
exhausted, often alongside other treatment, and often a long way from home. Acute reactions in a
treated field are painful, and they can interfere with eating, swallowing, washing and sleeping;
calling them self-limiting is accurate and is not reassurance. Late effects are permanent. They
are the ones people live with for the rest of their lives, and the fact that they were weighed
carefully at planning does not make them any smaller for the person who has them. Depending on the
site, fertility, sexual function, continence, lymphoedema, appearance and cognition are all in
scope, and each of those is somebody's life and not a row in a constraint table.

The possibility of a radiation-associated second malignancy is real, and it is a genuinely hard
thing to hold alongside a treatment given with the intention of cure. None of the arithmetic above
says what will happen to any individual, and no figure of any kind appears in either half of this
answer for that reason.

## What a Gym Leader is listening for

* Five hits in one turn against one hit in each of five turns. Which mechanic makes the
  difference, and who does it benefit?
* What happens to the argument for fractionation if both sides are holding Leftovers?
* Super Fang halves current HP and the code floors the result at 1. Which half of that is the
  radiobiology, and which half is the thing that makes a survival curve finite?
* Why does Earthquake reach a target that is underground when almost nothing else does, and what
  is that an analogy for?
* Solar Beam is halved by any weather except sun. Name the clinical property that is.
* Three of the four Rs argue for prolonging a course and one argues against. Which, and what does
  that imply about an unplanned gap?
* Why is an acute reaction managed and a late reaction prevented?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific to
this answer:

* A current standard textbook of radiobiology, for the damage mechanisms, the survival-curve
  argument, the four Rs and the fraction-size dependence of late-responding tissue.
* Your national or regional body for radiotherapy practice and its published dose-fractionation
  guidance, for which schedules are used for which indication where you work. These differ
  materially between countries.
* Your centre's own radiotherapy protocols and normal-tissue dose constraints, which bind local
  practice and are the only place a constraint should be read from.
* The consensus normal-tissue tolerance literature your planning service works to, for the
  dose–volume relationships described in general terms here.
* The primary literature, for any claim about hypofractionation in a specific disease, which is
  active and is where practice has moved most.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about radiobiology and schedule design, dressed in a game so that the
difference between a total and a schedule stays concrete. It has had no clinical review. **No
dose, fraction size, number of fractions, fractionation-sensitivity value or normal-tissue
constraint appears here, and none should be inferred** — those belong to the protocol and the
planning system, which are the authority, and this is not. Schedules differ substantially between
countries, regions and centres and are revised; yours governs. Nothing here describes any
individual's treatment, and nothing here is a guide to managing a reaction in a real person.
Anyone affected by cancer — their own diagnosis or someone else's — should be talking to the
clinical team looking after that person, who have the plan, the images and the history, none of
which are here, and anyone unwell during a course should use the on-treatment or acute oncology
route their centre gave them rather than reading this. The analogy carries scheduling and
environment only: no part of it stands in for a person, and none of it says anything about what
happens to anybody.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source. The multi-hit count is drawn in
`Cmd_setmultihitcounter` as `Random() & 3`, redrawn as `(Random() & 3) + 2` when that exceeds 1
and otherwise incremented by 2, which gives two and three hits at three-eighths each and four and
five at one-eighth each; the base powers quoted are Rock Blast 25, Bullet Seed 10 and Fury Swipes
18 from the move data. Ingrain's end-of-turn heal is a sixteenth of maximum HP floored at 1 in
`ENDTURN_INGRAIN`, and Leftovers is the same arithmetic under `HOLD_EFFECT_LEFTOVERS`. Super Fang
is `Cmd_damagetohalftargethp` — current HP divided by two, set to 1 if that is zero — and Seismic
Toss and Night Shade are both `EFFECT_LEVEL_DAMAGE`. The semi-invulnerability rule, the ignore
flags and Lock-On's override are in `Cmd_accuracycheck`; Fly is 70 base power at 95 accuracy and
Dig 60 at 100. The weather multipliers — Fire halved and Water multiplied by fifteen tenths in
rain, the reverse in sun, and Solar Beam halved by rain, sandstorm or hail — are in the base
damage calculation in `src/pokemon.c`, Solar Beam's skipped charge turn in sun is the first test
in `AttacksThisTurn` in the battle script commands, and weather is set as a temporary condition in
the same project. Castform's type being rewritten to Fire, Water, Ice or Normal from the weather
flags, conditional on it having Forecast, is the routine quoted in `src/battle_util.c`. Shedinja's
base HP of 1 is in the species data.

Three Pokémon facts here are **not** from Emerald's own code and are marked as such rather than
left to imply otherwise. Cloyster's ability list including Skill Link from the fourth generation
on, and its base Defense of 180 against base HP 50, are read from the Emerald expansion's species
data, which is a fan reimplementation rather than an official source; what Skill Link does — fix a
two-to-five-hit move at its maximum — is described from working knowledge of the fourth generation
and later, not from a routine opened here. Drought and Drizzle as the abilities Groudon and Kyogre
bring the sun and the rain with are from working knowledge of those games. Everything else Pokémon
here is Emerald-generation; later generations changed some of these values and none of those later
values is quoted.

The radiobiology is old and stable: the damage mechanisms, the primacy of the double-strand break,
the multiplicative survival argument, the four Rs and the greater fraction-size sensitivity of
late-responding tissue have been the standing account for decades and are the least likely part of
this answer to date. What moves is the schedule — the direction of travel in several diseases has
been towards fewer, larger fractions where the biology allows, and towards tighter physical
conformality, with uptake uneven between countries and often determined by availability rather
than by evidence. No schedule, dose or constraint is quoted here, deliberately. Those are the
facts that date, and they belong to the protocol in force where the reader works.
