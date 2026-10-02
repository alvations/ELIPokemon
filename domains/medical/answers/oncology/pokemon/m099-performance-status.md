---
id: "m099"
slug: performance-status
style: pokemon
category: oncology
difficulty: intermediate
question: "Why does a crude ordinal performance status scale predict tolerance of systemic therapy better than more precise measurements, and where does it mislead?"
tags: [performance-status, assessment, reliability, eligibility, geriatric-oncology]
---

# Hidden Power reads one bit of each Individual Value and throws eighteen bits away

`Cmd_hiddenpowercalc` in Emerald is twelve lines and it is the best model of a crude index in the
whole cartridge.

A battler carries six **Individual Values**, each five bits wide — `MAX_IV_MASK` is thirty-one —
so thirty bits of hidden, per-individual variation. **Hidden Power** reads **twelve** of them. It
builds `typeBits` from bit zero of each of the six, and `powerBits` from bit one of each of the
six, and discards the top three bits of every single value. Then:

```
   gDynamicBasePower = (40 * powerBits) / 63 + 30;
   dynamicMoveType   = ((NUMBER_OF_MON_TYPES - 3) * typeBits) / 63 + 1;   // then skip ???
```

Thirty bits in, two readings out: a base power somewhere between thirty and seventy, and one of
sixteen types. Eighteen bits of precise, genuine, individual information are simply not consulted.

And the result is a real move that does real damage and gets chosen over alternatives. The crude
index is not a summary of the precise data for a reader's convenience. **It is the input the
machinery actually uses.**

As elsewhere in this specialty: **the objects of study are index functions, thresholds and
gates.** No Pokémon in this answer stands in for a person, and the analogy is dropped entirely at
the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
**consensus**, **country-dependent**.

## What the index does, drawn

```
   THE PRECISE DATA                      WHAT THE INDEX READS

   hpIV        0..31   ░░░░░            bit 0  ──┐
   attackIV    0..31   ░░░░░            bit 1  ──┤
   defenseIV   0..31   ░░░░░              ...    ├──►  typeBits  (6 bits)
   speedIV     0..31   ░░░░░                     │     powerBits (6 bits)
   spAttackIV  0..31   ░░░░░                   ──┘
   spDefenseIV 0..31   ░░░░░
                       ▲▲▲
                       │││ THREE BITS OF EACH, NEVER CONSULTED

   ───────────────────────────────────────────────────────────────────────────

   AND THE TWO ENDS COLLAPSE

      every IV at 31   ──►  typeBits 63, powerBits 63
                       ──►  index 16, which is at or past ??? so it steps
                            to 17 — Dark — at base power seventy.
                            EVERY perfect spread gives the SAME answer.

      all six bits zero ──► Fighting, base power thirty.
                            And (40 * 0) / 63 + 30 cannot go below thirty.

      A CEILING and a FLOOR, and a great many different spreads landing
      on one identical reading in between.

   ───────────────────────────────────────────────────────────────────────────

   AND THE MOVE'S OWN DATA ENTRY SAYS SOMETHING ELSE ENTIRELY

      [MOVE_HIDDEN_POWER]  .power = 1   .type = TYPE_NORMAL   .accuracy = 100

      What is written in the table is not what the instrument does.
```

## Why reading twelve bits beats reading thirty

Three mechanisms, and they compound (**mechanism**).

**It integrates.** No single precise measurement captures what performance status captures. A
haemoglobin, an albumin, a tumour measurement and a walking test each describe one thing; the
scale describes the net effect of everything on what the person can actually do. Hidden Power is
one reading computed across all six values rather than a seventh value sitting beside them, which
is the structural difference. The nursing answer on early warning scores makes the same argument
about a composite built from simple bedside observations, and the mechanism is the same mechanism.

**It is reproducible enough.** Agreement between observers on a coarse ordinal is moderate rather
than excellent, and it is better than agreement on a finer-grained alternative (**consensus**).
The information a reading carries is bounded by its reproducibility, so extra levels nobody
assigns the same way add resolution and subtract information. This specialty's answer on staging
makes the same point about why a staging system uses discrete categories for a continuous extent:
a classification used by many people is optimised for agreement rather than fidelity. The scale
and the finer-grained alternative — a short ordinal associated with the Eastern Cooperative
Oncology Group and the World Health Organization, and the Karnofsky scale — are not
interchangeable, and mappings between them are approximations (**definitional**, **consensus**).

**It is always available.** `Cmd_hiddenpowercalc` needs nothing but the battler's own stored
values; it runs in the move's own script and never waits for anything. A measurement that needs
equipment, a technician or a wait is not available at the moment the decision is made, and one
taken from the conversation always is (**mechanism**).

And it was built against the thing it is used for. It predicts **tolerance of treatment**, which
is a different quantity from a measurement of function, and it is a property of the person rather
than of the tumour — which is why it sits on a different axis from stage and grade entirely
(**definitional**).

## Where it misleads, one mechanic at a time

### Many spreads, one reading

Two battlers with completely different Individual Values can share a Hidden Power exactly, because
only one bit of each value reaches the index. That is the **conflation of causes**, and it is the
most important point in this answer.

The same performance status arises from long-standing unrelated disease, from anaemia, from a
drainable effusion, from uncontrolled symptoms, from deconditioning after a hospital stay, and
from the cancer. Some of those are reversible. A poor status with a reversible contributor is
**not** a reason to withhold treatment until the reversible thing has been looked for, and
treating the reading as the finding is a common and consequential error (**mechanism**,
**consensus**). The question *why is it this* is a different and better question from *what is
it*.

### The reversible contributor, and the ability that proves it is checked explicitly

`CalculateBaseDamage` contains one line that is this point in miniature:

```
   if ((attacker->status1 & STATUS1_BURN) && attacker->ability != ABILITY_GUTS)
       damage /= 2;
```

A burned battler reads as half as strong on the only number the function will use. Nothing about
its Attack stat changed — the halving is applied to the damage, after the stat has been read. Cure
the burn and the reading is restored in full. **The index was correct and the cause was
reversible**, which is the whole clinical argument with the machinery exposed.

The same function also shows what an exception looks like when somebody has thought about it.
**Guts** is named in the condition, so a **Swellow** or a **Hariyama** is exempt from the halving;
**Milotic**'s **Marvel Scale** is tested in the adjacent line and multiplies Defence by one and a
half *while* a status condition is present. A system that knows which readings its own conditions
distort writes the exceptions down.

### A snapshot, with no direction in it

**Overgrow** and its three siblings are tested as `attacker->hp <= (attacker->maxHP / 3)` — a
single comparison at a single instant. **Sceptile** has Overgrow, **Blaziken**, **Swampert** and
**Heracross** have the analogous abilities for their own types, and not one of those tests knows
whether the HP is falling or recovering. The threshold is read now and says nothing about the
direction of travel.

A performance status recorded at one visit has exactly that limitation, and the trajectory over
weeks carries more information than the level does (**consensus**). A status carried forward from
a letter written a month ago is not a current reading, and is routinely used as one.

Worth noting what the arithmetic does at the edge, because it is about the threshold and not about
any creature: a cut-off defined as a fraction of a maximum is unreachable when the maximum is one.
**Shedinja**'s base HP is one, one divided by three floors to zero, and a strictly-positive HP can
never be at or below zero. The same shape is why the scale's bottom category compresses states
that are clinically very different, and why its top category cannot separate someone exceptionally
fit from someone just inside it — which matters, because the top category is where intensive
regimens are considered.

### The index used for the wrong purpose, and the source saying so

The sharpest fact in this answer. Hidden Power's computed type is honoured by the damage
calculation and **deliberately ignored** somewhere else. `Cmd_datahpupdate` chooses which type to
record for Counter and Mirror Coat, and because Hidden Power sets
`F_DYNAMIC_TYPE_IGNORE_PHYSICALITY`, that routine falls back to the move's **base** type — Normal
— rather than the computed one. The decompilation's own comment spells out the consequences:
Hidden Power will only ever trigger **Counter** and never **Mirror Coat**, and a Hidden Power of
the Fire type cannot thaw a frozen target.

One reading, valid for one purpose, explicitly overridden for another, with the override
documented in the file. That is what performance status needs and frequently does not get. It is a
valid input to tolerance and to eligibility. It is not a measure of the disease, it is not
regimen-independent, and it is not a statement about an individual's outlook. "Fit for treatment"
is not a property of a person alone but of a person and a particular regimen: a status adequate
for one schedule may not be adequate for another with different organ toxicity, and the scale
cannot express that (**mechanism**).

### Assigned, not computed

Here the game and the clinic differ, and the difference is the point. `Cmd_hiddenpowercalc` is
arithmetic: run it twice and you get the same answer. Performance status is **assigned by an
observer**, so it carries observer variation — and the variation is not symmetrical. Recorded
status is systematically better than the account the person gives of themselves, and clinicians
and patients disagree in that direction often enough that it is a known property of the instrument
rather than an anecdote (**consensus**).

Nothing in Pokémon models an observer disagreeing with a subject, and nothing here pretends
otherwise. The gap is worth naming rather than papering over, because it is the single largest
difference between a computed index and an assigned one.

### Whole domains outside the index

Cognition, mood, nutrition, polypharmacy, social support and falls are outside performance status
by construction — the three discarded bits of every value. That is the explicit rationale for
structured geriatric assessment in older adults, which finds problems the scale does not detect
and changes management in a substantial share of the people it is applied to (**consensus**,
strongly **country-dependent** in whether it is resourced at all).

### The gate, and what a gate does to the evidence

`Cmd_maxattackhalvehp` — **Belly Drum** — is an eligibility criterion written as code. Two
conditions, both required: the Attack stat stage must be **below** `MAX_STAT_STAGE`, **and**
current HP must be **strictly greater** than half of maximum HP. If either fails, the script jumps
to the failure branch and nothing happens at all. No partial effect. No reduced version. Admitted
or excluded, on a reserve threshold read before anything is attempted. The answer on margins uses
**Substitute**'s quarter-of-maximum gate for the same shape; Belly Drum is the version with two
independent exclusion criteria.

Clinically, that gate is where the evidence base bends. Trials recruit predominantly from the
better categories, so the published evidence is weakest exactly where the decision is hardest — in
people whose status is poor, which is also where the potential for both benefit and harm is
largest (**consensus**). That is a structural feature of the literature rather than a criticism of
any trial.

## What good use of it looks like

Short, and all of it follows (**consensus**): record **who** assigned it and **when**, because an
observation without a source and a time is incomplete — the nursing answer on documentation makes
the same point; record the **person's own account** alongside it, because the two disagree in a
known direction; ask **why** it is what it is and look for reversible contributors before it
excludes anything; **reassess** rather than carry forward, and note the direction; and state the
**question** rather than the reading alone — fitness for a named regimen, not fitness in general.

## Where the metaphor stops

Everything above is index functions, thresholds and gates, and code is a good place to see them
because the discarded bits are visible. What follows is about people, so it is said plainly and
without the analogy.

A performance status is recorded about somebody, usually without their knowing it has been
recorded, and it can decide whether a treatment is offered or a trial is mentioned. That is a
considerable amount of weight on a judgement made in a few seconds by someone who has met the
person once, often on a day that is not representative. People who are managing a great deal at
home with a great deal of effort are frequently recorded as more independent than they are,
because they describe themselves that way — out of pride, out of fear that treatment will be
withdrawn, or simply because the question was asked in a form that invited a short answer.

The practical consequence is the one that belongs first rather than last: ask the person what
their day actually looks like, and ask someone who lives with them if they are there. It takes
longer than assigning a category, and it is how the category stops being wrong.

Nothing in either half of this answer is a statement about any individual's outlook, and no
clinical figure of any kind appears in either half. Both omissions are deliberate.

## What a Gym Leader is listening for

* Hidden Power reads twelve bits of thirty. Which clinical property is the discarding, and which
  is the reading?
* Every perfect Individual Value spread gives the same Hidden Power. Name the two instrument
  defects that one fact demonstrates.
* The burn halving is tested with `ability != ABILITY_GUTS`. What are the two separate lessons in
  that line?
* Overgrow tests one comparison at one instant. What does a performance status share with it?
* `F_DYNAMIC_TYPE_IGNORE_PHYSICALITY` makes one routine ignore the computed type. What is the
  clinical version of using the right reading for the wrong purpose?
* Belly Drum has two independent conditions and no partial effect. What does a gate of that shape
  do to a body of evidence?
* Where does this analogy break, and why is that break the most important thing on the page?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* The definitional source for whichever scale your service records — the Eastern Cooperative
  Oncology Group's own description of its scale, the World Health Organization's parallel version,
  or the Karnofsky scale as published. The exact category wording matters and is deliberately not
  reproduced here.
* Your national or regional guidance for the disease and regimen in question, for the performance
  status at which a treatment is considered and what is advised when it is poorer. These are
  regimen-specific and differ between countries.
* Your own institution's systemic therapy assessment policy, which governs what must be recorded
  before treatment and by whom.
* The published guidance on geriatric assessment in oncology from the professional society issuing
  it in your region, for which domains are assessed and what the assessment is held to add.
* The primary literature, for inter-observer agreement on the scales, for the direction and size
  of clinician–patient disagreement, and for the representativeness of trial populations.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about what a functional assessment scale can and cannot bear, dressed in
a game so that the discarded information stays visible. It has had no clinical review. **No scale
category, cut-off, agreement statistic or eligibility threshold appears here, and none should be
inferred** — the category wording belongs to the body that publishes the scale, the thresholds at
which treatment is considered are regimen-specific and differ between countries and institutions,
and both are revised; the guidance and policy in force where you work are the authority, and this
is not. It is not an assessment tool and not a decision aid, it says nothing about anybody's
outlook, and it describes no individual's situation. Anyone affected by cancer — their own
diagnosis or someone else's — should be talking to the clinical team looking after that person,
who have the history and the examination, neither of which is here. The analogy carries index
arithmetic and gating only: no part of it stands in for a person, and no creature's resilience is
the subject of any sentence in it.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source. `Cmd_hiddenpowercalc` in
`src/battle_script_commands.c` builds `powerBits` from bit one of each of `hpIV`, `attackIV`,
`defenseIV`, `speedIV`, `spAttackIV` and `spDefenseIV`, and `typeBits` from bit zero of the same
six; sets `gDynamicBasePower` to `(40 * powerBits) / 63 + 30`, giving thirty to seventy; and sets
`dynamicMoveType` to `((NUMBER_OF_MON_TYPES - 3) * typeBits) / 63 + 1`, incrementing again if the
result reaches `TYPE_MYSTERY`, then flags it with `F_DYNAMIC_TYPE_IGNORE_PHYSICALITY` and
`F_DYNAMIC_TYPE_SET`. `include/constants/pokemon.h` gives `NUMBER_OF_MON_TYPES` as eighteen,
`TYPE_MYSTERY` as nine, `TYPE_DRAGON` as sixteen and `TYPE_DARK` as seventeen, which is why an
all-thirty-one spread lands on Dark; the same file gives `MAX_IV_MASK` as thirty-one.
`Cmd_datahpupdate` selects the move's base type rather than the dynamic one when
`F_DYNAMIC_TYPE_IGNORE_PHYSICALITY` is set, and the decompilation's own comment states that Hidden
Power therefore only ever triggers Counter and that a Fire-typed Hidden Power cannot defrost a
target. Hidden Power's own entry in `src/data/battle_moves.h` is `.power = 1`, `.type =
TYPE_NORMAL`, `.accuracy = 100`, `.pp = 15`. In `CalculateBaseDamage` in `src/pokemon.c`, the burn
halving is `(attacker->status1 & STATUS1_BURN) && attacker->ability != ABILITY_GUTS`, applied to
the damage after the stat has been read; Marvel Scale and Guts are each tested as a one-and-a-half
multiplier contingent on `status1`; and Overgrow, Blaze, Torrent and Swarm are each tested as
`attacker->hp <= (attacker->maxHP / 3)` against their own move type. Species entries give Swellow
`{ABILITY_GUTS, ABILITY_NONE}`, Hariyama `{ABILITY_THICK_FAT, ABILITY_GUTS}`, Heracross
`{ABILITY_SWARM, ABILITY_GUTS}`, Milotic `{ABILITY_MARVEL_SCALE, ABILITY_NONE}`, Sceptile
`{ABILITY_OVERGROW, ABILITY_NONE}`, Blaziken and Swampert their own type's equivalents, and
Shedinja a base HP of one with `{ABILITY_WONDER_GUARD, ABILITY_NONE}`. `Cmd_maxattackhalvehp`
requires the Attack stat stage to be below `MAX_STAT_STAGE` **and** current HP to exceed half of
maximum HP, floors that half to one when maximum HP is one, and otherwise jumps to the failure
branch. Hidden Power's power formula changed in a later generation and nothing here is claimed
about any generation but the third.

The clinical reasoning is structural and will not date: the trade between resolution and
reproducibility, the conflation of reversible with irreversible causes, and the gap between a
snapshot and a trajectory are properties of any coarse assigned ordinal rather than of the current
scales. What moves is everything around it — which scale is recorded, the thresholds at which
particular regimens are considered, and whether structured geriatric assessment is routine in
older adults are set locally and nationally and are being revised, with geriatric assessment
expanding unevenly; patient-reported functional measures and objective activity data are being
investigated as complements and have no settled place. No category, cut-off or clinical figure is
quoted here, deliberately.
