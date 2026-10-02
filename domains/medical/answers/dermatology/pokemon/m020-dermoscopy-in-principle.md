---
id: "m020"
slug: dermoscopy-in-principle
style: pokemon
category: dermatology
difficulty: intermediate
question: "What does dermoscopy add over the naked eye, and why is it pattern recognition over a structured vocabulary rather than magnification?"
tags: [dermoscopy, optics, vocabulary, pattern-recognition, training]
---

# A Nature is a word for something no amount of staring at the sprite will show you

Every Pokémon carries a Nature, taken from its personality value by the simplest arithmetic the
games contain: the personality value modulo twenty-five. There are twenty-five of them, they are a
closed named set, and each one raises one stat by a tenth and lowers another by a tenth. Adamant
is Attack up and Special Attack down. Timid is Attack down and Speed up. Bold is Attack down and
Defense up. Relaxed is Defense up and Speed down. Five of the twenty-five — Hardy, Docile,
Serious, Bashful and Quirky — do nothing at all.

None of that is visible. It is doing work in every single **battle**, it is the difference between
winning and losing a **Speed Tier**, and you will never find it by looking harder at the picture.
That is the situation a dermatoscope is built for.

A dermatoscope magnifies, usually about tenfold, and the magnification is the least interesting
thing about it. Two other properties account for almost all its value: it **removes the light
scattered back off the surface of the skin**, which was what limited the view in the first place,
and it delivers what is underneath through a **structured vocabulary of named structures**, which
makes a finding shareable and arguable instead of an impression. A hand lens has the magnification
and neither of the other two, which is why a hand lens is not a dermatoscope.

## The optics, because this is the part most often got wrong

**Smokescreen** has a base power of zero. It does not reduce anything's health, and it decides
battles, because what it lowers is accuracy. **Sand Attack** is the same idea; **Bright Powder**
does it from the other side of the field. A trainer facing that does not solve it by switching to
a move with higher base power — **Focus Blast** and **Zap Cannon** and **Dynamic Punch** are the
three hardest-hitting moves in the game to actually land, and turning the power up while the aim
is degraded is **Hustle**, which is a known trade and not a fix.

```
   WHY IT IS NOT A MAGNIFYING GLASS
   ==================================================================================

   NAKED EYE, OR A HAND LENS              DERMATOSCOPE
   =========================              ============
        incident light                         incident light
              \   most of it reflects                \   immersion fluid matches the
               \  straight back off the               \  refractive index, or a
                \ dry keratin surface                  \ crossed polariser rejects
                 v                                      v the surface reflection
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   # stratum corneum             #       # stratum corneum             #
   ===============================       ===============================
   | epidermis                   |       | epidermis                   |
   | pigment network, nests      |  -->  | pigment network, nests      | --> visible,
   ===============================       ===============================     and nameable
   | papillary dermis            |       | papillary dermis            |
   | vessels, collagen           |       | vessels, collagen           |
   ===============================       ===============================
                you see a blur                    you see structures
   ==================================================================================
   More power into a Smokescreen is still a miss. Haze does not out-damage a
   stat change, it erases it; Machamp's No Guard does not improve accuracy, it
   removes accuracy from the calculation entirely, in both directions.
   The obstruction was the problem. Delete the obstruction.
```

**Machamp** is the clean illustration. From the fourth generation onward it can have **No Guard**,
and No Guard does not make Machamp more accurate — it makes every move hit, whether Machamp is
attacking or being attacked, which is why **Dynamic Punch** on a Machamp is a different move from
Dynamic Punch anywhere else. **Haze** works the same way on stat stages: it does not overpower
them, it wipes them. The dermatoscope is in that family of solutions. It does not out-resolve the
glare, it removes the glare, with immersion fluid matching the refractive index at the surface or
with crossed polarisers rejecting the reflected light.

Those two methods are **not interchangeable**. Some structures show better with contact immersion,
and certain bright white structures appear only under polarisation. A practitioner who only ever
uses one mode has a systematic blind spot, exactly as a team built only around **Compound Eyes**
accuracy has a different blind spot from one built around **No Guard**, and knowing which mode
produced an image is part of reading it.

## The vocabulary, which is the second thing it adds

It is a two-level system and conflating the levels is the commonest conceptual error.

**Level one: name the structures.** The pigment network and whether it is regular or atypical,
dots, globules, streaks and radial lines, structureless areas, blue-white structures, regression
features, and vessel morphology — dotted, comma, hairpin, arborising, glomerular.

**Level two: recognise the pattern they make.** Not that a globule is present, but the arrangement
and symmetry of globules across the whole lesion.

The split matters because a word is worthless without its table. Adamant means nothing to a
trainer who has not learned which stats it moves, and an Adamant Pokémon that only knows special
attacking moves is a correctly-named structure attached to a wrong conclusion — which is precisely
the trainee who can name every dermoscopic feature and still cannot read the lesion. The **Type
Chart** is the same object: the vocabulary of **Super Effective** and **Not Very Effective** is
only informative to somebody holding the lookup.

And a vocabulary has a **domain** it does not extend past. A Nature never touches **HP**, and
never touches accuracy or evasion — the code refuses those three outright, so no Nature is ever an
answer to a question about them. The dermoscopic lexicon is site-specific in the same hard way:
facial skin, acral skin, the nail apparatus and mucosal surfaces have genuinely different
vocabularies, not the trunk vocabulary carried over. On palms and soles the decisive observation
is whether pigment follows the furrows or the ridges of the skin markings, which has no
counterpart on a back.

Several published structured algorithms exist for turning these observations into a decision, and
which one is taught differs by centre and by country. None is reproduced here, deliberately: a
criteria set recalled from memory and written down without its source is worse than none, and the
one to learn is the one your service uses.

## Training, stated plainly

Dermoscopy improves diagnostic accuracy for melanoma **in trained hands**, and used without
training it may do no better than the naked eye. The mechanism is not mysterious: the instrument
adds information, and information you cannot interpret moves a decision without improving it. A
**Bottle Cap** and **Hyper Training** can max an **Individual Value** that was never visible, and
neither is any use to a trainer who does not know what IVs do. The device is the easy part.

## What it does not do

* **It does not replace the primary morphology and the distribution.** It sits on top of them,
  applied to a lesion already described, sited and palpated.
* **It does not make a changing lesion safe.** This is **Zoroark**. With **Illusion** it walks out
  wearing the appearance of the last conscious Pokémon in the party, and the opposing side
  computes type effectiveness against the species it can *see* — the game models the observer
  being wrong. Only a damaging hit breaks it. **Mimikyu** does the same thing with a rag. A
  reassuring appearance does not override a history of change, growth, bleeding, ulceration or
  symptoms. The history outranks the image.
* **It is worse at some things.** Amelanotic, hypomelanotic and nodular lesions are harder
  dermoscopically, and those are not the benign end of the range.
* **It does not see deep.** Its useful depth is roughly the epidermis and papillary dermis. It is
  not a measure of thickness.
* **It informs a threshold, not a diagnosis.** The output is a decision about biopsy, excision,
  monitoring or referral. Histology is the diagnosis.

## Where the metaphor stops

This section carries no Pokémon, because the mechanism is over and the consequence is not
something to be cute about.

This answer is about assessing lesions that may be skin cancer, so the stakes belong in the open
rather than in a footnote.

On one side, under-recognition means a melanoma found later than it could have been, and found
later means a worse outcome. On the other, over-referral is not free either: it fills clinics and
delays the next person, and a biopsy leaves a permanent scar on somebody who did not need one.
That is an argument for being trained, not an argument for being relaxed.

And between the two there is a person waiting. Someone told that a lesion needs urgent assessment
will spend the intervening days frightened, and will remember how they were told for a long time
after they have forgotten the result. What you say while arranging the referral is part of the
care, not an add-on to it.

The hardest line in this answer is the one aimed at whoever is reading it about their own skin.
**Nothing here can be used to assess your own mole.** This answer deliberately contains no
criteria and no checklist, and looking the criteria up elsewhere does not fix that, because the
problem was never the missing list — it is that the observations are unreliable without trained
interpretation, and least reliable of all when the person interpreting them has the most to lose.
A mole or other lesion that is new, changing, growing, itching, bleeding, ulcerating, or that
simply looks unlike your others, needs to be seen in person, whatever any description appears to
show.

## What a Gym Leader is listening for

Why magnification alone adds little, in one sentence about the stratum corneum. The difference
between contact immersion and polarised dermoscopy, and why both exist. Which of the two levels of
the vocabulary trainees overestimate in themselves. And what you would do with a lesion whose
dermoscopic appearance is reassuring and whose history is not.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md).
Specific to this answer:

* For the descriptive lexicon of dermoscopic structures and the site-specific vocabularies: a
  standard dermoscopy atlas or textbook, current edition, and the consensus terminology documents
  published by the International Dermoscopy Society.
* For the structured algorithms deliberately not reproduced here, and for which one to learn: the
  dermoscopy training material used by your own service, plus the educational resources of your
  national dermatology professional body.
* For the evidence that accuracy depends on training: the systematic reviews of dermoscopy for
  melanoma diagnosis indexed in the Cochrane Library, where trained against untrained use is
  addressed properly.
* For when to refer regardless of what the dermatoscope shows: your region's suspected-skin-cancer
  referral guideline, issued by the national body that sets referral thresholds where you
  practise.

The Pokémon claims were checked separately, against the pret decompilation of Pokémon Emerald: the
twenty-five Natures and their stat table, the derivation from the personality value, the refusal
to modify HP, accuracy or evasion, Smokescreen having zero base power and lowering accuracy, and
Butterfree's Compound Eyes. Machamp's No Guard, which arrived in the fourth generation and so
postdates those games, and the Illusion behaviour including the opposing side reasoning from the
false species, were checked against the pokeemerald-expansion project.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

This answer is about skin cancer assessment, so the limit needs stating without hedging and
without a joke. **It explains why a tool exists and what kind of information it produces. It
contains no criteria, no feature list usable as a checklist, and nothing whatsoever that could be
used to assess a mole — on yourself or on anyone else.** That is deliberate, and it is not an
oversight to be corrected by looking the criteria up elsewhere. The central claim of this answer
is that these observations are unreliable without trained interpretation, and that claim applies
with the most force to somebody examining their own skin, with the most to lose and the least
calibration.

Urgent-assessment pathways for suspected skin cancer exist because this assessment cannot be done
from a page. Anyone with a mole or other lesion that is new, changing, growing, itching, bleeding,
ulcerating, or that simply looks unlike their others, needs to be seen in person, and that applies
whatever any image or description appears to show.

Local guidance is the authority on referral thresholds, on which dermoscopy algorithm is used, and
on who is trained to use one. All three differ by country and by institution.

## Where this stands, October 2026

The optics and the descriptive lexicon are settled. What keeps moving is the integration of
dermoscopy with photographic monitoring and automated image analysis, where the evidence
accumulates faster than the guidance that would tell a service how to use it, and where the
training dependency above is the main open question rather than a solved one. Current as of
October 2026.
