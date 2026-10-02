---
id: "m007"
slug: pharmacodynamics-agonists-and-antagonists
style: pokemon
category: pharmacology
difficulty: advanced
question: "Distinguish agonist, partial agonist, antagonist and inverse agonist, and explain why a competitive antagonist shifts a dose-response curve while a non-competitive one flattens it."
tags: [pharmacodynamics, receptors, antagonism, efficacy, dose-response]
---

# Earthquake into Flygon is zero, and no amount of Earthquake changes that.

Two questions decide everything, and they are independent of each other. **Can the move touch this
target at all?** And **how much happens when it does?** The type chart answers the first, the
multiplier answers the second, and the four things a move can be are just the four interesting
combinations of those two answers.

The receptor is **the turn**. A Pokémon takes exactly one action, so whatever occupies the turn
has the site, and whatever does not occupy it gets nothing.

| Class | Can it take the turn? | What happens then | What it does to the battle |
| --- | --- | --- | --- |
| Full agonist | yes | the most available | **Swords Dance**, +2 stages, climbing toward the ceiling |
| Partial agonist | yes | less than the most | **Howl**, +1 stage — and it spent the turn **Swords Dance** wanted |
| Antagonist | yes | nothing at all | **Splash** under **Encore**: the turn is taken and nothing happens |
| Inverse agonist | yes | worse than nothing | **Growl**, −1 stage, which is *below* where you started |

Two of those rows need defending, because they are the two that get marked wrong.

**Howl is an antagonist whenever Swords Dance was available.** It takes the turn and returns less
than the turn was worth. Against a Pokémon sitting at stage 0 with nothing better to do, Howl is
an improvement. Against a Pokémon that could have used Swords Dance, Howl is a loss. Same move,
opposite sign, decided entirely by what else was on the table.

**Growl only means anything because stage 0 is not zero.** A Pokémon with no boosts and no drops
still attacks perfectly well — the site is doing something with nothing on it. That background is
what Growl takes away from, and it is why there is somewhere below baseline to go. And the games
are strict about the limit: at −6 Growl simply fails, because there is nothing left to reduce. If
the baseline were nothing, Growl and Encore-into-Splash would be the same move.

## The arithmetic

```
   ATTACK STAT STAGES -- the exact fractions the games store, not approximations

   stage        -6      -4      -2      -1       0      +1      +2      +4      +6
   stored     10/40   10/30   10/20   10/15   10/10   15/10   20/10   30/10   40/10
   multiplier  0.25    0.33    0.50    0.67    1.00    1.50    2.00    3.00    4.00
                                                ▲                               ▲
                                        baseline, nothing on            the ceiling,
                                        the site at all                 and it is hard

   COMPETITIVE -- Intimidate takes one stage on switch-in. Watch the ceiling.

                           starting at  0        starting at  -1  (Intimidate)
   after 1 Swords Dance        +2  = ×2.00           +1  = ×1.50
   after 2 Swords Dances       +4  = ×3.00           +3  = ×2.50
   after 3 Swords Dances       +6  = ×4.00 ◄ cap     +5  = ×3.50
   after 4 Swords Dances       +6  = ×4.00           +6  = ×4.00 ◄ SAME cap, one
                                                                   extra turn to reach

   NON-COMPETITIVE -- Reflect halves physical damage for five turns.

   stage                     0       +2       +4       +6
   without Reflect         ×1.00    ×2.00    ×3.00    ×4.00
   with Reflect            ×0.50    ×1.00    ×1.50    ×2.00  ◄ the cap is HALVED, and
                                                               +6 is the top of the
                                                               ladder, so no number of
                                                               Swords Dances recovers it
```

```
   damage, as a share of what the unopposed attacker would do

   100 ┤ unopposed                   ┌──────────────────  reaches the cap
       │                             │
       │ + Intimidate                            ┌──────  SAME cap, one more turn
       │                                         │
    50 ┤ + Reflect                   ┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌  cap at half, and no amount
       │                             │                    of Swords Dance gets past it
     0 ┼─────────────────────────────────────────────▶  turns spent setting up

         Intimidate : the whole ladder slides down one rung, top rung unchanged
         Reflect    : every rung is halved, including the top one
```

## Why those two shapes follow

**Intimidate** takes a stage. It does not remove the ladder. Every rung above you is still there,
so spending another turn on **Swords Dance** climbs past the loss, and the top rung is still
×4.00. The cost is turns, not ceiling. That is the whole of surmountability, and it is also why
Intimidate matters enormously against a Pokémon with no time to set up and barely at all against
one with four free turns.

**Reflect** does something different: it takes rungs out of the ladder rather than moving you down
it. The multiplier is applied after the stage multiplier, so halving survives everything you do
upstream of it, and **+6 is the top**. There is no rung above ×4.00 to climb to, so ×2.00 is
simply where the ceiling now is for the next five turns. A thing you cannot climb past is a
different animal from a thing you can, and it is why the fix for Reflect is not more setup but
**Brick Break**, which removes the screen, or waiting the five turns out.

And the games put one beautiful exception in: **Reflect does not apply to a critical hit.** A
ceiling with a hole in it is still a ceiling, but it tells you the halving was never a property of
the attacker.

**Overkill is the caveat that ruins most answers.** If a hit would do 400 to a Pokémon with 200 HP
left, Reflect halving it to 200 changes nothing you can see: the Pokémon still faints. Halve the
ceiling in a matchup with that much slack and the outcome is identical, so the flattening is
invisible until you run the margin thin. The same slack makes **Howl** look exactly as good as
**Swords Dance**. The clean pictures above are the no-slack case.

## No effect at all, and the limits of aiming

```
   TYPE EFFECTIVENESS -- applied on top of everything above

   Thunderbolt  →  Gyarados     Water ×2 × Flying ×2        =  ×4     everything lands
   Ice Beam     →  Dragonite    Dragon ×2 × Flying ×2       =  ×4     everything lands
   Flamethrower →  Blastoise    Water ×1/2                  =  ×0.5   something lands
   Thunderbolt  →  Venusaur     Grass ×1/2 × Poison ×1      =  ×0.5   something lands
   Earthquake   →  Gyarados     Flying ×0                   =  ×0     nothing, ever
   Thunderbolt  →  Dugtrio      Ground ×0                   =  ×0     nothing, ever
   Earthquake   →  Flygon       Levitate                    =  ×0     nothing, ever —
                                                                      and Flygon is a
                                                                      Ground-type itself
```

A ×0 is not a weak hit. It is the absence of a target, and it is the easiest thing in the games to
forget while staring at a damage calculation. **Shedinja** is the extreme: its ability **Wonder
Guard** means nothing but a super-effective hit does anything at all, so the overwhelming majority
of the move list is ×0 against it regardless of how hard it is thrown.

Aiming, though, is almost never absolute. **Earthquake** in a Double Battle hits both opponents
*and your own partner* — the games mark it as foes-and-ally and mean it. The move did not become
less accurate; you reached for something with more reach and it stopped distinguishing.
**Thunderbolt** makes the point on a timescale instead: a 10 % paralysis chance per use is clean
nineteen times out of twenty for one turn and not remotely clean across a career.

```
   chance Thunderbolt has paralysed nothing yet, after n uses  =  0.9 ⁿ

   n              1       3       7      15  (Thunderbolt's full PP)
   still clean   90 %    73 %    48 %    21 %
   so at least
   one paralysis 10 %    27 %    52 %    79 %
```

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. Here it stops.

The place this material is used most urgently is opioid overdose and its reversal, and the
consequences there are not abstract. A competitive antagonist with a shorter duration of action
than the agonist it is opposing can wear off while the agonist is still present, so someone who
has responded can deteriorate again — which is why reversal is never the end of an episode of
care. Giving a full antagonist to someone physically dependent on an opioid precipitates
withdrawal, and withdrawal is severe distress. The same is true of a partial agonist displacing a
full one. None of that is a ladder of multipliers, and describing it as one would be grotesque.

If anyone may have taken too much of any medicine or drug, contact emergency services immediately.
Nothing in this answer or its technical twin can be used to decide whether someone is safe, and
the decision about any medicine belongs with the prescriber or pharmacist who holds the record.

## What a Gym Leader is listening for

* The ladder slid down a rung but the top rung is unchanged. Intimidate, or a weaker attacker?
* Why does waiting out **Reflect** work when setting up more does not?
* Draw what **Howl** does to a Pokémon already holding **Swords Dance** boosts, and say why.
* How would 200 HP of overkill change your reading of both diagrams above?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* A standard pharmacology textbook for receptor theory, the occupancy equation and the Schild
  relationship that this answer's stat-stage ladder stands in for.
* The International Union of Basic and Clinical Pharmacology, through its guide to pharmacology
  database, for receptor nomenclature and for which ligands are currently classified as inverse
  agonists rather than antagonists.
* Your national formulary's monograph for any drug the technical twin of this answer names — in
  the United Kingdom the British National Formulary, published by NICE with the pharmaceutical
  press; elsewhere the equivalent national formulary.
* The summary of product characteristics, or the regulator-approved prescribing information, for
  the specific product, for any claim about its receptor selectivity.
* Your national guidance on opioid substitution and on opioid overdose management. This differs
  substantially between countries and no single document covers it.

The Pokémon figures are a different matter and were checked: the stat-stage fraction table,
Intimidate dropping one stage, Reflect halving physical damage for five turns in a single battle
and not applying to a critical hit, Brick Break removing screens, Encore lasting three to six
turns, Earthquake targeting foes and ally, Thunderbolt's ten per cent secondary chance and fifteen
PP, the zero-effect entries of the type chart, Flygon's Levitate and Shedinja's Wonder Guard all
come from the public decompilation of the Game Boy Advance games, read directly.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in it are the Pokémon ones.** Its technical twin
contains no doses and no targets, only arithmetic on defined quantities. Drug classification
moves, selectivity claims are relative, and clinical use differs between countries and
formularies. Nothing here should be used to make a decision about anyone's treatment, including
your own. Anyone with a question about a medicine they are taking should raise it with their own
prescriber or pharmacist, and in a suspected overdose of any kind the right action is to contact
emergency services immediately. A battle has a reset button. Nothing outside the game does.

## Where this stands, October 2026

Receptor theory is stable and the equations behind this answer have not changed in decades. The
game mechanics cited are fixed in released software, though the series has changed some between
generations — Surf, for instance, does not hit your partner in the Game Boy Advance games and does
in later ones — and this answer names the version it is describing. What moves is drug
classification and everything about clinical use. Check the current formulary.
