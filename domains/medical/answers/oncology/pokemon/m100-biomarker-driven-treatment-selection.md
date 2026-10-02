---
id: "m100"
slug: biomarker-driven-treatment-selection
style: pokemon
category: oncology
difficulty: advanced
question: "Why are a biomarker test and the drug it selects for treated as one object rather than two, and what goes wrong when they are separated?"
tags: [biomarkers, companion-diagnostics, assay-validation, pre-analytics, cut-offs]
---

# Thick Club doubles Attack, and the species check is in the same line as the doubling

`CalculateBaseDamage` in Emerald has a run of six consecutive lines that are companion diagnostics
written as code. Each one is a held item and an identity test, in one condition, with no
separation between them:

```
   if (attackerHoldEffect == HOLD_EFFECT_DEEP_SEA_TOOTH && attacker->species == SPECIES_CLAMPERL)
       spAttack *= 2;
   if (defenderHoldEffect == HOLD_EFFECT_METAL_POWDER && defender->species == SPECIES_DITTO)
       defense *= 2;
   if (attackerHoldEffect == HOLD_EFFECT_THICK_CLUB
       && (attacker->species == SPECIES_CUBONE || attacker->species == SPECIES_MAROWAK))
       attack *= 2;
```

**Thick Club** on **Cubone** or **Marowak** doubles Attack. **Light Ball** on **Pikachu** doubles
Special Attack. **Metal Powder** on **Ditto** doubles Defence. **Deep Sea Tooth** and **Deep Sea
Scale** on **Clamperl** double Special Attack and Special Defence. **Soul Dew** on **Latias** or
**Latios** multiplies both special stats by one and a half.

Hold any of them on anything else and the effect is not smaller. It is **absent**. The item is
real, it occupies the one held-item slot, the game shows it in the summary, and the condition is
never true, so the line is never executed. The item's entire value is contingent on a test the
code performs at the moment of use — and the test and the effect are not two objects. They are one
`if`.

As elsewhere in this specialty: **the objects of study are hold-effect gates, identity tests,
threshold parameters and lookup tables.** No Pokémon in this answer stands in for a person, and
the analogy is dropped entirely at the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
(**consensus**, **country-dependent**).

## Companion and complementary, drawn as two different tables

```
   COMPANION — the species gate                COMPLEMENTARY — sHoldEffectToType

   one condition, one effect,                  a SEVENTEEN-ROW table pairing a
   all or nothing:                             hold effect with a type:

     Thick Club  + Cubone/Marowak                {HOLD_EFFECT_FIRE_POWER, TYPE_FIRE}
     Light Ball  + Pikachu                       {HOLD_EFFECT_WATER_POWER, TYPE_WATER}
     Metal Powder+ Ditto                         ... fifteen more ...
     DeepSeaTooth+ Clamperl
     DeepSeaScale+ Clamperl                     Charcoal's holdEffectParam is 10,
     Soul Dew    + Latias/Latios                so for a Fire-typed move the
                                                ATTACKING STAT gets a TENTH more,
   wrong holder ──► the line never              and for anything else nothing.
   runs.  Not reduced.  ABSENT.
                                                a WEIGHT, not a GATE.

   ───────────────────────────────────────────────────────────────────────────────

   AND THE SAME NUMBER, TWO ANSWERS, BECAUSE THE THRESHOLD IS NOT THE NUMBER'S

      GetGenderFromSpeciesAndPersonality:
          if (gSpeciesInfo[species].genderRatio > (personality & 0xFF))  female
          else                                                          male

      personality & 0xFF = sixty-four, say.

         Treecko   genderRatio = PERCENT_FEMALE(12.5) = 31   ──►  31 > 64  false  ──► MALE
         Kecleon   genderRatio = PERCENT_FEMALE(50)   = 127  ──► 127 > 64  true   ──► FEMALE

      ONE assay value.  TWO scoring thresholds.  TWO answers.  A score
      without its scoring system and its disease is not a result.

      And for Chansey (MON_FEMALE) and Beldum (MON_GENDERLESS) the switch
      returns before the comparison — a question that is definitional in
      that disease and so is never tested.
```

## Why the pairing is one object

A drug licensed for a biomarker-defined population was tested in people chosen by a **specific
test**: a particular antibody or probe or panel, on a particular platform, applied to a specified
specimen prepared a specified way, read by a specified algorithm at a specified cut-off. The trial
result is a statement about **that selection** (**mechanism**). Change the test and you select a
different population, even while believing you measure the same molecule.

So where an authorisation is restricted to a biomarker-defined population, the test that defines
it is typically authorised alongside the drug and the label refers to the test or the kind of test
required (**definitional**, strongly (**country-dependent**), because the machinery, the
terminology and even the categories differ between jurisdictions).

The six lines above are what that looks like when nobody can separate the two: the holder is
checked by name, in the same condition, by the same function, at the moment the effect would
apply. And the games even reproduce the jurisdictional part. The Soul Dew condition carries
`!(gBattleTypeFlags & (BATTLE_TYPE_FRONTIER))` — **the same item on the same species does nothing
inside the Battle Frontier**. One venue, one written rule, one pairing switched off, which is what
"approved here and not there" looks like from the inside.

The distinction to learn is **companion** against **complementary** (**definitional**). A
companion diagnostic is required to select: the result is a gate, and a negative means the drug is
not used — the species check. A complementary diagnostic informs without gating: the result is a
weight — the `sHoldEffectToType` table, seventeen rows pairing a hold effect with a type, where
**Charcoal**'s `holdEffectParam` of ten adds a tenth to a Fire-typed move and nothing at all to
anything else. Treating a complementary result as a gate, or a companion result as advisory, is a
category error with a direct clinical consequence (**consensus**), and which assays sit in which
category is jurisdiction-specific and changes.

## One specimen, two assays, two outcomes

**Clamperl**'s entry in the evolution table is the cleanest thing in this answer:

```
   [SPECIES_CLAMPERL] = {{EVO_TRADE_ITEM, ITEM_DEEP_SEA_TOOTH, SPECIES_HUNTAIL},
                         {EVO_TRADE_ITEM, ITEM_DEEP_SEA_SCALE, SPECIES_GOREBYSS}},
```

The same species, two different items, two entirely different outcomes — **Huntail** or
**Gorebyss** — and the method is `EVO_TRADE_ITEM`, so the item is necessary and not sufficient: a
trade has to happen as well. Two conditions, both required, before the outcome is determined. And
the two items are the *same* two that gate the damage doubling, so each one is simultaneously the
selector and the thing selected for.

If you want the clinical sentence: which assay was run on this specimen determines which decision
is available, and the specimen does not tell you which assay to run. The outcome is a property of
the pairing rather than of the tissue.

## The cut-off is a parameter in a table

Much of what is measured is **continuous** — an amount of protein, a proportion of cells, a copy
number, a fraction of reads — and what is reported is a category.

`GetEvolutionTargetSpecies` holds the clean case. **Feebas** evolves into **Milotic** by
`EVO_BEAUTY`, and the condition is `gEvolutionTable[species][i].param <= beauty` with the
parameter set to one hundred and seventy. A stored byte on one side, a number somebody chose on
the other, and a single comparison. Nothing in a Feebas is different in kind at one hundred and
sixty-nine.

Clinically the cut-off is a convention, chosen to be reproducible between observers and to
correspond to a decision, and it is **disease-specific and assay-specific**: the same molecule is
scored by different algorithms, over different cell populations, at different cut-offs, in
different diseases (**definitional**, **consensus**). A score reported without its scoring system
and the disease it was validated in is not usable. This specialty's answer on surgical margins
makes the banding argument in full, with Flail's six thresholds, and it is not re-derived here.
The point specific to biomarkers is that the cut-off was often chosen **because a trial used it**,
making it a property of the evidence rather than of the biology — so *which cut-off* and *which
trial* are the same question.

## What the gate cannot see: pre-analytics

Here the game has nothing, and saying so is more useful than inventing something. A held item in
Emerald either is in the slot or is not; there is no state in which the item is present but
degraded, and the one held-item slot — which the nursing answer on indwelling devices already uses
— has no concept of how the item was stored.

The commonest way a biomarker result is wrong has nothing to do with the assay itself
(**mechanism**, **consensus**): time from removal of the tissue to fixation, the fixative, how
long fixation lasted, whether the specimen was decalcified, how old the block is, and how the
sections were cut all affect what can be detected. An assay validated on one preparation process
is not validated on another, which is why acceptable pre-analytic conditions are specified in the
assay's instructions and are part of what a laboratory is accredited for — and why cytology
specimens, needle washings and small-volume samples are a **separate validation question** rather
than a smaller version of the same one.

"The test was negative" and "the test was performed on a specimen the test is validated for" are
two claims, and only the second makes the first interpretable.

## Analytic equivalence is demonstrated, not assumed

`Cmd_critcalc` gives the second family of identity gates, and they are gates for a different stat
in a different function: a **Lucky Punch** adds two to the critical-hit index *only if the holder
is* **Chansey**, and a Stick adds two *only if the holder is* **Farfetch'd**. Same shape,
different file, written out again — because nobody assumed the first set of checks covered them.

That is the habit the subject requires (**consensus**). Different antibody clones against the same
protein, different probe sets against the same rearrangement and different sequencing panels
covering the same gene do **not** give interchangeable results. Concordance is an empirical
question answered by comparison studies, and the answer is often "good but not equivalent", which
is exactly the range in which a value near the decision boundary matters most. Three consequences
(**consensus**, (**country-dependent**) in enforcement): a laboratory-developed test used in place
of an authorised one needs local validation against a defined comparator; external quality
assurance schemes exist because laboratories drift, and participation is a condition of
accreditation in many systems; and reporting the method is not bureaucratic detail, because a
result without its clone, platform and scoring convention cannot be matched to the evidence it is
meant to be matched against.

## What goes wrong when the two come apart

The failures are symmetrical and both are clinical (**mechanism**).

A **false negative** withholds an effective treatment from someone who would have benefited, and
it is invisible — nobody ever learns what would have happened. A **false positive** commits
someone to real toxicity with no mechanism of benefit, and the right way to say that is this
repository's **Type Effectiveness** zero rather than a reduced effect: Ground into **Flygon** is
nothing, because **Levitate** is its only ability in Emerald's species data. Without the target
there is no route for the drug to act through, so the toxicity is the whole of what is received.

Two more failures are about the evidence rather than the person. A trial using a poorly
discriminating assay **dilutes its own effect**, because the treatment arm contains people who
could not have benefited — so an apparently negative trial of a targeted agent is sometimes a
statement about the assay (**consensus**). And a drug shown to work in a selected population, used
in an unselected one, inherits none of the evidence: the item is in the slot and the condition is
false.

## Where the organ-first logic inverts, and what a panel returns

Some indications are defined by the molecular alteration **irrespective of the tissue of origin**
(**consensus**, (**country-dependent**) in which are approved and funded). Three things change:
who orders the test and when, because the alteration appears in diseases nobody routinely looked
in; what the limiting factor is, which becomes the assay's validation **across** diseases rather
than within one, since prevalence, specimen types and the relevant cut-off all vary by site; and
where the result is handled, because a finding in a disease with no local pathway needs a forum —
the molecular tumour board or the multidisciplinary meeting, which the previous answers here
describe.

And a multiplex panel returns more than the question asked. Some findings have a matched option,
some only in a trial, some only in another disease, and some none at all; frequently the panel
returns nothing actionable, which is a result and not a failure (**consensus**). Tiered reporting
exists to keep those separable, with the tiers themselves a local convention
(**country-dependent**). The point that matters here: a panel result is **not** a companion
diagnostic result unless that panel is the one validated for that indication, and detecting an
alteration does not import the evidence attached to a different assay for it. Thick Club in the
slot is not Thick Club in the condition.

## Where the metaphor stops

Everything above is hold-effect gates, identity tests and threshold parameters, and code is a good
place to see them because the test and the effect sit in the same line. What follows is about
people, so it is said plainly and without the analogy.

A laboratory property decides, for a particular person, whether a treatment is offered. That is an
uncomfortable fact and it is the plain truth of this subject. Being told "you are not eligible"
and being told "the test on your sample did not show the thing this drug needs" are the same event
described at two levels, and the second is both more honest and harder to say. Where a result is
borderline, or the specimen was marginal, or a different assay might answer differently, that is
information the person has an interest in — not because it changes today's decision, but because
it is the reason the decision is what it is.

The waiting deserves naming too. Molecular results take time, the time is rarely explained, and it
falls in the period immediately after a diagnosis when nothing else appears to be happening and
the delay is experienced as inaction. Saying what is being tested, why it takes as long as it
does, and what each possible answer would mean costs very little and changes that period
considerably.

## What a Gym Leader is listening for

* Thick Club's species check and its doubling are in one condition. What is the clinical claim,
  and why is "one condition" the whole of it?
* Hold Light Ball on something other than Pikachu. Is the effect reduced or absent, and which word
  is the clinically correct one?
* Soul Dew is switched off inside the Battle Frontier. What does that model?
* Clamperl has two evolution rows and the method needs a trade as well as the item. Name both
  things that illustrates.
* Feebas evolves at a stored byte against a parameter of one hundred and seventy. What is the
  parameter a property of — the Feebas, or the evidence?
* Lucky Punch's species check is written out again in a different function. What habit is that,
  and what does assuming the opposite cost?
* Which part of this subject has no mechanic in the game at all, and why is that the part that
  goes wrong most often?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* The summary of product characteristics or equivalent label for the agent, published by the
  licensing authority in your country — for the biomarker-defined population and for what is said
  about the test required to identify it. The single most useful document here.
* The assay's own instructions for use, published by its manufacturer, for the validated specimen
  types, acceptable pre-analytic conditions, scoring algorithm and cut-off. A result interpreted
  without this document is being interpreted against an assumption.
* Your national or regional guidance for biomarker testing in the disease, for which tests are
  recommended, at which point in the pathway, and which assays are accepted. These differ sharply
  between countries and are revised frequently.
* Your own laboratory's accreditation scope and its external quality assurance participation,
  which together are the evidence that the test in front of you performs as the comparison studies
  say.
* The published guidance on variant and biomarker reporting tiers from the professional body
  issuing it in your region, for how a finding's clinical significance is classified.
* The primary literature, for concordance studies between named assays and for the trials that
  established each cut-off.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about why a test and a drug are one object, dressed in a game so that
the identity check and the effect stay visibly inseparable. It has had no clinical review. **No
assay, antibody clone, platform, gene, drug, cut-off or concordance figure appears here, and none
should be inferred** — those are assay-specific and disease-specific, they differ between
countries and laboratories, and they are revised frequently; the label, the assay's instructions
for use and the local guidance in force where you work are the authority, and this is not. It is
not a testing protocol, not a reporting guide and not a decision aid, and it describes no
individual's specimen or situation. Anyone affected by cancer — their own diagnosis or someone
else's — should be talking to the clinical team looking after that person, who have the specimen,
the report and the history, none of which are here. The analogy carries identity gates, thresholds
and lookup tables only: no part of it stands in for a person, and the pre-analytic part of the
subject is marked above as having no counterpart rather than being given one.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source. `CalculateBaseDamage` in `src/pokemon.c`
contains the species-gated hold effects in consecutive lines: `HOLD_EFFECT_SOUL_DEW` with Latias
or Latios and `!(gBattleTypeFlags & (BATTLE_TYPE_FRONTIER))`, giving one and a half times Special
Attack for the attacker and Special Defence for the defender; `HOLD_EFFECT_DEEP_SEA_TOOTH` and
`HOLD_EFFECT_DEEP_SEA_SCALE` with Clamperl, doubling Special Attack and Special Defence;
`HOLD_EFFECT_LIGHT_BALL` with Pikachu, doubling Special Attack; `HOLD_EFFECT_METAL_POWDER` with
Ditto, doubling Defence; and `HOLD_EFFECT_THICK_CLUB` with Cubone or Marowak, doubling Attack. The
same function iterates `sHoldEffectToType`, a seventeen-row table of hold-effect and type pairs,
applying `(stat * (holdEffectParam + 100)) / 100` only when the move's type matches the row;
`src/data/items.h` gives Charcoal `HOLD_EFFECT_FIRE_POWER` with `holdEffectParam` ten.
`Cmd_critcalc` in `src/battle_script_commands.c` adds two to its index for
`HOLD_EFFECT_LUCKY_PUNCH` with an explicit comparison against `SPECIES_CHANSEY` and two for
`HOLD_EFFECT_STICK` against `SPECIES_FARFETCHD`. `GetGenderFromSpeciesAndPersonality` in
`src/pokemon.c` returns the stored `genderRatio` directly for `MON_MALE`, `MON_FEMALE` and
`MON_GENDERLESS` — zero, two hundred and fifty-four and two hundred and fifty-five in
`include/constants/pokemon.h` — and otherwise returns female when
`gSpeciesInfo[species].genderRatio > (personality & 0xFF)`; `PERCENT_FEMALE` is defined in
`src/data/pokemon/species_info.h` as `min(254, ((percent * 255) / 100))`, so
`PERCENT_FEMALE(12.5)` is thirty-one and `PERCENT_FEMALE(50)` is one hundred and twenty-seven;
Treecko carries the first, Kecleon and Clamperl the second, Chansey `MON_FEMALE` and Beldum
`MON_GENDERLESS`. `src/data/pokemon/evolution.h` gives Clamperl two rows, both `EVO_TRADE_ITEM`,
to Huntail with Deep Sea Tooth and Gorebyss with Deep Sea Scale, and Feebas one row, `EVO_BEAUTY`
with parameter one hundred and seventy, to Milotic; `GetEvolutionTargetSpecies` tests `EVO_BEAUTY`
as `param <= beauty` against `MON_DATA_BEAUTY`. Flygon's species entry is Ground and Dragon with
`{ABILITY_LEVITATE, ABILITY_LEVITATE}`. Several of these items behave differently in later
generations and nothing here is claimed about any generation but the third.

The clinical argument is structural and will not date: evidence obtained in a population defined
by a test is evidence about that selection, pre-analytics and analytic method and scoring
convention are all part of the test, and a laboratory property therefore determines a clinical
outcome. Everything concrete moves quickly — which drugs are restricted to biomarker-defined
populations, which assays are authorised alongside them, each regulator's terminology and
categories, the cut-offs, which indications are tumour-agnostic, and whether a multiplex panel is
accepted in place of a single-analyte companion test are all changing and unevenly adopted between
countries, and tiered reporting conventions are being revised. No assay, clone, cut-off or
clinical figure is quoted here, deliberately.
