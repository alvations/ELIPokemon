---
id: "014"
slug: scaling-laws
style: pokemon
category: training
difficulty: intermediate
question: "Explain neural scaling laws and the Chinchilla compute-optimal result."
tags: [scaling-laws, chinchilla, compute-optimal, kaplan, inference-cost]
---

# Scaling laws: Rare Candy or actual battles?

You have a fixed budget for the summer. You can spend it two ways:

* 🍬 **Rare Candy** — pure levels. Bigger numbers, right now.
* ⚔️ **Actual battles** — slower, but your Pokémon learns from every fight.

The scaling law question is: *what's the split?*

## The first answer was wrong 🍬

For years the accepted wisdom was **"mostly Rare Candy."** Get the level up. Levels are what
win battles. Feed the candy, hit Level 100, worry about experience later.

So everyone built enormous, under-battled Pokémon: Level 100 with the battle instincts of a Level
25. Huge stats, no idea what to do with them.

## Chinchilla: it's roughly 50/50 ⚖️

Then someone actually ran the experiment properly — four hundred training runs, each with a
schedule tuned for its own budget rather than one schedule copy-pasted across all of them. That
detail was the whole bug: the old study had handicapped exactly the "fewer levels, more battles"
corner it then declared inferior.

The corrected answer: **level and experience should grow together.** Roughly **20 battles per
level.**

```
   Fixed summer budget — where do you spend it?

   how │  ╲                                   ╱
   bad │   ╲      the old advice ──┐         ╱
        │    ╲                     ▼        ╱
        │     ╲___             ╱‾‾‾╲      ╱
        │         ‾‾‾──────────     ─────
        │              ▲
        │              └── sweet spot: ~20 battles per level
        └──────────────────────────────────────────────►
       all candy                              all battles
       (Lv100, clueless)                  (Lv15, brilliant, still dies
                                           to a Gym Leader's stat check)

   The proof: a properly battled Lv70 Chinchilla beat a candy-stuffed
   Lv280 Gopher, on the same summer budget, at nearly everything.
```

Four times smaller. Four times more battle experience. Won anyway.

## The plot twist 🔁

Chinchilla answers *"cheapest way to raise a strong Pokémon."*

But nobody raises a Pokémon to admire it in the PC box. You're going to **battle with it every
single day for years.** And here's the thing: your daily costs scale with your Pokémon's
**level**, not with how many battles it took to get there. A Level 280 monster is expensive to
field every single day. A Level 70 is cheap forever.

So if you're going to compete daily, the right move is deliberately "wrong":

> **Keep the level low. Grind battles way past the point of diminishing returns.**

Pay once in a brutal training summer. Save every single day after.

That's why modern teams raise Level 7-to-70 Pokémon on **15,000 battles** — ratios of 300:1
instead of 20:1. Wildly "inefficient" by Chinchilla, completely correct in practice, because the
summer is one bill and the season is a thousand.

## The genuinely useful part 🔮

The real power of a scaling law isn't the ratio. It's **prediction**.

Raise a few cheap Pokémon on small budgets. Plot how good they get. The curve is so smooth and
regular that you can read off, in advance, how strong a Pokémon costing your **entire year's
budget** will be — before you spend a single dollar of it.

That's the difference between betting the season on a hunch and knowing what you're buying.

## Four caveats ⚠️

**Low loss ≠ wins tournaments.** The curve predicts how well your Pokémon predicts. It's much
vaguer about whether it beats the Elite Four.

**Battle quality matters more than the law says.** 1,000 real Gym battles beat 10,000 fights
against wild Rattata. Curation shifts the whole curve; the law's *shape* is stable, its
*position* isn't.

**You can run out of opponents.** There are only so many good trainers. (Rematches help — about
four times through the same circuit is nearly as good as fresh opponents. After that, sharply
diminishing.)

**The summer isn't the whole story.** What actually makes a Champion is everything *after* the
grind — the coaching, the tournament practice, learning to take instruction. None of that is in
these curves at all.
