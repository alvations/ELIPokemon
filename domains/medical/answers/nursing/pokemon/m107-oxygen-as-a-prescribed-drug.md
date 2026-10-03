---
id: "m107"
slug: oxygen-as-a-prescribed-drug
style: pokemon
category: nursing
difficulty: intermediate
question: "Why is oxygen treated as a drug that is prescribed and titrated to a target range rather than as something simply given?"
tags: [oxygen, titration, hypoxaemia, prescribing, monitoring]
---

# Eight weather bits in one `u16`, and not one of them is a dose.

```
   #define B_WEATHER_RAIN_TEMPORARY      (1 << 0)
   #define B_WEATHER_RAIN_DOWNPOUR       (1 << 1)  // unused
   #define B_WEATHER_RAIN_PERMANENT      (1 << 2)
   #define B_WEATHER_SANDSTORM_TEMPORARY (1 << 3)
   #define B_WEATHER_SANDSTORM_PERMANENT (1 << 4)
   #define B_WEATHER_SUN_TEMPORARY       (1 << 5)
   #define B_WEATHER_SUN_PERMANENT       (1 << 6)
   #define B_WEATHER_HAIL_TEMPORARY      (1 << 7)
   ──────────────────────────────────────────────────────────────────────────────────────────
   That is the entire field layer of the third generation. Four phenomena, eight bits, and
   the only axis any of them has is PRESENT or ABSENT. There is no "half rain". The second
   bit is carried in the header with the comment `// unused`, and the only place anything
   reads it is `ENDTURN_RAIN`, to choose which continuation message to print.
```

Start there, because it is the place the analogy breaks and the break is the point. Oxygen's whole
difficulty is the intensity axis — the quantity that has a floor *and* a ceiling — and the games
have no intensity axis at all. Everything the field layer *does* model is still worth having,
because four of the five decisions in an oxygen prescription are in here and modelled well. The
dose is the one that is not, and naming that in the body rather than at the end is the honest
version.

Markers used below, because this half carries clinical claims. (**mechanism**) follows from
physiology; (**consensus**) is mainstream agreement across major guidance; (**country-dependent**)
means the reader's own guidance decides. Code blocks are from the Emerald decompilation and carry
no marker.

## One setter, one field, everybody present

`Rain Dance` does not do anything to a battler. It writes `gBattleWeather`, a single global, and
from that moment every damage calculation in the battle reads it — for both sides, for every
species, for the rest of the clock. That asymmetry between **a state of the room** and **a
treatment given to a person** is the first thing an oxygen prescription has to get right, and the
reason a prescription names a person and a target rather than a wall socket. (**mechanism**)

## The same field, opposite signs, and the sign belongs to the recipient

```
   // src/pokemon.c, inside CalculateBaseDamage
   if (gBattleWeather & B_WEATHER_RAIN_TEMPORARY)
   {
       switch (type)
       {
       case TYPE_FIRE:  damage /= 2;              break;
       case TYPE_WATER: damage = (15 * damage) / 10; break;
       }
   }
   ──────────────────────────────────────────────────────────────────────────────────────────
   One field state. Exactly ×0.5 and exactly ×1.5, in the same switch, four lines apart.
   `B_WEATHER_SUN` a few lines below is the mirror image. And `Solar Beam` is halved by ANY
   weather that is not sun — a third sign, on one named move, from the same global.
```

So the question "is rain good?" has no answer: it has a different answer for **Ludicolo**, which
is Water/Grass and holds **Swift Swim** or **Rain Dish**, than it has for **Torkoal**, which is
pure Fire. The field is identical; the sign is a property of the recipient's own type, which is
fixed in the species table before the battle begins.

That is the clinical structure of the upper edge, and it is why there are two standing target
ranges rather than one. In a person with chronic hypercapnic respiratory failure, a high inspired
concentration can produce a rising carbon dioxide and a respiratory acidosis — by loss of the
hypoxic contribution to ventilatory drive, by reversal of hypoxic pulmonary vasoconstriction
worsening ventilation–perfusion matching, and by the Haldane effect, with the last two probably
the larger terms. (**consensus**, **mechanism**) Same intervention, opposite sign, and which sign
you get is a property of the person. The ranges themselves are (**country-dependent**).

**Castform** is the limiting case and it belongs here. `CastformDataTypeChange` rewrites the
battler's own type from the field — `SET_BATTLER_TYPE(battler, TYPE_WATER)` under rain,
`TYPE_FIRE` under sun, `TYPE_ICE` under hail, and back to `TYPE_NORMAL` when none of the three is
up. The recipient's response to the field is itself changed by the field. m096 uses the same
routine as the reversible counterpart to an irreversible change; here it is simply the reason the
sign cannot be read off the prescription.

## No benefit at all for someone already in range

```
   case ABILITY_RAIN_DISH:
       if (WEATHER_HAS_EFFECT && (gBattleWeather & B_WEATHER_RAIN)
        && gBattleMons[battler].maxHP > gBattleMons[battler].hp)
       {
           ...
           gBattleMoveDamage = gBattleMons[battler].maxHP / 16;
   ──────────────────────────────────────────────────────────────────────────────────────────
   Three conditions, and the third is the one to read. At full HP the ability does not fire
   at all — not a smaller amount, nothing. The rain is still falling. The holder still has
   the ability. The benefit is simply unavailable, because there is no deficit to correct.
```

That is the floor of the therapeutic window stated as code, and it is the reason the indication is
hypoxaemia rather than breathlessness. Oxygen corrects a deficit; where there is no deficit there
is nothing for it to do, and the trials comparing oxygen with air in non-hypoxaemic breathlessness
do not support a symptomatic benefit beyond that of air. (**consensus**) The maxHP/16 is the house
Leftovers denominator from m002 and m005, here with the condition that m005's version does not
carry.

## Turning it on again is not titration

```
   static void Cmd_setrain(void)
   {
       if (gBattleWeather & B_WEATHER_RAIN)
       {
           gMoveResultFlags |= MOVE_RESULT_MISSED;
           gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_WEATHER_FAILED;
       }
       else
       {
           gBattleWeather = B_WEATHER_RAIN_TEMPORARY;
           ...
           gWishFutureKnock.weatherDuration = 5;
       }
   ──────────────────────────────────────────────────────────────────────────────────────────
   Rain Dance into existing rain FAILS. It does not top up the five-turn clock, it does not
   deepen anything, and it consumes the turn. The only two operations the engine offers are
   "set it" and "it is already set". `Cmd_setsandstorm` is the same function with a different
   bit. There is no adjust.
```

Which is the first half of the clinical point and `ENDTURN_RAIN` is the second:

```
   case ENDTURN_RAIN:
       if (gBattleWeather & B_WEATHER_RAIN)
       {
           if (!(gBattleWeather & B_WEATHER_RAIN_PERMANENT))
           {
               if (--gWishFutureKnock.weatherDuration == 0)
               ...
   ──────────────────────────────────────────────────────────────────────────────────────────
   The decrement is INSIDE a test for the permanent bit. Kyogre's Drizzle sets
   `(B_WEATHER_RAIN_TEMPORARY | B_WEATHER_RAIN_PERMANENT)` — both bits — so the damage
   modifier above, which tests the temporary bit, fires exactly as it would from Rain Dance,
   and the clock is never read. Identical effect. Identical readout. One has a review point
   and one does not, and the difference is one bit nothing displays.
```

That is the characteristic oxygen failure, stated as precisely as it can be stated. The error is
rarely giving oxygen to someone who does not need it. It is giving oxygen to someone who needed it
on Tuesday, at a setting chosen on Tuesday, read against no written target, and still running on
Friday — the same intervention with the clock deleted. The review point is the intervention.
(**mechanism**) And this is m038's device in another tract: a thing started once, for a good
reason, that nothing afterwards asks about.

Drizzle also tells you where responsibility sits. The ability belongs to **Kyogre**, and the rain
persists after Kyogre has left the field — which is m009's whole device, the standing property
against the discrete act, and it is exactly the structure of oxygen started in an emergency by
someone who will not be there tomorrow. Most national guidance explicitly permits starting without
a prescription in that situation, with documentation afterwards. (**country-dependent**)

## The whole layer is written as the absence of two abilities

```
   #define WEATHER_HAS_EFFECT ((!ABILITY_ON_FIELD(ABILITY_CLOUD_NINE) \
                             && !ABILITY_ON_FIELD(ABILITY_AIR_LOCK)))
   ──────────────────────────────────────────────────────────────────────────────────────────
   Every weather effect in the engine is gated on this macro, and the macro is defined
   NEGATIVELY: the field works unless one of two named abilities is present anywhere. The
   damage switch above sits inside `WEATHER_HAS_EFFECT2`. Rain Dish sits inside
   `WEATHER_HAS_EFFECT`. Nothing asks whether the weather is up without also asking this.
```

m052 is built on that definition and the point carries here. The thing that decides whether the
field has any effect at all is not in the field and not in the battler: it is a third object
somewhere on the board. In oxygen's case the third object is the monitoring. A saturation inside
the target range is fully compatible with a rising carbon dioxide, because oximetry reports the
proportion of available haemoglobin carrying oxygen and says nothing about carbon dioxide or pH.
(**mechanism**, **consensus**) So the instrument that confirms the oxygen is right cannot detect
the commonest harm from getting it wrong; only a blood gas reads that. m102 holds the full
oximetry argument, including that the reading can be normal in carbon monoxide poisoning and that
accuracy is reduced, biased toward over-reading, in people with darker skin pigmentation — which
matters most exactly where a decision turns on whether the number is inside the range or just
below it. (**consensus**)

## Where the metaphor stops

A mask is not a neutral object to wear, and nothing above models that.

It is claustrophobic for many people. It makes speech hard and lip-reading impossible. It
interferes with eating, drinking and being understood, and it dries the mouth and the nose. People
take them off, and the usual conclusion drawn — non-compliance — is a statement about the
prescription rather than about the person. Nasal cannulae are tolerated better by most people and
are frequently the difference between a treatment that is received and one that is only written
down.

For someone frightened and breathless, the mask also arrives at the worst possible moment, often
from behind, held by a stranger. Saying what is about to happen in short sentences first, and
checking afterwards, is not a courtesy; it is what determines whether the treatment stays on.

Long-term oxygen at home reorganises a household. Tubing across floors, a concentrator audible at
night, rules about who may smoke indoors, and a visible marker of illness in the living room.
Those are decisions about a home, and the people who live in it have a legitimate say that is not
a clinical variable.

And the structural point, because blaming individuals for it is the common error: oxygen goes
unprescribed and unreviewed largely because the prescription chart, the observation chart and the
flowmeter are three separate objects in three places, and the person adjusting the flowmeter often
has no written target to adjust it against. Changing that is the fix. Asking people to be more
careful is not.

## What Nurse Joy is listening for

That the indication is hypoxaemia and not breathlessness, and what the non-hypoxaemic trial
evidence actually shows. Why a target range with two edges is prescribed rather than a flow, and
which of the two standing ranges applies to whom locally. The upper-edge mechanisms, with the
ventilation–perfusion and Haldane terms named and not only the hypoxic-drive one. Why a rising
carbon dioxide calls for controlled reduction and escalation rather than switching the oxygen off.
Why the delivery device is a separate decision from the flowmeter, and what fixed-performance
delivery controls that variable-performance delivery does not. Why oximetry cannot see the
upper-edge harm. And the local arrangements: who prescribes, who titrates, where the target is
written, how someone at risk of hypercapnia is flagged, and what the fire rules are.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The reader's **national respiratory society's guideline on emergency oxygen use in adults**,
  which sets the target ranges, the device classes and the prescription requirement, and differs
  by country.
* The reader's institutional oxygen prescribing and administration policy, including who may
  initiate without a prescription and who may titrate.
* The reader's national guidance on home and long-term oxygen therapy, which is a separate pathway
  and is commonly confused with acute oxygen.
* A current textbook of respiratory physiology, for the oxygen cascade, the dissociation curve,
  hypoxic pulmonary vasoconstriction and the Haldane effect.
* The published trial literature on conservative against liberal oxygen targets, and on oxygen
  against air in non-hypoxaemic breathlessness.
* The reader's national medical device regulator's current position on pulse oximeter accuracy and
  skin pigmentation.
* The reader's local fire safety policy for medical gases.

The Pokémon material is from the **pret/pokeemerald** decompilation of Pokémon Emerald: the
weather bit definitions in `include/constants/battle.h`; `WEATHER_HAS_EFFECT` in
`include/battle_util.h`; `Cmd_setrain` and `Cmd_setsandstorm` in `src/battle_script_commands.c`;
the `ENDTURN_RAIN` case, the `ABILITY_RAIN_DISH` case, the Drizzle case and
`CastformDataTypeChange` in `src/battle_util.c`; the weather multipliers inside
`CalculateBaseDamage` in `src/pokemon.c`; and Ludicolo's, Torkoal's, Castform's and Kyogre's
entries in `src/data/pokemon/species_info.h`.

## Scope and safety

This explains why oxygen is treated as a prescribed drug, using a game's field-state layer, at the
level of someone already training in or qualified for clinical practice. It is not an oxygen
guideline and not a prescribing aid. It states **no target saturation range, no flow, no device
setting, no inspired fraction and no threshold** of any kind, deliberately, because all of those
are set by the reader's national guidance and local policy and differ between countries. Nothing
here has had clinical review. Nothing here is for use during an emergency or for any decision
about any person's care. If someone is unwell or breathless right now, the local emergency number
is the correct response.

## Where this stands, October 2026

The mechanical material is fixed; Emerald's eight weather bits are not going to grow a ninth. The
physiology is stable, and so is the prescription-and-target-range structure, which is now
near-universal in national guidance. What dates is everything numerical: the specific ranges, the
designation of who is at risk of hypercapnic respiratory failure, and the device recommendations —
all country-dependent and all revised more than once. The conservative-against-liberal target
question in acute illness is an active trial literature whose balance has shifted within the last
decade. The pulse oximetry pigmentation question is the fastest-moving item here and is under
regulatory review in several jurisdictions, so the guidance a reader finds will be newer than
this. Their national respiratory society's oxygen guideline and their own institution's policy are
the authority throughout.
