---
id: "m120"
slug: the-biopsy-decision
style: pokemon
category: dermatology
difficulty: advanced
question: "Why does the choice of where and how to take a skin biopsy determine what the report can say, and what can a biopsy never settle?"
tags: [biopsy, histopathology, sampling, clinicopathological-correlation, request-form]
---

# One sixteen-bit word, two masks, two answers — and a sentinel that reads as valid under both

A level-up learnset entry is one `u16`. It holds two things at once, and which one you get depends
entirely on the mask you apply:

```
   #define LEVEL_UP_MOVE(lvl, move)  ((lvl << 9) | move)

   #define LEVEL_UP_MOVE_ID   0x01FF      // the low nine bits:  WHICH MOVE
   #define LEVEL_UP_MOVE_LV   0xFE00      // the high seven:     AT WHAT LEVEL
   #define LEVEL_UP_END       0xFFFF      // end of list
   ==================================================================
   entry & LEVEL_UP_MOVE_ID  ->  a move
   entry & LEVEL_UP_MOVE_LV  ->  a level

   SAME WORD. The two reads do not disagree; they answer different
   questions, and neither one is the whole record.

   AND THE SENTINEL IS ALL BITS SET. 0xFFFF masks to the maximum
   value under BOTH masks. A reader that forgets to test for
   LEVEL_UP_END gets a confident, well-formed, entirely wrong
   answer -- not an error, an answer.
   ==================================================================
```

Take a real entry. **Bulbasaur**'s level-up learnset contains `LEVEL_UP_MOVE( 7, MOVE_LEECH_SEED)`
— one word. Mask it with `LEVEL_UP_MOVE_LV` and the answer is 7. Mask it with `LEVEL_UP_MOVE_ID`
and the answer is **Leech Seed**. Ask the **Move Reminder** and it reads that table for entries at
or below the Pokémon's level; ask the **Move Deleter** and the table is not consulted at all,
which is m087's point about what can and cannot be restored. One word, several readers, and each
reader gets exactly what its mask permits.

That is a biopsy. The block is the word. The sectioning plane is the mask. Vertical sections and
transverse sections do not disagree with each other; they answer different questions about the
same specimen, and the plane is chosen in the laboratory on the basis of what the request form
asked for. And the sentinel is the non-diagnostic report, which is well-formed, confidently
worded, and says nothing about the person — while reading exactly like a result.

m089 established the house device for this and it is worth restating: sampling from inside the
blister reads `gBattleMons[i].status2`, gets a genuine zero, and the answer was in
`gSideStatuses[side]` all along — **a confident zero from the wrong structure is worse than no
result**. m089's version is about *site*, it is settled, and it is **not re-derived here**. This
answer is about the other four decisions.

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. (**mechanism**) —
follows from the method and is checkable by reasoning. (**definitional**) — a term's meaning.
(**consensus**) — standard across current textbooks and national guidance. (**country-dependent**)
— differs between countries or institutions, and yours is the authority. The Pokémon claims are
not marked this way; they are listed in the `## Sources` section with the file they were checked
against.

## Five structures, five depths: a query has to reach the store the answer is in

The five structures are not interchangeable and they are not at the same level. `status2` is a
battler volatile wiped on switch. `status1` survives every switch. `gStatuses3` is a third store
with its own bits. The side statuses belong to a side and carry their own timers. The field
weather belongs to nobody at all. A routine that reads only `status2` is not asking the wrong
question — it is asking a question that **cannot reach** the store the answer is in, and it
returns a clean zero either way.

Technique in a skin biopsy is exactly that choice of reach. (**mechanism**)

| Technique | Reaches | Returns a clean zero on |
| --- | --- | --- |
| **Shave / curette** | Epidermis and upper dermis, often tangentially | Depth of invasion; margin status; whole-lesion architecture |
| **Punch** | A cylinder through epidermis and dermis; the depth depends on the instrument and how far it was pressed | The architecture of a large lesion; anything in the fat, unless it was deliberately taken deep |
| **Incisional / wedge** | A transect spanning the lesion **edge** and adjacent normal skin, to a chosen depth | Whole-lesion architecture; the total depth of a tumour |
| **Excisional** | The whole lesion with a margin, full thickness | Nothing structural — which is why it is the technique when architecture or depth is the question |
| **Deep incisional to subcutis** | Subcutaneous fat, and the septa and lobules in it | Nothing in that compartment — but it had to be asked for, because a routine punch does not get there |

The rule behind the table is the one that makes the whole analogy work: **the pathologist cannot
report on tissue that is not in the pot.** Every entry in the third column is a report that comes
back accurate and useless. (**mechanism**)

Two applications where the reach decides everything:

**Panniculitis and large-vessel vasculitis live in the fat.** The classification turns on whether
the inflammation is septal or lobular and on the state of the vessels in the septa, so a specimen
that stops in the dermis cannot classify it. (**definitional**, **consensus**) This is the
commonest depth failure and it is wholly a decision made before the cut: an incisional biopsy
taken deliberately deep, or a generous punch pushed to fat, is what the question requires.

**Where melanoma is a possibility, excision of the whole lesion is the standard where
practicable**, because staging rests on depth of invasion measured through the thickest part and a
partial sample risks missing it. (**consensus**) No measurement, threshold or stage boundary
appears in this answer. Who performs it, with what margin and in what setting, is firmly
(**country-dependent**).

## Sample where the process is running, not where it has finished

Secondary change is a record of time rather than of diagnosis — m016's point, and it decides the
site. The centre of an established plaque or an annular lesion is frequently its oldest part,
where the diagnostic infiltrate has resolved and secondary change has replaced it. A sample from
there is a sample of the past. (**mechanism**)

* **Inflammatory dermatosis**: the **active edge**, not the centre.
* **Ulcerated or necrotic centre**: avoid it, unless the ulcer itself is the question. Necrotic
  tissue reports as necrosis.
* **Suspected vasculitis**: a **fresh** lesion, because the findings evolve over days and the
  characteristic changes sit in a defined early window, which is in the guidance rather than
  reproducible here. (**consensus**)
* **Hair loss**: the **active margin**, sent in a way that permits the sectioning plane the
  question needs.
* **Suspected infection**: the medium matters more than the site. Fresh tissue to microbiology
  *as well as* a fixed sample — m118's argument, and the commonest reversible failure in that
  territory.
* **Suspected immunobullous disease**: perilesional normal-appearing skin for immunofluorescence,
  plus the edge of a fresh blister for histology. m089, and not repeated.

## The medium is a one-way door, and so is treating first

Formalin fixes tissue, which makes most things possible and a few things permanently impossible.
Immunofluorescence needs fresh tissue or a specific transport medium. Culture needs fresh tissue.
Whether a given molecular test works on fixed material is a property of **your laboratory** rather
than of the technique. (**country-dependent**)

The decision about medium is made at the moment of the request and the specimen is in the pot
within seconds of the cut. Nothing recovers from putting the only sample in formalin when culture
was the question. (**mechanism**)

There is a second one-way door with the same shape, and it is the one m086 built its answer
around. **Growl** is a real move — base power 0, accuracy 100, 40 PP — that drops the target's
Attack by one stage, so the damage numbers afterwards are visibly smaller while **Leech Seed**,
living in `gStatuses3` and draining `maxHP / 8` with no Attack term in the expression, is
untouched. A treatment aimed at the readout changes the readout.

Applied to a specimen rather than to a sign: **treatment that suppresses the process changes the
histology.** A topical or systemic corticosteroid can render an inflammatory infiltrate
non-diagnostic, and treating a suspected infection can render it unculturable. Where the histology
is going to matter, the biopsy comes before the treatment that would alter it, and where it did
not, the report has to be read knowing that. (**mechanism**, **consensus**)

## Transverse against vertical is the mask, and it is requested rather than default

Back to the two masks, because this is where they cash out.

**Vertical (conventional) sections** show full thickness at one place — the epidermis, the
dermo-epidermal junction, the depth of an infiltrate, the level of a split. That last is m089's
whole subject, and it is a vertical-section question.

**Transverse (horizontal) sections** cut across the specimen and show **many follicles at one
level at once**, which is what permits counting follicles, the ratio of terminal to miniaturised
hairs, and the ratio of anagen to telogen. That is the plane that answers a hair-loss question,
and it is **not the default**. (**consensus**) Requesting it is the difference between a report
reading "non-scarring alopecia" and one that quantifies the pattern — and m087's argument about
what the hair cycle records only works if somebody asked for the plane that can read it.

Same specimen. Different mask. Neither read is wrong and neither is the whole record.

The equivalent for a neoplasm is **orientation and margin marking**, which is what permits a
statement about *which* margin is involved. That information exists only if someone created it at
the time. (**mechanism**)

## `FlagGet` has two paths to FALSE, and so does "non-specific dermatitis"

This is the most consequential thing in the answer and the game states it in nine lines.

```
   bool8 FlagGet(u16 id)
   {
       u8 *ptr = GetFlagPointer(id);

       if (!ptr)                                  return FALSE;   <-- LOOKUP FAILED
       if (!(((*ptr) >> (id & 7)) & 1))           return FALSE;   <-- BIT IS CLEAR
       return TRUE;
   }
   ==================================================================
   And GetFlagPointer returns NULL for id == 0. So flag zero, and
   any id with no backing storage, reads exactly the same as a flag
   that exists and is genuinely off.

   CONTRAST VarGet, a different storage class in the same file:

       u16 VarGet(u16 id)
       {
           u16 *ptr = GetVarPointer(id);
           if (!ptr) return id;        <-- returns the ID ITSELF.
           return *ptr;                    An impossible value, which
       }                                   is at least a signal.
   ==================================================================
   One storage class fails SILENTLY into "no". The other fails into
   something a caller can notice. Only the second can hold a
   pertinent negative.
   ==================================================================
```

m073 established this for the clinical record. It arrives in the laboratory unchanged.

**"Non-specific dermatitis" and "no diagnostic features seen" are `FlagGet` returning FALSE.**
They are statements about *this sample*. They cannot distinguish *the features are not present in
this person* from *the features are not present in this block* — two completely different clinical
situations, reported in the same words, and routinely read as the first. (**mechanism**)

Three more things a biopsy cannot settle, each with a sibling answer:

* **Sampling error in a heterogeneous lesion.** One sample of a lesion that varies across its
  extent is a sample of one part. m097 makes this the whole argument in neoplasia; in inflammatory
  disease it is why several sites are taken in erythroderma, where the yield is better from
  multiple and repeating later is a recognised strategy rather than a failure (**consensus**) —
  m119's territory.
* **A diagnosis that is clinical by definition.** Hidradenitis suppurativa rests on lesions, sites
  and chronicity, and a biopsy neither confirms nor excludes it (m117). Sarcoidosis requires a
  conjunction including exclusion of other causes, so histology is one of three elements (m118).
* **A question nobody formulated.** A biopsy taken because the diagnosis is uncertain, with no
  prior statement of what each answer would change, usually changes nothing. m086 makes this point
  about the skin scraping and it generalises.

Which is why the request form is part of the instrument. A pathologist is performing
**clinicopathological correlation**, a method rather than a courtesy. (**definitional**) Age,
site, duration, distribution, morphology, current and recent medicines, immune status, relevant
travel and occupational exposure, what has been treated and with what — and above all the
differential being entertained and what each answer would change. (**consensus**) A form reading
"exclude lymphoma" and a form reading "rash?" produce different work on the same block.

## Hitmonlee pays for the miss, and Rock Head does not help

Last device, and it settles the question of whether the five decisions above are refinement or
substance.

Most recoil is billed as a fraction of damage **dealt** — `EFFECT_RECOIL`, the cost of success.
There is a second, much smaller class. `EFFECT_RECOIL_IF_MISS` has exactly **two** members in the
third generation: **Jump Kick**, Fighting, base power 70, accuracy 95, 25 PP, and **Hi Jump
Kick**, Fighting, base power 85, accuracy 90, 20 PP. **Hitmonlee** learns Jump Kick at level 16
and Hi Jump Kick at level 26. The script is blunt about what happens on a miss:

```
   BattleScript_EffectRecoilIfMiss::
       attackcanceler
       accuracycheck BattleScript_MoveMissedDoDamage, ACC_CURR_MOVE
       goto BattleScript_HitFromAtkString
   BattleScript_MoveMissedDoDamage::        <-- the MISS branch, and it
       attackstring                            still does damage. To you.
       ppreduce
```

**Steelix** and **Aggron** are the species that hold **Rock Head** in the third generation, and
both are Steel-types, so both are also exempt from **Sandstorm** by the type clause m119 sets out.
Exemptions in this game come from different places and do not compose into a general immunity —
which is the right expectation to bring to a procedure's harms as well.

And the ability that is supposed to cover recoil does not cover this one. `ABILITY_ROCK_HEAD`
appears in `BattleScript_MoveEffectRecoil` and nowhere near the crash branch — and inside that
script the `jumpifmove MOVE_STRUGGLE, BattleScript_DoRecoil` line sits **before** the ability
check, so Struggle's recoil is unwaivable too. Rock Head waives the cost of success. It does not
waive the cost of failure, and it does not waive the cost of having no option. m104 built an
answer on this and it is reused here rather than re-derived.

A biopsy is a wound, deliberately made, and the cost is paid on the miss branch. (**mechanism**)

* **Scar**, permanent, and at some sites — upper trunk, shoulders, earlobes, jawline — with a
  recognised risk of keloid or hypertrophic scarring that is higher in some skin types and should
  be discussed before rather than after. (**consensus**)
* **Bleeding**, which needs the medicines history.
* **Infection.**
* **Pain**, at the time and afterwards.
* **Delayed or poor healing** — the specific problem on the lower leg, in arterial disease, in
  diabetes, and on irradiated or previously operated skin. The vascular reasoning is m055's and it
  applies before cutting as well as before compressing.

Every one of those is paid for a non-diagnostic biopsy exactly as for a diagnostic one. The harm
attaches to the act, not to the result. Which is the answer to the question this section opened
with: getting the five decisions right is not refinement. It is the difference between paying the
cost for something and paying it for nothing.

## Where the metaphor stops

No Pokémon in this answer stands in for a person, and nothing above maps a specimen or a patient
to a creature. The devices are a bit-mask, a null-pointer return and a script label, all of which
are facts about code. Nothing in the game stands for being cut, waiting, or being told a result.

**Being biopsied is a more significant event than the people arranging it tend to register.** It
involves being cut, usually awake, often in a part of the body someone would rather not expose, by
someone they have just met, for a reason they may understand only partly. The commonest thing said
afterwards is that nobody explained what was being looked for. Where the question includes cancer,
the gap between procedure and result is a period of real fear, and how bad it is depends
substantially on what was said at the time and whether anyone gave a realistic date.

**Three things follow, and all three are within anyone's gift.** Saying what is being looked for
in plain words, including the possibility that is the worrying one. Saying what the result will
and will not settle — specifically that a non-specific answer is possible and what the plan would
then be, because an unexpected "inconclusive" is experienced as a failure unless it was named as a
possibility beforehand. And giving a real timeframe and a route by which the result will actually
reach them: results going astray between services is common and entirely avoidable.

**And the scar deserves its own sentence, because it is the part most often skipped.** It is
permanent, it is in a place a clinician chose, and for a facial or otherwise visible site the
cosmetic consequence may matter far more to the person than to the person holding the blade.
Asking before choosing the site, wherever there is any choice at all, is a small act with a
lasting consequence.

Nothing here is for any reader's own use, no procedure described is an instruction, and nothing in
this answer is guidance on how to perform one. Anyone with a new, changing, bleeding or
non-healing skin lesion needs assessment in person, and a changing pigmented lesion is assessed
urgently.

## What a Gym Leader is listening for

Which technique reaches which compartment, and the clean-zero column. Why a panniculitis cannot be
classified from a shallow specimen. Why a pigmented lesion is excised whole where practicable. Why
the active edge rather than the centre. What has to be decided before the specimen enters the pot.
Why treating first changes the report. Transverse against vertical sectioning, which question each
answers, and which one you have to ask for. What belongs on the request form and why it changes
the work done on the block. The difference between a non-specific report and an exclusion, in
terms of the two paths to FALSE. Which dermatological diagnoses are clinical by definition. And
the harms, which are billed on the miss branch.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For biopsy technique, site selection by indication and specimen handling: a current standard
  textbook of dermatology and of dermatological surgery, and your own service's procedural
  protocol.
* For what your laboratory accepts — medium, minimum sample size, whether molecular testing works
  on fixed material, how to request transverse sectioning, how to request polarised light: the
  user handbook of your histopathology and immunodermatology laboratory. It is the authority on
  handling and it differs between laboratories.
* For suspected melanoma and other skin cancer — which lesions are excised whole, by whom, with
  what margin, in what setting: your national skin cancer guidance and your local pathway.
* For the timing window in suspected cutaneous vasculitis and the immunofluorescence requirements:
  the specialist guidance of your national dermatology body.
* For tissue culture in suspected infection: your local microbiology and mycology laboratory's
  user handbook, as m118's sources.
* For consent, documentation and what must be discussed before a procedure: your national
  regulator's guidance and your institution's consent policy.
* For keloid and hypertrophic scarring risk by site and skin type: a current standard textbook of
  dermatology.

The Pokémon claims were checked separately against source. `LEVEL_UP_MOVE(lvl, move)` being
defined as `((lvl << 9) | move)` with `LEVEL_UP_MOVE_ID` 0x01FF, `LEVEL_UP_MOVE_LV` 0xFE00 and
`LEVEL_UP_END` 0xFFFF, so the sentinel masks to the maximum value under both masks; `FlagGet`
having two distinct `return FALSE` paths, one from a null pointer and one from a genuinely clear
bit, with `GetFlagPointer` returning NULL for id zero, against `VarGet` returning the id itself on
a failed lookup; the five state structures of the third generation being `status1`, `status2`,
`gStatuses3`, the side statuses and the field weather, with `status2` and `gStatuses3` zeroed on
an ordinary switch and `status1` untouched by `SwitchInClearSetData`; Growl having base power 0,
accuracy 100 and 40 PP and lowering Attack by one stage, while Leech Seed lives in `gStatuses3`
and drains `maxHP / 8` with no Attack term; `EFFECT_RECOIL_IF_MISS` having exactly two members,
Jump Kick at base power 70, accuracy 95, 25 PP and Hi Jump Kick at base power 85, accuracy 90, 20
PP, both Fighting-type and both making contact; Hitmonlee learning Jump Kick at level 16 and Hi
Jump Kick at level 26, with Mega Kick at 46 and Reversal at 51 in the same table; Bulbasaur's
learnset containing `LEVEL_UP_MOVE( 7, MOVE_LEECH_SEED)`; Rock Head being held by Steelix and
Aggron, both Steel-types; `BattleScript_EffectRecoilIfMiss` directing a miss to
`BattleScript_MoveMissedDoDamage`, which does damage to the user; and `ABILITY_ROCK_HEAD`
appearing only in `BattleScript_MoveEffectRecoil`, after the `jumpifmove MOVE_STRUGGLE,
BattleScript_DoRecoil` line and nowhere in the crash branch — all from the pret decompilation of
Pokémon Emerald. The Rock Head reading is m104's and the `FlagGet` reading is m073's, both from
the same source.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, not a procedural guide and not reviewed by a clinician. It is not
for use in making a decision about anyone's care, including your own, and nothing here is
instruction in how to perform a procedure.

**No measurement, margin, depth threshold, staging boundary, anaesthetic agent, dose or time
window appears in this answer, and none of it addresses any reader's own treatment.** The omission
of the melanoma staging measurements and of the vasculitis timing window is deliberate: both are
defined in the documents named above and a figure quoted here without the document would be worse
than the principle stated without it.

Anyone with a new, changing, bleeding or non-healing skin lesion needs to be assessed in person. A
changing pigmented lesion is assessed urgently.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The method is settled and is the part worth memorising: the specimen bounds the report, the
compartment has to be in the pot, the medium is irreversible, the sectioning plane is a choice,
and the request form is part of the instrument. The pertinent-negative problem is settled and
remains widely mishandled.

What moves is at the edges. Molecular and sequencing-based testing on tissue has expanded what a
fixed specimen can be asked, which has relaxed the fresh-tissue requirement in some laboratories
and not in others, so it is firmly (**country-dependent**) and sending fresh tissue when infection
is in the differential remains the safe default. Digital pathology and whole-slide imaging have
changed how second opinions are obtained more than what a specimen can say, and computational
assessment of dermatopathology slides is active with its place in routine reporting unsettled. In
skin cancer, who takes the diagnostic specimen — dermatology, surgery, or primary care under a
local scheme — has shifted in several countries and is the part most likely to differ from what
you were taught. Non-invasive imaging including reflectance confocal microscopy and optical
coherence tomography is reducing biopsy numbers in some specialist centres without replacing them,
and availability is narrow. Current as of October 2026.
