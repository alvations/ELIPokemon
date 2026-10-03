---
id: "m126"
slug: the-soft-abdomen-and-serial-examination
style: pokemon
category: emergency
difficulty: intermediate
question: "Why is a soft abdomen weak evidence, and why is the abdominal examination repeated rather than recorded once?"
tags: [abdomen, examination, serial, evidence, revision]
---

# Yawn writes the state into `gStatuses3`, and `gStatuses3` has no graphic

`Cmd_setyawn` is four lines long and the interesting thing about it is which array it writes to:

```
   if (gStatuses3[gBattlerTarget] & STATUS3_YAWN
       || gBattleMons[gBattlerTarget].status1 & STATUS1_ANY)
       -> jump to the failure branch
   else
       gStatuses3[gBattlerTarget] |= STATUS3_YAWN_TURN(2);
```

`STATUS3_YAWN` is bits 11 and 12 of `gStatuses3`, a two-bit counter holding the number of turns to
go. Nothing is written into `status1`. Nothing is written into `status2`. And
`UpdateStatusIconInHealthbox` reads `MON_DATA_STATUS` — that is `status1` and nothing else — then
tests five bits in a fixed order, Sleep, then any Poison, then Burn, then Freeze, then Paralysis,
and draws the matching graphic. Anything that is not one of those five falls through to the blank
tile and the function returns.

So a Pokémon that is two turns from being asleep, by a mechanism that has already fired and is
already counting, looks on screen exactly like one that is perfectly well. Not *similar*. Byte for
byte, in the only structure the healthbox consults, identical.

## The blank tile is not a negative result, and the engine never claimed it was

This is worth stating as code because it is the whole error in one line.
`UpdateStatusIconInHealthbox` ends its else-branch with `statusGfxPtr =
GetHealthboxElementGfxPtr(HEALTHBOX_GFX_39)` — the empty tile — copies it in, adds the ball icon
and returns. It did not look at `gStatuses3`. It did not look at `statStages`. It did not look at
`gSideStatuses`. The blank means *none of five bits in one field*, and a player who reads it as
*nothing is wrong* has added a claim the function never made.

And the precedence makes it worse rather than better. Sleep is tested first, so a Pokémon that is
both asleep and badly poisoned shows SLP and only SLP. The single slot is filled by whichever bit
comes first in a chain whose order has nothing to do with which condition matters more. Question
m102 counts the same shape from the other end: nine end-of-turn HP sinks held in five stores, five
graphics, four of the nine invisible.

## The state and the consequence are determined at two different times

Here is the part that makes Yawn the right mechanic for a repeated examination rather than for a
hidden one.

`ENDTURN_YAWN` runs once per battler per turn. It decrements the two-bit counter, and **only when
the counter reaches zero** does it do the real work:

```
   gStatuses3[battler] -= STATUS3_YAWN_TURN(1);
   if (counter now zero
       && !(status1 & STATUS1_ANY)
       && ability != ABILITY_VITAL_SPIRIT
       && ability != ABILITY_INSOMNIA
       && !UproarWakeUpCheck(battler))
   {
       CancelMultiTurnMoves(battler);
       status1 |= STATUS1_SLEEP_TURN((Random() & 3) + 2);   // two to five turns
   }
```

Three facts, each load-bearing.

**The duration is drawn at resolution, not at setting.** `(Random() & 3) + 2` is evaluated when
the counter hits zero. At the moment Yawn was used, the length of the eventual sleep *did not
exist anywhere in memory*. No examination of any structure at that moment could have found it,
because it had not been rolled. Contrast `Cmd_trysetfutureattack`, which question m068 reads for
the opposite property: Future Sight computes the whole consequence at the instant of use and
stores it, so a reading taken then is a reading of the outcome. Yawn and Future Sight are the two
halves of the point. Some consequences are already in the file and merely hidden; some have not
been computed yet, and there is nothing to find.

**Four conditions are re-tested at resolution that were also tested at setting, and one is not.**
Insomnia, Vital Spirit, an Uproar and any `status1` are checked in both places. **Safeguard is
checked only at setting** — `jumpifsideaffecting BS_TARGET, SIDE_STATUS_SAFEGUARD` sits in
`BattleScript_EffectYawn` and appears nowhere in `ENDTURN_YAWN`. So a Safeguard raised after the
Yawn landed does not stop the sleep, and a Safeguard raised before it prevents the Yawn entirely.
Same protection, same target, opposite results, and the only difference is *when the check runs*.
Question m103 reads the Safeguard check site for prevention; this is the same site read for
timing.

**A set that succeeded can still resolve into nothing.** If the target acquires any `status1` from
any source during those two turns, the counter runs down and the branch does not fire. The state
was real, the counter was real, and the outcome is absent.

## The failure branch is one string with six roads into it

`BattleScript_EffectYawn` is seven instructions of gatekeeping before anything is written:

```
   attackcanceler
   attackstring
   ppreduce
   jumpifability  BS_TARGET, ABILITY_VITAL_SPIRIT -> BattleScript_PrintBankAbilityMadeIneffective
   jumpifability  BS_TARGET, ABILITY_INSOMNIA     -> BattleScript_PrintBankAbilityMadeIneffective
   jumpifstatus2  BS_TARGET, STATUS2_SUBSTITUTE   -> BattleScript_ButItFailed
   jumpifsideaffecting BS_TARGET, SAFEGUARD       -> BattleScript_SafeguardProtected
   accuracycheck  BattleScript_ButItFailed, NO_ACC_CALC_CHECK_LOCK_ON
   jumpifcantmakeasleep BattleScript_ButItFailed
   setyawn        BattleScript_ButItFailed
```

Six distinct ways to end up with no Yawn, and they print **three** strings between them. Vital
Spirit and Insomnia get their own message. Safeguard gets its own. And a Substitute, a missed
accuracy roll, an Uproar in progress, an already-present status and an already-present Yawn all
land on `BattleScript_ButItFailed` — one string, five unrelated causes. That is question m101's
`BattleScript_ButItFailed` device exactly, met here in a different move: the readout cannot tell
you which of five things happened, and three of the five are facts about *the attempt* rather than
about the target.

Yawn's own data entry is worth reading beside that. Power 0, Normal type, **accuracy 100**, 10 PP,
`FLAG_PROTECT_AFFECTED | FLAG_MAGIC_COAT_AFFECTED | FLAG_MIRROR_MOVE_AFFECTED`. Accuracy 100 is
not accuracy 0: Haze and Psych Up carry `.accuracy = 0`, which the engine reads as *skip the
check*, and Yawn does not. So Yawn runs the full accuracy calculation against the target's evasion
stage and can simply miss — a nil result produced entirely by the conditions of the examination
and not at all by what is there.

## Looking again is reading the same address at a later time

Nothing about Yawn is hidden in the sense of encrypted. `gStatuses3[battler]` is a plain `u32` and
the two bits are right there. What makes the state unreadable is that the **display** does not
consult that array, and what makes a second look informative is that the array's contents **change
between looks without anybody doing anything**.

That is the difference between a hidden variable and a moving one, and it is the difference
between a better test and a second test. A better test would be a healthbox that drew
`gStatuses3`. A second test is reading the same `u32` after `ENDTURN_YAWN` has run once. Only one
of those two is available to a player, and it is the one that requires a turn to pass.

Pin the pair down with real entries. Slowpoke and Slowbro have Yawn at level 1, Slowking too;
Gulpin learns it at 6, Dunsparce at 11, Togepi at 16, Relicanth at 22, Snorlax at 24, Chimecho at
25, Wooper at 31, Quagsire at 35, and Slakoth and Slaking have it from level 1. Any of those can
put a two-turn counter into an array the screen does not read, and the only way the other player
finds out is `STRINGID_PKMNWASMADEDROWSY` printed once at the time, or a turn going past.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is somebody with abdominal pain.

A line in a record reading *abdomen soft, non-tender* is routinely read as *there is nothing
surgical here*, and it does not say that. (**Definitional** — this is about what the finding
denotes, before any argument about how good it is.)

Palpation reports at least four tests in one phrase: voluntary guarding, which is about the
examination rather than the abdomen; involuntary guarding or rigidity, which is a reflex arc
requiring irritation of the parietal peritoneum and an intact arc to produce it; tenderness, which
is a reported experience elicited by the examiner; and a mass or distension, which requires a
structure large enough and superficially enough placed for a hand to reach it. Because involuntary
guarding is downstream of a process reaching one specific surface, a soft abdomen is consistent
with nothing happening, with something happening that has not yet reached that surface, and with
something well established in a person whose arc cannot produce the sign. (**Mechanism.**) The
record does not distinguish those three and they have nothing in common clinically.

The negative is weak in four separable ways. It declares late, because the hand finds the
peritoneal phase and not the visceral one. (**Mechanism.**) The arc is blunted in identifiable
groups — older age, immunosuppression including corticosteroids, diabetes, spinal cord injury,
recent abdominal surgery, substantial abdominal wall adiposity, pregnancy displacing the viscera,
and sedating or analgesic medication — and in several of those the systemic signs are blunted at
the same time, so two independent readouts fail together. (**Consensus.**) It is anatomically
selective, since retroperitoneal, pelvic and sub-diaphragmatic processes may never irritate a
surface the hand can load, making *soft* a true statement about the abdominal wall and a false one
about the abdomen. (**Mechanism.**) And agreement between examiners on abdominal signs is
imperfect and is worst for the borderline findings that change a decision; the published agreement
statistics vary by setting and by sign and none is quoted here. (**Consensus.**) The mirror-image
error matters too: a rigid abdomen is not specific either, since pain arising outside the abdomen,
a basal chest process, conditions causing abdominal pain without peritoneal inflammation, and
simple frightened tensing all produce it.

What the second examination adds is a direction, which is a different variable with different
content: a resolving process and an advancing one can give identical single examinations and
opposite pairs. (**Mechanism.**) Three things follow. The second examination's information is
destroyed unless the first was recorded comparably — where the hand went, what was found, what was
specifically absent, and **when**, because the time is the denominator of the change rather than
administrative metadata. The interval has to be chosen from the time constant of the process under
consideration rather than from the rhythm of the department. And somebody has to be named as
responsible for the next look, which is the component that fails when the department is busy.
(**Consensus** that explicit timing and explicit responsibility are what make reassessment work;
the local mechanism for recording them is (**country-dependent**).)

The examination sits among other inputs with different time constants — the history, the
observations, the laboratory tests that lag the process, and imaging, which is a snapshot taken at
a cost of its own. A normal result from a slow input early in a fast process is uninformative
rather than reassuring, which is the same structural point again. (**Mechanism.**) No clinical
decision rule is named anywhere in this answer, and no score, threshold, reassessment interval or
imaging pathway appears, because each is local and revised and because a rule used from memory is
one of the failure modes the subject is about.

What is at stake for a person is not in the mechanics. Somebody with abdominal pain is frightened,
often more than they say, and the examination is an intrusion by a stranger. The reassuring
sentence is heard and acted on, so a plan to look again has to be said out loud alongside it,
including what would make returning urgent — question m012's argument about what separates a
safety-net that works from reassurance that only sounds like one. Tensing is usually the
expectation of being hurt rather than obstruction, which makes a gentle, explained, unhurried
examination an instrument and not a courtesy. And the account of the change belongs to the person
and to whoever is with them: *it was not like this this morning* is primary data, it is often not
asked for, and it carries a trajectory no single examination can.

No Pokémon stands for a patient anywhere in this answer, and that shaped it. No Pokémon is unwell,
nothing is examined by anybody, and no creature's state represents a person's. The game is
carrying three ideas and no others: that a state can live in a structure the display does not
consult, so a blank readout is a statement about one field and not about the subject; that some
consequences have not yet been computed at the moment you look, so there is nothing to find rather
than something hidden; and that a check performed at one time and the same check performed later
are different questions, because what they test moves in between. Pain, fear and the intrusion of
being examined are stated above without ornament and are not mechanics.

## What a Gym Leader is listening for

* Which array does `Cmd_setyawn` write to, and which array does the healthbox read?
* `UpdateStatusIconInHealthbox` draws a blank tile. State precisely what that blank asserts.
* The icon chain tests five bits in a fixed order. What does that do to a Pokémon with two
  conditions?
* When is the length of the eventual sleep decided? Contrast Future Sight.
* Safeguard is checked in one of the two places. Which, and what follows for a Safeguard raised a
  turn late?
* Give five routes into `BattleScript_ButItFailed` from the Yawn script, and say which of them are
  facts about the attempt rather than the target.
* Yawn has accuracy 100 and Haze has accuracy 0. What does the engine do differently with those
  two numbers?
* What is the difference between a hidden variable and a moving one, and which of the two does a
  second look address?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* A current standard textbook of **emergency medicine** and one of **general surgery**, for the
  physiology of the peritoneal reflex, the anatomical reasons some processes are impalpable, and
  the evidence on inter-observer agreement in abdominal signs.
* The current standards for assessment and reassessment in the emergency department issued by
  **the reader's national emergency medicine college**, which is where the expectation for
  documented reassessment sits and which differs between countries.
* **The reader's own employing organisation's** policy on reassessment intervals, on who is
  responsible for a repeat examination, and on the local imaging and referral pathway for
  abdominal pain.
* **The primary literature**, for the diagnostic performance of individual abdominal signs. No
  sensitivity, specificity or agreement statistic is quoted here.

Markers used in the plain-prose section above: (**mechanism**) (follows from anatomy, physiology
or the structure of the problem and is checkable by reasoning), (**definitional**) (about what a
term denotes), (**consensus**) (agreed across mainstream sources as of writing),
(**country-dependent**) (genuinely differs between countries, services or institutions). No
guideline number, document title, score, threshold or interval is given, and nothing is quoted,
because none of these was opened. The Pokémon side is in the opposite position and is sourced file
by file in the closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *what a physical finding does and does not establish*, written for
someone already trained, and the Pokémon framing covers only where a state is stored, when a
consequence is computed, and what a check performed at one time does not establish about a later
one. It is deliberately not a protocol and not a decision aid: it names no clinical decision rule,
no score, no threshold, no reassessment interval and no imaging pathway, and it is not something
to consult while assessing anyone. No diagnostic performance figure appears, because those are
setting-dependent and no source was opened. Reassessment standards, imaging availability and
referral criteria differ sharply between countries and institutions. The reader's own national
guidance and local policy are the authority; this is not, and it has had no clinical review.
Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. `Cmd_setyawn` failing on an existing Yawn
or any `STATUS1_ANY` and otherwise writing `STATUS3_YAWN_TURN(2)`; `STATUS3_YAWN` occupying bits
11 and 12 of `gStatuses3`; `ENDTURN_YAWN` decrementing that counter and, at zero, applying
`STATUS1_SLEEP_TURN((Random() & 3) + 2)` behind checks on `STATUS1_ANY`, Vital Spirit, Insomnia
and `UproarWakeUpCheck` with no Safeguard test; and the ten-instruction `BattleScript_EffectYawn`
with its Safeguard jump and its five roads into `BattleScript_ButItFailed` are read from
`src/battle_script_commands.c`, `src/battle_util.c`, `include/constants/battle.h` and
`data/battle_scripts_1.s`. `UpdateStatusIconInHealthbox` reading `MON_DATA_STATUS` alone, testing
Sleep, any Poison, Burn, Freeze and Paralysis in that order and falling through to
`HEALTHBOX_GFX_39` is read from `src/battle_interface.c`. Yawn's accuracy of 100 against Haze's
and Psych Up's 0 is from `src/data/battle_moves.h`, and the level-up entries for Slowpoke,
Slowbro, Slowking, Slakoth and Slaking at 1, Gulpin at 6, Dunsparce at 11, Togepi at 16, Relicanth
at 22, Snorlax at 24, Chimecho at 25, Wooper at 31 and Quagsire at 35 are from
`src/data/pokemon/level_up_learnsets.h`. All of it is **third generation**, read from
`pokeemerald`; Yawn's interaction with later additions such as powder immunity and Safety Goggles
does not exist in this generation, and later games change both the status display and the ability
list, so a reader checking today's game should read today's game. On the clinical side the
mechanism is long-standing and the measurements are not: the diagnostic performance of individual
abdominal signs is setting-dependent and still being restudied, imaging thresholds move with
availability and dose considerations, the decision rules in use differ by country and are revised,
and local expectations for who reassesses and how often change with each reorganisation. Principle
dated October 2026; read the current guidance for anything past the principle.
