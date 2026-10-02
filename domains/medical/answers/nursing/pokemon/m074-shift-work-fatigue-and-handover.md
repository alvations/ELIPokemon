---
id: "m074"
slug: shift-work-fatigue-and-handover
style: pokemon
category: nursing
difficulty: advanced
question: "Why is fatigue treated as a safety factor rather than a personal failing, and what makes the handover at the end of a night shift the most dangerous one?"
tags: [fatigue, shift-work, circadian, handover, human-factors]
---

# There is no tiredness bit. The status word has room for six things and this is not one of them.

Open `include/constants/battle.h` and `STATUS1_ANY` is defined as the union of exactly six named
conditions — sleep, poison, burn, freeze, paralysis and bad poison. That is the complete list of
things the games will put an icon on. **Tiredness is not in it, and there is no unused bit waiting
for it either.** Everything below follows from a system that models the state it cannot measure as
"nothing is wrong".

What the word *does* hold is more interesting than that absence:

```
   STATUS1_SLEEP   (1 << 0 | 1 << 1 | 1 << 2)   // First 3 bits (Number of turns to sleep)
   ─────────────────────────────────────────────────────────────────────────────────────────
   Sleep is not a flag. It is a COUNTER, three bits wide, living in the same word as
   poison and burn — a quantity, with a value, that has to be discharged. The icon
   shows you that it is non-zero. The icon does not show you the number.
   ─────────────────────────────────────────────────────────────────────────────────────────
   And the header's two comments are the whole handover problem in fourteen words:

     status1  "These persist outside of battle and after switching out."
     status2  "They are removed after exiting the battle or switching out."

   Every volatile state is wiped at the boundary. The sleep counter is one of the few
   things that CROSSES it — and it is the thing nobody hands over.
```

## The counter runs down by trying to act, not by time passing

This is the detail that makes the mapping exact rather than decorative. The decrement does not
live in an end-of-turn routine. It lives inside `AtkCanceler_UnableToUseMove`, the fourteen-case
chain m067 is built on, reached at the moment the battler attempts a move:

```
   u8 toSub;
   if (ability == ABILITY_EARLY_BIRD) toSub = 2; else toSub = 1;
   ... status1 -= toSub ...
   ──────────────────────────────────────────────────────────────────────────────────────
   Two consequences, both of them real on a ward.

   ONE. The clock only advances when you try to work. A turn spent attempting
   something is the only thing that pays down the debt, and the attempt fails. The
   cost is charged and no work is produced.

   TWO. EARLY BIRD subtracts 2 instead of 1. Read what that is and is not: it does
   not abolish the requirement, it does not let the holder act while the counter is
   above zero, and it is an ABILITY — a standing property of the species, not a
   choice, not a technique, and not something anyone can decide to have.
```

## What you can still do while the counter is non-zero: two moves, and both are degraded

The code is blunt about it. The branch that keeps a sleeping battler from acting carries one
exception: `if (gCurrentMove != MOVE_SNORE && gCurrentMove != MOVE_SLEEP_TALK)`. Two moves. That
is the entire permitted repertoire.

```
   move         what it is                                 what it costs
   ───────────  ─────────────────────────────────────────  ───────────────────────────────
   Snore        base power 40, accuracy 100, PP 15, with   40. For comparison, Hyper Beam
                a 30 per cent flinch chance                is 150 and Brick Break is 75.
                                                           Output is about a quarter of a
                                                           real attack, and the useful part
                                                           of it is a coin-flip
   Sleep Talk   picks one of the user's other moves AT      you do not choose. The
                RANDOM and uses it                          selection is made for you, and
                                                            it can be the wrong one
   ─────────────────────────────────────────────────────────────────────────────────────────
   And Snore FAILS OUTRIGHT if the user is not asleep: its script jumps to
   BattleScript_ButItFailed unless STATUS1_SLEEP is set. The workaround for working while
   impaired is not available to anyone who is not impaired. Sleep Talk's random pick runs
   through the same CheckMoveLimitations that m071's Encore list lives in, and it excludes
   Focus Punch, Uproar and every two-turn move before it draws.

   Working through it is implemented. It is implemented as low output, or as output you
   did not select. m043 uses Snorlax learning Rest at 28 and Snore at the same level 28 for
   adherence; the fact doing work here is that the two were put in at once, as a pair,
   because the designers understood that the restorative and the working-while-impaired
   workaround belong to the same problem.
```

## Yawn: the sleep that was decided two turns ago

**Snorlax** learns **Yawn** at level 24, four levels before **Rest**. `Cmd_setyawn` does not cause
sleep. It sets a **two-turn** counter in `gStatuses3`, and at the end of the turn that counter
reaches zero the engine checks that nothing else is in `status1`, that the ability is not
**Insomnia** or **Vital Spirit**, and that no **Uproar** is running — and then calls
`CancelMultiTurnMoves` and sets sleep for `(Random() & 3) + 2`, two to five turns.

Two things in that sequence are worth sitting with. The sleep **was already decided**; the counter
was set before anything looked drowsy. And `CancelMultiTurnMoves` is the same routine m071 is
built on: whatever multi-turn sequence was running is terminated and its counter returns to zero.
The microsleep does not merely cost the turn it happens in. It cancels the chain.

## The handover at the worst hour: Helping Hand checks the format, not the need

**Helping Hand** has priority 5 — it is designed to go first, before anything it is meant to
support. And `Cmd_trysethelpinghand` reads like this:

```
   gBattlerTarget = the partner's position;
   if (gBattleTypeFlags & BATTLE_TYPE_DOUBLE
       && the partner is not absent
       && neither battler has already used it)   -> it works
   else                                           -> BattleScript_ButItFailed
   ──────────────────────────────────────────────────────────────────────────────────────
   The FIRST condition is the battle format. In a single battle the move fails outright,
   every time, with no partial effect and no message explaining the structural reason.
   It does not fail because the user was insufficiently willing. It fails because there
   is nobody in the other slot.
   ─────────────────────────────────────────────────────────────────────────────────────
   And look at what else only exists with a partner: Follow Me and Rage Powder, which
   redirect an attack away from an ally. Three of the games' cooperative moves, all of
   them unavailable in exactly the format where one battler faces everything alone.
```

m002 covers what a handover is doing and m070 covers what crosses a boundary. The point here is
narrower: **the mechanisms that let one party cover for another are gated on a second party
existing**, and that gate is checked against the format rather than against how much help is
needed. Overnight the format changes. Nothing in the check knows that.

And the state that does cross the boundary is the one with no icon of its own. **Truant** — m001's
device — is the purest form: **Slaking** acts on alternate turns, which is a halving of output
written into the species, and nothing on the summary screen says so. A rota is a **Truant** you
cannot read off the sheet.

## Rest: the one full restoration, and every way it refuses

**Rest** is the games' only complete recovery, and the Advance code makes its terms explicit.
`Cmd_trysetrest` executes `gBattleMons[...].status1 = STATUS1_SLEEP_TURN(3)` — an **assignment**,
not an OR, so poison, burn, freeze and paralysis are all wiped in the same instruction. Total
restoration. The price is in the same line: **exactly three turns** of the counter, during which
the only options are **Snore** and **Sleep Talk**.

Then read the script in order, because the refusals are the interesting part:

```
   BattleScript_EffectRest::
     jumpifstatus BS_ATTACKER, STATUS1_SLEEP, ...RestIsAlreadyAsleep
     jumpifcantmakeasleep ...............................RestCantSleep
     trysetrest .........................................AlreadyAtFullHp
   ──────────────────────────────────────────────────────────────────────────────────────
   Rest FAILS if:
     * the battler is already asleep;
     * an UPROAR is running anywhere on the field — Uproar wakes every sleeping
       battler on BOTH sides, every turn, unless its ability is Soundproof;
     * the ability is INSOMNIA or VITAL SPIRIT;
     * HP is already full.
   ─────────────────────────────────────────────────────────────────────────────────────
   The third line is the one worth the whole section. The ability whose entire effect is
   "cannot be put to sleep" also makes the only full restoration in the game fail. The
   thing that keeps you awake is the thing that stops you recovering, and the game
   implements it as one check against one ability.
```

**Uproar** is the environmental version of the same point, and it is checked for every battler on
the field rather than for the one making the noise. Daytime is an **Uproar**. **Soundproof** is
one species-level ability and there is no item that grants it.

## Where the metaphor stops

A status word with no bit for tiredness is a fair picture of a performance variable with no
readout, and nothing above is a person.

This question is unusual in the set because the person harmed is often the staff member. Long-term
shift work is associated with real health effects and with effects on family life that appear in
no incident report, and someone who drives home after twelve hours and a night without breaks is
taking a risk nobody has assessed.

It lands on patients too, and unevenly. A person who deteriorates at four in the morning is cared
for by the fewest and most tired people of the day, and their deterioration has to be noticed by
exactly the faculty that fails first. That is not an argument for pessimism; it is the argument
for why thresholds, escalation criteria and checklists exist. They are the parts of the system
that do not get tired.

And it must be said: someone who makes a mistake at the end of a long night and is treated as the
cause of it will not report the next one. The reporting that makes a rota's pattern visible
depends on the error being treated as a property of the shift. An institution unable to do that
loses the data it would need to fix the rota.

## What Nurse Joy is listening for

Why a state with no bit is managed differently from a state with an icon. What it means that the
sleep counter is three bits and the icon shows only that it is non-zero. Why a counter that only
decrements on an attempt is a worse deal than it looks. What **Early Bird** does and does not
change, and why "it is an Ability" is the important part. Why the entire permitted repertoire
while asleep is base power 40 and a random selection. What `CancelMultiTurnMoves` costs a sequence
that was four-fifths finished. Why **Helping Hand** checks the format and not the need. And which
ability makes **Rest** fail — because that is the sentence worth carrying out of this answer.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to this
answer:

* The reader's national occupational health and safety body's guidance on shift work and fatigue,
  for the risk-management framing and the employer duties.
* The reader's own working-time regulations or collective agreement, for shift length, consecutive
  nights, rest periods and breaks. This is law or contract, it differs by country, and it is the
  authority for every number this answer declines to give.
* The reader's institutional fatigue risk management policy and night-shift and napping policy.
* The reader's professional body's position statements on safe staffing and on fatigue.
* A current textbook of sleep medicine or of human factors in healthcare, for the circadian,
  homeostatic and time-on-task model and for the order in which capacities fail.
* The published literature on shift work and long-term health outcomes, and on the road-traffic
  risk of the post-shift commute — both observational, with the magnitude contested.
* The handover literature, for the content most likely to be omitted under time pressure.

Separately, and unlike the above: the six conditions in `STATUS1_ANY`, the three sleep bits and
the header comment naming them a turn count, the two header comments on persistence across a
switch, the decrement living inside `AtkCanceler_UnableToUseMove` with **Early Bird** subtracting
2, the **Snore**-and-**Sleep Talk** exception, **Snore**'s base power 40, accuracy 100, PP 15 and
30 per cent flinch chance, its refusal to work on a battler that is awake, **Sleep Talk**'s random
draw and its exclusions, **Hyper Beam**'s 150 and **Brick Break**'s 75, **Yawn**'s two-turn
counter and its four conditions and its call to `CancelMultiTurnMoves`, the 2-to-5-turn sleep it
sets, **Snorlax**'s **Yawn** at 24 and **Rest** and **Snore** both at 28, **Rest**'s single
assignment of a three-turn counter and all four of its failure paths, **Uproar** waking every
sleeping battler unless **Soundproof**, and **Helping Hand**'s priority of 5 and its battle-format
condition were all read directly out of the public disassemblies of the games, which this
environment could reach.

## Scope and safety

This explains why fatigue is managed as a system property, for someone already training in or
qualified for clinical practice. It is not a protocol, not a fatigue risk assessment and not
advice about anyone's own working pattern, sleep or health, and it deliberately states no shift
length, no number of consecutive nights, no rest interval and no nap duration — those are set by
law, negotiated agreement and local policy, which are the authority, and the only numbers here
belong to a video game. It is not occupational health advice and has had no clinical or legal
review. Anyone whose own sleep, health or safety at work is affected needs their occupational
health service and their own clinician, not a revision note. Nothing here is for use in an
emergency; if someone is unwell right now, the local emergency number is the correct response.

## Where this stands, October 2026

The physiology is stable and old, and the order in which capacities fail is not in dispute at the
level stated. What moves is everything around it: working-time law and the regulatory treatment of
fatigue as an employer duty differ sharply by country and change with legislation; institutional
napping policy is changing in several health systems and in opposite directions; and the long-term
health effects of shift work are an active observational literature where the direction is agreed
and the magnitude is not. The reader's own regulations and local policy are the authority
throughout. The game facts above are pinned to the Advance-generation disassembly, and nothing is
claimed here about how **Rest**, **Yawn** or **Helping Hand** behave in any other generation.
