---
id: "m077"
slug: pharmacogenomics-and-the-population-dose
style: pokemon
category: pharmacology
difficulty: advanced
question: "A licensed dose is a choice made for a population. What does a pharmacogenomic result actually change about that choice, and why does knowing a genotype so often leave the prescription unchanged?"
tags: [pharmacogenomics, metaboliser-phenotype, prodrugs, variability, equity]
---

# One bit of a 32-bit number decides whether a Snorlax has Immunity or Thick Fat.

The Game Boy Advance games keep the population figure and the individual figure in the same
expression, which is the cleanest statement of this topic anywhere.

```
   #define CALC_STAT(base, iv, ev, statIndex, field)                   \
       u8 baseStat = gSpeciesInfo[species].base;                       \
       s32 n = (((2 * baseStat + iv + ev / 4) * level) / 100) + 5;     \
       n = ModifyStatByNature(GetNature(mon), n, statIndex);

   baseStat   the SPECIES figure. Identical for every Snorlax ever made.
   iv         the INDIVIDUAL figure, 0-31, drawn once and never changed.
   ev         the ACQUIRED figure, which is what happened to this one.

   All three are added INSIDE the same bracket, then scaled together. So the
   individual deviation is magnified by exactly the same factor as the species
   figure -- which is why individual variation gets bigger in absolute terms as
   the body gets bigger, and why "it is only an IV" stops being true.
```

Base stats are the licensed dose: chosen for a species, correct for nobody in particular. The
Individual Values are the reason that is a bet.

## A two-allele locus, written as `personality & 1`

```
   CreateBoxMon:
       if (gSpeciesInfo[species].abilities[1])
       {
           value = personality & 1;
           SetBoxMonData(boxMon, MON_DATA_ABILITY_NUM, &value);
       }

   GetAbilityBySpecies(species, abilityNum):
       return abilityNum ? abilities[1] : abilities[0];
```

One bit of one 32-bit word, drawn from `Random32()` and never rewritten. And the Emerald data
splits every species into three kinds of locus, which is exactly the split that decides whether a
test is worth running.

| Locus | Species, with the data | What a test of that one bit tells you |
| --- | --- | --- |
| Polymorphic, and the two alleles do different things | **Snorlax** `{Immunity, Thick Fat}`; **Chansey** and **Blissey** `{Natural Cure, Serene Grace}`; **Onix** `{Rock Head, Sturdy}`; **Magnemite** `{Magnet Pull, Sturdy}`; **Farfetch'd** `{Keen Eye, Inner Focus}` | everything: being unable to be poisoned and halving incoming Fire and Ice are not neighbouring phenotypes |
| Polymorphic in the data, silent in effect | exactly three species: **Granbull** `{Intimidate, Intimidate}`, **Vibrava** and **Flygon** `{Levitate, Levitate}` | nothing. The bit is written, the bit is read, and both answers are the same ability |
| Monomorphic — `abilities[1]` is `ABILITY_NONE` | **Shuckle** `{Sturdy}`, **Gastly** `{Levitate}`, **Ditto** `{Limber}`, **Smeargle** `{Own Tempo}`, **Pikachu** `{Static}`, **Groudon** `{Drought}`, and most of the Pokédex | nothing, and the test never even runs: the `if` is false and the bit is not written at all |

Three classes, one test. That is the coverage argument made concrete: a panel that reads
`personality & 1` is decisive for a **Snorlax**, a silent variant on a **Flygon**, and
uninformative on a **Shuckle** — and the panel cannot tell you which it is looking at. "No
actionable variant detected" means *this locus, in this population*, and nothing more.

## Hidden Power is a phenotype computed from a genotype nothing displays

This is the best single mechanic in the games for the topic, because the arithmetic is written
out.

```
   Cmd_hiddenpowercalc  -- TWO bits of each of the six IVs, doing two different jobs

   powerBits  =  bit 1 of hpIV, attackIV, defenseIV, speedIV, spAttackIV, spDefenseIV
   typeBits   =  bit 0 of the same six

   gDynamicBasePower       = (40 * powerBits) / 63 + 30        range 30 .. 70
   dynamicMoveType         = ((NUMBER_OF_MON_TYPES - 3) * typeBits) / 63 + 1
                             (then stepped past Normal, and past TYPE_MYSTERY)

   powerBits    0     16     32     48     63
   base power  30     40     50     60     70
```

Twelve bits. One of them decides nothing you can see, and six of them together decide which of
sixteen types the move counts as. Two **Ditto** of the same level with the same move in the same
slot produce different types and different base powers, and **nothing on the sprite, the summary
screen or the Pokédex entry shows it**. `m020` made that point about the Nature; here the hidden
value is doing arithmetic.

## The sign flip, which is where everyone loses the mark

Those twelve bits are not good or bad. They are good or bad *given what you point them at*.

```
   Suppose typeBits computes to Ground.

   into Magnemite  { TYPE_ELECTRIC, TYPE_STEEL }    ×2 and ×2  ──►  ×4
   into Flygon     { TYPE_GROUND, TYPE_DRAGON }
                   abilities = { Levitate, Levitate }           ──►  ×0

   SAME genotype. SAME move. SAME computed type and power.
   Opposite consequence, and the thing that decides is not in the genotype.
```

That is the prodrug reversal, and `m007` is where the zero itself is argued: Ground into
**Flygon** is not weak, it is absent, and `m044`'s point applies too — no increase in the
delivered amount crosses a zero. A metaboliser phenotype has exactly this shape. The activity
figure is the same number; whether low activity means too much drug or too little depends on
whether the molecule administered was the active one, and the genotype report does not know.

And note what makes **Flygon** a triple lesson here. Its ability bit is a silent variant, its
typing makes a Ground reading meaningless, and **Vibrava**, the stage before it, carries the same
duplicated slot. One species, three separate reasons a result can be true and useless.

## Nature: a second locus, smaller, directional, and blind to one output

```
   GetNature(mon)  =  personality % NUM_NATURES        NUM_NATURES = 25

   gNatureStatTable[nature][5]  over Attack, Defense, Speed, Sp.Atk, Sp.Def
       Adamant  { +1,  0,  0, -1,  0 }
       Impish   {  0, +1,  0, -1,  0 }
       Lonely   { +1, -1,  0,  0,  0 }
       Naughty  { +1,  0,  0,  0, -1 }
       Sassy    {  0,  0, -1,  0, +1 }

   ModifyStatByNature:  +1 -> stat × 110 / 100,  -1 -> stat × 90 / 100

   and, first line of the routine:
       if (statIndex <= STAT_HP || statIndex > NUM_NATURE_STATS) return stat;
       ──► NO Nature modifies HP. Five of the five natures above leave it alone,
           and so do the other twenty.
```

A tenth, up on one output and down on another, five of the twenty-five natures neutral, and one
output immune to the whole locus. That is a variant that explains part of the variance and not
most of it: the same **Snorlax** can be **Adamant** or **Sassy**, and its maximum HP is identical
either way. Knowing the Nature tells you something real about two numbers and nothing whatever
about a third.

## Phenoconversion: Skill Swap never touches `abilityNum`

**Role Play** (power 0, accuracy 100, 10 PP) copies the target's ability onto the user. **Skill
Swap** (power 0, accuracy 100, 10 PP) exchanges them. Neither writes `MON_DATA_ABILITY_NUM`; both
change what is *expressed* for the rest of the fight.

So a **Snorlax** whose stored bit says **Thick Fat** can be standing there not having it, and a
read of the stored byte will still say **Thick Fat**, correctly, and be clinically wrong. That is
phenoconversion in one sentence, and `m009` is the interaction half: the genotype is not the
phenotype, and the list of what else is present is part of the result.

## Read the stat if the stat is what you need

The summary screen shows the computed figure. It does not show the Individual Value, and it does
not need to: if what you want to know is how hard this **Blissey** hits, the screen has already
added the base, the Individual Value, the Effort Values and the Nature together and told you.
Going behind that to the genotype adds nothing, which is the first and commonest reason a result
changes no decision — `m041`'s rule, that you measure the thing when you can and infer it when you
cannot.

**Hidden Power** is the exception that proves it. Its computed type appears on no screen at all.
For that one property the hidden value is the *only* instrument, and the result is worth having
before you commit — which is exactly the shape of the drug–gene pairs where pre-treatment testing
is genuinely standard.

## One word, read by many routines, never rewritten

`personality` is drawn once, in `CreateBoxMon`, from `Random32()`. Thereafter it decides the
Nature, the ability slot, an **Unown**'s letter via `GET_UNOWN_LETTER`, a **Spinda**'s spot
pattern — `m016`'s device — and, together with the trainer id, whether the thing is shiny, through
`HIHALF(otId) ^ LOHALF(otId) ^ HIHALF(personality) ^ LOHALF(personality)`.

One permanent value, many downstream readouts, no routine to change it. That permanence is why
storing the result is worth doing, and it is equally why a wrong reading of it never expires.

## Where the metaphor stops

Everything above is mechanism. Three things about genetic information in people are not mechanism
and are said here without analogy.

A pharmacogenomic result is **information about relatives as well as about the person tested**,
even when it was ordered for one narrow prescribing question. Pharmacogenes are generally not
disease genes, which is why this is usually a small issue rather than a large one — but it is not
nothing, and consent, storage and disclosure are governed by law and policy that differ between
countries.

It is **permanent and it travels**. A result entered in a record will be read years later by
people who did not order it and may not have the context that explains what it does and does not
mean. A mislabelled phenotype is a durable error, and the right response to a surprising result is
the same as for any test: ask whether it fits before acting on it.

And the coverage problem has a plain name. The reference data and the allele panels on which
pharmacogenomics was built **over-represent populations of European ancestry.** A technology that
performs better for the people it was developed on, deployed uniformly, widens a gap instead of
closing one. Saying so is not a criticism of the science; it is a description of what has to be
fixed for the science to deliver what it promises, and the fix is population-appropriate panels
and reference data rather than more enthusiasm.

One last thing, because it is how this topic goes wrong in front of a person. A genotype is never
a reason to disbelieve what someone reports. If a person says a medicine did not work or was not
tolerated, "the genotype was normal" is not an argument against them — at most it is a reason to
look for the other explanation. Nothing in this pair indicates what anyone should take, change or
stop, and a pharmacogenomic result in somebody's own record is a conversation for their prescriber
or pharmacist, not something to act on from a revision answer.

## What a Gym Leader is listening for

* Where in `CALC_STAT` is the species figure, where is the individual one, and why does the
  bracketing matter?
* **Snorlax**, **Flygon** and **Shuckle**. Same one-bit test, three different amounts of
  information. Say which and why.
* **Hidden Power** computes to Ground. Give the multiplier into **Magnemite** and into **Flygon**,
  and say which part of the genotype decided it. (Neither.)
* Which output does no Nature in the game touch, and what is that the analogue of?
* **Skill Swap** resolves. What does a read of `MON_DATA_ABILITY_NUM` now return, and is it right?
* Why does reading an Individual Value add nothing about **Blissey**'s hitting power, and
  everything about its **Hidden Power**?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **The published drug–gene guidelines of the clinical pharmacogenetics implementation
  consortium**, and **the pharmacogenetics recommendations of the Dutch pharmacogenetics working
  group.** These are the two bodies whose documents are most used to decide whether a drug–gene
  pair is actionable and what the action is. They are separately maintained, they do not always
  agree, and neither replaces the product licence where they differ.
* **Your national formulary and the product's approved prescribing information**, for whether a
  genotype or phenotype is mentioned for that drug at all, and whether testing is required rather
  than merely informative. This differs by country.
* **Your national genomic medicine service's test directory**, for what is orderable where you
  work, on what indication, and with what turnaround.
* **A current clinical pharmacology or pharmacogenomics textbook chapter**, for the phenotype
  terminology, the prodrug reversal, phenoconversion, and the distinction between variability in
  exposure and variability in response.
* **The primary literature**, for how much of the variance in clearance a given gene explains, for
  allele frequencies by ancestry, and for the predictive performance of any specific test. Neither
  half of this pair states such a figure.

The Pokémon figures are a different matter and were read directly from the public decompilation of
the Game Boy Advance games rather than recalled: the `CALC_STAT` macro and the separate maximum-HP
expression in `CalculateMonStats`; `MAX_IV_MASK` of 31 and the two `Random()` draws packed into
six five-bit Individual Values in `CreateBoxMon`; `personality = Random32()`, written once;
`abilityNum = personality & 1` being set only when `gSpeciesInfo[species].abilities[1]` is
non-zero, and `GetAbilityBySpecies` selecting on it; the ability pairs quoted for Snorlax,
Chansey, Blissey, Onix, Magnemite, Farfetch'd, Granbull, Vibrava, Flygon, Shuckle, Gastly, Ditto,
Smeargle, Pikachu and Groudon, with Granbull, Vibrava and Flygon the only three entries in that
file whose two slots hold the same ability; `Cmd_hiddenpowercalc` taking bit 1 of the six
Individual Values for `(40 * powerBits) / 63 + 30` and bit 0 of the same six for the type,
stepping past Normal and `TYPE_MYSTERY`; `GetNature` as `personality % NUM_NATURES` with
`NUM_NATURES` 25, `gNatureStatTable`'s rows for Adamant, Impish, Lonely, Naughty and Sassy,
`ModifyStatByNature`'s `× 110 / 100` and `× 90 / 100`, and its opening guard that returns the
figure unmodified for HP; Flygon's and Magnemite's typings; Role Play and Skill Swap's data and
effects; `GET_UNOWN_LETTER` and `GET_SHINY_VALUE` both reading `personality`. The arithmetic in
the blocks above is recomputed from those figures.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** Neither half
names a drug–gene pair as actionable, and neither gives allele frequencies, variance-explained
figures or doses, deliberately: those belong to the drug–gene guidance, the product licence and
the primary literature, and they are revised. Nothing here indicates whether anyone should be
tested, or what should be done with a result. A result in a person's own record is a matter for
their prescriber or pharmacist, and a normal result is not a reason to disbelieve a reported
effect. Nothing here should be used to make a decision about anyone's treatment, including the
reader's own.

## Where this stands, October 2026

The mechanism is mechanism and does not date, and the game mechanics quoted are fixed in released
software — though the series has changed several of them between generations, and every figure
here is pinned to the Game Boy Advance games, where Individual Values run 0 to 31 and the ability
slot is one bit. The clinical half dates faster than most of this specialty. **Which drug–gene
pairs are actionable** is revised on a rolling basis and pairs have been both added and
downgraded. **What is orderable** depends on a national test directory that changes. **Whether
testing is pre-emptive or reactive** is an open service-design question that different countries
are currently answering differently. And the **coverage and reference-data problem** is the
subject of substantial active work, so any statement about how panels perform across ancestries
dates quickly. Check the current guidance, your national test directory and the product licence.
