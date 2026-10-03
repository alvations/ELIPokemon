---
id: "m128"
slug: the-threatened-limb
style: pokemon
category: emergency
difficulty: advanced
question: "Why is time the whole of the problem in a threatened limb, and why is the examination comparative?"
tags: [limb, ischaemia, time, comparative-examination, revision]
---

# The accuracy check never reads one number, and the Badly Poisoned counter never reads down

Two mechanics, and the answer is the pair of them. One is a measurement that does not exist except
as a difference. The other is a cost that is a function of nothing but elapsed turns.

## The accuracy formula has no absolute terms in it

This is the whole of `Cmd_accuracycheck`'s arithmetic, once the early exits are past:

```
   if (gBattleMons[gBattlerTarget].status2 & STATUS2_FORESIGHT)
       buff = gBattleMons[gBattlerAttacker].statStages[STAT_ACC];
   else
       buff = gBattleMons[gBattlerAttacker].statStages[STAT_ACC]
              + DEFAULT_STAT_STAGE
              - gBattleMons[gBattlerTarget].statStages[STAT_EVASION];

   if (buff < MIN_STAT_STAGE)  buff = MIN_STAT_STAGE;
   if (buff > MAX_STAT_STAGE)  buff = MAX_STAT_STAGE;

   calc  = sAccuracyStageRatios[buff].dividend * gBattleMoves[move].accuracy;
   calc /= sAccuracyStageRatios[buff].divisor;
```

Read the else-branch carefully, because it is doing three things at once.

**The attacker's accuracy stage is never used on its own.** It is added to the target's evasion
stage with the sign reversed. A Pokémon with an accuracy stage of +2 facing one with an evasion
stage of +2 indexes the table at exactly the same place as a pair with both at zero. The two
readings are only meaningful together, and the engine never computes either one alone.

**`DEFAULT_STAT_STAGE` is the offset that makes the difference readable.** The stat stages are
stored as `0` to `12` with `6` as neutral, so `acc − evasion` ranges from `−6` to `+6` and would
index off the front of a thirteen-entry array. Adding `DEFAULT_STAT_STAGE` back in puts the
neutral case at index 6, where `sAccuracyStageRatios` holds `{1, 1}`. The constant is not a fudge;
it is the statement that **a difference of zero is the normal result** — and the normal result has
to be written down somewhere for a difference to mean anything.

**One condition deletes the comparison.** `STATUS2_FORESIGHT` on the target drops the evasion term
entirely, and what is left is `buff = acc`: an absolute reading of a quantity that was never
meaningful in absolute terms. The engine has not improved the measurement. It has thrown away the
control and kept the sample.

And that one bit does a second, unrelated job, which is worth seeing because it is the same shape
as question m061's device. `TYPE_FORESIGHT` is a **sentinel row sitting inside the
type-effectiveness table**, and when the bit is set the walk over the table `break`s at the
sentinel instead of stepping past it — so every row after that point, which is where the Ghost
immunities live, is never consulted. One bit; two mechanisms; the only thing they have in common
is the bit. Foresight is learned by Venonat and Venomoth at 1, Noctowl at 1, Sableye at 5,
Hoothoot at 6, Duskull and Dusclops at 12, Mudkip at 19, Marshtomp and Swampert at 20, Machop,
Machoke and Machamp at 22, and Hitmonlee at 36.

## Psych Up is the only move whose effect is to take the other side's reading as your own

`Cmd_copyfoestats` is five lines and has no failure case:

```
   for (i = 0; i < NUM_BATTLE_STATS; i++)
       gBattleMons[gBattlerAttacker].statStages[i] = gBattleMons[gBattlerTarget].statStages[i];

   gBattlescriptCurrInstr += 5; // Has an unused jump ptr (possibly for a failed attempt) parameter.
```

Eight slots copied wholesale, the other side's numbers written over your own. And the comment in
the source is the detail: the script passes it `copyfoestats BattleScript_ButItFailed`, so a
failure branch exists, is wired up in `BattleScript_EffectPsychUp`, and **is never taken** — the
command skips its five bytes unconditionally. Somebody reserved a way for the comparison to fail
and then found no case in which it could.

Psych Up's data entry is consistent with that: power 0, Normal, `.accuracy = 0` — which the engine
reads as *skip the accuracy check altogether*, so it does not go through the formula above — 10
PP, and `FLAG_SNATCH_AFFECTED` with no `FLAG_PROTECT_AFFECTED`, so Protect does not stop it.
Psyduck and Golduck learn it at 31, Spoink and Grumpig at 19, Spinda and Meditite at 38, Medicham
at 40, Espeon at 42, Drowzee at 43 and Hypno at 55.

Two more things in the engine bear on the same point.

**`Haze` is the opposite operation and it is deliberately bilateral.** `Cmd_normalisebuffs` loops
over *every battler on the field* and writes `DEFAULT_STAT_STAGE` into all eight slots — both
sides, all stats, in one pass. Haze does not restore your readings; it abolishes the comparison by
making every reading the reference value. Its entry is power 0, Ice type, accuracy 0, 30 PP,
`MOVE_TARGET_USER`, which is a move that targets itself and changes the opponent. Ekans has it at
44, Zubat at 46, Koffing and Weezing at 33, Murkrow at 22, Surskit at 37, Vaporeon at 42, Seviper
at 43, Arbok, Golbat and Crobat at 56, Wooper at 51, Quagsire at 61.

**`AccuracyCalcHelper` can bypass the whole calculation before it starts.** Its first test is
`gStatuses3[target] & STATUS3_ALWAYS_HITS` with the right `battlerWithSureHit`, and on a match it
returns TRUE and the comparison never runs. That is Lock-On and Mind Reader, which question m044
reads as the intravenous route: the point there and here is the same — this is not a more accurate
measurement, it is the measurement being skipped. Lock-On is Magnemite at 32, Magneton at 35,
Remoraid at 11, Nosepass at 46, Regirock, Regice and Registeel at 57; Mind Reader is Nincada,
Ninjask and Shedinja at 19, Meditite and Medicham at 22, Hitmonlee at 31, Articuno at 37 and
Breloom at 45.

## The other mechanic is a counter, and the counter is the whole cost

`ENDTURN_BAD_POISON` in `src/battle_util.c`:

```
   gBattleMoveDamage = gBattleMons[battler].maxHP / 16;
   if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
   if ((status1 & STATUS1_TOXIC_COUNTER) != STATUS1_TOXIC_TURN(15))
       status1 += STATUS1_TOXIC_TURN(1);
   gBattleMoveDamage *= (status1 & STATUS1_TOXIC_COUNTER) >> 8;
```

Four lines, five properties, and every one of them is the clinical point.

* **The base is `maxHP/16` and the multiplier is the turn count.** The *n*th turn costs *n* times
  the first. The running total after *n* turns is `n(n+1)/2 × maxHP/16` — quadratic in elapsed
  turns, so the second half of any interval costs more than the first half of the same interval.
* **On turn one it does `maxHP/16`, which is exactly half what ordinary Poison does.**
  `ENDTURN_POISON` is a flat `maxHP/8`. So at first contact, the condition whose cost compounds
  looks **milder** than the one whose cost does not. This is the established Part I device from
  questions m024 and m054, and it is in this answer for the same reason it is in those: the
  readout at the first look is anti-correlated with the trajectory.
* **The counter increments before the multiply, so there is no free turn.** The first end-of-turn
  pass takes the counter from 0 to 1 and bills ×1. Nothing is ever charged at zero.
* **It is capped at 15 and it never decrements.** No move, item, ability or action in the game
  moves `STATUS1_TOXIC_COUNTER` downwards. It is cleared only by clearing the poison outright —
  `status1 &= ~(STATUS1_PSN_ANY | STATUS1_TOXIC_COUNTER)` — which is all or nothing.
* **It survives switching out.** `SwitchInClearSetData` resets all eight stat stages to
  `DEFAULT_STAT_STAGE`, zeroes `status2`, zeroes `gStatuses3` and wipes the whole `DisableStruct`
  byte by byte — and it never touches `status1`. So every volatile reading is reset by leaving the
  field and the counter is not. Question m070 reads the same function for what crosses a boundary
  and what does not; this is the field that crosses.

And one thing the screen does with all of that: nothing. `UpdateStatusIconInHealthbox` tests
`STATUS1_PSN_ANY`, which is `POISON | TOXIC_POISON`, and draws one PSN graphic. The same graphic
on turn one and on turn fifteen, and the same graphic for the flat condition and the compounding
one. The counter occupies bits 8 to 11 of a field the healthbox reads and then does not look at.

Toxic itself is a TM in this generation and is learned by level-up by remarkably few species —
Gulpin at 28, Swalot at 31, Dustox at 38 and Roselia at 45 — so in practice the counter usually
arrives from a TM, which is to say from a decision somebody made earlier and off-screen.

## Where the game has nothing

Two gaps, and saying so is more useful than inventing something.

**Nothing in this engine is irreversible.** The counter is cleared outright by a Full Heal, by a
Pecha Berry, by Natural Cure on a switch, by Rest, by Heal Bell — and after it is cleared the next
application starts at 1 again. There is no record that it ever reached 15 and no residue of having
been there. That is the single largest difference between the counter and anything it is standing
for here, and it is stated inside the body rather than at the end because a reader using the
device needs it at the point of use.

**Nothing in this engine records when anything started.** `gBattleResults.battleTurnCounter`
counts turns of the battle, not turns since a condition began, and the toxic counter is a *count
of billings*, which is the same number only if nothing interrupted. There is no stored timestamp
anywhere. So the engine has no mechanic at all for the single most important field in this
presentation, and the absence is the honest thing to report.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is a person in severe pain whose
limb is threatened.

A limb whose perfusion has failed is unusual in that almost everything is settled by one variable:
**elapsed time since perfusion failed**, which is running before anyone has been told.
(**Mechanism.**) Two consequences follow, and they are the same consequence twice. Every step that
does not shorten the interval is a cost with no offsetting benefit, including steps that would be
good practice in almost any other presentation. And the examination has to be read against the
other limb, because almost none of its findings carry information in absolute terms.

Tissues distal to an occlusion do not fail together. Nerve is least tolerant, with sensory fibres
involved before motor, so the earliest objective change is in sensation and the earliest motor
change already indicates a later point on the clock — the second finding is not a more severe
version of the first but a later one. Muscle is intermediate, and once it has infarcted, restoring
flow introduces a second problem rather than only solving the first, with systemic consequences
and the possibility of rising compartment pressure after flow returns. Skin, fat and bone are most
tolerant, so an unremarkable-looking limb is a weak negative in the same structural way a soft
abdomen is — question m126's argument. (**Mechanism** for the ordering and its consequences;
(**consensus**) for the clinical handling of reperfusion.) The pulse is not a clock at all:
whether it is present depends on the level of the occlusion and on what collateral exists.

The examination is comparative because its findings are differences. Limb temperature, colour,
capillary refill, sensation, power and the level at which pulses are palpable each mean very
little in isolation — colour especially, since the standard descriptions fail in darker skin,
which is question m018's argument — and each becomes a measurement when read against the
contralateral side. That control is unusually good: same person, same circulation, same ambient
temperature, same minute, same observer. (**Mechanism.**) Which makes the failure mode
predictable. Bilateral disease, a previous amputation, a prosthesis, pre-existing neuropathy,
residual weakness from an earlier stroke, longstanding bilateral peripheral arterial disease, a
limb already in a cast — in each the paired reading is gone, and what remains is an absolute
reading of a quantity that was never absolute. The correct response is to say so explicitly and
look for another reference: the person's own account of their usual state, a previous examination,
a previous record of pulses.

The examination cannot establish **when the clock started**, and that is the variable everything
depends on. Sudden against gradual onset points at different mechanisms and at different start
times for identical findings; a gradual onset may mean collateral supply has had time to develop,
so one examination can be compatible with a limb that has hours and with one that has had a poor
supply for years. (**Consensus** for the onset distinction; (**mechanism**) for the collateral
argument.) Somebody else frequently supplies the time — who last saw the person moving normally,
when they last stood, when the pain began relative to something datable. This is question m068's
reasoning about mechanism of injury: the information exists at one point, must be collected there,
and must be handed on because the next person cannot recover it. And it should be recorded as a
**clock time rather than a duration**, because *four hours* written at eleven o'clock is wrong by
one o'clock and is routinely re-read as current. (**Mechanism.**)

What follows structurally, with no protocol, agent, dose, technique, classification, score or
threshold named anywhere in this answer: steps that can run in parallel should, because a
sequential workflow spends the only resource that matters; the referral is early and provisional
rather than complete and late; investigation genuinely competes with the clock and the trade-off
is local — question m104's argument about a test with its own harm; and the field most often lost
across a handover is the time of onset, which is the one thing no later examination can
regenerate. Which service receives the referral, how it is contacted and what response is expected
are (**country-dependent**) and institutional.

And what is at stake for a person is not a mechanic. Someone in this situation is usually in
severe pain, often out of proportion to anything visible, and that pain is itself information —
disproportionate, poorly localised and unrelenting, and pain on passive movement is a finding. It
also makes the rest of the examination worse, because the paired comparison the whole assessment
rests on cannot be performed properly on somebody who cannot bear to be touched. Because time is
the dominant cost there is a standing temptation to skip whatever does not shorten the interval,
and comfort is the usual casualty; nothing in the clock argument justifies that. The specific
management of pain is deliberately not described here, and neither is anything about outcome or
prognosis, both as a matter of policy for this directory rather than oversight. A person being
assessed has usually already worked out what the possibilities are and will be reading the room,
so honest, specific, non-promissory information — what is being done, who has been called, what
the next decision point is and when — is what they can use. And the account of time usually
belongs to somebody who is not the patient, who is frightened, often blaming themselves for not
noticing sooner, and holding the single most valuable piece of information in the encounter. They
should be asked carefully rather than hurriedly.

No Pokémon stands for a patient anywhere in this answer. No creature is injured, no limb exists,
nothing is ischaemic and nothing is lost. The game is carrying three ideas and no others: that a
measurement can have no absolute terms in it, so deleting the control does not produce a worse
reading but a different and emptier kind of reading; that a cost can be a function of nothing but
elapsed time, can compound, and can be charged at a rate that is smallest at the first look; and
that a count of billings is not a timestamp, so an engine with no stored start time has nothing to
say about when anything began. Pain, fear and the weight carried by whoever found the person are
stated above without ornament and are not mechanics.

## What a Gym Leader is listening for

* Write out the accuracy formula. How many of its terms are absolute?
* What is `DEFAULT_STAT_STAGE` doing in that expression, and what would break without it?
* `STATUS2_FORESIGHT` changes the formula. Say how, and say whether that is an improvement.
* That same bit does a second job elsewhere. What, and what does it skip?
* `Cmd_copyfoestats` is passed a failure pointer. What happens to it?
* Haze targets the user and changes the opponent. Explain, and say what it does to the comparison.
* What does `AccuracyCalcHelper` do before the formula runs, and which two moves set that bit?
* Give the cost of the *n*th turn of Badly Poisoned, and the running total after *n* turns.
* On turn one, which does more damage, Poison or Badly Poisoned? What is the lesson?
* Which of `status1`, `status2`, `gStatuses3` and `statStages` survive `SwitchInClearSetData`?
* Name the two things this engine has no representation of at all.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* A current standard textbook of **vascular surgery**, for the differential tolerance of nerve,
  muscle and skin to ischaemia, for the consequences of reperfusing infarcted muscle, and for the
  relationship between the level of occlusion and the pulse examination.
* The current guidance on acute limb ischaemia issued by **the reader's national vascular society
  or the relevant surgical college** — the document carrying the classification in use, the time
  expectations and the imaging recommendations, none of which appears here.
* The current referral and time-critical pathway standards of **the reader's national emergency
  medicine college**, and **the reader's own employing organisation's** policy on which service
  receives this referral and what response is expected.
* A current standard textbook of **clinical neurology or neurophysiology**, for the ordering of
  sensory before motor involvement in a nerve deprived of perfusion.
* **The primary literature**, for anything about time windows and salvage, which is where the
  quantitative claims live and why no time figure is quoted here.

Markers used in the plain-prose section above: (**mechanism**) (follows from anatomy or physiology
and is checkable by reasoning), (**consensus**) (agreed across mainstream sources as of writing),
(**country-dependent**) (genuinely differs between countries, services or institutions). No
classification, score, threshold, time window, technique, agent or dose is given, and nothing is
quoted, because none of these was opened. The Pokémon side is in the opposite position and is
sourced file by file in the closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why one variable can dominate a presentation and why an
examination is a paired measurement*, written for someone already trained, and the Pokémon framing
covers only comparative arithmetic and a one-way counter. It is deliberately not a protocol and
not a decision aid: no classification system, no score, no threshold, no time window, no imaging
pathway, no technique, no agent and no dose. The management of pain is not described, and nothing
about outcome or prognosis appears anywhere, both deliberately. Referral routes, response-time
expectations, imaging availability and surgical arrangements differ sharply between countries and
institutions. The reader's own national guidance and local policy are the authority; this is not,
and it has had no clinical review. Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. `Cmd_accuracycheck`'s `buff = acc +
DEFAULT_STAT_STAGE - evasion`, its Foresight branch, the clamp to `MIN_STAT_STAGE` and
`MAX_STAT_STAGE`, `sAccuracyStageRatios` holding `{1, 1}` at index 6, `AccuracyCalcHelper`
returning early on `STATUS3_ALWAYS_HITS`, `Cmd_copyfoestats`'s eight-slot copy and unconditional
five-byte skip with the unused failure pointer, `Cmd_normalisebuffs` writing `DEFAULT_STAT_STAGE`
into every slot of every battler, and `TYPE_FORESIGHT` as a sentinel row that truncates the
type-effectiveness walk are read from `src/battle_script_commands.c`. `ENDTURN_BAD_POISON`'s
`maxHP/16`, its cap at `STATUS1_TOXIC_TURN(15)`, the increment before the multiply, and
`ENDTURN_POISON`'s flat `maxHP/8` are from `src/battle_util.c`; `STATUS1_TOXIC_COUNTER` occupying
bits 8 to 11 and `STATUS1_PSN_ANY` covering both poisons are from `include/constants/battle.h`;
`DEFAULT_STAT_STAGE` as 6 with `MIN_STAT_STAGE` 0 and `MAX_STAT_STAGE` 12, and `NUM_BATTLE_STATS`
as 8, are from `include/constants/pokemon.h`. `SwitchInClearSetData` resetting the stat stages,
`status2`, `gStatuses3` and the whole `DisableStruct` while never touching `status1` is from
`src/battle_main.c`, and the single PSN graphic from `src/battle_interface.c`. The move entries
for Psych Up, Haze and Toxic and the level-up entries quoted for Foresight, Psych Up, Haze,
Lock-On, Mind Reader and Toxic are from `src/data/battle_moves.h` and
`src/data/pokemon/level_up_learnsets.h`. All of it is **third generation**, read from
`pokeemerald`. The badly-poisoned counter's behaviour on switching out is generation-dependent and
changes in later games, and the stat-stage multiplier tables change too, so a reader checking
today's game should read today's game. On the clinical side the mechanism is stable and the
numbers are not: time windows quoted for salvage differ between sources and are still argued
about, classification systems differ between societies and are revised, imaging recommendations
move with availability and technique, and referral routes and response expectations are
institutional. Principle dated October 2026; read the current guidance for anything past the
principle.
