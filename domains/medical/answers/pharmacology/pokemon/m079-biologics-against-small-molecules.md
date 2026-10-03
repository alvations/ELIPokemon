---
id: "m079"
slug: biologics-against-small-molecules
style: pokemon
category: pharmacology
difficulty: advanced
question: "What actually changes when a medicine is a biologic rather than a small molecule, and in what sense is a biosimilar not a generic?"
tags: [biologics, biosimilars, immunogenicity, comparability, pharmacovigilance]
---

# A move is a row in a table. A Pokémon is a draw from a routine, and the routine is the product.

**Surf** is not an object in these games. It is `gBattleMoves[MOVE_SURF]` — a row with a power, a
type, an accuracy, a PP count, a priority and a flag word. Every **Surf** in every cartridge is
that row. There is nothing to vary.

A **Snorlax** is not a row. It is an *instance*, built by a routine that specifies a process and
then draws the product, and no two of them come out the same. That distinction is the whole of
this topic, and the Game Boy Advance code states both halves of it in code you can read.

## The small molecule: a row, and Sketch hands you the row

`Cmd_copymovepermanently` is **Sketch**'s implementation, and the function name is the argument.
What a **Smeargle** acquires is the move — the same row, written into a slot, permanently. Two
**Smeargle** that have Sketched **Surf** do not have two similar Surfs. They have **Surf**.

`m045` uses Sketch for horizontal transfer of a resistance determinant; here the same mechanic
does the generic-medicine job, and for the same reason: what moved was the *identity*, so no
comparison is required afterwards. A generic's approval rests on one kinetic study precisely
because the row is the row.

And `m045`'s other route makes the same point from the far side. An **Egg Move** arrives through
the **Day Care** instead of through **Sketch** — a different mechanism, a different set of
conditions — and what lands in the slot is still the identical row. Two manufacturing routes, one
substance. That is exactly why a generic's dossier does not ask how the molecule was synthesised,
and exactly why a biosimilar's does.

## The biologic: the routine is specified and the product is drawn

```
   CreateBoxMon(boxMon, species, level, fixedIV, ...)

     personality = Random32();                       ◄── 32 bits, once, never rewritten
     ...
     value = Random();
     iv = value & MAX_IV_MASK;          hpIV         MAX_IV_MASK = 31
     iv = (value & (MAX_IV_MASK << 5)) >> 5;   attackIV
     iv = (value & (MAX_IV_MASK << 10)) >> 10; defenseIV
     value = Random();                               ◄── a SECOND draw for the other three
     ... speedIV, spAttackIV, spDefenseIV

     if (gSpeciesInfo[species].abilities[1])
         value = personality & 1;       abilityNum

     GiveBoxMonInitialMoveset(boxMon);

     checksum = CalculateBoxMonChecksum(boxMon);
     EncryptBoxMon(boxMon);
```

Read that as a manufacturing specification, because that is what it is. The *routine* is fixed and
published. The *output* is six five-bit draws and a 32-bit word, so two **Snorlax** made by the
same routine on the same day differ in their six Individual Values, in their Nature, in which of
`{Immunity, Thick Fat}` they express, and therefore in what they do — all within specification,
all normal, none of it a defect. `m077` is what those draws mean for an individual; here the point
is upstream of that. **You cannot specify the product. You can only specify the process.**

The Emerald data even contains the three grades of within-specification difference that a release
specification has to tell apart.

| Grade of difference | The data | The analogue |
| --- | --- | --- |
| Real, and it changes the function | **Snorlax** `{Immunity, Thick Fat}`; **Chansey** and **Blissey** `{Natural Cure, Serene Grace}` | a variant the functional assays detect — the one a comparability exercise exists to exclude |
| Real in the data, null in function | **Granbull** `{Intimidate, Intimidate}`, **Vibrava** and **Flygon** `{Levitate, Levitate}` — the only three entries in that file whose two slots agree | a glycoform or charge variant that is measurably present and functionally indistinguishable. Within specification, and correctly so |
| Not drawn at all | **Shuckle** `{Sturdy}`, where `abilities[1]` is `ABILITY_NONE`, so the bit is never written | an attribute the process does not vary: characterise it once, do not monitor it per batch |

The middle row is the one worth keeping, because it is where the public argument about biosimilars
usually goes wrong. A **Flygon**'s ability bit genuinely differs between individuals, a test that
reads it genuinely returns two different answers, and **Levitate** comes out either way. "Not
identical" and "not the same medicine" are different claims, and the second does not follow from
the first.

## Transform is the comparability exercise, and the boundary is an `offsetof`

This is the best mechanic in the games for the biosimilar question, because the regulator's
"totality of evidence" is replaced by a single byte offset you can look up.

```
   Cmd_transformdataexecution

     for (i = 0; i < offsetof(struct BattlePokemon, pp); i++)
         battleMonAttacker[i] = battleMonTarget[i];

     for (i = 0; i < MAX_MON_MOVES; i++)
         pp[i] = min(gBattleMoves[moves[i]].pp, 5);

   struct BattlePokemon, and where the copy stops
   ──────────────────────────────────────────────────────────────────────────────
   0x00  species             ┐
   0x02  attack              │
   0x04  defense             │
   0x06  speed               │
   0x08  spAttack            │  COPIED. Everything the comparability exercise
   0x0A  spDefense           │  compares, including the HIDDEN attributes:
   0x0C  moves[4]            │  all six Individual Values cross the boundary.
   0x14  the six IVs,        │
         isEgg, abilityNum   │
   0x18  statStages[8]       │
   0x20  ability             │
   0x21  types[2]            │
   0x23  (unused)            ┘
   ──────────────────────────────────────── offsetof(..., pp) = 0x24 ───────────
   0x24  pp[4]               ← NOT copied: overwritten with min(declared, 5)
   0x28  hp                  ┐
   0x2A  level               │
   0x2B  friendship          │  NOT COPIED AT ALL. The copy keeps its own.
   0x2C  maxHP               │
   0x2E  item                │
   0x30  nickname            │
   0x3B  ppBonuses           │
   0x3C  otName              │
   0x44  experience          │
   0x48  personality         │
   0x4C  status1             │
   0x50  status2             │
   0x54  otId                ┘
```

Three categories, and they are exactly the three a comparability exercise produces.

**Identical, including what you cannot see.** Because the six Individual Values cross the
boundary, a **Ditto** that has used **Transform** produces a **Hidden Power** of the target's type
and the target's base power — the twelve bits `m077` works through came across intact. The
analytics reached the hidden attributes, which is the whole claim biosimilarity rests on.

**Different by design, and the difference is written down.** The PP is set to `min(declared, 5)`
whatever it was. The copy's *supply* is not the original's supply, and nobody is pretending
otherwise. That is a known, specified, documented difference — the analogue of a different
excipient, a different device, a different presentation.

**Not compared at all.** `maxHP` is on the far side of the offset. A **Ditto** that has
Transformed into a **Blissey** carries **Blissey**'s attack and defence figures across — computed
from bases of 10 and 10, which are not what a **Blissey** is for — and keeps its own maximum HP,
computed from a base of 48 against **Blissey**'s 255. The one number that makes a **Blissey** a
**Blissey** is the one number on the far side of the offset. So the copy matches on everything the
routine looked at and does not match on capacity, because capacity was never in the copy. Whether
that matters depends entirely on what you are using it for — which is, word for word, the
interchangeability argument.

## What the copy does not inherit: the provenance

Everything past `0x24` includes `otName`, `otId` and `personality`, and the Box-level fields the
routine wrote at creation — `MON_DATA_MET_LOCATION`, `MON_DATA_MET_LEVEL`, `MON_DATA_MET_GAME`,
`MON_DATA_POKEBALL` — are not in `struct BattlePokemon` at all and cannot cross.

And then there is the detail that makes it a labelling point rather than an omission:

```
   gDisableStructs[attacker].transformedMonPersonality = gBattleMons[target].personality;
```

The game records *whose* personality value it is wearing, in a **separate field**, for display,
while the copy's own identity is untouched. A thing that behaves like the reference product, is
displayed as the reference product, and carries its own identifier in its own field — which is why
a biologic is prescribed, dispensed and recorded by brand with the batch number rather than by the
name of the molecule. Two biosimilars of one reference product are two products, and an adverse
event has to be attributable to the one that caused it.

The series later built a mechanic that is nothing but this problem. **Zoroark**'s **Illusion** — a
fifth-generation Ability, not present in the Game Boy Advance games, and `m037`'s device for the
record that is wrong in the way that matters — makes the field display one species while a
different one is standing there. Nothing about the creature changed; only the label did. A
pharmacovigilance system that records the molecule and not the product is in exactly that
position, and the naming conventions for biologics exist to stop it.

## Immunogenicity: Disable is raised against the agent just used

```
   Cmd_disablelastusedattack

     find i such that gBattleMons[target].moves[i] == gLastMoves[target]
     requires:  disabledMove == MOVE_NONE        (only ONE at a time)
                i != MAX_MON_MOVES               (it must be in the repertoire)
                pp[i] != 0                       (there must be supply left)
     then:      disabledMove = moves[i]
                disableTimer = (Random() & 3) + 2     ──► two to five turns
```

Specific to the exact agent that was just used, raised after the exposure rather than before it,
limited in duration, and keyed to a slot rather than to a class. Anti-drug antibodies have that
shape: they are product-specific, they develop on exposure, and they neutralise what provoked
them. **Disable** also has to find the move in the repertoire — the response needs something to
recognise.

**Imprison** is the cross-reactive shape, and it is the opposite direction. Power 0, accuracy 100,
10 PP, `MOVE_TARGET_USER`: it makes unusable, in the opponent's hands, every move the *user
itself* knows, checked slot by slot in `CheckMoveLimitations`. One recognition event, several
agents blocked, because what was recognised is shared.

The honest limit: **Disable** blocks a move outright, and a real anti-drug antibody response can
also work by clearing the drug faster without blocking it. The code has nothing for that second
route, and a failure that looks identical from outside but has two different mechanisms is exactly
the thing the clinical investigation exists to separate.

## An elimination route that depends on the target

```
   ppreduce, with the target's ability consulted:
       if (gBattlerAttacker != gBattlerTarget
           && gBattleMons[gBattlerTarget].ability == ABILITY_PRESSURE)
           ppToDeduct++;
```

`m009` uses **Pressure** for an Ability that acts while present and stops when it leaves. Here it
does a second job: the rate at which the agent's supply is consumed is a function of a property of
the *target*, not of the agent. That is the shape of target-mediated disposition, where a drug is
eliminated partly by binding the thing it was given to find.

And the limit, stated rather than glossed: **Pressure** adds one, linearly, every time. Real
target-mediated clearance **saturates**, which is why an antibody's half-life is not a constant.
Nothing in these games saturates an elimination route, so that part of the pharmacology has no
mechanic and the technical twin has to carry it.

## A product that fails closed

```
   DecryptBoxMon(boxMon);
   if (CalculateBoxMonChecksum(boxMon) != boxMon->checksum)
   {
       boxMon->isBadEgg = TRUE;
       boxMon->isEgg    = TRUE;
       substruct3->isEgg = TRUE;
   }
   ... and MON_DATA_NICKNAME then returns gText_BadEgg
```

Every stored instance carries a checksum, the checksum is verified on every read, and a mismatch
does not produce a slightly wrong **Snorlax**. It produces something the game renames, refuses to
treat as itself, and will not let you use. The product is fragile, the fragility is anticipated,
and the failure mode is designed to be loud.

That is the cold chain. A **Surf** cannot be spoiled, because there is nothing to spoil; an
instance can, and the only reason you find out is that somebody built a check in. The real
contrast is worse than the game's, and it is the first thing in the plain-prose section below.

## Where the metaphor stops

Everything above is mechanism. Three things about biologics in people are not, and they pull in
different directions.

**Biosimilar competition is the main reason biologics become affordable, and affordability is
access.** In several health systems the arrival of biosimilars is what allowed a therapy to be
offered at the stage of disease where it works best, rather than reserved until everything else
had failed. That is a large public-health good and it is the honest counterweight to everything
else here.

**A switch made for cost reasons is still a change a person experiences.** Reported worsening
after a non-medical switch is well documented, and it has two components that have to be held
apart: a real pharmacological difference, which the comparability exercise is designed to exclude,
and a nocebo component arising partly from how the switch was explained, which is real and
measurable. `m080` is the mechanism of the second. The two have different remedies, and conflating
them serves nobody — dismissing a reported deterioration as nocebo is not acceptable, and
attributing every deterioration to the switch is not accurate. A loss of response after a switch
deserves the same investigation as a loss of response without one.

**A cold chain failure leaves no mark.** The game's checksum is a courtesy the real world does not
extend: a protein that has been warm or frozen can look and inject exactly as it should and have
lost activity, with no mechanical sign that anything happened. Unlike a crushed modified-release
tablet, there is nothing to see. That is why handling requirements for these products are absolute
rather than advisory, and why the right response to a suspected breach is to ask rather than to
guess.

Nothing in this pair indicates whether any product should be switched, continued or stopped, for
anyone. Biosimilar switching is governed by national and institutional policy and by the person's
own specialist team, and anyone whose biologic has been or may be changed should take their
questions there, where the evidence for their specific product is known.

## What a Gym Leader is listening for

* Why does **Sketch** need no comparison afterwards, and **Transform** need a byte-by-byte
  specification of what crossed?
* Give the offset at which **Transform** stops copying, and name three fields on the far side of
  it.
* A **Ditto** has Transformed. Why does its **Hidden Power** come out as the target's, and why
  does its maximum HP not?
* What is `min(declared, 5)` the analogue of, and why is it not a defect?
* Why does the game store `transformedMonPersonality` in a separate field rather than overwriting
  `personality`?
* **Disable** fails if the slot has no PP left. What does that correspond to?
* **Pressure** adds one to the deduction, every time. Which part of antibody kinetics does that
  get right, and which does it get wrong?
* **Flygon** `{Levitate, Levitate}` beside **Snorlax** `{Immunity, Thick Fat}`. Both are
  within-specification differences. Why does only one of them matter?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **Your regional or national medicines regulator's guidance on similar biological medicinal
  products**, which defines the comparability exercise, what analytical similarity has to show,
  when a clinical study is required and when indication extrapolation is accepted. The major
  regulators' versions differ in detail and have been revised repeatedly.
* **The same regulator's guidance on immunogenicity assessment of therapeutic proteins**, for the
  assay issues that make published immunogenicity rates non-comparable between products.
* **The product's own summary of product characteristics or approved prescribing information**,
  for its immunogenicity data, handling and storage requirements, dose interval and licensed
  indications. Two biosimilars of one reference product have two of these and they are not
  interchangeable documents.
* **Your national and institutional policy on biosimilar substitution and switching.** This is the
  most country-dependent material in the pair: who may switch, whether a pharmacy may substitute,
  and what must be recorded are all decided nationally.
* **Your national pharmacovigilance scheme's guidance on reporting for biologics**, for the brand
  and batch requirement and why it exists.
* **Your specialty society's position statement on switching** in the relevant disease area, where
  one exists — that is where the clinical switching evidence and the communication material are
  usually summarised.
* **A current clinical pharmacology textbook chapter on biologics**, for target-mediated
  disposition, neonatal Fc receptor recycling and the kinetics generally.

The Pokémon figures are a different matter and were read directly from the public decompilation of
the Game Boy Advance games rather than recalled: `gBattleMoves` entries as static data;
`Cmd_copymovepermanently` as Sketch's implementation; `CreateBoxMon`'s `personality = Random32()`,
its two `Random()` draws packed into six five-bit Individual Values with `MAX_IV_MASK` of 31, its
`abilityNum = personality & 1` guarded on `abilities[1]`, its `GiveBoxMonInitialMoveset`, its
`CalculateBoxMonChecksum` and `EncryptBoxMon`; the checksum mismatch path setting `isBadEgg` and
`isEgg` and `MON_DATA_NICKNAME` then returning `gText_BadEgg`; the full field layout and offsets
of `struct BattlePokemon`, with `offsetof(struct BattlePokemon, pp)` at `0x24`;
`Cmd_transformdataexecution`'s byte copy up to that offset, its `pp[i] = min(declared, 5)`, and
its `gDisableStructs[attacker].transformedMonPersonality` assignment; `Cmd_hiddenpowercalc`
reading the six Individual Values; Blissey's base HP of 255 and Ditto's of 48; the ability pairs
quoted for Snorlax, Chansey, Blissey, Granbull, Vibrava, Flygon and Shuckle, with Granbull,
Vibrava and Flygon the only three entries in that file whose two slots hold the same ability;
`GiveBoxMonInitialMoveset` and the Day Care's egg-move route as alternatives to Sketch;
`Cmd_disablelastusedattack`'s slot search on `gLastMoves`, its three preconditions and its
`(Random() & 3) + 2` timer; Imprison's move data and its enforcement through
`GetImprisonedMovesCount` inside `CheckMoveLimitations`; and the `ppToDeduct++` for a target with
`ABILITY_PRESSURE` in the PP-reduction routine. Every figure above is from the Game Boy Advance
games; the single exception is flagged where it appears, Zoroark and Illusion being a
fifth-generation addition named as such rather than read from this decompilation.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** Neither half
names a product, and neither states an immunogenicity rate, a half-life, a dose or a storage
condition — those are product-specific, they live in the product's own information, and a figure
of that kind lifted from a revision answer would be worse than no figure. Nothing here indicates
whether any biologic should be started, switched, continued or stopped. Switching is governed by
national and institutional policy and by a specialist team, and anyone whose treatment has been or
may be changed should take their questions there. Nothing here should be used to make a decision
about anyone's treatment, including the reader's own.

## Where this stands, October 2026

The mechanism — the process as part of the product, catabolic elimination, target-mediated
disposition, the two functional classes of anti-drug antibody and the inverted evidence pyramid —
does not date, and the game mechanics quoted are fixed in released software and pinned above to
the Game Boy Advance games, where Individual Values run 0 to 31 and the ability slot is one bit.
Three clinical things date quickly. **Which products have biosimilars** changes as patents expire,
and with it the economics. **The substitution and interchangeability rules** are being actively
revised in several jurisdictions and in different directions, including movement toward requiring
less clinical data than earlier guidance did, so a statement about what an approval requires is
dated the moment the guidance is reissued. And the **naming conventions** meant to keep products
distinguishable in pharmacovigilance are not uniform between regions. Check your own regulator's
current guidance and your national substitution policy.
