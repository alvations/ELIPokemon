---
id: "m118"
slug: granulomatous-pattern-versus-cause
style: pokemon
category: dermatology
difficulty: advanced
question: "Why does a report of granulomatous inflammation name a pattern rather than a cause, and what has to happen next for the cause to be found?"
tags: [granuloma, sarcoidosis, histopathology, special-stains, mycobacteria]
---

# One greyed-out move, eight reasons, six stores, and one of them is on the other side of the field

Open the battle menu and a move is greyed out. That readout is honest, informative and completely
silent about why. `CheckMoveLimitations` is the function that produces it, and it is worth reading
in full because its shape is the shape of a histopathology report.

```
   CheckMoveLimitations -- every condition that greys out a slot
   ==================================================================================
   for (i = 0; i < MAX_MON_MOVES; i++)
   {
     1  empty slot        moves[i] == MOVE_NONE
     2  no PP             pp[i] == 0
     3  Disable           moves[i] == gDisableStructs[battler].disabledMove
     4  Torment           moves[i] == gLastMoves[battler]
                            AND status2 & STATUS2_TORMENT
     5  Taunt             gDisableStructs[battler].tauntTimer
                            AND gBattleMoves[moves[i]].power == 0
     6  Imprison          GetImprisonedMovesCount(battler, moves[i])
     7  Encore            gDisableStructs[battler].encoreTimer
                            AND encoredMove != moves[i]
     8  Choice lock       holdEffect == HOLD_EFFECT_CHOICE_BAND
                            AND *choicedMove != moves[i]
                            -- a Choice Band sitting in the item slot
                                   |
                                   v
         unusableMoves |= gBitTable[i];     <-- ALL EIGHT write here
   }
   ==================================================================
   EIGHT conditions. ONE bitfield. The caller receives a bit and no
   indication of which condition set it.

   AND THE STORES THEY READ FROM:
     gBattleMons[].moves / .pp        the Pokemon's own move data
     gBattleMons[].status2            the volatile store
     gDisableStructs[]                four separate timers in one struct
     gLastMoves[]                     a different global array
     gBattleStruct->choicedMove       the battle-scratch store
     gStatuses3 -- via GetImprisonedMovesCount, WHICH READS THE
                   OTHER SIDE OF THE FIELD
   ==================================================================
   TWO OF THE EIGHT CANNOT BE EXCLUDED FROM THE QUERY. Conditions
   1-6 are each guarded by `check & MOVE_LIMITATION_*`, so a caller
   can ask a narrower question. Encore and the Choice lock carry no
   such guard -- they apply whatever was asked.
   ==================================================================
```

Condition five is worth one concrete line, because it shows how little the readout carries.
**Taunt** greys out a slot only when `gBattleMoves[moves[i]].power == 0`, so after one Taunt a
Pokémon loses **Calm Mind**, **Swords Dance**, **Protect** and **Light Screen** — all four at base
power 0 — while keeping every attacking move it owns. **Disable** greys out one named move.
**Torment** greys out whichever move was used last. **Encore** greys out all three of the others.
Four mechanics, four entirely different underlying situations, and on screen each of them is a
slot in grey.

A report of "granulomatous dermatitis" is that bitfield. It is true, it is useful, and it is one
value written by any of a long list of conditions that read from different places. (**mechanism**)
And the Imprison row is the one to hold on to, because the cause of a granuloma in the skin is
frequently not in the skin at all.

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. (**mechanism**) —
follows from the biology and is checkable by reasoning. (**definitional**) — a term's meaning.
(**consensus**) — standard across current textbooks and national guidance. (**country-dependent**)
— differs between countries or institutions, and yours is the authority. The Pokémon claims are
not marked this way; they are listed in the `## Sources` section with the file they were checked
against.

## The pattern is the bitfield, and the cause is the condition that set it

A granuloma is an organised collection of macrophages, often with multinucleate giant cells, with
or without a lymphocyte cuff and with or without central necrosis. (**definitional**) It forms
when macrophages meet something they cannot clear or digest, and it keeps forming while the
something persists. (**mechanism**)

Three consequences, and they are the whole argument.

* **Anything persistent can set the bit.** An organism that resists killing, a particle that
  cannot be digested, a self-antigen, a degenerate piece of the host's own matrix.
* **The repertoire is narrow.** Tissue has only so many ways to wall something off, so unrelated
  stimuli converge on similar architecture — eight conditions, one `|=`.
* **So the architecture under-determines the cause.** It carries real weight, the way the
  greyed-out slot does narrow things, and it is nothing like sufficient.

The architectural patterns and what each leans toward:

| Pattern | Leans toward | What it does not establish |
| --- | --- | --- |
| **Sarcoidal** — tight, "naked", scanty lymphocytes, little necrosis | Sarcoidosis | Also foreign-body reactions including tattoo pigment, and some infections (**consensus**) |
| **Tuberculoid** — caseating central necrosis with a lymphocyte cuff | Mycobacterial infection | Not a diagnosis of it, and absence of necrosis does not exclude it |
| **Palisading** — histiocytes around altered collagen, mucin or fibrin | Granuloma annulare, necrobiosis lipoidica, rheumatoid nodule | Which of the three; the centre's content is a histological judgement |
| **Suppurative** — neutrophil abscesses inside granulomas | An organism: deep fungal, atypical mycobacterial, bacterial | Which organism. This is where the stain and the culture carry most weight (**consensus**) |
| **Foreign body** — giant cells engulfing identifiable material | Exogenous or endogenous material | Whether the material arrived from outside or from a ruptured structure inside — m117's follicle produces this with the host's own keratin |

And the causes, which cut across every row rather than lining up with one: infection (mycobacteria
including leprosy and the atypicals, deep and subcutaneous fungi, leishmania, treponemes); foreign
material, exogenous or endogenous in the wrong compartment; immune-mediated disease (sarcoidosis,
granulomatous rosacea, cutaneous Crohn's disease, granulomatous cheilitis); matrix disease
(granuloma annulare, necrobiosis lipoidica, rheumatoid nodule); granulomatous disease in
immunodeficiency; and drug reactions, including to some immunomodulatory agents. (**consensus**)

The non-correspondence between the two lists is the answer to the question in the title.

## Imprison reads the other side, and so does the cause

`GetImprisonedMovesCount` is condition six, and it is the only one that leaves the battler's own
data entirely. It walks the **opposing** battlers, reads their `gStatuses3` for
`STATUS3_IMPRISONED_OTHERS`, and compares their move slots against yours. The move is greyed out
because of something stored on a Pokémon you are not looking at.

That is the most useful single line in this answer. A cutaneous granuloma's cause is frequently
not cutaneous. (**mechanism**, **consensus**)

* **Sarcoidosis** is systemic, and skin involvement may be its presenting feature — so the
  assessment that finds the cause includes the eyes, the lungs, the heart and calcium handling,
  which are in the guidance named below rather than in the dermatology consultation alone.
* **Cutaneous Crohn's disease** is granulomatous skin arising from a disease of the bowel.
* **A foreign body** may have been implanted years earlier, somewhere else, by something nobody
  thought to ask about.
* **An inhaled or injected antigen** is in the history, not the specimen.
* **A drug** is on the list, not in the block.

A work-up that reads only the battler's own stores will return a confident bit and no cause. The
systems review is not an adjunct to the investigations; in a large share of cases it *is* the
investigation. (**consensus**)

## The negative stain is m089's confident zero, with a different instrument

m089 established the house version of this: sampling from inside the blister reads
`gBattleMons[i].status2`, gets a genuine zero, and the answer was sitting in `gSideStatuses[side]`
all along — **a confident zero from the wrong structure is worse than no result**, because an
absent result and an unobtainable one are reported identically.

Granulomatous disease has the same failure with a different cause. Here the zero comes from an
**insensitive query** rather than the wrong store. Histochemical stains for organisms — acid-fast
for mycobacteria, silver and periodic-acid for fungi — are specific but insensitive in tissue.
(**consensus**) In paucibacillary disease the organisms are few and unevenly distributed, and the
section examined is a thin slice of a small sample. "No acid-fast bacilli seen" means exactly what
it says and is routinely read as "not mycobacterial".

So what actually interrogates the cause:

```
   WHAT ANSWERS THE CAUSE QUESTION, AND WHAT IT COSTS
   ==================================================================================
   INSTRUMENT                     ESTABLISHES               THE CATCH
   ===========================    ======================    =====================
   tissue culture --              identification, and       needs FRESH TISSUE,
   mycobacterial and fungal       susceptibility            not the formalin pot,
                                                            so it must be decided
                                                            BEFORE the cut
   ===========================    ======================    =====================
   molecular testing on tissue    identification where      availability and the
                                  culture is slow or        targets offered are
                                  fails                     country-dependent
   ===========================    ======================    =====================
   POLARISED LIGHT on the         birefringent foreign      somebody has to ask.
   section already cut            material -- silica,       The material is in the
                                  talc, suture, fillers     block already
   ===========================    ======================    =====================
   serology / interferon-gamma    EXPOSURE, not tissue      interpretation varies
   release / tuberculin           diagnosis                 by population and by
                                                            immune status
   ===========================    ======================    =====================
   clinical and systems review    the cause, in a large     it is not on the list
                                  share of cases            of "investigations"
   ==================================================================
   The first row is the commonest reversible failure in this whole territory,
   and it is reversible at the moment of the request form and nowhere later.
   ==================================================================
```

The polarised-light row deserves its own sentence. Cross-polarisation on a histological section is
the same physics m020 sets out for dermoscopy: change the illumination and structure that was
present and unseen becomes visible. It costs nothing, it is not routine, and so the material sits
in the block unrecorded until a question is asked that calls for it. m073's `FlagGet` point
applies exactly — a store that returns the same answer for "nothing there" and "nobody looked"
cannot hold a pertinent negative.

## Water Absorb is why the direction matters

If the cause were only of academic interest, the pattern report would be enough. It is not,
because the two main branches need interventions of **opposite sign**, and that is a thing the
game models precisely rather than vaguely.

Surf is a Water move with base power 95. Against most targets it does damage. Against a Pokémon
with **Water Absorb** the ability fires in `AbilityBattleEffects`, the script becomes
`BattleScript_MoveHPDrain`, and `gBattleMoveDamage` is set to `maxHP / 4` and then **multiplied by
minus one**. The same act heals the target by a quarter of its maximum. And the result flag
written is `MOVE_RESULT_DOESNT_AFFECT_FOE`, which is a third thing again. (At full HP it does
neither: the script becomes `BattleScript_MonMadeMoveUseless`.)

One act, three signs, decided by a property of the target you cannot see from outside. m055 uses
this device in this specialty already and this answer reuses it rather than inventing a second.

The holders are worth naming because the list is longer than the famous entry. **Water Absorb** in
the third generation belongs to **Lapras**, **Vaporeon**, **Politoed**, **Poliwag**,
**Poliwhirl**, **Poliwrath**, **Wooper**, **Quagsire** and **Mantine** — nine species, several of
which no player would check before pressing Surf, and **Quagsire** in particular is the one people
misremember as holding Cloud Nine instead. Nothing on the sprite says which of the nine you are
facing, and the first Surf is how you find out. m055's point was that the game records an
opponent's ability only when it fires; the same holds here, and it is why the first course of
immunosuppression in an unidentified granuloma is the experiment rather than the treatment.

* **An infective granuloma treated with immunosuppression gets worse**, and in mycobacterial and
  deep fungal disease the worsening can be substantial. That is the whole reason latent
  tuberculosis screening precedes immunosuppressive and biologic therapy as a routine rather than
  a precaution. (**consensus**)
* **An immune-mediated granuloma treated with antimicrobials** does not respond, and the
  non-response costs months.

So the pattern report is a question. Treating it as an answer is choosing a sign at random.

## Sarcoidosis is a conjunction, and that makes it unstable by construction

Cutaneous sarcoidosis needs a compatible clinical picture, non-caseating granulomas on histology,
and **exclusion of the other causes of the same pattern** — infection and foreign material in
particular. (**consensus**, **definitional**) There is no positive test.

Two things follow, and the second is the one that gets missed.

A report of non-caseating sarcoidal granulomas is **not** a diagnosis of sarcoidosis, however
often it is read as one. And because the diagnosis rests partly on exclusion, it is provisional in
the way exclusion diagnoses always are: a granulomatous disease called sarcoidosis that is not
behaving as expected should send you back to infection and foreign body, not up the
immunosuppression ladder. (**mechanism**) Lupus pernio is the variant conventionally flagged for
its association with more extensive systemic disease. (**consensus**)

Treatment at the level of principle only; no agent, dose, strength or regimen appears in this
answer. Granuloma annulare is frequently self-limiting, so the balance between treating and
waiting is real. Necrobiosis lipoidica carries an association with diabetes that makes assessment
of glucose handling part of the work-up, and the lesions are liable to ulcerate. Cutaneous
sarcoidosis is treated according to extent, site and systemic involvement, and the disfiguring
facial forms are treated more aggressively than their physical extent alone would suggest.
Infective causes are treated according to organism and susceptibility — which is what the extra
pot buys.

## Where the metaphor stops

No Pokémon in this answer stands in for a person, and a greyed-out move slot is a fact about a
bitfield rather than about anybody's prospects. Three things need saying without ornament.

**Granulomatous conditions are slow, and being investigated slowly has its own weight.** The
sequence described above routinely takes months, often with an interim label that later changes.
When the shortlist contains both an infection and an immune disease, the person waiting is holding
two quite different futures at once, and that is worth acknowledging rather than managing.

**Several of these conditions are visibly disfiguring, and on the face.** Lupus pernio and the
plaque forms of cutaneous sarcoidosis can be prominent and persistent; necrobiosis lipoidica on
the shins is visible and liable to ulcerate; facial granulomatous disease is not concealable. The
extent of skin affected is a poor guide to what it costs someone, so a treatment decision weighing
only physical extent will systematically under-treat the disfiguring forms. That is not a sympathy
point; it is a decision-making error with a known direction.

**And two sentences are worth saying out loud.** First, that a pattern report is genuinely
informative even though it is not a diagnosis — because "we do not know yet" and "the test told us
nothing" are different statements and they get confused, usually in the direction that makes
someone lose confidence in the process. Second, that a change of label later is the process
working rather than an earlier mistake, because an exclusion diagnosis is provisional by
construction and saying so in advance costs nothing.

Nothing here is for any reader's own use and no treatment named or implied is a recommendation.
Granulomatous skin disease needs specialist assessment. The situations needing it urgently: any
possibility of mycobacterial or deep fungal infection before immunosuppression is started; eye
symptoms with suspected sarcoidosis; a non-healing or ulcerating lesion; and any granulomatous
diagnosis in someone whose immune system is suppressed, where the infective possibilities widen
considerably.

## What a Gym Leader is listening for

What a granuloma is, definitionally, and why the structure forms at all. The architectural
patterns, what each leans toward, and why no pattern maps onto one cause. What a negative
acid-fast or fungal stain on tissue does and does not establish. What has to be decided before the
knife rather than after. What polarised light adds and why it is not routine. The three elements
of a sarcoidosis diagnosis, and why a report of non-caseating granulomas is not one. Why a
granulomatous diagnosis that is not behaving sends you back to infection. Why latent tuberculosis
screening precedes immunosuppression. And why a cutaneous granuloma's cause is so often not
cutaneous.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For granuloma architecture, the patterns and the differential for each: a current standard
  textbook of dermatopathology.
* For what your laboratory needs in order to culture mycobacteria or fungi from tissue — medium,
  quantity, fresh or in saline, and how to label the request: the user handbook of your local
  microbiology and mycology laboratory. It is the authority and it differs between laboratories.
* For sarcoidosis — the diagnostic framework, the systemic assessment including eye, cardiac,
  pulmonary and calcium evaluation, and the treatment pathway: your national sarcoidosis guidance
  and the specialist guidance of your national dermatology body.
* For latent tuberculosis screening before immunosuppressive or biologic therapy: your national
  tuberculosis guidance, which specifies test, population and timing and differs substantially by
  country.
* For leprosy, including case definitions and classification: your national guidance and the
  relevant international programme documentation.
* For granuloma annulare and necrobiosis lipoidica, including the diabetes association: a current
  standard textbook of dermatology and your national diabetes guidance.
* For antimicrobial and antifungal agents and treatment duration in mycobacterial and deep fungal
  disease: your national formulary and national antimicrobial guidance.

The Pokémon claims were checked separately against source. `CheckMoveLimitations` containing
exactly the eight ORed conditions listed above, all writing into one `unusableMoves` bitfield,
with conditions one to six each guarded by a `check & MOVE_LIMITATION_*` test while the Encore and
Choice-lock conditions carry no such guard; its reading from `gBattleMons[].moves`, `.pp` and
`.status2`, from four timers in `gDisableStructs[]`, from `gLastMoves[]`, from
`gBattleStruct->choicedMove` and, through `GetImprisonedMovesCount`, from `gStatuses3` on the
other side of the field; Water Absorb firing in `AbilityBattleEffects` for a Water move of
non-zero power, redirecting to `BattleScript_MoveHPDrain`, setting `gBattleMoveDamage` to `maxHP /
4` with a floor of 1 and then multiplying it by minus one, writing
`MOVE_RESULT_DOESNT_AFFECT_FOE`, and redirecting to `BattleScript_MonMadeMoveUseless` instead when
the absorber is at full HP; Surf having base power 95, accuracy 100 and 15 PP; Water Absorb in the
third generation being held by Lapras, Vaporeon, Politoed, Poliwag, Poliwhirl, Poliwrath, Wooper,
Quagsire and Mantine, with Quagsire's two abilities being Damp and Water Absorb rather than Cloud
Nine; and Calm Mind, Swords Dance, Protect and Light Screen each having base power 0 and therefore
each being blocked by Taunt — all from the pret decompilation of Pokémon Emerald, the ability
holders read from the species information table rather than recalled. The `gSideStatuses` and
`status2` contrast is m089's and is from the same source.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No agent, dose, regimen, duration, test threshold or diagnostic score appears in this answer,
and none of it addresses any reader's own treatment.** The insensitivity of the histochemical
stains is given as a direction rather than a figure on purpose: the numbers depend on organism,
burden and laboratory, and one figure quoted here would mislead in most of the situations it would
be applied to.

Granulomatous skin disease needs specialist assessment. Any possibility of mycobacterial or deep
fungal infection must be addressed before immunosuppression is started. Eye symptoms with
suspected sarcoidosis, a non-healing or ulcerating lesion, and granulomatous disease in someone
whose immune system is suppressed all need prompt assessment in person.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The central argument is settled and is the part worth memorising: a granuloma is a response
pattern, the repertoire is narrow, and the architecture under-determines the cause. The
insensitivity of tissue stains for organisms is settled. The requirement that sarcoidosis be a
conjunction including exclusion of infection is settled.

What moves is the identification step. Molecular detection of mycobacteria and fungi directly from
tissue, including from fixed material in some laboratories, has improved and partially relaxed the
fresh-tissue requirement — partially, and only where the service exists, so it is firmly
(**country-dependent**) and sending fresh tissue remains the safe default. Metagenomic sequencing
of tissue is moving from research into selected diagnostic use and its place is unsettled. On the
treatment side, granulomatous reactions to newer immunomodulatory agents are increasingly
recognised, which adds a drug column to a differential that used not to have one prominently.
Sarcoidosis pathways and the role of steroid-sparing and biologic agents in cutaneous disease
continue to be revised, and funding differs by country. Current as of October 2026.
