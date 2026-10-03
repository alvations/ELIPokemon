---
id: "m135"
slug: perioperative-checklist-and-first-day
style: pokemon
category: nursing
difficulty: intermediate
question: "Why does a surgical safety checklist exist when every item on it is already somebody's job, and what is the first day after an operation actually watching for?"
tags: [perioperative, surgical-safety-checklist, postoperative, handover, baseline]
---

# `TryDoEventsBeforeFirstTurn` is a named phase, and nothing can be chosen until it finishes.

Emerald does not begin a battle by offering you the menu. It runs a function whose entire job is
to put every standing condition into effect, in a fixed order, before anybody may act — and the
last thing it does is hand control to the move menu by assignment. The function is about ninety
lines, it does nothing a careful reader could not have predicted, and it is the clearest statement
in the cartridge of what a surgical safety checklist is for: **not new information, but a defined
moment at which nobody may proceed.**

Markers used below, because this half carries clinical claims. (**mechanism**) means it follows
from the structure; (**definitional**) is what the word means; (**consensus**) is mainstream
agreement across major guidance; (**country-dependent**) means the reader's own policy or legal
framework decides. Code blocks carry no marker. No fasting interval, observation frequency, drain
volume, dose or physiological threshold appears anywhere here.

## The phase, in the order it actually runs

```
   static void TryDoEventsBeforeFirstTurn(void)
   {
       if (gBattleControllerExecFlags) return;      ◄── will not start mid-animation

       1. sort gBattlerByTurnOrder with GetWhoStrikesFirst(..., TRUE)
                                                   who acts before whom, settled FIRST
       2. AbilityBattleEffects(..., ABILITYEFFECT_SWITCH_IN_WEATHER, ...)
                                                   the field's standing conditions
       3. while (switchInAbilitiesCounter < gBattlersCount)
              ABILITYEFFECT_ON_SWITCHIN, fastest to slowest
       4. ABILITYEFFECT_INTIMIDATE1
       5. ABILITYEFFECT_TRACE
       6. while (switchInItemsCounter < gBattlersCount)
              ITEMEFFECT_ON_SWITCH_IN, fastest to slowest
       7. the reset block: monToSwitchIntoId, gChosenActionByBattler, gChosenMoveByBattler,
          TurnValuesCleanUp(FALSE), SpecialStatusesClear(), absentBattlerFlags,
          gBattleCommunication[], STATUS2_FLINCHED cleared on every battler,
          turnEffectsTracker, wishPerishSongState, moveendState, faintedActionsState,
          turnCountersTracker, gMoveResultFlags, gRandomTurnNumber = Random()
       8. gBattleMainFunc = HandleTurnActionSelectionState;
                                                   ◄── and ONLY NOW is there a menu
   }
   ──────────────────────────────────────────────────────────────────────────────────────────
   Eight steps, one order, every one of them something that would have happened anyway. The
   function introduces nothing. What it introduces is the BOUNDARY.
```

That is the whole answer to *"we already do all of that"*. Every item on a surgical safety
checklist is already somebody's job; what the checklist adds is a point in time at which the whole
team has to stop, out loud, together, and confirm them before anything irreversible happens
(**mechanism**). The failures it targets have one profile — rare, catastrophic, irreversible, and
assembled out of information several people each hold one piece of: the wrong person, the wrong
side, the wrong procedure, a missing implant, an unanticipated airway, an unmentioned allergy, an
item left inside somebody (**consensus**). A task that is everybody's job is nobody's, and step 8
is the engine's version of the fix.

And it is worth naming what steps 3 to 6 actually put into effect, because the list is short and
every entry is a standing property that somebody brought into the room with them. The
`ABILITYEFFECT_ON_SWITCHIN` case list holds exactly seven: **Drizzle** on **Kyogre**,
**Sand Stream** on **Tyranitar**, **Drought** on **Groudon**, **Intimidate**, **Forecast** on
**Castform**, **Trace**, and **Cloud Nine** or **Air Lock** sharing one branch — **Rayquaza**'s
being the latter. Steps 4 and 5 then re-run **Intimidate** and **Trace** separately, because each
needs a target chosen and a message printed and neither can be resolved inside the loop that
discovered it.

And `ITEMEFFECT_ON_SWITCH_IN` holds exactly two hold effects, which is the detail that earns its
place:

```
   case ITEMEFFECT_ON_SWITCH_IN:
       case HOLD_EFFECT_DOUBLE_PRIZE:         ◄── Amulet Coin. Sets moneyMultiplier = 2.
           gBattleStruct->moneyMultiplier = 2;     Nothing to do with the battle at all
       case HOLD_EFFECT_RESTORE_STATS:        ◄── White Herb
           for (i = 0; i < NUM_BATTLE_STATS; i++)
               if (gBattleMons[battler].statStages[i] < DEFAULT_STAT_STAGE)
                   gBattleMons[battler].statStages[i] = DEFAULT_STAT_STAGE;
   ──────────────────────────────────────────────────────────────────────────────────────────
   Two items. One RESTORES THE BASELINE before the first turn — it writes the same
   DEFAULT_STAT_STAGE the intro wrote — and the other is about prize money. A real checklist
   is the same mixture: items that decide whether somebody survives the next hour, sitting
   beside items that exist because somebody has to be billed, and the pause does not rank
   them.
```

Step 1 is worth its own sentence. The very first thing the function settles is **who acts before
whom**, and it settles it with `ignoreChosenMoves` set to `TRUE` — before anybody has chosen
anything. Establishing roles before the work starts, rather than discovering them during it, is
the part of the checklist that looks least clinical and has the strongest claim to be the active
ingredient (**consensus**).

## Every step stores how far it got, which is why an interruption cannot skip one

```
   gBattleStruct->overworldWeatherDone        a flag:  step 2 has happened
   gBattleStruct->switchInAbilitiesCounter    an index: step 3 has reached THIS battler
   gBattleStruct->switchInItemsCounter        an index: step 6 has reached THIS battler

   ... and each step is written to RETURN as soon as it produced an effect:

       if (!gBattleStruct->overworldWeatherDone && AbilityBattleEffects(...) != 0)
       { gBattleStruct->overworldWeatherDone = TRUE; return; }      ◄── leaves, mid-phase

       while (gBattleStruct->switchInAbilitiesCounter < gBattlersCount)
       {
           if (AbilityBattleEffects(ABILITYEFFECT_ON_SWITCHIN, ...) != 0) effect++;
           gBattleStruct->switchInAbilitiesCounter++;                ◄── advanced BEFORE
           if (effect != 0) return;                                        the return
       }
   ──────────────────────────────────────────────────────────────────────────────────────────
   The phase is re-entered on the next frame and RESUMES where it stopped, because the
   position is stored outside the function. Interrupt it with a Drizzle animation, an
   Intimidate message, a Berry being eaten — and no step is repeated and none is skipped.
```

This is the structural feature of a checklist that is almost never taught, and the engine makes it
obvious. A pause performed in a room with people moving through it **will** be interrupted, and
the thing that makes it survive interruption is that its position is held somewhere other than in
the head of the person reciting it. A paper or screen checklist, read item by item with a visible
mark against each, is `switchInAbilitiesCounter`. A checklist recited from memory is a local
variable, and it is lost on the first interruption (**mechanism**).

## Three passes at three defined moments

The engine checks three times, at three points of no return, with three different case lists — and
that is the three-pause structure exactly.

```
   the engine's pass                      the pause              the question it answers
   ────────────────────────────────────── ────────────────────── ───────────────────────────────
   TryDoEventsBeforeFirstTurn              SIGN IN                before induction: is this the
   — once, before any action is even        (before anaesthesia)   right person, consenting to
   selectable                                                      the right procedure on the
                                                                    right site, with airway,
                                                                    allergies, blood and
                                                                    equipment accounted for?
                                                                    After induction they cannot
                                                                    answer for themselves, which
                                                                    is why the boundary is here
   ────────────────────────────────────── ────────────────────── ───────────────────────────────
   AtkCanceler_UnableToUseMove             TIME OUT               before the incision: does
   — m067's chain, run at the instant of    (before the incision)  everyone know who everyone
   the act, every time. In order: sleep                            else is, what is about to be
   with Early Bird and the Snore and                               done, what is expected to be
   Sleep Talk exceptions, freeze, Truant,                          difficult, and what each
   Hyper Beam's recharge, flinch, Disable,                         discipline is worried about?
   Taunt, Imprison, confusion, paralysis                           And it is re-run EVERY turn,
   at Random() % 4, Attract's infatuation,                         so a clear pass last time is
   Bide, and the thaw. Fourteen cases                              no evidence about this time
   ────────────────────────────────────── ────────────────────── ───────────────────────────────
   TurnBasedEffects and the                SIGN OUT               before anybody leaves: what
   HandleEndTurn_ family                    (before leaving        was actually done, do the
   — the end-of-turn roster, m109's          theatre)               counts reconcile, where are
   fixed-order case list                                            the specimens going, and
                                                                     what does the ward need to
                                                                     watch for?
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Three passes, three moments, three case lists, and each placed immediately before
   something that cannot be undone.
```

The content of each clinical pause is local and the placement is the design (**consensus**); the
items on any given version of the list belong to the reader's own theatres
(**country-dependent**).

And the sign out is the one the engine warns you about. `HandleEndTurn_BattleWon` calls
`BattleStopLowHpSound` twice, on two different branches, because by the time a battle is over the
control flow has already split and things that should happen once have to be written twice to
happen at all. The clinical version is that the sign out is the pause most often truncated,
because by then the operation is finished and people are leaving the room (**consensus**).

## The baseline is what the reset block exists to create

Step 7 looks like housekeeping and it is the most load-bearing step in the function.

```
   where the stat stages are first written:
       BattleIntroDrawTrainersOrMonsSprites — during the INTRO, before anything happens:
           for (i = 0; i < NUM_BATTLE_STATS; i++)
               gBattleMons[gActiveBattler].statStages[i] = DEFAULT_STAT_STAGE;

   and where they are written again:
       SwitchInClearSetData — on a switch, unless the move was Baton Pass:
           same loop, same DEFAULT_STAT_STAGE

   #define DEFAULT_STAT_STAGE 6        (MIN 0, MAX 12, in include/constants/pokemon.h)
   and the White Herb's switch-in branch writes the SAME 6 back over anything lower
   ──────────────────────────────────────────────────────────────────────────────────────────
   6 is both the NEVER-SET value and the CLEARED value, which is m070's pertinent-negative
   problem: a stage reading 6 cannot be distinguished from a stage that was raised and
   then reset. Without the intro's write there would be no 6 to compare against at all —
   so the housekeeping step is the thing that makes a later reading mean a CHANGE.
```

Everything watched after an operation is a comparison, and the comparator is the preoperative set
of observations (**mechanism**). Without it, a postoperative value is a reading rather than a
change, and the change is the information. m001 is the full argument about reading a composite
against a trend; the perioperative version is sharper, because the person will move quickly and
nobody will know in which direction. The other half of step 7 is the same shape:
`TurnValuesCleanUp` zeroes the whole `ProtectStruct` byte by byte, `SpecialStatusesClear` does the
same to `SpecialStatus`, and `status2 &= ~STATUS2_FLINCHED` is applied to every battler — a batch
of unrelated fields deliberately set to a known value at one defined moment, which is what
"baseline observations, allergies, site marked, medicines decision recorded" is as a list.

## The watch list, and the sinks with no pixel

What the first day is watching for is four mechanisms, and the engine's relevant fact is that its
own end-of-turn roster is long while its display reads one field.

```
   mechanism watched on day one        what shows EARLY                     the engine's parallel
   ─────────────────────────────────── ──────────────────────────────────── ──────────────────────
   AIRWAY and VENTILATION — residual    reduced rate or depth, sleepiness,   m107's trap: a
   anaesthesia, neuromuscular           intermittent snoring obstruction,    saturation inside a
   blockade, opioid effect              a saturation held up by oxygen       target range is fully
                                        while carbon dioxide rises          compatible with a
                                                                             rising carbon dioxide
   ─────────────────────────────────── ──────────────────────────────────── ──────────────────────
   BLEEDING and HYPOVOLAEMIA            rising pulse, narrowing pulse        m034's PP: the budget
                                        pressure, cool peripheries,          being spent is not on
                                        reduced urine output, restlessness   the bar, and the bar
                                        — a FALLING pressure is LAST         is all the game shows
   ─────────────────────────────────── ──────────────────────────────────── ──────────────────────
   THE SITE and the cavity operated     a change in drain character or       Leech Seed, Nightmare,
   on                                   volume, distension, a leak, pain     Curse and the Bind,
                                        out of proportion to the expected    Clamp, Fire Spin,
                                        course                               Whirlpool and Wrap
                                                                             family: real HP sinks
                                                                             in stores the
                                                                             healthbox never reads
   ─────────────────────────────────── ──────────────────────────────────── ──────────────────────
   THE PREDICTABLE SYSTEMS              retention; nausea and vomiting;      m102's count: nine
   CONSEQUENCES                         hypothermia and shivering;           end-of-turn sinks held
                                        glycaemic disturbance; immobility    in five stores, and
                                        and venous thromboembolic risk;      UpdateStatusIconIn-
                                        confusion that is new                Healthbox reads ONE.
                                                                             Leftovers, Rain Dish,
                                                                             Sandstorm and Hail all
                                                                             move HP with no pixel
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Every row compensates before it decompensates, which is why the first day is a frequency
   and a baseline rather than a single review.
```

That compensation point is both mechanism and mainstream agreement, and it is the reason the first
postoperative day is an observation frequency against a baseline rather than a single review
(**mechanism**, **consensus**).

Two of those rows need saying outside the table.

**New confusion is a finding with a differential** — hypoxia, hypotension, sepsis, retention,
pain, medicines, withdrawal, electrolyte disturbance — and not an expected feature of being old
and having had an operation (**consensus**). It is the single most commonly misattributed
postoperative observation, and the assessment and management of delirium are a separate subject
that belongs elsewhere and not in a register built out of a video game.

**Postoperative pain** is on the watch list and is deliberately not analysed here: its assessment
and management belong to local policy and to the person's own clinicians. What is in scope is only
the structural fact that pain out of proportion to the expected course is **a finding about the
operation** rather than only a comfort problem, and that treating it purely as something to be
medicated can bury the finding (**consensus**).

And the handover. The recovery-to-ward transfer is the point of maximum information loss in the
whole pathway, for m070's and m002's reasons: the largest transfer, between two teams with no
shared context, about somebody who cannot yet supply their own history, at the moment the baseline
matters most and the receiving team has never seen it. What a ward needs is not a summary of the
operation but **the expected course and the specific triggers for this operation** — without
which deviation cannot be told from normal recovery and the observation plan collapses back to
generic thresholds (**mechanism**). m070's `SwitchInClearSetData` is the exact object: what is
deleted at the boundary against what survives it, with the history in neither column.

## Where the metaphor stops

It stops completely at the person on the table, and nothing above is about them. Every device in
this answer is about a *process* — an ordered phase, a stored position, three pauses, a baseline,
a watch list — and that is deliberate. Nothing in a game stands for somebody anaesthetised, and
nothing in a game stands for the first day after an operation as it is experienced.

An operation is one of the very few things in medicine done *to* somebody while they are not
present to themselves, and every part of this subject is organised around that fact. Being
anaesthetised means handing over your airway, your position, your dignity and your ability to
object to a room full of people you met twenty minutes ago, most of whom you will never see again
and some of whom you will never see at all. Patients are frequently more frightened of the
anaesthetic than of the surgery, and that fear is rarely addressed because the anaesthetic is
treated as the technical part. The checklist's introductions exist partly for the team's sake and
partly because a person who is asked their name and their procedure, by someone looking at them,
is being treated as present.

Consent and capacity are the parts of this subject with the largest consequences and the least
room for a revision answer. Who may consent, what must be disclosed, what happens when capacity is
absent or fluctuating, and how an advance decision is handled differ profoundly between countries,
and all of it is law. They are named here and not reasoned about here; the reader's own legal
framework and local policy are the only authority on them.

Two things about the first day that belong to the person rather than to the process. Waking up
disorientated, cold, nauseated and barely able to move is frightening, and being told beforehand
that each of those is expected changes the experience of it substantially — one conversation, and
it is routinely skipped. And people are usually too unwell on the first day to ask the question
they most want answered, which is what was found and what it means, so it gets answered on a ward
round they will not remember, or by whoever happens to be nearest, or not at all.

And the context, because it decides whether the pauses happen. The checklist is performed by a
team under production pressure in a system measured on theatre throughput, and the sign out is the
item that competes most directly with the next case. An institution that answers a checklist
failure by auditing completion rates, having changed nothing about the time between cases, has
chosen the one variable that measures the form rather than the pause.

## What Nurse Joy is listening for

Why the failures a checklist targets have the profile they do, and why a defined pause is the
answer to that profile specifically. The three pauses, the question each answers, and why each
sits immediately before a point of no return. The two halves of the active ingredient — the
content and the team process — and the evidence that implementation rather than existence
determines the effect. Why the position of a checklist has to be stored outside the person
reciting it. Why the baseline is the most clinically load-bearing item in the preoperative list,
and why `DEFAULT_STAT_STAGE` is the right picture of what a missing one costs. The four mechanisms
watched on the first day, and why each compensates before it decompensates. Why new confusion is a
finding with a differential. Why the recovery-to-ward handover is the point of maximum information
loss, and what it has to contain. Why "post-op" is a dangerous explanation. And the local answers:
which checklist version is in use, what the local fasting and observation policies say, and what
the reader's own legal framework requires for consent.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The **surgical safety checklist published by the World Health Organization**, together with the
  locally adapted version in use in the reader's own theatres — which is the one that binds, and
  which differs from the original by design, because local adaptation is part of the method.
* The reader's national guidance on routine preoperative assessment and on perioperative care for
  the adult surgical patient, which sets the fasting, optimisation and observation requirements
  locally and differs by country.
* The reader's institutional policy on postoperative observation frequency, recovery discharge
  criteria and the recovery-to-ward handover.
* The published literature on the surgical safety checklist: the original multi-site study, the
  later population-level evaluations that did not reproduce its effect size, and the
  implementation research that is the best available explanation of the discrepancy. The contested
  effect size lives there and should be read rather than summarised.
* The reader's national guidance on recognising and responding to acute deterioration, for the
  escalation structure the first day depends on.
* The reader's own legal framework on consent and capacity. This is law, it differs profoundly
  between countries, and nothing here substitutes for it.
* A current textbook of perioperative or surgical nursing, for the preoperative content and the
  postoperative complication mechanisms.

The Pokémon material is from the **pret/pokeemerald** decompilation of Pokémon Emerald:
`TryDoEventsBeforeFirstTurn` with its three stored position markers, `TurnValuesCleanUp`,
`SpecialStatusesClear`, `SwitchInClearSetData`, `BattleIntroDrawTrainersOrMonsSprites` and the
`HandleEndTurn_` family in `src/battle_main.c`; `AtkCanceler_UnableToUseMove` and
`TurnBasedEffects` in `src/battle_util.c`; `BattleStopLowHpSound` in `src/battle_gfx_sfx_util.c`;
and `DEFAULT_STAT_STAGE` in `include/constants/pokemon.h`. The order of the eight steps and the
locations of the stat-stage writes were read out of the source rather than recalled.

## Scope and safety

This explains what a surgical safety checklist is for and what the first postoperative day is
watching for, through a game's pre-turn initialisation code, at the level of someone already
training in or qualified for clinical practice. It is not a checklist, not a preoperative or
postoperative protocol, and not a guide to managing any complication. It deliberately states no
fasting interval, observation frequency, drain output volume, dose or physiological threshold,
because all of those are set by the reader's institution and national guidance, which are the
authority. It does not address the assessment or management of postoperative pain, or of delirium,
both of which are out of scope here and belong to local policy and to the person's own clinicians.
It is explicitly not a basis for reasoning about consent or capacity, which are legal matters
belonging to the reader's own jurisdiction. Nothing here has had clinical review. Nothing here is
for use in an emergency or for a decision about any person's care. If someone is unwell right now,
the local emergency number is the correct response.

## Where this stands, October 2026

The mechanical material is fixed, and the structural argument does not date: the failures a
checklist targets are rare, catastrophic and assembled out of information held in pieces, and a
defined pause is the response to that structure. What has been contested for over a decade is the
size of the effect — the original multi-site result was not reproduced at population scale, and
the most persuasive account of why is about implementation rather than about the instrument.
Expect that argument to continue, and expect the checklist to keep being adapted locally, which is
how it was designed to be used. The surrounding practice moves faster: enhanced recovery pathways,
day-case expansion, reduced fasting, preoperative optimisation programmes and increasingly
structured handover tools are all active, and every one of them changes what the first day looks
like. Everything procedural and legal here is local, and the reader's institutional policy,
national guidance and legal framework are the authority throughout.
