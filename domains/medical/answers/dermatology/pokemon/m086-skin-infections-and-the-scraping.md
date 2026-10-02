---
id: "m086"
slug: skin-infections-and-the-scraping
style: pokemon
category: dermatology
difficulty: intermediate
question: "Why do skin infections and infestations that look alike need different treatments, and what is the skin scraping or swab actually for?"
tags: [skin-infection, dermatophyte, scabies, microscopy, antimicrobials]
---

# Earthquake does nothing at all to Beautifly and lands normally on Dustox, and they were the same cocoon

**Wurmple** is a Bug-type with **Shield Dust**, and at level 7 it evolves. Which way it evolves is
decided by one line in `GetEvolutionTargetSpecies`: the personality value is shifted right by
sixteen bits, and if that upper half modulo ten is four or less you get a **Silcoon**, and
otherwise you get a **Cascoon**. Nothing in the game shows you the number. It was written when the
Wurmple was generated and it has not changed since — the same device m016 uses for **Spinda**'s
spots, applied to a fork in the road instead of a pattern of dots.

Then look at what the two cocoons actually are. Silcoon and Cascoon have **identical base stats**:
50 HP, 35 Attack, 55 Defence, 15 Speed, 25 Special Attack, 25 Special Defence. The same single
ability, **Shed Skin**. The same pure Bug typing. The same effort yield of two Defence points.
They differ in body colour and in one single point of experience yield — 71 against 72.

And then they diverge completely:

```
   ONE HIDDEN NUMBER, TWO TYPINGS, AND A MOVE THAT IS A ZERO AGAINST ONE OF THEM
   ==================================================================================

                         BEAUTIFLY                    DUSTOX
   ===================   ==========================   ===========================
   from                  Silcoon (upper half of       Cascoon (upper half of
                         the personality value        the personality value
                         mod ten is 4 or less)        mod ten is 5 or more)
   ===================   ==========================   ===========================
   types                 Bug / Flying                 Bug / Poison
   ===================   ==========================   ===========================
   ability               Swarm                        Shield Dust
   ===================   ==========================   ===========================
   the stat it keeps     Special Attack 90            Special Defence 90
   ===================   ==========================   ===========================
   a Ground move         NO EFFECT. Ground into       lands at exactly x1:
                         Flying is coded              x0.5 into Bug multiplied
                         TYPE_MUL_NO_EFFECT           by x2 into Poison
   ===================   ==========================   ===========================
   a Rock move           x4 -- Rock is super          x2 -- super effective
                         effective into Bug AND       into Bug, ordinary into
                         into Flying                  Poison
   ==================================================================================
   The cocoons were interchangeable. The answers are not, and one of them is a zero,
   which is the m007 point: a zero is not a small number. No amount of Earthquake
   gets you past it.
```

That is the whole argument for the skin scraping. An annular scaly plaque is tinea, or discoid
eczema, or psoriasis in an odd configuration, or granuloma annulare. An antifungal has no
mechanism against a mite; an acaricide has none against a dermatophyte; and a topical steroid has
none against either. The appearance is the cocoon stage. The sample is the only way to read the
number that decides which of several non-interchangeable treatments can work at all.

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. **mechanism** —
follows from biology and is checkable by reasoning. (**definitional**) — a term's meaning.
(**consensus**) — standard across current textbooks and national guidance. (**country-dependent**)
— differs between countries or institutions, and yours is the authority. The Pokémon claims are
not marked this way; they are listed in the `## Sources` section with the file they were checked
against.

## Growl makes the hits smaller and does not touch Leech Seed

**Growl** is a real move with base power 0, accuracy 100 and 40 PP, and it does one thing: drop
the target's Attack by one stage. Watch the damage numbers afterwards and they are visibly
smaller. Something is working.

**Leech Seed** has accuracy 90 and sets a flag in a different place entirely — `gStatuses3`, not
the battler's stats. At the end of every turn the drain is computed as the seeded battler's
**maximum HP divided by eight**, with a floor of 1. There is no Attack term in that expression.
Growl does not reduce it by a single point. Six Growls do not reduce it by a single point.

A topical corticosteroid on tinea is Growl. It genuinely does something — the scale goes, the edge
softens, the itch settles — and the organism keeps spreading, because the steroid is aimed at the
host response and the host response was the thing you were using to follow the disease.
(**mechanism**) The resulting hard-to-recognise widening eruption has a name, tinea incognito, and
it is produced by a perfectly reasonable sequence of decisions.

The generalisation is the one to carry out of this answer: **a treatment aimed at the readout
changes the readout.** After Growl, a smaller number no longer means what it meant.

What actually clears Leech Seed is **Rapid Spin**, and the way it clears is instructive in its own
right — the routine checks for being wrapped first, then Leech Seed, then **Spikes**, and returns
after the first one it finds. One thing per use, in a fixed order. That is m045's stewardship
point and it is exactly how a treatment plan with four problems in it behaves.

## Shield Dust blocks the secondary effect and not the hit

Dustox keeps Wurmple's **Shield Dust**, and the code is precise about what it does: in
`SetMoveEffect` the Shield Dust clause fires only when the effect is **not primary** and its index
is low in the table. The hit still lands. The burn or the flinch that would have come with it does
not.

That is the cleanest statement of what suppressing inflammation buys. The secondary consequences
are blunted and the primary mechanism is untouched, and the Pokémon in front of you looks like it
is handling the fight better than it is.

## Doom Desire is computed now and lands later

**Jirachi** learns **Future Sight** at level 40 and **Doom Desire** at level 50, and both run
through `Cmd_trysetfutureattack`. The routine calls `CalculateBaseDamage` **at the moment the move
is used**, stores the result, sets a counter to three, and flags the target's whole side. What
lands later is a number computed from the state of the battle at the moment of setting — not from
the state when it arrives. A second one cannot be set while the first is pending.

Mycology culture is that. The result describes the skin as it was when the sample was taken, grown
slowly and reported later, which is why the sample goes **before** treatment starts and why a
scraping taken from a site already treated answers a question about a different field. Microscopy
is the quick look; culture names the species and takes much longer, and species identification is
what tells you whether the source was an animal and whether systemic treatment is likely to be
needed. (**consensus**)

Two honest limits, because the game is honest about them too. Doom Desire has accuracy 85, not 100
— a negative scraping does not exclude the diagnosis, and in nail disease a single negative
against a convincing picture is usually repeated. And the swab discipline from m055 applies
unchanged: skin is colonised, colonisation is not infection, and a bacterial swab from a site that
is merely colonised invites antibiotics nobody needed.

## Spikes belong to the side, not to the Pokémon

**Spikes** is laid on a side of the field, stacks to three layers in the third generation — three,
not two, and this is a generation-three change — and goes on costing every entry until something
clears it. The Pokémon standing there did not bring it and cannot remove it by being treated.

Scabies is that shape. The mite population spans a household, so the hazard is in the environment
and in the untreated contacts, and treating one person while leaving the field seeded reliably
fails. The itch persisting after successful treatment is a hypersensitivity response to mite
material still in the skin rather than evidence of failure. (**mechanism**) The contact protocols,
the laundering, the number of applications and the agent are all (**country-dependent**), and
crusted scabies — very high mite burden, usually in someone immunosuppressed, often not very itchy
— is managed differently and more aggressively.

## Where the result changes the plan rather than confirming it

```
   THE DECISIONS A RESULT ACTUALLY TURNS
   ==================================================================================

   SITE / SITUATION             WHY THE RESULT MATTERS MORE THAN USUAL
   ==========================   =====================================================
   scalp                        topical treatment does not reliably reach the
                                follicle, so confirmed disease generally means
                                systemic therapy, and the agent differs by organism
                                and by age -- country-dependent
   ==========================   =====================================================
   nail                         long treatment, systemic agents with interactions and
                                monitoring, and a high rate of non-fungal mimics:
                                confirmation before committing is standard
   ==========================   =====================================================
   a child with scalp disease   contact tracing, school and nursery advice, and
                                treatment of family members: all country-dependent
   ==========================   =====================================================
   treatment failure            resistance, wrong class, wrong diagnosis, or
                                re-exposure -- four different answers
   ==========================   =====================================================
   immunosuppression            atypical organisms, atypical appearances, and a lower
                                threshold for sampling and for biopsy
   ==================================================================================
```

## Where the metaphor stops

No Pokémon in this section. There are a small number of situations in this territory where the
question stops being which organism and becomes how quickly someone is seen, and they are worth
stating without ornament:

* **pain out of proportion to the appearance, rapid spread, skin necrosis, crepitus, or systemic
  illness** — necrotising soft tissue infection is a surgical emergency and does not wait for a
  swab;
* **spreading erythema with fever, rigors, confusion or low blood pressure** — sepsis assessment,
  not a dermatology referral;
* **widespread monomorphic punched-out erosions in someone with eczema** — eczema herpeticum,
  which is urgent;
* **shingles involving the ophthalmic distribution, or the tip of the nose, or a disseminated
  eruption in someone immunosuppressed** — urgent same-day assessment;
* **widespread superficial blistering and skin shedding in a young child with fever** —
  staphylococcal scalded skin syndrome, a paediatric emergency;
* **any rash with mucosal involvement, systemic upset, or blistering after a new medicine** — that
  is m054's territory and the thresholds there are low on purpose.

The ordinary stakes are smaller and still real. These conditions are visible, they are on the
hands and the face, and people are routinely treated as unclean because of them. Scabies in
particular carries a stigma that has nothing to do with hygiene and that stops people presenting;
the same is true of head lice in school-age children and their families. Treatment that requires a
household conversation, or applying a product to the whole body at a set time, or washing
everything in a house, is a large practical imposition on people who may not have a washing
machine or a spare set of bedding. An agreed plan that fits the household is part of the treatment
and not an administrative afterthought.

And stated without softening: nothing here is for any reader's own use, no agent named is a
recommendation, and anyone with a spreading, painful, blistering or feverish skin problem needs
assessing in person rather than reading about classes of organism. If someone is systemically
unwell, that is an emergency call.

## What a Gym Leader is listening for

Why a corticosteroid changes the appearance of tinea without changing its course — Growl against
Leech Seed, and no Attack term in `maxHP / 8`. Where on an annular plaque the scraping is taken,
and why. What microscopy answers that culture does not, and the reverse. Why a negative mycology
result in nail disease is usually repeated. Why scalp and nail disease usually need systemic
treatment. Why routine swabbing of colonised skin causes harm. Which lesion in scabies is the
diagnostic one, and why the widespread rash is not. Why itch after successful scabies treatment is
expected. And the one that separates candidates: what would make you biopsy rather than swab.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For antifungal, antiviral, antibacterial and acaricidal agents — licensed indications, age
  restrictions, interactions, monitoring and duration: your national formulary.
* For when and how to sample, transport and interpretation: your local microbiology and mycology
  laboratory's user handbook, which specifies what that laboratory accepts and how it reports.
* For scabies and head lice — treatment of contacts, environmental measures, repeat applications
  and crusted scabies: the guidance of your national public health body, and your local health
  protection team for outbreaks and institutional settings.
* For school and nursery exclusion and contact tracing in scalp disease: your national public
  health guidance, which differs between countries.
* For antimicrobial choice under stewardship, including when a swab should be taken at all: your
  national antimicrobial guidance and your local microbiology policy.
* For the clinical descriptions and the mimics: a current standard textbook of dermatology.

The Pokémon claims were checked separately against source. Wurmple being a Bug-type with Shield
Dust; its level-7 split into Silcoon when the upper sixteen bits of the personality value modulo
ten are four or less and into Cascoon otherwise; Silcoon and Cascoon sharing base stats of
50/35/55/15/25/25, the Shed Skin ability, pure Bug typing and a two-point Defence effort yield
while differing in body colour and in experience yield of 71 against 72; Silcoon and Cascoon
evolving at level 10 into Beautifly and Dustox; Beautifly being Bug/Flying with Swarm and 90 base
Special Attack and Dustox being Bug/Poison with Shield Dust and 90 base Special Defence; Ground
being coded `TYPE_MUL_NO_EFFECT` into Flying, not very effective into Bug and super effective into
Poison; Rock being super effective into both Bug and Flying; Growl having power 0, accuracy 100
and 40 PP and lowering Attack by one stage; Leech Seed having accuracy 90, living in `gStatuses3`
and draining maximum HP divided by eight with a floor of 1; Rapid Spin checking wrapped, then
Leech Seed, then Spikes and returning after the first; Spikes stacking to three layers; the Shield
Dust clause in `SetMoveEffect` applying only to non-primary effects; and Jirachi learning Future
Sight at level 40 and Doom Desire at level 50, both running through `Cmd_trysetfutureattack`,
which computes the damage at the moment of use, stores it, sets a counter of three and flags the
target's side — all from the pret decompilation of Pokémon Emerald. Doom Desire's accuracy of 85
and Future Sight's of 90 are from the same move data file.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No agent, route, duration or sampling protocol named here is an instruction, and none of it
addresses any reader's own treatment.** Agents and durations differ by country, by age and by
site, and the formulary and local microbiology policy where you practise are the authority.

Anyone with a rash that is spreading rapidly, painful out of proportion to its appearance,
blistering, involving the eye or the mouth, or accompanied by fever or feeling unwell needs to be
assessed in person and urgently. Suspected necrotising soft tissue infection, sepsis, eczema
herpeticum and ophthalmic shingles are emergencies — call your local emergency number or use your
local urgent care route.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The biology is settled and is the part worth memorising: the classes of organism, what each sample
answers, and why suppressing the host response changes the readout rather than the disease. What
moves is everything procedural. Antifungal choice for scalp disease has long-standing differences
between countries in which agent comes first and at what age it is licensed. Scabies management
has been under active revision in several countries following reports of reduced efficacy of
established topical treatments and sustained outbreaks in institutional settings, and the role of
oral treatment, the number of applications and the contact protocols all differ by national
guidance. Resistance patterns in skin and soft tissue infection are local by definition. Molecular
testing has become more available for fungal and viral diagnosis and is changing turnaround times,
and therefore what is worth waiting for. The Wurmple fork, by contrast, has worked the same way
for the whole of the third generation. Current as of October 2026.
