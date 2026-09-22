---
id: "244"
slug: zero-stages-and-memory-arithmetic
style: pokemon
category: open-weights
difficulty: advanced
question: "Walk me through DeepSpeed's ZeRO stages 1, 2 and 3 with real memory arithmetic. What does each one shard?"
tags: [zero, deepspeed, distributed-training, memory, data-parallelism]
---

# Each stage deletes one kind of duplicate. The last one also takes away your summary screen.

Eight Trainers in a **VGC** practice group decide to run the same six: **Garchomp**,
**Incineroar**, **Amoonguss**, **Rillaboom**, **Gholdengo** and **Chien-Pao**. The obvious way is
the wasteful way — all eight of them breed all six, **Effort Value** train all six, and keep all
six in their own boxes, so that eight identical ledgers exist for a team that only ever plays one
match at a time.

The fix comes in three steps, and each one deletes exactly one kind of duplicate. Step one: only
one Trainer keeps each Pokémon's long-term ledger. Step two: only one Trainer keeps the points it
earned in the last battle. Step three: only one Trainer keeps the Pokémon at all, and the others
trade it in when they need it.

## The arithmetic, on a team you can picture

Everything a fully prepared Pokémon carries sorts into three piles:

```
   2 numbers   the four moves and the one held item it fights with   ┐ on the field
                                                                      ┘ every turn
   2 numbers   the Effort Values it earned in the last battle,       ┐ produced once,
               not yet showing on the summary screen                  ┘ banked once
  12 numbers   the permanent ledger: six EV totals and six           ┐ never touched
               Individual Values                                       ┘ mid-battle
  ──
  16 numbers   per Pokémon
```

```
   6 Pokémon, 8 Trainers.                   entries each Trainer must keep

   everyone keeps everything                = 96.0   ████████████████   unworkable
   step 1: share the 12-number ledger       = 33.0   █████▌             workable
   step 2: share the last battle's EVs too  = 22.5   ███▊
   step 3: share the Pokémon themselves     = 12.0   ██
             │       │        │
             │       │        └ the ledger: shared from step 1 on
             │       └ the earned EVs: shared from step 2 on
             └ the Pokémon: still copied eight times until step 3

   step 1:  4×6 = 24.0  +  12×6/8 =  9.0   →  33.0
   step 2:  2×6 = 12.0  +  14×6/8 = 10.5   →  22.5
   step 3:                 16×6/8 = 12.0   →  12.0
```

Read the middle column, not the total. Step one alone takes 96 entries to 33 — the difference
between a group that cannot start and one that can. Step two saves another ten and a half. Step
three saves the same again *and* keeps saving as the group grows, which the first two do not: put
sixty-four Trainers in the group and step two is stuck above the twelve entries of duplicated
Pokémon while step three falls to one and a half.

## Do not trust that table; count your own notebook

Twelve numbers for the ledger is the tidy version. Anybody who has actually kept the notes knows
there are more columns than that: the Nature, the Ability, whether **Pokérus** has been through
it, whether a **Bottle Cap** has already been spent on it, which parent the **Destiny Knot**
passed each value down from. Call it eighteen rather than fourteen and step two comes out at
`12 + 18×6/8 = 25.5` entries, not 22.5.

Nobody is going to hold you to eighteen against fourteen. Knowing that the tidy table
under-counts, and that the honest number is in your own notebook rather than in the table, is
the point.

## What none of this covers: PP

Sharing ledgers does nothing whatsoever about what the **match itself** burns. Four moves at
their own PP, a **Focus Sash** spent the moment it saves you, a **Choice Scarf** locking Garchomp
into whatever it picked first, **Leftovers** ticking a sixteenth of Incineroar's HP back each
turn:

```
   6 Pokémon × 4 moves × their own PP, spent turn by turn, plus every
   consumable item on the team — none of it appears in the 16 numbers above.

   The fixes are separate tools: a Leppa Berry restores PP mid-battle,
   an Ether or a Max Elixir restores it after, and PP Up raises the
   ceiling before you ever set out.
```

A Trainer who quotes twelve entries and then cannot say why the team still ran dry in round four
has memorised the table and not the game.

## What each step costs

**Trading.** Steps one and two move the same amount of paperwork around, just differently. **Step
three moves Pokémon**: the holder trades Garchomp over before the match and takes it back after,
so the traffic through **Pokémon HOME** and the **Global Trade Station** runs about half as much
again as it did. That is the real price of step three.

**You lose the summary screen.** Under step three a Pokémon you are not battling with is *not in
your boxes*. You cannot open its summary, you cannot read its Individual Values, you cannot hand
it a **Bottle Cap**, and you cannot put it in with a **Destiny Knot**. Every one of those needs
you to ask the holder to trade it across first, and trade it back when you are done. Every habit
you had of just going and looking at your own Pokémon meets this rule.

**And you need room for the biggest single thing.** A Pokémon arrives whole or not at all. You
cannot borrow Garchomp's Attack without borrowing Garchomp, so whatever else you have shared
away, you must keep enough free space for one entire Pokémon to land in.

**Rounding is a bigger lever than any of the steps.** Four Effort Values buy one stat point
anyway, so recording the ledger to the nearest four halves the notebook. It also costs you the
last point whenever two halves round the same way — which is a convergence problem, not a free
win, and the reason the careful breeders do not do it.

## Choosing

Step two if the six Pokémon themselves fit in everybody's boxes and you want the cheapest thing
that works. Step three when they do not, when the group keeps growing, or when you need the room
for something longer. Do not open at step three out of ambition: you are paying half again in
trades and giving up the summary screen for space you may not need.

## What a Gym Leader digs into next

* Why does step two stop improving once the group is large, however many Trainers you add?
* Where does the ledger actually live when the holder has left the Pokémon at the **Day Care**?
* You moved to step three and the group now plays half as many practice matches. What do you time
  first?
* Why does banking EVs every fourth battle instead of every battle change the trading and not the
  entries?
* Which of these savings survive if the team stops **Hyper Training** altogether?

## Where this stands, September 2026

Four EVs to a stat point, 510 across the team's six stats with 252 the ceiling in any one,
Individual Values running 0 to 31, the Destiny Knot passing values down, Pokérus doubling the
haul — all of these come from rulebooks that have not moved in years and are safe to quote. The
sixteen-numbers-per-Pokémon split is my own bookkeeping, not a printed rule, and the match
figures are a sketch rather than a measurement. What the ledger contains changes with every
generation. Dividing it by the number of people keeping it does not.
