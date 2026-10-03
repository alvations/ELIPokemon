---
id: "m136"
slug: the-home-visit
style: pokemon
category: general-practice
difficulty: intermediate
question: "What changes about a clinical assessment when it happens in someone's home rather than in a consulting room, and why is the environment itself part of the information?"
tags: [home-visit, assessment, context, housebound, decision-making]
---

# A house in Emerald is twenty-eight bytes, and three of them are permissions

This specialty's vocabulary is filters. m011 and m081 took the **Repel**, m082 took the nine
encounter-rate levers, m112 took the three rods and the fact that fishing runs no filter at all,
and m113 took the fourth member of the family — the gate in front of a field move, whose
conditions are almost entirely about the ground you are standing on.

This answer stays with that fourth filter and walks it indoors, because indoors is where the world
stops saying yes. Nothing here is ill, no creature stands in for a person, and the thing being
studied is a **map**: `struct MapHeader` in `include/global.fieldmap.h`, and what changes about a
Trainer's capabilities when the header under their feet is somebody's house.

## The whole environment is twenty-eight bytes, and you are not told its name

```
   READ OUT OF include/global.fieldmap.h AND data/maps/.../map.json.
   The header is a 28-byte struct. Here is the one for the ground floor of
   Brendan's house in Littleroot Town, field for field as the JSON states it.

   ─── WHAT KIND OF PLACE THIS IS ────────────────────────────────────────────────
       map_type .................... MAP_TYPE_INDOOR      (8 of 10 defined types)
       region_map_section .......... MAPSEC_LITTLEROOT_TOWN
       weather ..................... WEATHER_NONE
       requires_flash .............. false
       cave ........................ (not set)
       connections ................. null        <- no neighbours. ONE way out,
                                                   and it is a warp, not an edge

   ─── THREE BITS THAT ARE PERMISSIONS, NOT PROPERTIES ───────────────────────────
       allow_cycling ............... false    read by Overworld_IsBikingAllowed()
       allow_escaping .............. false    read by CanUseDigOrEscapeRopeOnCurMap()
       allow_running ............... false
       show_map_name ............... false    you are not even told where you are

   THE POINT: not one of those three bits is about the Trainer. The Mach Bike is
   still in the bag. The Running Shoes are still on. An Escape Rope is still an
   Escape Rope. The capability did not change; the room did, and the room is
   where the permission is stored.

   AND THE REFUSAL NAMES THE PLACE, NOT THE ITEM. Use an Escape Rope in a house
   and ItemUseOutOfBattle_EscapeRope falls to the else branch, which prints
   gText_DadsAdvice: DAD's advice - there's a time and place for everything.
   The item is fine. The advice is about where you are standing.
```

Four of the ten map types — `MAP_TYPE_ROUTE`, `MAP_TYPE_TOWN`, `MAP_TYPE_OCEAN_ROUTE` and
`MAP_TYPE_CITY` — make `Overworld_MapTypeAllowsTeleportAndFly` return TRUE. `MAP_TYPE_INDOOR` is
not one of them, and neither is `MAP_TYPE_SECRET_BASE`, the other indoor type, which is a house
the Trainer built. So **Fly** and **Teleport** are gone the moment the door closes behind you: not
weakened, not less accurate, unavailable, and unavailable because of a comparison against a byte
of the room.

## Indoors, eleven of the fourteen field moves are refused by the room

m113 counted the gate's conditions and found ten of fourteen reading only the world. Stand in a
house and that tally turns into an outcome.

```
   THE FOURTEEN FIELD MOVES, EVALUATED ON THE FLOOR OF A HOUSE

   refused by the room
     Fly ............ Overworld_MapTypeAllowsTeleportAndFly(MAP_TYPE_INDOOR) = FALSE
     Teleport ....... the same single question about the map type
     Dig ............ the map does not permit Dig or an Escape Rope
     Flash .......... gMapHeader.cave is not TRUE
     Cut ............ no cuttable-tree object, and the 3x3 square of tiles in front
                      holds no cuttable metatile behaviour
     Strength ....... no pushable-boulder object in front
     Rock Smash ..... no breakable-rock object in front
     Surf ........... IsPlayerFacingSurfableFishableWater() = FALSE
     Waterfall ...... the tile in front is not a waterfall, and you are not surfing
     Dive ........... no dive warp under or over this position
     Secret Power ... the tile in front is not a secret-base site
                      (eleven refusals, ten of them printing PARTY_MSG_CANT_USE_HERE)

   still available
     Soft-Boiled .... hp > maxHp / 5 on the selected Pokemon
     Milk Drink ..... the same function, the same test
                      (the two that read the holder instead of the world - and
                       both of them are moves whose function is GIVING something)
     Sweet Scent .... SetUpFieldMove_SweetScent is "return TRUE". No condition.

   And Sweet Scent is the interesting one, because the gate says yes and the
   world still has nothing. Indoors GetCurrentMapWildMonHeaderId() returns
   HEADER_NONE, the player's tile is not MetatileBehavior_IsLandWildEncounter,
   SweetScentWildEncounter() returns FALSE - and it returns FALSE only AFTER the
   screen has already faded red, at which point FailSweetScentEncounter hands
   over to EventScript_FailSweetScent. The permission, the animation, and then
   nothing.
```

Three capabilities out of fourteen survive the doorway. The two that survive on the holder's own
reserve are the two that hand something over, and the one that survives unconditionally is the one
that asks the world a question the world indoors cannot answer.

## No encounter table, so nothing comes at you — the information is in the furniture

Every pair in this specialty so far has been about something arriving: a slot rolled out of a
twelve-entry table, a rate test against 2 880, a filter deciding whether the roll happens. **An
indoor map has no entry in `src/data/wild_encounters.json` at all.** There is no table, no rate,
no slot, and therefore nothing for the Repel or for **Keen Eye** to cancel. The two filters this
specialty was built on have no work to do in a house.

What the house has instead is furniture, and the furniture has to be asked.

```
   src/field_control_avatar.c. Press A and GetInteractionScript tries FOUR sources,
   in this fixed order, returning the first that is not NULL:

     1  GetInteractedObjectEventScript   the people and things placed on the map
     2  GetInteractedBackgroundEventScript   signs, and hidden items
     3  GetInteractedMetatileScript      the furniture itself
     4  GetInteractedWaterScript         water in front of you

   SOURCE 3 IS ONE FUNCTION WITH TWENTY-EIGHT TESTS IN IT, hand-written, in order:

     always evaluated ........................ 20 tests
       a TV screen, a PC, a closed door in Sootopolis City, a Sky Pillar door, a
       cable box, a Pokéblock feeder, the Trick House puzzle door, a region map,
       the Running Shoes manual, a picture bookshelf, an ordinary bookshelf, a
       Pokémon Center bookshelf, a vase, a trash can, a shop shelf, a blueprint,
       a wireless box, a second cable box, a questionnaire, a Trainer Hill timer

     only when your elevation equals the tile's .. 7 tests
       the Secret Base PC, the record-mixing PC, a sand ornament, a shield or toy
       TV, and three classes of decoration

     only when it does NOT ....................... 1 test  (a Secret Base poster)

     and three of the twenty-eight also ask WHICH WAY YOU ARE FACING
       the TV screen, the wireless box results, the second cable box

   The ground floor of Brendan's house carries 7 object events, 3 warps,
   4 coord events and 0 background events. Four of those coord events fire
   because you WALKED ONTO A TILE: MOM speaks without being asked.
```

So the house is not quiet, it is differently indexed. Nothing is rolled at you. Everything is
either placed where you must stand to read it, or scripted to fire because you crossed a
particular tile — and the list of furniture that answers at all is maintained by hand,
twenty-eight entries long, in the same shape as the hand-written `sSoundMovesTable` nursing m075
found and the comment-maintained `sFieldMoves` alignment of m113.

## The Itemfinder reports presence and a direction, and that is its entire output

The one instrument in the bag that is built to find what is in a place rather than what is coming
at you is the **Itemfinder**, and it is worth reading because its honesty is unusual.

`ItemfinderCheckForHiddenItems` walks the map's background events, keeps only those of kind
`BG_EVENT_HIDDEN_ITEM` whose flag — `hiddenItemId + FLAG_HIDDEN_ITEMS_START` — has not already
been set, and accepts any whose offset from the player lies within **seven metatiles horizontally
and five vertically**: a 15-by-11 rectangle, wider than it is tall because that is the shape of
the screen. It then checks the adjoining maps through the connections as well. Where two
candidates are in range, `SetDistanceOfClosestHiddenItem` keeps the one with the smaller sum of
absolute offsets, breaking a tie on the vertical and then on whichever is further south.

And then it tells you almost nothing. Four beeps, and one of exactly three strings:
`gText_ItemFinderNothing` when the rectangle was empty, `gText_ItemFinderNearby` after the player
has been turned to face the nearest candidate, or `gText_ItemFinderOnTop` when you are standing on
it, delivered by spinning the player through the four directions. No distance. No identity. No
count. An instrument that says *there is something here and it is that way*, which is more than
nothing and much less than a finding.

## What the cartridge does not have, and it is the half that matters most

Here the game has nothing, and saying so is better than inventing something.

There is no mechanic for being a guest. A Trainer in Hoenn walks into any house in any town
without knocking, crosses the room, reads the bookshelf, examines the trash can and leaves, and no
flag is set, no permission is asked, nobody objects and no door is ever locked against them. The
engine models the *room* in detail — twenty-eight bytes, three permission bits, twenty-eight
furniture tests — and models the entering of it not at all.

Which is exactly backwards from the thing being explained, and the gap is worth leaving visible
rather than papering over. Everything above is a good model of how a place changes what can be
done in it. Nothing above is a model of whose place it is. The second half of that is in the
plain-prose section below, where it belongs.

## Where the metaphor stops

Being assessed at home is not a neutral experience. For some people it is a relief — not having to
dress, get into a car or be helped into a building. For others it is an intrusion at the worst
possible time, in a house they are ashamed of, in front of a relative they did not want involved.
Both reactions are common and neither is a mistake.

What a clinician sees in a house is a home, and a home is not a presentation. An untidy kitchen is
not neglect. A cold room may be a choice, a tariff or an inability to pay, and those are different
problems with different answers. Reading poverty as decline, or decline as poverty, are both
errors, both are made quickly, and both are made silently. The cost falls on somebody who has just
let a stranger into the only space they control.

Two things that arise in houses are not treated anywhere in this pair. Where a visit raises a
concern about someone's safety, or about whether they are able to make a particular decision,
those are governed by legislation and local procedure that differ by jurisdiction, they cannot be
reasoned out from mechanism, and they are deliberately out of scope.

And the asymmetry of the ending. The clinician leaves and the day continues; the person stays in
the situation that was just assessed, usually with less certainty than the plan implies. Some of
the decisions made in houses are about where somebody is going to live, which is among the most
consequential conversations in this specialty, and it is not improved by being held standing up in
a hallway.

## What a Gym Leader is listening for

Whether the Trainer identifies the three permission bits as properties of the *room* and not of
the bag, and says that `gText_DadsAdvice` names the place rather than the item. Then the four map
types that allow **Fly** and **Teleport**, with `MAP_TYPE_INDOOR` and `MAP_TYPE_SECRET_BASE`
excluded. Then the tally: eleven of fourteen field moves refused indoors, the two survivors
reading the holder's own reserve, **Sweet Scent** passing its gate and failing on the world after
the screen has already flashed. Then the absence of an encounter table, with the consequence that
this specialty's two filters have nothing to cancel. Then the four interaction sources in order,
and the twenty-eight hand-written metatile tests split 20 / 7 / 1 with three reading the facing.
Then the **Itemfinder**'s 15-by-11 rectangle and its three strings. Then the honest gap — that
nothing in the engine models knocking — and why it is left stated rather than filled.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The reader's own national and local arrangements for home visiting and out-of-hours care — who
  is obliged to visit, who decides, what is carried and how it is recorded
  (**country-dependent**).
* The guidance on comprehensive assessment of older people, and on frailty identification, issued
  by the reader's national body or geriatric medicine society.
* The safeguarding procedure and the capacity legislation in force where the reader works, which
  govern the two situations this pair explicitly does not treat (**country-dependent**).
* The reader's own organisation's lone-working policy, which governs clinician safety on visits
  and is local without exception.
* The published literature on home-based assessment, hospital-at-home and admission-avoidance
  services, read for which outcomes move and which do not.

The Pokémon facts are a separate matter and are not covered by the line above. The 28-byte
`MapHeader` and its `allowCycling`, `allowEscaping`, `allowRunning` and `showMapName` bitfields;
the JSON for the ground floor of Brendan's house in Littleroot Town, including `MAP_TYPE_INDOOR`,
`WEATHER_NONE`, null connections and its event counts; the ten `MAP_TYPE_` constants and the four
that `Overworld_MapTypeAllowsTeleportAndFly` accepts; `Overworld_IsBikingAllowed` and
`CanUseDigOrEscapeRopeOnCurMap` reading one bit each; `gText_DadsAdvice` as the escape-rope
refusal; the fourteen field-move conditions as m113 read them; `SweetScentWildEncounter` returning
FALSE on `HEADER_NONE` and `FailSweetScentEncounter` handing to `EventScript_FailSweetScent`; the
four sources tried by `GetInteractionScript` and the twenty-eight `MetatileBehavior_` tests inside
`GetInteractedMetatileScript`; and `ItemfinderCheckForHiddenItems` with its seven-by-five offset
window, its flag check and its three message strings, were all read directly from the pret
decompilation projects, which this environment can reach. These are Emerald's; other cartridges
differ, and the generation has to be stated or the number should not be.

## Scope and safety

This is revision material about the structure of an assessment carried out in someone's home,
written for someone already training in or qualified for the field. It is not a clinical
reference, not a decision aid, and nothing here should inform a decision about whether any
individual is visited, assessed, moved or admitted. No equipment list, visiting criterion,
interval or threshold appears here on purpose: all are local, several are contractual and all are
revised. **Safeguarding and mental capacity are deliberately out of scope**, because both are
governed by legislation and local procedure that differ by jurisdiction. The map types, permission
bits, tile offsets and message identifiers above are real and stand in for a mechanism; none of
them is a clinical quantity and no clinical figure should be read out of them. If someone is
unwell right now, the relevant action is to contact local urgent care or the local emergency
number, not to read this.

## Where this stands, October 2026

The structural claims — that information rises and capability falls, that the visited population
is selected rather than representative, that the live decision is often about where care happens
rather than what the diagnosis is, and that the net has to have a named holder — are mechanism and
consensus and will not move. The arrangements will: who visits, whether visiting is contractual,
which member of the team does it, what portable testing exists and what hospital-at-home capacity
sits behind it. Portable diagnostics have widened what can be carried through a door and that
widening is ongoing. The Emerald code is stable because the games are finished. Take the
arrangements from current local guidance rather than from here, as of October 2026.
