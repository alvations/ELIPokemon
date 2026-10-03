---
id: "m124"
slug: haematological-against-solid-tumours
style: pokemon
category: oncology
difficulty: advanced
question: "Why do the staging and response vocabularies of solid tumour oncology not transfer to the haematological malignancies, and what replaces them?"
tags: [haematological-malignancy, staging, remission, residual-disease, classification]
---

# Spikes is the only move in Emerald aimed at a side, and the usual result questions do not fit it

Every move carries a field saying what it is aimed at, and that field decides which questions
about the result can even be asked. Sort all three hundred and fifty-five of them and the classes
come out very unevenly:

```
   247  a chosen target        Body Slam, Cross Chop, Shadow Ball, Thunder, Hydro Pump ...
    67  the user or its side   Reflect, Light Screen, Mist, Safeguard, Swords Dance ...
    22  both opponents         Surf, Blizzard, Rock Slide, Razor Leaf, Heat Wave,
                               Hyper Voice, Icy Wind, Twister, Water Spout, Eruption ...
     9  depends on the turn    Counter, Mirror Coat, Metronome, Mirror Move, Sleep Talk,
                               Nature Power, Assist, Magic Coat, Snatch
     5  everything adjacent    Earthquake, Magnitude, Explosion, Self-Destruct, Teeter Dance
     4  a random opponent      Thrash, Petal Dance, Outrage, Uproar
     1  the opposing SIDE      Spikes — and nothing else in the entire game
```

For any of the two hundred and forty-seven, the whole result vocabulary works. **Cross Chop** into
a **Blissey**: *how much damage*, *was it super effective*, *did it miss at eighty accuracy*, *is
the bar lower than it was*. There is a located object, it has an HP value, and every one of those
questions has a well-formed answer. **Shuckle** has a terrible one and **Wailord** an enormous
one, and the questions are the same questions about both.

For the one, almost none of them does. Spikes has **no base power and no accuracy figure at all**
— both fields are zero. It has no damage, so *how much* has no referent; it cannot miss, so *did
it miss* has no referent; there is no HP bar belonging to a side, so *is it lower* has no
referent. What it leaves behind is a flag on the side plus a count of layers, and the questions
you would ask of a chosen target are not wrong about it — **they are undefined on it.**

That is this answer. A solid tumour oncologist and a haematologist use words that sound like each
other — *stage*, *response*, *complete*, *residual* — and each word is defined by an instrument
applied to a kind of object. Carry a word across and you have not made an error of fact. You have
asked a question with no referent, which is harder to notice.

Spikes has done two jobs in this corpus already: the nursing answer on hand hygiene uses it as a
hazard belonging to the environment and set by someone who has left, and the emergency answer on a
presentation that looks social uses its absent screen indicator. **Neither of those is the device
here.** This answer is about its `.target` field and its storage, and nothing about who laid it.

As elsewhere in this specialty, **the objects of study are data fields, target classes and
stores.** No Pokémon in this answer stands in for a person, and the analogy is dropped entirely at
the end.

Clinical claims carry the same marks as the rigorous half: (**mechanism**), (**definitional**),
(**consensus**), (**country-dependent**).

## Two target classes, drawn

```
   MOVE_TARGET_SELECTED  (247 of 355)        MOVE_TARGET_OPPONENTS_FIELD  (1 of 355)

   ┌──────────────────────────┐              ╔══════════════════════════════════╗
   │  a battler               │              ║  a SIDE                          ║
   │   • hp, maxHP            │              ║   • no hp                        ║
   │   • an HP bar on screen  │              ║   • no bar                       ║
   │   • types, stats, stages │              ║   • gSideStatuses bit             ║
   │   • status1 and status2  │              ║   • gSideTimers[].spikesAmount    ║
   └──────────────────────────┘              ╚══════════════════════════════════╝

   QUESTIONS WITH A REFERENT:                QUESTIONS WITH A REFERENT:

     how much damage?            ✓             how much damage?            ✗ power 0
     was it super effective?     ✓             was it effective?           ✗ no typecalc
     did it miss?                ✓             did it miss?                ✗ accuracy 0
     is the bar lower?           ✓             is the bar lower?           ✗ no bar
                                               how many layers?            ✓ spikesAmount
                                               is it present at all?       ✓ the bit

   ───────────────────────────────────────────────────────────────────────────

   AND THE STORE IS THE WRONG SHAPE FOR THE OTHER ENTRIES

   struct SideTimer {
       u8 reflectTimer;      u8 reflectBattlerId;        ─┐
       u8 lightscreenTimer;  u8 lightscreenBattlerId;     │  five pairs:
       u8 mistTimer;         u8 mistBattlerId;            │  A CLOCK and
       u8 safeguardTimer;    u8 safeguardBattlerId;       │  WHO SET IT
       u8 followmeTimer;     u8 followmeTarget;          ─┘
       u8 spikesAmount;                                  ── alone.  A COUNT.
   };                                                       No timer.  No id.

      One entry in the structure is measured by a different KIND of
      quantity from every other entry, and the fields the others carry
      do not exist for it.
```

## The anatomical scheme needs a located object, and what that means

Worth doing properly, because "they just use different systems" fails under questioning.

The anatomical staging scheme is a **communication protocol over an extent** (**definitional**).
It works because extent is a real, ordered, partly observable quantity for a tumour that started
in one place. This specialty's answer on staging against grading sets out what the three
categories encode and why they are recorded separately rather than summed, and the notation's
details — the prefix recording which measurement it was, the edition recording which version of
the stage groups applies — are all doing that one job.

Three things have to be true for the scheme to mean anything (**mechanism**):

* a **site of origin** with a boundary, so extent is measurable at all;
* a **downstream nodal field**, so regional involvement is a distinguishable state;
* a **distinction between local and distant**, so the third category is a different biological
  statement from the second.

For a leukaemia all three fail at once, and for mechanistic rather than notational reasons. The
marrow is one organ distributed through the whole skeleton, so there is no *here*. The abnormal
cells are in the circulation as a consequence of what they are rather than as a step in a cascade,
so *distant spread* is not an event that may or may not have happened. And an organ that every
vessel passes through has no regional nodal field.

That is `.power = 0` in a data entry. It is not a weak move. The field that carries the magnitude
holds zero because magnitude is not the kind of thing this entry has, and this specialty's answer
on the oncological emergencies makes the companion point about `.power = 1` as a placeholder in a
different family.

For a lymphoma the failure is partial, which is why lymphoma classification looks closer to
anatomical staging than leukaemia classification does: there are discrete involved sites, they can
be imaged and measured, and their number and distribution carry information. What does not
transfer is the **ordering** — a lymphoma at multiple distant sites is not in the same clinical
position as a carcinoma at multiple distant sites, and treating the anatomical category as if it
carried the same implication is the characteristic error (**mechanism**, **consensus**).

And the cartridge has a class for exactly that in-between position: the nine moves whose target
*depends on the turn*. **Counter** and **Mirror Coat** both carry the placeholder base power of
one — the same placeholder this specialty's answer on the oncological emergencies finds across
Sonic Boom, Dragon Rage, Seismic Toss and Night Shade — and neither of them has a target until the
turn has resolved, because each returns to whoever hit the user and with which kind of attack.
**Metronome**, **Mirror Move**, **Sleep Talk** and **Assist** do not even know which *move* they
are until they run, and **Magic Coat** and **Snatch** acquire an object only if somebody supplies
one. Nine entries in the whole game where the question *what was this aimed at* has no answer
before the fact.

That is the lymphomas. Which vocabulary applies — the chosen-lesion one or the compartment one —
is not settled by a general rule but by the disease and the presentation in front of you. A nodal
mass is measurable the way a carcinoma deposit is measurable; marrow involvement in the same
person is not. Both apply, and which one carries the decision depends on what is actually there
(**mechanism**, **consensus**).

## `spikesAmount`: a count where every other entry keeps a clock

Read `struct SideTimer` again. Five of its entries are **pairs**: a timer and the identifier of
the battler who set the effect. Reflect, Light Screen, Mist, Safeguard, Follow Me. Then one entry
on its own, `spikesAmount`, with no timer and no identifier beside it.

So the one effect that belongs to a field rather than a battler is also the one measured by a
**count** rather than by a **clock**, and the one for which the fields its neighbours carry simply
do not exist. The store is the wrong shape for it, and somebody solved that by giving it a
different kind of field rather than by forcing it into the pattern.

Each haematological family did exactly that: built its classification from whichever variable
actually carries information, and the choice of variable is the biology (**mechanism**).

**Lymphomas** use a distribution scheme — the number and grouping of involved regions and their
relation to the diaphragm, with extranodal involvement recorded separately. The historical
framework is the Ann Arbor scheme and the version in current use is a modification of it; the
modifications, and the role of metabolic imaging within them, have changed and continue to
(**definitional**, **consensus**, (**country-dependent**)). Prognostic indices built from clinical
and laboratory variables sit alongside the stage and often carry more weight than it does — which
is a structural statement about how much information a distribution contains.

**The myelomas** are classified by markers of disease burden and of biology rather than by
anatomical extent, in frameworks maintained by an international working group and revised as the
evidence changes (**definitional**, **consensus**). The disease has a quantitative marker in blood
or urine, which is unusual and consequential: this specialty's answer on tumour markers sets out
what such a molecule can and cannot do, and myeloma is one of the places where it does a great
deal. That is `spikesAmount` — a quantity in its own units, for an object with no bar.

**The chronic lymphocytic leukaemias** use frameworks built from blood counts, nodal and organ
involvement, and marrow failure. Two long-standing schemes are in use and they are not identical,
which is itself the point: a classification is a protocol, and two protocols over one disease can
both be valid (**definitional**).

**The acute leukaemias are not staged at all**, and this is the sharpest fact in the topic. There
is nothing for a stage to order. What replaces it is classification by lineage, morphology,
immunophenotype, cytogenetics and molecular genetics, feeding a **risk stratification** — a
different kind of object from a stage, grouping by expected behaviour and by what treatment is
indicated, built from the biology of the clone rather than from where it has reached
(**definitional**, **consensus**). Somebody who asks for the stage of an acute leukaemia has asked
a question with no referent, and the honest answer is to say so rather than supply an
approximation. That is the whole of the `.target` argument in one clinical sentence.

## Two words, two instruments, and what bounds each from below

The response vocabulary diverges further than the staging vocabulary does, and almost entirely
because of what each instrument can reach.

**Solid tumour response is a change in the size of named lesions on an imaging test.** This
specialty's answer on response assessment and surrogates sets out the structured criteria, what
they buy, and where information is lost at each link. The feature that matters here is the floor:
complete response means *no visible lesion on an imaging test*, and an imaging test has a
resolution limit. The category is defined by the instrument's blind spot (**definitional**,
**mechanism**).

**Haematological remission is a state of a sampled compartment.** Complete remission in an acute
leukaemia is defined on a marrow sample — a proportion of blasts below a specified level, with
recovery of peripheral counts and absence of disease outside the marrow (**definitional**, with
the exact criteria set by the current classification and therefore (**country-dependent**) in
which version is in force). That is a different kind of statement. Not *nothing can be seen*, but
*this sample meets this specification*.

Three consequences, all mechanical.

**The words denote different depths of evidence.** "Complete" means below the resolution of an
imaging test applied to a lesion in one case, and within a specification applied to a sample in
the other. Those are not comparable amounts of residual disease in either direction, and treating
them as one word is how a reader acquires a false equivalence (**mechanism**).

**The sampling properties are opposite.** This specialty's answer on tumour heterogeneity and the
single biopsy sets out why one piece of one solid lesion is a sample of a population under
selection and is not representative. A marrow aspirate samples a compartment whose contents
circulate and mix, which makes it *more* representative of its whole than a solid tumour biopsy is
of its lesion — not perfectly, since marrow disease can be patchy and a trephine adds
architectural information an aspirate cannot, but the direction of the difference is the point
(**mechanism**, **consensus**).

**The schedules differ in kind.** A solid tumour is measured when it is imaged, and this
specialty's answer on response assessment makes the point that a measurement made on a schedule
inherits the schedule. A blood count is available whenever blood is taken, so for several
haematological diseases the burden is trackable nearly continuously. That changes what the word
*progression* can mean (**mechanism**). The cartridge has the same split: a battler's HP is
readable every frame, and `spikesAmount` changes only when something sets or clears it.

## The store the cartridge does not have

This is the section where naming the gap is better than building a device for it.

**Measurable or minimal residual disease** is disease detected below the level at which morphology
can see it, by applying a more sensitive instrument — multiparameter flow cytometry, or a
molecular assay for a disease-specific target — to the same sample. It is reported against a
stated sensitivity, because a negative result means *not detected at this sensitivity* and nothing
stronger (**definitional**, **mechanism**). In several diseases it directs treatment: whether to
intensify, whether to proceed to transplantation, whether to stop (**consensus**, strongly
(**country-dependent**) in which assay, which threshold, which decision).

It is a **depth axis**, not a better response assessment: complete remission and residual-disease
status are two readings of one sample by two instruments with different floors, and the coarser
one is not wrong but bounded.

**Emerald has no store of that shape.** `spikesAmount` is an unsigned byte. It holds zero, one,
two or three — `Cmd_trysetspikes` refuses at three rather than refreshing, which is the
fails-rather-than-refreshes shape the emergency answer on immobilisation and the dermatology
answer on urticaria both document in `Cmd_setsafeguard`, and it is theirs. What there is no room
for is **a value below the resolution of the coarse reading**. When the count is zero the bit
clears and there is nothing left to interrogate; there is no second, finer instrument that could
return a non-zero where the first returned zero.

The nearest shape in the cartridge is the opposite problem, and it belongs to other answers: the
HP bar's forced minimum of one pixel, which this specialty's answer on tumour markers sets beside
Super Fang's floor and `Cmd_scaledamagebyhealthratio`'s as three separate routines refusing to
report zero. That is a coarse instrument that **cannot** say zero. Residual-disease assessment is
a fine instrument that **can** say non-zero where the coarse one said zero. They are not the same
asymmetry, and pretending the bar covers it would teach a false equivalence.

And the clinical reason solid tumour oncology has no such axis is structural rather than
technological: residual-disease assessment needs a compartment you can sample representatively and
an assay with a floor below the coarse instrument's. For a solid tumour the compartment is the
body. There is no sample that stands for the whole of it, which is why a complete response on
imaging cannot be refined by a more sensitive look at the same specimen — there is no specimen
(**mechanism**).

## Where the two vocabularies are converging

Three places, all live rather than resolved.

**Circulating tumour DNA as a residual-disease instrument for solid tumours.** Assays detecting
disease-derived DNA in blood after curative-intent treatment are an attempt to build the depth
axis solid tumour oncology has never had, using the circulation as the samplable compartment.
Whether acting on such a result improves outcomes is under investigation and the place of these
assays is not settled (**consensus**, **country-dependent**). If it settles, it would import a
haematological vocabulary into solid tumour oncology wholesale — and it would also give adjuvant
treatment the per-patient readout that this specialty's answer on treatment intent shows it has
never had.

**Metabolic imaging in the lymphomas**, which brought an imaging-based response vocabulary into a
disease classified by distribution, and interim response assessment with it (**consensus**,
(**country-dependent**)).

**Molecular classification generally**, where the traffic has mostly run from haematology outward:
the acute leukaemias were doing genomically-defined classification long before solid tumour
oncology was, and this specialty's answer on biomarker-driven treatment selection describes where
it has arrived (**consensus**).

What is not converging is the staging vocabulary. A disease of a distributed compartment will not
acquire a primary site, and the anatomical scheme will not acquire a way to describe one. One move
in three hundred and fifty-five has that target class, and no amount of work on the other three
hundred and fifty-four changes what questions fit it.

## Where the metaphor stops

Everything above is data fields, target classes and storage shapes, and the cartridge is a good
place to see them because the field that decides which questions fit is one line of a struct. What
follows is about people, so the analogy stops and nothing below leans on it.

The words themselves do work in people's lives, and two of them do more harm than any
classification system. **Remission** is heard by almost everybody as a synonym for *cured*, and it
is not one — it is a statement about a sample meeting a specification. The gap between what the
word means to the person using it and what it means to the person hearing it is one of the widest
in medicine, and closing it is a matter of saying what was measured rather than of finding a
softer word. **Residual disease not detected** is heard as *gone*, and it means *not detected at
this sensitivity*. People are entitled to that qualifier and generally cope with it better than
clinicians expect.

The other human fact here is that the two specialties feel different to be treated in.
Haematological treatment is frequently intensive, inpatient, prolonged and count-dependent: long
periods of being unwell in hospital away from home, isolation precautions, and a rhythm of blood
tests that organises the whole of life. Solid tumour treatment is more often cyclical and
outpatient. Neither is harder in general and the comparison is not useful to anybody going through
either; what is useful is that the shape of the burden differs, so somebody moving between the two
— or supporting somebody in one while having experience of the other — is not comparing like with
like.

Nothing in either half of this answer says anything about what will happen to any individual, and
no clinical figure of any kind appears in either half. Both omissions are deliberate. And nothing
in the game stands in for a person: the subject throughout has been which questions a stored
quantity can answer.

## What a Gym Leader is listening for

* Exactly one move in the game carries `MOVE_TARGET_OPPONENTS_FIELD`. What does its loneliness
  demonstrate about a vocabulary built for a different target class?
* Spikes has `.power = 0` and `.accuracy = 0`. Which clinical questions are those two zeros?
* Name the three things an anatomical staging scheme needs, and say which fails for a leukaemia.
* Why does the scheme fail only partially for a lymphoma, and what specifically does not transfer?
* What is the stage of an acute myeloid leukaemia? Justify the answer.
* `spikesAmount` has no timer and no `battlerId` where five neighbours have both. What is the
  clinical version of a quantity in its own units?
* What bounds complete response from below, and what bounds complete remission from below? They
  are not the same kind of bound.
* Where does the cartridge have no store of the right shape, and why is the HP bar's forced one
  pixel *not* the same asymmetry?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific to
this answer:

* The current edition of the World Health Organization classification of haematolymphoid tumours,
  which is the definitional source for how these diseases are named and grouped. The edition
  matters and the groupings move between editions.
* The current response criteria for the specific disease in question, from the international
  working group that maintains them. There is a separate set for the acute leukaemias, for the
  lymphomas, for the myelomas and for the chronic lymphocytic leukaemias, each defining its own
  categories, and each is the only place its criteria should be read.
* The current anatomical staging classification used where you work, for the contrast — and
  because it says itself which diseases it does not apply to.
* The published guidance on residual-disease assessment for the disease concerned, from the body
  that issues it in your region, for which assay, at what sensitivity, at which timepoints, and
  what each result triggers. All four differ between diseases and between countries.
* A current standard textbook of haematology, for the lymphoma distribution scheme and its current
  modifications, for the myeloma and chronic lymphocytic leukaemia frameworks, and for the
  prognostic indices that sit alongside them.
* The primary literature, for the evidence linking residual-disease status to outcome in each
  disease, and for the trials of acting on circulating tumour DNA after treatment of a solid
  tumour.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about classification and response vocabulary, dressed in a game so that
the field deciding which questions fit stays visible. It has had no clinical review. **No
classification category, blast proportion, count threshold, assay sensitivity or response
criterion appears here, and none should be inferred** — those belong to the working group that
maintains each set of criteria, they differ between diseases and between the versions in force in
different countries, and they are revised; the classification and criteria in force where you work
are the authority and this is not. It is not a staging manual, not a reporting standard and not a
decision aid, it says nothing about what will happen to any individual, and it describes no
individual's situation. Anyone affected by cancer or by a blood disorder — their own diagnosis or
someone else's — should be talking to the clinical team looking after that person, who have the
samples and the results, neither of which is here. The analogy carries data fields and storage
shapes only: no part of it stands in for a person, and no creature's situation is the subject of
any sentence in it.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source and nothing here is claimed about any
generation but the third. Counting `.target` across `src/data/battle_moves.h` gives two hundred
and forty-seven `MOVE_TARGET_SELECTED`, sixty-seven `MOVE_TARGET_USER`, twenty-two
`MOVE_TARGET_BOTH`, nine `MOVE_TARGET_DEPENDS`, five `MOVE_TARGET_FOES_AND_ALLY`, four
`MOVE_TARGET_RANDOM` and one `MOVE_TARGET_OPPONENTS_FIELD`, which is Spikes; the eight constants
are defined in `include/battle.h`, where `MOVE_TARGET_SELECTED` is zero and the rest are single
bits. Spikes' entry is `.effect = EFFECT_SPIKES`, `.power = 0`, `.type = TYPE_GROUND`, `.accuracy
= 0`, `.pp = 20`, `.target = MOVE_TARGET_OPPONENTS_FIELD`; Reflect's is `.power = 0`, `.accuracy =
0`, `.target = MOVE_TARGET_USER`. `struct SideTimer` in `include/battle.h` holds
`reflectTimer`/`reflectBattlerId`, `lightscreenTimer`/`lightscreenBattlerId`,
`mistTimer`/`mistBattlerId`, `safeguardTimer`/`safeguardBattlerId`,
`followmeTimer`/`followmeTarget`, and then `spikesAmount` with no partner field.
`Cmd_trysetspikes` in `src/battle_script_commands.c` jumps to its failure branch when
`gSideTimers[targetSide].spikesAmount == 3` and otherwise sets `SIDE_STATUS_SPIKES` in
`gSideStatuses[targetSide]` and increments the count; `include/constants/battle.h` gives
`SIDE_STATUS_SPIKES` as bit four and `SIDE_STATUS_SPIKES_DAMAGED` as bit nine, a separate bit
recording that the hazard has acted. Three-layer Spikes is a third-generation feature and the
second generation has one layer. Spikes' other two uses in this corpus are named in the opening
note and the device here is neither of them.

The clinical reasoning will not date in its structural half: an anatomical scheme needs a located
primary, a distributed compartment does not have one, a sample that stands for its compartment
permits a depth axis and one that does not cannot, and a word is defined by the instrument that
reports it. Everything built on top is being revised, some of it quickly. The classification of
haematolymphoid tumours is in active revision, the groupings have moved between recent editions,
and more than one competing current framework is in circulation — itself a good illustration of a
classification being a protocol rather than a description. The response criteria for each family
are periodically updated. Residual-disease assessment is the fastest-moving part: which assay, at
what sensitivity, at which timepoint and what the result triggers are all under revision and
differ sharply between countries. And the attempt to build an equivalent axis for solid tumours
from circulating tumour DNA is the thing most likely to make this answer's central asymmetry look
dated, which is worth saying rather than leaving for a reader to find. No category, threshold or
criterion is quoted here, deliberately.
