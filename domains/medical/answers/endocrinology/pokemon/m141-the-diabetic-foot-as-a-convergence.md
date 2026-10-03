---
id: "m141"
slug: the-diabetic-foot-as-a-convergence
style: pokemon
category: endocrinology
difficulty: advanced
question: "Why is a diabetic foot ulcer better understood as a convergence of three mechanisms than as a complication of one?"
tags: [diabetes, neuropathy, peripheral-arterial-disease, foot-ulceration, infection]
---

# Spikes, Heal Block and a Badly Poisoned counter are three slots in one table, and Rapid Spin clears exactly one of them

This specialty reads hormones off the field: weather is the glucose-control hormones, terrain is
the axis hormones. This answer works a third layer that the others have not needed, and it is the
one the games keep on the **ground**.

**Spikes** is the right starting device because of where it lives. It is not on the Pokémon.
`Cmd_trysetspikes` writes `SIDE_STATUS_SPIKES` into `gSideStatuses[targetSide]` and increments
`gSideTimers[].spikesAmount`, so it belongs to the half of the field rather than to anything
standing on it (**mechanism**). Whoever set it has usually gone. **Skarmory** learns it at level
42 and, being part Flying, never pays for it — the setter is exempt from its own hazard
(**mechanism**). That is the m036 device from nursing, and it is the shape of repetitive
mechanical load: a property of the floor, accruing, owned by nobody present.

Then the arithmetic, which is exact: `spikesDmg = (5 - spikesAmount) * 2` and `gBattleMoveDamage =
maxHP / spikesDmg`, giving **an eighth, a sixth, then a quarter** for
one, two and three layers, with a floor of 1 (**mechanism**). It is charged on entry, once,
flagged by `SIDE_STATUS_SPIKES_DAMAGED` so it cannot fire twice for the same arrival. Every step
onto that side costs, and the cost per step rises with how long nobody cleared it.

| In the battle | What it stands for |
| --- | --- |
| **Spikes** in `gSideStatuses`, not on the battler | Mechanical load: a property of the ground, not of the limb |
| `(5 - spikesAmount) * 2` — an eighth, a sixth, a quarter | A cost per step that rises with accumulated deformity |
| `spikesAmount == 3` making `Cmd_trysetspikes` **fail** | The analogy's ceiling, which the real thing does not have |
| **Skarmory**, part Flying, setting **Spikes** at level 42 | A hazard whose setter never pays for it |
| Grounded, or not: **Flygon**, **Claydol**, an **Air Balloon** | Tissue that meets the floor, and tissue that does not |
| **Gravity**, an **Iron Ball**, **Ingrain**, **Smack Down** | Weight-bearing: what makes a limb feel the floor |
| **Heal Block**'s timer, and `MOVE_LIMITATION_HEAL_BLOCK` | Arterial disease: the repair route greyed out |
| `HandleEndTurnIngrain`'s `!healBlockTimer` guard | The sixteenth a turn that does not arrive |
| **Leftovers**, and the item slot it occupies | The small continuous repair, and what it competes with |
| **Badly Poisoned**, counter climbing, capped at 15 | Infection: the fast clock in a slow limb |
| `sEndTurnEffectHandlers`, an ordered array of handlers | Three terms scored separately, summed by nobody |
| `Cmd_rapidspinfree`, exactly one thing per use | One intervention, one term |
| **Heavy-Duty Boots** and `IsBattlerAffectedByHazards` | Offloading: one item that deletes a whole term |
| **Flail** stuck in its floor band, base power 20 | A severity reporter suppressed by the disease |
| `HandleEndTurnPoison` and `HandleEndTurnBurn`, one bar falling | Two processes, one appearance |
| **Shed Shell**, which solves a trapping problem and nothing else | An intervention precisely scoped to one term |

**This answer defers to two others.** m024 owns **Badly Poisoned** against **Poisoned** as two
trajectories under one readout, and **Stealth Rock** as the hazard waiting at the door; I use the
Toxic counter's arithmetic here and do not re-argue its diagnostic point. m056 owns **Flail** as
the inverse amplified reporter, and the last section of this answer is that reporter's floor band
doing a job at a different level.

Clinical claims below are marked (**mechanism**), (**definitional**), (**consensus**) or
(**country-dependent**). The Pokémon mechanics are not clinical claims and carry no marker; they
were read from the decompilations and the Sources section says which.

## Three terms, three stores, and one table that runs them all

```
   THREE STORES. NOTHING IN ANY OF THEM KNOWS ABOUT THE OTHER TWO.

   gSideStatuses[side]          volatiles.healBlockTimer      status1
   ─────────────────────        ─────────────────────────     ───────────────
   SIDE_STATUS_SPIKES           HEAL BLOCK                    STATUS1_TOXIC_POISON
   spikesAmount 1·2·3           a countdown                   + TOXIC_COUNTER
   charged ON ENTRY             blocks the repair             charged EVERY turn
   maxHP/8 · /6 · /4            at selection AND at           maxHP/16 × counter
   Flying and Levitate          every end-turn guard          counter climbs to 15
   exempt                                                     and then stops

        │                              │                           │
        │   AND THE TABLE THAT RUNS THEM, in this order:            │
        │                                                           │
        ▼                              ▼                           ▼
   ┌───────────────────────────────────────────────────────────────────────┐
   │  sEndTurnEffectHandlers[]                                            │
   │     …                                                                │
   │     [ENDTURN_AQUA_RING]  → heals, if !healBlockTimer                 │
   │     [ENDTURN_INGRAIN]    → heals maxHP/16, if !healBlockTimer        │
   │     [ENDTURN_LEECH_SEED] → drains                                    │
   │     [ENDTURN_POISON]     → maxHP/16 × counter                        │
   │     [ENDTURN_BURN]       → its own fraction, its own bit             │
   │     …                                                                │
   │     [ENDTURN_HEAL_BLOCK] → ticks its own timer down                  │
   │     …                                                                │
   │  Each entry is a separate function with its OWN guard. Not one of    │
   │  them reads another's store, and nothing anywhere adds them up and   │
   │  asks whether the total is survivable.                              │
   └───────────────────────────────────────────────────────────────────────┘
                     │
                     ▼
            THE VISIBLE THING: a bar going down, which is the term
            that arrived last and the only one with a graphic
```

That picture is the whole answer. Three stores, three handlers, three guards, one visible readout,
and no summation anywhere.

## Term one: grounded, and what grounded actually means here

Generation III's spikes check is two conditions and no more. The damage block is guarded by `&&
!IS_BATTLER_OF_TYPE(gActiveBattler, TYPE_FLYING) && gBattleMons[gActiveBattler].ability !=
ABILITY_LEVITATE`, so a Flying type is exempt and a **Levitate** holder is exempt, and nothing
else in the Advance source is (**mechanism**). **Flygon**'s only ability in both slots is
**Levitate**, so **Flygon** never takes a point from **Spikes** however many layers are down.
**Claydol** is the better example because it is funnier and more exact: it is a **Ground** type
with **Levitate**, so the most earth-bound typing in the game is not grounded.

The expansion generalises that two-line check into `IsBattlerGroundedInverseCheck`, and the order
of its tests is the part worth knowing:

```
   IRON BALL held            → grounded, return TRUE
   STATUS_FIELD_GRAVITY up   → grounded, return TRUE
   volatiles.root (Ingrain)  → grounded, return TRUE
   volatiles.smackDown       → grounded, return TRUE
   ── only now the exemptions ──
   Air Balloon / Levitate / Magnet Rise / Telekinesis → NOT grounded
   Flying type                                        → NOT grounded
```

The overrides are tested **before** the exemptions, so **Gravity** beats **Levitate** and an
**Iron Ball** beats an **Air Balloon** (**mechanism**). m091 established that ordering for the
pituitary answer; here it carries a different and more literal point. **Grounded is
load-bearing.** A hand and a foot in the same person can have the same loss of sensation, and only
one of them is standing on the hazard — and what makes the difference is not the nerve, it is
**Gravity**.

That is why the protective loss and the mechanical load are two facts and not one. The loss of the
signal is on the battler. The hazard is on the ground. The two only meet in something that is
grounded, and nothing in the games makes a battler grounded by *choice* — **Iron Ball**,
**Gravity**, **Ingrain** and **Smack Down** are all things that happen to it.

And the honest limit, stated here where the device is used rather than at the end:
**`Cmd_trysetspikes` refuses a fourth layer.** At `spikesAmount == 3` it takes the failure branch,
so the hazard saturates at a quarter and stops getting worse. Repetitive load on a deforming foot
does not saturate. The device is right about accumulation and wrong about the ceiling.

## Term two: the sixteenth a turn that does not arrive

**Heal Block** is the second store and it is a timer on the battler rather than on the field.
`IsHealBlockPreventingMove` returns true for any healing move while `volatiles.healBlockTimer` is
non-zero (**mechanism**), and the move is then removed from selection by
`MOVE_LIMITATION_HEAL_BLOCK` — one of **eighteen** branches of a single `else if` chain in the
current expansion, alongside **Disable**, **Torment**, **Taunt**, **Imprison**, **Encore**, the
**Choice Band** lock, an **Assault Vest** and **Gravity**. Every one of them greys out a slot and
the grey is identical. Generation III's version of that chain was five named mechanics in eight
ORed conditions; the list has grown and the readout has not.

But the part that matters for this limb is not the selection screen. It is that **every
end-of-turn repair carries its own copy of the guard**. `HandleEndTurnIngrain` reads
`volatiles.root && !volatiles.healBlockTimer && !IsBattlerAtMaxHp(battler)` and only then calls
`SetHealAmount(battler, GetDrainedBigRootHp(battler, maxHP / 16))` (**mechanism**).
`HandleEndTurnAquaRing` is the same function with a different volatile. Ice Body and Rain Dish
each carry the check again, separately.

So the repair arm is not weaker. It is **gated**, in several places independently, by a state that
has nothing to do with the repair arm's own machinery. **Ingrain** is still rooted. **Big Root**
would still have multiplied the drain. The sixteenth simply does not arrive, and nothing on screen
says why.

This is where the arterial term sits. It does not cause the wound and it does not cause the load.
It is the reason the thing the other two terms demand cannot be supplied (**mechanism**). And note
what it competes with: **Leftovers** occupies the one item slot, which is m014's and m038's budget
argument, and the slot cannot hold **Leftovers** and the thing that solves term one at the same
time. That constraint is real and the last section is about it.

## Term three: the counter that climbs on a different clock

The third store is `status1`, and the entry that matters is **Badly Poisoned**.
`HandleEndTurnPoison` computes a sixteenth of maximum HP and then multiplies: `gBattleMoveDamage
*= (status1 & STATUS1_TOXIC_COUNTER) >> 8`, with the counter incremented each turn until it
reaches `STATUS1_TOXIC_TURN(15)` and then held there (**mechanism**).

Two things follow and they are the clinical shape exactly. The cost **accelerates**, so the turn
on which it is noticed is not the turn on which it mattered. And on turn one it is charging
**half** of what ordinary **Poison** charges — the dangerous trajectory is the quieter one at the
start, which is m024's point and is not re-argued here.

What this term adds to the picture is a **clock**. Terms one and two are measured in the length of
a battle; this one is measured in turns and it compounds. Three mechanisms running at three speeds
in one place is why urgency and chronicity sit side by side, and why the service that addresses
the slow terms cannot be the only thing in the room (**consensus**).

## Two handlers, one bar falling

`HandleEndTurnPoison` and `HandleEndTurnBurn` are **different entries in
`sEndTurnEffectHandlers`**. They read different bits of `status1`, apply different fractions, and
both end with the same thing happening on screen: a bar going down at the end of a turn
(**mechanism**).

That is the shape of a warm, swollen, red foot that might be an acute Charcot process and might be
infection (**consensus**). Two mechanisms, two stores, one appearance — and the one that is
modifiable is modifiable by *stopping the loading*, which is the opposite of what you would do if
you had decided it was the other one.

The honest limit belongs right here. **The games always print the cause.** `HandleEndTurnPoison`
pushes a string that names the poison, and the ambiguity above is mine rather than the
cartridge's. What the code genuinely gives me is the architecture — two independent handlers
producing one visible event — and not the diagnostic difficulty. The diagnostic difficulty is real
and it is in the serious half.

## Why the reporter is sitting at its floor band

The thyroid answer reads an axis through **Flail**, whose base power is computed from the user's
own remaining HP in 48ths through a six-entry table — 200, 150, 100, 80, 40 and then **20 across
everything above two thirds of the bar** (**mechanism**). The move's own entry in the data lists
power 1; the number that matters is produced by the effect.

Reuse it here one level down. The reporter for this limb is the host response: how much it hurts,
how inflamed it looks, what the systemic markers do. And **terms one and two are both suppressing
that reporter.** The sensory loss removes one input to it outright. The repair-supply term is the
same supply the inflammatory response travels on, so the local signs are muted for the same reason
the healing is (**mechanism**).

So **Flail** is sitting in the flat band at 20 and you cannot tell how far past 20 the situation
is, because there is no number below it. The floor is blind and the floor is where this foot
lives. Which is exactly why the real assessment is built on things that do not depend on the host
response at all — the extent of tissue loss, the depth, whether bone is reached, and whether
perfusion is adequate (**consensus**). You stop asking the reporter and go and look at the field,
which is what m056 concluded about the thyroid axis for the same structural reason.

## One spin clears one thing, and one item deletes a whole term

`Cmd_rapidspinfree` is an `if / else if / else if` chain and it is the most useful three branches
in this answer:

```
   if      (status2 & STATUS2_WRAPPED)   → free the trapping,  and STOP
   else if (gStatuses3 & LEECHSEED)      → clear Leech Seed,   and STOP
   else if (gSideStatuses & SPIKES)      → spikesAmount = 0,   and STOP
   else                                  → nothing happens
```

**Rapid Spin** clears exactly one thing per use, in that fixed order (**mechanism**). It has
nothing to say about `healBlockTimer` and nothing to say about `status1`. **Forretress** is the
species to hang this on, because it learns **Rapid Spin** at level 22 and **Spikes** at level 49 —
the same Pokémon sets the hazard and clears it, twenty-seven levels apart, and clearing it still
touches only the one store.

That is why a wound dressed with great care for months can be no better. The dressing is the third
branch of a chain whose first two branches were the live ones.

And then the item, which is the best thing the games give this answer.
`IsBattlerAffectedByHazards` begins with the alive check and then:

```
   holdEffect == HOLD_EFFECT_HEAVY_DUTY_BOOTS  →  ret = FALSE
```

**Heavy-Duty Boots** does not reduce the hazard. It removes the battler from the hazard term
entirely, unconditionally, before any arithmetic runs (**mechanism**). That is offloading, and the
mapping is almost too neat: for a load-driven wound on a limb that cannot report load, taking the
load off the site **is** the treatment rather than an adjunct to covering it (**mechanism**,
**consensus**).

The cost is in the same line of code. It is a **held item**, and there is one slot. **Heavy-Duty
Boots** and **Leftovers** cannot both be in it. One term solved means another term's small
continuous repair is not running, and the games never ask whether the item is still the right one
— the four-slots-and-one-item argument from m014 and m038, landing on a real trade rather than a
rhetorical one.

## The mapping I am declining

Three refusals, and the first is the important one.

**Nothing in this answer stands in for a person's foot, and no Pokémon here is the patient.**
Everything above is a side of a field, a store in a struct and a handler in a table. The
temptation in this topic is enormous — a limb, a loss, something that can be taken away — and the
specialty's conventions rule that out for good reason. The outcome that everybody thinks about
when this subject comes up is in the plain prose below, with no mechanic attached, and it stays
there.

**I am not mapping the absent warning signal to anything, because the games have nothing for it.**
Every point of damage in Pokémon is displayed. There is no state in which a battler takes
**Spikes** damage and the bar does not move, no state in which the cause is not printed, and no
mechanic anywhere for a cost that is paid and not noticed. That absence is the single most
important fact about this limb, and the nearest thing the cartridge offers — a hazard count that
is nowhere on screen, a side status you cannot query — is about the *accumulation* being
invisible, not the damage. I have used it for that and stopped there. Writing an invented mechanic
for unnoticed harm would have scored better and taught something false.

**And I am not building a fifth terrain for this.** m094 declined to invent one for the
growth-hormone axis and set the precedent; the four are spoken for — **Grassy Terrain** thyroid
hormone, **Psychic Terrain** cortisol, **Misty Terrain** calcium, **Electric Terrain** the
reproductive clock, their four **Tapu** setters and a **Terrain Extender** for the long half-life
— and this answer is not about a hormone at all. It is about three hazards and a limb that is
**grounded**, which is the same grounding check the terrain layer already uses, extended downward
rather than sideways. That reuse is the point: the check that decides who feels an axis hormone is
the check that decides who feels the floor.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of three independent accumulating costs, each held in a different
place, each gated by its own condition, with one visible readout and nothing summing them. The
picture is fair, and the single clinical conclusion it supports is the right one: a wound that is
being dressed and still loaded is being treated in the term that is not driving it.

Here is what the picture leaves out.

A diabetic foot ulcer is usually **painless**. That is the most consequential human fact in this
topic and the least intuitive to anybody whose feet work normally. A painless wound does not feel
like an emergency to the person who has it, and frequently does not get treated like one by the
system around it either. Delay is built into how this presents. People are nonetheless routinely
described in their own notes as having presented late.

The main treatment is the main cost. Offloading means not walking on it, for weeks to months, to
heal something that does not hurt — and not walking means not working, not driving, not collecting
children, not leaving the house. Calling that a question of adherence is a category error. It is a
question about what somebody can afford to stop doing.

Amputation is the outcome everyone working in this area is thinking about, and there is no
mechanic above for it and will not be. It is a loss and it changes a life. It is also not a
foregone conclusion: specialist multidisciplinary foot services exist precisely because
trajectories change, and that is a better thing to know than any staging system.

A note about who is reading. Somebody reading about this is more likely to have diabetes than to
be sitting an examination. If that is you: there is nothing here to compare yourself with — no
thresholds, no dressings, no antibiotics, no timescales — and that is deliberate. A new wound, a
newly warm or swollen foot, or any change in a foot that already had a wound is a reason to
contact the service that knows you, promptly. Not a reason to read an analogy about entry hazards.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national guidance on the diabetic foot, for risk stratification, screening, referral routes
  and expected timescales. This is the most locally specified part of the subject.
* Your national or specialty-society guidance on diabetic foot infection and on diabetic foot
  osteomyelitis, for classification and the diagnostic sequence used where you work.
* Your national or specialty-society guidance on peripheral arterial disease, for the non-invasive
  assessment used, its failure modes in diabetes and the thresholds that trigger imaging.
* **Your local microbiology and antimicrobial policy.** Nothing about antimicrobial choice appears
  here and that policy is the authority.
* **Your own institution's pathway** for the multidisciplinary foot service, including what counts
  as urgent and who may refer.
* A current textbook of diabetes or vascular medicine, for the fibre populations involved in the
  neuropathy, the pattern of arterial disease, the plantar compartment anatomy, and acute Charcot
  neuroarthropathy.

The Pokémon side is different and is sourced properly. `Cmd_trysetspikes` writing
`SIDE_STATUS_SPIKES` and capping `spikesAmount` at 3 with a failure branch; the Generation III
spikes damage being `(5 - spikesAmount) * 2` against maximum HP with a floor of 1, flagged once
per arrival by `SIDE_STATUS_SPIKES_DAMAGED`, and skipped only for a Flying type or
`ABILITY_LEVITATE`; **Skarmory** learning **Spikes** at level 42 and **Forretress** learning
**Rapid Spin** at 22 and **Spikes** at 49; **Skarmory** being Steel and Flying, **Forretress** Bug
and Steel, **Flygon** Ground and Dragon with **Levitate** in both ability slots, and **Claydol**
Ground and Psychic with **Levitate**; `Cmd_rapidspinfree`'s three-branch chain in the order
trapping, **Leech Seed**, **Spikes**; `IsHealBlockPreventingMove`, `MOVE_LIMITATION_HEAL_BLOCK` as
one branch of the eighteen-branch `CheckMoveLimitations` chain, and `HandleEndTurnIngrain`'s
`!healBlockTimer` guard around `GetDrainedBigRootHp(battler, maxHP / 16)`; `HandleEndTurnPoison`
multiplying a sixteenth by `(status1 & STATUS1_TOXIC_COUNTER) >> 8` and holding at turn 15; the
order of `sEndTurnEffectHandlers`; `IsBattlerGroundedInverseCheck` testing **Iron Ball**,
**Gravity**, **Ingrain** and **Smack Down** before **Levitate**, an **Air Balloon**, **Magnet
Rise**, **Telekinesis** and the Flying type; `IsBattlerAffectedByHazards` returning FALSE outright
for `HOLD_EFFECT_HEAVY_DUTY_BOOTS`; and **Flail**'s six-band table on 48ths with a listed base
power of 1 were all read from the pokeemerald and pokeemerald-expansion decompilations rather than
from memory. **Heavy-Duty Boots** is a Generation VIII item and **Gravity**, **Smack Down**,
**Heal Block** and **Magnet Rise** are Generation IV or later; the **Spikes** arithmetic and the
two-condition exemption are Generation III and differ from the later grounding routine. Nothing
here depends on a figure that was not read from code.

## Scope and safety

The Pokémon here is doing one job: making it concrete that three independent costs held in three
different places are not one problem, that each intervention addresses one of them, and that the
readout which would grade severity is suppressed by two of the three. It is not a clinical
reference, not a decision aid, not a wound-care protocol, and not about any individual's care.
**No doses, antimicrobial choices, thresholds, classification cut-offs or dressing selections
appear here on purpose** — all are local and all change. Check your own service's pathway and your
local microbiology policy. Nothing here has had clinical review. No Pokémon in this answer stands
in for a person, a limb or an outcome, and a foot that is new to a service is an urgent clinical
assessment rather than a reading exercise.

## What a Gym Leader digs into next

* Why does **Spikes** live in `gSideStatuses` rather than on the battler, and what does that
  change about who is responsible for it?
* Why does **Claydol**, a Ground type, never take **Spikes** damage — and why is that the whole
  hand-against-foot argument?
* Why does **Gravity** beat **Levitate**, and why is "grounded" the load-bearing word in this
  answer?
* Why is **Heal Block** checked again inside `HandleEndTurnIngrain` when it has already greyed the
  move out?
* Why does **Rapid Spin** stop after one branch, and which branch is a dressing?
* Why do **Heavy-Duty Boots** and **Leftovers** compete, and what is the clinical version of that
  competition?
* Why is **Flail** stuck at 20 in this limb, and what do you measure instead?

## Where this stands, October 2026

The three-store architecture, the independence of the terms, the grounded rule, the
one-thing-per-spin removal and the suppressed reporter are mechanism and do not date. What dates
on the Pokémon side is the constants and the cast: the **Spikes** damage fractions and its
two-condition exemption are Generation III and the later grounding routine supersedes them; three
layers is a Generation III change from Generation II's one; **Heavy-Duty Boots** is Generation
VIII, **Gravity**, **Smack Down**, **Heal Block** and **Magnet Rise** Generation IV or later, and
an **Air Balloon** Generation V; `CheckMoveLimitations` has grown from eight ORed conditions to
eighteen branches and will grow again; and the expansion's end-turn table is reorganised between
releases. Check the current generation's data. On the clinical side everything procedural moves —
risk-stratification categories, classification systems, vascular thresholds, offloading methods,
antimicrobial choice and duration, revascularisation criteria and how a foot service is accessed —
so check current local guidance, your own institution's pathway and your local microbiology
policy.
