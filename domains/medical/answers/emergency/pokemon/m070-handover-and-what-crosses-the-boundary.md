---
id: "m070"
slug: handover-and-what-crosses-the-boundary
style: pokemon
category: emergency
difficulty: intermediate
question: "Why is the handover from pre-hospital to hospital the point at which information loss costs most, and what is it that actually gets lost?"
tags: [handover, information-loss, pertinent-negatives, human-factors, revision]
---

# Switching out zeroes the struct, and Baton Pass is a hand-written list of what to keep

`SwitchInClearSetData` in Emerald's `src/battle_main.c` is the most precise statement about
handover anywhere in the games, because it is a boundary with the field list written out in C.
When a Pokémon leaves the field, unless the move that did it was Baton Pass, the function does
this:

```
   DELETED at the boundary                           source
   ──────────────────────────────────────────────────────────────────────────────────
   all six statStages[]  →  DEFAULT_STAT_STAGE       the loop at the top
   status2 = 0            confusion, Focus Energy, Substitute,
                          infatuation, trapping, Rage, Bide, Nightmare …
   gStatuses3 = 0         Leech Seed, Lock-On, Perish Song, Ingrain,
                          Mud Sport, Water Sport, semi-invulnerability …
   the WHOLE DisableStruct, byte by byte:
                          ptr = (u8 *)&gDisableStructs[gActiveBattler];
                          for (i = 0; i < sizeof(struct DisableStruct); i++)
                              ptr[i] = 0;
   the history:           gLastMoves, gLastLandedMoves, gLastHitByType,
                          gLastResultingMoves, gLastPrintedMoves, gLastHitBy,
                          lastTakenMove, lastTakenMoveFrom
   ──────────────────────────────────────────────────────────────────────────────────
   SURVIVES: status1 (sleep, poison, burn, paralysis, freeze), HP, PP, the moves,
             the stats, the item — everything that lives in the saved struct rather
             than in battle memory.
   ──────────────────────────────────────────────────────────────────────────────────
```

Look at which side of that line things fall on. What survives is the **persistent record**. What
is deleted is everything that was true *about the situation* — the accumulated position, the
volatile flags, the counters, and, last and most pointedly, the entire history of what had just
been happening. The boundary keeps the chart and throws away the story.

## Baton Pass is the structured handover, and its field list is explicit

One move exists whose entire function is to carry state across that boundary, and the interesting
thing is not that it works. It is that the engine spells out, by hand, exactly what it carries:

```
   status2  &= (STATUS2_CONFUSION | STATUS2_FOCUS_ENERGY | STATUS2_SUBSTITUTE
                | STATUS2_ESCAPE_PREVENTION | STATUS2_CURSED);

   gStatuses3 &= (STATUS3_LEECHSEED_BATTLER | STATUS3_LEECHSEED | STATUS3_ALWAYS_HITS
                | STATUS3_PERISH_SONG | STATUS3_ROOTED | STATUS3_MUDSPORT
                | STATUS3_WATERSPORT);

   and copied back out of a saved disableStructCopy:
       substituteHP, battlerWithSureHit, perishSongTimer,
       perishSongTimerStartValue, battlerPreventingEscape
```

That is a whitelist. Twelve named bits and five named fields — **Leech Seed**, **Lock-On**,
**Perish Song**, **Ingrain**, **Mud Sport**, **Water Sport**, **Substitute**, **Focus Energy**,
confusion, **Curse**, the trapping of a **Mean Look**, and the Substitute's remaining hit points —
chosen in advance by somebody who had to decide which parts of a situation are worth the cost of
carrying. Everything not on the list is deleted by the same code path as an ordinary switch — the
`&=` is doing the deleting. A structured handover is not a mechanism that transfers everything; it
is a decision about which fields exist, and the design question is entirely *which ones*.

And then the part that earns the whole analogy: **the history fields are not on the list.**
`gLastMoves`, `gLastHitBy`, `gLastLandedMoves` are cleared for a Baton Pass exactly as for any
other switch. The deliberate, purpose-built handover tool carries current state and drops the
record of how that state came about. A Pokémon that arrives via Baton Pass has the stat stages and
not the reason for them.

## The gap is invisible, which is the irreducible problem

`DEFAULT_STAT_STAGE` is 6, the middle of the table in `gStatStageRatios`, and it is both the value
for *never modified* and the value written in by `SwitchInClearSetData`. There is no third value
meaning *this was raised and then cleared at a boundary*. Reading `statStages[STAT_SPEED] == 6` on
the far side of a switch, nothing in memory distinguishes:

* nobody ever used a Speed-modifying move on it;
* it had been dropped two stages and the switch reset it;
* it had been raised four stages and the switch reset it.

Identical bytes, three different situations. That is the pertinent-negative problem exactly, and
it is not a flaw in the code — it is what happens whenever a default value and a cleared value are
the same value. No format fixes it from the receiving side; it can only be fixed by the sending
side *stating* the thing, which is the whole argument for saying out loud what was checked and
found absent.

`status1` behaves the other way and the contrast is instructive. Poison survives the switch,
because it lives in the saved struct. So the receiving side gets the status condition and loses
the stat position, which means the boundary is not uniformly lossy — it is lossy in a specific,
predictable direction, and knowing the direction is what lets you compensate for it deliberately.

Except for one ability, and it is worth the detour. `Cmd_switchoutabilities` has exactly one case
in its whole switch statement: **Natural Cure**, carried by **Blissey**, **Starmie** and
**Roselia**, sets `status1 = 0` when the holder leaves the field. For those three, the one thing
that normally crosses the boundary is the one thing deliberately destroyed at it. A field list is
not a fact about the boundary; it is a set of decisions, and a per-case exception can run either
way.

## The exception somebody had to add afterwards

Two lines in `SwitchInClearSetData` are worth more than the rest of this answer put together:

```
   gDisableStructs[gActiveBattler].isFirstTurn = 2;
   gDisableStructs[gActiveBattler].truantSwitchInHack = disableStructCopy.truantSwitchInHack;
```

The whole `DisableStruct` has just been zeroed byte by byte, and then one field is copied back out
of the saved copy. Its name in the decompilation is `truantSwitchInHack`. Somebody found that
**Truant**'s loafing counter being wiped by a switch produced wrong behaviour, and rather than
redesign the boundary they added one field to the carry-over list and called it a hack in the
name.

That is what a handover standard looks like in real life. It is not derived from first principles;
it is a list that grows an entry every time somebody discovers something important was being lost,
and the awkward entries are the ones with the most history behind them. `isFirstTurn = 2` on the
line above is the same thing in the other direction: a field deliberately *set* rather than
cleared, because the receiving side needs to know it has just arrived.

## What the boundary cannot be blamed for

* **It cannot carry what was never recorded.** If nothing ever wrote to a field, clearing it loses
  nothing. The loss happens at the boundary; the omission happened earlier.
* **Clearing is mostly correct.** A Substitute belongs to the Pokémon that made it and a trapping
  effect belongs to the Pokémon that was trapped. Carrying everything would be wrong, not
  generous, and that is exactly why a field list has to be *designed* rather than maximised.
* **And the tool has a cost.** Baton Pass occupies a move slot and spends a turn — and getting to
  it costs more than that. **Ninjask** learns **Swords Dance** at level 25, **Agility** at 38 and
  Baton Pass at 45, and has **Speed Boost** raising the stat every turn it stays in, so the whole
  point of the move is to carry a position that took several turns to build. A handover that
  carries more is not free; somebody is paying for it in time and attention at the moment when
  both are scarcest. **Smeargle**, which can learn the move by copying it, pays the same price.

## Where the metaphor stops

Plain prose from here, with no game in it, because the rest is about people.

A handover is a transfer of state across a boundary, and it carries only what it has fields for.
Numbers, times, interventions and identifiers cross easily. What crosses badly is
disproportionately contextual, comparative and negative: the scene and its details; the
trajectory, which needs two points and is destroyed by reporting only the latest set of
observations; how much support those observations were obtained on; what was actively examined and
found absent; and the sender's own impression, which is an aggregation over many weak signals and
will not volunteer itself unless it is asked for as a closed question. That is **mechanism** — a
property of any bounded transfer, checkable by reasoning.

The pre-hospital-to-hospital boundary is where this costs most for a reason specific to it: it is
the point at which the only people who saw the scene stop being present, and the scene cannot be
re-examined. Every other handover in a patient's journey passes information the receiving team
could in principle obtain again. This one passes some of it for the last time. Add to that the
fact that the first framing sets the receiving team's priors most strongly, that the receiving
team is being asked to receive and act at the same moment, and that the two sides use some of the
same words for different things, and the costs compound. Failures of handover are a well-described
and much-studied source of avoidable harm across healthcare, which is why this has a literature
rather than being a matter of conscientiousness. **(Consensus.)**

Structured handover formats are in widespread use, several exist, and they differ between
ambulance services, hospitals and countries — **country-dependent**, and this answer names none,
because naming one as the standard would be wrong and a half-remembered format is worse than the
local one. What a format fixes is the field-list problem; a single-speaker convention fixes
divided attention; read-back fixes the vocabulary problem; the written record arriving with the
patient fixes the last-item problem; and asking a closed question about the sender's single
greatest concern fixes the aggregation problem. None of them can create information that was never
observed, and a fluent handover of the wrong frame is a failure that a format makes more likely
rather than less.

Two things about the people. The handover happens over the person it is about, in the third
person, while they listen — the content does not change and the way it is said can. And the person
handing over has often worked alone or in a pair, under pressure, sometimes for a long time,
making decisions without the resources the receiving team has; their impression is the densest
thing they carry, the hardest to articulate at speed, and the item most often not asked for.

No Pokémon stands for a patient anywhere in this answer, nothing in the game represents a person
or a transfer of care, and nothing here is a sequence of actions. The game is carrying one idea: a
boundary that deletes everything it has no field for, and a hand-written list of what was judged
worth keeping.

## What a Gym Leader is listening for

* What exactly does `SwitchInClearSetData` delete, and what survives? Which side of the line is
  the battle *history* on?
* Baton Pass carries twelve named bits and five named fields. What is the general point about a
  structured handover being a whitelist?
* Why does it matter that the history fields are not on Baton Pass's list either?
* `DEFAULT_STAT_STAGE` is both the never-modified value and the cleared value. What problem is
  that, and who can fix it?
* `truantSwitchInHack` is one field copied back after the struct was zeroed, for **Slaking** and
  **Slakoth** alone. What does its existence tell you about how field lists come to be?
* Natural Cure deletes at the boundary the one thing that normally survives it. What does that say
  about reading a field list as a fact rather than as a decision?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../for-agents/SOURCES-emergency.md`](../../for-agents/SOURCES-emergency.md), and they apply
here. Specific to this answer:

* **The handover standard agreed between the reader's own emergency department and the ambulance
  service that brings patients to it.** This is the document that governs the transfer and it is
  local by nature; no national or international format substitutes for it.
* The current clinical practice guidelines issued by **the ambulance service or national paramedic
  body for the country the reader practises in**, for how the sending side is trained to structure
  what it says.
* The current guidance on safe transfer of care issued by **the reader's own national body for
  clinical guidelines or national patient-safety body**.
* **The human-factors and team-communication material taught on the reader's own resuscitation or
  trauma course**, which is where read-back, the single-speaker convention and the protected
  handover moment are taught.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why a transition loses information and what kind*, written for
someone already trained, and the Pokémon framing covers one idea: a boundary with a declared field
list. It is deliberately not a protocol — it names no handover format, no mnemonic, no field list,
no sequence of actions, no thresholds, no doses and no settings, and it is not something to
consult while acting. Handover formats and the standards attached to them differ between ambulance
services, hospitals and countries, and they are revised. The agreed local standard where the
reader works is the authority; this is not, and it has had no clinical review. Nothing here
describes any real person or any real handover.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. The reset of all six stat stages, the
`status2 = 0` and `gStatuses3 = 0` assignments, the byte-by-byte zeroing of the whole
`DisableStruct`, the clearing of `gLastMoves`, `gLastLandedMoves`, `gLastHitByType`,
`gLastResultingMoves`, `gLastPrintedMoves`, `gLastHitBy` and the `lastTakenMove` arrays, the Baton
Pass whitelists for `status2` and `gStatuses3`, the five fields copied back from
`disableStructCopy`, `isFirstTurn = 2` and the field literally named `truantSwitchInHack` are all
read from `SwitchInClearSetData` in `src/battle_main.c`. Natural Cure being the sole case in
`Cmd_switchoutabilities` is from `src/battle_script_commands.c`, its holders from
`src/data/pokemon/species_info.h`, and Ninjask's Swords Dance at 25, Agility at 38 and Baton Pass
at 45 from `src/data/pokemon/level_up_learnsets.h`. `DEFAULT_STAT_STAGE` being the middle entry of
`gStatStageRatios` is from `src/pokemon.c`. Those are Generation III behaviours; what Baton Pass
carries has been adjusted in later generations as new volatile states were added, so a reader
checking today's list should read today's game. On the clinical side the analysis is long-standing
and that handover is a high-risk transition is settled, while every specific is not: which format,
what its fields are, how long a protected period runs and whether read-back is mandated all differ
by service and country and are revised. Principle dated October 2026; read the agreed local
standard for anything past the principle.
