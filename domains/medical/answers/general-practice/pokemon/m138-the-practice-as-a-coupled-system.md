---
id: "m138"
slug: the-practice-as-a-coupled-system
style: pokemon
category: general-practice
difficulty: advanced
question: "Why are list size, appointment length and continuity one set of coupled constraints rather than three separate decisions, and what happens to the slack?"
tags: [capacity, list-size, consultation-length, continuity, workload]
---

# Thirty balls and five hundred steps, and nothing in the cartridge converts one into the other

The **Safari Zone** is the one place in Hoenn where the engine puts hard budgets on an excursion
and then declines to make them fungible. m049 used the Kanto version of it for the shared-counter
argument — thirty balls against the expected encounters of a whole walk, where no individual throw
can be named as the wasteful one. This answer uses the **Emerald** version for a different
property of the same room: there are *two* budgets, they run down on two unrelated events, the
session ends on whichever empties first, and the two endings are indistinguishable.

A note on register before anything else. The counters below are being read as a **budget**,
exactly as m049 read them, and for nothing else. Nothing in this pair treats catching as an act
done to a patient; the conventions file rules that mapping out and it stays out. An encounter here
is a piece of work arriving, which is how m011 and m081 have used the grass throughout.

## Two budgets, set in one function, spent on two different events

```
   READ OUT OF src/safari_zone.c AND data/scripts/safari_zone.inc.

   EnterSafariMode()
       gNumSafariBalls        = 30
       sSafariZoneStepCounter = 500
       sSafariZoneCaughtMons  = 0
       sSafariZonePkblkUses   = 0
       and SetSafariZoneFlag(), which is what makes any of the rest run

   SPENT BY TWO UNRELATED EVENTS

     steps  SafariZoneTakeStep(), called on every step while the flag is set:
              DecrementFeederStepCounters();        <- note the ORDER
              sSafariZoneStepCounter--;
              if (counter == 0) -> SafariZone_EventScript_TimesUp

     balls  spent in battle; when the last one goes, gBattleOutcome becomes
            B_OUTCOME_NO_SAFARI_BALLS and CB2_EndSafariBattle takes the
            gNumSafariBalls == 0 branch -> SafariZone_EventScript_OutOfBalls

   AND THE TWO ENDINGS ARE THE SAME ENDING

     TimesUp  : lockall, SE_DING_DONG, message, waitbuttonpress, releaseall,
                goto SafariZone_EventScript_Exit
     OutOfBalls: lockall, SE_DING_DONG, message, waitbuttonpress, releaseall,
                goto SafariZone_EventScript_Exit

     Exit     : setvar VAR_SAFARI_ZONE_STATE, 1
                special ExitSafariMode
                warp MAP_ROUTE121_SAFARI_ZONE_ENTRANCE, 2, 5

   Same chime, same structure, same warp, same tile. Two completely different
   binding constraints and one door, and after ExitSafariMode has run both
   counters read zero, so afterwards you cannot tell from the state which one
   bound. NOTHING anywhere converts a ball into a step or a step into a ball.
```

Which budget binds is not a property of the room. It is a property of how the excursion is
conducted: walk a long way and throw rarely and the step counter binds; throw at everything and
the balls bind well before the clock does, which is the arithmetic m049 did in Kanto. The room is
identical in both cases.

And the generation has to be stated or the number should not be. m049's counter is **502**, which
is Kanto's, written into `wSafariSteps` *before* a three-press auto-walk at the gate. Emerald's is
**500**, and `special EnterSafariMode` runs *after* `applywaitmovement` has finished the
seven-command entry movement — six `walk_left` and a `walk_down` — so in Emerald the walk in is
free, because the flag that makes `SafariZoneTakeStep` do anything is not set until the walking
has stopped. Two cartridges, two numbers, and two different orderings of the same two
instructions.

## Three classes of lever, and every one of them is paid for in steps

```
   WHAT A TRAINER CAN ACTUALLY CHANGE, and which term it touches

   the RATE - how often work arrives
      m082's nine levers: x16, Mach Bike or Acro Bike x80/100, White Flute and
      Black Flute +/-50 per cent, Cleanse Tag x2/3, lead Stench /2 (x3/4 in the
      Battle Pyramid), Illuminate x2, White Smoke /2, Arena Trap x2, Sand Veil /2
      in a sandstorm, capped at 2 880. Not one of them touches a slot.
      The Safari Zone's land areas carry an encounterRate of 25.

   the TABLE - what the work can be
      per AREA, not per zone. Safari Zone South's twelve land slots, with the
      Generation III shares of 20/20/10/10/10/10/5/5/4/4/1/1 per cent:

         Oddish     slots 1, 2 ................ 40 per cent
         Girafarig  slots 3, 4 ................ 20
         Natu       slot 5 .................... 10
         Doduo      slot 6 .................... 10
         Wobbuffet  slots 8, 10, 12 ........... 10   (5 + 4 + 1)
         Gloom      slot 7 ..................... 5
         Pikachu    slots 9, 11 ................ 5   (4 + 1)

      walk north instead and the table is Phanpy, Oddish, Natu, Gloom, Xatu and
      Heracross - and Heracross is slots 10 and 12, which is 5 per cent. Same
      zone, same entry fee, same two budgets, different work.

   the ATTRIBUTE - what the work is like when it arrives
      a Pokéblock on a feeder, and that is the whole of it.

   ─────────────────────────────────────────────────────────────────────────────
   ALL THREE ARE PAID FOR IN STEPS. Changing area is steps. Walking to a feeder
   is steps. Riding to raise the rate costs 20 per cent of the rate itself.
   There is ONE resource and three things to spend it on.
```

## The feeder is a standing investment that depreciates on the working clock

`SafariZoneActivatePokeblockFeeder` writes into one of ten slots in `sPokeblockFeeders`, storing
the map, the coordinates, the Pokéblock itself and `stepCounter = 100`. Then:

* `DecrementFeederStepCounters()` runs on **every** Safari step, before the session counter is
  touched, and decrements every active feeder — whether you are standing next to it or on the far
  side of the zone. At zero the slot is `memset` to nothing.
* `GetPokeblockFeederWithinRange` accepts a feeder whose Manhattan distance from the player is **5
  or less**. Outside that, an active feeder does nothing at all.
* And what it buys, in `PickWildMonNature`: with the Safari flag set and on `Random() % 100 < 80`,
  if a feeder is in range, the twenty-five natures are shuffled and the first one for which
  `PokeblockGetGain` is positive is returned.

So the investment does not change the rate, does not change the table, and does not change how
many balls or steps are left. It changes the **nature** of what appears — a per-individual
attribute that no screen in the game displays, which is m020's device from dermatology pointed at
a different question. It costs a Pokéblock, one of ten slots, the steps to walk there, and the
steps to stay within five tiles of it; and its hundred-step life is spent by the same event that
spends the session.

That is the shape worth carrying: a standing arrangement whose useful life is consumed by the
ordinary work, which must be visited to be used, and whose entire return is in a quality of the
encounter rather than in the count of encounters.

## The lead changes an attribute of everything you meet, and nothing records it

m015 established badge-gated obedience as this specialty's continuity device: a Pokémon somebody
else raised does not obey, and the rule is in the code. The encounter generator contains a quieter
version of the same idea, and it is about slot zero.

* **Synchronize.** In `PickWildMonNature`, if no feeder applies and `gPlayerParty[0]` has
  **Synchronize**, then on `Random() % 2 == 0` the wild Pokémon is given the lead's own nature,
  computed as `personality % NUM_NATURES`.
* **Cute Charm.** In `CreateWildMon`, for any species with a mixed gender ratio, if
  `gPlayerParty[0]` has **Cute Charm** then on `Random() % 3 != 0` — two thirds of the time — the
  wild Pokémon is generated with the gender opposite the lead's.

Neither changes the rate. Neither changes the table. Neither changes a counter. Who is in slot
zero changes a property of the thing that arrives, two thirds of the time in one case and half of
it in the other, and the only place that property can be observed is afterwards, in the
individual, by someone who knows what to look at.

## What is recorded at the end, which is two numbers

```
   ExitSafariMode()
       TryPutSafariFanClubOnAir(sSafariZoneCaughtMons, sSafariZonePkblkUses);
       ResetSafariZoneFlag();
       ClearAllPokeblockFeeders();
       gNumSafariBalls = 0;
       sSafariZoneStepCounter = 0;

   TWO COUNTS SURVIVE THE EXCURSION, AND THEY ARE BROADCAST.

     mons caught .......... counted in CB2_EndSafariBattle on B_OUTCOME_CAUGHT
     Pokeblocks used ...... += gBattleResults.pokeblockThrows

   NOT RECORDED, ANYWHERE
     how many steps were taken, or how many were left
     how many encounters happened at all
     what was met and let go
     whether the balls or the clock ended it
     which feeder was placed, where, or whether anything ever came near it
```

Two activity counts, and both of them count an *act* rather than a resolution: a throw that
succeeded, and a Pokéblock that was spent. The one quantity a Trainer actually manages — where the
five hundred steps went — is zeroed on the way out and reported to nobody.

## Where the metaphor stops

The person who needs the most time is usually the person least able to ask for it. That is the
equity argument about appointment length and it is not solved by anybody working harder; it is a
property of how time is allocated and of who finds it easy to operate an allocation system.

The second thing is that the unmeasured term in a service's arithmetic is somebody's evening. When
the residual lands in work done outside booked sessions it lands on named people, in hours nobody
counts, and it gets drawn on first precisely because drawing on it never registers as a failure.
Nursing m074 argues that fatigue is a safety factor rather than a personal failing, and that
applies here in full: a system balancing itself on unmeasured goodwill has somebody's tiredness as
its safety margin.

And the honest statement about continuity. It is a clinical good with evidence behind it, and it
is also, concretely, a constraint that removes options from a timetable. Pretending it is free is
what makes it the first thing cut when access is under pressure, because the case for it never
gets made as a resource case. Both halves are true, they pull against each other, and a practice
that says out loud which it is choosing, and for whom, is doing something better than one implying
it has chosen neither.

## What a Gym Leader is listening for

Whether the Trainer names both budgets and then says what no mechanic provides — any conversion
between them. Then the two exit scripts, identified as structurally identical down to the warp
tile, with the consequence that the binding constraint is not recoverable afterwards. Then the
generation: 500 in Emerald written after the entry movement, 502 in Kanto written before a
three-press auto-walk, and the rule that the generation is stated or the number is not. Then the
three classes of lever — rate, table, attribute — with the point that all three are paid for in
the same steps. Then the feeder: ten slots, a hundred steps each, decremented before the session
counter on every step, Manhattan range five, and a return consisting entirely of a nature nobody
can see. Then **Synchronize** and **Cute Charm** as slot zero changing an attribute of every
arrival, with the fractions right. Then what `ExitSafariMode` preserves — two counts of acts — and
the long list of what it does not. Then the hard one: which single thing a Trainer would have to
log to tell, at the end of a walk, which budget had been binding all along.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The contract or regulation that governs registration, list closure, access requirements and
  funding in the reader's own system, which determines which of these terms a practice may
  actually change (**country-dependent**).
* The reader's own organisation's workforce and activity data, including whatever it records about
  work done outside booked sessions.
* The published literature on consultation length and on continuity of care, read for associations
  and for the limits of the causal claims, both of which are argued about.
* A current textbook of health services research or operations management in healthcare, for
  queueing behaviour and for why utilisation close to capacity produces disproportionate waiting.

The Pokémon facts are a separate matter and are not covered by the line above. `EnterSafariMode`
setting thirty balls and a five-hundred step counter; `SafariZoneTakeStep` decrementing the
feeders before the session counter and running `SafariZone_EventScript_TimesUp` at zero;
`CB2_EndSafariBattle` and `B_OUTCOME_NO_SAFARI_BALLS`; the two exit scripts and their shared
`goto` and warp destination; `ExitSafariMode` calling `TryPutSafariFanClubOnAir` with the catch
and Pokéblock counts and zeroing both budgets; the ten-entry `sPokeblockFeeders` array with its
hundred-step counters, `DecrementFeederStepCounters`, the `memset` on expiry and the Manhattan
range of five in `GetPokeblockFeederWithinRange`; `PickWildMonNature`'s 80-per-cent feeder branch,
its nature shuffle and `PokeblockGetGain` test, and its **Synchronize** branch on `Random() % 2 ==
0`; `CreateWildMon`'s **Cute Charm** branch on `Random() % 3 != 0`; the Safari Zone land encounter
rate of 25 and the twelve-slot tables for the South and the North areas as
`src/data/wild_encounters.json` lists them; the nine rate levers and the 2 880 cap; and Kanto's
`wSafariSteps` value of 502 written before `SafariZoneEntranceAutoWalk` with a count of three,
were read directly from the pret decompilation projects, which this environment can reach. The
Generation III slot shares of 20/20/10/10/10/10/5/5/4/4/1/1 per cent are the ones this domain's
conventions file records; the species-to-slot assignments above were recomputed from the JSON
rather than recalled, because a per-route share is the one figure in this corpus that has been got
wrong twice by memory.

## Scope and safety

This is revision material about how the capacity of a general practice behaves as a system,
written for someone already training in or qualified for the field. It is not a clinical
reference, not a decision aid, and nothing here should inform a decision about any individual's
care, appointment or referral. No list size, consultation length, staffing ratio, waiting-time
target or workload threshold is named here on purpose: all are local, several are contractual and
all are revised. Nothing here is a statement about how any particular practice should be
organised, and nothing in it measures anybody's performance. The ball counts, step counters, slot
shares and multipliers above are real and stand in for a mechanism; none of them is a clinical
quantity and no clinical figure should be read out of them. If someone is unwell right now, the
relevant action is to contact local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The identity behind this pair is arithmetic and will not move, and so will the consequences: that
the residual lands in whatever is unmeasured, and that uniform appointment length is a design
choice with an equity cost. What moves is everything numerical and contractual — list sizes,
standard appointment lengths, staffing models, the scope of other professional roles, access
requirements, and the balance between booked and same-day work. Multidisciplinary teams and
asynchronous contact have changed where the residual lands rather than removing it. The Emerald
and Kanto code is stable because the games are finished. Take anything operational from current
local requirements rather than from here, as of October 2026.
