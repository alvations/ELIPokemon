---
id: "223"
slug: trillion-parameter-moe-sparsity
style: pokemon
category: open-weights
difficulty: advanced
question: "A lab ships a 1T-parameter MoE activating 32B, then a 2.8T one activating 104B. What is sparsity a knob for?"
tags: [mixture-of-experts, sparsity, scaling-laws, attention, open-weights]
---

# The chart went from fifteen types to eighteen. A turn still spends one.

Question 207 makes the first cut: whoever is out decides the turn's cost, the whole team decides
the weight. True, and not the interesting part. The interesting part is that **how many types
exist on the Type Chart, against how many a turn actually spends, is a number somebody chose** —
and it has gone up twice.

Kanto shipped with fifteen types. Johto added **Dark** and **Steel**, making seventeen. **Kalos**
added **Fairy**, making eighteen. Through all of it, a turn still spends one move and the chart
still looks up one type against the defender. The pool grew. The spend did not.

## The law the chart is obeying

Hold the spend fixed at one move a turn and widen the pool, and every matchup gets answered more
precisely. This is not a feeling; it is the whole reason the chart was widened.

**Fairy** is the clean case. Before **Kalos**, a **Dragonite** at the **Pokémon League** was
answered with **Ice Beam** — 90 **Base Power**, 100% accurate, and four times effective because
**Dragonite** is part Flying. But **Clair**'s **Kingdra** is part Water, so **Ice Beam** lands on
it for exactly neutral damage: the Water half halves it, the Dragon half doubles it, and the chart
hands you nothing. That gap is what **Fairy** filled. **Moonblast** at 95 **Base Power** and 100%
accuracy answers both, and Dragon moves do nothing at all back.

```
   one move a turn.  widen only the pool it is drawn from.

   chart size  =  types available / types a turn spends

    15   ████████████████████████████████████   gaps ▲   Kanto
    17   ██████████████████████████████         gaps │   Johto: Dark, Steel
    18   ██████████████████████                 gaps ▼   Kalos: Fairy

                                 ▲                         ▲
                                 │                         │
                 the gaps keep closing as you       WHERE IT STOPS is a
                 add types                          carrying decision,
                                                     not a battling one
```

Widening is buying better matchups with **memory**, not with effort. Fifteen types meant 225 cells
to hold. Eighteen means 324. **Valerie** does not get more turns than **Lance** did. She gets a
better answer available on the turn she has.

## Finer, not just more

The three new types were narrow on purpose. **Steel** resists an enormous amount but has one job;
**Dark** exists to answer Psychic; **Fairy** exists to answer Dragon. That is what a fine-grained
pool means — more entries, each smaller, so the lookup lands closer. The old types were not split
up either: **Steelix** and **Scizor** and **Magneton** were *re-typed into* the new slots when
they opened, and **Gardevoir** picked up **Fairy** alongside Psychic the moment it existed.

One type stays out of the accounting. **Normal** is the move you can always throw: only Rock and
Steel resist it and only **Gengar** and friends ignore it outright. **Body Slam** is what you
reach for when the chart has nothing sharper. It is always there, so it is not part of the ratio.

## The other half of the ledger

The part most Trainers miss: **reading** the opponent costs turns too. Check the **Pokédex** entry
for every Pokémon on the other side, every turn, and you are paying for the lookup as well as the
move. Doubling how much you read buys you maybe a percent in how well you choose — and at turn 128
of a **Battle Tower** streak it costs you most of the time you have. **Kingdra** is one entry.
Reading it twice is not twice as useful.

## What changes when the chart stops fitting

```
   Kanto chart     15 x 15  =  225 cells      one head holds it
   Kalos chart     18 x 18  =  324 cells      one head, barely

   modern roster   the whole thing            TWO bags, not one

   ┌──────── bag 0 ────────┐        ┌──────── bag 1 ────────┐
   │  half the answers     │◄──────►│  half the answers     │
   └───────────────────────┘  walk  └───────────────────────┘
                              ▲
                              └ every turn that needs the OTHER bag is a
                                trip on foot, not a reach into the one
                                you are holding. That is the line.
```

Going from one bag to two is the whole discontinuity. Inside one bag, switching to the right
answer is free. Across two, it is a walk, and if every opponent for six turns wants the same
answer out of the far bag, you are making that walk six times while everything else waits. That is
why the hardest work is not owning the answers but spreading them so no single one is the
bottleneck.

## What a Gym Leader is listening for

That you treat the size of the chart as a decision somebody made against evidence, not a fact of
nature; that you mention the cost of *reading* in the same breath as the cost of *acting*; and
that you know the bag boundary is the cliff, not the number of entries. The strongest answers add
that "how many types exist" and "how many a turn spends" are two different counts, and say which
one is being quoted.

## Where this stands, September 2026

The chart numbers are from the games and do not rot. The rest — which roster is current, how many
bags it takes to carry — comes from what each release published about itself, and it moves every
few months. The reasoning holds: same spend per turn, wider pool, better matchups, heavier bag.
Re-check the roster the release published, not what somebody said about it.
