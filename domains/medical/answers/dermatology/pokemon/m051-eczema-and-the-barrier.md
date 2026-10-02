---
id: "m051"
slug: eczema-and-the-barrier
style: pokemon
category: dermatology
difficulty: core
question: "Why is atopic eczema best understood as a barrier disease, and why is the quantity of emollient the intervention rather than an adjunct?"
tags: [eczema, barrier, emollient, filaggrin, itch]
---

# A Substitute costs a quarter of your own HP, and it is made out of you

**Substitute** is not a buff. The code is unambiguous about this: it takes exactly a quarter of
the user's maximum **HP**, it hands that quarter over to a doll that then takes the damage, and —
this is the part people forget — **it fails outright if the user's current HP is at or below that
quarter**. You cannot put up a Substitute out of nothing. It is a structure, and it is built from
the same substance it is protecting.

While it stands, it is doing more than soaking damage. The secondary effects that would otherwise
land on the Pokémon behind it do not land: the status condition, the stat drop, the thing the
attacker was really there for. Break it and all of that goes straight through on the next hit,
with no announcement that anything has changed.

That is the epidermal barrier. In atopic eczema it is deficient — reduced filaggrin, a disordered
lipid matrix of ceramides, cholesterol and free fatty acids — and it is deficient in skin that
looks completely normal, not only in the patches that are flaring. Water leaves outwards.
Irritants, allergens and microbes come inwards. The threshold for inflammation drops.
**Substitute** was never the flourish on the set; it was load-bearing.

## Heavy-Duty Boots, and the hazard that only costs you without them

**Heavy-Duty Boots** have one of the shortest item descriptions in the games: *protects from the
effects of traps set on the field*. With the Boots on, **Spikes** and **Stealth Rock** are simply
not events — the Pokémon walks in and nothing happens. Take them off and every single entry costs
something, and it costs again on the next entry, and the hazard has not changed at all. The
difference is entirely in what is on the feet.

An irritant is an entry hazard. So is a surfactant, so is wool, so is a house-dust-mite allergen,
so is *Staphylococcus aureus*. None of them is new on the field. Intact skin walks past them.
Barrier deficient skin pays each time.

## Rollout, which is what a loop looks like when you write the numbers down

**Rollout** has 30 base power, 90 accuracy and 20 **PP**, and none of that is the interesting
part. The interesting part is that its power doubles on each consecutive turn it keeps going, up
to five turns, and doubles again if **Defense Curl** was used first. A move that starts at 30 and
is multiplying because it has not stopped.

```
   THE TWO ARMS OF THE CYCLE, AND WHAT CUTS EACH ONE
   ==================================================================================

                    +-------------------------------------------+
                    |   THE SUBSTITUTE IS BROKEN                |
                    |   reduced filaggrin, disordered lipid     |
                    |   matrix, raised water loss outwards,     |
                    |   raised surface pH                       |
                    +--------------------+----------------------+
                                         |
                 hazards now land        |        cracks, fissures,
                 on every entry          |        water lost
                                         v
   IMMUNOLOGICAL ARM  <------------------+------------------>  MECHANICAL ARM
   ==================                                          ==============
   type 2 inflammation                                          itch
   (IL-4, IL-13, IL-31 among others)                            scratching
   |                                                            |
   | the stat drops that a                                      | Rollout: 30 base
   | Substitute would have                                      | power, doubling
   | blocked now land, and                                      | every turn it is
   | they drive the itch                                         | not interrupted
   +------------------->  THE BARRIER GETS WORSE  <-------------+
   ==================================================================================
   HAZE cuts the LEFT arm. It wipes every stat stage on the field, both sides,
   back to neutral -- and it does not rebuild one point of a broken Substitute.
   SUBSTITUTE cuts the RIGHT arm, by being there at all.
   Use Haze and never Substitute and you are on a relapse cycle by construction.
```

## Haze is the cleanest mapping in this answer, so it is worth being precise about

**Haze** resets the stat stages of **every** Pokémon on the field to neutral. The implementation
loops over all battlers and writes the default into all seven slots; it is indiscriminate, it is
immediate, and it is extremely useful. What it does not touch, at all, is `substituteHP`. A broken
Substitute stays broken through a Haze.

A potent topical corticosteroid is **Haze**. It will clear the accumulated inflammatory state and
it is the right move when that state is what is in front of you. It rebuilds nothing. An emollient
is putting the **Substitute** back up, at the cost of the resource it is made from, on skin that
looks fine as well as skin that does not.

The reverse mistake is just as common and worth naming. Putting up Substitute after Substitute
while your stats are at minus four is also losing. Emollient alone on actively inflamed skin is
under-treatment, and the instinct to avoid the steroid and double the moisturiser prolongs the
flare.

## Light Screen, and why the intervention is the amount

**Light Screen** costs 30 **PP** and sets a timer to exactly **five**. Five turns, then it is
gone, and from the fourth generation a **Light Clay** stretches it to eight. Nothing about Light
Screen is improved by wanting it more. It is a timer, so the only levers are how often you set it
and how long each setting lasts.

An emollient's effect on water loss is transient in exactly that way. [mechanism] Twice a day, and
more often during a flare, beats a richer preparation used once, and that is a statement about
frequency rather than about potency.

And the quantity is set by the fact that it goes on the **whole surface**, not on the patches,
because the barrier defect is present in normal-looking skin. National formularies publish tables
of suitable amounts per week; for an adult with widespread dry skin the figures are of the order
of several hundred grams a week, and a 50 g or 100 g tube is not a week of anything.
[country-dependent] Look the table up. The sibling answer in this set on topical quantity makes
the general case; here the quantity is not a dosing detail, it *is* the treatment of the
structural lesion.

Acceptability is part of the dose, and the games already made this argument: a **Master Ball**
catches nothing from inside the bag. The greasy ointment that is refused delivers zero, and the
preparation somebody will actually use on their hands at work beats the theoretically optimal one.
Soap goes too — surfactants strip the lipid matrix, so an emollient wash in place of soap is the
same intervention and not an extra.

## Dry Skin, which is an actual named ability and does the whole thing in four words

From the fourth generation **Paras** and **Parasect** carry a second ability called **Dry Skin**,
and its in-game description is *Heat hurts, Water restores*. The implementation is exactly that: a
Water move heals a quarter of maximum HP instead of damaging, a Fire move comes in at 1.25 times,
it gains an eighth of maximum HP at the end of each turn in rain, and it loses HP in sun.

One ability, pointing in two directions, keyed entirely to what the environment is doing. That is
the barrier phenotype, and the fact that the games named it Dry Skin is a coincidence worth
taking.

## What the preparations differ in, and what they do not

They sit on a gradient of lipid content from lotions through creams to ointments; they may add
humectants such as urea or glycerol, which hold water in, and occlusives such as the paraffins,
which reduce its loss. Preservatives and fragrances can themselves sensitise, so a worsening
eczema in somebody using five products is a reason to think about contact allergy rather than to
reach for a stronger **Haze**. Paraffin-containing emollients carry a real fire risk once the
residue has soaked into fabric and dressings, and national medicines regulators have issued safety
communications about it.

Two things taught confidently a decade ago have not held, and the honest answer says so: daily
emollient from birth as **primary prevention** in at-risk infants has not shown the benefit the
early work suggested, and bath additives tested in children already using leave-on emollients
added no clinically useful benefit, with several national bodies withdrawing them. The order and
spacing of emollient against topical corticosteroid is genuinely unsettled and practice varies.

Above the first rung the ladder runs through topical calcineurin inhibitors, phototherapy,
conventional systemic immunosuppressants, and the newer targeted biologics and oral Janus kinase
inhibitors, with eligibility and monitoring that are firmly **country-dependent**. Every one of
those rungs is a better **Haze**. Not one of them puts up a **Substitute**, which is why the
emollient does not stop when the systemic starts.

## Where the metaphor stops

This section carries no Pokémon, because the mechanism is over and the consequences are not
something to be cute about.

Itch is not a minor symptom and should not be recorded as one. It interrupts sleep every night,
for the person and for whoever shares the house, and chronic sleep deprivation does to judgement,
mood and school performance what chronic sleep deprivation does. Children scratch in their sleep
and wake bleeding. Parents sit up with them.

The treatment is a daily unpaid job. Emolliating a whole body twice a day takes real time, twice a
day, every day, with no end date given. It marks clothes and bedding. Many people cannot reach
their own back or their own feet. Asking what the eczema and its treatment stop someone doing is a
better question than asking how itchy it is, and it changes management more often.

The visible disease carries a social cost that is easy to under-weigh from behind a desk —
covering up in heat, avoiding swimming, avoiding changing rooms, flinching at a handshake. And
people with long-standing eczema have often been told by several clinicians to use the treatment
sparingly, and then told that it did not work. Being told a treatment failed when it was never
delivered in the amount it needed is a harm that outlasts the consultation by years.

One clinical thing has to be said flatly rather than through an analogy, because it is the thing
that gets missed. Widespread monomorphic punched-out erosions on atopic skin, with fever or in
someone systemically unwell, may be eczema herpeticum rather than infected eczema. It is an urgent
problem, it is treated with systemic antiviral therapy and senior involvement, and it is named
here precisely because it looks like the ordinary thing.

Without softening: nothing in this answer is for any reader's own use, and no quantity named here
is a prescribing instruction. Anyone whose eczema is not improving, or who is worried about a
treatment they have been given, needs the prescriber or pharmacist who issued it.

## What a Gym Leader is listening for

Why a defective barrier raises the risk of food and aeroallergen sensitisation, and what that
implies about the sequence of the atopic march. How you would separate colonisation from infection
at the bedside without a swab — which in this register is why a **Pokémon** standing in a
**Sandstorm** is not necessarily being damaged by it. Why emollient quantity is specified per week
rather than per application. And what you would reconsider in an asymmetrical eczema that has not
responded to three weeks of adequate treatment.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in the dermatology sources file in the
writers' directory for this domain, and they are the authority for everything procedural or
quantitative here. Specific to this answer:

* For emollient quantities per week and for the preparations available: the emollient and barrier
  preparation section of your national formulary, including its table of suitable quantities. The
  figures differ between countries and nothing here substitutes for the table.
* For the fire risk associated with paraffin-containing emollients: the drug-safety communications
  issued by your national medicines regulator, and the summary of product characteristics for the
  individual preparation.
* For the management pathway, including criteria for systemic and targeted therapy: the atopic
  eczema guideline issued by the national body that sets guidance where you practise.
* For filaggrin and the barrier biology: a current standard textbook of dermatology.
* For the primary-prevention and bath-additive questions, where the position has changed: the
  primary literature, because this is the material a textbook edition lags on.

The Pokémon claims were checked separately against source. Substitute's quarter-of-maximum-HP cost
and its failure when the user is already at or below that quarter, its blocking of secondary move
effects, Haze resetting the stat stages of every battler on the field, Light Screen's five-turn
timer and 30 PP, and Rollout's 30 base power, 90 accuracy and 20 PP are all from the pret
decompilation of Pokémon Emerald. Rollout's doubling on consecutive turns and after Defense Curl
is the move's documented behaviour and is not quoted from a code line here. The Master Ball always
succeeding is from the pret decompilation of Pokémon Red. Heavy-Duty Boots and its description,
and Paras and Parasect carrying Dry Skin with its quarter-max-HP heal from Water moves, its 1.25
multiplier against Fire and its eighth-of-maximum-HP recovery per turn in rain, are from the
pokeemerald-expansion project, because those are fourth-generation and eighth-generation content
and the pret decompilations stop at the third.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No quantity, preparation or treatment step named here is a prescribing instruction, and none of
it addresses any reader's own treatment.** The figures are here so the reasoning behind them is
visible — why the amount is large, why it is specified per week — and not so they can be applied
to a person. Paediatric quantities, which differ by age, have deliberately not been reproduced. An
answer here agreeing with your memory is not confirmation; check the formulary before anything
reaches a patient.

Anyone whose skin condition is not improving needs to be seen. A widespread eruption on atopic
skin with fever, with monomorphic punched-out erosions, or in someone systemically unwell needs to
be seen urgently rather than managed from a revision page.

Local guidance and the formulary where you practise are the authority on all of this, and they
differ by country and by institution.

## Where this stands, October 2026

The barrier model and the filaggrin association are settled, and they are the stable part of this
answer — rather more stable than **Light Screen**, which has had a **Light Clay** bolted onto it
since the third generation. What has moved, and moved against the earlier consensus, is primary
prevention: daily emollient from birth is no longer the straightforward recommendation it looked
like becoming. Bath additives have gone the same way in several countries. The systemic and
targeted end of the ladder is the fastest-moving part of the specialty, and eligibility,
sequencing and monitoring for the biologics and the Janus kinase inhibitors differ between
countries and are being revised repeatedly, so nothing here should be read as describing what is
funded or licensed where you work. Current as of October 2026.
