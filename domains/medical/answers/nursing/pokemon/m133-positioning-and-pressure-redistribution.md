---
id: "m133"
slug: positioning-and-pressure-redistribution
style: pokemon
category: nursing
difficulty: intermediate
question: "What does repositioning change mechanically that a support surface cannot, and why is interface pressure only part of the load?"
tags: [pressure-ulcers, repositioning, biomechanics, shear, support-surfaces]
---

# `Low Kick` reads the weight out of the Pokédex entry. The height is the line above it.

`sWeightToDamageTable` is six lines long and it is the cleanest statement in the cartridge of why
interface pressure is not the whole story. It computes how hard a load lands from the target's
mass, in bands, out of a published species figure — and the dimension that mass is spread over is
stored one field away in the same struct and is never read.

m004 holds this subject's other half and holds more of it than its title suggests: the
pressure-time curve drawn through the **Whirlpool**, **Wrap**, **Bind**, **Fire Spin** and
**Clamp** family, **Grip Claw** and **Binding Band** as the two axes of it, **Future Sight** as
damage already settled and not yet shown, and **Onix** — base Defence **160**, base HP **35** —
as anywhere bone sits close to the surface. None of that is re-derived here. **Onix** appears
below for an unrelated reason, as a weight band, and the two uses are not the same device.

Markers used below, because this half carries clinical claims. (**mechanism**) means it follows
from the mechanics; (**definitional**) is what the word means; (**consensus**) is mainstream
agreement across major guidance; (**country-dependent**) means the reader's own national guidance
or local policy decides. Code blocks carry no marker. No repositioning interval, angle, pressure
figure or risk score appears anywhere here.

## Mass is in the table. Area is in the struct, one line away, and nothing reads it.

```
   static const u16 sWeightToDamageTable[] =
   { 100, 20,  250, 40,  500, 60,  1000, 80,  2000, 100,  0xFFFF, 0xFFFF };

   for (i = 0; sWeightToDamageTable[i] != 0xFFFF; i += 2)
       if (sWeightToDamageTable[i] >
           GetPokedexHeightWeight(SpeciesToNationalPokedexNum(species), 1))   ◄── 1 == weight
           break;
   gDynamicBasePower = (sWeightToDamageTable[i] != 0xFFFF)
                       ? sWeightToDamageTable[i + 1] : 120;

   u16 GetPokedexHeightWeight(u16 dexNum, u8 data)
   {
       case 0:  return gPokedexEntries[dexNum].height;    ◄── never called from here
       case 1:  return gPokedexEntries[dexNum].weight;    ◄── always called from here
   }
   ──────────────────────────────────────────────────────────────────────────────────────────
   Six bands: under 10.0 kg → 20, then 40, 60, 80, 100, and 120 from 200.0 kg upward.
   And the two fields sit on consecutive lines of one struct.
```

Now put four species through it, with the height printed beside the answer:

```
   species      weight      height      the band it lands in     what the formula used
   ──────────── ─────────── ─────────── ──────────────────────── ───────────────────────────
   Snorlax       460.0 kg    2.1 m       120                      the weight
   Steelix       400.0 kg    9.2 m       120                      the weight
   Wailord       398.0 kg    14.5 m      120                      the weight
   Onix          210.0 kg    8.8 m       120                      the weight
   ──────────── ─────────── ─────────── ──────────────────────── ───────────────────────────
   Shuckle        20.5 kg    0.6 m       40                       the weight
   Magikarp       10.0 kg    0.9 m       40                       the weight
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Snorlax puts 460 kg through 2.1 m. Wailord puts 398 kg through 14.5 m. SAME ANSWER —
   and above the top threshold the table is flat, so the difference is not even
   compressed, it is discarded. Shuckle at twice Magikarp's mass gets the same 40 because
   both sit inside one band.
```

That is force against pressure, written as a lookup table. **Load is what the body weighs;
pressure is what the body weighs divided by the area it goes through** (**definitional**), and
what makes a bony prominence dangerous is the second term and not the first (**mechanism**). The
sacrum, the ischial tuberosities, the greater trochanter, the heel and the occiput are not special
because more force passes through them; they are special because the force that does passes
through almost no tissue on its way to bone.

The honest limit, stated here because this is where the device is used: the engine's table is
**banded and capped**, and neither is true of the clinical quantity. Risk tools band, which is
why two people inside one band are not the same person and why a banded output is a prompt to
assess rather than a prediction (**consensus**). But tissue loading has no cap, and nothing at
all in `sWeightToDamageTable` corresponds to the term that actually decides the outcome — how much
load this particular tissue will take before it fails. That depends on perfusion, oxygenation,
nutrition, previous damage at the site and the moisture and temperature at the skin
(**mechanism**, **consensus**), and there is no field for it in `gPokedexEntries` or anywhere
else.

## The halving is keyed to a field in the move's data, not to how many battlers are hit

This is the support surface, and the detail is better than the idea.

```
   // src/pokemon.c, inside CalculateBaseDamage, in BOTH the physical and special branches:
   if ((gBattleTypeFlags & BATTLE_TYPE_DOUBLE)
    && gBattleMoves[move].target == MOVE_TARGET_BOTH
    && CountAliveMonsInBattle(BATTLE_ALIVE_DEF_SIDE) == 2)
       damage /= 2;
   ──────────────────────────────────────────────────────────────────────────────────────────
   move             .target in src/data/battle_moves.h   does the load get divided?
   ──────────────── ──────────────────────────────────── ───────────────────────────────────
   Rock Slide        MOVE_TARGET_BOTH                     YES — halved across two
   Surf              MOVE_TARGET_BOTH  (third gen)        YES — halved across two
   Earthquake        MOVE_TARGET_FOES_AND_ALLY            NO. It hits THREE battlers and
                                                           each takes the full figure
   ─────────────────────────────────────────────────────────────────────────────────────────────
   The division is conditional on a FIELD, not on the number of bodies in contact. And the
   third clause is the one to read twice: when only one defender is left standing, the
   halving does not apply and the survivor takes the undivided amount.
```

Spreading a load over more area means less at each point, and the engine will do it — but only
where it has been told the shape of the contact, and not at all for Earthquake, which is the move
that most obviously ought to qualify. A surface redistributes by **immersion** (the body sinks in)
and **envelopment** (the surface conforms around it), both of which are ways of saying *increase
the contact area* (**definitional**), and whether a given surface achieves them for a given
person depends on their shape, their weight and how the surface is set up — which is exactly the
engine's point that the division is a property of the specification rather than of the situation
(**mechanism**).

The `CountAliveMonsInBattle(...) == 2` clause is the heel. As contact area is lost, the load per
remaining point goes back up, and there is almost no tissue between the calcaneus and the skin to
redistribute into — so the only intervention that reliably works there is taking the heel out of
the load path altogether (**consensus**).

## `Reflect` halves it, and gives two-thirds when it has to cover two

```
   if ((sideStatus & SIDE_STATUS_REFLECT) && gCritMultiplier == 1)
   {
       if ((gBattleTypeFlags & BATTLE_TYPE_DOUBLE)
        && CountAliveMonsInBattle(BATTLE_ALIVE_DEF_SIDE) == 2)
           damage = 2 * (damage / 3);        ◄── TWO THIRDS when it covers two battlers
       else
           damage /= 2;                      ◄── a half when it covers one
   }
   ──────────────────────────────────────────────────────────────────────────────────────────
   Light Screen is the same code in the other branch of CalculateBaseDamage, split on
   IS_TYPE_PHYSICAL — m075's point, that the wrong barrier is unreachable code rather than
   weaker protection. The `gCritMultiplier == 1` guard is m042's: a critical hit ignores the
   screen entirely, so the protection has an exact documented bypass.
```

A barrier that has to cover more gives less at each point, implemented as a one-line difference
between a half and two thirds. That is a redistributing surface, and it is also the argument for
why the surface is never the whole plan: **Reflect reduces, and no reduction is a zero**. Every
loaded point is still loaded, the total force is unchanged, and the thing that produced the load
has not gone anywhere.

## `Protect` is the zero — and it fails if you use it last

```
   static void Cmd_setprotectlike(void)
   {
       u16 lastMove = gLastResultingMoves[gBattlerAttacker];
       if (lastMove != MOVE_PROTECT && lastMove != MOVE_DETECT && lastMove != MOVE_ENDURE)
           gDisableStructs[gBattlerAttacker].protectUses = 0;        ◄── reset, not decay

       if (gCurrentTurnActionNumber == (gBattlersCount - 1))
           notLastTurn = FALSE;                                      ◄── READ THIS ONE

       if (sProtectSuccessRates[protectUses] >= Random() && notLastTurn) { ... protected = 1; }
   }
   static const u16 sProtectSuccessRates[] =
       { USHRT_MAX, USHRT_MAX / 2, USHRT_MAX / 4, USHRT_MAX / 8 };
   ──────────────────────────────────────────────────────────────────────────────────────────
   Protect is the only thing in this answer that produces a true zero: nothing gets through
   at all. And it FAILS OUTRIGHT if the user is the last to act in the turn. Offloading has
   to happen BEFORE the load, not after it. A reposition performed after the tissue has
   carried the load for the whole interval has done nothing for that interval, and the
   notLastTurn flag is the engine agreeing.
```

So the two operations are two different objects, and they are not alternatives
(**mechanism**):

```
   Reflect  = a support surface      reduces magnitude everywhere, produces no zeros,
                                      changes nothing about the total force
   Protect  = a change of position   produces a zero for the structures it unloads, and
                                      only if it happens in time
   ─────────────────────────────────────────────────────────────────────────────────────────────
   A surface that permits a longer interval is still a surface that produces no zeros on its
   own.
```

Sitting is the worst case in the whole subject, and for the `Low Kick` reason rather than this
one: it concentrates most of the body's weight onto the ischial tuberosities, over the smallest
contact area in the body's repertoire, and it is held for the longest unbroken periods, because a
chair is where someone is put in order to be left safely (**mechanism**). A chair cushion is a
`Reflect`. It produces no zeros either, and a person who cannot shift their own weight in it is
accumulating load throughout.

The decay in `sProtectSuccessRates` is where this device stops, and the limit belongs here rather
than in a footnote. The halving models a *player* leaning on one answer repeatedly, and it resets
to zero the moment the last resulting move was not one of the family — m060's fact. It is not a
claim that repositioning works less well the more you do it, and nothing in the clinical
literature says that. The schedule is individualised to the person's skin response, their surface,
their posture and their tolerance of being moved, and the evidence that it is working is the skin
itself (**consensus**); the specific interval is weakly evidenced and locally set
(**country-dependent**).

## `Macho Brace` halves the Speed of whoever is wearing it, and nothing ever asks

```
   src/battle_main.c, GetWhoStrikesFirst:   if (holdEffect == HOLD_EFFECT_MACHO_BRACE)
                                                speedBattler1 /= 2;
   src/pokemon.c,     MonGainEVs:           if (holdEffect == HOLD_EFFECT_MACHO_BRACE)
                                                evIncrease *= 2;
   ──────────────────────────────────────────────────────────────────────────────────────────
   One item, attached for a benefit measured somewhere else entirely, imposing a standing
   halving in a place the player is not looking while it does so. Nothing in the games ever
   asks whether it is still wanted — m038's one-held-item-forever, doing a second job that
   fits exactly.
```

m004 names device-related damage as a category and lists the sites — oxygen tubing behind the
ears, mask edges, casts, splints, tube fixings, compression — as *every point under something you
attached on purpose*. What the **Macho Brace** adds is the mechanics of why it is a category at
all, and it has all three parts: the contact area is **small and fixed**, so magnitude per unit
area is high and the load does not redistribute as the person shifts; the load is **continuous**
for as long as the device is there; and the benefit it was applied for is **measured somewhere
else entirely**, which is why nobody looks (**mechanism**). In one of those cases — the collar,
the cast, the splint — removing the device to look is the thing you must not do, which makes it
the only site on the list where inspection itself needs a plan (**consensus**).

## The term `CalculateBaseDamage` does not have

Shear is the third property of load and the game has no object for it. Every term in the damage
pipeline is a **scalar**: base power, attack, defence and a stat-stage ratio inside
`CalculateBaseDamage`; then the critical multiplier, the type multiplier from `Cmd_typecalc`, and
`ApplyRandomDmgMultiplier`'s `100 - (Random() % 16)`, which is the familiar 85-to-100 band. Not
one of them has a direction.

The nearest thing the cartridge has is `FLAG_MAKES_CONTACT`, which m075 counts on 111 of 355 move
entries and which **Rough Skin**, **Iron Barbs** and a **Rocky Helmet** read without asking
anything about how hard the hit was — and m004 already uses that as rubbing being its own damage.
But a contact flag is a **boolean about whether two bodies touched**, not a direction, and shear
is entirely a question of direction. There is no vector anywhere in the pipeline, so there is
nothing to map the mechanism onto, and inventing one would be worse than saying so.

The clinical mechanism in plain terms: when the head of the bed is raised, the skin and
superficial tissue are held by friction against the sheet while the skeleton and deep tissue slide
downwards under gravity, deforming the tissue in between — at the sacrum above all
(**mechanism**). Sliding a person rather than lifting them does the same thing in a few seconds.
This is the point where manual handling and pressure area care stop being two subjects, and the
engine's silence about it is the largest single gap between this answer's device and its subject.
The other half of the silence is that the games have no concept of the load a body puts on itself
over time: m004 carries the time term, through the **Damp Rock**, and this answer deliberately
stops at the mechanics.

## Where the metaphor stops

Repositioning is something done *to* a person, several times a day and often at night, and nothing
above is written from their side.

It wakes people up. A schedule that is clinically sound and applied without negotiation produces
fragmented sleep, and fragmented sleep in hospital has consequences of its own. It can hurt — not
only in the obvious cases but in anybody with a painful joint, a recent operation or an injury —
and how that is assessed and managed is deliberately outside this answer and belongs to local
policy and to the person's own clinician. Being turned means being touched, often by somebody you
met this morning, often in a way that exposes you, and the entire difference between care and
handling lies in whether you were told what was about to happen and asked rather than instructed.

The hardest version is where the schedule and the person's wishes conflict. Someone may decline to
be moved, repeatedly, for reasons that are their own, and an adult who understands what is at
stake is entitled to decline. Where capacity is uncertain, where the preference persists and where
the consequence is serious, this stops being a bedside judgement and enters a framework about
capacity, consent and best interests that differs profoundly between countries. It is named here
and not reasoned about here: the reader's own legal framework is the only authority. The same
applies at the end of life, where comfort can displace prevention altogether and the right plan
may be one that accepts the risk — agreed with the person and those close to them, recorded, and
not a lapse in care.

And the context, because it decides whether any of the mechanics above ever happen.
Repositioning is staffing-limited: it usually needs more than one person, it competes with
everything else on the shift, and it is the task most easily postponed because its omission has no
immediate visible consequence. Pressure damage is also distributed in ways that track frailty,
deprivation and length of stay rather than anybody's technique. An institution that answers its
pressure ulcer rate by auditing turn charts, without changing establishment or equipment, has
chosen the one variable individuals cannot move.

## What Nurse Joy is listening for

The three properties of load, and which instrument measures which. Why interface pressure is a
surface, perpendicular measurement of damage that is frequently neither at the surface nor
perpendicular. Why redistribution and offloading are different operations, and which one produces
a zero. Heels, and why they are the clearest case in the subject. Why sitting is both the
highest-pressure posture and the longest-held one. The mechanism of shear when the head of the bed
is raised, and why sliding rather than lifting does the same thing in seconds. What the
tilt-versus-lateral argument is actually about — the greater trochanter — and why the angles and
intervals are consensus and local rather than mechanism. Device-related pressure injury as its own
category, with the mechanical reason. What sets tissue tolerance, and why a banded risk score is
therefore a prompt and not a prediction. And the local answers: which surface for whom, who
authorises it, how the schedule is individualised and recorded, and what happens when it is
declined.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The current **international guideline on the prevention and treatment of pressure ulcers**
  produced jointly by the major national pressure injury advisory panels — the document that
  settles the classification, the repositioning and support surface recommendations and the
  strength of evidence behind each, and which is revised on a cycle.
* The reader's national guidance on pressure ulcer prevention, which sets the risk assessment
  tool, the documentation requirement and the local reporting threshold.
* The reader's institutional policy on repositioning, support surface allocation and equipment
  provision, including who authorises which surface and how quickly it arrives.
* The reader's national manual handling guidance and local policy, for the sliding-versus-lifting
  argument, which is a staff injury question as much as a tissue one.
* The published literature on repositioning frequency and on support surfaces, which is where the
  weakness of the evidence for any specific interval lives and which should be read before
  asserting one.
* The reader's own legal framework on capacity, consent and best interests, for the refusal
  section. This is law and differs profoundly between countries.
* A current textbook of tissue viability or of soft tissue biomechanics, for deep tissue
  deformation and for shear.

The Pokémon material is from the **pret/pokeemerald** decompilation of Pokémon Emerald:
`sWeightToDamageTable` and `Cmd_weightdamagecalculation`, `Cmd_setprotectlike` with
`sProtectSuccessRates`, `Cmd_typecalc` and `ApplyRandomDmgMultiplier` in
`src/battle_script_commands.c`; `CalculateBaseDamage` with its Reflect, Light Screen and
multi-target clauses in `src/pokemon.c`;
`GetPokedexHeightWeight` and `gPokedexEntries` in `src/pokedex.c` and
`src/data/pokemon/pokedex_entries.h`; the `.target` fields in `src/data/battle_moves.h`; and
`HOLD_EFFECT_MACHO_BRACE` in `GetWhoStrikesFirst` in `src/battle_main.c` and in `MonGainEVs` in
`src/pokemon.c`. Every weight and height above was read out of the Pokédex entry data rather than
recalled, and the multi-target clause was checked in the source because a halving for
`MOVE_TARGET_FOES_AND_ALLY` would have been a plausible thing to assume and is not there.

## Scope and safety

This explains the mechanics of load in pressure ulcer prevention, through a game's damage
calculation, at the level of someone already training in or qualified for clinical practice. It is
not a repositioning policy, not a risk assessment tool and not a guide to selecting equipment for
anybody. It deliberately states no repositioning interval, no angle, no interface pressure figure
and no risk score, because all of those are set by the reader's national guidance and
institutional policy, which are the authority. It does not address the assessment or management of
pain associated with being moved, which is out of scope here and belongs to local policy and to
the person's own clinician. It is explicitly not a basis for any decision where someone is
declining to be repositioned, which involves capacity, consent and best interests and belongs to
the reader's legal framework. Nothing here has had clinical review. Nothing here is for use in an
emergency or for a decision about any person's care. If someone is unwell right now, the local
emergency number is the correct response.

## Where this stands, October 2026

The mechanical material is fixed and so is the physics: force, area and direction do not date, and
the finding that deep tissue fails before the skin shows it has been stable for a long time. The
classification of pressure injury and the terminology around it have been revised repeatedly and
will be again, so the international guideline is the place to check which version is current. What
is genuinely unsettled is repositioning frequency: the trial evidence is weak, the comparators are
inconsistent, and the interaction with the support surface is the plausible reason the results do
not converge — so expect the interval recommendations to keep moving while individualisation stays
put. Support surface technology, microclimate management and early-detection devices such as
subepidermal moisture measurement are all moving faster than the guidance about them. Everything
procedural is local, and the reader's national guidance and institutional policy are the authority
throughout.
