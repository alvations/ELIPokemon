---
id: "m088"
slug: photoprotection-and-cumulative-dose
style: pokemon
category: dermatology
difficulty: core
question: "Why is photoageing a function of cumulative ultraviolet dose, and why is the number printed on a sunscreen not the protection a person gets?"
tags: [photoprotection, ultraviolet, photoageing, sunscreen, prevention]
---

# Thunder is printed as 70, cannot miss in rain, and is 50 in harsh sunlight

**Thunder** has one number in `gBattleMoves`: accuracy 70, alongside power 120, 10 PP and a 30 per
cent paralysis chance. That 70 is a true statement about the move and a poor prediction of what
happens.

In rain, `AccuracyCalcHelper` sees `EFFECT_THUNDER` and returns before the accuracy check runs at
all: the move cannot miss. In harsh sunlight, `Cmd_accuracycheck` overwrites `moveAcc` with **50**
before any other modifier. And in ordinary weather the printed figure is multiplied through a
stage ratio table, then by **Compound Eyes** at 130/100 if **Butterfree** is using it, then by
**Sand Veil** at 80/100 if a Sandstorm is up and the target has it, then by **Hustle** at 80/100
for a physical move, and finally by a held item: **Bright Powder** carries `holdEffectParam` 10,
so accuracy times 90 over 100, and **Lax Incense** carries 5, so times 95 over 100. Same two
items, same hold effect, different parameter.

One printed number. Four or more real ones. **Which one applies is decided by the sky and by what
is standing in front of you, and nothing about the number on the move is dishonest — it is just a
statement about a defined test.**

That is the sun protection factor. It is a ratio: the ultraviolet dose needed to produce a defined
erythemal response with the product on, over the dose needed without it, measured in a laboratory
at a standardised application density considerably heavier than anyone uses, against an endpoint
that responds mostly to one part of the spectrum. [definitional] Honest about the experiment. Not
a prediction of what a person gets at the beach.

```
   FOUR THINGS THE PRINTED FIGURE DOES NOT TELL YOU
   ==================================================================================

   THE PROPERTY                   WHY IT IS NOT IN THE NUMBER
   ============================   ===================================================
   longer-wavelength protection   the factor is calibrated on ERYTHEMA, which is
                                  predominantly a shorter-wavelength endpoint. A
                                  separate measure exists for the longer waveband,
                                  and the grading systems, marks and test methods
                                  differ by country -- not interchangeable
   ============================   ===================================================
   how thickly it went on         the test density is heavier than real use, so real
                                  protection is lower, and this is the commonest
                                  reason a product looks like it failed
   ============================   ===================================================
   the shape of the curve         factor against transmitted fraction is reciprocal,
                                  so the first step removes a large share of the
                                  transmitted dose and the last step removes a small
                                  one -- the high numbers are not a trick, the
                                  marginal gain is just small
   ============================   ===================================================
   whether it is still there      water, sweat, towels, rubbing and time remove it;
                                  water resistance is tested separately
   ==================================================================================
```

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. *mechanism* — follows
from biology and is checkable by reasoning. *definitional* — a term's meaning. *consensus* —
standard across current textbooks and national guidance. *country-dependent* — differs between
countries or institutions, and yours is the authority. The Pokémon claims are not marked this way;
they are listed in the `## Sources` section with the file they were checked against.

## The Sandstorm exemption list is the photoprotection hierarchy, in code

`Cmd_weatherdamage` costs a battler **maximum HP divided by sixteen** every turn a Sandstorm is
up, with a floor of 1. And then it lists five separate ways to take nothing at all:

```
   FIVE ROUTES TO ZERO, AND THEY ARE NOT THE SAME KIND OF THING
   ==================================================================================

   THE ROUTE                      WHAT IT IS                   THE PHOTOPROTECTION
                                                               EQUIVALENT
   ============================   ==========================   ====================
   first or second type is ROCK   a standing property,          clothing, a wide
                                  checked by name against      brim, close-weave
   Shuckle is Bug/Rock,           three constants. No           fabric: a physical
   Tyranitar is Rock/Dark         multiplier, no roll           barrier over the area
   ============================   ==========================   it covers, needing no
   first or second type is        same check, different         reapplication and not
   GROUND -- Sandslash,           constant                     depending on how it
   Dugtrio                                                      was spread
   ============================   ==========================   ====================
   first or second type is        same check again --           ...
   STEEL -- Skarmory, Steelix     Skarmory is Steel/Flying
   ============================   ==========================   ====================
   the ability is SAND VEIL --    an ability, not a type.       sunscreen: a real
   Cacturne, Sandslash,           Also the same ability         effect, entirely
   Dugtrio                        that multiplies incoming      dependent on being
                                  accuracy by 80/100            present and intact
   ============================   ==========================   ====================
   STATUS3_UNDERGROUND or         not on the field. Dig and     shade, timing, being
   STATUS3_UNDERWATER             Dive put you there           indoors: the exposure
                                                               never happens
   ==================================================================================
   The ordering in the clinic is not a value judgement, it is the same arithmetic.
   Three of those five routes are CATEGORICAL -- a check against a constant, which
   poor technique cannot degrade. One is an ability that has to be there. And being
   Underground is the only one that is not protection at all: it is absence.
```

That is why photoprotection advice consisting only of a product recommendation is incomplete
advice. A categorical reduction cannot be ruined by spreading it thinly. A multiplicative one can
be reduced to almost nothing by exactly that.

And Sand Veil earns its place in the table twice over, because in the code it does two jobs with
one name: it exempts the holder from the storm's damage **and** it multiplies an incoming move's
accuracy by 80/100. A real sunscreen is similarly not one thing — filters, vehicle, substantivity
and the pigment that absorbs visible light are separate properties under a single number.

## Effort values are the cumulative dose, and nothing displays them

Every time a Pokémon in the party survives a battle, `MonGainEVs` runs. It looks up the defeated
species' six effort-yield fields and adds them to six hidden counters — **Wurmple** yields one HP
point, **Beautifly** three Special Attack, **Dustox** three Special Defence. The multiplier is
doubled by **Pokérus** or by a held **Macho Brace**. The total is capped at 510 and each
individual counter at 255, and the function clips mid-loop when the cap is reached.

Then look at where those counters surface. In `CalculateMonStats` the maximum HP is `(((2 * baseHP
+ hpIV + hpEV / 4) * level) / 100) + level + 10`. **The effort value enters divided by four.**
Three deposits can accumulate and move nothing visible at all; the fourth moves the number by a
point.

That is photoageing, and it is why the forearm and the upper inner arm of the same person at the
same age do not look the same:

```
   THE DEPOSIT, THE DIVISOR, AND THE REVERSAL THAT IS ONLY PARTIAL
   ==================================================================================

   THE GAME                               THE SKIN
   ====================================   ===========================================
   a small amount is added per            dose is irradiance multiplied by exposure
   encounter, from a per-species field    time: latitude, season, time of day,
                                          altitude, cloud, reflection off snow,
                                          water, sand and concrete -- multiplied by
                                          how long you were in it
   ====================================   ===========================================
   nothing on the summary screen shows    the dermal change -- collagen loss and
   the counter                            disorganisation with accumulation of
                                          abnormal elastotic material -- precedes the
                                          visible coarse wrinkling
   ====================================   ===========================================
   the stat formula divides the counter   a visible change appears only once the
   by four, so most deposits move         accumulated dose has crossed a threshold,
   nothing visible                        which is why photoageing looks like it
                                          started suddenly in middle age
   ====================================   ===========================================
   a Pomeg Berry lowers one counter and   topical retinoids have the best-established
   raises friendship. Partial, specific,  evidence for improving photodamaged skin;
   and the game has a dedicated message   field treatments reduce the actinic
   for a counter that cannot fall any     keratosis burden on a damaged field; device
   further                                treatments improve specific features. None
                                          of it restores the dermis
   ====================================   ===========================================
   HONEST LIMIT: effort values cap at     ultraviolet dose does NOT cap. The analogy
   510 total and 255 per stat             breaks here and it is worth saying so
                                          rather than leaving the cap to imply a
                                          ceiling that does not exist
   ==================================================================================
```

Two patterns of deposit are worth keeping apart, because they do not carry the same consequences.
Chronic cumulative exposure — the outdoor worker's lifetime — is most associated with keratinocyte
cancers and with actinic keratoses as a field change. Intermittent intense exposure with sunburn,
particularly in childhood, features more prominently in the epidemiology of melanoma. Both are
dose; they are different distributions of the same dose. [consensus] The recognition and referral
reasoning for the cancers themselves lives in the oncology answers m061 to m065 and in this
specialty's m020, and none of it is re-derived here.

## Safeguard is five turns and will not refresh itself

**Safeguard** sets a side status and a timer of exactly 5, and `Cmd_setsafeguard` **fails outright
if Safeguard is already up** — it does not top the timer back up. That is the same non-refresh
behaviour the endocrinology answers m057 to m059 build on, and here it is simply what
reapplication is: a product has a duration, it is removed by water and sweat and towels and
rubbing, and putting more on top of an intact layer is not the same act as replacing a layer that
has gone.

## Two wavebands, which the game would call two types

```
   WHAT THE SPECTRUM ACTUALLY DOES
   ==================================================================================

                       SHORTER WAVELENGTH (UVB)       LONGER WAVELENGTH (UVA)
   =================   ============================   ===========================
   how deep            largely epidermal              reaches the dermis
   =================   ============================   ===========================
   main mechanism      DIRECT absorption by DNA,      indirect -- reactive oxygen
                       producing photoproducts        species damaging lipids,
                       between adjacent               proteins and DNA at one
                       pyrimidines                    remove
   =================   ============================   ===========================
   the acute sign      sunburn: the dominant          pigment darkening, with much
                       waveband for erythema          less erythema per unit dose
   =================   ============================   ===========================
   window glass        largely blocked                passes
   =================   ============================   ===========================
   thin cloud          attenuated                     substantially transmitted
   =================   ============================   ===========================
   through the year    varies strongly with the       varies far less: present
   and the day         sun's angle                    across the day and the year
   =================   ============================   ===========================
   dominant role       carcinogenesis via direct      photoageing: dermal elastosis
                       DNA damage, and ageing too     and collagen degradation
   ==================================================================================
   Visible light is not inert either: it contributes to pigment darkening and matters
   in melasma and the photodermatoses, which is why some products aimed at pigmentary
   disease include a visible-light-absorbing pigment.
   "It is cloudy", "I was indoors by the window" and "it is winter" are each true
   about one waveband and false about the other -- the type chart is not one column.
```

## The groups for whom the arithmetic changes

**Photosensitising medicines** — several antibiotic classes, diuretics, retinoids, amiodarone,
some antifungals and many more — lower the dose at which a reaction occurs, and the eruption is a
drug eruption, which is m054's territory. **The photodermatoses** are disorders where ultraviolet
is the trigger rather than a risk factor. **Immunosuppression**, especially after solid organ
transplantation, substantially changes the risk of keratinocyte cancers for a given exposure
history, and those patients are usually in a structured surveillance pathway. **A previous skin
cancer** changes subsequent management. **Children** matter disproportionately, because the total
is a lifetime total. **The genetic DNA-repair deficiencies** are rare and change everything.

And the trade-off that is genuinely unsettled: ultraviolet contributes to cutaneous vitamin D
synthesis, so complete avoidance has a cost, and the balance struck between photoprotection advice
and vitamin D sufficiency is **country-dependent** and differs by latitude, population and
national policy. Picking one country's answer and asserting it would be wrong.

## Where the metaphor stops

No Pokémon in this section.

The people with the highest lifetime ultraviolet doses are mostly people who were working.
Construction, agriculture, fishing, landscaping, roofing, delivery, outdoor sport and military
service all involve exposure that is not a lifestyle choice, and in many countries occupational
ultraviolet exposure is poorly regulated compared with other occupational carcinogens. Advice
built around not going out at midday is advice for people whose employer decides when they go out.
Where a national occupational health framework does address it, that framework is the authority,
and it differs considerably between countries.

Photoprotection advice also lands unevenly for another reason. The visible signs of photodamage,
the available formulations, the cosmetic acceptability of mineral filters on different skin tones,
and the assumption that darker skin needs no advice at all are all areas where the standard
teaching is calibrated on a narrow range of skin — m018 makes that argument in full. Higher
constitutive melanin reduces but does not abolish ultraviolet-related harm, and photoprotection
remains relevant in all skin tones, with the pigmentary consequences of ultraviolet and visible
light a prominent concern in skin that tans readily.

Two things that should be said without euphemism. A tan is a response to DNA damage, not a sign of
health, and there is no such thing as a safe tan from ultraviolet exposure. And sunbeds deliver
ultraviolet deliberately; their use is restricted or banned for minors in many countries and the
restrictions are country-dependent.

Without softening: nothing here is for any reader's own use, no product or factor named here is a
recommendation, and this answer cannot be used to judge any particular person's risk. Anyone with
a new, changing, bleeding or non-healing lesion on sun-exposed skin needs to be assessed in person
rather than reassured by a general argument about dose, and anyone with a severe reaction to sun
exposure, or a reaction after starting a new medicine, needs medical assessment.

## What a Gym Leader is listening for

Which waveband dominates sunburn and which dominates dermal photoageing. Why window glass and thin
cloud change one and not the other. The exact definition of the sun protection factor, and the
three things it does not tell you — the Thunder problem: one printed number, several real ones.
Why real-world protection is lower than the label figure. Why the curve of factor against
transmitted dose flattens. Why clothing and shade sit above sunscreen in the hierarchy — three
categorical routes to zero against one ability that has to be present. Which exposure pattern is
more associated with keratinocyte cancer and which with melanoma. What photosensitising medicines
do to the dose-response. And the honest answer on vitamin D.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For how the sun protection factor and longer-wavelength protection are measured and labelled:
  the cosmetic product regulations and labelling rules of the regulator where you practise. These
  differ substantially between regions and the marks are not interchangeable.
* For national photoprotection advice, including sunbed restrictions and advice for children: the
  public health body and the cancer prevention body of the country where you practise.
* For the vitamin D balance and any supplementation advice: your national public health guidance,
  which differs by latitude and by population.
* For occupational ultraviolet exposure: the occupational health and safety regulator where you
  practise, and any national guidance on outdoor work.
* For photosensitising medicines: your national formulary, which lists photosensitivity as an
  adverse effect agent by agent.
* For the photodermatoses, photoageing histology and the treatment of photodamaged skin: a current
  standard textbook of dermatology and the specialist guidance of your national dermatology body.
* For surveillance after transplantation or previous skin cancer: your regional skin cancer
  pathway and your transplant centre's protocol.

The Pokémon claims were checked separately against source. Thunder's data — power 120, accuracy
70, 10 PP, 30 per cent paralysis chance; `AccuracyCalcHelper` returning early for `EFFECT_THUNDER`
in rain so the move cannot miss, and `Cmd_accuracycheck` setting `moveAcc` to 50 in sun; the
accuracy stage ratio table; Compound Eyes multiplying by 130/100 and Butterfree carrying it; Sand
Veil multiplying by 80/100 in a Sandstorm; Hustle multiplying by 80/100 for physical moves; Bright
Powder and Lax Incense sharing `HOLD_EFFECT_EVASION_UP` with `holdEffectParam` 10 and 5
respectively; `Cmd_weatherdamage` costing maximum HP divided by sixteen with a floor of 1 and
exempting a battler whose first or second type is Rock, Ground or Steel, or whose ability is Sand
Veil, or who is Underground or Underwater; Tyranitar being Rock/Dark with Sand Stream as its only
ability, Shuckle Bug/Rock, Sandslash and Dugtrio Ground with Sand Veil, Cacturne Grass/Dark with
Sand Veil, Skarmory Steel/Flying and Steelix Steel/Ground; `MonGainEVs` reading the defeated
species' six effort-yield fields, doubling for Pokérus or a held Macho Brace, and clipping at 510
total and 255 per counter; Wurmple yielding one HP point, Beautifly three Special Attack and
Dustox three Special Defence; the maximum HP formula dividing the effort value by four; the Pomeg
Berry lowering a counter while raising friendship, with a dedicated message for a counter that
cannot fall further; and Safeguard setting a side status with a timer of 5 and failing outright
rather than refreshing when it is already up — all from the pret decompilation of Pokémon Emerald.
Note that `Cmd_weatherdamage` contains no Special Defence boost for Rock types in a Sandstorm;
that is a fourth-generation change and is not in this code.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No product, factor, application amount, exposure time or supplementation advice named here is an
instruction, and none of it addresses any reader's own treatment or behaviour.** No numerical
factor value appears in this answer on purpose: the labelling systems differ by region and the
authority is the regulator and the public health body where you practise.

Anyone with a new, changing, bleeding, crusting or non-healing lesion on sun-exposed skin needs to
be assessed in person. A severe reaction to sun exposure, or any reaction to sunlight that begins
after starting a new medicine, needs medical assessment.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The physics and the histology are settled and are the part worth memorising. What moves is
regulation and product science. Filter approvals differ by region and several filters licensed in
one jurisdiction are not available in another, which is a long-standing difference rather than a
transitional one. Labelling of longer-wavelength protection has been through more than one
revision and still differs by region. The environmental impact of specific filters on reef
ecosystems has driven local bans in some jurisdictions, and systemic absorption of organic filters
has been the subject of regulatory review in more than one region, and what those regulators
actually concluded is readable only in their own published statements rather than here. The
vitamin D balance remains genuinely contested at the level of national advice. Occupational
ultraviolet exposure has been gaining recognition as an occupational carcinogen in several
countries, and that is the area most likely to look different in five years. The Sandstorm
exemption list, by contrast, is six conditions in one `if` and has not needed revising. Current as
of October 2026.
