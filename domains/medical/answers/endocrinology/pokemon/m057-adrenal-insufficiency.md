---
id: "m057"
slug: adrenal-insufficiency
style: pokemon
category: endocrinology
difficulty: advanced
question: "Adrenal insufficiency is uncommon and its symptoms are unremarkable. Why is it the endocrine diagnosis it is most dangerous to miss?"
tags: [adrenal, cortisol, aldosterone, acth, crisis]
---

# An empty item slot looks exactly like Leftovers for twenty quiet turns

A held item does not announce itself. **Leftovers** returns a sixteenth of the holder's maximum HP
at the end of every turn, unconditionally, costing no turn and needing no decision — the house
mapping for a continuous background correction, carried over unchanged from the insulin answer
*(mechanism)*. A **Sitrus Berry** does nothing at all until HP drops to half or below, then fires
once, restores a quarter of maximum HP in Generation IV onward, and is consumed *(mechanism)*.
Background and load. Two halves of one job, which the real thing does from one source and the
games split across two item slots.

And here is the geometry that makes this the dangerous one. **You cannot see the item slot.** A
Pokémon holding nothing and a Pokémon holding Leftovers look identical until the end of the turn,
and then differ by a sixteenth, which nobody is counting in a quiet battle. A Pokémon holding
nothing and a Pokémon holding a Sitrus Berry look identical *all the way down to half HP* — and
the moment you find out is the moment the berry that was never there fails to fire. The discovery
and the emergency are the same event.

| In the battle | What it stands for |
| --- | --- |
| **Leftovers**: 1/16 of max HP, every turn, unconditionally | The continuous baseline output |
| **Sitrus Berry**: fires at the half-HP threshold, then gone | The demand-driven reserve |
| An **empty item slot** | The deficit, which is invisible until load |
| **Psychic Terrain**, which blocks priority moves at grounded targets | Cortisol: permission, and proportion |
| **Tapu Lele**'s **Psychic Surge**, on entry, five turns | The ACTH-driven limb of the cortex |
| **Tapu Bulu**'s **Grassy Surge**, on its own schedule | The limb that is not on that loop at all |
| A terrain already up, so the setter's ability does nothing | Suppression by supply from outside |
| **Flail**'s base power, 20 up to 200 | The reporter, inverse and amplified |
| **Fake Out**, **Mach Punch**, **Aqua Jet**, **Sucker Punch** | The fast first response, let through |

Claims are marked *(mechanism)*, *(definitional)*, *(consensus)* or *(country-dependent)* where it
matters.

## Two setters, one side, and only one of them takes orders

```
   the ally's HELPING HAND ──► the FLAIL user ──► THE TWO SETTERS ON THE SIDE
                                                            │
              ┌─────────────────────────────────────────────┴──────────────────┐
              │                                                                │
      TAPU LELE, Psychic Surge                                   TAPU BULU, Grassy Surge
      sets Psychic Terrain on entry                              sets Grassy Terrain on entry
      renewed because the loop asks for it                       renewed on its own account,
              │                                                  for reasons of its own
              │                                                                │
      ◄── feedback onto the levels above ──┘                      NOT in that loop at all
              │                                                                │
              ▼                                                                ▼
      priority moves do not land ·                               a sixteenth a turn to every
      the fast first hit is damped                               grounded Pokémon · the floor
                                                                 under the bar · volume

   ── WHICH SETTER IS MISSING DECIDES WHICH COLUMN GOES DARK ────────────────────────────

   BOTH GONE          no Psychic Terrain AND no Grassy Terrain
   (the cortex)       FLAIL IS AT 200, because the loop is open and shouting
                      → the fast hits all land · the sixteenth a turn is gone
                      → the bar drifts down with nothing holding its floor

   LELE ONLY          Psychic Terrain lapses on its five-turn clock. Grassy Terrain
   (upstream, or      is renewed as usual by a setter that never needed the orders.
    supply from       FLAIL IS AT 20 — the reporter is quiet, and quiet is wrong
    outside)          → and the OTHER terrains that level 2 was setting may be gone too
```

**Tapu Bulu** not taking orders is the whole of the split. It is why one failure takes the floor
out from under the bar and the other does not, and why the two are not a mild and a severe version
of the same thing *(mechanism)*.

And the loud version is visible. When the reporter is pinned at 200 turn after turn, you can see
it without measuring anything — **the announcement is the finding**, and the announcement happens
only when the setter itself is the thing that is gone.

## The commonest cause is a terrain somebody else set

Here is a verified mechanic that does more analogical work than any species in this answer.
`TryChangeBattleTerrain` **returns false if the terrain is already the one being set**, so a Surge
ability entering onto its own terrain does nothing at all — the ability does not even announce
itself, and, critically, **the timer is not refreshed either** *(mechanism)*.

Picture twenty turns of someone else keeping Psychic Terrain up from the far side. Your **Tapu
Lele** comes in and out and its ability never fires once, because there was never anything for it
to do. The side stops being built around needing it. Then the outside supply stops — and the
terrain lapses on the clock it was set with, not on a fresh one, and nothing renews it. Nobody has
done anything wrong. The setter has simply not been exercised, and it does not come straight back.

This is the commonest shape of the problem by a long way *(consensus)*, and notice what it looks
like: **Lele only**. Flail quiet. Grassy Terrain fine. Which is to say, it looks nothing like the
loud version that gets taught, and the loud version is what people are watching for.

## Why the quiet turns tell you nothing, and what actually discriminates

A bar drifting down slowly, a side that feels sluggish, nothing on the field that explains it:
every one of those has a dozen causes and none of them points here *(consensus)*. You do not find
this by pattern-matching the vibe of the battle. You find it by noticing the things that follow
from the **mechanic**:

* **Fast moves landing that should not land.** **Fake Out** connecting, **Mach Punch** going
  first, **Sucker Punch** getting through: Psychic Terrain blocks priority moves aimed at grounded
  targets, so their success is a statement about the terrain *(mechanism)*.
* **The floor gone from under the bar**, which is Grassy Terrain's sixteenth a turn missing, and
  which happens only when **both** setters are out *(mechanism)*.
* **Flail pinned at 200**, which points at the setter itself rather than upstream *(mechanism)*.
* **A terrain on the field that your side did not set** — a history question about the last twenty
  turns, not a measurement of this one *(consensus)*.
* **The other terrains missing too**, which puts the fault at level 2 rather than at the cortex
  *(mechanism)*.

## The test is a push, and the push goes the other way

The house rule, and it holds for every axis in this specialty: **you test a loop by pushing it in
the direction it should resist.** A suspected shortage is therefore tested by **supplying** —
setting the condition from outside, or sending in the setter deliberately and watching whether
anything happens *(consensus)*. The reporter is read alongside, because the reporter is what
separates "the setter is gone" from "the setter was never asked".

Two failure modes, both mechanical:

* **Supplying can be falsely reassuring early.** A **Tapu Lele** that has sat unexercised for a
  few turns still has **Psychic Surge** and will still fire it the moment it is given something to
  do *(mechanism)*. The push interrogates the setter. The fault is upstream of the setter.
* **What lands is not what was sent.** **Reflect** halves incoming physical damage for five turns,
  eight while the setter holds **Light Clay**, and changes nothing about the attacker
  *(mechanism)*. Grade the attacker by what the defender felt and Reflect has made you wrong, in
  whichever direction it happens to be up.

## The collapse, as a mechanic and not as a procedure

What the decompensated version looks like is a combination you cannot easily produce another way.
The bar is falling and **restoring it from the bag does not hold** — because the problem is not
the bar, it is that nothing is damping what is arriving, and no amount of restoring substitutes
for the missing permission *(mechanism)*. The floor is gone, the fast hits are all landing, and
whatever started it is usually still on the field.

The mechanic is: restore the missing permission, restore the floor, and deal with whatever
precipitated it — and go and look for the precipitant, because there nearly always is one. What is
actually done, in what order, is a protocol, it differs between countries and institutions, and it
is deliberately not on this page.

## Why supplying the item does not close the loop

Put **Leftovers** in the slot and the baseline is covered. The slot now holds one item, and the
berry is not in it. The threshold response is not restored by supplying the baseline, because what
is missing is not the item — it is the **sensor and the decision** that would have chosen which
one this turn needed *(mechanism)*. That is the same open-loop problem the insulin answer works
through, with the same two-part shape, and it is why the arrangements that exist for increased
requirement exist at all. Those arrangements are specific, they are set up with a person's own
team, and they differ between countries *(country-dependent)*.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a control loop with two outputs under two different controllers,
and of a reserve whose absence is invisible until it is called on. The picture is fair. What the
collapse is for a person is not a battle, and an item slot is not a life.

Delayed diagnosis in adrenal insufficiency is common, documented, and harmful, and it is usually
nobody's single mistake — a non-specific syndrome with a low prior gets attributed to something
commoner several times before it is attributed correctly. Saying that is more useful than
pretending the diagnosis is easy.

People living with treated adrenal insufficiency depend on an external supply of something the
body normally regulates for itself, every day, with no days off, and with the extra burden of
having to recognise and act on increased requirement during any illness. That burden is carried by
the person rather than by a clinic, which is why the education given at diagnosis matters as much
as the prescription.

And a note about who is reading. Someone reading this is more likely to be living with adrenal
insufficiency, or caring for someone who is, than revising it. If that is you: nothing above is an
instruction, a dose, a threshold or a plan. The arrangements for illness, and the emergency
arrangements, are specific to you and are set up with your own team. The plan you already have is
the one that applies, and it is not something to re-derive from an analogy about item slots.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../for-agents/SOURCES-endocrinology.md`](../../for-agents/SOURCES-endocrinology.md) for
the standing documents of this specialty. Specific to this answer:

* Your national guideline on adrenal insufficiency, or the equivalent specialty society guidance
  issued in your country, for diagnosis, testing and the arrangements around illness.
* **Your own institution's protocol** for suspected adrenal crisis and for perioperative and
  intercurrent-illness cover. It overrides a national document where they differ.
* Your national formulary, for anything about a glucocorticoid or mineralocorticoid preparation
  and for the guidance on withdrawal after prolonged use.
* Your laboratory's handbook, for the assays it runs and the sample handling they need.
* A current endocrinology textbook, for the zonal anatomy of the cortex and the independence of
  the mineralocorticoid limb from the pituitary loop.

The Pokémon side is different and is sourced properly. **Leftovers**' sixteenth, the **Sitrus
Berry**'s half-HP trigger and its quarter-of-maximum restore from Generation IV, **Grassy
Terrain**'s sixteenth a turn to grounded battlers, the grounded-only rule, the five-turn and
eight-turn terrain timers, the **Surge** abilities and their holders, **Flail**'s band table,
**Reflect** with **Light Clay**, and the fact that a Surge ability does nothing and refreshes no
timer when its own terrain is already up were all read from the pokeemerald and
pokeemerald-expansion decompilations rather than from memory.

## Scope and safety

The Pokémon here is doing one job: making a two-output control loop, and the invisibility of a
missing reserve, concrete. It is not a clinical reference, not a decision aid, and not about any
individual's care. **No doses, thresholds, test protocols or illness-cover arrangements appear
here on purpose** — they differ between countries and institutions and are revised, and a revision
page is the wrong place to get them from. Check the formulary and your local protocol. Nothing
here has had clinical review. The metaphor covers mechanism and stops at outcome: adrenal crisis
is a medical emergency and is not material for a battle analogy. If someone is unwell now, contact
local emergency services.

## What a Gym Leader digs into next

* Why can you not tell an empty item slot from a **Sitrus Berry** slot until the bar reaches half?
* Why does only one of the two setters take orders, and what does that change about the readout?
* Why does a Surge ability entering onto its own terrain do nothing, and why does the timer
  matter?
* Why is restoring the bar from the bag not enough when the problem is the missing permission?

## Where this stands, October 2026

The two-output architecture, the reserve geometry and the invisibility of the deficit are
mechanism and do not date. What dates on the Pokémon side is the constants and the cast: terrains
arrived in Generation VI and the **Surge** abilities in Generation VII, the **Sitrus Berry**
restored a flat 30 HP in Generation III and a quarter of maximum from Generation IV, and
**Rillaboom**, **Pincurchin** and **Indeedee** carry their Surge as a **Hidden Ability**. Check
the current generation's data. On the clinical side everything procedural and numeric moves —
protocols, thresholds, assays, illness and emergency arrangements, and withdrawal guidance — so
check current local guidance and your own institution's protocol.
