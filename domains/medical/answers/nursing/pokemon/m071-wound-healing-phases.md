---
id: "m071"
slug: wound-healing-phases
style: pokemon
category: nursing
difficulty: intermediate
question: "Why is wound healing described as a sequence of overlapping phases, and what does it mean to say that a wound is stuck?"
tags: [wound-healing, inflammation, debridement, assessment, chronic-wounds]
---

# Rollout is a five-turn programme, and one miss sends the counter back to zero.

**Rollout** has a base power of 30 and a printed accuracy of 90. What it does not have is a flat
output. `Cmd_rolloutdamagecalculation` sets a timer of 5 on the first hit and then doubles the
base power once for every turn already elapsed, so the chain is not five uses of a 30-power move —
it is one escalating programme:

```
   turn   rolloutTimer   doublings   base power   base power with DEFENSE CURL set
   ─────  ─────────────  ──────────  ───────────  ────────────────────────────────
     1          4             0           30                    60
     2          3             1           60                   120
     3          2             2          120                   240
     4          1             3          240                   480
     5          0             4          480                   960
   ──────────────────────────────────────────────────────────────────────────────
   Each row needs the row above it to have happened. The power on turn four is not a
   property of turn four; it is the record of turns one to three.
```

**Donphan** learns **Defense Curl** at level 9 and **Rollout** at level 33 — the precondition
arrives twenty-four levels before the move it multiplies, and nothing in **Rollout**'s own entry
mentions it. **Miltank** has the same pair at 8 and 34. The doubling is read off
`STATUS2_DEFENSE_CURL`, a single bit set earlier by a different move. That is what a phase is: an
earlier step whose only product is the conditions for a later one.

Now the part that makes this a wound-care analogy rather than a curiosity. **If the chain breaks,
it does not pause.** On a miss the code calls `CancelMultiTurnMoves`, which sets `rolloutTimer`
back to **0**, and the next **Rollout** starts again at 30. At the printed 90 accuracy, the chance
that all five connect is 0.9 to the fifth power — a little under three in five, from the game's
own figure and no other. The same shape is in **Fury Cutter**: base 10, a counter that caps at 5,
and `Cmd_furycuttercalc` resetting that counter to **0** on any miss. **Scyther** and **Scizor**
both learn it at level 46.

## The overlap, and why one target can be in two states at once

The sequence is not the only thing running. While a **Rollout** chain is building,
`STATUS2_MULTIPLETURNS` is set, a **Leftovers** holder is still taking its sixteenth back at the
end of every turn, `rolloutTimer` is counting down, and an **Encore** timer may be running on the
other side. Four clocks, one position. Nothing in the games forces them into phase, and reading
only the loudest one tells you about the loudest one.

## Encore is the arrest, and it is filed with the other locks

**Encore** is the cleanest model of a process held at a stage it has already finished with.
`Cmd_trysetencore` sets `encoreTimer = (Random() & 3) + 3` — **three to six turns** — and then
`CheckMoveLimitations` marks every move that is *not* the encored one as unusable. The lock is not
implemented as "do this again". It is implemented as **"everything else is unavailable"**, which
is the distinction that matters: the chain is not choosing to repeat, it has nothing else it is
permitted to select.

```
   one function, CheckMoveLimitations, holds all of these side by side:
     Encore        every move except the encored one is unusable, 3-6 turns
     Disable       one named move is unusable
     Taunt         every move with base power 0 is unusable
     Imprison      every move the opponent also knows is unusable
     Choice Band   every move except *choicedMove is unusable
   ───────────────────────────────────────────────────────────────────────────
   Five different causes. ONE readout: the option is greyed out. If you are
   looking at the greyed-out option rather than at which of the five set it,
   you cannot tell which one to remove — and removing the wrong one changes
   nothing at all.
```

**Encore** also has refusals worth noting, because they are the obstacles that cannot be named:
`Cmd_trysetencore` fails outright if the last move was **Struggle**, **Encore** or Mirror Move, if
the target has no PP left in that slot, or if an **Encore** is already running on it. An arrest
whose cause is not on the list is still an arrest.

## The reason assessment comes before the product: the Ability is not on the screen

**Surf** into **Lapras** does not do reduced damage. `Water Absorb` turns it into a heal of a
quarter of maximum HP. **Vaporeon** is the same. **Flamethrower** into **Ninetales** is `Flash
Fire` — no damage, and the target's own Fire moves come out stronger afterwards. One act, two
signs, decided by a property that is not drawn on the sprite.

And the games are explicit about the information problem: an opposing Ability is written into the
record **only when it fires**, which is the device m055 is built on. Before it fires, the honest
state of knowledge is "unknown", and the only way to find out by using **Surf** is to use
**Surf**.

**Heal Block** is the other half of it. The end-of-turn handlers for **Ingrain** and **Aqua Ring**
are the same code twice, and both of them check `healBlockTimer` first: with it running, the
restorative is attempted and returns nothing, with no message about why. m039 uses **Heal Block**
for a route that is shut; here it is the quieter case — the intervention is in place, it is
correct, and the term that would have let it work is somewhere else entirely.

## Why the product is downstream and still not trivial

**Leftovers** restores maxHP/16 at the end of every turn and it is genuinely good. It cannot clear
**Encore**, it cannot restore a `rolloutTimer`, it cannot remove `healBlockTimer`, and it will not
make a 90-accuracy chain connect. **Rapid Spin** clears a hazard. **Knock Off** removes an item.
**Brick Break** removes a screen. Each of them is the answer to exactly one thing, and the skill
is not in holding more items — it is in knowing which term is the one holding the chain at turn
one.

## Where the metaphor stops

The arithmetic above is arithmetic, and a counter that resets on a miss is a fair picture of a
repair sequence that restarts when the insult recurs. Nothing in it is a person, and nothing in it
should be read as one.

A chronic wound is a long thing to live with. It leaks, it can smell, it dictates what someone can
wear and whether they can bathe, and dressing changes can be the part of the week a person dreads.
People with ulcers are frequently left with the impression that slow healing is a failure of their
own effort, and the phase account is an argument against that: the commonest reasons a wound is
not healing are perfusion, mechanical load, dead tissue and the disease underneath, and none of
those is a matter of trying harder.

Two things to say with no framing at all. Healing is not always the goal — for some wounds, in
advanced illness or in a limb that cannot be revascularised, the aim is comfort, containment of
exudate, odour control and fewer disturbances, and choosing that is a considered plan rather than
a defeat. And the decision about whether healing is achievable is made by assessing the person,
with them, and never by consulting a model of phases or anything in a game.

## What Nurse Joy is listening for

Why the power on turn four belongs to turns one to three. What `CancelMultiTurnMoves` does to a
chain that was four-fifths finished, and what the equivalent insult is in a wound. Why five
different causes of a greyed-out option have one readout, and which of the five you would test for
first. Why using **Surf** is a poor way to find out whether the target has `Water Absorb`. Why a
correct restorative can return nothing and say nothing about why. And which single term is holding
this particular chain at turn one — because that, and not the item in the slot, is the answer.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* A current tissue-viability or wound-care textbook, for the phases of healing, the intentions of
  closure and the cellular detail.
* The reader's national guidance on leg ulcer management, for the relationship between arterial
  assessment and compression, and for who may apply compression.
* The reader's institutional wound-care policy and its wound assessment documentation, for the
  review interval, the escalation route and the locally approved debridement methods.
* The reader's national guidance on nutrition support in wound healing, for the substrate claims.
* The primary and review literature on chronic wound inflammation and on biofilm, for the claims
  the rigorous half marks as not settled.

Separately, and unlike the above: **Rollout**'s base power of 30 and accuracy of 90, the timer of
5, the doubling per elapsed turn, the **Defense Curl** bit and its further doubling, the reset of
`rolloutTimer` on a miss, **Fury Cutter**'s base 10 and its counter cap of 5, **Encore**'s
three-to-six-turn timer and its refusal cases, the five entries sharing
`CheckMoveLimitations`, the identical end-of-turn handlers for **Ingrain** and **Aqua Ring** with
their shared `healBlockTimer` check, **Donphan**'s and **Miltank**'s learnset levels, and the
Abilities of **Lapras**, **Vaporeon** and **Ninetales** were all read directly out of the public
disassemblies of the games and their expansion, which this environment could reach. The figure of
a little under three in five is the game's own 90 accuracy raised to the fifth power and is
arithmetic, not a figure printed anywhere.

## Scope and safety

This explains a model of repair and what follows from it, for someone already training in or
qualified for clinical practice. It is not a protocol, not a decision aid and not a wound
assessment tool, and it deliberately names no dressing, no debridement method for a particular
wound, no perfusion index, no cut-off and no review interval — the only numbers in it belong to a
video game. Compression, debridement and the management of an infected or non-healing wound are
governed by local policy and by the competence of the person doing them; that policy is the
authority and this is not, and none of it has had clinical review. Nothing here is for use in an
emergency or for a decision about any person's wound, including the reader's own. If someone is
unwell right now, the local emergency number is the correct response.

## Where this stands, October 2026

The phase model is old and stable, and so is the mechanism underneath it. What moves is the layer
below — biofilm, the molecular signatures of non-progressing wounds, the evidence for individual
advanced therapies — and, faster than any of it, the procedural layer: review intervals, referral
criteria, debridement competence frameworks and compression rules, which differ by country
already. The local policy is the authority for all of it. The game figures above, by contrast, are
pinned: every one of them is read out of the Advance-generation code, and nothing is claimed here
about how **Rollout** or **Encore** behaved in any other generation.
