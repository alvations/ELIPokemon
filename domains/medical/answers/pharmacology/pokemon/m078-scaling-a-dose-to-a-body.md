---
id: "m078"
slug: scaling-a-dose-to-a-body
style: pokemon
category: pharmacology
difficulty: intermediate
question: "Why are some doses flat, some scaled by body weight, some by body surface area and some by organ function, and why is none of those scalings the whole answer?"
tags: [dose-scaling, allometry, body-surface-area, organ-function, calculation-error]
---

# The Pokédex stores height and weight. The battle engine reads the weight and never the height.

**This answer is about arithmetic.** Nothing in it stands in for a patient, and nothing in it
stands in for a small patient — the objects being scaled are damage formulas, and the two numbers
being argued over are two fields of a struct. That is not a hedge; it is the reason this topic can
be written in Pokémon at all. The taste rule and its reasoning are in the plain-prose section
below.

The Game Boy Advance code contains six different rules for setting one quantity, which is more
scaling rules than most pharmacology textbooks print, and it contains them side by side in one
file.

## Six rules for one quantity

```
   rule                      what the amount is a function of                  from the code
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Dragon Rage               nothing at all. 40.                   setword gBattleMoveDamage, 40
   Sonic Boom                nothing at all. 20.                   setword gBattleMoveDamage, 20
   Seismic Toss              the USER's level, linearly            Cmd_dmgtolevel:
   Night Shade                                                       gBattleMoveDamage =
                                                                      gBattleMons[attacker].level
   Low Kick                  the TARGET's catalogue weight,        Cmd_weightdamagecalculation,
                             in six bands                           via sWeightToDamageTable
   Super Fang                half the target's CURRENT state       m006's device
   Flail / Water Spout       the user's current state, in          m064's device
                             opposite directions
   everything else           level, both stats, base power,        CalculateBaseDamage, then
                             type, and a random factor              ApplyRandomDmgMultiplier
   ─────────────────────────────────────────────────────────────────────────────────────────────

   AND LOOK AT THE MOVE DATA for the first four:

     Dragon Rage    .power = 1     Seismic Toss   .power = 1
     Sonic Boom     .power = 1     Night Shade    .power = 1     Low Kick  .power = 1

   A placeholder. The field that is supposed to hold the amount holds a 1, because
   for these five the amount is not in the data at all -- it is computed somewhere
   else from something about a body. A dose written on a box and a dose worked out
   at the bedside are not the same kind of object, and the games distinguish them
   by putting a 1 in the box.
```

## The bands are not proportional, and the Pokédex proves it

```
   static const u16 sWeightToDamageTable[] =        // min. weight in HECTOGRAMS, base power
       { 100, 20,  250, 40,  500, 60,  1000, 80,  2000, 100,  0xFFFF, 0xFFFF };
   ... and anything at or above 2000 hectograms gets 120.

   band          weight (kg)       delivered base power
   ─────────────────────────────────────────────────────
   1             under 10               20
   2             10 to under 25         40
   3             25 to under 50         60
   4             50 to under 100        80
   5             100 to under 200      100
   6             200 and over          120

   NOW PUT REAL POKéDEX WEIGHTS THROUGH IT

   Gastly        0.1 kg   ─┐
   Caterpie      2.9 kg    ├─ all band 1, all base power 20
   Pikachu       6.0 kg   ─┘      ... a SIXTY-FOLD spread, one answer

   Pikachu       6.0 kg   ── band 1, power  20
   Shuckle      20.5 kg   ── band 2, power  40
                                ... a 3.4-fold spread, two different answers

   Onix        210.0 kg   ─┐
   Wailord     398.0 kg    ├─ all band 6, all base power 120
   Snorlax     460.0 kg    │
   Groudon     950.0 kg   ─┘      ... a 4.5-fold spread, one answer
```

That is banded dosing, exactly: coarse in the middle of a band, sharp at the edge, and the edges
chosen round. **Gastly** and **Pikachu** differ by a factor of sixty and are treated identically;
**Pikachu** and **Shuckle** differ by a factor of three and a half and are treated differently.
The banding is not wrong — six bands are a great deal better than one — but no band boundary in
that table was derived from anything about **Gastly**.

## And the weight it reads is not this one's weight

```
   if (sWeightToDamageTable[i] >
         GetPokedexHeightWeight(SpeciesToNationalPokedexNum(gBattleMons[target].species), 1))
```

It reads the **Pokédex** entry. The species figure. So a **Snorlax** freshly hatched and a
**Snorlax** at level 100 both return 4600 hectograms, and **Low Kick** gives the same answer to
both. The scaling rule is called weight-based and the number it uses is a catalogue value, not a
measurement of the individual in front of it.

Which is the stated-weight-against-measured-weight problem written into the engine, and it is the
sharpest thing in this answer. A dose rule can be perfectly correct in form and be fed a number
that is about the population rather than about the person.

## The second size parameter, recorded for every species and never read in battle

```
   struct PokedexEntry
   {
       /*0x00*/ u8  categoryName[12];
       /*0x0C*/ u16 height;   // in DECIMETRES
       /*0x0E*/ u16 weight;   // in HECTOGRAMS
       ...
   };

   u16 GetPokedexHeightWeight(u16 dexNum, u8 data)
   {
       switch (data)
       {
       case 0:  return gPokedexEntries[dexNum].height;   ◄── never requested by any
       case 1:  return gPokedexEntries[dexNum].weight;        battle routine
       default: return 1;
       }
   }

   Call sites of that function inside the battle engine: exactly ONE.
   It passes 1.
```

Two size columns, adjacent in one struct, filled in for every species. One of them is wired into a
damage calculation and the other is wired into a display. And the two columns **do not track each
other**:

```
   species      height    weight       the ratio nobody computes
   ─────────────────────────────────────────────────────────────────────
   Gastly        1.3 m     0.1 kg      tall and essentially massless
   Caterpie      0.3 m     2.9 kg      short and twenty-nine times heavier
   Shuckle       0.6 m    20.5 kg      half Gastly's height, 205× its mass
   Snorlax       2.1 m   460.0 kg
   Onix          8.8 m   210.0 kg      taller than Wailord's half, lighter
   Wailord      14.5 m   398.0 kg
   ─────────────────────────────────────────────────────────────────────

   Gastly is over four times Caterpie's height and a twenty-ninth of its mass.
   Wailord is 1.6× Onix's height and 1.9× its mass -- those two roughly track.
   SO THE CORRELATION BETWEEN THE TWO COLUMNS IS NOT A CONSTANT, and a rule built
   on one of them is not a rule built on the other, however similar they look in
   the middle of the range.
```

And the geometry underneath it, which is why the two can never be reconciled by a constant:

```
   Double every linear dimension of anything.

      length  ×2        AREA  ×4  (length²)        MASS  ×8  (length³)

   So AREA / MASS halves. Per unit of the smaller column, the smaller body gets
   MORE. Per unit of the larger column, it gets LESS. The two rules diverge in
   opposite directions as size changes and cross somewhere in the middle.
```

That is the whole of body surface area against body weight, and it does not need a patient in it.
The games record the second column and decline to use it — not because using it would be wrong,
but because nothing in a battle needed it. Which is the honest shape of the real argument too: a
scaling survives because something it predicted mattered, not because it is geometrically purer.

## Two scalings of the same body, in the same function

`CalculateMonStats` computes six quantities from the same inputs with two different expressions,
and the difference between them is three tokens.

```
   maximum HP      (((2 * baseHP + hpIV + hpEV / 4) * level) / 100) + level + 10
   the other five  (((2 * base   + iv    + ev / 4)  * level) / 100) + 5
                                                                      ▲
                                        + level + 10   against   + 5

   Same proxy, same scaling, two different additive terms -- so the CAPACITY term
   grows with the size parameter and the five RATE terms get a constant. m006's
   volume-against-clearance distinction is in the arithmetic, not in the
   interpretation.

   And the override that proves the formula is a model and not a law:
       if (species == SPECIES_SHEDINJA) newMaxHP = 1;
   One species for which the whole expression is discarded. Nature cannot touch HP
   either -- ModifyStatByNature returns the figure unchanged for it.
```

Put **Blissey**'s base HP of 255 and **Shedinja**'s hard-coded 1 at the two ends of that
expression and you have `m006`'s point in its strongest form: the capacity term and the rate terms
are computed from the same proxy by the same routine, and one species is simply excluded from the
model by name. A scaling rule that has a written exception is a scaling rule somebody has already
found the edge of.

## The mechanism question is settled before the scaling question

This is the order the code runs them in, and the order is the lesson.

```
   BattleScript_EffectLevelDamage::        (Seismic Toss, Night Shade)
       attackcanceler
       accuracycheck ...
       attackstring
       ppreduce
       typecalc                            ◄── runs FIRST
       bicbyte gMoveResultFlags, MOVE_RESULT_SUPER_EFFECTIVE | MOVE_RESULT_NOT_VERY_EFFECTIVE
       dmgtolevel                          ◄── OVERWRITES whatever typecalc scaled
       adjustsetdamage

   The ×2 and the ×0.5 are computed and then thrown away -- that bicbyte only
   clears the two MESSAGES, and dmgtolevel discards the number. But the ×0 case
   sets MOVE_RESULT_DOESNT_AFFECT_FOE, which that line does NOT clear.

   So: Seismic Toss into a Ghost is zero at every level there is, and no scaling
   rule anywhere rescues it. m007's zero again.
```

**Low Kick** makes the same point and makes it worse, because there the scaling actually ran.
`BattleScript_EffectLowKick` calls `weightdamagecalculation` and then jumps to
`BattleScript_HitFromCritCalc`, which is `critcalc`, `damagecalc`, `typecalc`,
`adjustnormaldamage` — in that order. **Low Kick** is `TYPE_FIGHTING` and **Gastly** is `{
TYPE_GHOST, TYPE_POISON }`. So the table was consulted, **Gastly**'s 0.1 kg was looked up, band 1
was selected, a base power of 20 was written into `gDynamicBasePower`, the damage was computed
from it — and then `typecalc` multiplied the whole thing by nothing. The band was correct. The
arithmetic was correct. The answer was zero, and `m007` is the reason.

## What no scaling rule touches

```
   static inline void ApplyRandomDmgMultiplier(void)
       randPercent = 100 - (Random() % 16);        ──► 85 .. 100, sixteen outcomes

   Cmd_psywavedamageeffect
       while ((randDamage = Random() % 16) > 10);
       gBattleMoveDamage = level * (randDamage * 10 + 50) / 100;
                                   ──► eleven equally likely multipliers,
                                       50 % to 150 % of the same input
```

**Psywave** is the honest picture of what a dose rule achieves. It takes one body parameter,
scales linearly off it, and then hands the result to an eleven-outcome draw. The rule chose the
centre of a distribution. It did not choose the outcome, and reading one outcome tells you about
the draw rather than about the rule — which is `m080`'s whole subject and `m041`'s reason for
measuring rather than inferring.

## Where the metaphor stops

The taste rule first, because it governed how this half was written. The obvious way to explain
weight-based dosing in Pokémon would be to put a small, low-level creature in the place of a small
patient and talk about how much more it needs per kilogram. That mapping is not available here and
was not used. It requires something in the game to *be* the patient whose body is the subject, and
`../../../SAFETY.md` fences that off, for reasons that apply with particular force to paediatric
material. So the subject above is the arithmetic: six formulas, two struct fields, one placeholder
and a geometric identity. Nothing in it is anybody.

Now the human part, without analogy.

The dominant cause of serious harm in this topic is not a mis-chosen scaling. It is
**arithmetic**. A weight-based or area-based regimen needs a measurement obtained, recorded in the
right units, multiplied, converted from a mass to a volume of some particular concentration, and
then measured out. Every one of those steps has produced documented ten-fold errors, and the three
that recur are a decimal point, a unit confusion, and a weight that was estimated or remembered
rather than measured. The size of the harm is not proportional to the size of the slip: there is
no such thing as a small decimal-point mistake.

What has worked is not asking people to be more careful. It is taking the arithmetic out of the
point of care — pre-calculated dosing charts, dose banding, standardised infusion concentrations,
ready-to-administer preparations, double-checks built into the task rather than requested, and
prescribing systems that refuse an implausible figure. `m044` describes the same engineering
answer for wrong-route errors, and it is right for the same reason: the error is rare,
catastrophic, and not a failure of diligence.

It is worth saying where this falls. Weight-based and area-based dosing is concentrated in
paediatric practice and in oncology, and that is therefore where the safeguards have had to be
built. That is a statement about where the arithmetic lives, not about any group of patients.

Nothing in this pair gives a dose, a scaling rule for any drug, or a weight descriptor for any
product, and in particular nothing here is a paediatric dosing method. Those live in the
formulary, in the product's own information, and in your local children's or chemotherapy dosing
reference, and those are the authorities. Anyone with a question about a dose they have been given
should ask their prescriber or pharmacist, who can check it against the product information in
seconds.

## What a Gym Leader is listening for

* **Dragon Rage** and **Seismic Toss** both have `.power = 1` in the move data. What is that 1
  telling you?
* **Gastly** and **Pikachu** differ sixty-fold in mass and get the same **Low Kick** answer.
  **Pikachu** and **Shuckle** differ three-and-a-half-fold and get different ones. What property
  of banding is that?
* Whose weight does **Low Kick** read, and in what sense is it not a measurement?
* Double a body's linear dimensions. What happens to the ratio of the two **Pokédex** columns, and
  which way does each dosing rule then err?
* Find the three extra tokens in the maximum-HP expression. What distinction are they?
* **Seismic Toss** into a Ghost, at level 100. Give the number and say which line of the battle
  script decided it.
* **Low Kick** into **Gastly**. Which band does the table select, and what is delivered?
* **Psywave** at a fixed level produces eleven different answers. What does that make a scaling
  rule responsible for, and what does it not?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **The product's own approved prescribing information**, for the dose, the scaling rule and
  crucially *which weight descriptor* it uses — total, ideal, adjusted or lean. That is a
  product-level fact and is not derivable from anything here.
* **Your national paediatric formulary or children's dosing reference**, which exists separately
  from the adult formulary in several countries precisely because weight-based dosing needs its
  own apparatus. It is the authority for that territory and this pair is not.
* **Your institution's injectable medicines guide and its chemotherapy dosing and dose-banding
  policy**, for standardised concentrations, banding tables and required checks. Local,
  overriding, and what you will be held to.
* **Your national renal association's or laboratory network's guidance on reporting and using
  estimated glomerular filtration rate**, for the indexed-against-absolute distinction that the
  technical twin sets out, and for which estimating equation is in use where you are.
* **A current clinical pharmacokinetics textbook's chapter on dose individualisation and
  allometry**, for the scaling exponent, the area-to-mass derivation, and size against function as
  scaling variables.
* **The primary literature**, for the surface-area controversy in cytotoxic dosing, for the
  evidence behind flat dosing of therapeutic antibodies, and for any allometric exponent. All
  three are contested and neither half of this pair states a figure from them.
* **Your national patient-safety body's alerts** on dose calculation and paediatric dosing errors.

The Pokémon figures are a different matter and were read directly from the public decompilation of
the Game Boy Advance games rather than recalled: `sWeightToDamageTable` holding `100, 20, 250, 40,
500, 60, 1000, 80, 2000, 100` with a terminator and a fall-through of 120, and
`Cmd_weightdamagecalculation` breaking on the first threshold greater than the target's weight;
`GetPokedexHeightWeight` returning height for 0 and weight for 1, with the single battle-engine
call site passing 1; `struct PokedexEntry` holding height in decimetres and weight in hectograms;
the Pokédex height and weight entries for Gastly, Caterpie, Pikachu, Shuckle, Onix, Snorlax,
Wailord and Groudon; `Cmd_dmgtolevel` assigning the attacker's level; the `setword` of 40 and 20
in `BattleScript_EffectDragonRage` and `BattleScript_EffectSonicboom`; `.power = 1` on Dragon
Rage, Sonic Boom, Seismic Toss, Night Shade and Low Kick; `BattleScript_EffectLevelDamage`'s order
of `typecalc`, the `bicbyte` of the two effectiveness flags, and `dmgtolevel`; `ModulateDmgByType`
setting `MOVE_RESULT_DOESNT_AFFECT_FOE` on the zero case; `CalculateMonStats`'s two expressions
and the Shedinja override to a maximum HP of 1; `ModifyStatByNature` returning the figure
unchanged for HP; `ApplyRandomDmgMultiplier` as `100 - (Random() % 16)`; and
`Cmd_psywavedamageeffect`'s rejection loop and `level * (randDamage + 50) / 100`;
`BattleScript_EffectLowKick` calling `weightdamagecalculation` and jumping to
`BattleScript_HitFromCritCalc`, which is `critcalc`, `damagecalc`, `typecalc`,
`adjustnormaldamage`; and Low Kick being `TYPE_FIGHTING` against Gastly's `{ TYPE_GHOST,
TYPE_POISON }`. Low Kick's weight-based power is a **third-generation** change: in Red and Blue it
is a flat 50-power Fighting move with a flinch chance, and in the second generation the same. The
arithmetic in the blocks above is recomputed from those figures.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones and one
geometric identity**: doubling a linear dimension multiplies area by four and mass by eight.
Neither half contains a dose or a dosing rule for any drug, and in particular neither is a
paediatric dosing method — that territory has its own reference works and they are the authority.
Anyone with a question about a dose they have been given should ask their prescriber or pharmacist
rather than work it out from anything on this page. Nothing here should be used to make a decision
about anyone's treatment, including the reader's own.

## Where this stands, October 2026

The mechanism — exposure as the target, two quantities behind it, the geometry of area against
mass, and function rather than size as the better proxy for an eliminating organ — does not date,
and the game mechanics quoted are fixed in released software, pinned above to the Game Boy Advance
games because Low Kick's weight table is a third-generation addition. Three clinical things date.
The **allometric exponent**, and whether one exponent is the right model, remains argued in the
population pharmacokinetics literature. The **surface-area convention in cytotoxic dosing** is
under active challenge and has already been displaced for several products, so which drugs are
dosed which way is a moving list. And the **reporting and estimating of renal function** has
changed in several countries within the last few years, which directly changes the figure a dosing
decision rests on. Check the product information, your paediatric or chemotherapy dosing
reference, and your own laboratory's reporting convention.
