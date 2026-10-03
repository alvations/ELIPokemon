---
id: "m145"
slug: lipids-as-a-risk-factor-not-a-disease
style: pokemon
category: endocrinology
difficulty: advanced
question: "A lipid panel is a risk factor rather than a disease. What does that change about treating the number?"
tags: [lipids, cardiovascular-risk, apolipoprotein-b, familial-hypercholesterolaemia, absolute-risk]
---

# Nothing in CalculateBaseDamage is the damage, and a Choice Band's ×150÷100 is worth a great deal against one target and almost nothing against another

`CalculateBaseDamage` in the Advance source is the right object for this answer because it is
**nothing but a chain of multiplications**, and no line in it is the damage. Read the chain in the
order the code applies it:

```
   attack = attacker->attack                       ← from base stat, IVs, EVs, level
   if (ability == HUGE_POWER || PURE_POWER)   attack *= 2
   if (ShouldGetStatBadgeBoost(FLAG_BADGE01_GET))  attack = (110 * attack) / 100
   type-matching hold item                         attack = attack * (param + 100) / 100
   if (holdEffect == CHOICE_BAND)                  attack = (150 * attack) / 100
   if (THICK_CLUB && species is CUBONE or MAROWAK)  attack *= 2
   if (LIGHT_BALL && species is PIKACHU)            spAttack *= 2
   if (METAL_POWDER && defender is DITTO)           defense *= 2
   if (DEEP_SEA_TOOTH && species is CLAMPERL)       spAttack *= 2
   ...then the level-and-power term, then Reflect or Light Screen in whichever
   of the two branches the move's category selects, then type effectiveness,
   then STAB at ×1.5, then a critical hit, then a damage roll of 85-100%
```

Fourteen-odd factors, each a one-line conditional, and **the output is a product**
(**mechanism**). Change exactly one of them and you change the product by that one factor. The
same factor removes a large absolute amount from a large product and a small absolute amount from
a small one, and nothing about the factor has changed between those two cases.

That is the whole of this answer, and the arithmetic is the argument rather than an illustration
of it.

| In the battle | What it stands for |
| --- | --- |
| `CalculateBaseDamage`, a chain of multiplications | Risk as a product of several terms |
| A **Choice Band**'s `(150 * attack) / 100` | One modifiable term, contributing a factor |
| The same **Choice Band** against two different targets | Relative effect constant, absolute effect not |
| **Earthquake** into a **Flygon** with **Levitate** | A factor multiplied by zero, which no amount fixes |
| **Sandstorm**'s `maxHP / 16`, every turn, to everybody not exempt | Continuous exposure, invisible per turn |
| One **Sand Stream** on one **Tyranitar**, for the whole field | A single upstream term, set once, affecting everyone present |
| The **Leftovers** sixteenth, the same denominator with the sign flipped | Why the pair cancel, and why neither is noticeable |
| A **Base Stat**, fixed by species and movable by nothing | A term in the product that no intervention touches |
| **Huge Power** on an **Azumarill**: `attack *= 2`, applied **first** | A monogenic condition: standing, early, before every modifier |
| `abilities = {ABILITY_THICK_FAT, ABILITY_HUGE_POWER}` | Two slots in one species, decided per individual |
| An Ability recorded only when it fires | Why the condition is underdiagnosed |
| An **Egg Move** against **Sketch** | Transmitted between generations, not acquired in the battle |
| `bodyColor`, read **only** by `DoPokedexSearch` | A field that correlates with everything and causes nothing |
| **Magikarp**, `BODY_COLOR_RED`, a pure Water type | The counterexample that shows the correlation is not the mechanism |
| The **Damage Roll** at 85 to 100 per cent | An estimate is not what happened |
| The **Type Chart**, in the cartridge, shown nowhere | A decision aid is information moved forward, not new information |

**This answer defers to five others.** m007 owns type effectiveness as a zero. m023 owns the
argument that a threshold is not a property of the molecule. m055 owns the game recording an
opponent's Ability only when it fires. m083 owns the chart being in the cartridge and nothing
showing it. m085 owns **Sandstorm** as **Leftovers** with the sign reversed and the prevention
paradox it carries. None is re-argued.

Clinical claims are marked (**mechanism**), (**definitional**), (**consensus**) or
(**country-dependent**). The Pokémon mechanics carry no clinical marker; the Sources section says
where each was read.

## The product, drawn, and why identical values diverge

```
   TWO BATTLERS. SAME CHOICE BAND. SAME ×150÷100.

   ── battler A ───────────────────────┐   ── battler B ────────────────────┐
   base-and-level term       LARGE     │   base-and-level term      small   │
   × Huge Power               ×2       │   × Huge Power              ×1     │
   × type effectiveness       ×2       │   × type effectiveness      ×1     │
   × STAB                     ×1.5     │   × STAB                    ×1     │
   × Choice Band              ×1.5  ◄──┼── the SAME factor ──────────►×1.5  │
   × Reflect                  —        │   × Reflect                 ×0.5   │
   ────────────────────────────────────┘   ─────────────────────────────────┘
        product: a great deal                 product: very little

   REMOVE the Choice Band from each. Battler A loses a third of a large
   number. Battler B loses a third of a small one. The factor was identical.
   The thing that differed was EVERYTHING ELSE.

   ── and the term that is usually the biggest is the one nobody chose ──
   `level` enters the base term directly and multiplies everything after it.
   In the real estimate, age is the term that behaves like level.

   ── AND THE EDGE CASE ──
   Earthquake into Flygon: TYPE_MUL_NO_EFFECT. The product is zero. Stack
   a Choice Band, a Thick Club and six stages of Attack on top and it is
   still zero, because a factor multiplied by nothing is nothing.
```

Three readings of that picture, all of them (**mechanism**).

**The same factor, two different absolute quantities.** This is relative against absolute risk
reduction stated as arithmetic rather than as statistics. Lowering the causal particle
concentration reduces risk by approximately a proportion, reasonably consistently; the absolute
benefit is that proportion times the person's untreated risk (**consensus**). Both descriptions
are true of the same multiplication.

**The biggest term is usually the one nobody chose.** `level` enters the base term and multiplies
everything downstream of it, and in every commonly used risk model age carries more weight than
the lipid value (**consensus**). Which is why two people with identical panels correctly receive
different recommendations: the lipid term is one factor and the product differs.

**And the lipid value gets treated as the target because it is the lever.** Of all those
conditionals, a **Choice Band** is the one you can take off. You cannot take off the level. Of the
terms in a real risk estimate, the lipid value is one of the few that moves substantially and
measures easily — and a lever that moves is easy to mistake for a destination.

The zero case is m007's and it belongs here as the limit of the whole picture. **Earthquake** into
a **Flygon** is `TYPE_MUL_NO_EFFECT`, and no amount of improvement in any other factor crosses it
(**mechanism**). It is the reminder that a product is a product: terms do not add, so one of them
being absent is not a partial result.

## Sandstorm is the exposure, and nobody notices any single turn

Generation III's `Cmd_weatherdamage` is four lines of arithmetic and it is exact:

```
   if (gBattleWeather & B_WEATHER_SANDSTORM)
       if (neither type is ROCK, STEEL or GROUND
           && ability != ABILITY_SAND_VEIL
           && not STATUS3_UNDERGROUND && not STATUS3_UNDERWATER)
               gBattleMoveDamage = maxHP / 16;   with a floor of 1
```

A sixteenth of maximum HP, at the end of every turn, to everybody on the field who is not exempt
(**mechanism**). It is the same denominator as **Leftovers**, which is why the two cancel exactly
— m085 put that as **Sandstorm** being **Leftovers** with the sign reversed, and the observation
does a second job here.

**Nobody notices one turn of it.** A sixteenth is a sliver. What matters is the sum over however
many turns the weather runs, and the sum is the thing that decides the battle. That is cumulative
exposure: the mechanism in the arterial wall is retention of particles over time, so the
accumulated burden is concentration multiplied by duration and a single lipid measurement is a
sample of the **height** of that exposure at one instant (**mechanism**). The strongest evidence
in the area is about the duration term: conditions that raise the causal particle concentration
from birth produce clinical disease decades earlier than the same concentration arriving in
midlife (**consensus**).

Two further properties of the sandstorm make it the right device rather than merely an adequate
one.

**It is set once, upstream, for everybody.** One **Tyranitar** with **Sand Stream** sets it on
entry and it applies to every battler present, including its own side. A single upstream term
producing a small cost to a large number of people is the prevention paradox exactly, which m085
argues and this answer does not.

**And its effect depends on a macro written as an absence.** `WEATHER_HAS_EFFECT` is defined in
terms of there being no **Air Lock** on a **Rayquaza** and no **Cloud Nine** on a **Psyduck** or
**Golduck** anywhere on the field — the weather bit stays set and nothing reads it
(**mechanism**). m052 made that point in dermatology. Here it is the reminder that an exposure
term can be present in the data and contributing nothing, which is the next section's subject from
the other side.

## Body Color is in the data, correlates beautifully, and causes nothing

This is the best thing the cartridge has for association against causation, and it is verifiable
in two greps.

`bodyColor` is a field in `gSpeciesInfo`, one per species. It is read in **exactly one place in
the whole source**: `DoPokedexSearch`, which compares it when somebody searches the **Pokédex** by
colour. Nothing in `CalculateBaseDamage` reads it. Nothing in `battle_util.c` reads it. Nothing in
`pokemon.c` reads it (**mechanism**).

And it **correlates**. **Gyarados** is `BODY_COLOR_BLUE`. So is **Lapras**. So is **Wailord**. So
is **Azumarill**. Search the **Pokédex** for blue and you will pull out a great many Water types,
and a classifier built on **Body Color** would predict typing better than chance. Then
**Magikarp** is `BODY_COLOR_RED` and is a pure Water type, and **Charizard** is `BODY_COLOR_RED`
and is Fire — the correlation was real, the exceptions are real, and the field enters no
calculation anywhere (**mechanism**).

So: a term that predicts, and that intervening on would change nothing, because it is not in the
formula. Painting a **Magikarp** blue does not alter one point of damage.

That is high-density lipoprotein cholesterol, and it is the cleanest example in cardiovascular
medicine. The inverse association with risk is robust, long-observed and reproducible.
Interventions that raise it pharmacologically have not produced the risk reduction the association
predicted, and genetic variants that raise it are not associated with the lower risk a causal
relationship would require (**consensus**). It behaves as a marker — of metabolic state, of
particle handling, of things correlated with both — rather than as a cause available to be acted
on.

The useful generalisation, and the reason this is worth learning in the clinical setting rather
than in a statistics course: **a term can earn its place in a prediction model without being a
target.** `bodyColor` earns its place in `DoPokedexSearch`. It has no place in the damage formula.
Those are two different jobs and the field is good at one of them.

Two neighbours behave differently and deserve a line each. **Lipoprotein(a)** is largely
genetically determined and not meaningfully moved by lifestyle, which in this metaphor makes it a
**Base Stat** — in the product, multiplying, and not touched by any item in the bag
(**consensus**); whether and in whom it is measured differs markedly by country
(**country-dependent**). And triglycerides are partly a marker of remnant particles, which are
themselves causal, so they are not noise — while **very** high triglycerides are a different
problem carrying a risk of pancreatitis, which is a disease rather than a risk term and gets no
mechanic here (**consensus**).

## Huge Power is applied first, and it is in the species data

Now the exception, and it is the most important section.

```
   if (attacker->ability == ABILITY_HUGE_POWER || attacker->ability == ABILITY_PURE_POWER)
       attack *= 2;
```

That line sits **above** every badge boost, every type-matching item, the **Choice Band**, the
**Thick Club** and everything else in the chain (**mechanism**). It is not a modifier somebody
applied during the battle. It is a property of the species data — `[SPECIES_AZUMARILL]` carries
`abilities = {ABILITY_THICK_FAT, ABILITY_HUGE_POWER}` — and it has been true since the
**Azumarill** was created.

Four consequences, and they are the four clinical facts about familial hypercholesterolaemia.

**An estimate computed without reading the ability field is wrong by a factor of two, and the
arithmetic is fine.** **Azumarill**'s base Attack is **50**, which is unremarkable, and work out
its damage from its base stats and you will be out by half. A general-population risk model — in
which age carries the most weight — returns a low estimate for a young adult with this monogenic
condition and is badly wrong, because the term that governs their case is not one of its inputs
(**mechanism**). Using such a model there is a named error, not an approximation (**consensus**).

**The condition is in the species and not in the battle.** m045's distinction is the frame:
**Sketch** copies a move horizontally, inside one encounter, and an **Egg Move** arrives
vertically, from the generation before. **Huge Power** is in the species data. It is the vertical
one, and it is the reason the highest-yield act after this diagnosis is testing the relatives —
the condition is inherited in an autosomal dominant pattern, so each first-degree relative has a
substantial prior probability and systematic cascade testing finds affected people who had no
reason to be looked at (**mechanism**, **consensus**).

**But it is not certain in a relative**, and the data says so rather better than a hedge would.
**Azumarill** has **two** ability slots and **Thick Fat** is the other one. Which an individual
**Azumarill** has is decided per individual and is nowhere on the sprite. A relative has a prior
probability, not a diagnosis, and the testing is what converts one into the other.

**And it is underdiagnosed for a reason that is in the code.** m055 found it in dermatology: the
game records an opponent's Ability **only when it fires**. Until **Huge Power** does something
visible, nothing in the battle tells you it is there. The condition is usually asymptomatic until
it is not, and the lipid value is easy to read as "a bit high" rather than as a diagnostic finding
(**consensus**).

Which diagnostic criteria are used, whether genetic testing is involved and how cascade testing is
organised and funded all differ between countries, several sets of criteria exist and they
disagree, and **no criteria and no values appear here** (**country-dependent**).

## The roll, and the chart

Two short ones to close the arithmetic honestly.

**An estimate is not an outcome.** The final step of the damage calculation is a roll of 85 to 100
per cent of the computed figure (**mechanism**). The computation can be exactly right and the
number that lands is still one draw. A risk estimate is a statement about a reference population
with somebody's characteristics, not a measurement of them — and a model is an equation fitted to
a particular population over a particular period, calibrating poorly outside it, with several in
use that take different inputs and produce different outputs (**country-dependent**).

**And the chart was always in the cartridge.** m083 made this point in general practice: the type
chart is in the data, nothing in the battle menu shows it, and looking it up is **information
moved forward rather than new information** (**mechanism**). A risk calculator is exactly that. It
does not measure anything. It arranges what was already in the record into a form a decision can
be made on, and the thing it mostly reveals is how much of the product was age all along.

## The mapping I am declining

Three refusals.

**No Pokémon here stands in for a person, and nothing stands in for an event.** This topic's
outcomes are cardiac and they are the kind of thing `SAFETY.md` fences off, so the metaphor stays
on the **formula**: a chain of conditionals in `CalculateBaseDamage`, a sixteenth a turn from a
field condition, and a field in the species data that nothing reads. Plaque gets no mechanic, an
infarct gets no mechanic, and the picture stops at the arithmetic of a product.

**I am not using the badge boost, although it is right there.** `ShouldGetStatBadgeBoost` appears
three times in this very function, and m050 in general practice has worked the ×110/100 relative
multiplier at length as an advantage awarded for having already won. Pulling it in here would be
the second borrowed argument in one paragraph doing a job the **Choice Band** already does, and a
forced reuse teaches a false equivalence. One modifiable factor is enough to carry the
relative-against-absolute point; a second would be decoration. (It did turn up a correction to the
conventions file, which is in my hand-back rather than here.)

**And I am not building a fifth terrain, or reaching for the weather layer, for a lipid.** A lipid
is not a hormone and it does not sit at a regulated level — that is the entire point of the
answer. Weather in this specialty is the glucose-control hormones and terrain is the axis
hormones, and a risk factor belongs to neither: it is a **factor in a product** and a **sixteenth
a turn**, which is why this answer lives in the damage formula and in `Cmd_weatherdamage`'s
arithmetic rather than in the field-condition vocabulary. **Sandstorm** is used here for its
denominator and its reach, not as a hormone. m094 declined to invent a terrain it did not need and
this answer declines to borrow one it does not fit.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a product of factors, of a small continuous cost whose sum is
what matters, of a data field that predicts beautifully and causes nothing, and of a standing
property applied before every modifier. The picture is fair, and the conclusion it supports is the
right one: a lipid value is one term in an estimate and it is not a disease.

Here is what the picture cannot carry.

The commonest harm in this area is not a side effect. It is a conversation that leaves somebody
believing they have a disease they do not have, or believing they do not have one they do.

Being told a cholesterol result is high, with no context about the other terms, hands a person a
number and no way to read it. Some are frightened by a finding that in their circumstances means
very little. Others are reassured by a result described as borderline when the thing that actually
matters about them is a family history of early cardiac death. Both are failures of explanation
and both are avoidable.

The reverse harm is specific and serious. A young adult with familial hypercholesterolaemia may be
told repeatedly that their risk score is low — which is true of the score and wrong about them.
People in this situation sometimes find out when a relative dies young. If one thing survives this
answer it should be that a markedly raised value in a young person with a family history of early
cardiac disease is not a slightly worse version of a common finding.

And there is a social weight here that no arithmetic reaches. Cholesterol has been an object of
public moralising for decades, so a raised result often arrives attached to an implied verdict
about how somebody eats. Lipid handling is substantially genetic, and the largest term in most
risk estimates is age, which nobody chose. A consultation that treats the number as evidence about
a person's discipline is factually wrong and reliably counterproductive.

A note about who is reading. Anybody reading about this is more likely to have had a cholesterol
result than to be sitting an examination. If that is you: there are deliberately no numbers,
targets or thresholds anywhere on this page to compare yours against, because a lipid value means
something only alongside your age, your blood pressure, your smoking history, your family history
and the rest — and that reading belongs to the clinician who ordered it, not to an analogy about
damage formulas. If there is early heart disease in your family, that is specifically worth
raising with them, because it changes what your own result means. And nothing here is about any
medicine you may have been offered.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national guidance on cardiovascular risk assessment and lipid management, for which risk
  model is recommended, its derivation population, the thresholds at which action is advised and
  what is offered.
* **The risk model used where you work**, specifically its derivation population and period, and
  any guidance on populations in which it calibrates poorly. A model applied outside its
  derivation population is the commonest quiet error here.
* **Your national formulary**, for anything about a lipid-lowering medicine. No agents are named
  here and the formulary is the authority.
* Your national or specialty-society guidance on familial hypercholesterolaemia, for the
  diagnostic criteria used, the role of genetic testing, and how cascade testing of relatives is
  organised and funded.
* Your national or specialty-society guidance on lipoprotein(a), for whether, when and in whom it
  is measured.
* **The primary literature**, for the genetic and trial evidence on high-density lipoprotein
  cholesterol as a non-causal marker, for the lifetime-exposure evidence, and for the
  proportional-against-absolute benefit relationship.
* A current textbook of lipidology or vascular biology, for the retention-and-modification
  mechanism, the structure of apolipoprotein-B-containing particles, and the clearance pathway
  affected in familial hypercholesterolaemia.

The Pokémon side is different and is sourced properly. `CalculateBaseDamage` in `src/pokemon.c`
applying `attack *= 2` for `ABILITY_HUGE_POWER` or `ABILITY_PURE_POWER` **before**
`ShouldGetStatBadgeBoost`, the type-matching hold-item multiplier, the **Choice Band**'s `(150 *
attack) / 100`, the **Thick Club** on **Cubone** and **Marowak**, the **Light Ball** on
**Pikachu**, **Metal Powder** on **Ditto**, the **Deep Sea Tooth** and **Deep Sea Scale** on
**Clamperl** and the **Soul Dew** on **Latias** and **Latios**; `[SPECIES_AZUMARILL]` carrying
`abilities = {ABILITY_THICK_FAT, ABILITY_HUGE_POWER}` with a base Attack of **50**, and **Marill**
carrying the same two abilities; **Tyranitar** being Rock and Dark with `ABILITY_SAND_STREAM` in
its first slot and nothing in its second; `Cmd_weatherdamage` computing `maxHP / 16` with a floor
of 1 and exempting Rock, Steel and Ground types, `ABILITY_SAND_VEIL`, and the underground and
underwater states, all behind `WEATHER_HAS_EFFECT`; `bodyColor` existing in `gSpeciesInfo` and
being read only by `DoPokedexSearch`, with **Gyarados**, **Lapras**, **Wailord** and **Azumarill**
blue, **Magikarp** `BODY_COLOR_RED` and a pure Water type, and **Charizard** red and Fire; and
**Flygon** being Ground and Dragon with `abilities = {ABILITY_LEVITATE, ABILITY_LEVITATE}` were
all read from the pokeemerald decompilation rather than from memory. Two cautions, both
deliberate. Generation III **Sandstorm** gives Rock types **no** Special Defence boost — that is a
Generation IV change and `Cmd_weatherdamage` contains no such line — and **Magic Guard** is absent
from its exemption list because **Magic Guard** is a Generation IV ability. The damage roll of 85
to 100 per cent and the ordering of the modifier chain are Advance-era specifics and the chain has
been reorganised in later generations.

## Scope and safety

The Pokémon here is doing one job: making it concrete that a product of factors behaves
differently from a sum, that the same factor is worth different absolute amounts against different
products, that a small continuous cost is read as its integral, and that a field which predicts
well can be absent from the formula entirely. It is not a clinical reference, not a decision aid,
not advice about anybody's cholesterol, and not about any individual's care. **No lipid values,
targets, thresholds, risk-score outputs, percentage risk reductions, numbers needed to treat,
diagnostic criteria or drug names appear here on purpose** — a number lifted from this page and
compared against somebody's own result would be the exact misuse this answer argues against. Check
your own national guidance and your national formulary. Nothing here has had clinical review. No
Pokémon in this answer stands in for a person, a plaque or an event, and a family history of early
cardiac disease materially changes what a lipid result means and is a matter for a clinician.

## What a Gym Leader digs into next

* Why is it load-bearing that `CalculateBaseDamage` multiplies rather than adds?
* Why is the same **Choice Band** worth a great deal to one battler and almost nothing to another,
  and which clinical distinction is that?
* Why is `level` the term that behaves like age, and why does that resolve the identical-panels
  puzzle?
* Why does **Earthquake** into a **Flygon** stay at zero no matter what else you stack?
* Why does one turn of **Sandstorm** tell you nothing and the sum of them decide the battle?
* Why is one **Sand Stream** on one **Tyranitar** the prevention paradox?
* Why does `bodyColor` being read only by `DoPokedexSearch` settle the
  association-against-causation question?
* Why is **Magikarp** the species that makes that argument rather than breaking it?
* Why does **Huge Power** being applied *first* matter more than its being a doubling?
* Why does **Azumarill** having two ability slots make it the right model for testing a relative?

## Where this stands, October 2026

The multiplicative structure of risk estimation and what it implies about identical values in
different people, the proportional-against-absolute relationship, the retention mechanism and the
lifetime-integral nature of the exposure, the non-causal status of high-density lipoprotein
cholesterol, and the categorical difference between a risk factor and a monogenic disorder are
settled and do not date. What dates on the Pokémon side is the chain and the constants: the
modifier order in `CalculateBaseDamage`, the 85-to-100 damage roll, the species-specific item
doublings and the badge-boost calls are Advance-era specifics and the calculation has been
restructured in later generations; **Sandstorm**'s exemption list gained **Magic Guard** in
Generation IV and Rock types gained a Special Defence boost in the same generation, neither of
which is in the Generation III function; and `bodyColor`'s single reader is a property of this
source rather than a permanent fact. On the clinical side everything operational moves: which risk
model is recommended and where it is trusted, every threshold and target, which agents are used
and in what order — this has changed substantially in recent years and continues to — fasting
against non-fasting sampling, whether apolipoprotein B or lipoprotein(a) is measured routinely,
the diagnostic criteria for familial hypercholesterolaemia, and how cascade testing is organised
and funded. Check current local guidance and your national formulary.
