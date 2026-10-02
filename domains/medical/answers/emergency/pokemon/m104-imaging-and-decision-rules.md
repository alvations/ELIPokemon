---
id: "m104"
slug: imaging-and-decision-rules
style: pokemon
category: emergency
difficulty: advanced
question: "Why is imaging a test with a harm of its own, and what is a clinical decision rule actually for?"
tags: [imaging, decision-rules, harm, over-testing, revision]
---

# Take Down charges you only when it lands. Hi Jump Kick charges you precisely when it does not.

Emerald has two classes of recoil move and the difference between them is the whole subject.

`EFFECT_RECOIL` bills a fraction of the damage **actually dealt**. Take Down is 90 base power, 85
accuracy, 20 PP, and `MOVE_EFFECT_RECOIL_25` computes `gHpDealt / 4`; Submission is 80 power at 80
accuracy with the same effect; Double-Edge is 120 power at 100 accuracy and
`MOVE_EFFECT_RECOIL_33` computes `gHpDealt / 3`. Miss, and `gHpDealt` is zero, and you pay
nothing.

`EFFECT_RECOIL_IF_MISS` is the other shape, and Hitmonlee carries both of its members — Jump Kick
at level 16, 70 power and 95 accuracy, and Hi Jump Kick at 26, 85 power and 90 accuracy. Read
`BattleScript_EffectRecoilIfMiss`:

```
BattleScript_EffectRecoilIfMiss::
	attackcanceler
	accuracycheck BattleScript_MoveMissedDoDamage, ACC_CURR_MOVE
	goto BattleScript_HitFromAtkString
BattleScript_MoveMissedDoDamage::
	attackstring
	ppreduce
	resultmessage
	jumpifbyte CMP_COMMON_BITS, gMoveResultFlags, MOVE_RESULT_DOESNT_AFFECT_FOE, BattleScript_MoveEnd
	printstring STRINGID_PKMNCRASHED
	damagecalc
	typecalc
	adjustnormaldamage
	manipulatedamage DMG_RECOIL_FROM_MISS
	healthbarupdate BS_ATTACKER
	datahpupdate BS_ATTACKER
```

On a miss the engine computes the damage the move *would* have done, halves it —
`DMG_RECOIL_FROM_MISS` is `gBattleMoveDamage /= 2`, floored at 1 and capped at half the target's
maximum HP — and takes it off the user. The cost arrives exactly in the case where no information
was obtained.

## The cost that is paid for nothing, and the one case that is exempt

```
   Take Down, Submission, Double-Edge        Jump Kick, Hi Jump Kick
   ─────────────────────────────────────────────────────────────────────────────────────
   hit   → damage dealt, recoil = a          hit   → damage dealt, no recoil at all
           quarter or a third of it
   miss  → nothing happens, nothing paid     miss  → STRINGID_PKMNCRASHED, and half the
                                                     damage it would have dealt comes
                                                     off the user
   ─────────────────────────────────────────────────────────────────────────────────────
     ONE exception, written into the script: if the result carries
     MOVE_RESULT_DOESNT_AFFECT_FOE the script jumps straight to MoveEnd and no
     crash damage is applied. The only free failure is the one where the move
     could never have done anything to that target in the first place.
```

That exception is worth stopping on. A Hi Jump Kick aimed at Gengar is a question with no possible
answer — Fighting into Ghost is question m007's zero, not a small number — and the engine charges
nothing for it. Every other failure is billed. A player who treats the printed 90 accuracy as the
whole cost of the move has read the power and the accuracy and missed the branch underneath them.

There is one more asymmetry and it is the sharpest fact in the answer.
`BattleScript_MoveEffectRecoil` opens with two jumps:

```
	jumpifmove MOVE_STRUGGLE, BattleScript_DoRecoil
	jumpifability BS_ATTACKER, ABILITY_ROCK_HEAD, BattleScript_RecoilEnd
```

**Rock Head** cancels the recoil from a hit entirely — Onix has it as its first ability and learns
Double-Edge at level 57; Rhyhorn has it as its second and learns Take Down at 43; Aron and Aggron
carry it too. And `Rock Head` is checked **nowhere** in the crash branch. The ability that exempts
you from the cost of succeeding does not exempt you from the cost of failing, and `MOVE_STRUGGLE`
is tested before the ability so that Struggle's recoil is never waived at all.

The benefit of the move is conditional on hitting. One of its two costs is not. That is the entire
structure, and it is question m008's therapeutic index with the fraction moved to the other
branch: there the printed ratio was not the margin, here the printed accuracy is not the price.

## What a rule is for: Repel is one input and one comparison

`IsWildLevelAllowedByRepel` in `src/wild_encounter.c` is nine lines of logic and is the best
illustration in the game of what a written rule does.

```
   if (!VarGet(VAR_REPEL_STEP_COUNT))        -> return TRUE          (not in force: allow)
   for each party slot, in order:
       if it has HP and is not an egg:
           return (wildLevel < ourLevel) ? FALSE : TRUE              (decide on the first one)
   return FALSE
```

Notice what it is and is not. It is **deterministic**: the same inputs give the same answer every
time, and anybody can check it afterwards. It is **crude on purpose**: it reads one level, from
one party slot, and nothing else — not the species, not the type, not whether that encounter was
rare or wanted, not how many steps you have taken. And its purpose is not to find encounters. Its
purpose is to make **skipping** them cheap, repeatable and not a judgement call, which is exactly
what a decision rule in a department is for.

It also decides on the **first** slot with HP that is not an egg and returns immediately. The
threshold is therefore whatever that Pokémon's level happens to be, chosen for reasons that have
nothing to do with the rule.

Two further details, both in the data rather than in the prose. The three strengths of the item
differ only in **how long the rule is in force** and not at all in what it tests:
`holdEffectParam` is 100 for a Repel, 200 for a Super Repel and 250 for a Max Repel, and all three
call the same `ItemUseOutOfBattle_Repel`, which writes that number into `VAR_REPEL_STEP_COUNT`.
And it cannot be topped up early: with the counter non-zero the use is refused with "the Repel's
effects lingered", which is exactly the non-refreshable setter question m103 reads in
`Cmd_setsafeguard`. A rule has a window, the window is a count, and the count is the only thing
the three versions disagree about.

## Three shapes of restraint, and they are not interchangeable

| | How it decides | Same answer twice? | Checkable afterwards? |
| --- | --- | --- | --- |
| **Repel** — `IsWildLevelAllowedByRepel` | one comparison against one level | yes | yes, it is in the source |
| **Keen Eye or Intimidate** — `IsAbilityAllowingEncounter` | slot one only; needs level above 5; blocks when the wild level is at or below yours minus 5; **and then only on `!(Random() % 2)`** | no | no |
| **Cleanse Tag, White Flute, Black Flute** | the rate itself: × 2/3 for a Cleanse Tag held in slot one, up 50% for the White Flute, down 50% for the Black | yes | yes |

Three mechanisms, all of which reduce the number of encounters, and only the first is a rule. The
Keen Eye path is a coin flip on top of a comparison — Skarmory has Keen Eye from its species data
and Tauros has Intimidate — and no amount of observing it tells you what it will do next. The
flute and the Cleanse Tag never decide anything at all: they move the rate, and the player makes
no decisions differently. The Flutes are also mutually exclusive by construction, since
`ItemUseOutOfBattle_BlackWhiteFlute` clears the other flag whenever it sets one.

## How the rule fails

Four failures, all mechanical.

* **It is not in force.** With the step counter at zero the function returns TRUE on the first
  line. A rule that is not running is not restraining anything, and nothing about the screen says
  which state you are in.
* **It is bypassed entirely by the unfiltered path.** `SweetScentWildEncounter` calls
  `TryGenerateWildMon(..., 0)` — `flags = 0`, where an ordinary step passes
  `WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE`. Sweet Scent asks the open question, and the open
  question returns precisely what your filters would have suppressed. Question m048 is built on
  that line.
* **Its input was chosen for other reasons.** The comparison is against the first healthy party
  slot, so swapping your lead changes the rule's output without changing the rule.
* **It only covers what it was written to cover.** The level comparison says nothing about the
  encounter you actually did not want, and a rule's silence is not a verdict.

## It is still a good move

None of this is an argument against Hi Jump Kick. 85 base power at 90 accuracy on a Pokémon that
learns it at 26 is a strong option, and the comparison that matters is against the alternative in
the other three slots — question m014's budget — and not against doing nothing. The crash branch
is a reason to know what the move costs on a miss, which is a different thing from a reason not to
use it. A move that is decisive when it lands can be worth a cost that is paid when it does not;
the judgement is a trade between options, and a player who refuses every move with a downside has
four empty slots.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is a test performed on a person.

An imaging test is an act with effects of its own, and its costs are largely unconditional while
its benefit is conditional on the result changing what happens next. **(Mechanism.)** The costs
are four: ionising radiation where the modality uses it, which carries a dose-related stochastic
risk that accumulates over a lifetime and weighs more heavily the younger the person is; the time
to the result, during which the decision it was meant to inform has not been made; the capacity
consumed, which is the next person's access to the same resource; and findings unrelated to the
question asked, each capable of generating its own investigations and its own label.
**(Consensus** on the radiation risk being dose-related and on incidental findings being common
and generating their own harms; every figure, dose reference level and national framework is
**country-dependent** and none is given here.**)** It follows that a test with a low probability
of changing management is net harm even when it feels harmless, and that the right comparison is
the test against its alternative rather than against nothing.

A clinical decision rule in this setting mostly exists to make **not** testing defensible,
reproducible and auditable. That objective explains its design: it is tuned asymmetrically, to
miss as close to nothing as its derivation allows, and it pays for that with many people who
satisfy it and have nothing — so criticising such a rule for low specificity mistakes its purpose.
It returns a category rather than a probability, which is what makes it reproducible and
auditable. It is valid only in the population that validated it, and use outside that population
is the commonest misuse. **(Consensus.)** No rule is named or reproduced here, deliberately: a
rule used from memory is one of the known ways they fail, and the reader's own institution holds
the exact wording of the ones in force.

No Pokémon stands for a patient anywhere in this answer, nothing in the game represents a person,
a test, a dose or an outcome, and no part of it is a sequence of actions. The game is carrying two
ideas: that an act can charge you most precisely when it tells you nothing, and that a written
rule exists to make an omission reproducible rather than to find anything. What is at stake when
the test belongs to a person — that a decision not to image is a positive decision and is
experienced completely differently when it is explained, that reassurance is a real but unreliable
benefit, and that an incidental finding can convert someone who was well into someone with a
surveillance schedule while nobody who made the original decision ever learns of it — is stated
here without ornament, and it is not a mechanic.

## What a Gym Leader is listening for

* Take Down and Hi Jump Kick both carry recoil. In which case does each one charge you?
* `DMG_RECOIL_FROM_MISS` halves something and caps it. Halves what, and caps it at what?
* One failure is exempt from crash damage. Which, and why is that the interesting one?
* Rock Head waives one of the two costs and not the other. Which, and what is the general lesson?
* `IsWildLevelAllowedByRepel` reads one number from one slot. Name three things it deliberately
  ignores, and say what its job actually is.
* Which of Repel, Keen Eye and the Cleanse Tag is a rule, and what are the other two?
* Sweet Scent passes `flags = 0`. What does the open question return?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* The current imaging referral guidance issued by **the national radiology body or college for the
  country the reader practises in**, for which test answers which question and for the
  justification framework.
* The current radiation protection framework issued by **the reader's national radiation
  protection authority or regulator**, for justification, optimisation, dose reference levels and
  the duties attached to requesting an exposure. In many countries this is a legal instrument and
  the obligations are not interchangeable between them.
* **The reader's own institution's** list of decision rules in force, with their exact wording and
  the populations they apply to — the authority on every criterion, and the reason none is
  reproduced here.
* A current standard textbook of **emergency medicine**, for the derivation-and-validation logic
  of decision rules and for the incidental-findings literature.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *the structure of a testing decision*, written for someone already
trained, and the Pokémon framing covers that structure and nothing else. It is deliberately not a
protocol and not a decision aid: it names no decision rule, reproduces no criteria, and states no
threshold, dose, dose reference level, modality recommendation or interval, and it is not
something to consult while deciding anything about anyone. Imaging referral guidance, radiation
protection law and the set of rules in force differ between countries, regulators and institutions
and are revised. The reader's own national body, regulator and local policy are the authority;
this is not, and it has had no clinical review. Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. Take Down at 90 power and 85 accuracy with
20 PP, Submission at 80 and 80, Double-Edge at 120 and 100, Jump Kick at 70 and 95 and Hi Jump
Kick at 85 and 90, and their `EFFECT_RECOIL`, `EFFECT_DOUBLE_EDGE` and `EFFECT_RECOIL_IF_MISS`
entries are read from `src/data/battle_moves.h`; the quarter and third computed from `gHpDealt`,
and `DMG_RECOIL_FROM_MISS` halving the would-be damage with a floor of 1 and a cap at half the
target's maximum HP, from `src/battle_script_commands.c`; the crash script with its
`MOVE_RESULT_DOESNT_AFFECT_FOE` escape from `data/battle_scripts_1.s`;
`IsWildLevelAllowedByRepel`, `IsAbilityAllowingEncounter` with its level-above-5 condition, its
minus-5 comparison and its `!(Random() % 2)`, `ApplyCleanseTagEncounterRateMod`'s two thirds,
`ApplyFluteEncounterRateMod`'s fifty per cent each way, and `SweetScentWildEncounter`'s `flags =
0` against an ordinary step's `WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE` from
`src/wild_encounter.c`; the White Flute setting the up-flag and clearing the down-flag from
`src/item_use.c`; Hitmonlee's Jump Kick at 16 and Hi Jump Kick at 26 from
`src/data/pokemon/level_up_learnsets.h`; and Skarmory's Keen Eye and Tauros's Intimidate from
`src/data/pokemon/species_info.h`. Those are Generation III behaviours and later generations
change several of them, so a reader checking today's game should read today's game. On the
clinical side the structural argument is long-standing and the specifics are not: which rules are
in force, their criteria, imaging referral guidance, dose reference levels and the legal duties
attached to an exposure all differ by country and institution and move with each revision, and the
incidental-findings literature is active. Principle dated October 2026; read the current guidance
for anything past the principle.
