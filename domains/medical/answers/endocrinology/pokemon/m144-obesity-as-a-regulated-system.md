---
id: "m144"
slug: obesity-as-a-regulated-system
style: pokemon
category: endocrinology
difficulty: advanced
question: "Body fat mass is a regulated variable with a defended level. What does treating it as regulated rather than as an accumulation change?"
tags: [obesity, energy-homeostasis, leptin, set-point, adipose-tissue]
---

# Two multipliers push an effort value up and nothing anywhere multiplies a decrease, and a stat stage is not a stat

Before anything else, what this answer is **not** doing. No Pokémon here stands in for a person or
for a person's body. **Snorlax** does not appear in this answer except in the section where I
explain why it does not, and no species is cast as a size. The subject is a **stored number in a
struct**, the loop that writes it, and the loop that defends it — and the games turn out to model
the thing that matters about that loop, which is that it is strongly asymmetrical, more exactly
than I expected.

Here is the fact the whole answer hangs on. `MonGainEVs` adds effort values from ordinary play. It
carries **two multipliers**, both of which double the gain:

```
   if (CheckPartyHasHadPokerus(mon, 0))   multiplier = 2;   else multiplier = 1;
   ...
   if (holdEffect == HOLD_EFFECT_MACHO_BRACE)   evIncrease *= 2;
```

And to reduce an effort value there is exactly one route: six specific Berries,
`ITEM6_SUBTRACT_EV`, defined as **−10**, one at a time, each consumed in the using
(**mechanism**). There is **no multiplier anywhere in the source on a decrease.** Two doublings
up. None down. One scarce consumable at a fixed step. That is the asymmetry of this loop written
as data, and it was not put there to model anything.

| In the battle | What it stands for |
| --- | --- |
| An **Effort Value**, stored, capped, never displayed | The regulated quantity: stored, and not the number you read |
| `MonGainEVs` running on ordinary play, no item, no decision | Accumulation that needs nothing to be decided |
| **Pokérus** doubling it, and **Macho Brace** doubling it again | Two multipliers, both on the way up |
| `ITEM6_SUBTRACT_EV` = **−10**, and no multiplier anywhere | The only route down: fixed step, scarce, one at a time |
| **Pomeg**, **Kelpsy**, **Qualot**, **Hondew**, **Grepa**, **Tamato** | Six items, six stats, consumed on use |
| **HP Up**, **Protein**, **Iron**, **Carbos**, **Calcium**, **Zinc**, +10 | And an item route up that stops early, at `EV_ITEM_RAISE_LIMIT` |
| `if (pokerus == 0) pokerus = 0x10;` | A ratchet: a transient state leaving a permanent marker |
| `CheckPartyHasHadPokerus` reading the **whole** byte | The gain stays doubled after the thing that doubled it has gone |
| `hpEV / 4` inside `CalculateMonStats` | Small reductions buying nothing visible |
| Maximum HP from base, **Individual Values** and effort, in one number | A single figure that cannot be decomposed into what made it |
| **Grassy Terrain** at full strength over a **Flygon** | Signal maximal, receiver not grounded, no response |
| `TryChangeBattleTerrain` returning FALSE on its own terrain | Supplying more of a signal already present, to no effect |
| No terrain at all, and then **Tapu Bulu** entering | The rare case where supplying the signal works |
| **Gravity**, an **Iron Ball**, **Ingrain** — tested *first* | Acting on the receiver rather than on the signal |
| **Leftovers** every turn against a **Sitrus Berry** at a threshold | The long clock and the short clock, into one controller |
| A **Stat Stage**, multiplying, stored nowhere, cleared by **Haze** | A change that is real while applied and leaves no record |
| A **Soothe Bell**'s ×150÷100, truncating | A modifier that does nothing where the step is smallest |
| A **Luxury Ball**'s +1, on positive changes only | A modifier written to work in one direction |
| A **Rare Candy** writing the table value outright | A readout moved, and the record of how destroyed |
| **Shedinja**'s hard-coded 1 in `CalculateMonStats` | A formula with a branch where it does not apply |
| A **Rare Candy** writing the experience field outright | A readout with no trajectory kept behind it |
| `GetDrainedBigRootHp`, and a **Big Root** in the slot | A multiplier that applies to what is gained |
| **Snorlax**, deliberately not used anywhere | See the declining section |

**This answer defers to four others.** m021 owns the two-break distinction and its second break —
the loop still running with the gain turned down — which is the whole of the resistance section.
m022 owns **Leftovers** against a **Sitrus Berry** as continuous against threshold-triggered. m084
owns **Pokérus**' permanent marker and the ever-had query. m142, written alongside this one, owns
`gStatStageRatios` as the *size* of a response; here the interest is a different property of the
same table, which is that a stage is not stored at all. None of them is re-argued.

Clinical claims are marked (**mechanism**), (**definitional**), (**consensus**) or
(**country-dependent**), and where a question is genuinely **unsettled** this answer says so in
that word rather than reaching for a marker. The Pokémon mechanics carry no clinical marker; the
Sources section says where each was read.

## The loop, with both clocks and both multipliers drawn in

```
   WHAT WRITES THE STORED NUMBER, AND WHAT READS IT

   ── THE LONG CLOCK ────────────────────────────────────────────────────────
   the store itself reports its own size, continuously, like LEFTOVERS:
   maxHP/16 at the end of every turn, invisible per turn, decisive over many

   ── THE SHORT CLOCK ───────────────────────────────────────────────────────
   and a threshold-triggered event, like a SITRUS BERRY at hp <= maxHP/2:
   fires once, on a condition, and is gone

        both of them arrive at the SAME controller — m022's pair, doing a
        second job: there it was basal against bolus, here it is the size
        of the store against what has just happened

                            │
                            ▼
   ╔══════════════════════ THE CONTROLLER ══════════════════════╗
   ║  two opposing populations reading the same two inputs      ║
   ║    one pushes the number down · one pushes it up           ║
   ╚═════════════════════════╤══════════════════════════════════╝
                             │
        ┌────────────────────┴────────────────────┐
        ▼                                         ▼
   WHAT GOES IN                            WHAT IS SPENT
   MonGainEVs, from ordinary play           and this arm is the one
   × 2 if CheckPartyHasHadPokerus           everybody forgets
   × 2 if HOLD_EFFECT_MACHO_BRACE
        │                                         │
        └────────────────────┬────────────────────┘
                             ▼
                   THE STORED NUMBER
                   capped: MAX_PER_STAT_EVS 255, MAX_TOTAL_EVS 510
                             │
                             ▼
   ── AND THE ONLY ROUTE DOWN ───────────────────────────────────────────────
      a POMEG BERRY.  ITEM6_SUBTRACT_EV = −10.  One stat. Consumed.
      No Pokérus doubling. No Macho Brace doubling. No multiplier exists.

   Two multipliers up. Zero down. The asymmetry is in the data, not the play.
```

## The asymmetry, read straight out of the item table

Six Berries reduce an effort value and that is the entire inventory: **Pomeg** for HP, **Kelpsy**
for Attack, **Qualot** for Defence, **Hondew** for Special Attack, **Grepa** for Special Defence
and **Tamato** for Speed. Each entry in `item_effects.h` is four lines:

```
   const u8 gItemEffect_PomegBerry[10] = {
       [4] = ITEM4_EV_HP,
       [5] = ITEM5_FRIENDSHIP_ALL,
       [6] = ITEM6_SUBTRACT_EV,        // −10
       EV_BERRY_FRIENDSHIP_CHANGE,     // +10 / +5 / +2 by friendship band
   };
```

Four properties, and each one is doing clinical work (**mechanism**).

**The step is fixed and small.** −10, every time, whatever the current value. Nothing accelerates
it, nothing scales it to how far there is to go.

**It is a consumable.** One Berry, one step, gone. Accumulation needed no item at all; reduction
needs an item per step.

**It raises friendship in the same instruction**, by +10, +5 or +2 depending on which band the
counter is in — so the thing that reduces the stored number also moves a *different* stored
number, and the party-menu routine has a message for the case where friendship moved and **the
effort value could not fall**. An intervention with an effect on something adjacent and sometimes
no effect on its target is an honest piece of data to have found.

**And the vitamin route up stops early.** **HP Up**, **Protein**, **Iron**, **Carbos**,
**Calcium** and **Zinc** each add +10, and the code caps them at `EV_ITEM_RAISE_LIMIT`, which is
**100** — so the item route up hits a ceiling that ordinary play does not, because `MonGainEVs`
goes all the way to `MAX_PER_STAT_EVS` at 255. The deliberate route is limited and the passive
route is not.

One-directional modifiers turn up elsewhere in the same save data, which is worth one paragraph
because it shows the asymmetry is a habit of the design rather than an accident of this table.
m094 read the friendship routine out of the source: a **Luxury Ball** adds 1 to every **positive**
friendship change and nothing to a negative one, and a **Soothe Bell** multiplies a positive
change by 150 and divides by 100 with integer truncation — so it does **precisely nothing** when
the increment is 1 (**mechanism**). An amplifier that is invisible exactly where the step is
smallest, and a bonus written to apply in one direction only. The games keep doing this, and the
loop in a person keeps doing it too.

The clinical statement that maps onto that stack is this one, and it is consensus rather than
mechanism because it rests on measurement (**consensus**). Reducing the store provokes a
coordinated, multi-channel, **sustained** response: energy expenditure falls by more than the lost
tissue accounts for, hunger signalling rises, satiety signalling falls, and none of it resolves
when the reduction stops. Increasing the store provokes something much weaker. Two multipliers up,
none down.

And one consequence of that which the house conventions require me to state where it belongs
rather than at the end: **return towards the defended position after a reduction is the predicted
behaviour of this loop.** It is what a system with two multipliers in one direction does when the
applied force is removed. Nothing in `MonGainEVs` is a statement about anybody's effort, and nor
is the real thing.

## The ratchet, which is one line and a wrong-looking query

`UpdatePartyPokerusTime` runs the **Pokérus** clock down and then does something odd:

```
   if ((pokerus & 0xF) < days || days > 4)   pokerus &= 0xF0;   // active phase over
   else                                      pokerus -= days;
   if (pokerus == 0)                         pokerus = 0x10;    // ← this line
```

When the active phase ends, the low nibble clears — and if that would leave the byte at zero, the
code **writes the high nibble back in** so that the record of having had it survives
(**mechanism**). And the query that `MonGainEVs` uses is `CheckPartyHasHadPokerus`, which tests
the **whole byte** rather than the active nibble. Its sibling two functions above tests `& 0xF`
and is the one that asks whether it is active now.

So the doubling is permanent. The transient state is gone, the marker it left is not, and the
function that decides how fast the stored number grows reads the marker (**mechanism**). m084
found this in general practice as labelling that outlives what it labelled; here it is the gain on
an accumulation loop, changed once and never changed back.

That is the shape of a defended position that has **moved upward and is now defended at the new
level** (**consensus**). A spring returns to one position from either side; this does not. **By
what mechanisms the defended position moves, and how reversibly, is not settled**, and I am not
going to let a satisfying line of C imply that it is.

## A stat stage is not a stat, and nothing records that it happened

`gStatStageRatios` is thirteen rows, from 10/40 at −6 to 40/10 at +6, and a stage **multiplies the
computed value**. The value itself comes from somewhere else entirely:

```
   newMaxHP = (((2 * baseHP + hpIV + hpEV / 4) * level) / 100) + level + 10
```

A stage touches none of those terms. It is held in `gBattleMons[]` for the duration of a battle,
it is discarded when the battler switches out, and **Haze** — `Cmd_normalisebuffs` — writes
`DEFAULT_STAT_STAGE` into every stat of every battler on the field in one loop (**mechanism**).
m142 uses the same table for the *magnitude* of a response; the property that matters here is the
other one. **A stage is not stored.** Whatever happened to it, the stored value is exactly what it
was.

That is the difference between acting on the regulated variable and acting on the regulation, and
it is the most useful thing in this answer. A six-stage reduction is enormous — a quarter of the
value — and it is real while it lasts, and it leaves no trace in the save data. Changing the
stored number requires something that writes to `hpEV`, and the only things that do are
`MonGainEVs`, the six Berries, the six vitamins and a level-up recalculation.

And the integer division is worth one sentence, because it is the quietest unfairness in the
formula: `hpEV / 4`. Three effort points buy nothing. At the scale the stat is computed on, a
small reduction in the stored number does not move the displayed number at all (**mechanism**).

And one more thing the save data does not keep, which m087 found in dermatology. A **Rare Candy**
does not add experience: its `ITEM3_LEVEL_UP` branch in the item-effect routine **writes**
`gExperienceTables[growthRate][level + 1]` into the experience field outright, discarding whatever
progress was already there (**mechanism**). The readout moves and the record of how it got there
is destroyed. A weight recorded at one appointment is the same kind of object: a current value
with no trajectory attached, and the trajectory is usually the more informative of the two.
Nothing in `CalculateMonStats` keeps a previous maximum either — it reads the old value only to
compute a delta for a message and then overwrites it, which m094 used for the absence of a stored
baseline.

## Signal maximal, receiver not grounded

Now the resistance, and this is where the specialty's own terrain layer carries the argument with
nothing added to it.

Terrain reaches **grounded** battlers only. Put **Grassy Terrain** up at full strength — five
turns, eight if **Tapu Bulu** was holding a **Terrain Extender** — and a **Flygon** feels
precisely none of it, because **Levitate** is its only ability in both slots (**mechanism**).
**Claydol** is the sharper example: a **Ground** type that is not grounded. The field is maximal.
The receiver is not in contact with it. Nothing is wrong with the field.

Two code facts finish the argument.

**More signal accomplishes nothing.** `TryChangeBattleTerrain` returns FALSE when the requested
terrain is already up, without even refreshing `terrainTimer` (**mechanism**). Sending a second
**Tapu Bulu** in does not produce more field.

**And the overrides are tested before the exemptions.** In `IsBattlerGroundedInverseCheck`, an
**Iron Ball**, **Gravity**, the **Ingrain** root and **Smack Down** each `return TRUE` *above* the
lines that exempt **Levitate**, an **Air Balloon**, **Magnet Rise**, **Telekinesis** and the
Flying type (**mechanism**). **Gravity** beats **Levitate**. m091 established that ordering for
the pituitary answer.

Read those three together and you have the therapeutic situation exactly (**consensus**). In
common obesity the circulating store hormone is **high**, not low; giving more of it does not
produce the expected response; and that is not a dosing problem. This is m021's second break — the
loop running with the gain turned down — rather than its first. The decisive contrast is that in
the **rare** congenital deficiency of that hormone there is no field at all, so **Tapu Bulu**
entering an empty field does exactly what the diagram says it should, and replacement works
dramatically. Empty field: set it. Field already up over a **Flygon**: setting it again is not the
intervention.

What is the intervention is **Gravity** — something that acts on whether the receiver is in
contact at all. The interventions understood to work in this condition act on the regulating
circuits rather than against the regulated variable: pharmacotherapy engaging the gut-hormone
satiety arms of the same controller, and metabolic and bariatric surgery, where a purely
restrictive explanation is now considered incomplete and changes in gut-hormone signalling and in
the defended level are understood to carry much of the effect (**consensus**). Which procedures
and which agents are available, to whom and on what criteria, differ markedly by country and
health system, and **no agents, doses, eligibility criteria or outcome figures appear in this
answer** (**country-dependent**).

## One number, four contributors, and no decomposition anywhere

Read the maximum-HP formula once more as a measurement instrument rather than as arithmetic:

```
   newMaxHP = (((2 * baseHP + hpIV + hpEV / 4) * level) / 100) + level + 10
```

Four inputs. **Base stat**, which is the species. An **Individual Value**, fixed at creation and
displayed nowhere. An **Effort Value**, accumulated and displayed nowhere. And level. The output
is one number on the status screen, and **nothing in the game shows you the decomposition**
(**mechanism**). Two Pokémon of the same species at the same level can show the same maximum HP
having arrived there by different combinations, and the combination is what you actually wanted to
know.

That is a ratio of mass to height squared, and the objection to it is the same objection: the same
value arises from different combinations of fat mass, lean mass and frame, and the number does not
say which (**mechanism**). It performs reasonably as a descriptor of a group and poorly as a
description of an individual, which is a property of that kind of measure rather than a defect
peculiar to this one. Where the store sits matters more for metabolic risk than its total does,
which is why a waist measurement is recorded alongside it or instead of it (**consensus**).

And the formula has a hard-coded exception. `CalculateMonStats` begins:

```
   if (species == SPECIES_SHEDINJA)   newMaxHP = 1;
```

The function has a branch where its own formula does not apply. That is the *shape* of a measure
whose relationship to what it predicts is not the same everywhere — and several countries and
bodies apply different cut-offs for some populations on exactly that basis
(**country-dependent**). I am using the shape and stopping there: I am not casting a species as a
population, which would be grotesque, and no cut-offs from any system appear here.

## The mapping I am declining

Four refusals, and the first is the reason this answer is built the way it is.

**I am not casting any Pokémon as a body, and specifically not Snorlax.** It is the mapping
everybody thinks of within two seconds, it would have scored perfectly well, and it is exactly the
kind of joke the house rule about checking a joke against "would I say this in front of somebody
who has it" exists to catch. The whole topic is one where the register of the writing is part of
the harm or part of the remedy, so the metaphor stays on the **loop**: a stored integer, the
function that writes it, the multipliers on that function, and the absence of multipliers in the
other direction. Nothing above is about how a creature looks.

**And nothing stands in for a person's appearance, size or effort.** `MonGainEVs` is a function.
The reason that matters is in the plain prose below: this is the condition most often treated in
clinical settings as evidence about somebody's character, and an analogy that repeated the mistake
would be worse than no analogy.

**I am not building a fifth terrain for the store hormone.** Adipose tissue is a secreting organ,
which makes it a setter, and a setter wants a field. m094 declined to invent a fifth terrain for
the growth-hormone axis and said so in a section like this one; the four are assigned — **Grassy
Terrain** thyroid hormone, **Psychic Terrain** cortisol, **Misty Terrain** calcium, **Electric
Terrain** the reproductive clock — and the games give exactly four, one at a time. So this answer
borrows the **grounding check** from that layer, which is the part it actually needed, and keeps
the store itself in the stat-and-effort layer where a stored number belongs. Extending the layer
downward beats adding to it sideways.

**And I am not pretending the code settles what is unsettled.** The **Pokérus** line is a
beautiful ratchet and it tells you nothing about *how* a defended position moves upward in a
person, which is an open question. The relative contributions of the food environment, sleep, the
gut microbiome, early life and genetics are not settled and the primary literature is where to
read about them. A satisfying line of C is not evidence.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a stored quantity with two multipliers on its accumulation, no
multiplier on its reduction, one scarce fixed-step route down, a marker that permanently changes
the gain, a transient multiplier that leaves no record, and a receiver that can be out of contact
with a maximal signal. That picture is fair and the conclusion it supports is the right one:
durable change in a regulated quantity requires acting on the regulation.

Here is what the picture cannot carry, and in this topic it is the more important half.

People with obesity are routinely treated, in clinical settings, as though the condition were
evidence about their character. That is a documented phenomenon with measurable consequences:
avoidance of health care, delayed presentation of unrelated conditions, and symptoms attributed to
weight without being investigated. Somebody who has been weighed and lectured at every appointment
for twenty years has a rational basis for not attending the next one, and the clinical cost of
that is borne by the person and caused by the service.

The mechanism above is, among other things, a correction to that. A loop that defends one
direction strongly returns towards its defended position when the applied force stops. That is the
expected behaviour of the system, and it is recorded in notes as failure, relapse and
non-adherence — three words that describe a person rather than a loop.

Stigma is also not confined to clinicians. It is in the equipment, the furniture, the gowns, the
cuffs, and the width of a chair in a waiting room, and the absence of a thing that fits is a
message whether or not anybody intended one.

The language used about this condition is contested by the people who have it, with reasonable
disagreement about which terms are acceptable and to whom. Asking rather than assuming is the only
general rule available.

A note about who is reading. Anybody reading about this is more likely to be living with it than
revising it. If that is you: there are deliberately no numbers, cut-offs, categories, drugs or
diets anywhere on this page, and nothing here is advice about your body. What the mechanism does
say is that the thing being described is a regulated physiological system and not a verdict about
you. Anything about what to do belongs with your own clinical team — who can also be asked to
investigate a symptom on its merits.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* A current textbook of endocrinology or metabolic physiology, for the hypothalamic circuitry, the
  long-term and short-term signals and their convergence, and the experimental basis of adaptive
  thermogenesis.
* **The primary literature**, for the magnitude and persistence of the counter-regulatory response
  to reduction, for the mechanism of metabolic surgery, and for everything this answer marks as
  unsettled. This field moves faster than a revision page.
* Your national guidance on the assessment and management of obesity, for the measures
  recommended, the cut-offs applied and to which populations, referral criteria, and what is
  commissioned where you work.
* **Your national formulary**, for anything about a medicine in this area. No agents are named
  here and the formulary is the authority.
* Your national or specialty-society guidance on metabolic and bariatric surgery, for eligibility,
  procedures and follow-up.
* Published guidance from the relevant professional bodies on **weight stigma in health care and
  on language**, which exists, is specific, and is not in a physiology textbook.

The Pokémon side is different and is sourced properly. `MonGainEVs` taking `multiplier = 2` from
`CheckPartyHasHadPokerus(mon, 0)` and multiplying again for `HOLD_EFFECT_MACHO_BRACE`, and capping
at `MAX_PER_STAT_EVS` 255 and `MAX_TOTAL_EVS` 510; the six EV-lowering Berries — **Pomeg**,
**Kelpsy**, **Qualot**, **Hondew**, **Grepa** and **Tamato** — each carrying `ITEM4_EV_*`,
`ITEM5_FRIENDSHIP_ALL`, `ITEM6_SUBTRACT_EV` defined as **−10** and the
`EV_BERRY_FRIENDSHIP_CHANGE` triple of +10, +5 and +2; `ItemUseCB_ReduceEV` having a distinct
message for the case where friendship moved and the effort value did not; the vitamins carrying
`ITEM6_ADD_EV` of **+10** against `EV_ITEM_RAISE_LIMIT` of **100**; `UpdatePartyPokerusTime`
clearing the low nibble and then writing `0x10` back when the byte would be zero, with
`CheckPartyHasHadPokerus` testing the whole byte against the sibling function's `& 0xF`;
`gStatStageRatios`' thirteen rows from 10/40 to 40/10 and `Cmd_normalisebuffs` writing
`DEFAULT_STAT_STAGE` to every stat of every battler; `CalculateMonStats` computing maximum HP as
`(((2 * baseHP + hpIV + hpEV / 4) * level) / 100) + level + 10` with its `SPECIES_SHEDINJA` branch
returning 1; `TryChangeBattleTerrain` returning FALSE when the terrain is already the one
requested, without refreshing `terrainTimer`, which is 8 with a **Terrain Extender** and 5
without; `IsBattlerGroundedInverseCheck` testing an **Iron Ball**, **Gravity**, the root volatile
and **Smack Down** before exempting **Levitate**, an **Air Balloon**, **Magnet Rise**,
**Telekinesis** and the Flying type; and **Flygon** being Ground and Dragon with `abilities =
{ABILITY_LEVITATE, ABILITY_LEVITATE}` while **Claydol** is Ground and Psychic with **Levitate**
were all read from the pokeemerald and pokeemerald-expansion decompilations rather than from
memory, as were the **Rare Candy**'s `ITEM3_LEVEL_UP` branch writing
`gExperienceTables[growthRate][level + 1]` into the experience field rather than adding to it,
`CalculateMonStats` reading the old maximum only to compute a message delta before overwriting it,
and `GetDrainedBigRootHp` being the function `HandleEndTurnIngrain` calls on its `maxHP / 16`. The
**Soothe Bell** and **Luxury Ball** arithmetic is m094's reading and is reused on its authority.
The effort-value system, the six Berries and the vitamin cap are Generation III as described and
the effort mechanics were revised in later generations; the terrains, their **Tapu** setters and a
**Terrain Extender** are Generation VII and VIII, and **Gravity**, **Smack Down** and **Magnet
Rise** are Generation IV or later.

## Scope and safety

The Pokémon here is doing one job: making it concrete that a stored quantity can have multipliers
on its accumulation and none on its reduction, that a transient multiplier leaves no record while
a stored value does, and that a maximal signal reaching a receiver that is not in contact with it
is not a problem of signal strength. It is not a clinical reference, not a decision aid, not
advice about anybody's weight, and not about any individual's care. **No body-mass-index values,
cut-offs, waist measurements, categories, drug names, doses, eligibility criteria or outcome
figures appear here on purpose** — this is the subject where a number lifted from a revision page
is most likely to be read as a verdict about the reader. Check your own national guidance and your
national formulary. Nothing here has had clinical review. **No Pokémon in this answer stands in
for a person, a body, a size or anybody's effort**, and a symptom deserves investigation on its
merits regardless of anybody's weight.

## What a Gym Leader digs into next

* Where are the two multipliers in `MonGainEVs`, and why does it matter that there is no
  counterpart on `ITEM6_SUBTRACT_EV`?
* Why is a **Pomeg Berry** raising friendship in the same instruction an honest thing to have
  found?
* Why does the vitamin cap at 100 sit below `MAX_PER_STAT_EVS` at 255, and what does that say
  about deliberate against passive routes?
* Why does `if (pokerus == 0) pokerus = 0x10;` make the gain permanent, and which query makes it
  matter?
* Why is a **Stat Stage** not a stat, and what is the clinical version of that distinction?
* Why does a maximal **Grassy Terrain** over a **Flygon** place this in m021's second break rather
  than its first?
* Why is **Gravity** the intervention and a second **Tapu Bulu** not?
* Why can `(((2 * baseHP + hpIV + hpEV / 4) * level) / 100) + level + 10` not be run backwards
  from its output?

## Where this stands, October 2026

The loop, its two clocks, the asymmetry of its defence, the persistence of the counter-regulatory
response, the location of the defect on the response side rather than the signal side, and the
general principle that durable change in a regulated quantity requires acting on its regulation
are mechanism and settled consensus, and do not date. What dates on the Pokémon side is the
constants: the effort-value system described here is Generation III, the per-stat and total caps
and the vitamin limit were revised in later generations, **Pokérus**' arithmetic and the
EV-lowering Berries' fixed −10 are Advance-era specifics, and the terrains with their **Tapu**
setters are Generation VII and VIII while **Gravity**, **Smack Down** and **Magnet Rise** are
Generation IV or later. Check the current generation's data. On the clinical side a great deal
moves: the mechanisms by which the defended position shifts, the contributions of environment,
sleep, microbiome, early life and genetics, the pharmacology of this area — which has changed
faster than anything else in this specialty in recent years — the mechanistic account of metabolic
surgery, which measures and cut-offs apply to which populations, commissioning and eligibility,
the disease-classification question, and the guidance on language and stigma. All
country-dependent, revised, or openly unsettled. Check current local guidance, your national
formulary and the primary literature.
