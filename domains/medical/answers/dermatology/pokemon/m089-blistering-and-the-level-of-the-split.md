---
id: "m089"
slug: blistering-and-the-level-of-the-split
style: pokemon
category: dermatology
difficulty: advanced
question: "Why does the level at which the skin splits determine almost everything that follows in a blistering disease?"
tags: [blistering, pemphigus, pemphigoid, immunofluorescence, biopsy]
---

# The game stores "protected" in five different places, and the place decides what gets through

Ask what is protecting a Pokémon and the honest answer is a question back: protected at which
level? Because the third-generation code does not have one place for that. It has five, they are
separate C variables, and **which variable a state is written into decides what reads it, what
clears it, and what survives a switch.**

```
   FIVE STRUCTURES, FIVE CLEARING RULES
   ==================================================================================

   WHERE IT LIVES          WHAT IS IN IT                  WHAT CLEARS IT
   =====================   ============================   ===========================
   status1                 sleep, poison, burn, freeze,   NOT a switch. It survives
   (on the battler)        paralysis, badly poisoned      leaving the field and the
                           plus its 4-bit counter         end of the battle
   =====================   ============================   ===========================
   status2                 confusion, Substitute,         set to ZERO by
   (on the battler)        Transformed, infatuation,      SwitchInClearSetData on
                           Focus Energy, Torment,         any switch that is not
                           Nightmare, Curse, Foresight    Baton Pass
   =====================   ============================   ===========================
   gStatuses3              Leech Seed and the battler     also zeroed on the same
   (a separate array,      receiving from it, Perish      switch -- a different
   same battler)           Song, Ingrain, Yawn, Mud       variable, same rule, and
                           Sport, Water Sport, being      the separation is why
                           Underground or Underwater      Rapid Spin can clear one
                                                          and not the other
   =====================   ============================   ===========================
   gSideStatuses and       Reflect, Light Screen,         nothing a switch does.
   gSideTimers             Spikes with its layer count,   These belong to the SIDE.
   (on the side)           Safeguard, Mist, a pending     Brick Break takes the
                           Future Sight                   screens; Rapid Spin takes
                                                          Spikes; the timers run out
   =====================   ============================   ===========================
   gBattleWeather          rain, Sandstorm, sun, hail     a timer -- UNLESS an
   (the whole field)                                      ability set it, in which
                                                          case the PERMANENT bit is
                                                          up and the countdown is
                                                          skipped entirely
   ==================================================================================
   And statStages sits alongside them, reset to DEFAULT_STAT_STAGE on a switch and
   wiped by Haze, which clears every stage and -- as m051 is precise about -- does
   not touch substituteHP by a single point.
```

That is a blistering disease. The word blister names a cavity and says nothing about which plane
the cavity is in, and the plane decides everything downstream: the appearance, the mechanical
behaviour, the healing, the biopsy site, the test and the treatment.

```
   WHERE THE SKIN CAN SPLIT, FROM THE SURFACE DOWN
   ==================================================================================

   ~~~~~~~~~~~~~~~~~~~~~~~~ stratum corneum ~~~~~~~~~~~~~~~~~~~~~~~~
   --- LEVEL 1: SUBCORNEAL ------------------------------------------
        roof is almost nothing. Staphylococcal scalded skin, where a
        toxin cleaves a desmosomal protein directly, and bullous
        impetigo
        -> ruptures instantly, often seen only as erosion with a
           collarette of scale; heals without scarring
   ==================================================================
        | keratinocytes joined by DESMOSOMES
   --- LEVEL 2: INTRAEPIDERMAL / SUPRABASAL -------------------------
        pemphigus vulgaris: autoantibody against desmosomal adhesion
        proteins, so keratinocytes come apart from EACH OTHER
        -> flaccid, ruptures easily, extensive erosion, MUCOSAL
           involvement prominent and often FIRST, heals without
           scarring because the base is still epidermis
   ==================================================================
        | BASEMENT MEMBRANE ZONE -- hemidesmosomes, lamina lucida,
        | lamina densa, anchoring fibrils
   --- LEVEL 3: SUBEPIDERMAL ----------------------------------------
        bullous pemphigoid, mucous membrane pemphigoid, dermatitis
        herpetiformis, epidermolysis bullosa acquisita, porphyria
        cutanea tarda, bullous lupus
        -> TENSE, full-thickness epidermal roof, stays intact for
           days, and healing may leave scarring and milia because
           the split is at or below the membrane that organises
           repair
   ==================================================================
   --- SEPARATELY: FULL-THICKNESS EPIDERMAL NECROSIS ----------------
        Stevens-Johnson syndrome and toxic epidermal necrolysis: the
        epidermis DIES rather than coming apart. That is m054's
        territory, it is usually drug-induced, it is an emergency,
        and no extent threshold for it appears in this answer
   ==================================================================
   Inherited epidermolysis bullosa is classified on the same axis,
   because the missing structural protein sets the level and the
   level predicts scarring and extracutaneous involvement.
```

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. **mechanism** — follows
from biology and is checkable by reasoning. (**definitional**) — a term's meaning. (**consensus**) —
standard across current textbooks and national guidance. (**country-dependent**) — differs between
countries or institutions, and yours is the authority. The Pokémon claims are not marked this way;
they are listed in the `## Sources` section with the file they were checked against.

## Three guards, three levels, one function, in a fixed order

`SetMoveEffect` is where the game decides whether a status or secondary effect actually lands, and
it reads three protections in sequence. They are not three strengths of the same thing. They are
three different levels, and each has its own exemption:

```
   THE ORDER THE CODE CHECKS, AND WHAT EACH ONE LETS PAST
   ==================================================================================

   GUARD            WHERE IT LIVES        WHAT IT BLOCKS, EXACTLY
   ==============   ===================   =========================================
   Shield Dust      an ABILITY on the     only effects that are NOT primary, and
   (Wurmple,        battler               only those low in the effect table. The
   Dustox)                                hit still lands -- what came along with
                                          it does not
   ==============   ===================   =========================================
   Safeguard        the SIDE              non-primary effects lower still in the
                    (gSideStatuses,       table -- and explicitly NOT when the
                    timer of 5)           source is an ability, which the code
                                          marks with its own hit flag
   ==============   ===================   =========================================
   Substitute       the BATTLER's         anything not aimed at the user. Costs
                    status2, with its     maximum HP divided by four to set, and
                    HP in a separate      FAILS OUTRIGHT if current HP is at or
                    field                 below that quarter -- a barrier built
                                          out of the thing it protects
   ==================================================================================
   Read the middle column. A clinician who says "they are on something for it" has
   said as little as a trainer who says "it is protected". The level is the content.
```

## Each level has its own remover, and they are not interchangeable

This is where the analogy earns the space it is taking up, because the removal asymmetry is
exactly the diagnostic asymmetry.

**Brick Break** — Fighting, power 75, accuracy 100 — runs `Cmd_removelightscreenreflect`, which
zeroes both screen flags and both timers on the opposing side. It does nothing whatever to a
Substitute, because a Substitute is not in `gSideStatuses`.

**Rapid Spin** checks being wrapped, then Leech Seed, then Spikes, and **returns after the first
one it finds** — one thing per use, in a fixed order, which is m045's point about review.

**Haze** clears every stat stage and leaves `substituteHP` untouched.

**A switch** zeroes `status2` and `gStatuses3` and resets the stat stages, and leaves `status1`
exactly as it was — and **Baton Pass** carries a hand-written whitelist of exceptions, which m070
builds a whole answer on.

**And a critical hit does not break a screen. It bypasses it.** The damage formula applies Reflect
and Light Screen only `if (gCritMultiplier == 1)`. The screen is still up afterwards. Nothing was
removed; the damage simply went through a route the screen was never in — which is the same
structural point m042 makes about first-pass extraction.

So: four removers, four levels, no overlap. Now the clinical statement that falls straight out of
it.

## Taking the immunofluorescence sample from the blister is reading the wrong variable

A suspected immunobullous disease needs more than one sample, and the sites are different because
the questions are different:

```
   ONE SUSPECTED DIAGNOSIS, FOUR SAMPLES, FOUR SITES
   ==================================================================================

   SAMPLE                     SITE                        WHAT IT ANSWERS
   ========================   =========================   ===========================
   histology                  edge of a FRESH blister,    at what level is the split,
                              including intact roof       and what cells are present
   ========================   =========================   ===========================
   direct                     PERILESIONAL skin that      is there bound antibody or
   immunofluorescence         looks normal -- NOT the     complement, where, and in
                              blister                     what pattern
   ========================   =========================   ===========================
   serum                      a vein                      what is the circulating
                                                          antibody directed against
   ========================   =========================   ===========================
   salt-split skin, where     the laboratory, on serum    is the target above or
   it is used                                             below the lamina densa --
                                                          the level question again,
                                                          asked of the laboratory
   ==================================================================================
```

The immunofluorescence sample comes from normal-appearing skin **beside** the blister, because the
test detects immunoreactants bound in tissue and the inflammatory environment inside a blister
cavity degrades exactly what is being looked for. A sample from the roof or the base can come back
negative while the disease is unambiguously present. (**mechanism** **consensus**)

Which is `gBattleMons[gActiveBattler].status2` returning zero while `gSideStatuses[side]` has
`SIDE_STATUS_SAFEGUARD` set. **The read succeeded. The variable was wrong. And a confident zero
from the wrong structure is worse than no result**, because it reads as an answer and the repeat
costs weeks. The handling also differs — fresh or in a specific transport medium rather than
formalin — and the laboratory where you practise specifies which, which is (**country-dependent**).

## Nikolsky's sign is a side status, not a battler status

**Spikes** are laid on a side of the field. The cost you observe at one switch-in is not the
extent of the hazard; the hazard covers everything that enters on that side, and it stacks to
three layers in the third generation — three, a generation-three change.

Lateral shearing pressure on apparently normal skin produces separation when adhesion has been
lost **across an area** rather than only where a blister is visible. A positive Nikolsky sign
points to an intraepidermal, adhesion-molecule-mediated process, and the blister you can see is
simply where separation has already happened. (**mechanism**) The eliciting technique and the named
variants differ between texts and the sign is not specific on its own.

## Wonder Guard, and the splits that engage none of the machinery

**Shedinja**'s **Wonder Guard** sits at the type-effectiveness level — above the damage formula,
above the screens, above everything in the table two sections up. It is used here strictly for
that type-override point, as m047 uses it, and for nothing else.

The clinical equivalent is the group of causes that produce a blister without engaging any
adhesion mechanism at all: friction, burns, cold injury, oedema blisters on a swollen leg, an
exaggerated insect bite reaction, bullous cellulitis, bullous diabeticorum, pressure blisters. No
autoantibody, no toxin, no missing protein — and no immunofluorescence panel required. They are
also the commonest blisters there are, which is why the mechanical mimics come before the
immunobullous workup rather than after it.

Three other mechanisms complete the set. A **toxin** cleaving a desmosomal protein directly, which
is staphylococcal scalded skin and is an infectious paediatric emergency rather than an
immunobullous disease. A **missing structural protein**, which is inherited epidermolysis bullosa.
And a **metabolic** cause: porphyria cutanea tarda, subepidermal blistering with fragility on
sun-exposed skin, hypertrichosis and scarring, associated with liver disease, alcohol, iron
overload, oestrogens and hepatitis C — the associations being why the diagnosis matters beyond the
skin.

## Barrier loss over an area is the Substitute cost, scaled up

**Substitute** costs maximum HP divided by four and fails if current HP is at or below that
quarter. m051 builds the eczema barrier argument on exactly that: a barrier made out of the
substance it protects, with a failure condition when there is not enough substance left.

Extensive blistering is that argument at a larger scale. Fluid and protein loss, impaired
thermoregulation, pain, and an eroded surface that is readily colonised and secondarily infected.
Extensive disease therefore needs what looks like burns care — fluid balance, temperature,
analgesia, nutrition, meticulous handling and an environment that reduces shear — alongside
whatever is treating the cause. Mucosal involvement adds a mouth too sore to eat, eyes at risk of
scarring, and genital and oesophageal disease that is missed because nobody looked.

Treatment of the immunobullous diseases is immunosuppression, with topical therapy playing a
larger role in localised pemphigoid than people expect, and with rituximab having changed
first-line practice in pemphigus in several countries over the last decade. Which agents, in what
order, at what threshold and with what funding is firmly (**country-dependent**), and no agent, dose
or regimen appears here.

## Where the metaphor stops

No Pokémon in this section. Three things need saying without ornament.

**The emergencies.** Widespread blistering with mucosal involvement, especially beginning within
weeks of a new medicine, with fever or feeling unwell, needs the same response as a burn of
similar extent — immediate senior assessment and usually a specialist unit, by whatever acute
route exists where you work. Blistering with extensive skin detachment, with eye involvement, or
with an inability to drink, is a medical emergency. A young child with widespread superficial
blistering and fever is a paediatric emergency. Suspected drug-induced blistering is m054's
territory and its thresholds are deliberately low.

**The ordinary course.** These are chronic diseases, mostly in older people, treated with
immunosuppression that carries its own risks, and the burden is substantial: raw skin, disturbed
sleep, dressings, hospital visits, and treatment side effects competing with disease effects.
People with inherited epidermolysis bullosa live with this from birth and the daily dressing
routines are measured in hours; they are looked after by specialist services, and the expertise
sits there rather than in a revision answer.

**And the part that is easy to get wrong in conversation.** Extensive erosion is frightening to
look at and frightening to have, and nothing in this answer should be used to estimate what will
happen to any particular person. That is not something a mechanism answer can do, and the
specialist team with the actual findings is the only place that question belongs.

Without softening: nothing here is for any reader's own use, and no treatment named here is a
recommendation. Anyone with unexplained blistering, blistering involving the mouth or eyes,
blistering after a new medicine, or blistering with fever or feeling unwell needs to be assessed
in person and urgently. Extensive blistering or skin detachment is an emergency — call your local
emergency number.

## What a Gym Leader is listening for

Why a tense blister implies a deeper split than a flaccid one. Why one heals with scarring and the
other does not. What Nikolsky's sign actually demonstrates, and what it does not. Which two
biopsies you take, from where, and what happens when the immunofluorescence sample comes from the
blister — the wrong variable, read perfectly. What salt-split skin is asking. Which group of
diseases involves the mouth first, and why that follows from the target molecule. Why
staphylococcal scalded skin is not an immunobullous disease despite splitting the epidermis. How
inherited epidermolysis bullosa is classified, and why the classification predicts scarring. And
the mechanical mimics, because most blisters are not autoimmune.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For the immunobullous diseases — diagnostic criteria, antibody targets, the role of each assay
  and the treatment ladders: the specialist guidance of your national dermatology body, and a
  current standard textbook of dermatology for the anatomy and the classification.
* For biopsy technique, sample site, transport medium and what each laboratory accepts: the user
  handbook of the immunodermatology laboratory your service sends to. It is the authority on
  handling and it differs between laboratories.
* For the definitions, categories and extent thresholds of the severe drug-induced reactions: your
  national guidance and the specialist unit's protocol. No threshold for them appears in this
  answer on purpose.
* For immunosuppressive agents, including rituximab — licensed indications, funding, monitoring
  and infection prophylaxis: your national formulary and your national or regional funding policy.
* For inherited epidermolysis bullosa: your national specialist service for it, which is where the
  expertise and the dressing protocols live.
* For porphyria cutanea tarda, its investigation and its associations: your national porphyria
  service or specialist laboratory.

The Pokémon claims were checked separately against source. The five storage structures and their
contents — `status1` holding sleep, poison, burn, freeze, paralysis and badly poisoned with a
four-bit counter; `status2` holding confusion, Substitute, Transformed, infatuation, Focus Energy,
Torment, Nightmare, Curse and Foresight; `gStatuses3` holding Leech Seed and its receiving
battler, Perish Song, Ingrain, Yawn, Mud Sport, Water Sport and the semi-invulnerable states; the
side statuses holding Reflect, Light Screen, Spikes with its layer count, Safeguard, Mist and a
pending Future Sight; and the weather being field-wide with a permanent bit that skips the
countdown when an ability set it — are all from the pret decompilation of Pokémon Emerald, as is
`SwitchInClearSetData` zeroing `status2` and `gStatuses3` and resetting the stat stages to
`DEFAULT_STAT_STAGE` while leaving `status1` alone, and Baton Pass's explicit whitelist. So are
the three guards in `SetMoveEffect` and their exact conditions; Substitute costing maximum HP
divided by four and failing when current HP is at or below that quarter; Reflect and Light Screen
having timers of 5 and applying only when `gCritMultiplier == 1`; Brick Break having power 75 and
accuracy 100 and zeroing both screens on the opposing side; Rapid Spin checking wrapped, then
Leech Seed, then Spikes and returning after the first; Haze clearing stat stages without touching
`substituteHP`; Spikes stacking to three layers in the third generation; and Shedinja's Wonder
Guard. Nothing in this answer rests on a mechanic from a later generation.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No agent, dose, regimen, extent threshold or scoring system appears in this answer, and none of
it addresses any reader's own treatment.** The omission of the detachment thresholds in the severe
drug reactions is deliberate: those categories are defined in the documents named above, and
quoting a figure here without the document would be worse than leaving it out.

Anyone with unexplained blistering, with blistering involving the mouth, eyes or genitals, with
blistering that began after a new medicine, or with blistering accompanied by fever or feeling
unwell, needs to be assessed in person and urgently. Extensive blistering or skin detachment is a
medical emergency — call your local emergency number.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The anatomy and the level-determines-everything argument are settled and are the part worth
memorising; the biopsy site rule for immunofluorescence is settled and still routinely got wrong.
What moves is treatment and some of the classification. Rituximab changed first-line treatment of
pemphigus in several countries within the last decade, and whether it is first-line, funded and
available where you practise is (**country-dependent**). The pemphigoid group has been subdivided
further as antigen-specific assays have become more widely available, and the nomenclature of
mucous membrane pemphigoid and its variants has moved. An association between pemphigoid and
dipeptidyl peptidase-4 inhibitors has been recognised and reported widely enough to change
prescribing review in some services, and the strength of it is still being characterised.
Inherited epidermolysis bullosa has seen the first gene- and cell-based therapies reach licensing
in some jurisdictions, which is the fastest-moving part of this territory. The five storage
structures are stable across the whole third generation, which is the only reason this analogy can
be stated to the variable name. Current as of October 2026.
