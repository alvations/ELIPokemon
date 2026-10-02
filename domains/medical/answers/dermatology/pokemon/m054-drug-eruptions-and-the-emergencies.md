---
id: "m054"
slug: drug-eruptions-and-the-emergencies
style: pokemon
category: dermatology
difficulty: advanced
question: "How are drug eruptions recognised as patterns, and which few of them are emergencies?"
tags: [drug-eruption, pattern-recognition, severe-reactions, timeline, allergy-label]
---

# On turn one a Badly Poisoned Pokémon is taking half what a merely Poisoned one is

The healthbox prints three letters. **PSN**. It prints the same three letters whether a Pokémon is
**Poisoned** or **Badly Poisoned**, because the code that chooses the status graphic tests a
single combined poison flag and hands back one sprite for both. There is no second icon in the
third generation, so **Toxic** — 85 accuracy, 10 **PP** — announces itself on screen exactly the
way the 30 per cent poison chance on a **Sludge Bomb** does. The display cannot tell you which of
the two you are looking at.

The arithmetic underneath is completely different, and it is different in a direction that catches
people out:

```
   SAME ICON. DIFFERENT TRAJECTORY. AND THE WORSE ONE STARTS SMALLER.
   ==================================================================================

   TURN        POISONED (maxHP/8 flat)      BADLY POISONED (maxHP/16 x counter)
   =========   ==========================   ========================================
   1           2/16 of max HP               1/16   <-- HALF as much damage
   2           2/16                         2/16   <-- now identical
   3           2/16                         3/16
   4           2/16                         4/16
   5           2/16                         5/16
   ...         2/16                         ... and the counter keeps incrementing,
                                            capped at fifteen turns
   ==================================================================================
   On turn one, the Pokemon that is in real trouble is the one taking LESS damage.
   You cannot tell them apart from the icon. You cannot tell them apart from the
   first number. You tell them apart from the SHAPE OF THE SEQUENCE -- and from
   whether anything else has gone wrong at the same time.
   ==================================================================================
```

That is the whole shape of recognising a drug eruption. Most cutaneous adverse drug reactions are
benign and look broadly alike: a morbilliform or maculopapular exanthem, symmetrical, trunk-first,
itchy, in somebody who is otherwise well. A small number look much the same on day one and are
life-threatening. Separating them is the entire clinical skill, and it is done on **pattern** —
the morphology, the mucosae, the systemic features, the latency, the trajectory — not by reasoning
about the pharmacology of the suspect drug.

So the order of questions is fixed. First: is this one of the severe patterns. Second: which
pattern. Only third: which drug, and what happens to the chart. Reversing those is how a severe
reaction gets a telephone review and a reassurance.

## The discriminators, which are a short list and need no laboratory

```
   WHAT SEPARATES A BENIGN EXANTHEM FROM A SEVERE REACTION
   ==================================================================================

   FEATURE                 BENIGN EXANTHEM          POINTS TOWARDS SEVERE
   =====================   ======================   ===============================
   mucosae                 spared                   eyes, mouth, genitals involved
                                                    -- especially two or more sites
   =====================   ======================   ===============================
   skin sensation          itchy                    PAINFUL, tender, burning
   =====================   ======================   ===============================
   epidermis               intact                   dusky, blistering, sloughing,
                                                    detaching with lateral pressure
   =====================   ======================   ===============================
   systemically            well                     fever, unwell, facial oedema,
                           afebrile or low fever    lymphadenopathy
   =====================   ======================   ===============================
   organs                  uninvolved               transaminases, creatinine,
                                                    eosinophils, atypical
                                                    lymphocytes, haematuria
   =====================   ======================   ===============================
   extent                  limited, trunk-first     widespread, confluent,
                                                    erythrodermic
   =====================   ======================   ===============================
   TRAJECTORY              static or settling       extending hour by hour
   ==================================================================================
   Only the organ row needs a laboratory. Everything else is a two-minute
   examination that includes the mouth, the eyes and the genitals -- which is
   precisely why those three get skipped.
```

## Future Sight, and the reaction whose culprit you stopped thinking about

**Future Sight** has 80 base power, 90 accuracy and 15 **PP**, and it does something no other move
in the third generation does. When it is used, the damage is **calculated immediately** and
stored, and a counter is set to three. Nothing happens. The counter ticks down at the end of each
turn, and the hit arrives two turns later, from a Pokémon that may not even be on the field any
more. **Doom Desire** runs on the same counter.

A trainer reading the board on the turn the move was used sees nothing and concludes nothing
happened.

Latency is the single most useful discriminator between the severe drug reaction patterns, and it
points in both directions. An urticarial reaction arrives in minutes to hours. A morbilliform
exanthem arrives within the first fortnight. Acute generalised exanthematous pustulosis arrives
within a few days. And the drug hypersensitivity syndrome arrives **later than an exanthem** —
weeks rather than days — which is exactly why its culprit is so often a drug that has been in the
chart long enough to stop looking suspicious. The damage was computed when the move was used. It
lands on turn three.

## The Held Item was never drawn on the sprite

A wild **Pikachu** in Hoenn may be holding an **Oran Berry**. It may be holding a **Light Ball**.
The sprite shows neither, the summary screen shows neither, and the way you find out is **Knock
Off** — you ask, directly, and something falls out.

The drug chart is the **Held Item**, and the method for finding the culprit is a timeline rather
than a hunch. Every drug started, stopped or changed in the relevant window, with dates:
prescriptions, over-the-counter preparations, herbal and traditional medicines, intravenous
contrast, and anything given in another institution. The window is set by the pattern, which is
why the pattern is identified first — a reaction with the latency of a hypersensitivity syndrome
will not be explained by something started yesterday, and an urticarial reaction will not be
explained by something started last month.

Certain classes recur across the severe patterns: the antibiotics, particularly beta-lactams and
sulfonamides; the aromatic anticonvulsants; allopurinol; the non-steroidal anti-inflammatory
drugs; several antiretrovirals. Pharmacogenomic associations exist for some drug and population
pairs, and pre-treatment testing is required in some countries for some of them — which ones, and
for whom, is firmly (**country-dependent**) and is a formulary question.

## Why rare and catastrophic gets a written rule rather than a judgement call

Four moves in the games are one-hit knockouts: **Guillotine**, **Horn Drill**, **Fissure** and
**Sheer Cold**. The data for them is almost comically thin — base power stored as 1, accuracy 30,
five **PP**. They almost never come off. And competitive play's standard rulesets ban them
outright, alongside the evasion-raising moves, under what the community calls the OHKO clause.
That clause is a players' ruleset, written and maintained by a community, not a line in the game's
code, and it is worth being exact about that.

The reasoning behind it is the reasoning behind a severe-reaction pathway. A rare event with a
catastrophic and unrecoverable outcome is not well handled by individual judgement in the moment,
because the base rate is low enough that the correct response feels like over-reaction every
single time it is made. So it gets written down in advance by people who are not under time
pressure. That is what the severe cutaneous adverse reaction pathway in a hospital is, and it is
why the right move on seeing mucosal involvement and painful skin is to escalate rather than to
weigh probabilities.

## The other patterns worth holding by name

**Fixed drug eruption** — one or a few round, dusky, sharply demarcated plaques that recur **at
the same site** on every re-exposure. The recurrence at the same place is the diagnosis, and it is
as reproducible as **Tyrogue** branching on one stat comparison.

**Vasculitic eruption** — palpable purpura, dependent distribution, which prompts assessment for
renal and other organ involvement rather than dermatological treatment alone.

**Photosensitivity** — confined to exposed sites, with sparing under a watch strap, in a collar
shadow, in the submental triangle. The spared areas are the finding, in exactly the way
**Skarmory** walking in untouched is how you know there are **Spikes** down; the sibling answer in
this set on distribution works that through.

**Urticaria and angioedema** — wheals, each one lasting under a day, with angioedema of lips,
tongue or airway. Minutes to hours, not days.

**Lichenoid, psoriasiform, acneiform, bullous and pigmentary** patterns all exist and all have
characteristic culprit classes, and that is a reference text rather than one answer.

## The allergy label is an intervention and it lasts longer than the episode

What gets written in the record outlives the admission by decades. A label reading only
"penicillin — rash" cannot distinguish a childhood viral exanthem from anaphylaxis, and the
downstream cost is measurable: broader-spectrum alternatives, worse outcomes in some infections,
more resistance. The useful record states the drug, the date, the pattern, the latency, the
severity, what happened on withdrawal, and whether it was ever formally assessed. Equally, a
genuinely severe reaction has to be recorded so that it cannot be missed, with the cross-reacting
agents named. Both failures are common and they fail in opposite directions.

It is the **Original Trainer** and **ID No.** field of the whole business: a small entry, written
once, that every later reader is bound by and that nobody can correct from the outside.

## Where the metaphor stops

The metaphor stops here and it stops completely, because four of these reactions are emergencies
and being approximately right about them is not useful. No analogy, no compression.

**Anaphylaxis.** Onset in minutes. The diagnosis rests on sudden airway, breathing or circulatory
compromise after an exposure, usually but **not always** with skin or mucosal features — cutaneous
signs may be absent, and waiting for them is a described cause of delay. Treatment is
intramuscular adrenaline, immediately, at the dose and site set by your resuscitation council's
current guidance, with a call for help. This answer states no dose, deliberately. Anaphylaxis is a
resuscitation topic and that guidance is the authority.

**Stevens-Johnson syndrome and toxic epidermal necrolysis.** A spectrum divided by the percentage
of body surface detached, with the threshold values in the standard classification rather than
here. The features are mucosal involvement, typically two or more of ocular, oral and genital;
skin that is painful rather than itchy; dusky atypical target lesions or confluent erythema;
blistering; epidermal detachment; and a prodrome that can look like a viral illness. The latency
from starting the drug is characteristically days to a few weeks. Management is immediate
withdrawal of the suspect drug, urgent senior and multidisciplinary involvement, and transfer to a
unit equipped for extensive epidermal loss. Supportive care dominates and the role of specific
immunomodulatory treatments is genuinely contested. Ophthalmology is involved early, because
ocular sequelae are a major source of long-term disability.

**Drug reaction with eosinophilia and systemic symptoms, also called drug hypersensitivity
syndrome.** The distinguishing feature is latency: it starts weeks rather than days after the drug
was begun. Fever, facial oedema, widespread eruption, lymphadenopathy, eosinophilia or atypical
lymphocytosis, and visceral involvement — hepatitis most often, but also kidney, lung and heart.
It can worsen or relapse after the drug has been stopped, and late autoimmune sequelae including
thyroid disease are described, so follow-up runs beyond recovery.

**Acute generalised exanthematous pustulosis.** Rapid onset, characteristically within a few days.
Dozens to hundreds of small sterile non-follicular pustules on oedematous erythema, often
beginning in the flexures and on the face, with fever and neutrophilia. It usually settles with
desquamation after withdrawal, and the main differential is pustular psoriasis.

These are serious illnesses and the human part of them has to be said too. Extensive epidermal
loss is intensely painful; the pain is continuous, is worsened by every necessary intervention,
and is routinely under-treated. People in that situation need analgesia planned deliberately by
people with the expertise to do it, and they need to be asked.

The experience is frightening in a particular way, because the cause was a treatment. Someone who
becomes critically unwell from a tablet prescribed for something minor is dealing with a loss of
trust as well as an illness, and the people who prescribed it are often carrying something too.
Neither is helped by the conversation being avoided.

The consequences do not all end with the admission: ocular scarring, dry eye and visual loss,
chronic mucosal disease, nail and skin changes, lasting fatigue and persistent psychological
distress are all described after the severe reactions. Follow-up is not a formality.

Without softening: nothing in this answer helps anybody decide about a rash they have now, and
these patterns are not self-assessable. Anyone who develops a rash with fever, with soreness of
the mouth, eyes or genitals, with skin that is painful or blistering, or who feels unwell after
starting a new medicine, needs urgent in-person assessment. Anyone with sudden breathing
difficulty, throat or tongue swelling, or faintness after a medicine needs an emergency ambulance
— call your local emergency number rather than reading further.

## What a Gym Leader is listening for

Why the mucosae are examined before the trunk when a drug eruption is suspected. Why latency
discriminates between the severe patterns better than morphology does — the **Future Sight**
counter rather than the board on the turn it was used. What separates acute generalised
exanthematous pustulosis from pustular psoriasis. Why a drug hypersensitivity syndrome can worsen
after the drug has been stopped. What a useful allergy entry contains. And why a benign exanthem
and day one of a severe reaction can look identical, and what you do with that uncertainty.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in the dermatology sources file in the
writers' directory for this domain, and they are the authority for everything procedural or
quantitative here. Specific to this answer:

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md).
Specific to this answer:

* For anaphylaxis recognition and treatment, including the adrenaline dose, route and repeat
  interval, and the observation period afterwards: the current guidance of your national
  resuscitation council. This answer states no dose. That guidance is the authority and it is
  revised.
* For the classification of Stevens-Johnson syndrome and toxic epidermal necrolysis by detached
  body surface area, and for the severity scoring tools: a current standard dermatology text and
  the specialist guideline issued by your national dermatology body.
* For the management of severe cutaneous adverse reactions, including whether and which
  immunomodulatory treatment is used: the specialist guideline where you practise, and the primary
  literature, because this is contested.
* For drug-specific risk, pharmacogenomic pre-treatment testing requirements and cross-reactivity:
  your national formulary and the summary of product characteristics for the drug.
* For adverse-reaction reporting: the scheme operated by your national medicines regulator.
* For allergy-label assessment and de-labelling: your national allergy body's guidance and your
  own institution's policy, which is what you will be held to.

The Pokémon claims were checked separately against source. Ordinary poison costing a flat eighth
of maximum HP each turn while badly poisoned costs a sixteenth multiplied by a counter that
increments each turn and is capped at fifteen, the healthbox selecting one shared PSN graphic from
a single combined poison flag, Toxic's 85 accuracy and 10 PP, Sludge Bomb's 30 per cent chance of
inflicting ordinary poison, Future Sight's 80 base power, 90 accuracy and 15 PP with its damage
calculated at the moment of use and its counter set to three, Doom Desire sharing that counter,
Guillotine, Horn Drill and Fissure each stored with base power 1, accuracy 30 and 5 PP, and the
wild Pikachu's possible Oran Berry and Light Ball are all from the pret decompilation of Pokémon
Emerald. Sheer Cold is a fourth-generation move and is named from general knowledge of the series
rather than from those files. **The OHKO clause is a competitive community ruleset, not game code,
and no decompilation was or could be consulted for it** — it is named here as what it is.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**This answer deliberately contains no drug doses, no severity score cut-offs and no detachment
thresholds**, because those are exactly the numbers that must come from a current primary document
rather than from revision material. It names patterns in order to explain how they are told apart,
and it cannot be used to identify a reaction in a real person. An answer here agreeing with your
memory is not confirmation.

Nothing here is for self-assessment. A rash with fever, with soreness of the mouth, eyes or
genitals, with painful or blistering skin, or in someone who feels unwell after starting a new
medicine, needs urgent in-person assessment. Sudden breathlessness, throat or tongue swelling, or
faintness after a medicine needs an emergency ambulance — call your local emergency number rather
than reading further.

Local guidance, your resuscitation council and the formulary where you practise are the authority
on all of this, and they differ by country and by institution.

## Where this stands, October 2026

The pattern descriptions and the discriminating features here are long-settled and are the stable
part of the answer. Three things are not. The role of specific immunomodulatory therapy in
Stevens-Johnson syndrome and toxic epidermal necrolysis remains contested and practice differs
between centres and countries. Pharmacogenomic pre-treatment screening is expanding, and which
drug and population pairs require it differs by country and is being added to. And allergy
de-labelling has moved from a specialist interest to an organised activity in several health
systems, with pathways that did not exist a decade ago. Anaphylaxis guidance is revised
periodically by the resuscitation councils, which is why no dose appears above. Current as of
October 2026.
