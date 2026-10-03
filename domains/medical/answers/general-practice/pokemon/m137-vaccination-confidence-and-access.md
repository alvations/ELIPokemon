---
id: "m137"
slug: vaccination-confidence-and-access
style: pokemon
category: general-practice
difficulty: advanced
question: "Why are confidence and access two different problems in a vaccination programme, and what follows from the fact that an unvaccinated person looks the same either way?"
tags: [vaccination, coverage, access, confidence, population-health]
---

# One step, six ways to produce nothing, and the engine stores which one only until the next step

This specialty's vocabulary is filters, and the two it was built on sit four lines apart in
`src/wild_encounter.c`:

```
   if (flags & WILD_CHECK_REPEL    && !IsWildLevelAllowedByRepel(level))    return FALSE;
   if (... && flags & WILD_CHECK_KEEN_EYE && !IsAbilityAllowingEncounter(level)) return FALSE;
```

m011 and m081 took the first, m111 took its threshold, m082 took the nine rate levers in front of
both, m112 took the path that runs neither, and m113 took the fourth filter in the family. What
this answer takes is the thing none of them needed: **the two filters are different questions, the
step that fails either one produces exactly the same nothing, and no part of the engine records
which.**

Nothing here is ill, no creature stands in for a person, and nothing is being persuaded of
anything. The object of study is a conjunction of independent tests with one shared output.

## The two filters, read field by field

```
   READ OUT OF src/wild_encounter.c.

                            IsWildLevelAllowedByRepel        IsAbilityAllowingEncounter
   ──────────────────────── ──────────────────────────────── ──────────────────────────────────
   what it needs first      VAR_REPEL_STEP_COUNT non-zero    the lead not being an egg
                            - i.e. an ITEM, consumed, that
                              somebody had to buy and use
   whom it reads            walks all six slots and stops    gPlayerParty[0] ONLY. Not the
                            at the FIRST member with HP        first healthy one. Slot zero
                            that is not an egg
   what about them          that member's LEVEL               that member's ABILITY, and only
                                                              Keen Eye or Intimidate
   the comparison           wildLevel < ourLevel -> cancel    level <= leadLevel - 5 -> cancel
   a precondition           none                              leadLevel > 5, so the whole
                                                              filter is unreachable with a
                                                              lead at level 5 or below
   how reliable             deterministic                     !(Random() % 2). It fires on
                                                              HALF the eligible steps
   failure with nothing     no member with HP at all ->       lead is an egg -> returns TRUE,
   to read                  falls through to FALSE and          which cancels nothing
                            cancels EVERY encounter
   what it costs            Repel 100 steps at 350,          nothing. It is a standing
                            Super Repel 200, Max Repel         property of whoever is in
                            250 at 700                         front
   ──────────────────────────────────────────────────────────────────────────────────────────
   TWO TESTS. NEITHER SUBSTITUTES FOR THE OTHER. A Max Repel does nothing whatever
   about the ability term, and putting a Keen Eye lead in slot zero does nothing
   whatever about the Repel term. And both of them return the same FALSE.
```

The asymmetries are the whole point. One term is a consumable somebody has to possess, remember
and spend; the other is a standing property of whoever happens to be in front. One is
deterministic; the other works half the time it applies. One reads the first party member with HP;
the other reads slot zero whatever is in it. They are not two settings of one dial. They are two
unrelated tests whose only shared feature is what happens when either says no.

## Six exits, one nothing

```
   ONE ORDINARY STEP ON GRASS, in StandardWildEncounter. Every arrow marked X
   returns FALSE, and the player sees an ordinary step with nothing in it.

   step taken
      │
      ├─X  sWildEncountersDisabled                     (a script switched it off)
      │
      ├─X  landMonsInfo == NULL                        (this map has no table)
      │
      ├─X  new metatile type AND Random() % 100 >= 60  (a 40 per cent silent skip)
      │
      ├─X  WildEncounterCheck failed                   (the rate: x16, Mach Bike or
      │                                                 Acro Bike x80/100, WHITE or
      │                                                 Black Flute +/-50 per cent,
      │                                                 Cleanse Tag, lead Stench /2,
      │                                                 Illuminate x2, White Smoke /2,
      │                                                 Arena Trap x2, Sand Veil /2 in
      │                                                 sandstorm, capped at 2 880,
      │                                                 then one roll - m082's nine)
      │
      ├─ roamer branch: Latios or Latias is on this map
      │     └─X  !IsWildLevelAllowedByRepel(roamer->level)
      │          the Repel, called INLINE here, and the ability filter is not
      │          consulted at all on this path
      │
      └─ TryGenerateWildMon(..., WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE)
            ├─X  the Repel said no
            └─X  the lead's Keen Eye or Intimidate said no

   SIX CAUSES. ONE OBSERVABLE. And nothing is written anywhere: the next step
   re-rolls every one of them from scratch, so not even the previous answer
   survives to be compared with this one.
```

The only cause in that list that ever announces itself is the Repel, and it announces the wrong
thing: when `VAR_REPEL_STEP_COUNT` reaches zero the game runs `EventScript_RepelWoreOff` to tell
you the *item* has ended. It never told you it was working.

## Which tests are even run depends on which door you came in by

This is the part that is easy to miss, because the two filter checks look unconditional and are
not. They are bits in a `flags` argument, and the caller decides.

```
   WHO PASSES WHAT, read from the call sites

   an ordinary land or water step .... WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE   both
   a mass outbreak .................. WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE   both
   the roaming Latios or Latias ..... the Repel, inline; the ability never asked
   the Battle Pyramid ............... WILD_CHECK_KEEN_EYE                      one
   the Battle Pike .................. WILD_CHECK_KEEN_EYE                      one
                                      - and then the second check carries
                                        gMapHeader.mapLayoutId != LAYOUT_BATTLE_
                                        FRONTIER_BATTLE_PIKE_ROOM_WILD_MONS, so in
                                        Lucy's facility even that one is switched off
                                        by a comparison against the room
   Sweet Scent ...................... flags = 0                                none
   fishing .......................... GenerateFishingWildMon takes no flags at all
```

Seven entry points, five different subsets of two tests. A Trainer's protection is not a property
of the Trainer or of the route; it is a property of **which function was called**, and nothing in
the overworld tells you which one that was. m112 found the same shape in fishing and made the
distinction that matters: Sweet Scent's zero is deliberate, and fishing's missing argument is a
parameter nobody threaded through. The Battle Pike's exclusion is a third kind — written on
purpose, in the condition itself, naming one room.

## The one lever that changes which thing appears, and the denominator it reads

The nine rate levers do not touch a slot, which m082 established and m112 restated. There is an
exception the family has not used, and it is instructive.

Before the ordinary slot roll, `TryGenerateWildMon` tries twice to let the lead bias *which* slot
comes up: `TryGetAbilityInfluencedWildMonIndex` with **Magnet Pull** against Steel, then with
**Static** against Electric. Each attempt reads `gPlayerParty[0]`, requires that exact ability,
and then fails on `Random() % 2 != 0` — so, like the second filter, it is a half-of-the-time
intervention. On success it calls `TryGetRandomWildMonIndexByType`, which collects the slots of
the matching type and picks among them.

Two properties of that helper are worth having.

**It is a no-op at both ends of the range.** `if (validMonCount == 0 || validMonCount == numMon)
return FALSE;` — a lead with **Magnet Pull** changes nothing on a route with no Steel-type in the
table, which is unsurprising, and changes nothing on a route where *every* slot is Steel, which is
the interesting half. A targeted lever aimed at a subgroup does nothing when the subgroup is empty
and nothing when the subgroup is everybody.

```
   A TARGETED LEVER, WORKED OUT ON ONE ROUTE. Every figure read from
   src/data/wild_encounters.json, with the Generation III twelve-slot shares.

   Route 110, land table, encounterRate 20:

     slot  share  species      Electric?        ordinary weighted roll
     ────  ─────  ───────────  ─────────        ──────────────────────
       1    20%   Poochyena        no            Electrike ...... 30%
       2    20%   Electrike       YES            Minun .......... 15%
       3    10%   Gulpin           no            Plusle .......... 2%
       4    10%   Electrike       YES            everything else  53%
       5    10%   Minun           YES
       6    10%   Oddish           no
       7     5%   Minun           YES
       8     5%   Gulpin           no
       9     4%   Wingull          no
      10     4%   Wingull          no
      11     1%   Plusle          YES
      12     1%   Plusle          YES

   Now put a Static lead in slot zero. Half the steps take the biased path, and
   that path returns validIndexes[Random() % validMonCount] - UNIFORMLY OVER THE
   SIX MATCHING SLOT INDICES, with the slot shares thrown away:

     biased draw      Electrike 2/6, Minun 2/6, Plusle 2/6   = 33.3% each

     overall, half biased and half not
       Electrike   0.5 x 33.3 + 0.5 x 30   =  31.7%     from 30%  - barely moved
       Minun       0.5 x 33.3 + 0.5 x 15   =  24.2%     from 15%
       Plusle      0.5 x 33.3 + 0.5 x  2   =  17.7%     from  2%  - almost nine
                                                                    times over

   THE LEVER WAS AIMED AT A TYPE AND MOST OF ITS EFFECT LANDED ON THE SMALLEST
   MEMBER OF THAT TYPE. Nothing about Plusle was targeted. It is over-represented
   because the selection is uniform over eligible SLOTS while the eligible slots
   carry unequal shares - so the largest relative change always goes to whoever
   held the smallest share beforehand, and the intended beneficiary moves least.
```

Two routes make the early return concrete in both directions. On **Route 116** there is no
Electric-type and no Steel-type in the twelve slots — Poochyena 28 per cent, Whismur 20, Nincada
20, Taillow 20, Abra 10, Skitty 2 — so `validMonCount` is zero and both abilities do nothing. And
**Rusturf Tunnel** is the other end: all twelve slots are Whismur, so for any ability biasing
towards *that* type `validMonCount == numMon` and the function returns FALSE as well. Empty target
group and universal target group, same return value, same observable.

**And in the shipped game it is handed the wrong denominator.** The function takes a slot count,
and the vanilla call passes `NUM_LAND_MONS_ENCOUNTER_SLOTS` for every area — including the water
case, whose table is shorter. `pokeemerald` fixes this behind `#ifdef BUGFIX` by threading the
real size through; without the fix the count is simply wrong, the error is silent, and the only
thing on screen is an encounter that looks exactly like all the others. A rate measured against a
denominator nobody checked is the oldest failure in this whole subject, and the cartridge contains
it as a compile-time switch.

## Nothing in the engine stores a reason

Here the game has nothing, and saying so is the point rather than a gap.

There is no field anywhere — not in `gSaveBlock1Ptr`, not in the wild-encounter module, not in the
Pokédex — that records why a step produced no encounter. The Pokédex has `Seen` and `Own` flags,
which nursing m037 used for documented-as-encountered against documented-as-confirmed, and m084
found that `GetSetPokedexFlag` has no case that clears a bit. But neither flag array has a third
state for *this did not happen, and here is which test refused it*. The closest the engine comes
is a counter of steps remaining on an item.

So the register holds the result. It does not hold the cause, no later query can recover the
cause, and every step re-rolls the whole conjunction. That is not a limitation of the analogy; it
is the same limitation the subject has.

## Where the metaphor stops

The people least likely to be counted as vaccinated are, repeatedly and in many countries, the
people least likely to be registered with a service, least likely to have a usual clinician, most
likely to be moving between addresses, and most likely to have had experiences of health care that
give them no reason to expect to be listened to. That is the inverse care law operating on a
preventive programme, and m050 is the argument for why it is a mechanism rather than a complaint.

It also matters how the uncounted are described. A person who was never reached, a person who
could not get there, a person with a question nobody answered and a person who has considered the
offer and declined are four different situations that produce one identical entry in a record.
Collapsing them is inaccurate, and it does real damage: it attributes to individual choice a
shortfall that is mostly structural, and it makes the conversation with the fourth group harder by
having been held in public about all four. This answer does not characterise anybody's reasons,
and that is a deliberate limit.

And the asymmetry nobody involved escapes. Serious adverse events following immunisation are rare
and they are real, and when one occurs it occurs to an identifiable person who was well, who
attended for prevention, and whose harm is attributable to a specific act on a specific day.
Infections that did not happen are neither identifiable nor attributable to anyone. Holding both
of those honestly is genuinely uncomfortable, and the discomfort is not evidence of having
reasoned badly. The answer is not to flatten either side: a population-level benefit and an
individual-level harm can both be real, surveillance exists because of the second, and no
arithmetic about the first makes the second easier for the person it happened to.

## What a Gym Leader is listening for

Whether the Trainer reads the two filters as separate tests rather than as one protection, and
names at least four of the asymmetries — item against standing property, all six slots against
slot zero, deterministic against a one-in-two roll, and the two different ways each behaves with
nothing to read. Then the six exits of one step, with the 40 per cent new-metatile skip and the
roamer's inline Repel both offered unprompted. Then the flags: five different subsets across seven
entry points, with **Sweet Scent**'s deliberate zero distinguished from fishing's missing argument
and from the Battle Pike's named exclusion. Then **Magnet Pull** and **Static** as the one lever
that touches a slot, with the `validMonCount == numMon` no-op explained rather than just quoted.
Then the `#ifdef BUGFIX` denominator. Then the absence: no field anywhere stores which test
refused, and the Pokédex's two flag arrays have no third state. Then the hardest one — what a
Trainer would have to log, on every step, to be able to tell afterwards which term was binding.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The reader's national immunisation schedule and its accompanying handbook, issued by the
  national public health body or health department, which is the authority for every age,
  interval, product, contraindication and catch-up route — none of which is named in this pair
  (**country-dependent**).
* The national guidance on vaccine storage and the cold chain, and the local standard operating
  procedure derived from it.
* The national adverse-event reporting scheme for vaccines, for how a suspected reaction is
  reported and what the scheme's known biases are.
* The World Health Organization's published material on the behavioural and social drivers of
  vaccination, which is where the mainstream separation of the demand-side terms is set out.
* The reader's own practice-level and area-level coverage data, disaggregated by population group,
  which is the only place the local version of this argument can be settled.

The Pokémon facts are a separate matter and are not covered by the line above. The two filter
checks and their `WILD_CHECK_REPEL` and `WILD_CHECK_KEEN_EYE` bits; `IsWildLevelAllowedByRepel`
returning TRUE on a zero step counter, walking all six slots to the first with HP that is not an
egg, comparing the wild level against that member's, and falling through to FALSE;
`IsAbilityAllowingEncounter` reading `gPlayerParty[0]` only, accepting Keen Eye or Intimidate,
requiring a lead above level 5, cancelling at or below the lead's level minus five and firing on
`!(Random() % 2)`; the 100, 200 and 250 step counts and the 350 and 700 prices of the three
Repels; the six FALSE exits of the land path in `StandardWildEncounter` including the 40 per cent
new-metatile skip, the rate pipeline with its nine levers and its 2 880 cap, and the roamer
branch's inline Repel call; the flag subsets passed by the Battle Pike, the Battle Pyramid, Sweet
Scent and fishing, and the Pike's map-layout exclusion inside the second check;
`TryGetAbilityInfluencedWildMonIndex` with Magnet Pull and Static, its `Random() % 2` gate, the
`validMonCount == 0 || validMonCount == numMon` early return, and the `#ifdef BUGFIX` slot-count
argument; and `EventScript_RepelWoreOff`, were all read directly from the pret decompilation
projects, which this environment can reach. These are Emerald's.

## Scope and safety

This is revision material about how a vaccination programme behaves as a system, written for
someone already training in or qualified for the field. It is not a clinical reference, not a
decision aid, and nothing here should inform whether any individual receives any vaccine, when, or
in what order. **No schedule, age, interval, dose, contraindication, coverage figure or
population-protection threshold is named in this pair on purpose** — all are set nationally, all
are revised, and the national schedule and its handbook are the only acceptable source for them.
Nothing here is a statement about the safety or effectiveness of any particular product. No
individual's or group's reasons for a decision are characterised, and this answer contains no
method for changing anybody's mind. The step counts, prices, multipliers and slot counts above are
real and stand in for a mechanism; none of them is a clinical quantity and no clinical figure
should be read out of them. If someone is unwell right now, the relevant action is to contact
local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The structural claims — that coverage is a product of terms, that the binding term dominates, that
access and the decision are different terms with different remedies, that the record stores the
result rather than the cause, and that benefits are unattributable while harms are not — are
mechanism and consensus, and they are stable. Everything specific moves: schedules, products,
eligible groups, catch-up arrangements, the channels through which offers are made, and who may
administer. The evidence on what improves uptake has grown substantially and remains
setting-dependent. The Emerald code is stable because the games are finished, except that `BUGFIX`
is a switch in an actively maintained decompilation and a reader should check which side of it
they are reading. Take the schedule and everything attached to it from current national guidance
rather than from here, as of October 2026.
