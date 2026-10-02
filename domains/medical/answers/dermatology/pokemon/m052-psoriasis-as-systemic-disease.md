---
id: "m052"
slug: psoriasis-as-systemic-disease
style: pokemon
category: dermatology
difficulty: intermediate
question: "Why is psoriasis described as a systemic inflammatory disease that presents on the skin, and what follows from that for assessment?"
tags: [psoriasis, comorbidity, interleukin, arthritis, biologics]
---

# Kyogre does not attack you, it changes the weather, and then six other things attack you

**Kyogre** has one ability and it is **Drizzle**. Send it out and the implementation does
something that no attacking move does: it writes rain into the field itself, and in the third
generation it writes it as **permanent** — the end-of-turn code that counts weather down
explicitly skips weather that an ability set. The rain does not expire. Nothing has been damaged
yet.

Then look at what the rain is now doing, in different places, to different Pokémon, on both sides
of the field:

* Every **Water**-type move is multiplied by one and a half, and every **Fire**-type move is
  halved.
* **Thunder** stops being a 70-accuracy gamble. In rain the accuracy check is bypassed outright —
  the code jumps straight past it.
* **Solar Beam** is halved, because any weather other than sun weakens it.
* A **Kingdra** with **Swift Swim** has its Speed doubled. Its base Speed of 85 is unremarkable
  right up until the moment it is not.
* A **Ludicolo** with **Rain Dish** recovers a sixteenth of its maximum **HP** at the end of every
  turn, for free, indefinitely.

Six readouts, in six places, from one upstream event. If you were handed a battle log that showed
only the Thunder landing, you would conclude that you had an accuracy problem. You would be
describing the one box you could see.

Psoriasis is the weather. Activated dendritic cells produce interleukin-23; interleukin-23
sustains a T-helper-17 population; those cells produce interleukin-17A and its relatives; and
keratinocytes respond by proliferating, keeping their nuclei into the stratum corneum and
recruiting neutrophils. The plaque — thick, sharply demarcated, silvery-scaled — is that cascade's
readout in one organ. The same cytokines are at work on synovium, on entheses, on vascular
endothelium, on gut mucosa and on the uveal tract.

## One setter, several readouts

```
   ONE AXIS, SEVERAL ORGANS, AND WHERE THERAPY INTERVENES
   ==================================================================================

   THE SETTER                  THE AXIS                    READOUT IN ONE PLACE
   =====================       ==================          ==========================
   susceptibility              dendritic cell              SKIN
   (HLA-C*06:02 among          |                           keratinocyte proliferation,
   others) plus a trigger      | interleukin-23            parakeratosis, neutrophils
   - streptococcal throat      v                           in the corneum, dilated
     infection                 Th17 population             dermal capillaries
   - skin injury: Spikes       |                           ==========================
     laid where you were       | interleukin-17A           JOINT AND ENTHESIS
     hurt, the Koebner line    | and relatives             synovitis, enthesitis,
   - certain drugs             v                           dactylitis, axial disease
   - abrupt withdrawal of      effector inflammation       ==========================
     a systemic steroid        in several tissues          VESSEL WALL
   - smoking, obesity                                      accelerated atherosclerosis
   =====================                                   ==========================
                                                           GUT / EYE
   The plaque is ONE box.                                   inflammatory bowel disease,
   The one you can see is not                               uveitis
   the one that matters most.                              ==========================
   ==================================================================================
   RAYQUAZA's AIR LOCK, or a GOLDUCK's CLOUD NINE, acts at the narrow part of this
   diagram. The macro that gates every single weather effect in the game is literally
   written as "no Cloud Nine on the field AND no Air Lock on the field". One ability,
   and the Water boost, the Fire reduction, the Thunder accuracy bypass, the Solar
   Beam penalty, the Swift Swim doubling and the Rain Dish tick all stop at once.
   A topical acts in one box. That is the whole difference.
```

**Air Lock** is the sharpest fact in this answer and it is worth being exact about. Rayquaza is
the only Pokémon in the third generation that has it, and **Psyduck** and **Golduck** are the only
two carrying **Cloud Nine**. Neither ability removes the rain. `gBattleWeather` still says rain.
What the macro does is make every consumer of that value stop consuming it. The driver is
untouched and the downstream effects are gone.

That is what an agent directed at interleukin-23 or interleukin-17 does, and it is why one drug
improves skin **and** joints while a potent topical cannot. The topical is standing in one of the
boxes on the right.

## What follows for assessment, in order of how often it is missed

**Psoriatic arthritis.** A substantial minority of people with psoriasis develop it — figures of
the order of one in five to one in three are commonly quoted, and they move with the population
studied and the case definition. The skin disease usually arrives years before the joint disease,
so the skin appointment is the screening opportunity, and what it prevents is structural and
permanent. The questions are about pattern rather than about pain: morning stiffness lasting more
than half an hour, better with movement than with rest, a whole digit swollen rather than a joint,
heel or insertional pain, inflammatory back symptoms. Validated screening questionnaires exist and
which one is used is **country-dependent**.

**Nails.** Pitting, onycholysis, subungual hyperkeratosis and the salmon-coloured oil drop sign
travel with psoriatic arthritis and with disease of the neighbouring distal interphalangeal joint,
which is anatomically unsurprising given what the nail apparatus and that joint share. The nail is
the **Pokédex** AREA page of this condition: a small panel, easy to skip, and it tells you which
part of the map you are actually in.

**Severity is not area.** Body surface area and composite scores are the currency for eligibility
and for trials, and they under-rate certain sites badly. Scalp, nails, palms, soles, flexures and
genital skin can occupy almost no area and run somebody's life. This is **Base Stat Total** doing
its usual damage: **Shedinja** has 1 base HP and the lowest total in this answer, and **Wonder
Guard** means only a super-effective move touches it at all, while **Chansey**'s 250 base HP sits
next to a base Attack of 5. The single aggregate number was never the thing. That is why an impact
measure runs beside the area measure rather than instead of it.

**Cardiometabolic risk.** The associations with metabolic syndrome, obesity, type 2 diabetes,
hypertension, dyslipidaemia, fatty liver and cardiovascular events are robust. Whether they are
causal, shared-pathway, or confounded by smoking, alcohol and adiposity is still argued, and the
honest line is that the association holds and the mechanism does not. The practical consequence is
not in dispute: cardiovascular risk factors get reviewed, on an interval that is
**country-dependent**.

**And the spared organ is not evidence of nothing happening.** **Tyranitar**'s **Sand Stream**
puts up a **Sandstorm** that costs a sixteenth of maximum HP per turn to everything on the field —
except **Rock**, **Ground** and **Steel** types, anything with **Sand Veil**, and anything that
happens to be underground or underwater at the time. Tyranitar is Rock and Dark and takes nothing
from the storm it set. Reading the field off the Pokémon that is comfortable would tell you there
was no storm.

## Triggers, and the one that is a prescribing trap

Streptococcal pharyngitis seeding guttate psoriasis is the classic. Injury seeding plaques along
the line of the injury is the Koebner phenomenon — three layers of **Spikes** in one place because
somebody used the move three times, which the sibling answer in this set on distribution works
through properly. Smoking and obesity travel with both incidence and severity. Lithium,
beta-blockers, antimalarials and the interferons are the drug classes textbooks consistently name.

The trap is the systemic corticosteroid. Stopping one abruptly, given for something else entirely,
can precipitate a severe flare including the generalised pustular and erythrodermic forms, and
that is the standard reason systemic steroids are not psoriasis treatment. It is an **Explosion**
problem: the move resolves and then the field is not what you set it up to be.

## The ladder, and why its rungs have different reach

A vitamin D analogue, usually combined with a topical corticosteroid, plus coal tar and dithranol
in some settings, acts in the skin box. Phototherapy — narrowband ultraviolet B, or psoralen with
ultraviolet A — acts in the skin and in the infiltrate just under it, with a cumulative-dose
record kept because lifetime exposure matters. Methotrexate, ciclosporin and acitretin are the
long-standing systemic three and act broadly, with monitoring set by your own formulary.

The biologic classes are where the **Air Lock** sits: tumour necrosis factor, the shared p40
subunit of interleukin-12 and interleukin-23, interleukin-17 and its receptor, and interleukin-23
alone, with oral small molecules alongside. Which agents are licensed, which are funded, in what
order and on what criteria is **country-dependent** and moves often enough to be looked up rather
than recalled.

## Where the metaphor stops

This section carries no Pokémon, because the mechanism is over and the consequences are not
something to be cute about.

Two clinical states sit outside the ladder because they are acute, and they are stated plainly for
that reason. Generalised pustular psoriasis and erythrodermic psoriasis present with a person who
is systemically unwell — impaired thermoregulation, fluid and electrolyte loss, and a risk of
secondary infection. Both are inpatient problems with senior and often multidisciplinary
involvement, and neither is recognised by its score.

Psoriasis is visible, and it sheds. Scale on dark clothing, on car seats, in the bed, on the floor
of a changing room. People describe the shedding as the most humiliating part, more than the itch,
and they are rarely asked about it.

The assumption of contagiousness is met constantly — in swimming pools, at hairdressers, in gyms,
from strangers, and sometimes from healthcare staff. Genital and flexural involvement affects
sexual relationships and is almost never volunteered. Scalp involvement affects hair, hats and
barbers. These are not side issues; they are why two people with identical scores need different
plans.

Depression and anxiety are more common in this condition than in matched populations. That is
something to ask about directly and gently, in the same visit as the skin, by someone with time to
hear the answer. If a person's mood is the dominant problem then the dominant problem is their
mood, and it does not wait for the plaques to clear.

Without softening: nothing in this answer is a treatment plan for anyone. Psoriasis is highly
treatable and the options have improved a great deal. Anybody whose disease is not controlled, or
who has noticed joint pain or stiffness, needs their own clinician and not a revision page.

## What a Gym Leader is listening for

Why an agent aimed at interleukin-23 improves skin and joints while a potent topical cannot —
which in this register is why **Air Lock** beats out-damaging the rain. Why nail involvement
raises your suspicion of psoriatic arthritis, and what in the anatomy explains it. What is wrong
with body surface area as the only severity measure, and which sites break it. Why systemic
corticosteroids are not psoriasis treatment. And what you would do differently in somebody with a
tiny area of disease and a severe impact score.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in the dermatology sources file in the
writers' directory for this domain, and they are the authority for everything procedural or
quantitative here. Specific to this answer:

* For the treatment pathway, severity thresholds and biologic eligibility: the psoriasis guideline
  issued by the national body that sets guidance where you practise, with your region's funding
  criteria alongside it. These differ substantially between countries and change often.
* For the systemic agents and the biologics — dosing, contraindications, pre-treatment screening
  and monitoring: your national formulary and the summary of product characteristics for each
  product.
* For psoriatic arthritis screening and referral: the psoriatic arthritis guidance issued by your
  national rheumatology body, which also names the questionnaires in local use.
* For the comorbidity associations and the argument about mechanism: the primary literature, since
  this rests on observational evidence rather than on mechanism.
* For the immunology, the histology and the clinical variants: a current standard textbook of
  dermatology.

The Pokémon claims were checked separately against source. Kyogre's Drizzle, Groudon's Drought,
Tyranitar's Sand Stream and Rayquaza's Air Lock each being that species' only ability, Psyduck and
Golduck carrying Cloud Nine as a second ability, Kingdra's base Speed of 85 and Ludicolo's Rain
Dish, the rain multipliers of one and a half for Water and one half for Fire, Solar Beam halved by
any weather other than sun, Thunder's accuracy check bypassed in rain, Swift Swim doubling Speed
in rain, Rain Dish and Leftovers each restoring a sixteenth of maximum HP, Sandstorm costing a
sixteenth of maximum HP while sparing Rock, Ground and Steel types and Sand Veil holders,
Shedinja's 1 HP and Wonder Guard, Chansey's 250 base HP and base Attack of 5, and the weather
macro being written as the absence of Cloud Nine and Air Lock on the field are all from the pret
decompilation of Pokémon Emerald.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No agent, class, severity threshold or eligibility criterion named here is a prescribing
instruction, and none of it addresses any reader's own treatment.** The drug classes appear so the
reasoning about where in the cascade they act is visible, not so a reader can locate themselves on
a ladder. Pre-treatment screening and monitoring for the systemic and biologic agents are
substantial, are set locally, and have deliberately not been reproduced.

Generalised pustular and erythrodermic psoriasis need urgent assessment. Anyone with widespread
redness and scaling who feels unwell, feverish or shivery needs to be seen urgently rather than to
read about it.

Local guidance and the formulary where you practise are the authority on all of this, and they
differ by country and by institution.

## Where this stands, October 2026

The immunology here — the interleukin-23 and interleukin-17 axis as the therapeutic target — is
settled enough to teach, and it is why the answer is shaped as it is. The comorbidity associations
are robust; the causal reading is not, and anyone asserting it confidently has gone past the
evidence. What moves fastest is the top of the ladder: licensed indications, funded positions,
head-to-head comparisons and what to do after a first biologic has failed are all being revised
and differ between countries. Treat any specific agent, line of therapy or threshold named here as
something to re-check — with more suspicion than you would apply to **Drizzle**, which has behaved
identically since **Hoenn**. Current as of October 2026.
