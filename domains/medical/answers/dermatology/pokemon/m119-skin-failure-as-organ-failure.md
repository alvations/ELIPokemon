---
id: "m119"
slug: skin-failure-as-organ-failure
style: pokemon
category: dermatology
difficulty: advanced
question: "What does the skin actually do, and what happens to the rest of the body when a large area of it stops doing it?"
tags: [erythroderma, skin-failure, thermoregulation, barrier, organ-failure]
---

# A plaque is a volatile on one battler; losing most of the skin is weather

This answer takes the device m089 established and pushes it along the one axis the other
dermatology answers have not used: **scope**.

The third generation keeps "protected" in five separate structures — `status1`, `status2`,
`gStatuses3`, the side statuses with their timers, and the field weather. m089 used that to argue
about sampling, and m116 used it to argue about clearance. The fifth structure is the odd one out,
and it is the one this answer needs. **`gBattleWeather` belongs to neither battler.** It is a
single `u16` with no owner, read by routines that never look at a Pokémon's own data, and nothing
in the switch path touches it at all.

A plaque, a blister, a patch of eczema: those are `status2`. They belong to a battler, they are
read by the routines that read that battler, and they are cleared when that battler leaves. Lose
most of the skin's function and the state has **moved structure**. It is not a bigger `status2`.
It is weather, and the consequences are the consequences of being in that store: different
readers, different clock, and it survives everything that would clear a volatile.

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. (**mechanism**) —
follows from the physiology and is checkable by reasoning. (**definitional**) — a term's meaning.
(**consensus**) — standard across current textbooks and national guidance. (**country-dependent**)
— differs between countries or institutions, and yours is the authority. The Pokémon claims are
not marked this way; they are listed in the `## Sources` section with the file they were checked
against.

## One setter, one fraction, everybody present pays

Sandstorm is the cleanest arithmetic in the game and it is the right arithmetic here. m055 uses
the Leftovers-against-Sandstorm comparison in this specialty already; this answer uses the other
half of the same mechanic, the part about who pays.

```
   Cmd_weatherdamage, as written
   ==================================================================================
   if (WEATHER_HAS_EFFECT)
   {
     if (gBattleWeather & B_WEATHER_SANDSTORM)
     {
       if (   types[0] != TYPE_ROCK  && types[0] != TYPE_STEEL
           && types[0] != TYPE_GROUND
           && types[1] != TYPE_ROCK  && types[1] != TYPE_STEEL
           && types[1] != TYPE_GROUND
           && ability  != ABILITY_SAND_VEIL
           && !(gStatuses3[b] & STATUS3_UNDERGROUND)
           && !(gStatuses3[b] & STATUS3_UNDERWATER))
       {
           gBattleMoveDamage = maxHP / 16;      // floored at 1
       }
       else gBattleMoveDamage = 0;
     }
     ...
   }
   ==================================================================
   THREE THINGS TO NOTICE

   1  ONE setter. Sand Stream fires once, or one Sandstorm is used
      once, and the cost is then billed to EVERY battler present,
      every end of turn, from one global.

   2  The EXEMPTION LIST IS BY TYPE, NOT BY NAME. Rock, Steel,
      Ground. Nobody is spared for being important or for belonging
      to anybody. You are spared for WHAT YOU ARE.
      (And Hail's exemption list is Ice only -- a different field
      effect spares a different set.)

   3  There is NO Special Defence boost for Rock types in this
      function, or anywhere in the third generation. That is a
      fourth-generation addition and it is one of the most commonly
      misremembered facts in the game.
   ==================================================================
```

Map that onto a body that has lost most of its skin and the three numbered points are the three
things worth carrying. One upstream failure. A per-unit-time cost billed simultaneously to every
system that is not constitutionally exempt. And a set of exemptions determined by what each system
*is*, not by how important it is. (**mechanism**)

Worth naming the actual holders, because the third generation is stingier with them than memory
suggests. **Tyranitar** is the only species with **Sand Stream**, **Kyogre** the only one with
**Drizzle**, **Groudon** the only one with **Drought** — three species, three permanent field
states, one setter each. And Tyranitar is **Rock/Dark**, so the species that sets the sandstorm is
itself exempt from it by the type clause: the setter does not pay. The exempt list is populated
the same way — **Steelix** is Steel/Ground and **Aggron** is Steel/Rock, so both are spared by
what they are, while **Cacturne**, **Sandslash**, **Dugtrio** and **Gligar** are spared instead by
holding **Sand Veil**, which is a different clause in the same conditional. **Glalie** is pure Ice
and so is exempt from **Hail** and not from Sandstorm, because a different field effect carries a
different exemption list entirely.

That last point is the one that transfers. Which systems are spared when the barrier fails depends
on the *kind* of failure, not on its size: fluid loss, heat loss, protein loss, haemodynamic load
and infection risk are not spared or billed as a block, and reasoning about them as a block is the
error. (**mechanism**)

The six jobs and their six simultaneous bills:

| The job | What is billed when it fails |
| --- | --- |
| **Permeability barrier** | Transepidermal water loss rises; insensible fluid and electrolyte loss; dehydration and hypernatraemia. Invisible because it is not in a bag (**mechanism**) |
| **Thermoregulation** | **Hypothermia**, not hyperthermia. Inflamed skin is widely vasodilated and cannot conserve heat, so someone who looks hot is losing it, shivering, with a raised metabolic rate. Where sweating is also impaired the failure can reverse (**mechanism**, **consensus**) |
| **A haemodynamic compartment** | Vasodilation over a large area lowers peripheral resistance and raises cardiac output: a high-output state, peripheral oedema, and decompensation of pre-existing cardiac disease (**mechanism**, **consensus**) |
| **A structural protein store** | Scale is protein. Large-area shedding is a continuous drain: hypoalbuminaemia, oedema, negative nitrogen balance, raised requirement at the moment someone can least eat (**mechanism**) |
| **A barrier against infection** | Colonisation, fissuring, cellulitis, bacteraemia with the skin as the portal — the mechanism behind the mortality in this group (**consensus**) |
| **A pharmacokinetic barrier** | The stratum corneum is the rate-limiting step for percutaneous absorption, so absorption of anything applied rises substantially over a large broken area. m019's quantity argument (**mechanism**, **consensus**) |

Plus, over a longer horizon, cutaneous vitamin D synthesis, and the sensory and mechanical
protective functions — which is why shear injury and pressure damage are live risks in someone
immobile with fragile skin, and why m004's time-and-pressure argument applies here rather than
being a nursing aside.

## `_TEMPORARY` and `_PERMANENT` are two bits in one field, and that is the prognosis

This is the best thing in the data for this answer, and it is a distinction a player never sees
because the screen draws the same swirling sand either way.

```
   #define B_WEATHER_SANDSTORM_TEMPORARY (1 << 3)
   #define B_WEATHER_SANDSTORM_PERMANENT (1 << 4)
   #define B_WEATHER_SANDSTORM  (TEMPORARY | PERMANENT)
   ==================================================================
   SET BY A MOVE -- Cmd_setsandstorm:
        gBattleWeather = B_WEATHER_SANDSTORM_TEMPORARY;
        gWishFutureKnock.weatherDuration = 5;          <-- a clock

   SET BY AN ABILITY -- Sand Stream, on switch-in:
        gBattleWeather = B_WEATHER_SANDSTORM;          <-- both bits

   AND THE END-OF-TURN CODE:
        if (!(gBattleWeather & B_WEATHER_SANDSTORM_PERMANENT)
             && --gWishFutureKnock.weatherDuration == 0)

   C short-circuits the `&&`. With the PERMANENT bit set the
   decrement is NEVER EVALUATED. The clock is not ignored --
   it is never ticked. Nothing is counting down, because the
   setter is still standing on the field.
   ==================================================================
```

Erythroderma is the same field state arriving by two routes with two completely different clocks.
(**mechanism**)

**Set by an act, with a clock.** A drug reaction. The culprit is a discrete thing that was
introduced, stopping it is subtraction, and there is a timer running from the moment it stops.
Withdrawal of the drug is the highest-yield specific action available in this whole territory, and
it is the one cause reversed by taking something away rather than adding something.
(**consensus**)

**Set by a standing property, with no clock at all.** Psoriasis. Cutaneous T-cell lymphoma. The
inherited ichthyoses. The setter has not left the field, so the decrement is not reached, and
nothing resolves by waiting. (This is m009's asymmetry — Drizzle keeps raining after Kyogre has
gone — read in the direction where the ability-holder is *still there*.)

The field state looks identical on the screen. The two cases need different things, and the one
question that separates them is whether there is still a setter present.

## `WEATHER_HAS_EFFECT` is written as an absence, which is why the clue survives

The macro that decides whether field weather does anything at all is this, and it is written
backwards on purpose:

```
   #define WEATHER_HAS_EFFECT \
       ((!ABILITY_ON_FIELD(ABILITY_CLOUD_NINE) && !ABILITY_ON_FIELD(ABILITY_AIR_LOCK)))
```

There is no positive flag for "weather is working". The condition is the **absence** of two named
abilities — **Cloud Nine** and **Air Lock** — anywhere on the field, on either side. m052 made
this point about biologic therapy in psoriasis and it is reused here rather than re-derived: the
thing that switches off a field effect is not describable as a property of the field.

And the holders are worth checking rather than recalling, because this is a documented trap. In
the third generation **Cloud Nine** belongs to **Psyduck** and **Golduck** and to nobody else —
**Quagsire** is the species people attribute it to, and Quagsire's two abilities are **Damp** and
**Water Absorb**. **Air Lock** belongs to **Rayquaza** alone. So the entire off-switch for every
field effect in the game sits on three species, and a battle containing none of them has no way to
express "the weather is not doing anything".

The diagnostic consequence in erythroderma is the practical payoff. `gBattleWeather` is one
global, but it does not overwrite the battlers — every Pokémon present still has its own types,
its own ability and its own `status2`, and reading those is how you find out why the weather is
there. (**mechanism**)

So the examination in erythroderma is deliberately aimed at the places where the original disease
is still legible after everything else has gone uniformly red:

| Where to look | What it points to |
| --- | --- |
| **Nails and scalp** | Psoriasis, which also brings the prescribing trap: abrupt withdrawal of systemic corticosteroid can precipitate it, and can make it worse (**consensus**) |
| **Islands of sparing**, palmoplantar keratoderma, follicular prominence | Pityriasis rubra pilaris |
| **Lymphadenopathy**, severe unrelenting itch, a long prodrome of eczema that was never quite eczema, circulating atypical lymphocytes | Cutaneous T-cell lymphoma including Sézary syndrome — the cause most often diagnosed late |
| **Timing against a new medicine**, facial oedema, fever, eosinophilia, organ involvement | Drug reaction. m054's territory, and its thresholds for concern are deliberately low |
| **Flexural emphasis earlier in the course**, lichenification | Eczema. m051's territory |
| **Heavy crusting**, immunosuppression, an institutional setting | Crusted scabies, where the treatment is wholly different and immunosuppression is the wrong move. m086's territory |
| **A red, scaling, unwell newborn** | A different differential entirely — inherited ichthyoses, immunodeficiency, metabolic causes — and a paediatric emergency |

**Erythroderma** is erythema with scaling affecting most of the skin surface. (**definitional**)
It is conventionally defined with a body-surface percentage; that figure is in the documents named
below and is **not reproduced here**, following m089's handling of the detachment thresholds. It
is a syndrome with a differential rather than a diagnosis, and a substantial proportion remain
idiopathic after full assessment — some declaring a cause years later. (**consensus**)

Histology is frequently non-specific, the yield is better from several sites, and repeating it
later is a recognised strategy rather than an admission of failure. (**consensus**) Why that is,
and what the sampling decision actually determines, is m120's argument.

## Four of the nine sinks are not drawn on the screen

One more borrowed device, because it carries the monitoring argument exactly. m102 counted **nine
end-of-turn HP sinks held in five stores**, each with its own purpose-built jump instruction,
while `UpdateStatusIconInHealthbox` reads `MON_DATA_STATUS` only and draws five graphics — so four
of the nine are costing HP every turn with nothing on screen to say so.

That is the monitoring list in skin failure, and every item on it is on the list because a
numbered function above is failing silently. (**mechanism**)

* **Temperature**, because the failure direction is counterintuitive and a warm ambient
  environment is treatment rather than comfort.
* **Fluid balance and electrolytes**, because the loss is insensible and therefore absent from the
  chart unless someone accounts for it. What a fluid balance chart does and does not measure is
  m005's argument and it applies here with force.
* **Albumin and nutritional assessment**, because the protein drain is continuous.
* **Circulation**, because the high-output state is a mechanism and pre-existing cardiac disease
  is what makes it dangerous.
* **Infection surveillance**, with m055's discipline about colonisation held against the fact that
  the portal here is enormous.
* **The medicines list**, in both directions: a culprit to stop, and altered absorption of
  anything applied.

And the management principle, at the level of principle only; no agent, dose, strength, regimen,
fluid volume or temperature target appears anywhere in this answer. **Supportive care is the
treatment that keeps someone alive while the cause is identified, and it is not a holding
measure.** Warmth, fluid and electrolyte replacement, nutritional support, bland emollient care
over the whole surface, meticulous handling to reduce shear, pressure-area care, infection
surveillance. In extensive disease this is recognisably the list used after a burn of similar
extent, and in several countries such cases are managed in or alongside a burns or specialist
dermatology inpatient unit for that reason. (**country-dependent**) Two cautions are standard:
systemic corticosteroid can precipitate severe deterioration in erythrodermic psoriasis, and
immunosuppression given before an infective or infestive cause is excluded can be harmful, crusted
scabies being the well-described case. (**consensus**)

## Where the metaphor stops

No Pokémon in this answer stands in for a person, and nothing above maps a battler to a patient.
The whole device is deliberately the one structure in the five that has **no owner** — field
weather belongs to neither side — which is why it is the one that can carry this subject at all. A
global `u16` is not a body. That was the point of choosing it.

Three things need saying without ornament, and the first is the reason the analogy had to be put
down here rather than stretched.

**Erythroderma from any cause carries real mortality**, and the deaths come predominantly from the
mechanisms set out above — infection with the skin as the portal, cardiovascular decompensation,
metabolic and fluid derangement — rather than from the skin disease itself. Nothing in this answer
can say what will happen to any particular person; that belongs with the team who have the
findings. The framing exists because treating this as a severe rash over a large area rather than
as organ failure has a known and avoidable cost, and that deserves to be said without hedging.

**The experience is harder than the physiology suggests.** Itch in erythroderma is frequently
severe and unrelenting, and in the lymphoma-associated forms it is often the dominant symptom and
the hardest to relieve. Shivering while feeling hot is distressing and is routinely misread by
everyone present, including the person. Being cold, repeatedly exposed for examination, handled
often, unable to sleep, and visibly changed from head to foot is a cumulative burden that no
observation chart records. The appearance is frightening to have and frightening for family to
see.

**And three things follow for anyone doing this work.** Warmth and minimal handling are clinical
interventions and should be prescribed and recorded as such, not left to whoever is in the room.
Itch and discomfort need addressing actively and by people with the relevant expertise; treating
them as secondary to the physiology is a mistake rather than a prioritisation. And when no cause
is found — which happens, and persists in a meaningful proportion — saying so plainly, together
with what the plan is anyway, is better than an implied diagnosis that later changes.

Nothing here is for any reader's own use and no treatment named or implied is a recommendation.
Widespread redness of the skin with shivering, fever, feeling unwell, or redness beginning after a
new medicine, is a medical emergency needing assessment the same day — call your local emergency
number or use your local urgent care route. A red, scaling, unwell newborn or infant is a
paediatric emergency.

## What a Gym Leader is listening for

The six functions, and the systemic consequence of each one failing. Why hypothermia rather than
hyperthermia is the characteristic thermoregulatory failure, and when that reverses. The mechanism
of the high-output circulatory state. Where the protein goes. Why percutaneous absorption rises
and what that changes. What erythroderma is definitionally, and why it is a syndrome and not a
diagnosis. The causes and the one feature that points to each. Where the original disease stays
legible after generalisation. The two routes into the same field state, and which one has a clock.
Why the biopsy is often non-specific and what is done about it. Which two treatments can make
things worse before the cause is known. And why supportive care is the treatment rather than the
waiting room.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For the definition of erythroderma including the body-surface figure, the differential and the
  assessment: a current standard textbook of dermatology and the specialist guidance of your
  national dermatology body. The percentage is there and is deliberately not reproduced above.
* For the inpatient management of extensive skin failure — fluid and electrolyte replacement,
  nutrition, ambient temperature, handling, and criteria for admission to a specialist or burns
  unit: your local dermatology inpatient protocol and your regional burns service's referral
  criteria. These differ substantially by country and by institution.
* For erythrodermic and generalised pustular psoriasis, and the hazard of abrupt systemic
  corticosteroid withdrawal: your national psoriasis guidance, as m052's sources.
* For severe drug reactions and their management pathway: as m054's sources.
* For cutaneous T-cell lymphoma and Sézary syndrome: your national guidance on cutaneous lymphoma
  and your regional specialist service.
* For crusted scabies including contacts and institutional outbreaks: your national public health
  body's guidance, as m086's sources.
* For erythroderma in the neonate and infant: your national paediatric dermatology service.
* For anything applied to a large broken area, and for the altered absorption: your national
  formulary.

The Pokémon claims were checked separately against source. `gBattleWeather` being a single global
`u16` belonging to neither battler and untouched by `SwitchInClearSetData`;
`B_WEATHER_SANDSTORM_TEMPORARY` and `B_WEATHER_SANDSTORM_PERMANENT` being bits 3 and 4 of that
field with `B_WEATHER_SANDSTORM` defined as their union; `Cmd_setsandstorm` assigning the
temporary bit and setting `gWishFutureKnock.weatherDuration = 5`; Sand Stream, Drizzle and Drought
each assigning the permanent bit on switch-in; the end-of-turn guard being `if (!(gBattleWeather &
B_WEATHER_SANDSTORM_PERMANENT) && --gWishFutureKnock.weatherDuration == 0)`, so the decrement is
short-circuited away when the permanent bit is set; `Cmd_weatherdamage` billing `maxHP / 16` with
a floor of 1 and exempting a battler whose first or second type is Rock, Steel or Ground, or whose
ability is Sand Veil, or which is underground or underwater, with Hail's exemption being Ice type
only; the absence of any Special Defence boost for Rock types anywhere in that function, that
boost being a fourth-generation addition; and `WEATHER_HAS_EFFECT` being defined as
`!ABILITY_ON_FIELD(ABILITY_CLOUD_NINE) && !ABILITY_ON_FIELD(ABILITY_AIR_LOCK)`; Sand Stream
belonging to Tyranitar alone, Drizzle to Kyogre alone, Drought to Groudon alone, Cloud Nine to
Psyduck and Golduck only and Air Lock to Rayquaza only; Quagsire's two abilities being Damp and
Water Absorb rather than Cloud Nine; and Tyranitar being Rock/Dark, Steelix Steel/Ground, Aggron
Steel/Rock, Glalie pure Ice, and Sand Veil being held by Sandshrew, Sandslash, Diglett, Dugtrio,
Gligar, Cacnea and Cacturne — all from the pret decompilation of Pokémon Emerald, the species
facts read from the species information table rather than recalled. Sandstorm and Leftovers
sharing the `maxHP / 16` denominator is m055's observation from the same source, and the
nine-sinks-in-five-stores count is m102's.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No agent, dose, regimen, fluid volume, temperature target, body-surface-area threshold or
severity score appears in this answer, and none of it addresses any reader's own treatment.** The
omission of the body-surface figure from the definition of erythroderma is deliberate and follows
m089's handling of the detachment thresholds.

Widespread redness of the skin accompanied by shivering, fever, feeling unwell, or beginning after
a new medicine, is a medical emergency and needs assessment the same day. A red, scaling, unwell
newborn or infant is a paediatric emergency. Call your local emergency number or use your local
urgent care route.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The physiology is settled and is the part worth memorising: six functions, and the systemic
consequence of each failing. The hypothermia point is settled and still routinely got wrong. The
differential is settled, as is the observation that a substantial proportion remain idiopathic
after full assessment.

What moves is the specific treatment of each cause, and in two places the organisation of care.
Biologic and small-molecule therapy has changed the management of erythrodermic psoriasis and of
severe eczema in several countries, shortening some of these admissions; availability and funding
are firmly (**country-dependent**). Treatment of Sézary syndrome and advanced cutaneous lymphoma
has moved with targeted agents and the pathways differ by country. The framing of extensive skin
loss as organ failure needing critical-care-adjacent or burns-adjacent management has gained
ground rather than being settled, and where these patients are physically managed differs markedly
between health systems — the part of this answer most likely to read differently depending on
where you practise. The term "skin failure" itself is still contested in the literature, though
what it denotes is not. Current as of October 2026.
