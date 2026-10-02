---
id: "m102"
slug: breathlessness-splits-by-system
style: pokemon
category: emergency
difficulty: intermediate
question: "Why does the differential for breathlessness split by system rather than by severity, and what do the first few observations actually buy?"
tags: [breathlessness, differential, observations, oxygenation, revision]
---

# The bar drops for nine different reasons, and the nine are kept in five different places

At the end of every turn Emerald walks two lists. `DoFieldEndTurnEffects` in `src/battle_util.c`
has ten cases covering the whole field, and `DoBattlerEndTurnEffects` has nineteen covering one
battler at a time. Nine of the cases between them take HP away, and every one of the nine reads a
**different variable**. The bar moving is one observable. Which list it came from, and which store
in that list, is the only thing that determines what would stop it.

## The nine, and where each one lives

```
   what is taking the HP        the fraction         the store it is kept in
   ──────────────────────────────────────────────────────────────────────────────────────
   poison                       maxHP / 8            status1          (survives switching)
   Toxic                        maxHP / 16 × counter status1 + counter (survives switching)
   burn                         maxHP / 8            status1          (survives switching)
   Leech Seed                   maxHP / 8            gStatuses3       (cleared by switching)
   Curse                        maxHP / 4            status2          (cleared by switching)
   Nightmare                    maxHP / 4            status2          (cleared by switching)
   Wrap, Bind, Fire Spin,       maxHP / 16           status2 + wrappedBy
     Clamp, Whirlpool
   Sandstorm                    maxHP / 16           gBattleWeather   (whole field, both sides)
   Hail                         maxHP / 16           gBattleWeather   (whole field, both sides)
   ── and on the way in, not at the end of the turn ──
   Spikes, one to three layers  maxHP / 8, / 6, / 4  gSideStatuses    (belongs to the side)
   ──────────────────────────────────────────────────────────────────────────────────────
     ONE observable: the bar is shorter than it was. Nothing about the amount
     identifies the store, and the counter for one store does nothing to any other.
```

The last column is the whole argument. Switching out zeroes `status2` and leaves `status1`
untouched; Rapid Spin reaches `gStatuses3` and `gSideStatuses` and cannot touch either of the
others; an Antidote reaches exactly one bit of `status1` and nothing else, which is question
m003's device. Severity is in the bar. The answer is in the store.

## Three things the screen shows, and how far they get you

`UpdateStatusIconInHealthbox` in `src/battle_interface.c` reads `MON_DATA_STATUS` — that is
`status1`, and nothing else — and chooses between exactly five graphics: sleep, poison, burn,
freeze, paralysis. Poison and Toxic get the **same** icon, which is the convention questions m024
and m054 are built on. So the readable screen is three partitions:

* **the status icon**, which covers one of the five stores and collapses two of its cases;
* **the health bar**, which is 48 pixels of how much and zero pixels of why — question m029's
  point, and it never renders empty while anything is left;
* **the weather animation**, which covers `gBattleWeather` and is the only one of the field
  effects you can see without reading memory.

Cross those three and you have cut the list of nine down a long way for nothing spent. What you
have not done is name the cause, and four of the nine are **invisible to all three**: Leech Seed,
Curse, Wrap and Spikes draw no icon at all in Generation III. A player who treats a clear status
box as an empty one has made the error that question m070 calls the missing pertinent negative.

The script language admits the same split. There is a purpose-built instruction per store —
`jumpifstatus` for `status1`, `jumpifstatus2` for `status2`, `jumpifstatus3condition` for
`gStatuses3`, `jumpifsideaffecting` for `gSideStatuses` — and for weather there is no dedicated
instruction at all: Solar Beam's script reads the raw halfword, `jumpifhalfword CMP_COMMON_BITS,
gBattleWeather, B_WEATHER_SUN`. Five stores, four questions and one raw memory read. You cannot
ask one question that covers them.

## Every one of those fractions is a fraction of max HP

Each entry in the table is a proportion, and a proportion is not a quantity. One eighth of
Blissey's bar — base 255, the largest in the game — and one eighth of Shedinja's are the same
fraction and nothing like the same number. Shedinja's maximum HP is literally 1, so `maxHP / 8`
evaluates to zero, and then this runs:

```
   gBattleMoveDamage = gBattleMons[battler].maxHP / 8;
   if (gBattleMoveDamage == 0)
       gBattleMoveDamage = 1;
```

The floor turns one eighth into the entire bar. That is question m006's Super Fang distinction
with a different numerator, and question m064's observation that three separate routines in this
one game refuse to report zero.

And the direction can cancel. **Leftovers** restores `maxHP / 16` at the end of the turn, with the
same floor and the same denominator as Sandstorm. A Pokémon holding Leftovers in a sandstorm has
two live processes and a bar that does not move — which is question m034's whole subject, and the
reason a stable number is not the same thing as a stable state.

## The counter that is changing while the output is not

`ENDTURN_BAD_POISON` computes `maxHP / 16` and then multiplies it by the counter held in the upper
bits of `status1`. On the first turn that makes Toxic **half** of ordinary poison: the
milder-looking reading is the dangerous trajectory, and both draw the identical PSN graphic. By
the time the two readings cross, several turns of counter have already accumulated.

So the same number means different things depending which way it is travelling, and the single
reading cannot tell you which. The counter is the finding and it is not displayed anywhere.

## Several at once, and each needing its own removal

`Cmd_rapidspinfree` in `src/battle_script_commands.c` is an `else if` chain, and it clears
**exactly one thing per use**, in a written order:

```
   if      (status2 & STATUS2_WRAPPED)        -> free from Wrap, and stop
   else if (gStatuses3 & STATUS3_LEECHSEED)   -> clear Leech Seed, and stop
   else if (gSideStatuses & SIDE_STATUS_SPIKES) -> clear ALL Spikes layers, and stop
   else                                       -> do nothing
```

Three stores, one instruction, one effect. A Starmie that knows Rapid Spin from level 1, or a
Hitmontop that learns it at 25, spinning out of Wrap has done nothing whatever about the Leech
Seed or the Spikes, and the bar going down less afterwards is weak evidence about how many
processes are running. Question m045 reads the same routine for the same reason.

Two of the nine are also outside the chain altogether: nothing Rapid Spin does touches a burn, and
switching out — which zeroes `status2` wholesale, as question m070's `SwitchInClearSetData` shows
— leaves `status1` and the side's Spikes exactly where they were.

## Severity and mechanism are two different reads

`GetScaledHPFraction(hp, maxHP, 48)` turns the HP into pixels, and 48 pixels is the entire
vocabulary the bar has. It is a good severity read: it tells you how much is gone and roughly how
fast. It contains no information at all about which of five stores to look in, and no amount of
staring at it produces any. The two reads are taken from different places and written down
separately, and an answer that collapses them into one number has thrown away the half that
determines the treatment.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is a person who cannot get their
breath.

Breathlessness is the sensation produced when the drive to breathe and what breathing achieves do
not match, and the mismatch can be produced at any link of a chain: the drive and the bellows, the
upper airway, the lower airways, the alveoli and the pleural space, the carriage of oxygen in the
blood, and the pump that moves it. **(Mechanism.)** The differential is drawn by locus because
treatment is specific to locus; severity governs how fast to move and says nothing about which
link is broken. Two of the loci produce breathlessness with structurally normal lungs — too little
carrier, or a carrier occupied by something else — and a metabolic acid load produces fast deep
breathing in a respiratory system that is working correctly. **(Consensus.)**

The first few observations buy a partition rather than a diagnosis. The pattern of breathing and
whether a sentence can be completed separate a problem of the path from a problem of the supply;
whether findings are symmetrical, and whether a noise exists and where in the cycle it falls,
separate a one-sided mechanical cause from a diffuse one, and a noise disappearing is not an
improvement unless the work of breathing fell with it; and pulse oximetry reports the *proportion*
of available carrier that is carrying oxygen, so it is blind to how much carrier there is and
cannot distinguish a carrier occupied by carbon monoxide — the reading can be normal or high in
carbon monoxide poisoning, which is a property of the measurement and not a fault in it.
**(Consensus;** the device and confirmatory test used instead are **country-dependent.)** A rising
rate and a falling rate in the same person mean opposite things, and a slowing rate in someone who
was breathing fast may be the point at which the work can no longer be sustained. **(Consensus.)**
People have more than one organ, so two producers at once is ordinary, and a partial response to a
treatment aimed at one is weak evidence about mechanism.

No Pokémon stands for a patient anywhere in this answer, nothing in the game represents a person,
a symptom, a lung or an outcome, and no part of it is a sequence of actions. The game is carrying
two ideas: that one observable can be produced in several independent places, each with its own
non-interchangeable remedy, and that a proportion is not a quantity. What is at stake when the
breathing belongs to a person — that fear raises the drive and the drive raises the work, that
their own report of being worse than usual is the earliest signal available and is routinely
discounted, and that someone who has lived with the condition knows the shape of their own
deterioration better than a stranger meeting them for the first time — is stated here without
ornament, and it is not a mechanic.

## What a Gym Leader is listening for

* Nine end-of-turn effects take HP. Name four and say which store each is kept in.
* Which removal reaches which store? Say what Rapid Spin cannot touch, and what switching out
  cannot touch.
* The status icon reads one variable and chooses between five graphics. Which four of the nine are
  invisible to it?
* One eighth of Blissey's bar and one eighth of Shedinja's. Why are those the same fraction and
  not the same fact?
* Leftovers and Sandstorm share a denominator. What does the bar do, and what is happening?
* Toxic is half of ordinary poison on turn one and draws the same icon. What is the general
  lesson?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* The current acute oxygen and acute breathlessness guidance issued by **the national respiratory
  or thoracic society for the country the reader practises in**, for targets, devices and every
  threshold.
* The current guidance on pulse oximetry and its limitations issued by **the reader's national
  anaesthetic, respiratory or patient-safety body**, for where the measurement is unreliable and
  what is used instead.
* A current standard textbook of **emergency medicine** or of **respiratory medicine**, for the
  differential by system and for the physiology of the sensation.
* **The reader's own employing organisation's** escalation policy and observation-chart
  documentation, which governs practice where they work and outranks every general account
  including this one.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *how a differential is organised and what cheap observations are
worth*, written for someone already trained, and the Pokémon framing covers the structure of the
inference and nothing else. It is deliberately not a protocol: no sequence of actions, no oxygen
target, no device, no setting, no rate, no threshold, no drug, no dose, and nothing to consult
while assessing anyone. Oxygen guidance, escalation thresholds and chart wording differ between
national societies and between institutions and are revised. The reader's own society guidance and
local policy are the authority; this is not, and it has had no clinical review. Nothing here
describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. The ten field cases and nineteen battler
cases, the fractions for poison, burn and Leech Seed at maxHP/8, Toxic at maxHP/16 times the
counter held in `status1`, Curse and Nightmare at maxHP/4, the partial-trapping family at
maxHP/16, Sandstorm and Hail at maxHP/16 with their type exemptions, Leftovers at maxHP/16, and
the floor that turns a computed zero into 1 are all read from `src/battle_util.c`;
`Cmd_rapidspinfree`'s three-store `else if` chain and the Spikes formula `maxHP / ((5 - layers) *
2)` from `src/battle_script_commands.c`; the five status graphics and their single source in
`MON_DATA_STATUS` from `src/battle_interface.c`; the per-store jump instructions and Solar Beam's
raw weather read from `src/battle_script_commands.c` and `data/battle_scripts_1.s`; Blissey's base
255 and Shedinja's maximum of 1 from `src/data/pokemon/species_info.h`; and Starmie's Rapid Spin
at level 1 and Hitmontop's at 25 from `src/data/pokemon/level_up_learnsets.h`. Those are
Generation III behaviours — Sandstorm's Special Defence boost for Rock types and several of these
fractions are later changes — so a reader checking today's game should read today's game. On the
clinical side the structural argument is long-standing and the specifics are not: oxygen targets
have changed more than once and still differ between societies, the confirmatory tests used where
oximetry is unreliable are institutional, and chart wording and trigger points vary by country and
hospital. Principle dated October 2026; read the current guidance for anything past the principle.
