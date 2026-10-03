---
id: "m150"
slug: antivirals-and-antifungals
style: pokemon
category: pharmacology
difficulty: advanced
question: "Why are antivirals and antifungals harder to develop and to use than antibacterials, and what does the pursuit of selective toxicity cost in each case?"
tags: [antivirals, antifungals, selective-toxicity, resistance, diagnosis]
---

# Surf and Earthquake differ by one field, and it is not the power. Selectivity lives in `target`.

```
   src/data/battle_moves.h

   [MOVE_SURF] =            power  95   type WATER    target MOVE_TARGET_BOTH
   [MOVE_EARTHQUAKE] =      power 100   type GROUND   target MOVE_TARGET_FOES_AND_ALLY
   [MOVE_SELF_DESTRUCT] =   power 200   type NORMAL   target MOVE_TARGET_FOES_AND_ALLY
   [MOVE_EXPLOSION] =       power 250   type NORMAL   target MOVE_TARGET_FOES_AND_ALLY
```

In a double battle, Surf hits both opponents and leaves your partner alone. Earthquake hits both
opponents **and your partner**. The two moves have almost the same power and the same accuracy,
and the difference is one enumerated constant in one field of a data row.

That is selective toxicity, and it is the whole of this topic. Whether an agent can tell your side
from the other side is **not a function of how hard it hits**. It is a property of the
relationship between the mechanism and the thing it acts on, written in a field you have to go and
read.

In this answer the move is the drug, the opposing Pokémon is the pathogen, and the partner is the
host's own tissue. No Pokémon stands in for a patient.

## The ladder: three abilities, one job, three spectra

`IsRunningFromBattleImpossible` in `src/battle_main.c` runs three trapping checks in order, and
reading them in source order is reading the spectrum argument.

```
   if (gBattleMons[gActiveBattler].ability == ABILITY_RUN_AWAY)
       return BATTLE_RUN_SUCCESS;                    ← checked FIRST, before anything

   for each opposing battler i:

       if (gBattleMons[i].ability == ABILITY_SHADOW_TAG)
               → BATTLE_RUN_FAILURE
                 no condition at all. Anything. Everything.

       if (gBattleMons[gActiveBattler].ability != ABILITY_LEVITATE
        && !IS_BATTLER_OF_TYPE(gActiveBattler, TYPE_FLYING)
        && gBattleMons[i].ability == ABILITY_ARENA_TRAP)
               → BATTLE_RUN_FAILURE
                 TWO documented escapes, and one of them is an ability

   i = AbilityBattleEffects(..., ABILITY_MAGNET_PULL, ...);
   if (i != 0 && IS_BATTLER_OF_TYPE(gActiveBattler, TYPE_STEEL))
               → BATTLE_RUN_FAILURE
                 ONE type. Everything else walks away.
```

Three abilities doing the identical job — prevent the thing in front of you from leaving — with
three completely different spectra, and the spectrum is a condition in an `if` rather than a
strength.

**Shadow Tag** is the broad-spectrum antibacterial. You do not need to know what you are facing;
the check has no predicate on the target at all. It is carried by exactly two species,
**Wobbuffet** and **Wynaut**, which is the first thing worth noticing: the breadth of the agent
and the availability of the agent are independent facts, and the broadest one in the game is held
by a line of two.

**Arena Trap** — **Diglett**, **Dugtrio** and **Trapinch** — is the narrower agent with known
gaps, and the gaps are instructive. It fails against a Flying-type and it fails against Levitate:
a *type* and an *ability*, two different kinds of reason, tested separately because they are
separate things. So **Skarmory** escapes it by being Flying, and **Gengar**, **Weezing**,
**Claydol**, **Lunatone**, **Solrock**, **Duskull**, **Unown**, **Latias** and **Latios** all
escape it by holding **Levitate**, and no amount of knowing one of those routes tells you about
the other. An organism can be outside your spectrum for unrelated reasons, and the list of reasons
is not a single property.

**Magnet Pull** — **Magnemite**, **Magneton** and **Nosepass** — is the narrow antiviral. One
type, and nothing else, which means the ability is worthless unless you already know you are
facing **Magnemite**, **Magneton**, **Skarmory**, **Steelix**, **Scizor**, **Forretress**,
**Mawile**, **Aron**, **Lairon** or **Aggron**. The agent presupposes the diagnosis, and
that is not a limitation of the ability — it is what the ability *is*.

And then the detail that destroys the comfortable picture. **Skarmory** is Steel *and* Flying. It
**escapes Arena Trap**, the broader of the two conditional abilities, by being Flying — and it is
**held by Magnet Pull**, the narrowest ability in the game, by being Steel. Spectrum is not a
nesting hierarchy. A narrower agent can cover an organism a broader one misses, which is exactly
the situation with the agents in the technical half, and it is why "broad-spectrum" is a
description of a target list rather than a rank.

And `m007` is where the end of the ladder is argued properly: Ground into **Flygon** is ×0, not
×0.5, and no amount of anything crosses a zero. A target that is absent is categorically unlike a
target that is hard to reach. Note that **Flygon** gets there by **Levitate** while **Skarmory**
gets there by being Flying-typed, which are two different routes to the same multiplier — `m009`'s
ability-against-move asymmetry, in the one place where it decides whether a drug has a target at
all.

## Run Away is checked first, and it ends the battle

Look again at the top of that function. Before the engine asks about any trapping ability at all,
it asks whether the fleeing Pokémon has **Run Away** — and if it does, it returns success
immediately. The whole apparatus below never executes. Thirteen species carry it: **Rattata**,
**Raticate**, **Ponyta**, **Rapidash**, **Doduo**, **Dodrio**, **Eevee**, **Sentret**, **Furret**,
**Aipom**, **Dunsparce**, **Snubbull** and **Poochyena**. More species carry **Run Away** than
carry **Shadow Tag**, **Arena Trap** and **Magnet Pull** put together.

That is the self-limiting illness, and it is the hardest single problem in demonstrating that an
acute antiviral does anything. Most of these encounters end on their own, by a route that was
checked before any of your mechanisms were consulted. A trial that wants to show its agent made
the difference has to find the cases where `ABILITY_RUN_AWAY` was not present — which is exactly
`m146`'s point about enriching a trial population, with a specific cause.

## Fake Out: certain inside the window, and nothing outside it

```
   data/battle_scripts_1.s

   BattleScript_EffectFakeOut::
       attackcanceler
       jumpifnotfirstturn BattleScript_FailedFromAtkString
       setmoveeffect MOVE_EFFECT_FLINCH | MOVE_EFFECT_CERTAIN
       goto BattleScript_EffectHit

   and from battle_moves.h:
   [MOVE_FAKE_OUT] = power 40, accuracy 100, pp 10, priority 1,
                     target MOVE_TARGET_SELECTED
```

Two properties, and both of them are the antiviral timing argument.

The flinch is `MOVE_EFFECT_CERTAIN`. Not a chance — **certain**, inside the window. And the window
is one turn: `jumpifnotfirstturn` sends the whole script to `BattleScript_FailedFromAtkString`, so
on the second turn the move does not do less, it **fails outright**. Forty power and a priority of
1 on turn one; nothing at all on turn two.

That is a far better model of an acute antiviral than any dose-response curve, because it has the
right shape: the benefit is concentrated in a narrow early window, it is large inside that window,
and it is zero outside it. The clinical question for these agents is almost never *which one* — it
is *was it started in time*, and once the window has closed no increase in anything reopens it.
`m044`'s point about delivered dose applies in reverse: here the route and the amount are fine and
the **clock** is the binding constraint.

## Why a single mechanism loses to a large population: Thunder's 70

The games hand you the resistance arithmetic with a real accuracy figure.

```
   [MOVE_THUNDER] = power 120, accuracy  70     [MOVE_TOXIC] = accuracy 85
   [MOVE_SPORE]   = power   0, accuracy 100

   ONE mechanism, repeated. P(at least one failure in n attempts) = 1 - 0.70^n

      n = 1     0.30
      n = 2     0.51
      n = 3     0.66
      n = 5     0.83
      n = 10    0.97        ← the failure is not a risk any more. It is the
                              expected outcome of enough attempts.

   TWO mechanisms that must BOTH fail on the same attempt, Thunder and Toxic:
      0.30 × 0.15 = 0.045 per attempt
      P(at least one joint failure in 10) = 1 - (1 - 0.045)^10 ≈ 0.37

   THREE, with Spore's 100 in the mix:
      a mechanism that cannot fail on its own terms changes the product
      entirely -- which is why what you combine matters as much as how many.
```

A virus replicating in enormous numbers with an error-prone copying step is running the `n = 10`
column and then some. Against a single agent, a variant that defeats it is not a risk to be
managed; it is the arithmetic. Combination therapy is not caution — it is the only configuration
whose product is small, and the regimen has to be chosen so that one change cannot defeat all of
it at once.

Note what this arithmetic is **not**. It is recomputed here from Thunder's and Toxic's real
accuracy values in `battle_moves.h`, and it says nothing about any real mutation rate. `m010`'s
rule-of-three is the same shape of reasoning pointed the other way, at detection rather than at
escape.

## The egg: in the party, counted, and reached by nothing

```
   struct BattlePokemon
   0x17   isEgg:1            ← one bit, and it is carried INTO battle data:
                               gBattleMons[battler].isEgg = GetMonData(..., MON_DATA_IS_EGG)

   src/pokemon.c, RandomlyGivePartyPokerus
       do {
           rnd = Random() % PARTY_SIZE;
           mon = &party[rnd];
       } while (!GetMonData(mon, MON_DATA_SPECIES, 0)
              || GetMonData(mon, MON_DATA_IS_EGG, 0));
                             ← the thing that SPREADS re-rolls past every egg

   src/daycare.c, _GiveEggFromDaycare
       SetMonData(mon, MON_DATA_FRIENDSHIP, &gSpeciesInfo[species].eggCycles);
                             ← and the egg's countdown is stored in the
                               FRIENDSHIP field. One byte, two meanings,
                               selected by the isEgg bit.
```

An egg occupies a party slot. It is counted. It carries a bit into the battle structure. And it is
excluded from the mechanism that spreads through the party, by an explicit test in a do-while
loop. `m081` establishes the other half: `IsWildLevelAllowedByRepel` walks the party and stops at
the first member with HP **that is not an egg**, so the field instrument steps over it too.

That is a reservoir. Present, carried, counted in the total, read by nothing that matters, and
reached by neither the spreading process nor the instrument that measures. Treatment that clears
everything the instruments can see has not touched it, and a countdown is running in a byte that
for every other party member means something completely different.

Where the analogy stops, and it stops here rather than at the end of the answer: the egg's counter
runs down to a hatch, which is a scheduled event with a known endpoint. A latent viral reservoir
has no counter and no scheduled endpoint, which is exactly why suppression has to be continued
rather than completed. The game has the reservoir and does not have the indefiniteness, and that
is the more important half.

## What the field says about your own side

Back to the first block, because it has one more thing in it. `MOVE_TARGET_FOES_AND_ALLY` and
`MOVE_TARGET_BOTH` are both multi-target values; the difference between them is whether your own
side is in scope. Two further rows make the point that this is a **design decision per move** and
not a property of power or type:

```
   [MOVE_HEAL_BELL] =     target MOVE_TARGET_USER   (acts on your side only)
   [MOVE_AROMATHERAPY] =  target MOVE_TARGET_USER   (the same, Grass-typed)
   [MOVE_SPORE] =         target MOVE_TARGET_SELECTED
   [MOVE_SURF] =          target MOVE_TARGET_BOTH
   [MOVE_EARTHQUAKE] =    target MOVE_TARGET_FOES_AND_ALLY
```

Five rows, five scopes, one field. **Heal Bell** and **Aromatherapy** act on your own side and
nowhere else. **Spore** picks one target. **Surf** takes both opponents and spares your partner.
**Earthquake**, **Explosion** and **Self-Destruct** take everything adjacent including your own.
And **Toxic**, at 85 accuracy, picks one target and then does nothing at all to a Steel-type or a
Poison-type — a single-target agent with an intrinsic resistance problem written into the type
chart rather than into the move.

A drug class that cannot distinguish a fungal sterol from a host sterol is running the
**Earthquake** scope: it does what it does to whatever is adjacent, and the margin you have is
whatever difference exists between the two. A drug class aimed at peptidoglycan is running the
**Surf** scope: your own side is not a legal target, as a matter of structure. Nobody made
**Surf** more careful than **Earthquake**. The data row differs because the thing it describes
differs, and that is the whole of selective toxicity.

## Where the metaphor stops

The analogy above is about mechanism and spectrum. Three things about these infections are about
people, and the Pokémon framing is dropped for them.

**These infections concentrate in people who are already seriously unwell** — through treatment
that suppresses immunity, through advanced organ disease, through prematurity, through infection
that itself impairs immunity. So the narrow margins, the class interactions and the dose
adjustments all land in the people with the least physiological reserve and the longest medication
lists. Nothing in a battle format models that, and the attempt would require a creature to stand
in for the patient, which this corpus does not do.

**Delay is the dominant harm, and it is usually a pathway failure rather than a knowledge gap.**
The specimen that was not taken, the test sent at the wrong time, the imaging not requested, the
result that landed in a system nobody was watching. `m147` is the systems argument and it applies
here with the stakes raised: the fix is in the pathway.

**Access decides outcomes worldwide, and it is not distributed by need.** Many of these agents are
expensive, some need infusion and monitoring, and the binding constraint in much of the world is
diagnostic capacity rather than the drug — treatable infections go untreated for want of a test.
This is also where resistance and access meet: agricultural use of antifungal compounds related to
the medical ones is an established driver of environmental resistance, and the countries carrying
the resulting burden are generally not the ones making that decision. That is a description of a
structure, not a criticism of anyone's practice.

Nothing in this pair indicates what anyone should take, start or stop, and neither half names an
agent, a dose or a regimen. Suspected serious infection is an urgent clinical matter and not a
revision question.

## What a Gym Leader is listening for

* Surf and Earthquake. Which field differs, and what does that tell you about where selectivity
  lives?
* Put **Shadow Tag**, **Arena Trap** and **Magnet Pull** in order of spectrum and give the exact
  condition each one carries.
* Arena Trap has two escapes and they are different kinds of thing. Name both.
* Which check does `IsRunningFromBattleImpossible` perform *first*, and what clinical problem is
  that?
* What two things does `BattleScript_EffectFakeOut` establish about a treatment window?
* From Thunder's accuracy, compute the chance of at least one failure in ten attempts, and say
  what that is an argument for.
* The egg: name the three mechanisms that step over it, and the field its countdown is stored in.
* Where does the egg analogy break, and why is the broken half the important one?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **Your local antimicrobial guideline, including its antifungal and antiviral sections.** This is
  the authority for every choice, dose and duration both halves omit, and it is local because the
  organisms and their resistance patterns are local.
* **Your national formulary**, for the interactions, monitoring and organ-impairment adjustments
  of any specific agent. The antifungal interaction problem is not something to reason out from
  first principles when a monograph exists.
* **Your regional infection specialist service's guidance** and the relevant specialty society's
  guidelines on invasive fungal disease and on specific viral infections, for the diagnostic
  criteria both halves refer to without stating.
* **The world health organization's fungal priority pathogens list and its antimicrobial
  resistance reports**, for the resistance and access material.
* **A current medical microbiology or infectious diseases textbook chapter**, for the target
  structures, the drug classes and the distinction between intrinsic and acquired resistance.
* **The primary literature**, for any statement about effect sizes, treatment-window widths,
  resistance prevalence or mutation rates. Neither half of this pair states such a figure, and the
  arithmetic in the block above is computed from Pokémon accuracy values and is not a mutation
  rate.

The Pokémon figures are a different matter and were read directly from the public decompilation of
the Game Boy Advance games rather than recalled: the `power`, `accuracy` and `target` fields for
Surf, Earthquake, Self-Destruct, Explosion, Fake Out, Thunder, Toxic, Spore, Heal Bell and
Aromatherapy from `src/data/battle_moves.h`; `IsRunningFromBattleImpossible` in
`src/battle_main.c`, with the `ABILITY_RUN_AWAY` early return, the unconditional
`ABILITY_SHADOW_TAG` branch, the `ABILITY_ARENA_TRAP` branch's Levitate and Flying exclusions and
the `ABILITY_MAGNET_PULL` branch's `IS_BATTLER_OF_TYPE(TYPE_STEEL)` test, all in that order;
`BattleScript_EffectFakeOut` in `data/battle_scripts_1.s` with its `jumpifnotfirstturn` and its
`MOVE_EFFECT_FLINCH | MOVE_EFFECT_CERTAIN`; `isEgg` as a one-bit field at offset `0x17` of `struct
BattlePokemon` in `include/pokemon.h` and its assignment in `src/pokemon.c`;
`RandomlyGivePartyPokerus`'s do-while skipping eggs; and `_GiveEggFromDaycare` writing
`gSpeciesInfo[species].eggCycles` into `MON_DATA_FRIENDSHIP`. The holders of each ability were
found by filtering every `.abilities` field in `src/data/pokemon/species_info.h`: Shadow Tag is
Wobbuffet and Wynaut and nobody else, Arena Trap is Diglett, Dugtrio and Trapinch, Magnet Pull is
Magnemite, Magneton and Nosepass, Run Away is thirteen species, and Levitate is sixteen, including
Gengar, Weezing, Claydol, Lunatone, Solrock, Duskull, Unown, Latias and Latios. The typings quoted
for Skarmory, Magnemite, Magneton, Steelix, Scizor, Forretress, Mawile, Aron, Lairon and Aggron
are from the same file, and Skarmory's Steel-and-Flying pair is what produces the non-nesting
point. That a Poison-type move has no effect on a Steel-type, and that a Poison-type cannot be
poisoned, are type-chart and status facts of the Advance games rather than readings of any one
line quoted here. The Repel party walk is `m081`'s, verified there, and the ×0 against Flygon is
`m007`'s. The probability arithmetic above is recomputed from the quoted accuracy values.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones** — the
probabilities above are computed from move accuracy values and are not biological rates. Neither
half names an antiviral or antifungal agent, a dose, a duration, a therapeutic range or a regimen,
deliberately: those belong to the local antimicrobial guideline, the formulary and the infection
specialist, all of which are revised and all of which are local. Nothing here indicates what
anyone should take, start or stop, and suspected serious infection is an urgent clinical matter
rather than a revision question.

## Where this stands, October 2026

The structural argument — available difference determines available margin, and margin determines
spectrum, toxicity, resistance and the dependence on diagnosis — is mechanism and does not date,
and the game mechanics quoted are fixed in released software, pinned to the Game Boy Advance
games, where Fake Out has priority 1 and Thunder's accuracy is 70. Later generations changed
several of these values and added target scopes that do not exist here. The clinical half moves
fast. **New antifungal classes** with genuinely new targets have been in late-stage development
and would change the few-target-families claim if they reach practice. **Antifungal resistance**,
including intrinsically resistant species emerging in healthcare settings, is changing which
empirical choices are reasonable, and the agricultural driver is an active policy question.
**Antiviral development** moved faster in the last decade than in the three before it,
broad-acting agents against whole virus families are an active goal, and long-acting formulations
are changing the adherence picture. **Molecular diagnostics and resistance testing** are getting
faster, which moves the bottleneck. Check your local guideline and your national formulary.
