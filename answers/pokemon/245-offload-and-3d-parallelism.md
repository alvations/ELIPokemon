---
id: "245"
slug: offload-and-3d-parallelism
style: pokemon
category: open-weights
difficulty: advanced
question: "ZeRO-Offload moves optimizer state to CPU and ZeRO-Infinity to NVMe. When does that pay, and when is 3D parallelism the better answer?"
tags: [zero-offload, nvme, 3d-parallelism, pipeline, deepspeed]
---

# The Day Care buys you room you do not have. More Trainers buy you use of room you do.

The **Day Care** turns "there are only six slots and I need seven Pokémon raised" into "it will
be slow". That is a genuinely good trade when the alternative is not raising the seventh at all,
and a bad one the moment you had a friend standing right there who could have battled with it.

The decision is arithmetic, not taste: **compare the experience the Day Care can deliver per step
against the experience a battle delivers per turn.** If the walking was happening anyway, the Day
Care is free. If it is not, you are buying room with time, at a rate you should say out loud
before you hand the Pokémon over.

## The tiers, and what each one actually is

```
   ┌──────────────┬────────────────────┬─────────────────────────────────────────┐
   │ where        │ rough rate         │ what it can hold                        │
   ├──────────────┼────────────────────┼─────────────────────────────────────────┤
   │ the party    │ thousands of EXP   │ six Pokémon, all of them able to fight  │
   │              │   in four turns    │   this turn                             │
   │ the Day Care │ ONE EXP per step   │ two Pokémon. They level. They cannot    │
   │              │                    │   battle, and you must walk back        │
   │ Pokémon HOME │ no EXP at all      │ as many as you like — and not one of    │
   │              │                    │   them can do anything until it is      │
   │              │                    │   moved back into the game first        │
   └──────────────┴────────────────────┴─────────────────────────────────────────┘

   Read the second row carefully. The Day Care is not merely somewhere to put a
   Pokémon: it does the levelling FOR you while you are elsewhere. That is the
   whole reason to use it, and the whole reason it is slow.
```

## The arithmetic you should do before you hand anything over

Take a Pokémon on the Medium Fast curve, where reaching level *n* costs *n*³ experience, and say
you want it from **level 50 to level 60**:

```
   WHAT THE DAY CARE MUST DELIVER
     60³ = 216,000        50³ = 125,000
     difference                           =  91,000 experience
     at one experience point per step     =  91,000 STEPS of walking

   WHAT IT COSTS TO COLLECT
     ₽100 to take it back, plus ₽100 per level it gained
     ₽100 + 10 × ₽100                     =   ₽1,100

   WHAT THE SAME TEN LEVELS COST IN THE PARTY
     a handful of real battles, four turns each, with a Lucky Egg on

   VERDICT
     you were going to walk 90,000 steps anyway  →  free. Take the deal.
     you were sitting still                      →  ruinous. Do not.
```

The lever that makes the Day Care work is therefore **a long journey**: a region to cross, a
**Victory Road** to climb, a **Safari Zone** to walk out. The Day Care and a long walk are the
same trick pointed at different resources, and they compose. An **Exp. Share** in the party and a
Pokémon in the Day Care are not rivals; they are two ways of getting value out of steps you were
taking regardless.

**Pokémon HOME** moves the numbers an order of magnitude the wrong way. Nothing stored there
gains a single point, and nothing stored there can be sent out; it has to come back into the game
first. It is for the case where the honest alternative is "I cannot keep this Pokémon at all".

**One trap, and it is the good kind of trap to know about.** A Pokémon in the Day Care **does not
evolve**, however many levels it gains. Leave something whose evolution was due at 36, collect it
at 60, and it comes back exactly as you left it — the right level, the wrong Pokémon, and nothing
in your notes to explain it. That is a default you never set, biting you at the moment of
collection.

## When more Trainers is the right answer instead

Three ways to split the *work* rather than the storage, and they are independent of each other:

```
   ┌ more Trainers ───┐  Eight of them on different routes with the same team.
   │                  │  They compare notes once, at the end of the day.
   ├ more rooms ──────┤  The Indigo Plateau: Lorelei, then Bruno, then Agatha,
   │                  │  then Lance, in that order, and you cannot back out.
   │                  │  Only the challenger crosses a doorway — the CHEAPEST
   │                  │  split there is. The cost is the waiting:
   │                  │     1 challenger,  4 rooms  →  Lorelei idle 75% of it
   │                  │    12 challengers, 4 rooms  →  Lorelei idle 20% of it
   ├ one battle, two ─┤  A Multi Battle: two Trainers running one side of a
   │ Trainers         │  single fight, agreeing on every single turn.
   └──────────────────┘  The most talking of the three. Same room, or don't.
```

The rule of thumb that survives contact: **share a battle only with someone in the room, split
the rooms across the building, put more Trainers on top of that, and use the Day Care to mop up
whatever is left over.** And the choice against the Day Care is simply: do you have the Trainers?
More Trainers turn idle friends into progress. The Day Care turns a shortage of friends into
time. Eight people standing around and a seventh Pokémon to raise is not a Day Care problem. One
person, one Pokémon and a deadline is.

## What a Gym Leader digs into next

* Your training day got 40% longer after you started using the Day Care. Was it the walking or
  the walk back?
* Why does queueing more challengers shrink Lorelei's idle time, while adding a fifth room does
  not?
* What breaks when the two halves of a Multi Battle are not in the same room?
* Two Pokémon in the Day Care together: which of them is actually gaining what, and what else
  might you come back to?
* A **Rare Candy** delivers a level instantly and an **Amulet Coin** pays for a lot of them. Which
  line of the first table does that change, and by how much?

## Where this stands, September 2026

The Day Care rules quoted here are from the published guides and have been stable for
generations: one experience point per step, ₽100 to collect plus ₽100 per level gained, two
Pokémon at a time, and no evolution while deposited. The Medium Fast curve really does cost *n*³
to reach level *n*, so 50 to 60 really is 91,000. The comparison rates — thousands of experience
in four turns — are a sketch rather than a measurement, and they move with every generation's
experience formula. The rule does not: count what the slow path must carry, count what the fast
path was going to do anyway, and only take the deal when the second number covers the first.
