---
id: "m112"
slug: the-remote-consultation
style: pokemon
category: general-practice
difficulty: intermediate
question: "What does a remote consultation lose and gain compared with a face-to-face one, and why does the triage decision move rather than disappear?"
tags: [remote-consulting, telephone-triage, access, channel, safety-netting]
---

# The Old Rod cannot produce a Corphish, and it is not a worse Super Rod

m082 established the distinction this question needs: the encounter **rate** is how often you are
asked, the encounter **table** is what the answer can be, and the nine rate levers do not touch a
single slot. It also noted in passing that the three rods restrict *what is reachable* rather than
*how often*. This answer is that passing remark done properly, because the rods turn out to be the
cleanest statement in the cartridge of what a channel is.

Four instruments work Route 102. Walking its grass, surfing its water, and fishing that same water
with each of three rods. These are not four grades of one instrument. They read four different
tables, and two of them have no species in common at all.

## Four instruments, one map, four tables

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE EMERALD ENCOUNTER DATA AND THE WILD
   ENCOUNTER ROUTINE. Generation III declares each slot vector once, at the top of
   src/data/wild_encounters.json, and then gives species and levels per map.

   WALKING THE GRASS — twelve slots, 20 20 10 10 10 10 5 5 4 4 1 1
   table rate 20, so 20 x 16 = 320 against MAX_ENCOUNTER_RATE 2880  =  11.11% a step

     20  Poochyena lv3     10  Lotad     lv3      4  Zigzagoon lv4
     20  Wurmple   lv3     10  Lotad     lv4      4  Ralts     lv4
     10  Poochyena lv4      5  Zigzagoon lv3      1  Zigzagoon lv4
     10  Wurmple   lv4      5  Zigzagoon lv3      1  Seedot    lv3

   SURFING THE SAME WATER — five slots, 60 30 5 4 1
   table rate 4, so 64/2880  =  2.22% a step

     60  Marill  lv20-30     5  Marill  lv30-35     1  Goldeen lv20-30
     30  Marill  lv10-20     4  Marill  lv5-10

   FISHING THAT SAME WATER — ten slots in one table, indexed by three DISJOINT groups
   old_rod [0,1]   good_rod [2,3,4]   super_rod [5,6,7,8,9]
   no rate test at all; FishingWildEncounter starts a battle every time it is reached

     OLD ROD    70  Magikarp lv5-10        30  Goldeen  lv5-10
     GOOD ROD   60  Magikarp lv10-30       20  Goldeen  lv10-30    20  Corphish lv10-30
     SUPER ROD  40  Corphish lv25-30       40  Corphish lv30-35    15  Corphish lv20-25
                 4  Corphish lv35-40        1  Corphish lv40-45

   NOW READ IT BY SPECIES, WHICH IS WHERE THE ARGUMENT IS

     Marill      only by surfing      99 % of the surf table, unreachable by any rod
     Magikarp    only by rod          70 % of the Old Rod, 60 % of the Good Rod,
                                      and 0 % of the Super Rod
     Corphish    only by Good or      20 % of the Good Rod, 100 % of the Super Rod,
                 Super Rod            and NOT IN the Old Rod's table at any percentage
     Poochyena   only on land         30 % of the grass, in no water table anywhere

   THE OLD ROD AND THE SUPER ROD SHARE NOTHING. Not a weaker version of the same
   draw: two disjoint index groups into one ten-entry array. Whatever the Super Rod
   is for, the Old Rod is not a cheaper way of doing it.
```

## The coarse channel does not only narrow, it concentrates

Count the slots and then look at the top of each one. Twelve slots on land with the biggest at 20
per cent. Five slots on the water with the biggest at **60**. Two slots on the Old Rod with the
biggest at **70**. As the channel gets coarser, the commonest thing in what comes back gets
commoner, because there are fewer entries for the probability to be spread across.

That is two effects, not one, and they point the same way. The unusual becomes harder to reach —
on the Old Rod it is unreachable, there being no slot for it — and at the same time the common
becomes a larger share of everything the channel returns. A Trainer who has only ever used the Old
Rod on Route 102 will have met **Magikarp** seven times in ten and will have a confident and
entirely wrong picture of what is in that water.

## The engine has no mechanic for something noticed without being asked for

Here the cartridge has nothing, and saying so is more useful than inventing something.

Every wild encounter in Generation III is the result of a roll that some routine asked for. The
40 per cent chance of skipping the check on first stepping onto a new metatile type, the rate test
against 2 880, the slot roll, the level roll: each is a query with a return value. There is no
object anywhere in the engine that is *noticed*. Nothing is ever returned that nobody called for.
The nearest thing — the mass outbreak, which m081 used for urgency — is still a test, run in a
fixed place in `StandardWildEncounter`, and it has to be reached before it can fire.

So the single largest thing a remote channel removes has no counterpart here, and the analogy
cannot be stretched to cover it. The rods model exactly what a channel does to the *table*. They
model nothing at all about what is seen while you were looking at something else, because this
engine has no such category.

## Fishing runs no filters, and that is in the code rather than in the design

An ordinary step on land goes through, in order: the new-metatile roll, the rate test with its
nine levers and its cap, and then `TryGenerateWildMon` with both filter bits set,
`WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE`. Fishing goes through none of them.
`GenerateFishingWildMon` does not take a flags argument at all, so there is no Repel check and no
**Keen Eye** check in it, and
`FishingWildEncounter` runs no rate test and no metatile roll: cast, roll the slot, start the
battle.

Nobody decided that a Repel should not apply to fishing. The parameter was simply never threaded
through. This is the same shape as `SweetScentWildEncounter` passing **flags = 0**, which m048
used for the open question that bypasses every filter you had running — except that Sweet Scent
is a deliberate zero and fishing is an argument that was never added. The filters you rely on are
properties of one code path and not of the world, and the fast path is the one they were not
wired into.

## The rod is chosen before the water is known

This is the structural point and it is the whole reason the decision moves rather than disappears.

The slot vector is read *after* the rod is chosen. A Trainer standing at the water's edge picks
one of three instruments, and that pick decides whether **Corphish** is in the sample space at
all — and it is made before a single roll has happened, which is the moment of least information
in the entire exchange. Nothing about the water is visible beforehand. The Pokédex **Area**
screen will tell you a species occurs on a map; it will not tell you which rod reaches it.

And the pick is sticky in a way the rate levers are not. A Black Flute can be swapped for a White
Flute mid-route and the next step is already running the new multiplier. Choosing the wrong rod
costs the whole cast: the rounds, the window, the catch.

## What it costs to reach the five slots

The richer channel is not free, and the costs are in `Task_Fishing` rather than in the encounter
table:

| | required rounds | extra-round chance, 2nd and 3rd | window to press A |
| --- | --- | --- | --- |
| **Old Rod** | always exactly 1 | 0 and 0 | 36 frames |
| **Good Rod** | 1 + a roll under 3, so 1 to 3 | 40 and 10 per cent | 33 frames |
| **Super Rod** | 1 + a roll under 6, so 1 to 6 | 70 and 30 per cent | 30 frames |

Three things to read out of that. The instrument that reaches the five-slot table takes up to six
times as many rounds. Each round needs between one and ten dots before anything happens, and then
a bite on a one-in-two roll — raised to 85 in 100 if the lead holds **Suction Cups** or **Sticky
Hold**, which is the one place in this whole pipeline where a standing property of the party
improves the channel rather than the table. And the reaction window gets *shorter* as the rod gets
better: 36 frames on the Old Rod, 30 on the Super Rod. The channel that reaches more tolerates
less delay.

## Where the metaphor stops

One loss in a remote consultation belongs outside any structural account of channels. A clinician
on a telephone does not know who else is in the room. Somebody may not be able to speak freely
about their own health, their own home or their own safety, and the channel removes both the
privacy of a consulting room and the clinician's ability to notice that it has been removed. That
is not a limitation to be solved with a better question. It is a reason the channel is wrong for
some conversations, and local safeguarding and domestic abuse guidance is the authority wherever
there is any possibility of it.

The second thing. Remote channels are usually announced as an improvement in access, and for a
great many people they are exactly that: contact that was previously impossible because of work,
caring, transport, cost, pain or risk of infection. For others the same change is the point at
which care became unreachable — no data, no credit, no private space, a hearing impairment, a
first language that is not the system's, or no confidence that a voice on a telephone will be
believed. Being told access has improved while your own access has got worse is a particular kind
of harm, because it makes the problem look like yours. A system that offers channels should be
able to name which of its patients lost ground, and most cannot.

And the part the clinician carries. Working repeatedly at the edge of what a channel can support,
knowing that the thing you cannot see is the thing you would have noticed, is a sustained load. It
is a predictable consequence of the design and not a personal weakness, and naming it as a
property of the design is more useful than absorbing it quietly.

## What a Gym Leader is listening for

Whether the Trainer says *different table* rather than *worse odds*. Then the species read: that
**Marill** is unreachable by any rod and **Corphish** is absent from the Old Rod's table at any
percentage, with the disjoint index groups named. Then the concentration point — twelve slots
topping out at 20 against two topping out at 70 — offered as a second effect rather than the same
one. Then the absence, unprompted: that nothing in the engine is ever noticed without being asked
for, and that the rods therefore model only half of what a channel does. Then the filter
asymmetry, with the observation that nobody designed it. Then the structural claim: the rod is
chosen before the water is known. Then the costs, in rounds and in frames, with the direction of
the reaction window noticed.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The guidance on remote consulting and remote prescribing issued by the professional regulator
  and the relevant professional body where the reader works, which is the authority on what may
  be done remotely and differs substantially between systems (**country-dependent**).
* The reader's own organisation's access and triage policy, for who allocates channels, on what
  information, and what the conversion route is.
* The published literature on telephone and video triage, total triage and digital-first access,
  for measured effects on workload, safety, continuity and equity, where the direction of effect
  is not uniform across settings.
* The local safeguarding and domestic abuse guidance applying where the reader works, for the
  point in the plain-prose section above (**country-dependent**).

The Pokémon figures are a separate matter and are not covered by the line above. The
Generation III slot vectors — twelve land slots at 20 20 10 10 10 10 5 5 4 4 1 1, five water
slots at 60 30 5 4 1, and ten fishing slots at 70 30 / 60 20 20 / 40 40 15 4 1 grouped as
old_rod [0,1], good_rod [2,3,4] and super_rod [5,6,7,8,9] — together with the Route 102 land,
water and fishing tables and their table rates of 20, 4 and 30, the rate test multiplying by 16
against a maximum encounter rate of 2 880, the 40 per cent skip on first stepping onto a new
metatile type, `TryGenerateWildMon` receiving both the Repel and **Keen Eye** filter bits while
`GenerateFishingWildMon` takes no flags argument and `FishingWildEncounter` runs no rate test,
`SweetScentWildEncounter` passing flags of zero, the per-rod required rounds of exactly 1, 1 to 3
and 1 to 6, the extra-round chances of 0/0, 40/10 and 70/30, the reel windows of 36, 33 and 30
frames, the one-to-ten dot count, the one-in-two bite roll and its raise to 85 in 100 with
**Suction Cups** or **Sticky Hold** in the lead slot, were all read directly from the pret
decompilation projects, which this environment can reach. The tables quoted are Emerald's; other
third-generation titles differ.

## Scope and safety

This is revision material about the structure of a consultation channel, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here should inform whether any individual contact is handled remotely or in
person — that belongs with the clinician assessing them and with local policy. No criterion,
threshold or timescale for converting a remote contact to a face-to-face one is named here on
purpose: those are local, several are contested, and all are revised. What may lawfully and safely
be done remotely differs substantially by country and by profession, and the reader's own
regulator and organisation are the authority. The slot percentages, levels, frame counts and rolls
above are real and stand in for a mechanism; none of them is a clinical quantity and no clinical
figure should be read out of them. If someone is unwell right now, the relevant action is to
contact local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The structural claims — that a channel determines which findings are reachable, that incidental
observation is absent rather than degraded, and that remote-first access moves the sorting
decision to the point of least information — are mechanism and will not move. Almost everything
operational is moving. The channel mix changed abruptly in the early 2020s, has partially reverted
in several systems, and continues to be reorganised; the evidence on safety and on equity has
grown substantially and is still contested in direction; regulatory positions on remote
prescribing have tightened in some countries and not others; and automated history-taking and
triage tools are arriving faster than they are being evaluated. The Emerald tables are stable
because the games are finished. Take the operational detail from current local policy rather than
from here, as of October 2026.
