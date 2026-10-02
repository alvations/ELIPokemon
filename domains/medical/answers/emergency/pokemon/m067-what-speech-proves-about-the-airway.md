---
id: "m067"
slug: what-speech-proves-about-the-airway
style: pokemon
category: emergency
difficulty: intermediate
question: "Why does whether someone can talk carry so much information about the airway, and what exactly does a normal voice rule out and fail to rule out?"
tags: [airway, assessment, information-value, asymmetry, revision]
---

# The move went off, so fourteen checks and nine more cleared, and the game told you with one word

Every move script in Emerald begins with the same command. `attackcanceler`, the first instruction
in `BattleScript_EffectHit` and in almost everything else in `data/battle_scripts_1.s`, and
getting past it is the single cheapest piece of information in a battle. It is cheap because it
costs nothing to observe — the move either happened or it did not — and it is valuable because
what it clears is a **conjunction**, and a conjunction that comes out true tells you about every
term in it at once.

Read `Cmd_attackcanceler` in `src/battle_script_commands.c` and then `AtkCanceler_UnableToUseMove`
in `src/battle_util.c`. Between them, the move actually going off establishes all of the following
were simultaneously true at that instant.

## The conjunction, in the order the engine evaluates it

Each row below is a real condition with a real cause and, where one exists, a real counter. The
engine evaluates them top to bottom.

```
   Cmd_attackcanceler, in order    what typically put it there       what answers that one
   ────────────────────────────────────────────────────────────────────────────────────────────
   the battle is not over          —                                 —
   the attacker is on the field    —                                 —
   ── AtkCanceler_UnableToUseMove: fourteen cases, in this order ──
     CANCELER_FLAGS      Destiny Bond and Grudge cleared off the attacker
     CANCELER_ASLEEP     Parasect's Spore, 100 accuracy    Chesto Berry; Early Bird; Vital Spirit
     CANCELER_FROZEN     Ice Beam, Blizzard                Aspear Berry; Flame Wheel; Magma Armor
     CANCELER_TRUANT     being Slaking                     nothing at all
     CANCELER_RECHARGE   Hyper Beam, 150 power, 5 PP       nothing; it is the price of the move
     CANCELER_FLINCH     Fake Out, Rock Slide, King's Rock Inner Focus; it lasts one turn anyway
     CANCELER_DISABLED   Disable, 55 accuracy              choosing another move; waiting
     CANCELER_TAUNTED    Taunt, plus a zero-power move     choosing a move with power; waiting
     CANCELER_IMPRISONED Imprison                          a move the opponent does not know
     CANCELER_CONFUSED   Confuse Ray; Swagger at 90        Persim Berry; Own Tempo on Spinda
     CANCELER_PARALYZED  Thunder Wave, 100 accuracy        Cheri Berry; Limber on Persian
     CANCELER_IN_LOVE    Attract, 100 accuracy             Mental Herb; Oblivious on Wailord
     CANCELER_BIDE       Bide                              waiting it out
     CANCELER_THAW       (the unfreeze-by-own-move case)
   ── and back in Cmd_attackcanceler ──
   no ability blocked it           Soundproof on Exploud; Damp on Quagsire
   there was PP left               a Leppa Berry would have restored 10
   it obeyed                       IsMonDisobedient, gated on badges
   not bounced                     Magic Coat, FLAG_MAGIC_COAT_AFFECTED
   not stolen                      Snatch, FLAG_SNATCH_AFFECTED
   not redirected                  Lightning Rod on Rhydon or Manectric
   not stopped                     Protect, Detect, DEFENDER_IS_PROTECTED
   ────────────────────────────────────────────────────────────────────────────────────────────
     ONE observable: the attack string printed and the move resolved.
     True  ⇒ every row above held, at that moment.
     False ⇒ one row failed — and the loop stopped at the first one.
```

Twenty-odd conditions, one output. That is the structural reason a single cheap observation can be
worth more than an expensive one: nothing about the observation is clever, and the yield comes
from the length of the conjunction behind it.

## The asymmetry, and the loop that creates it

The `do ... while` at the bottom of `AtkCanceler_UnableToUseMove` runs `while
(gBattleStruct->atkCancelerTracker != CANCELER_END && effect == 0)`. It **stops at the first thing
that fired**. Nothing after that case is evaluated at all.

So the two outcomes are not mirror images. A move that resolves has been through every case and
cleared it. A move that did not resolve cleared only the cases before the one that stopped it, and
everything after is simply unknown — a Pokémon stopped at `CANCELER_ASLEEP` has not been checked
for Disable, for PP, for Taunt, or for anything else below. One word of output on the positive
side covers twenty conditions; the negative side covers one condition and leaves the rest dark.

The game is generous in a way reality is not, and this is the place to say so plainly rather than
later: when a move fails, Emerald *prints which check caught it*. There is a dedicated script per
case — `BattleScript_MoveUsedIsAsleep`, `BattleScript_MoveUsedFlinched`,
`BattleScript_MoveUsedIsParalyzed`, `BattleScript_MoveUsedIsDisabled` and so on, each with its own
message. No such label exists outside the game. The mechanic worth taking is the asymmetry of the
conjunction; the free diagnosis attached to the failure is a convenience of the engine and not a
feature of anything else.

## It is a statement about this turn only

The three rolls in the chain are re-rolled every single time, and they are the reason a pass
cannot be extrapolated forward.

* **Paralysis** is `(Random() % 4) == 0`, evaluated fresh at `CANCELER_PARALYZED` on every
  attempt. A move going off this turn changes nothing about next turn's roll.
* **Freeze** thaws on `Random() % 5` and otherwise stops the move; the status is still there on a
  turn where it happened not to fire.
* **Confusion** is `Random() & 1`, and on the losing half the Pokémon takes a typeless 40-power
  calculation against itself instead of acting.

And the state underneath can move while the output does not. The sleep counter in `status1` is
decremented inside `CANCELER_ASLEEP` on every attempt — by one, or by two if the ability is
**Early Bird** — so the same observable outcome sits on top of a quantity that is changing turn by
turn. A conjunction that held a moment ago is not a conjunction that holds now, and in a system
with counters and per-turn rolls the only honest reading of a pass is *at that instant*.

## The quality of the output, not just its presence

Emerald does make one gradation available, and it is the closest thing the engine has to the
difference between a clear voice and a strained one. A move can resolve and still be visibly
degraded: a Pokémon under **Taunt** can only use something with non-zero power, so what it does is
constrained before you see it; a Pokémon with one move **Disabled** has had its options narrowed
without any message appearing on the turn it chooses another; and `gProtectStructs` carries
`flinchImmobility`, `prlzImmobility` and `loveImmobility`, separate flags recording *which* kind
of failure happened, used later rather than displayed. The engine stores a more specific record
than it shows. What is displayed is the coarse pass or fail; what is kept is the detail.

## Where the metaphor stops

Plain prose from here, with no game in it, because this part is about a person being asked a
question.

A normal, fully formed, unlaboured sentence requires all of the following to be true at once: a
path from the mouth or nose down to the larynx that is not obstructed; air actually moving out
through it in sufficient volume; cords that can be brought together and set vibrating; surrounding
structures not so swollen or displaced that shaping is impossible; coordinated neuromuscular
control; a brain perfused and awake enough to intend an utterance; and enough respiratory reserve
that breath can be spent on speech rather than hoarded. Because every item must hold, one normal
sentence clears all of them — and because a false conjunction says only that some term failed, an
abnormal or absent voice is weakly informative and highly alarming. Silence is not reassurance; a
completely obstructed airway is silent. That is **mechanism**, checkable by reasoning.

Three qualifications matter more than the elegance of the argument. It is a statement about one
moment and never a prediction, which is why the question is asked again rather than ticked —
swelling, bleeding into a confined space and a continuing exposure can all let it hold now and
fail shortly. It says little about gas exchange below that path, so someone can speak normally
while oxygenating badly. And the test can be *unavailable* rather than failed — in the very young,
where no language is shared, where speech is affected at baseline, or where someone is sedated —
and treating unavailable as either passed or failed is an error in both directions. **(Consensus**
that the quality of the voice localises the problem and that patient-reported deterioration is
under-weighted; **country-dependent** for the vocabulary and for every threshold, none of which is
stated here.**)**

No Pokémon stands for a patient anywhere in this answer, nothing in the game represents a person,
an airway or an outcome, and no part of it is a sequence of actions. The game is carrying one
idea: that a cheap observation can be worth a great deal when what sits behind it is a long
conjunction, and that the value collapses asymmetrically when the observation is abnormal. What is
at stake when the conjunction belongs to a person is stated above without ornament, and it is not
a mechanic.

## What a Gym Leader is listening for

* What does getting past `attackcanceler` establish, and roughly how many conditions is that?
* Why does the `do ... while` loop stopping at the first firing case make the positive and
  negative results so unequal?
* Paralysis is re-rolled every turn. What does that mean about extrapolating a successful move
  forward?
* The sleep counter changes on a turn where the move still goes off. What is the general lesson
  there about an unchanged output?
* Emerald prints which check caught a failed move. Why is that the part of the analogy to throw
  away?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../for-agents/SOURCES-emergency.md`](../../for-agents/SOURCES-emergency.md), and they apply
here. Specific to this answer:

* The current adult and paediatric life support guidelines issued by **the national resuscitation
  council for the country the reader practises in**, for how the airway assessment is worded and
  ordered. There is no single global document and the councils differ.
* The current difficult-airway guidance issued by **the reader's national anaesthetic or
  airway-management society**, which is where the assessment of a threatened airway and its
  vocabulary live.
* A current standard textbook of **emergency medicine**, for the physiology of phonation and for
  what an altered voice localises.
* **The reader's own employing organisation's** airway and escalation policy, which governs
  practice where they work and outranks every general account including this one.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why one observation carries information*, written for someone
already trained, and the Pokémon framing covers the shape of the conjunction and nothing else. It
is deliberately not a protocol: no sequence of actions, no airway manoeuvre, no equipment, no
rates, no doses, no settings, no thresholds, and nothing to consult while acting. Airway
assessment wording and escalation thresholds differ between national councils, specialty societies
and institutions, and they are revised. The reader's own council, society and local policy are the
authority; this is not, and it has had no clinical review. Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. The fourteen-case cancel chain, its order,
the `effect == 0` short-circuit, the 1-in-4 paralysis roll, the 1-in-5 thaw, the 1-in-2 confusion
flip with its typeless 40-power self-hit, the Early Bird double decrement and the per-case message
scripts are all read from `AtkCanceler_UnableToUseMove` in `src/battle_util.c`; the surrounding
checks — zero HP, ability blocks, PP, the obedience check, Magic Coat, Snatch, Lightning Rod and
Protect — from `Cmd_attackcanceler` in `src/battle_script_commands.c`; the `flinchImmobility`,
`prlzImmobility` and `loveImmobility` flags from the same file; and `attackcanceler` opening the
shared hit script from `data/battle_scripts_1.s`. Those are Generation III behaviours; the cancel
order and several of the probabilities have been changed in later generations, so a reader
checking today's game should read today's game. On the clinical side the informational argument is
long-standing and the specifics are not: the wording of the airway assessment, the list of warning
features and every threshold vary by council and society and move with each revision. Principle
dated October 2026; read the current documents for anything past the principle.
