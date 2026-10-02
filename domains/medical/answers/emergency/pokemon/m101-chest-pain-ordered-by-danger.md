---
id: "m101"
slug: chest-pain-ordered-by-danger
style: pokemon
category: emergency
difficulty: advanced
question: "Why is the workup for chest pain ordered by danger rather than by likelihood, when a dozen unrelated mechanisms produce the same complaint?"
tags: [chest-pain, undifferentiated, prioritisation, differential, revision]
---

# Fifty-five scripts jump to the same five lines, and all fifty-five print "But it failed!"

Open `data/battle_scripts_1.s` and search for `BattleScript_ButItFailed`. It appears ninety-six
times: once as a label, and ninety-five times as a jump target. Those ninety-five jumps are
distributed across **fifty-five different script labels**, and the label they all land on is five
instructions long.

```
BattleScript_ButItFailed::
	pause B_WAIT_TIME_SHORT
	orbyte gMoveResultFlags, MOVE_RESULT_FAILED
	resultmessage
	waitmessage B_WAIT_TIME_LONG
	goto BattleScript_MoveEnd
```

One flag is set, one message is printed, the turn ends. Whatever brought you here is gone by the
second line.

## One string, fifty-five origins

The origins have nothing to do with each other. Every row below is read from the script file, and
each is a different kind of fact about a different part of the game state.

```
   what actually went wrong                                        where it is checked
   ──────────────────────────────────────────────────────────────────────────────────────────
   Parasect's Spore, 100 accuracy, into a target already burned    jumpifstatus STATUS1_ANY
   Snorlax's Belly Drum at level 15 with HP at or below half       maxattackhalvehp
   Focus Energy used twice in a row                                jumpifstatus2 FOCUS_ENERGY
   Snore chosen while the user is awake                            jumpifstatus STATUS1_SLEEP
   Teleport in a battle against another Trainer                    jumpifbattletype
   Attract aimed at Magnemite, Starmie or Shedinja — genderless,   tryinfatuating
     so the two genders compare equal
   Spite against a Pokémon with no PP left to take                 tryspiteppreduce
   Refresh with no burn, poison or paralysis to cure               cureifburnedparalyzed...
   Wish used while a Wish is already pending                       trywish
   Imprison where no move is shared with the other side            tryimprison
   Mimic, Sketch, Role Play, Skill Swap, Trick, Yawn, Taunt,       one guard each
     Torment, Encore, Disable, Mean Look, Perish Song, Memento,
     Helping Hand, Ingrain, Water Sport, Endeavor, Baton Pass …
   ──────────────────────────────────────────────────────────────────────────────────────────
     ONE observable: the string "But it failed!" and one bit in gMoveResultFlags.
     The string does not carry which row produced it. The rows live in different
     structs, are fixed by different things, and in several cases the counter to
     one is irrelevant to every other.
```

Gender, PP, HP, battle type, prior state, party legality, type, ability: eight unrelated
categories of cause, one sentence of output. A player who reads "But it failed!" and concludes
anything specific has over-read it, and the engine is not being coy — it genuinely does not
transmit the reason.

## The check that is read first is not the commonest one

`Cmd_resultmessage` in `src/battle_script_commands.c` decides which message to print, and its
shape is the whole point. `MOVE_RESULT_MISSED` is tested **before** the switch statement is
reached at all, so a miss outranks every other result regardless of what else is true. Inside the
switch the cases are read in a fixed written order, and in the compound branch at the bottom the
order is explicit: doesn't-affect first, then the one-hit KO, then `MOVE_RESULT_FOE_ENDURED`, then
`MOVE_RESULT_FOE_HUNG_ON` with its Focus Band script — and `MOVE_RESULT_FAILED` dead last.

Nothing about that order reflects how often each case happens. Plain failure is by far the most
common of them and it is checked last, because when several things are true at once the one worth
printing is the one that changes what the player does next. The ordering is a priority, written in
the source, exactly as `GetWhoStrikesFirst`'s bracket is in question m066 and as the priority byte
is in m031.

## Where the check is placed decides what you ever learn

Every script in the file opens with `attackcanceler`, and `accuracycheck` almost always comes
within the next three instructions — before `attackanimation`, before `damagecalc`, before any of
the expensive work. The cheap test that can redirect everything runs first. That is not an
aesthetic choice: a check placed after the animation would still be correct and would be useless,
because the thing it was meant to prevent has already happened.

Question m069 makes the same argument about where a refusal belongs. The ordering here is the
version with a clock on it.

## Several bits at once, and a switch that only matches one

`gMoveResultFlags` is a bitfield, eight bits wide, and more than one can be set in a single turn:

```
   MOVE_RESULT_MISSED             (1 << 0)
   MOVE_RESULT_SUPER_EFFECTIVE    (1 << 1)
   MOVE_RESULT_NOT_VERY_EFFECTIVE (1 << 2)
   MOVE_RESULT_DOESNT_AFFECT_FOE  (1 << 3)
   MOVE_RESULT_ONE_HIT_KO         (1 << 4)
   MOVE_RESULT_FAILED             (1 << 5)
   MOVE_RESULT_FOE_ENDURED        (1 << 6)
   MOVE_RESULT_FOE_HUNG_ON        (1 << 7)
```

The switch in `Cmd_resultmessage` is written over the masked value, so it matches **only when
exactly one bit is set**. The moment two are set the switch falls through to `default`, and the
fixed priority chain takes over. A single-cause match is the normal case and it is not the
dangerous case; the dangerous case is two true things at once, and what saves the engine there is
having written an order down in advance.

The header goes further and defines a composite:

```
   #define MOVE_RESULT_NO_EFFECT  (MOVE_RESULT_MISSED | MOVE_RESULT_DOESNT_AFFECT_FOE | MOVE_RESULT_FAILED)
```

Three mechanically unrelated outcomes — the roll went against you, there is no mechanism against
this target at all, and a guard clause refused — are folded into one name for the convenience of
whoever is reading it. The convenience is real and the collapse is lossy. The zero that question
m007 is built on — Earthquake into Flygon — is one of those three bits, and it is nothing at all
like the other two.

## The engine distinguishes where it can, and refuses where it cannot

It is not that the engine never separates causes. `gMissStringIds` in `src/battle_message.c` holds
five different strings for five different kinds of miss — the ordinary roll, Protect, evasion, a
damage-avoided case, and the Ground-type-makes-it-miss case. Five causes, five messages.

And `BattleScript_EffectSleep` shows both behaviours in one script, in nine lines:

* target already asleep → `BattleScript_AlreadyAsleep`, its own message;
* target cannot be made to sleep — an Uproar in progress, or Insomnia, or Vital Spirit →
  `BattleScript_CantMakeAsleep`, its own message, naming the ability;
* target has a Substitute up → the generic failure;
* target already has any other status at all → the generic failure.

Two causes get named; two get collapsed. Nothing about the second pair is less important than the
first pair — Substitute and an existing burn are completely different situations with completely
different answers — and the output simply does not distinguish them. Where a distinguishing
feature exists the engine prints it; where none exists it prints the generic string rather than
guessing, which is the honest behaviour and also the unhelpful one.

## It is written in the table rather than rediscovered

The jump table at the top of `battle_scripts_1.s` is one `.4byte` per move effect, in effect
order, and the shared failure label sits in the middle of the file with every script pointing at
it. Nobody re-derives the failure path per move; the order inside `Cmd_resultmessage` is one
written switch rather than fifty-five opinions. That is question m032's argument — Red and Blue
decided turn order with two if-statements and Emerald wrote it in a table — applied to the
reporting of a result rather than to the sorting of a turn.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is a person reporting a symptom.

Chest pain is one reported output with many unrelated generators: coronary supply-and-demand
mismatch or occlusion; an aortic wall splitting; obstruction of the pulmonary circulation;
inflammation of the pleura or air or fluid in the pleural space; pericardial inflammation or
restricted filling; oesophageal spasm, inflammation or a full-thickness tear; the chest wall
itself; referred pain from below the diaphragm; and presentations whose mechanism is not
structural at all. The complaint does not carry which. The generators differ in time-to-harm by
orders of magnitude and in treatment completely, and treatment for one of the major vascular
causes can worsen another — which is the argument against settling the question by pattern
recognition. **(Consensus** on the differential and on the harm of mistaking those two for each
other; the agents, thresholds and pathways are (**country-dependent**) and none is given
here.**)**

The workup is therefore ordered by a product: how likely this generator is here, how much harm
follows from missing it, and how much that harm is reduced by finding it now rather than later.
The third term is the one usually dropped, and it is the one that distinguishes "exclude the worst
first" from "assume the worst" — the first is the policy, the second is not. **(Mechanism**,
decision-theoretic and checkable by reasoning.**)** The first tests are the fast repeatable ones
whose result changes the next few minutes rather than the most discriminating ones available;
time-critical possibilities are pursued in parallel because the shortest clock binds; and where
the measured quantity changes over hours, a first result is not an exclusion. The generators are
not mutually exclusive, so finding a plausible benign cause establishes that it is present and not
that anything else is absent. **(Consensus.)**

No Pokémon stands for a patient anywhere in this answer, nothing in the game represents a person,
a symptom or an outcome, and no part of it is a sequence of actions. The game is carrying two
ideas and no others: that one output can have many unrelated generators which it does not
transmit, and that when two of them are true at once only a priority written down in advance
prevents the reasoning from collapsing onto the first match. What is at stake when the output
belongs to a person — the fear, the interval in which nobody can yet say, and the groups whose
presentations were long described as atypical and whose outcomes are worse for how that
description was applied — is stated here without ornament, and it is not a mechanic.

## What a Gym Leader is listening for

* Ninety-five jumps, fifty-five scripts, one message. What does the message establish?
* Name four of the failure causes and say which struct each lives in.
* Why is `MOVE_RESULT_MISSED` tested outside the switch, and why is `MOVE_RESULT_FAILED` checked
  last inside it?
* The switch only matches when exactly one bit is set. What happens when two are, and why is that
  the case worth writing an order for?
* `MOVE_RESULT_NO_EFFECT` folds three outcomes into one name. What is lost?
* Sleep names two of its four failure causes and collapses the other two. Why is that the honest
  behaviour rather than the lazy one?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* The current chest-pain assessment guidance issued by **the national body for clinical guidelines
  in the country the reader practises in**, for the pathway, the investigations in it and every
  threshold.
* The current acute coronary syndrome guidance issued by **the reader's national or regional
  cardiac society**, for definitions, for serial measurement and for the terminology now preferred
  over *typical* and *atypical*.
* A current standard textbook of **emergency medicine**, for the differential by mechanism and for
  what separates the major vascular causes from one another.
* **The reader's own employing organisation's** chest-pain pathway, which governs practice where
  they work and outranks every general account including this one.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all. Chest pain in particular is a presentation where delay is the harm.

This is revision material about *why an assessment is ordered the way it is*, written for someone
already trained, and the Pokémon framing covers the shape of the inference and nothing else. It is
deliberately not a protocol and not a decision aid: no test sequence, no risk score and no score's
criteria, no threshold, no interval, no agent, no dose, and nothing to consult while assessing
anyone. Chest-pain pathways differ between countries, regions and institutions and are revised.
The reader's own national guidance, society guidance and local pathway are the authority; this is
not, and it has had no clinical review. Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. The ninety-five jumps to one label across
fifty-five scripts, the five instructions at `BattleScript_ButItFailed`, the per-script guards
named above and the `BattleScript_EffectSleep` branch structure are read from
`data/battle_scripts_1.s`; `Cmd_resultmessage`'s miss-before-the-switch test, its exact-match
switch and the priority chain in its `default` branch from `src/battle_script_commands.c`, along
with `tryinfatuating`'s equal-genders comparison and `jumpifcantmakeasleep`'s Uproar, Insomnia and
Vital Spirit cases; the eight `MOVE_RESULT_` bits and the `MOVE_RESULT_NO_EFFECT` composite from
`include/constants/battle.h`; the five `gMissStringIds` entries from `src/battle_message.c`;
Spore's 100 accuracy from `src/data/battle_moves.h`; Snorlax learning Belly Drum at level 15 and
Parasect learning Spore at 27 from `src/data/pokemon/level_up_learnsets.h`; and Magnemite, Starmie
and Shedinja being `MON_GENDERLESS` from `src/data/pokemon/species_info.h`. Those are Generation
III behaviours and later generations change several of them, so a reader checking today's game
should read today's game. On the clinical side the structural argument is long-standing and the
specifics are not: which investigations sit in the first pass, how serial measurement is used,
which stratification tool is in force and the preferred vocabulary all differ by national body and
move with each revision. Principle dated October 2026; read the current pathway for anything past
the principle.
