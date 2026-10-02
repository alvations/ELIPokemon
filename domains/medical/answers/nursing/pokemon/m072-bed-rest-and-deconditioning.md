---
id: "m072"
slug: bed-rest-and-deconditioning
style: pokemon
category: nursing
difficulty: intermediate
question: "Why is bed rest an intervention with its own harms, and why is deconditioning quicker to produce than to reverse?"
tags: [mobility, deconditioning, bed-rest, immobility, early-mobilisation]
---

# Ingrain and Aqua Ring are the same heal. One of them also means you cannot leave.

The expansion's end-of-turn file contains two handlers, written one after the other.
`HandleEndTurnAquaRing` and `HandleEndTurnIngrain` are the same function twice: both skip a
battler already at full HP, both refuse to fire while `healBlockTimer` is running, both compute
`GetNonDynamaxMaxHP(battler) / 16`, both route the result through `GetDrainedBigRootHp` so a **Big
Root** holder gets the same bonus either way, and both hand off to a script whose only difference
is its name. The *only* substantive difference between the two handlers is **which volatile they
read**: one reads `aquaRing`, the other reads `root`.

```
   what the two moves print, in the games' own words
   ──────────────────────────────────────────────────────────────────────────────────
   Aqua Ring   "Forms a veil of water that restores HP."
   Ingrain     "Lays roots that restore HP. The user can't switch out."
   ──────────────────────────────────────────────────────────────────────────────────
   Identical first clause. Identical arithmetic — maxHP/16 per turn, the same
   denominator as LEFTOVERS. Then Ingrain has a second sentence, and the second
   sentence is the entire difference between the two interventions.
```

**Ingrain** is the older of the two: it is in the Advance games, and **Tangela** has it at level
1, **Lileep** at 22, **Cacnea** and **Cacturne** at 25, **Sunkern** at 18 and **Roselia** at 41.
**Aqua Ring** arrives a generation later. So the games got to the restorative-with-immobility
first and the restorative-without-immobility second, which is also the order in which the two were
taken seriously in wards.

## What the root actually costs, and where the code files it

Here is the fact worth the whole answer. In `Cmd_jumpifcantswitch`, the engine asks whether this
battler may be swapped out, and the condition it tests is one expression:

```
   if (gBattleMons[...].status2 & (STATUS2_WRAPPED | STATUS2_ESCAPE_PREVENTION)
       || gStatuses3[...] & STATUS3_ROOTED)
   ────────────────────────────────────────────────────────────────────────────────────
   STATUS2_WRAPPED            set by Wrap, Bind, Fire Spin, Clamp, Whirlpool, Sand Tomb
                              — something the opponent did, which also damages
   STATUS2_ESCAPE_PREVENTION  set by Mean Look, Block, Spider Web
                              — something the opponent did, with no damage at all
   STATUS3_ROOTED             set by Ingrain
                              — something you did to yourself, on purpose, to heal
   ────────────────────────────────────────────────────────────────────────────────────
   Three different causes, three different intentions, ONE conditional. To the engine
   deciding whether this battler can leave, the therapeutic root and Mean Look are the
   same state. m040 uses the binding moves for restraint that injures; this is the
   quieter case next to it — the immobility that was prescribed.
```

And being unable to leave is not neutral in a game built around leaving. Everything on the field
keeps applying: **Spikes**, **Toxic Spikes** and **Stealth Rock** stay on the ground, weather
keeps running, **Leech Seed** keeps draining, a **Perish Song** count keeps falling. The rooted
battler is perfectly safe from everything on the bench and fully exposed to everything in front of
it, and nothing on the screen scores that as a cost.

## The asymmetry: a sixteenth per turn against a half in one

**Ingrain** restores maxHP/16 at the end of each turn. **Super Fang** — the device m006 is built
on — removes half of current HP in a single use. Against a battler at full health those are the
same quantity with different exponents on the clock:

```
   one use of SUPER FANG            maxHP/2 gone, this turn
   to undo it with INGRAIN          maxHP/16 per turn × 8 turns
   ─────────────────────────────────────────────────────────────────────────
   Eight turns of rooting to repay one turn of something else. And the eight
   turns are themselves spent rooted, which is the part the arithmetic does
   not show: the repayment mechanism is the thing that is costing you.
```

That is the whole shape of deconditioning in one line. The loss has one timescale and the recovery
has another, the units are different, and the recovery pathway carries its own ongoing charge.

## Nothing counts the turns, and the code is unusually clear about why

Every comparable state in the Advance games has a counter attached. **Encore** has `encoreTimer`.
**Reflect** and **Light Screen** have `reflectTimer` and `lightscreenTimer`, both set to 5. Sleep
is literally three bits of `status1` holding a number. **Wrap** stores its remaining turns inside
`STATUS2_WRAPPED`.

`STATUS3_ROOTED` is **one bit with no timer**. It does not count down. Nothing decrements it,
nothing prints a message about it after the turn it was set, and `Cmd_trysetroots` *fails
silently* if the root is already there — so using **Ingrain** a second time does not even produce
an event. The state persists until a switch that the state itself prevents.

```
   state              timer?          who ends it
   ─────────────────  ──────────────  ───────────────────────────────────────────
   Encore             3-6 turns       the timer
   Reflect            5 turns         the timer, or Brick Break
   Light Screen       5 turns         the timer, or Brick Break
   Wrap / Bind        turns in-band   the timer
   Ingrain            NONE            a switch, which Ingrain forbids
   ─────────────────────────────────────────────────────────────────────────────
   The only state on this list with no clock is the one somebody chose on purpose.
   There is no prompt, because a prompt is a timer and this does not have one.
```

m038 made the same point about an item nobody asks about again, and m057 to m059 made it about a
setter that refuses to refresh its own clock. This is the third shape of the same defect, and it
is the worst of the three, because here the thing with no review is also the thing blocking the
exit.

## What the alternative looks like, and what it does not fix

**Aqua Ring** is the answer and it is not a magic answer. It gives the identical sixteenth, with
the identical **Big Root** bonus, and it leaves the switch available — which is to say the gain is
entirely in the option it preserves, not in the healing. **Heal Block** still shuts both of them
down and says nothing about why (m039's territory, and m071 uses the same silence). Neither of
them clears a hazard: that is **Rapid Spin**'s job, or **Defog**'s, and it has to be done by
someone. **Macho Brace** — m040's device — is the other half of the trade from the other
direction: an item that builds capacity over time at the price of being slower right now.

## Where the metaphor stops

Nothing above is a person. The rooted battler is a mechanism with a counter missing, not a
patient, and the arithmetic is offered because it is honest about a trade-off, not because the
trade-off is amusing.

The person most harmed by prolonged immobility is often the one least able to object: an older
person admitted for something else, who walked in and leaves unable to manage their own stairs.
The cause is not the illness. It is a fortnight in which it was nobody's specific job to get them
up, and the consequence can be the loss of their home.

The other side deserves the same plainness. Getting someone up carries real risk, needs real
staffing and equipment, and sometimes is simply not what the person wants that morning — and
someone who declines is making a choice, not making an error. The resolution is not to force and
not to leave, but to say the cost of staying in bed out loud, in the same sentence as the risk of
moving. And this is a staffing question as much as a clinical one: telling individual staff to
mobilise more, on a ward where it cannot be done safely with the people present, moves the blame
without moving the patient.

## What Nurse Joy is listening for

Why two handlers that differ by one field name are the right way to see this. What the second
sentence of **Ingrain**'s description costs, itemised. Why the engine files a self-inflicted root
in the same conditional as **Mean Look**. Why a sixteenth per turn and a half per use are not
comparable quantities. Which states in the games carry timers and which do not, and what follows
about review. Why using **Ingrain** twice produces no event at all. And who, on a real ward, owns
the decision that the root comes off — because in the games the answer is nobody, and that is the
defect being pointed at.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to this
answer:

* A current geriatric medicine textbook, for the physiology of immobility, sarcopenia and the
  loss-and-regain asymmetry.
* The reader's national guidance on rehabilitation after critical illness and in the acute
  hospital, for what early mobilisation is taken to mean locally.
* The reader's national stroke guideline, for the very-early-mobilisation question, where trial
  evidence has argued against the most aggressive versions.
* The reader's institutional policy on mobility assessment, moving and handling, and venous
  thromboembolism risk assessment — which carries thresholds this answer deliberately omits.
* The physiotherapy and occupational therapy assessment for any individual, which is the authority
  on what that person should be doing.
* The trial and systematic review literature on early mobilisation in critical care, after surgery
  and after stroke, for the claims the rigorous half marks as setting-dependent.

Separately, and unlike the above: the two end-of-turn handlers and every term they share, the
maxHP/16 fraction, the `GetDrainedBigRootHp` routing, the printed descriptions of **Ingrain** and
**Aqua Ring**, the single conditional in `Cmd_jumpifcantswitch` and the three state bits it tests,
the silent failure of `Cmd_trysetroots` on an existing root, the absence of any timer on
`STATUS3_ROOTED`, the five-turn timers on **Reflect** and **Light Screen**, the three sleep bits
of `status1`, and the level-up levels for **Tangela**, **Lileep**, **Cacnea**, **Cacturne**,
**Sunkern** and **Roselia** were all read directly out of the public disassemblies of the games
and their expansion, which this environment could reach. The eight-turn figure is maxHP/2 divided
by maxHP/16 and is arithmetic, not a number printed anywhere.

## Scope and safety

This explains why immobility is an active harm and why its reversal is slower than its onset, for
someone already training in or qualified for clinical practice. It is not a protocol, not a
decision aid and not a mobility assessment, and it states no rate, no interval and no
thromboprophylaxis threshold, deliberately — the only numbers in it belong to a video game.
Whether a particular person should be mobilised, how, and with how many people is set by local
policy and by the therapy assessment for that person; those are the authority and this is not, and
none of it has had clinical review. Nothing here is for use in an emergency or for a decision
about any person's care, including a decision about whether someone should get out of bed. If
someone is unwell right now, the local emergency number is the correct response.

## Where this stands, October 2026

The physiology is stable and so is the asymmetry. What is live is the dose-response question — how
early, how much, for whom — and it is live in opposite directions in different settings, with the
stroke literature the standing reminder that "as early as possible" is a hypothesis rather than a
principle. The procedural layer dates fastest: mobility documentation, therapy staffing models,
moving-and-handling policy and thromboprophylaxis guidance all differ by country and are revised
on a cycle, and the local policy is the authority for every part of it. The game facts above are
pinned where they belong: **Ingrain** and its conditional are read out of the Advance-generation
code, **Aqua Ring** out of the expansion, and no claim is made here about either in a generation
not named.
