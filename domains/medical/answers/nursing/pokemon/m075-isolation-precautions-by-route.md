---
id: "m075"
slug: isolation-precautions-by-route
style: pokemon
category: nursing
difficulty: core
question: "Why are isolation precautions keyed to the route of transmission rather than to the organism, and what follows from that?"
tags: [infection-prevention, transmission-based-precautions, ppe, isolation, standard-precautions]
---

# Read the four barrier descriptions. Not one of them names a species.

The games are unusually explicit here, and the quickest route into the argument is to put the
printed text of four protections side by side. These are the descriptions as they appear in the
data:

```
   Protective Pads   "Protects from effects triggered by making contact."
   Long Reach        "Moves don't make contact."
   Safety Goggles    "Protects from weather damage, powder and spores."
   Soundproof        "Avoids sound-based moves."
   ──────────────────────────────────────────────────────────────────────────────────────────
   Four protections. Every one of them is defined by a PROPERTY OF THE INCOMING MOVE —
   contact, powder, sound — and not one of them mentions who is throwing it, what type it
   is, or what species is holding anything. The barrier is keyed to the route. That is not
   a reading of the games; that is the games' own wording.
```

## The route the Advance games encode properly: contact, as a flag on the move

`FLAG_MAKES_CONTACT` is a bit in each move's own entry, and in Emerald it is set on **111 of the
355 entries** in the move table — one of which is the null move, so 111 out of 354 real ones. Six
abilities read that bit and nothing else about the attacker:

```
   ability        holder, in the Advance games   what it does on contact
   ─────────────  ─────────────────────────────  ─────────────────────────────────────────
   Rough Skin     Carvanha, Sharpedo             maxHP/16, every time, no roll
   Poison Point   Qwilfish                       poisons, one in three
   Static         Pikachu                        paralyses, one in three
   Flame Body     Magcargo (second ability)      burns, one in three
   Effect Spore   Parasect                       one in TEN, then sleep, poison or burn
   Cute Charm     several                        one in three, with further conditions
   ──────────────────────────────────────────────────────────────────────────────────────────
   Six abilities, SIX DIFFERENT consequences, ONE condition. None of them asks what the
   attacker is. All of them ask what the move did. And the flag is on the move, not on
   either battler, which means the route is a property of the act — which is the whole
   of the real argument in one bit.
   ──────────────────────────────────────────────────────────────────────────────────────────
   Note also what they do NOT care about: not the type, not the power, not the species,
   not whether anybody knew in advance. Earthquake has 100 base power and does not trigger
   one of them. Tackle has 35 and triggers all six.
```

## The route encoded as a hand-written list, and why that is worse

**Soundproof** is checked differently. There is no sound flag in the Advance move data. Instead
`AbilityBattleEffects` walks `sSoundMovesTable`, which is this, in full:

```
   static const u16 sSoundMovesTable[] =
   {
       MOVE_GROWL, MOVE_ROAR, MOVE_SING, MOVE_SUPERSONIC, MOVE_SCREECH, MOVE_SNORE,
       MOVE_UPROAR, MOVE_METAL_SOUND, MOVE_GRASS_WHISTLE, MOVE_HYPER_VOICE, SOUND_MOVES_END
   };
   ─────────────────────────────────────────────────────────────────────────────────────────
   TEN moves and a sentinel. Somebody typed them. Anything that is audible and is not on
   that list is not covered, and the gap is invisible from either side: Soundproof's text
   still says "Avoids sound-based moves."
   ─────────────────────────────────────────────────────────────────────────────────────────
   Contact: a flag, set on each of 111 moves as part of its own definition, so a new move
            carries its route with it.
   Sound:   a list, maintained separately, that a new move has to be remembered into.
   ─────────────────────────────────────────────────────────────────────────────────────────
   Same design intention, two implementations, and the second one fails silently. A
   precaution framework that enumerates conditions rather than describing routes has the
   list problem, and it is the reason route descriptions are written as mechanisms.
```

The powder family is the same shape from the other direction. **Spore**, **Sleep Powder** and
**Stun Spore** are all Grass-type status moves in the Advance games, and there is no powder flag
there at all — no shared property for anything to key off. The later item **Safety Goggles** is
what a route looks like once somebody has given it a name.

## Matching the barrier to the route: Reflect and Light Screen are in different branches

This is the part that settles it, and it is a fact about the damage calculation rather than about
any move's description. `CalculateBaseDamage` splits on `IS_TYPE_PHYSICAL(type)`, and the two
screens are applied inside the two halves:

```
   if (IS_TYPE_PHYSICAL(type)) {
         ... Apply Reflect:       if (sideStatus & SIDE_STATUS_REFLECT && gCritMultiplier == 1)
   } else {
         ... Apply Light Screen:  if (sideStatus & SIDE_STATUS_LIGHTSCREEN && gCritMultiplier == 1)
   }
   ───────────────────────────────────────────────────────────────────────────────────────────
   Put up REFLECT against a special attack and nothing happens — and the reason is not that
   it is weaker. The code that would consult it is in the other branch and is never reached.
   This is the type-effectiveness zero of m007 in a different costume: not reduced
   protection, NO protection, and no amount of re-applying it changes the branch.
   ───────────────────────────────────────────────────────────────────────────────────────────
   And in the Advance games the branch is chosen by the move's TYPE, which is m026's device:
   for three generations the category was derived from what the move was, and the fourth
   generation split it per move. That is precisely the shift this question is about — from
   keying a response to an identity to keying it to the actual mechanism of travel — and the
   games made it in 2006.
```

Three more properties of the screens, each of which has a direct counterpart:

**They are side statuses, not held items.** `gSideStatuses` carries them, under the header's own
comment, *per-side statuses that affect an entire party*. The barrier belongs to the area rather
than to an individual, which is what cohorting is. And in a double battle with two battlers still
up on the defending side the reduction is two-thirds rather than a half — the same barrier,
diluted by how many it is covering.

**Re-applying one does nothing.** `Cmd_setreflect` checks `SIDE_STATUS_REFLECT` first and, if it
is already set, flags the move as having missed. No top-up, no extended timer. m057 to m059 are
built on the same refusal in a different system.

**You are told it has gone after it has gone.** The timer is five turns; it is decremented at end
of turn; and `BattleScript_SideStatusWoreOff` prints *after* the decrement reached zero. The
notification that the barrier is down arrives when the barrier is already down, which is the
strongest argument in the whole answer for why the removal step — and not the application step —
is the one to get right.

**And one specific act removes both.** **Brick Break**, 75 base power, 100 accuracy, strips
**Reflect** and **Light Screen** before it lands. One move, named, that defeats a barrier which
was holding perfectly well against everything else.

## One barrier, one route, and the cupboard does not cover the field

```
   barrier          covers                        does NOT cover
   ───────────────  ────────────────────────────  ─────────────────────────────────────────
   Reflect          physical damage, halved        anything in the special branch
   Light Screen     special damage, halved        anything in the physical branch
   Safeguard        status conditions, 5 turns     damage of either kind, stat drops
   Mist             stat reductions               damage, status
   Soundproof       ten listed moves              the eleventh audible one
   Protective Pads  contact-triggered effects      the damage the contact move did
   ──────────────────────────────────────────────────────────────────────────────────────────
   m040 reads a table like this to show that no single protection covers everything. The
   point here is the complementary one and it is more useful: the question is never "is this
   barrier enough", it is "is this the barrier for THIS route" — and a Reflect against a
   special attack is not partial credit. It is a zero with the cost of a turn attached.
```

## Where identity enters: it changes the agent, never the route

Identity is not irrelevant, and the games are precise about where it enters. A critical hit walks
through both screens because `gCritMultiplier` is no longer 1. **Magic Guard** is exempt from
**Sticky Barb**. **Infiltrator**, a later-generation ability, ignores screens entirely. In every
one of those cases what changed is the **agent that gets through**, never which route the thing
was travelling by. Same route, different counter — which is the exact shape of an organism that
needs soap and water rather than hand rub.

## Where the metaphor stops

Flags, lists and branches are a fair picture of why a barrier has to match a route, and nothing
above is a person. The next part is, and the analogy has nothing to offer it.

Isolation is experienced as something done to a person. A door that stays shut, people who come in
dressed differently and leave sooner, a cancelled visit, meals delivered rather than shared, and
often no clear explanation of why, for how long, or what would end it. People describe feeling
contaminated and feeling blamed, and neither of those is an effect of any pathogen.

Nearly all of that is modifiable without weakening a single barrier: explaining the route rather
than the diagnosis, giving a timescale and the criteria that would end it, keeping the observation
frequency the clinical condition requires rather than the one the gowning makes convenient, and
arranging the contact that is still possible. None of those is a trade against infection control.
They are the parts of the intervention most often left out, because nothing counts them.

And isolation decisions are sometimes restrictions on where a person may go. Where that becomes a
deprivation of liberty it is a legal question, governed by the law of the jurisdiction, differing
profoundly between countries, and nothing in a revision note substitutes for it.

## What Nurse Joy is listening for

Why four printed descriptions that name routes and no species is the whole argument. What it means
that `FLAG_MAKES_CONTACT` lives on the move rather than on either battler, and why six abilities
with six different effects share one condition. Why a hand-written list of ten is a worse
implementation of the same idea than a flag on 111 moves, and what the clinical version of the
eleventh audible move is. Why **Reflect** against a special attack is a zero rather than a
reduction. Why a side status is the right shape for cohorting, and what the two-thirds in a double
battle corresponds to. Why being told the screen wore off *after* it wore off is the argument for
the removal sequence. And what changes when the organism is finally named — because in this
reading the answer is the agent, and never the route.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to this
answer:

* The reader's national infection prevention and control guidance, for the precaution categories
  as named locally, the assignment of conditions to routes and the aerosol-generating procedure
  list. This is the most country-dependent material here and the frameworks genuinely differ.
* The reader's institutional infection prevention policy, for room placement, cohorting, the
  personal protective equipment donning and removal sequence, the approved disinfectants and
  contact times, and the criteria for stepping precautions down.
* The reader's guidance on respiratory protective equipment, for fit testing and fit checking.
* The reader's national hand hygiene guidance, for which organisms require soap and water rather
  than alcohol-based hand rub.
* A current textbook of infection prevention and control, for the physics of droplet and airborne
  transmission and for the limits of that distinction.
* The published literature on the adverse consequences of contact isolation — observational, with
  the magnitude contested.
* The capacity and deprivation-of-liberty legal framework of the reader's jurisdiction, for
  anything restricting where a person may go.

Separately, and unlike the above: the printed descriptions of **Protective Pads**, **Long Reach**,
**Safety Goggles** and **Soundproof**; the count of 111 `FLAG_MAKES_CONTACT` entries among the
move table's 355; the six abilities gated on that flag with their holders and their one-in-three,
one-in-ten and unconditional rates; the ten entries of `sSoundMovesTable` and its sentinel; the
absence of any powder flag in the Advance data; the `IS_TYPE_PHYSICAL` split and the placement of
**Reflect** and **Light Screen** inside its two branches with their shared `gCritMultiplier == 1`
condition; the two-thirds reduction in a double battle; the header comment on `gSideStatuses`; the
five-turn timers, the failure of `Cmd_setreflect` on an existing screen and the position of the
wore-off message after the decrement; **Brick Break**'s 75 and 100; and **Earthquake**'s 100
against **Tackle**'s 35 were all read directly out of the public disassemblies of the games and
their expansion, which this environment could reach. **Protective Pads**, **Long Reach**, **Safety
Goggles** and **Infiltrator** are not Advance-generation features and were read from the
expansion; no generation number is claimed for them here.

## Scope and safety

This explains why precautions are organised by transmission route, for someone already training in
or qualified for clinical practice. It is not a protocol, not a decision aid and not a personal
protective equipment procedure: it deliberately names no donning or removal sequence, no
disinfectant, no contact time, no aerosol-generating procedure list, no route assignment for any
named condition and no stepping-down criterion, and the only numbers in it belong to a video game.
All of those are set by national and institutional infection prevention policy, which is the
authority; this is not, and it has had no clinical review. It is explicitly not guidance on
restricting a person's movement, which is a legal and capacity matter governed by the law where
the reader works. Nothing here is for use in an emergency or for a decision about any person's
care. If someone is unwell right now, the local emergency number is the correct response.

## Where this stands, October 2026

The design principle is stable and will outlast every list attached to it: precautions are keyed
to route because the route is inferable before the organism is named. What has moved, and is still
moving, is the droplet-airborne boundary and everything downstream of it — which conditions sit
where, which procedures count as aerosol-generating, what respiratory protection is specified for
which task, and how ventilation is accounted for. Several national bodies have revised their
positions in recent years and they do not all agree, so two readers in two countries will
correctly give different answers to the same specific question. Step-down criteria, disinfectant
lists and removal sequences are institutional and change with procurement and policy review. The
local framework is the authority for all of it. The game facts are pinned where they belong: the
flag, the list, the branch and the screens are read out of the Advance-generation code, the four
later counters out of the expansion, and the per-move damage category is noted as a
fourth-generation change rather than presented as always having been so.
