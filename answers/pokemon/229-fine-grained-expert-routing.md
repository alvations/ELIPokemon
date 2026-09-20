---
id: "229"
slug: fine-grained-expert-routing
style: pokemon
category: open-weights
difficulty: advanced
question: "How does fine-grained MoE routing actually work, and what does router collapse look like while it is happening?"
tags: [mixture-of-experts, routing, load-balancing, deepseek, training]
---

# Check the chart, send out eight. Stealth Rock is already up.

Question [011](011-mixture-of-experts.md) covers keeping more than you can send out, and
[207](207-sparse-moe-serving.md) covers what carrying them costs. This is the *choosing*: how
narrowly each one is built, what is already on the field before anybody is chosen, how you stop
yourself leading with **Garchomp** every single time, and how you spot that you have — while it
is happening, not at the **Indigo Plateau**.

## The choice, in numbers

```
   a box of 256 built specialists + 1 that is always up
   pick 8 · score them on the chart · 8 boxes, a turn may reach into at most 4

   opponent  ──► read the chart  ──► 256 scores
                                          │
                        + your own note on each   (affects who you pick,
                                          │        not how hard they hit)
                                      top 8 ──► weight them by the *unnoted*
                                                scores of those eight
                                          │
        ┌─────────────────────────────────┴────────────────────────┐
        ▼                                                          ▼
   Stealth Rock (always up)                   8 of 256 pulled from the box
   44,040,192 steps to set up                 8 × 44,040,192 steps to raise
                                                          │
                     the turn = the hazard + the weighted eight
```

That is a fair fight on effort, and it is the point. **9 × 2048 = 18432.** Nine narrow builds
cost exactly what one all-rounder costs: `9 × 44,040,192 = 396,361,728`. Nothing got cheaper.
What changed is that the 18,432 came off a shelf of 256 × 2,048 instead of out of one fixed
block.

And it reconciles against the whole collection:

```
   one narrow build                            =     44,040,192
   257 of them across 58 rounds                =        656.5 B
   + the three plain rounds, the stands, names =        670.9 B   (registered: 671 B)

   the 9 that actually move, across 58 rounds  =         23.0 B
   + the plain rounds, the stands, names       =         36.5 B   (on the field: 37 B)
```

If your count of the box does not land on the number on the registration sheet, you have
miscounted the box. This one lands, to within rounding.

## Why a wide box of narrow builds beats six all-rounders

At the same effort, cutting each build narrower and sending more of them buys **combinations**:

```
   8 all-rounders, send 2      C(8,2)     =                    28 answers
   one box of 30, send 6       C(30,6)    =               593,775
   64 specialists, send 8      C(64,8)    =         4,426,165,368
   256 specialists, send 8     C(256,8)   =   409,663,695,276,000
```

It is the same logic as **EVs**. You have 510 to spend and 252 is the most any one stat may take.
Spread them evenly and every stat gains 21 points at level 100 — four EVs to a point, 85 EVs, 21
points, six times over. Dump them instead, ten at a time out of a bag of **Protein**, **Carbos**
and **HP Up**, and two stats gain 63 points each while the rest gain nothing. Same 510. A box of
narrow builds is the second choice made 256 times over, and the answer to a given opponent is
assembled out of eight of them rather than found in one.

The cost is real. **Shedinja** has 1 HP and **Wonder Guard**, so no move that is not
super-effective damages it at all: it is either the entire answer or completely useless, an awkward
thing to keep 248 of. **Ferrothorn** walls half the chart and folds to one **Flamethrower**.
Narrow builds are fiddly to move in and out of the box, and reaching into four boxes at once is
four trips.

**Stealth Rock** is the other half of the idea. If every build is narrow, all 256 of them end up
separately learning that the opponent has to come in somehow. So you put the hazard up once —
**Tyranitar** sets it, or **Garchomp**, or **Ferrothorn** — and let it apply to everybody: 1/8 of
a switch-in's health at neutral, and a full half of **Charizard** the moment it lands. **Spikes**,
**Toxic Spikes** and **Sticky Web** do the same job for whatever walks in on the ground, and
**Toxapex** absorbs the Toxic Spikes simply by being a grounded Poison-type. That layer is 1/9th
of the effort on the turn, it applies before anyone is chosen, and it is doing work the other
eight no longer have to duplicate. Which is also why **Rapid Spin** and **Defog** are the first
thing the opponent reaches for.

## Spreading the work, and the rule that is no longer there

Leading is a positive-feedback trap. The one you lead with gets the experience, gets stronger,
and earns leading again. Left alone that ends with **Cynthia**'s **Garchomp** answering
everything, 247 of the box still sitting at level 5, and — in a Multi Battle — your partner
standing there waiting for you every single turn.

The bolted-on fix is a **clause**. **VGC** under **Regulation G** runs a Species Clause that
forbids two of the same species and an Item Clause that forbids two of the same held item, and
they work: they force the spread. They are also a second rulebook arguing with the first one.
Every time the clause overrules the matchup you wanted — no second **Choice Scarf**, no second
**Incineroar** — you have taken a worse turn on purpose, and past some point that costs more
than the imbalance did.

The better fix, and the one the strongest teams now use, does not touch the Pokémon at all:

* keep a private note beside each name in the box, and let it shift **who you reach for**;
* work out how hard they hit from the chart alone, with the note ignored, so nothing you did to
  spread the work weakens the Pokémon;
* after each battle, nudge the note up for whoever has not been out and down for whoever has.

Nobody gets worse EVs to make the rota fair. The rota lives in your hand, not in the Pokémon. You
measure it by the worst case — how far the most-used one sits above the average — not by the
average, because the average was always fine.

There is one more rule and it is purely about walking: the 256 sit in 8 boxes and a turn may reach
into at most 4. That caps the running, not the quality.

## What it looks like while it is going wrong

The trap is that **the streak counter looks fine**. Here is what to actually watch:

```
   how often each of the 256 has been out, box 30

   healthy                            collapsing
   ┌──────────────────────────┐       ┌──────────────────────────┐
   │▁▂▂▁▂▁▂▂▁▂▂▁▂▁▂▂▁▂▁▂▂▁▂▁▂ │       │█▁▁▁▆▁▁▁▁▁▁▇▁▁▁▁▁▁▁▁▁█▁▁▁ │
   └──────────────────────────┘       └──────────────────────────┘
    worst ≈ 1.1× the average           worst ≈ 7× the average, climbing

   turn length  ──► usual turns fine, the slow ones getting slower
   left behind  ──► rising: **Heatran** still level 5 when the Ground move lands
   how evenly you are choosing:
        one name, always        you have stopped answering the opponent
        every name, equally     you have stopped reading the chart at all
   streak       ──► unremarkable for hundreds of battles
```

Both ends are broken, which is why "the rota is perfectly even now" is not good news on its own.
A Trainer who sends out whoever is next in the box has a beautifully even rota and has stopped
being a Trainer.

## Where this stands, September 2026

The boxes keep getting bigger and the builds keep getting narrower. DeepSeek-V3 registers 671 and
fields 37; Mistral Large 3 is reported at 675 and 41; GLM-5.3 at about 744 and 40; Llama 4
Maverick at 400 and 17 across 128 specialists plus one always up; Kimi K3 is reported to send 16
out of 896. I read DeepSeek's own sheet directly. Everything else here came from write-ups,
because the noticeboards themselves were behind a gate I could not pass — read them before you
buy anything. The mechanism keeps: read the chart, take the top few, keep something always up,
and never let the rota reach inside the Pokémon.

## What a Gym Leader is listening for

* Why is `9 × 2048 = 18432` not a coincidence?
* Why does the note beside the name change who you pick and not how hard they hit?
* Your streak is fine and your slow turns are getting slower. What do you count first?
