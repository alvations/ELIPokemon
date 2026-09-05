---
id: "087"
slug: curse-of-dimensionality
style: pokemon
category: fundamentals
difficulty: intermediate
question: "What is the curse of dimensionality?"
tags: [curse-of-dimensionality, concentration-of-measure, knn, manifold-hypothesis]
---

# The curse of dimensionality: everyone is equally far away

You want to find **similar Pokémon**. Sounds easy.

## With one stat 📏

Sort everyone by Speed. Similar Speed, similar Pokémon — Jolteon next to Aerodactyl, Shuckle next
to Snorlax. Ten Pokémon covers the whole range nicely.

## With two stats 📊

Speed and Attack. Now you need a **grid** — fast-and-strong (Garchomp), fast-and-weak (Ninjask),
slow-and-strong (Snorlax), slow-and-weak (Magikarp) — and to cover it at the same resolution you
need a hundred Pokémon, not ten.

## With six stats 📈

To cover six-dimensional space at that resolution: **a million Pokémon.**

You have a thousand.

```
   1 stat:      🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴          nicely covered
   2 stats:     🔴 ⬜ 🔴 ⬜ ⬜ 🔴 ⬜ 🔴        getting sparse
   6 stats:     🔴 ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜
                ⬜ ⬜ ⬜ ⬜ ⬜ 🔴 ⬜ ⬜ ⬜ ⬜
                ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ 🔴      almost entirely empty
```

## The genuinely weird part 🤯

With six stats, sparseness is annoying. With **a thousand** measurements per Pokémon, something
stranger happens.

**Everyone is the same distance from everyone else.**

```
   📏 A FEW MEASUREMENTS              📊 A THOUSAND MEASUREMENTS
   ┌────────────────────┐             ┌────────────────────┐
   │  ●                 │             │   ● ● ● ● ● ●      │
   │       ✕ ← close    │             │  ● ●  ✕  ● ●       │  the nearest and
   │             ●      │             │   ● ● ● ● ● ●      │  the furthest are
   │   ●    ← far       │             │  ● ● ● ● ● ● ●     │  almost identical
   └────────────────────┘             └────────────────────┘
   "similar" means something          "similar" means nothing
```

Why: with a thousand measurements, **every** pair of Pokémon differs somewhere. Nobody matches on all
thousand. So every distance ends up around the same middling value, and "nearest neighbour" becomes a
coin flip between candidates that are all equally unlike your query.

📌 This breaks **anything built on similarity** — finding similar Pokémon, grouping them into
clusters, spotting the odd one out. The concept of "close" has stopped carrying information.

## So why does any of this work? 🤔

Because **real Pokémon don't fill the space.**

Imagine every mathematically possible combination of a thousand measurements. Almost all of them
are **nonsense** — creatures with Arceus's Attack and Magikarp's HP, with contradictory typings,
with Sturdy and Levitate at the same time.

Real Pokémon occupy a **tiny, highly structured pocket** of that enormous space. They cluster into
families. Stats correlate. Types constrain movesets.

```
   🌌 Everything the space allows:  ENORMOUS, and 99.999% nonsense

        ┌──────────────────────────────────────────┐
        │                                          │
        │                  🐛 ← real Pokémon        │
        │              🐛🐛🐛🐛                     │   a thin, curved,
        │            🐛🐛🐛🐛🐛                     │   structured ribbon
        │              🐛🐛🐛                       │   inside an enormous
        │                                          │   empty space
        │        (everything else: impossible)      │
        └──────────────────────────────────────────┘
```

And **on that ribbon, distance means something again.** Two Pokémon near each other on the ribbon
genuinely are similar, even though they're both floating in a thousand-dimensional void.

📌 **This is why the map works.** A good map isn't placing Pokémon randomly in a huge space — it
learned **where the ribbon is**, and lays them out along it. That's precisely the trick that rescues
"nearest neighbour" from meaninglessness.

The curse applies to points scattered **uniformly** through a huge space. Real data is never
uniform — and that's the only reason any of this is possible.

## What to do about it 🛠️

* 📉 **Compress to the axes that matter.** Find the handful of directions Pokémon actually vary along
  and work in those.
* 🗺️ **Learn a map instead of using raw measurements.** Build coordinates *designed* so that
  distance means what you need.
* ✂️ **Use fewer measurements.** Six base stats told you most of it. Often the honest answer.
* 📐 **Compare direction, not distance.** For very sparse descriptions, *"do these point the same
  way?"* survives much better than *"how far apart are they?"*
* 📚 **Get more Pokémon.** The only real cure for sparseness, and it gets exponentially more expensive
  with every measurement you add.
