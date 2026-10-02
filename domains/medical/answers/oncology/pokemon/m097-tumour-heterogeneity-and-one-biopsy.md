---
id: "m097"
slug: tumour-heterogeneity-and-one-biopsy
style: pokemon
category: oncology
difficulty: advanced
question: "In what sense is a single tumour biopsy a sample of a population under selection, and what follows for how a biomarker result is interpreted?"
tags: [heterogeneity, clonal-evolution, biopsy, sampling, liquid-biopsy]
---

# One number nobody shows you decides five things, and Repel deletes the draw after it is made

Two tables decide what a wild Pokémon is, and they are not the same kind of table.

`gSpeciesInfo[species]` holds what every member of the species has because it is that species:
base stats, both type slots, the ability list, the gender ratio. **Wurmple**'s entry says Bug and
Bug, `{ABILITY_SHIELD_DUST, ABILITY_NONE}`, and a gender ratio of `PERCENT_FEMALE(50)`. Every
Wurmple in the cartridge shares every word of that.

The **Personality Value** is the other table, and it is one thirty-two-bit integer per individual,
fixed the instant the thing is created. From it the game derives the nature, as `personality %
NUM_NATURES`; the ability slot, as `personality & 1`; the gender, by comparing `personality &
0xFF` against the species' gender ratio; **Spinda**'s spot pattern, which the dermatology answer
in this repository already uses; and — the one that matters here — whether a **Wurmple** will
become **Silcoon** or **Cascoon**, which `GetEvolutionTargetSpecies` decides as `(personality >>
16) % 10` against four.

Nothing on the sprite shows any of it. The Wurmple that becomes **Beautifly** and the Wurmple that
becomes **Dustox** are the same species, the same two type slots, the same ability, the same
sprite, and one decimal digit apart in a number the game never prints.

That is the shape of this answer. A species table that every member shares, a per-individual table
nobody displays, and then — separately — a set of filters that change which individuals you ever
meet without changing one field of any of them.

As elsewhere in this specialty: **the objects of study are generators, derived fields, filters and
flag arrays.** No Pokémon in this answer stands in for a person with cancer, for a tumour or for a
cell, and the analogy is dropped entirely at the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
(**consensus**, **country-dependent**).

## The three axes, drawn as what they are

```
   ANCESTRY  ──  gSpeciesInfo[species]        vs      the Personality Value

      shared by EVERY individual                      one u32 per individual
      ─────────────────────────────                   ─────────────────────────
      types[0], types[1]                              nature   = pv % 25
      base stats                                      ability  = pv & 1
      ability LIST                                    gender   = pv & 0xFF vs
      gender RATIO                                               genderRatio
                                                      Wurmple  = (pv>>16) % 10
      an agent aimed HERE                             Spinda's spots
      reaches all of them                             ─────────────────────────
                                                      an agent aimed HERE
                                                      reaches a SUBSET

   ──────────────────────────────────────────────────────────────────────────────

   HIDDEN SPREAD  ──  the six Individual Values

      value = Random();   iv = value & MAX_IV_MASK           ◄── MAX_IV_MASK is 31
                          iv = (value & (MAX_IV_MASK<<5))>>5
                          iv = (value & (MAX_IV_MASK<<10))>>10
      value = Random();   ... the same three again

      TWO draws.  SIX five-bit fields.  Thirty bits of variation, and the
      top bit of each sixteen-bit draw is never used at all.

   ──────────────────────────────────────────────────────────────────────────────

   THE FILTER  ──  and WHERE it sits in TryGenerateWildMon

      ChooseWildMonIndex_Land()   ──►  the slot is drawn
      ChooseWildMonLevel()        ──►  the level is drawn
      ────────────────────────────────────────────────────────  the individual
      if (flags & WILD_CHECK_REPEL && !IsWildLevelAllowedByRepel(level))        │
          return FALSE;                                          exists by here │
      if (flags & WILD_CHECK_KEEN_EYE && !IsAbilityAllowingEncounter(level))    │
          return FALSE;                                                        ▼
      ────────────────────────────────────────────────────────  and is DISCARDED
      CreateWildMon(...)          ──►  only now does it exist to you

      The filter does not redraw.  It DELETES.  Nothing about any individual
      changed; the composition of what you ever see did.
```

## Ancestry: the species table against the one per individual

A cancer is a **population** of related cells that diverged from a common ancestor, are still
diverging, and are under selection by oxygen, by space, by nutrient supply, by the immune system
and, once treatment starts, by the treatment (**mechanism**).

The two-table split is the clinically load-bearing part. An alteration present in the common
ancestor is in every cell of the disease; one that arose in a branch is in a subset
(**definitional**). An agent directed at the first treats the disease; an agent directed at the
second treats part of it, however well the test performed. That is `gSpeciesInfo` against the
Personality Value, and the game draws the line exactly where the clinic does.

The game even reproduces the awkward corner. `CreateBoxMon` writes the ability slot **only if
`gSpeciesInfo[species].abilities[1]` is non-zero** — so for Wurmple, whose second ability is
`ABILITY_NONE`, the field is never set at all. A determinant that exists for some members of the
category and is simply absent for others, so the assay for it returns nothing rather than
returning negative, is a familiar problem in a molecular report.

And **convergent evolution** — two regions arriving at the same pathway by different alterations,
so two samples look unalike and behave alike (**consensus**) — is in the species table twice over.
**Gengar** is Ghost and Poison with `{ABILITY_LEVITATE, ABILITY_NONE}`. **Skarmory** is Steel and
Flying with `{ABILITY_KEEN_EYE, ABILITY_STURDY}`. Both are immune to Ground. Neither is immune for
the reason the other is: one by an ability, one by a type slot. Sequence them and they disagree;
point Earthquake at them and they are identical.

## The hidden spread, and why a negative result is not an absence

The six **Individual Values** come from two `Random()` calls, three five-bit fields carved out of
each by `MAX_IV_MASK`, which `include/constants/pokemon.h` gives as thirty-one. Thirty bits of
per-individual variation, none of it on the sprite, and a reader of the sprite has no way to know
it is there.

Which gives the asymmetry the whole clinical argument turns on (**mechanism**):

* **Finding** an alteration establishes that it was present in the material examined, at a level
  the assay could see.
* **Not finding** one is compatible with absence, with presence below the limit of detection, with
  presence in a region the needle missed, and with a specimen that was not adequate for the test.

So a negative result is only interpretable alongside what was tested, how much of it there was,
and what the assay can see — which is why specimen adequacy belongs in a molecular report rather
than before it (**consensus**, reporting requirements **country-dependent**). The
limit-of-detection half of that argument is this specialty's answer on tumour markers, where three
separate routines in one game refuse to report zero; the surface-sampling half is the answer on
margins. Neither is re-derived here.

Repeat sampling improves the evidence and costs something, which is why multi-region sampling is a
research instrument and not routine, and why the question asked of any repeat biopsy is whether
the result would change management (**consensus**).

## The filter: Repel, Keen Eye, and the fact that it deletes

Now the part that is exactly right and is usually described wrongly.

In `TryGenerateWildMon`, the slot is drawn and the level is drawn **first**. Only then:

```
   if (flags & WILD_CHECK_REPEL && !IsWildLevelAllowedByRepel(level))      return FALSE;
   if (flags & WILD_CHECK_KEEN_EYE && !IsAbilityAllowingEncounter(level))  return FALSE;
```

`IsWildLevelAllowedByRepel` returns TRUE immediately if `VAR_REPEL_STEP_COUNT` is zero, then walks
the party, stops at the **first alive non-egg** member, and refuses the encounter if the wild
level is below that member's level. `IsAbilityAllowingEncounter` reads `gPlayerParty[0]` instead —
slot zero, whatever state it is in — and if that lead's ability is **Keen Eye** or **Intimidate**,
its level is above five, and the wild level is at least five below it, refuses the encounter on
`!(Random() % 2)`.

Four things in that worth having straight.

* **The filter deletes rather than redraws.** The individual was generated and then thrown away.
  Nothing about it changed. What changed is the composition of everything you will ever meet.
* **It is partial.** Keen Eye's half-chance means some of what the filter is against gets through,
  which is why a filtered population is *enriched* rather than purified.
* **Two filters in one function read the party differently** — one takes the first healthy member,
  the other takes slot zero regardless. Two instruments aimed at the same question, sampling
  differently, is this answer's last section.
* **Skarmory is one of the leads that does this**, because Keen Eye is the first entry in its own
  ability list. The thing doing the filtering is in the species table.

Clinically: treatment is that filter, and the ordinary account of progression needs **selection
only**. A resistant subpopulation present at low frequency beforehand, an agent that removes the
sensitive majority, and the expansion of what was left gives exactly the clinical picture — a deep
response, then progression — with no new mutation required (**mechanism**). Treatment-induced
mutagenesis is a separate claim with much weaker support, and asserting it where selection
suffices is a genuine error of reasoning.

Three consequences (**consensus**): progression is informative about composition, so the escape
mechanism is worth establishing rather than assuming — the previous answer in this specialty;
simultaneous combination beats sequential where the evidence supports it, because a sequence hands
the survivors an uncontested interval; and a pre-treatment molecular profile can expire, because
it describes a population that has since been filtered.

## Two instruments, and the one that pools

Tissue and plasma are not ranked, and treating one as a cheaper version of the other is the usual
mistake (**mechanism**, **consensus**).

A **tissue biopsy** is spatially specific: a named lesion, morphology and immunohistochemistry as
well as sequencing, so a change of histology can be established. Its weakness is that it is one
place.

**Circulating tumour DNA** inverts both, and the **Pokédex** is the shape of it.
`GetSetPokedexFlag` reads one bit per species out of `gSaveBlock2Ptr->pokedex.seen`, indexed by
national number minus one — and the nursing answer on suspicion against confirmation already uses
the fact that `seen` and `owned` are two separate arrays. What this answer wants is what a `seen`
bit *is*: a pooled, location-free, count-free assertion that the species was encountered
**somewhere**. No route. No map. No tally. Exactly what a plasma result is: an alteration is
present in the body, and the assay cannot say in which lesion.

Its other two weaknesses are in the same routine's neighbourhood. A species present on the map and
never met leaves no bit at all, which is a low-shedding or low-volume disease giving a negative
result while disease is present. And `GetSetPokedexFlag` cross-checks the `seen` bit against two
further copies, `gSaveBlock1Ptr->seen1` and `seen2`, and **clears all three** if they disagree —
a record that knows it can be wrong is still a record that has to be interpreted rather than read.

For the last blind spot the game needs a later generation, and this is not from Emerald, which has
no such ability: **Zoroark**'s **Illusion**, as implemented in the expansion, makes it appear as
the *last alive non-egg member of its own party* — `GetIllusionMonPartyId` walks the party
backwards to find it — and the disguise drops when the battler is damaged. The entry in the record
came from the holder's own side, not from the opponent. That is clonal haematopoiesis: plasma
variants that originate in the person's blood cells rather than in the tumour, which is why a
plasma result is interpreted with that possibility in mind rather than at face value
(**consensus**).

The honest summary: a negative plasma result is weak evidence of absence, a positive tissue result
is strong evidence of presence somewhere, and neither instrument makes the other redundant. What
is available, funded and accepted for a given decision differs markedly between countries and
institutions (**country-dependent**).

## Which lesion, and when

`IsWildLevelAllowedByRepel` reads the first healthy party member rather than the one you meant to
lead with, which is the sampling error in miniature: an accessible site answering a question
nobody asked.

**Which lesion** is decided by the question. For a diagnosis, the most accessible adequate lesion.
For a treatment decision at progression, the lesion that is **progressing** is usually the
informative one, because it is the part of the population that escaped (**consensus**). **When**
is governed by the same test as everything else here: a molecular result that cannot change what
is done, in a disease where no matched option is reachable, is a procedure with risk and no
decision attached (**consensus**, strongly (**country-dependent**), because reachability is
local).

## Where the metaphor stops

Everything above is generators, filters and flag arrays, and code is a good place to see them
because the order of operations is written down. What follows is about people, so it is said
plainly and without the analogy.

A biopsy is an invasive procedure with a wait before it, a wait after it, and a result that may
not be conclusive. Being asked for another one, having had bad news, is a reasonable thing to
decline and a reasonable thing to accept, and the test that justifies the request is whether the
answer would change what is offered — not whether the information would be interesting. That
reasoning belongs out loud, in the conversation with the person being asked, because it is what
makes the request legitimate.

It is worth being plain too that "the result might be a sampling artefact" is a hard sentence to
hear. People are told a test was negative and reasonably take that as a fact about themselves
rather than a fact about a fragment of tissue. The uncertainty described above is real, it is not
a hedge, and conveying it without turning a result into a riddle is a skill rather than a
disclaimer. None of this determines what will happen to any individual, and no clinical figure of
any kind appears in either half of this answer for that reason.

## What a Gym Leader is listening for

* `gSpeciesInfo` against the Personality Value. Which clinical distinction is that, and why does
  it decide what an agent can reach?
* Wurmple's ability slot is never written. What problem in a molecular report is that?
* Gengar and Skarmory are both immune to Ground for different reasons. Name the concept and say
  what it does to two samples from one tumour.
* The Repel check runs *after* the level is drawn. What does the position of that line in the
  function prove?
* Keen Eye refuses on a half-chance rather than always. What does the partialness buy the
  argument?
* A `seen` bit carries no route and no count. Which instrument is that, and what are its other two
  weaknesses?
* Illusion shows a member of the holder's own party. Which confounder is that, and which assay
  does it affect?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* The molecular reporting standard your laboratory reports against, published by the body that
  maintains it — for what specimen adequacy means for each assay, what is stated about the limit
  of detection, and how a negative result is to be worded. The single most useful document here.
* Your national or regional guidance on circulating tumour DNA testing in the specific disease,
  for whether it is accepted in place of tissue and for which decisions. This differs sharply
  between countries and is being revised.
* Your own institution's protocol for repeat biopsy at progression, including who authorises it
  and what the specimen requirements are.
* A current standard textbook of the specialty, for clonal evolution, truncal and subclonal
  alterations, and convergent evolution as concepts.
* The primary literature, for multi-region sequencing studies, for primary–metastasis discordance
  in a particular disease, and for clonal haematopoiesis as a source of plasma variants.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about what a tumour sample is a sample of, dressed in a game so that the
difference between a shared field and a per-individual one stays concrete. It has had no clinical
review. **No discordance rate, detection limit, allele fraction or sampling figure appears here,
and none should be inferred** — those are assay-specific and disease-specific, they differ between
laboratories and countries, and they are revised; the reporting standard and local protocol in
force where you work are the authority, and this is not. It is not a reporting guide, not a
testing protocol and not a decision aid, and it describes no individual's specimen or situation.
Anyone affected by cancer — their own diagnosis or someone else's — should be talking to the
clinical team looking after that person, who have the specimen, the report and the history, none
of which are here. The analogy carries generation, derivation and filtering only: no part of it
stands in for a person, a tumour or a cell.

## Where this stands, October 2026

The Pokémon facts are read from the projects' own source, Emerald except where stated. Wurmple's
species entry gives both type slots as Bug, `{ABILITY_SHIELD_DUST, ABILITY_NONE}`, and
`PERCENT_FEMALE(50)`, which the file's own macro defines as `min(254, ((percent * 255) / 100))`.
`GetNature` in `src/pokemon.c` is `GetMonData(mon, MON_DATA_PERSONALITY, 0) % NUM_NATURES`, with
`NUM_NATURES` twenty-five; `GetGenderFromSpeciesAndPersonality` returns female when
`gSpeciesInfo[species].genderRatio > (personality & 0xFF)` and male otherwise, with `MON_MALE`,
`MON_FEMALE` and `MON_GENDERLESS` as zero, two hundred and fifty-four and two hundred and
fifty-five; `CreateBoxMon` sets the ability slot to `personality & 1` **only inside** `if
(gSpeciesInfo[species].abilities[1])`, and derives the six Individual Values from two `Random()`
calls masked with `MAX_IV_MASK`, which `include/constants/pokemon.h` gives as thirty-one, at
shifts of zero, five and ten. `GetEvolutionTargetSpecies` holds `EVO_LEVEL_SILCOON` and
`EVO_LEVEL_CASCOON` as the same level requirement with `(upperPersonality % 10)` at most four
against greater than four, where `upperPersonality` is `personality >> 16`; the evolution table
gives both at level seven, with Silcoon to Beautifly and Cascoon to Dustox at level ten. Spinda's
spots deriving from the personality value is established in this repository's dermatology answer
on morphology and is not re-derived. Gengar's species entry is Ghost and Poison with
`{ABILITY_LEVITATE, ABILITY_NONE}`; Skarmory's is Steel and Flying with `{ABILITY_KEEN_EYE,
ABILITY_STURDY}`. In `src/wild_encounter.c`, `TryGenerateWildMon` calls `ChooseWildMonIndex_Land`
and `ChooseWildMonLevel` before testing `WILD_CHECK_REPEL` and `WILD_CHECK_KEEN_EYE` and only then
calls `CreateWildMon`; `IsWildLevelAllowedByRepel` returns true when `VAR_REPEL_STEP_COUNT` is
zero, otherwise returns at the first party member with non-zero HP that is not an egg and refuses
when the wild level is below that member's level; `IsAbilityAllowingEncounter` reads
`gPlayerParty[0]`, requires Keen Eye or Intimidate, a lead level above five and a wild level at
most the lead's level minus five, and then refuses on `!(Random() % 2)`. `GetSetPokedexFlag` in
`src/pokedex.c` indexes `pokedex.seen` and `pokedex.owned` as bit arrays by national number minus
one, and clears the bit in all three of `pokedex.seen`, `seen1` and `seen2` when they disagree.
Illusion is **not in Emerald**: the behaviour described is `SetIllusionMon` and
`GetIllusionMonPartyId` in `rh-hideout/pokeemerald-expansion`, which walk the party from the last
slot backwards for the last alive non-egg member, and the ability's cancellation on the holder
being damaged.

The clinical reasoning is structural and will not date. A tumour has always been a population, a
biopsy has always been one sample of it, and the asymmetry between finding something and not
finding it follows from sampling rather than from any current technology. What moves is everything
technological and administrative: assay sensitivity, which genes are on a panel, whether plasma
testing is accepted in place of tissue and for which decisions, whether serial or multi-region
sampling has a routine role, and how a negative result must be worded are all changing and
unevenly adopted between countries and between laboratories in one country. No assay, panel, gene
or clinical figure is named here, deliberately.
