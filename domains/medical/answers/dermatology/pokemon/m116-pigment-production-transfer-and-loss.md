---
id: "m116"
slug: pigment-production-transfer-and-loss
style: pokemon
category: dermatology
difficulty: advanced
question: "Why are the pigmentary disorders better grouped by whether melanin production, melanin transfer or the melanocyte itself has failed?"
tags: [pigmentation, melanocyte, vitiligo, melasma, mechanism]
---

# Which structure the state is stored in decides whether anything can ever clear it

m089 established the device this answer extends, so it is worth restating in one sentence. The
third generation keeps "protected" in **five separate structures** — `status1`, `status2`,
`gStatuses3`, the side statuses with their own timers, and the field weather — and which structure
a state lives in decides what reads it, what clears it, and what survives a switch. m089 used that
to argue about *sampling*: a confident zero from the wrong structure is worse than no result.

This answer uses the same five structures to argue about *clearance*, which is a different axis.
The question is not where you look. It is **which store the value landed in**, because two stores
with identical contents behave completely differently when the Pokémon leaves the field, and in
exactly one of them the value is gone forever.

That is the whole pigment argument. Melanin made and delivered into a cell that will be shed is in
one store. Melanin dropped into the dermis is in another. They look the same on the screen and
they are not the same object.

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. (**mechanism**) —
follows from the biology and is checkable by reasoning. (**definitional**) — a term's meaning.
(**consensus**) — standard across current textbooks and national guidance. (**country-dependent**)
— differs between countries or institutions, and yours is the authority. The Pokémon claims are
not marked this way; they are listed in the `## Sources` section with the file they were checked
against.

## `status2` is wiped on the way out and `status1` is not, and that is the prognosis

`SwitchInClearSetData` is the function that runs when a Pokémon leaves and another arrives, and it
is worth reading for what it does *not* do. On an ordinary switch it executes two assignments:

```
   ORDINARY SWITCH -- SwitchInClearSetData, the non-Baton-Pass branch
   ==================================================================================

   gBattleMons[gActiveBattler].status2 = 0;      <-- confusion, Substitute,
   gStatuses3[gActiveBattler]          = 0;          infatuation, trapping, Leech
                                                     Seed, Ingrain, Perish Song,
                                                     Focus Energy: all gone

   statStages[i] = DEFAULT_STAT_STAGE            <-- every stage back to neutral

   ClearBattlerMoveHistory(gActiveBattler);      <-- and the record of how it got
   ClearBattlerAbilityHistory(gActiveBattler);       here is destroyed too
   ==================================================================
   AND THE THING THE FUNCTION NEVER MENTIONS:

   status1  --  the word "status1" appears ZERO times in the whole
                function body. Burn, poison, paralysis, sleep and
                freeze are not cleared by switching out, because
                nothing in the switch path touches that field.
   ==================================================================
   TO CLEAR status1 YOU NEED A ROUTINE WRITTEN FOR THE PURPOSE.
   Cmd_switchoutabilities is a DIFFERENT command, and inside it the
   only case in the switch statement is:

        case ABILITY_NATURAL_CURE:
            gBattleMons[gActiveBattler].status1 = 0;

   One ability, one explicit assignment, in a routine that exists
   for no other reason.
   ==================================================================
```

Map that onto the epidermis and the mapping does the work for you. **Melanin delivered into a
basal keratinocyte is `status2`.** The holder is on a conveyor: it differentiates, moves up, and
is shed, and the pigment goes with it. Nobody has to intervene. Turnover is
`SwitchInClearSetData`, and it zeroes the field as a side effect of the holder leaving. Epidermal
pigment fades because its store is wiped on the way out. (**mechanism**)

**Melanin dropped into the dermis is `status1`.** The holder leaves, the store is untouched, and
nothing in the ordinary path has any instruction about it. Clearing it needs a routine written for
the purpose — in the skin, slow macrophage handling — and the fact that such a routine exists at
all does not make it fast. Dermal pigment persists for months to years, and it is the same
structural reason: it is in the field the switch path does not mention. (**mechanism**,
**consensus**)

This is why the single most useful bedside test in pigmentation is the one that asks **which
store** rather than **how much**. Wood's lamp accentuates epidermal pigment and does not
accentuate dermal pigment. (**consensus**) It is not measuring severity. It is reading the field
name.

## Baton Pass hands over the state and does not hand over the maker

Transfer is a real step with a real failure mode, and the game has a precise model of a handoff.
Baton Pass is implemented inside the same `SwitchInClearSetData`, as the other branch, and it is
not a copy. It is a **mask-and**: the surviving state is whatever is left after the field is ANDed
with a hand-written whitelist.

```
   BATON PASS -- the whitelist, exactly as written
   ==================================================================================
   status2 &= ( STATUS2_CONFUSION | STATUS2_FOCUS_ENERGY | STATUS2_SUBSTITUTE
              | STATUS2_ESCAPE_PREVENTION | STATUS2_CURSED )          five bits

   gStatuses3 &= ( STATUS3_LEECHSEED_BATTLER | STATUS3_LEECHSEED
                 | STATUS3_ALWAYS_HITS | STATUS3_PERISH_SONG
                 | STATUS3_ROOTED | STATUS3_MUDSPORT
                 | STATUS3_WATERSPORT )                              seven bits

   the DisableStruct is zeroed and then five fields are written back
   from a copy taken before the wipe: substituteHP, battlerWithSureHit,
   perishSongTimer, perishSongTimerStartValue, battlerPreventingEscape
   ==================================================================
   AND IN BOTH BRANCHES, UNCONDITIONALLY:

     gLastMoves, gLastLandedMoves, gLastResultingMoves, gLastHitBy
     ClearBattlerMoveHistory, ClearBattlerAbilityHistory

   The STATE is passed. The HISTORY is cleared either way.
   ==================================================================
```

A melanocyte makes melanosomes and delivers them along its dendrites into the surrounding basal
keratinocytes. What arrives is the pigment. What does not arrive is any record of which melanocyte
made it, or why, or when. (**mechanism**) The keratinocyte holds a value from a whitelist and no
provenance at all — which is precisely why a pigmented patch cannot be dated by looking at it, and
why the history has to come from the person rather than from the skin. m087 makes the same point
from the opposite direction for the nail plate, where the record of elapsed time *is* preserved
and can be read off; pigment is the case where it is not.

The whitelist is also the right shape for the failure. **Naevus depigmentosus** has melanocytes in
normal number and impaired melanosome transfer: the producer is present and the handoff does not
happen. (**consensus**) That is a Baton Pass where the bit was not in the mask. Nothing is wrong
with the maker, nothing is wrong with the receiver, and the value does not arrive.

## Vitiligo is a zero, and Flygon is the reason that matters

The house device for this is settled and this answer reuses it rather than inventing a new one.
Ground into Flygon is coded as **no effect**, not as a reduction. Earthquake has base power 100
and against Flygon it does nothing at all, and the correct description is not "it is less
effective". No repetition, no stacking and no amount of power crosses a zero. m007 established
this for a drug with no mechanism against its target; m089's Wonder Guard section is the same
shape.

**Hypopigmentation is a reduced value. Depigmentation is a zero.** (**definitional**) In vitiligo
the melanocytes are gone from affected skin, so there is no cell for an upstream stimulus to act
on. (**mechanism**, **consensus**) The patches are chalk- or milk-white rather than merely pale,
they accentuate sharply under Wood's lamp, and white hairs inside a patch say the follicular
population has gone as well. (**consensus**)

Three things follow from it being a zero rather than a small number, and all three are the sort of
thing an answer should say out loud:

* ultraviolet exposure cannot darken it, so the patch does not tan and the contrast with the
  surrounding skin **increases** over a summer;
* anything aimed at reducing pigment production is aimed at a step that is not running;
* depigmented skin has no melanin and therefore none of melanin's photoprotection, which is the
  one genuinely urgent practical consequence in this whole answer. (**mechanism**)

Against that, **pityriasis versicolor** is a reduction and not a zero: a commensal yeast
overgrowing in the stratum corneum interferes with pigment production, and the melanocytes are
intact. (**mechanism**, **consensus**) It is Growl rather than Earthquake-into-Flygon — the number
gets smaller and the machinery is all still there. And it has the tail m086 would recognise: the
pale patches **outlast the organism**, so a treated patient whose colour has not yet returned has
not failed treatment. Saying that at the first visit prevents a second unnecessary course.

## The level-up learnset is the reservoir, and it is why repigmentation is perifollicular

The best mechanical fact in this territory is that recovery has a source, and the game has an
exact model of a source list.

A move the player deletes is gone from the Pokémon's four slots. Whether it can come back depends
entirely on whether it is in `gLevelUpLearnsets[species]` — the per-species table the Move
Reminder reads, walked until the `LEVEL_UP_END` sentinel. A level-up move is recoverable because
the source list still holds it. A move taught from a TM, or an Egg Move, is **not** in that table,
so the Move Deleter's work on it is irreversible. m087 used exactly this for scarring against
non-scarring hair loss, and the shape is identical here, so this answer reuses it rather than
deriving a second device for one idea.

Melanocytes persist in the **outer root sheath of the hair follicle**, and repopulation of
depigmented epidermis proceeds from there. (**mechanism**, **consensus**) The source list is
follicular. Three predictions follow, and every one of them is something you can see:

```
   WHAT THE RESERVOIR PREDICTS
   ==================================================================================
   OBSERVATION                        WHY, IN ONE LINE
   ================================   ===============================================
   repigmentation appears as           the source is follicular, so recovery starts
   PERIFOLLICULAR DOTS inside a        at the follicles and spreads outward -- it is
   patch, not as the border fading     not the edge creeping in
   ================================   ===============================================
   fingertips, palms, soles, lips      few or no follicles, so the species table has
   and mucosal margins respond         no entry to read. Acral and perioral disease
   poorly                              is the hard kind for a structural reason
   ================================   ===============================================
   a patch containing WHITE HAIRS      the follicular population has gone too. The
   predicts a worse response           Move Deleter got the Egg Move: nothing is left
                                       in the table to restore from
   ==================================================================
   The same argument as m087, from the other end. The recoverable case is the one
   where the source structure survives. Scarring is the case where it does not.
   ==================================================================
```

## Where the metaphor stops

No Pokémon anywhere in this answer stands in for a person, and none of the mechanics above says
anything about what will happen to anyone. A battle state being stored in one field rather than
another is a fact about a data structure; whether a person's pigment will return is a question for
the specialist service with the actual findings, and nothing here can answer it.

Three things need saying without ornament.

**Pigmentary disorders are routinely called cosmetic, and that label is wrong in a way that
changes care.** Visible difference in pigmentation on the face and hands carries a measured burden
of psychological distress and of avoidance of social and working situations, and in a number of
cultural contexts it carries stigma that extends to marriage and employment. The quality-of-life
burden of vitiligo specifically has been studied repeatedly and is substantial. Declining to
engage with it because nothing dangerous is happening is a failure of the consultation, not a
triage decision — and it is the commonest thing that goes wrong in this part of dermatology.

**Skin-lightening products bought outside regulated supply are widely used** for
hyperpigmentation, and some have been found to contain potent corticosteroids, mercury compounds,
or hydroquinone at unregulated strength. The harms are real and include irreversible paradoxical
pigmentation. Asking what someone has already tried, without disapproval, usually changes the
assessment; disapproval usually ends the disclosure. Which products are restricted and which
specific contaminants have been named in warnings differ by country, and the regulator where you
practise is the authority.

**And the diagnoses that are made only by someone thinking of them.** A pale patch with reduced
sensation needs leprosy considered. Pigment change beginning after a new medicine needs the
medicine considered. A pigmented lesion that is changing is a different question entirely and is
assessed urgently. None of those three is suggested by the colour alone, which is the point.

Nothing in this answer is for any reader's own use, and no treatment named or implied here is a
recommendation. Anyone with a new or changing pigmented lesion, a pale patch with altered
sensation, or pigment change that began after starting a medicine, needs to be assessed in person.

## What a Gym Leader is listening for

Which of the three steps has failed, and what in the examination told you. Hypopigmented or
depigmented, and why that single word changes the plan. What Wood's lamp accentuates, what it does
not, and why that makes it prognostic rather than diagnostic. Why dermal melanin persists when
epidermal melanin does not — in terms of the store, not the colour. Why pityriasis versicolor
leaves pale skin after the yeast has gone. How naevus anaemicus is separated from naevus
depigmentosus with no instrument. Where melanocytes repopulate from, and the three things that
predicts. And why the word cosmetic should not appear in the consultation.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For melanocyte biology, the synthetic pathway, the epidermal melanin unit and the classification
  of the pigmentary disorders: a current standard textbook of dermatology.
* For vitiligo — classification, assessment, associated autoimmune disease and treatment options
  including phototherapy and depigmentation: the specialist guidance of your national dermatology
  body. Availability and funding differ by country.
* For melasma and post-inflammatory hyperpigmentation, and for the licensed strengths of topical
  agents: your national formulary.
* For the regulation of skin-lightening products and the contaminants named in warnings: your
  national medicines and healthcare products regulator and your national public health body.
* For occupational chemical leukoderma: your national occupational health authority.
* For a hypopigmented patch with altered sensation: your national guidance on leprosy and the
  relevant international programme documentation, which hold the case definitions.

The Pokémon claims were checked separately against source. `SwitchInClearSetData` zeroing
`status2` and `gStatuses3` on an ordinary switch, resetting every stat stage to
`DEFAULT_STAT_STAGE`, calling `ClearBattlerMoveHistory` and `ClearBattlerAbilityHistory`
unconditionally, and containing no reference to `status1` anywhere in its body;
`Cmd_switchoutabilities` being a separate command whose switch statement has exactly one case,
`ABILITY_NATURAL_CURE`, assigning `status1 = 0`; Baton Pass being implemented as the other branch
of the same function, masking `status2` against five named bits and `gStatuses3` against seven,
and restoring five `DisableStruct` fields from a copy taken before the wipe; Ground being coded as
no effect into Flying; Earthquake having base power 100; Growl having base power 0, accuracy 100
and 40 PP and lowering Attack by one stage; and the Move Reminder reading
`gLevelUpLearnsets[species]` with a `LEVEL_UP_END` sentinel, so a level-up move is recoverable and
a TM or Egg Move deleted is not — all from the pret decompilation of Pokémon Emerald. Flygon's
Ground immunity comes from its Flying type and not from an ability.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No agent, strength, concentration, phototherapy dose or treatment schedule appears in this
answer, and none of it addresses any reader's own treatment.** The omission is deliberate: topical
depigmenting and repigmenting agents differ in licensed strength and availability between
countries, several circulate outside regulated supply at strengths that cause harm, and a figure
quoted here without the formulary would be worse than no figure.

Anyone with a new or changing pigmented lesion, a pale patch with reduced sensation, pigment
change that began after starting a medicine, or widespread depigmentation, needs to be assessed in
person. A changing pigmented lesion is assessed urgently.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The biology is settled and is the part worth memorising: three steps, three failure modes, and the
epidermal-versus-dermal store question that predicts whether colour can return. The reservoir
argument is settled too, and it is what makes the distribution of vitiligo's treatment response
intelligible rather than arbitrary.

What moves is treatment. Vitiligo has moved most: targeted immunomodulatory topical therapy
reached licensing in several jurisdictions within the last few years and changed the conversation
from camouflage and phototherapy to active treatment, and whether any of it is available or funded
where you practise is firmly (**country-dependent**). Phototherapy protocols and combination
regimens continue to be revised, and surgical melanocyte transfer remains specialist with narrow
indications. In melasma the move has been away from single-agent topical treatment toward
photoprotection plus combinations, with ultraviolet-independent visible-light pigmentation taken
more seriously than it was. Regulatory action on unlicensed skin-lightening products is active in
several countries and the compounds named change. Current as of October 2026.
