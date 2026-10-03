---
id: "m113"
slug: fitness-for-work-and-the-note
style: pokemon
category: general-practice
difficulty: intermediate
question: "Why is fitness for work a clinical judgement with no test, and what is a medical statement about fitness for work actually a statement about?"
tags: [fitness-for-work, certification, function, occupational-health, documentation]
---

# Cut examines nine tiles of ground and one thing about the Pokémon

This specialty's vocabulary is filters. m011 and m081 took the **Repel**, m082 took the nine
encounter-rate levers, m112 took the three rods. Every one of those filters what *comes at* you.
There is a fourth filter in the same cartridge and it has never been used here: the gate in front
of a field move, which filters what you may *do*. It is the one member of the family whose
conditions are almost entirely about the ground you are standing on, and that is exactly why it
belongs to this question.

Nothing in this answer is ill, nothing is being judged unfit, and no creature stands in for a
person whose health is in question. The object of study is `CursorCb_FieldMove` — the code that
decides whether a capability may be exercised here — and what is interesting about it is where it
looks.

## Three terms, three places, in a fixed order

```
   READ OUT OF src/party_menu.c AND THE fldeff_*.c FILES. Fourteen field moves, and
   the gate runs its tests in this order. Nothing later is reached if something
   earlier refuses.

   ─── 0 ── IS THE CAPABILITY PRESENT AT ALL ──────────────────────────────────────
       SetPartyMonFieldSelectionActions scans the four move slots against the
       fourteen-entry sFieldMoves table. A move not in a slot produces no menu
       entry, so the question is never asked.

   ─── 1 ── IS IT AUTHORISED ──────────────────────────────────────────────────────
       if (fieldMove <= FIELD_MOVE_WATERFALL && FlagGet(FLAG_BADGE01_GET + fieldMove) != TRUE)
             -> gText_CantUseUntilNewBadge

       The eight HM field moves line up with the eight badge flags BY ARITHMETIC:
       Cut/01, Flash/02, Rock Smash/03, Strength/04, Surf/05, Fly/06, Dive/07,
       Waterfall/08. The alignment is held by a source comment, not by a lookup
       table. The other six field moves are not gated at all.

   ─── 2 ── IS THE SITUATION RIGHT ────────────────────────────────────────────────
       sFieldMoveCursorCallbacks[fieldMove].fieldMoveFunc()
       Fourteen small functions. This is where almost all of the work happens, and
       almost all of it is about the world:

         Cut          a cuttable-tree object in front, OR a 3x3 square of tiles
                      around the facing position tested for elevation match,
                      collision and metatile behaviour  (5x5 with Hyper Cutter)
         Strength     a pushable-boulder object in front.  One condition
         Rock Smash   a breakable-rock object in front (or the Regirock braille)
         Flash        gMapHeader.cave == TRUE and the cave is not already lit
         Fly          Overworld_MapTypeAllowsTeleportAndFly(gMapHeader.mapType)
         Teleport     the same single question about the map type
         Dive         a dive warp exists under or over the current position
         Waterfall    the tile in front is a waterfall AND you are surfing north
         Dig          the current map permits Dig or an Escape Rope
         Secret Power the tile in front is a secret-base site, you are facing
                      NORTH specifically, and you do not already have a base
         Surf         PartyHasMonWithSurf() AND IsPlayerFacingSurfableFishableWater()
         Soft-Boiled  hp > maxHp / 5 on the selected Pokémon
         Milk Drink   the same function, the same test
         Sweet Scent  return TRUE.  No condition whatsoever

   THE TALLY, WHICH IS THE WHOLE ARGUMENT

     read only the world .................. 10 of 14
     read only the holder's own reserve .... 2 of 14  (and both are Soft-Boiled's test)
     read both ............................. 1 of 14  (Surf, the only one that asks
                                                       whether the party can do it)
     read nothing at all ................... 1 of 14  (Sweet Scent)

   AND THE REFUSAL MESSAGES, which are the system saying why

     PARTY_MSG_CANT_USE_HERE  ... ten of the fourteen entries
     PARTY_MSG_CANT_SURF_HERE ... Surf
     PARTY_MSG_NOTHING_TO_CUT ... Cut
     PARTY_MSG_NOT_ENOUGH_HP .... Soft-Boiled and Milk Drink

   Twelve of the fourteen refusals name the place or the absent task. Two name the
   holder. HERE is the word doing the work in ten of them.
```

## The same capability, usable or not depending on which way you are facing

Take one Pokémon with **Cut** in a slot, one badge in the case, and move it one step. Facing a
cuttable tree, `SetUpFieldMove_Cut` returns true on its first branch. Turn around and it falls to
the second branch, lays a 3×3 grid over the tile in front, and tests every cell for three separate
properties — is its elevation the same as yours, is it passable, is its metatile behaviour grass
it can cut. Nine cells, three tests each, and the answer can be no in all nine.

Nothing about the Pokémon changed. Its level did not change, its moves did not change, its
species did not change. The answer changed because the ground did.

And the one term that *is* about the Pokémon shows how small it is. **Hyper Cutter**
on the selected Pokémon swaps `CUT_NORMAL_SIDE` for `CUT_HYPER_SIDE`, widening the examined square
from 3×3 to 5×5. The standing property of the organism does not decide the answer. It widens the
window you look at the world through.

**Secret Power** is the limiting case and it is almost comic in how little of itself is about the
creature. It requires the tile in front to be a secret-base site, requires that you do not already
have a base, and requires you to be **facing north**. A capability, a badge-free move, and a
compass direction.

## There is no field anywhere that stores whether it can do the job

Here the cartridge has nothing, and saying so is the point rather than a gap.

A Pokémon in Generation III is four twelve-byte substructures. Between them they store the
species, the held item, experience, PP bonuses and friendship; four moves and four PP values; six
effort values and five contest stats and sheen; and then pokérus, the met location, the met level,
the game it was met in, which ball it came in, the original trainer's gender, six individual
values, the egg bit and the ability bit — and **thirty-two further bits of ribbons and awards**,
including a `marineRibbon`, a `landRibbon` and a `skyRibbon` that the games never distributed to
anybody.

There is room in that structure for three decorations that were never given out. There is no field
in it for whether this Pokémon can cut a tree.

Which is not an oversight. A stored answer would be wrong immediately, because the answer depends
on the tile in front of the player, and the tile in front of the player is not a property of the
Pokémon. So the engine does the only correct thing: it computes the answer at the moment of
asking, from the move slots, a flag somebody else set, and the ground. The absence of the field is
the mechanism.

## The two conditions that read the holder, and what they are attached to

Of the fourteen, exactly two read the holder's own reserve, and both are the same test:
`SetUpFieldMove_SoftBoiled` returns true only when the selected Pokémon's HP is strictly greater
than a fifth of its maximum. The two moves it gates, **Soft-Boiled** and **Milk Drink**, are the
two whose entire function is transferring resource to someone else.

That is a structural observation about where in the gate the one holder-keyed condition sits, and
it is deliberately not a claim about anybody's health. The house reading of the HP bar
comes from m001 nursing — a summary number standing in for the state it summarises — and the point
here is only about the *shape* of the conjunction: the conditions about the world are attached to
the tasks, and the single condition about the holder is attached to giving.

## The badge is held by somebody who has never seen the ground

`FlagGet(FLAG_BADGE01_GET + fieldMove)` is the first refusal, and the flag is set by a Gym Leader
who never meets the tile, never meets the tree, and is not consulted again. m015 established
badge-gating in this specialty as third-party authority, and it is worth noticing how differently
the two gates use the same eight flags. The obedience check reads **four** of them —
`FLAG_BADGE02_GET`, `04`, `06` and `08` — and compares the result against a *level*. The
field-move gate reads **all eight**, by arithmetic, and compares the result against a
*capability*. One register of authorisation, two gates, two different questions put to it.

Note also what the arithmetic gating means. `FLAG_BADGE01_GET + fieldMove` works only because the
first eight entries of the enum happen to be in badge order, and the source says so in a comment
rather than enforcing it. A capability list whose correctness is maintained by a comment is the
same shape as the hand-written `sSoundMovesTable` that m075 nursing found, and `sFieldMoves` has a
documented fragility of its own: it is terminated by a sentinel equal to `FIELD_MOVES_COUNT`, and
the source notes that any move sharing that value would be read as the end of the array. In the
shipped game nothing does, so this is a latent fragility and not a bug that fires — but it is the
shape of every hand-maintained list of what counts as work.

## Where the metaphor stops

The consequences of this judgement are mostly financial and they arrive immediately. For many
people the document is the difference between being paid and not, and the gap between a
clinician's sense of timescale and a household's is where the harm lives: a period chosen for
clinical tidiness can mean weeks without income. That is harm caused by the document rather than
by the illness, and it is invisible from inside the consultation.

It runs the other way too. Certification extended without review can be a slow harm, because long
absence is associated with a reduced chance of returning at all, and what is lost is not only
income but routine, contact and part of how somebody understands themselves. The direction of that
association is mainstream; its magnitude and how much of it is causal are argued about, and none
of it licenses pressing anybody back into work that is unsafe. Good work supports health better
than worklessness on average. Bad work does not, and that distinction matters more than the
generalisation.

And the part that no structure reaches. People asking for this document are often frightened — of
losing their job, of not being believed, of what happens if the answer is no — and the request
frequently arrives inside a consultation that was about something else. Being disbelieved while
unwell is its own injury, and it is distributed unequally: it falls hardest on people whose
symptoms are invisible, whose conditions fluctuate, whose first language is not the system's, and
who have been doubted before. None of the reasoning above touches that, and it is the part the
person will remember.

## What a Gym Leader is listening for

Whether the Trainer counts the tally rather than asserting that context matters: ten of fourteen
reading only the world, two reading the holder, one reading both, one reading nothing. Then the
refusal messages, with *here* identified as the operative word in ten of them. Then the one-step
demonstration — same Pokémon, same move, same badge, different tile — and **Hyper Cutter** named
as widening the window rather than deciding the answer. Then the absence, unprompted: three
undistributed ribbons stored and no field for capability, with the reason the field could not
exist. Then the badge as authority granted by somebody who has not seen the ground, with the
comment-maintained arithmetic noticed. Then the hardest one: how a Trainer would record a refusal
so that the next person reading it can tell which of the three terms failed.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The national sickness certification scheme applying where the reader works, issued by the
  relevant government department or social-security body: what the document is called, who may
  issue it, when it is required, what it may say, and what force it has (**country-dependent**).
* The guidance on sickness certification and fitness-for-work advice issued by the reader's own
  professional regulator and professional body, for the dual-role problem.
* The current occupational medicine textbook or national guidance for the reader's system, for
  job-demand analysis, adjustment and phased-return routes, and when occupational health referral
  is indicated.
* The published literature on work and health, read for effect sizes and for the limits of the
  causal claim, both of which are argued about.
* The equality or disability discrimination legislation applying where the reader works, for what
  adjustments an employer may be required to consider (**country-dependent**).

The Pokémon facts are a separate matter and are not covered by the line above. The fourteen-entry
`sFieldMoves` table and its sentinel, the eight HM field moves aligning with the eight badge flags
by the arithmetic `FLAG_BADGE01_GET + fieldMove` with the alignment noted in a source comment, the
order of the three gate tests in `CursorCb_FieldMove`, the individual conditions of
`SetUpFieldMove_Cut` (including the 3×3 square tested for elevation, collision and metatile
behaviour, and **Hyper Cutter** widening it to 5×5), `_Strength`, `_RockSmash`, `_Flash`, `_Fly`,
`_Teleport`, `_Dive`, `_Waterfall`, `_Dig`, `_SecretPower` (including the facing-north
requirement), `_Surf`, `_SoftBoiled` (HP strictly greater than a fifth of maximum) and
`_SweetScent` returning TRUE unconditionally, the four refusal message identifiers and their
distribution across the fourteen entries, and the contents of the four Generation III Pokémon
substructures including the never-distributed `marineRibbon`, `landRibbon` and `skyRibbon` bits,
were all read directly from the pret decompilation projects, which this environment can reach.
These are Emerald's; Ruby and Sapphire differ in which move opens the Regirock and Registeel
chambers, which the source itself notes.

## Scope and safety

This is revision material about the structure of a fitness-for-work judgement, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here should inform whether any individual is certified, for how long, or on
what terms — that belongs with the clinician assessing them and with the national scheme in
force. No
duration, threshold, criterion or form wording is named here on purpose: all are country-specific
and all are revised. **"Capacity for work" in this answer means functional ability against job
demands, and is not mental capacity** — decision-making capacity, consent and the law around them
are a separate subject, are deliberately not treated here, and are governed by their own local
legislation. The badge flags, tile tests, HP fractions and ribbon bits above are real and stand in
for a mechanism; none of them is a clinical quantity and no clinical figure should be read out of
them. If someone is unwell right now, the relevant action is to contact local urgent care or the
local emergency number, not to read this.

## Where this stands, October 2026

The structural claims — that fitness for work is a relation between function, task and adjustment,
that no test can measure a relation, and that the diagnosis is the weakest of the available
predictors — are mechanism and will not move. Everything institutional will: the name and format
of the document, who may issue it, the waiting period before it is required, whether it can
recommend adjustments, how it interacts with income protection, and how far issuing has been
extended beyond doctors. Several countries have changed more than one of those in the last decade
and the direction is not uniform. The evidence base on work and health has grown and remains
contested in magnitude. The Emerald code is stable because the games are finished. Take the scheme
itself from current national guidance rather than from here, as of October 2026.
