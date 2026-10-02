---
id: "m066"
slug: shock-categories-by-mechanism
style: pokemon
category: emergency
difficulty: advanced
question: "Why are the categories of shock defined by mechanism rather than by blood pressure, and how can the pressure be normal while perfusion is not?"
tags: [shock, perfusion, classification, haemodynamics, revision]
---

# Who moves first is a product of seven factors, and the game only ever shows you the product

Open `GetWhoStrikesFirst` in Emerald's `src/battle_main.c` and the Speed used to decide a turn is
never a stat you can look up. It is built, in order, out of seven separate things:

the stored `speed` field; doubled if the holder has **Swift Swim** in rain — **Kingdra**,
**Magikarp**, **Lotad** — or **Chlorophyll** in sun, which **Bellossom** and **Exeggutor** carry;
multiplied by the Speed stat-stage ratio out of `gStatStageRatios`; multiplied by 110/100 if the
player holds the **Dynamo Badge**, which is Wattson's, the third gym in Hoenn; halved if the held
item's effect is `HOLD_EFFECT_MACHO_BRACE`; quartered if `status1` carries `STATUS1_PARALYSIS`;
and then, if the holder has a **Quick Claw** and that turn's roll comes in under the threshold,
thrown away entirely and replaced with `UINT_MAX`.

Seven factors, one product, and the product is the only thing the battle ever displays — as the
order in which two Pokémon act. There is no readout of the factors. That is the whole shape of the
argument about blood pressure: the measured quantity sits at the end of a chain of
multiplications, and a chain of multiplications is exactly the sort of thing that comes out normal
while a term inside it has collapsed.

## The same output, four different broken factors

```
   speed used   =   stored speed  ×  weather ability  ×  stat-stage ratio
                      ×  badge  ÷  Macho Brace  ÷  paralysis   → then maybe overridden
   ──────────────────────────────────────────────────────────────────────────────────────
   what is wrong          which factor            what fixes THAT factor   what it does
                          it touches                                       to the others
   ──────────────────────────────────────────────────────────────────────────────────────
   paralysis              ÷ 4                     Cheri Berry              nothing
   two Speed drops        × 10/20                 Haze, or switching out   nothing
   Macho Brace on         ÷ 2                     take the item off        nothing
   the rain stopped       × 2 gone                rain again               nothing
   ──────────────────────────────────────────────────────────────────────────────────────
   one observable: "it moved second".  Four mechanisms.  Four non-interchangeable answers.
```

The right-hand column is the entire reason a classification has to name mechanisms. Emerald draws
these distinctions in different *places in memory*, not as degrees of one thing. Paralysis lives
in `status1`. Stat stages live in `statStages[STAT_SPEED]`. The Macho Brace lives in the item
field. The weather lives in `gBattleWeather`. And the counters follow memory, not symptoms:
`gItemEffect_CheriBerry` is six bytes with one bit set at index 3, `ITEM3_PARALYSIS`, and it
reaches `status1` and nothing else — the same bit a **Thunder Wave** at 100 accuracy wrote there,
and the same bit a **Lum Berry** would have cleared as part of `ITEM3_STATUS_ALL`.
`Cmd_normalisebuffs`, which is what Haze runs, loops every battler and sets `statStages[j] =
DEFAULT_STAT_STAGE` — and never touches `status1`, so Haze on a paralysed Pokémon is a wasted turn
out of the 30 PP its entry gives it. Match the counter to the wrong factor and the product does
not move.

## Compensation: why the product can look untouched

This is the part that makes the point rather than decorating it, and it works with real base
stats, read from `src/data/pokemon/species_info.h`.

**Ninjask** has base Speed 160. Quarter it for paralysis and the figure going into the comparison
is a quarter of what it was — one of the seven factors has collapsed by a factor of four. Put it
against **Shuckle**, base Speed 5, and Ninjask still moves first. The observable is unchanged.
*Nothing in the battle tells you anything happened.*

Now the other way. **Jolteon** has base Speed 130 and nothing wrong with it at all except two
Speed drops, which is `gStatStageRatios[4]` — 10/20, a halving. Against Ninjask at 160 it loses
the comparison, and so does **Electrode** at 140, and **Slaking** at 100 was never in the
conversation. One **Agility**, which is `EFFECT_SPEED_UP_2` and so two stages at once, reverses
that again without touching anything else in the chain. The observable has flipped on a change of
two stages in a Pokémon with no status condition, no item penalty and no weather problem.

So the output moved when little was wrong and held still when a factor had been quartered. Read as
a measurement of the machinery, "it moved second" is close to worthless on its own; it only
becomes informative alongside what you know about the factors going in. That is the argument
against classifying by the pressure, stated in a system where you can read the source and check
it.

## The bracket above the product, and the one override

Two further pieces of the routine matter here, and both have counterparts.

**Priority is read before any of this.** As question m031 sets out, if the two chosen moves sit in
different brackets the function returns on the bracket comparison and the seven-factor product is
computed and then discarded. A forced ordering sits on top of the whole calculation. The
counterpart is the presenting problem that re-sorts everything in front of it regardless of what
the measured numbers say.

**And one of the seven is not a multiplication at all.** Quick Claw's hold effect does not scale
anything: `speedBattler1 = UINT_MAX`. It replaces the quantity with the largest number the field
can hold, one turn in a number given by the item's own `holdEffectParam`. A term that overwrites
the product rather than contributing to it is a useful thing to have in the vocabulary, because it
is the shape of a mechanical obstruction: not a factor turned down, but the chain short-circuited
somewhere along its length.

## What the product genuinely does tell you

Not nothing — and overcorrecting here is its own error.

* **Read repeatedly, it has a direction.** One comparison is a snapshot. The same comparison turn
  after turn, going the wrong way, is a trend, and a trend is about a factor even when a single
  reading is not.
* **Against a known baseline it is informative.** If you know what the order was at the start of
  the battle, a change in it is a measurement. The number alone is not; the displacement is.
* **An extreme value still binds.** A product low enough that no plausible arrangement of the
  other factors explains it narrows the field sharply. The problem with the measured quantity is
  that it is uninformative in the middle of its range, which is where it usually is.

## Where the metaphor stops

Plain prose from here, with no game in it, because this part is about people.

Shock is inadequate delivery of oxygen to tissue relative to what the tissue needs. It is defined
at the cell and not at the cuff, and that is why its categories have to name mechanisms. Arterial
pressure is the product of flow and resistance; flow is rate times the volume ejected per beat;
that volume depends on what filled the ventricle, how well it squeezed, and what it had to push
against. The four broad categories each name a different broken term — the filling, the squeeze, a
mechanical block, or the loss of resistance together with a failure in how flow is distributed and
extracted. A product is preserved when one term falls and another rises, so a normal pressure says
the product is normal and says nothing about the terms. That is **mechanism**: it follows from the
relationships and is checkable by reasoning. **(Definitional** for what the word shock names;
**country-dependent** for the naming and boundaries of the distributive group, which have been
revised more than once.**)**

Two consequences belong here rather than in any table. The pressure is a defended variable, held
by work the person is doing, so it moves late and it is held best by the people with the most
reserve — which makes a normal reading least reliable as reassurance in exactly the people whose
collapse is steepest. And real presentations are frequently mixed, with more than one term failing
at once, so a category is a hypothesis held alongside others and revisited, not a label applied
once.

No Pokémon stands for a patient anywhere in this answer, and no part of the game is being used to
represent a person, an outcome or anyone's chances. The game is carrying one idea and one only:
the shape of a quantity that is computed as a product and observed only as the product. What that
shape costs when the quantity belongs to a person is not a mechanic, is not entertaining, and is
stated above without ornament. Nothing in this answer is a management sequence, a threshold or a
direction of action, and nothing in it is usable for a decision about anyone.

## What a Gym Leader is listening for

* Name the seven things that go into the Speed the turn-order routine compares, in order.
* Ninjask is paralysed and still moves first against Shuckle. What has the observable told you,
  and what has it hidden?
* Why is Haze useless against paralysis and a Cheri Berry useless against a Speed drop? What is
  the general principle there?
* Quick Claw sets the value to `UINT_MAX` rather than multiplying it. Why is a term that replaces
  the product worth a separate name?
* The product is uninformative in the middle of its range. What makes it informative anyway?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* A current standard textbook of **emergency medicine or of intensive care medicine**, for the
  definitions, the categories and the physiology of oxygen delivery.
* The current sepsis recognition and management guidance issued by **the reader's own national
  body for clinical guidelines**, which is where the distributive category's definitions and
  terminology actually live.
* The current major haemorrhage and trauma guidance issued by **the reader's regional or national
  trauma network**.
* **The reader's own employing organisation's** recognition-and-escalation policy, which governs
  practice where they work and outranks every general account including this one.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why a classification has the categories it has*, written for
someone already trained, and the Pokémon framing covers one thing: a quantity computed as a
product and observed only as the product. It is deliberately not a protocol and not a decision aid
— no management sequence, no thresholds, no doses, no rates, no volumes, no settings, and nothing
to consult while acting. The vocabulary and boundaries of the shock categories differ between
countries and institutions and have been revised. The reader's own national guidance and local
policy are the authority; this is not, and it has had no clinical review. Nothing here describes
any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. The seven-factor Speed calculation, the
Macho Brace halving, the paralysis quartering, the Dynamo Badge multiplier and the Quick Claw
override to `UINT_MAX` are read from `GetWhoStrikesFirst` in `src/battle_main.c`; the stat-stage
ratio table including 10/20 at minus two stages is `gStatStageRatios` in `src/pokemon.c`; the
Cheri Berry's single `ITEM3_PARALYSIS` bit is `src/data/pokemon/item_effects.h`; Haze's reset of
every battler's stat stages and its silence on `status1` is `Cmd_normalisebuffs` in
`src/battle_script_commands.c`; and the base Speeds of 160 for Ninjask, 130 for Jolteon and 5 for
Shuckle are from `src/data/pokemon/species_info.h`. Those are Generation III figures and some have
changed since — base stats and the paralysis divisor have both been revised in later games — so a
reader checking today's values should check today's game rather than this page. On the clinical
side, the mechanistic classification is mainstream and the vocabulary is not: the naming of the
distributive group, the sepsis definitions and every threshold attached to recognising poor
perfusion have moved and will move again. Principle dated October 2026; read the current national
guidance and local policy for anything past the principle.
