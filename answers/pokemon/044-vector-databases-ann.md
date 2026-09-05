---
id: "044"
slug: vector-databases-ann
style: pokemon
category: rag
difficulty: intermediate
question: "How do vector databases work? Explain HNSW and IVF."
tags: [ann, hnsw, ivf, pq, vector-database, recall]
---

# Finding the nearest Pokémon without checking all 100 million

You've got your map. Now: *"find me the Pokémon most similar to Gyarados."*

The honest way is to measure the distance to **every single Pokémon on the map**. With a hundred
million of them, that's a long walk for one question.

So you accept a deal: **give up on always finding the exact nearest one, in exchange for being a
thousand times faster.** You'll find the true nearest maybe 95% of the time, and something
extremely close the rest. For search, that's a fantastic trade.

## Method 1: Fly Points 🗺️

Build a network of shortcuts, layered like the Fly network — Pallet Town to Viridian to Pewter,
or one hop straight to Cinnabar.

```
  ✈️ TOP LAYER — a few major cities, huge distances
     ●──────────────────────●──────────────────●

  🚲 MIDDLE — towns, medium hops
     ●───●──────●────●─────●───●────●──●

  🚶 GROUND — every single Pokémon, tiny steps
     ●─●─●─●─●─●─●─●─●─●─●─●─●─●─●─●─●─●─●─●

  How you search:
    1. ✈️ Fly to whichever major city is closest to your target.
    2. 🚲 Drop a layer. Cycle to the nearest town.
    3. 🚶 Drop again. Walk to the nearest neighbour, repeat until
       no neighbour is closer.
    ✅ You've arrived, in a handful of hops instead of 100 million steps.
```

Beautiful, and the fastest good option there is. The cost: **the road network is often bigger than
the map it sits on.** You're storing every shortcut from every Pokémon. And removing a Pokémon
leaves a hole in the roads that you have to patch up periodically.

## Method 2: Regions 🏞️

Divide the map into regions — Kanto, Johto, Hoenn, Sinnoh — each with a centre.

```
   ┌─────────┬─────────┬─────────┐    your target is here ─┐
   │ 🌲KANTO │ 🏔️JOHTO │ 🌊HOENN │                        ▼
   │  ● ● ●  │  ● ● ●  │  ● ● ●  │              ┌──────────────┐
   ├─────────┼─────────┼─────────┤              │   ❄️ SINNOH   │
   │ ❄️SINNOH│ 🏜️UNOVA│ ⚡KALOS │              │ search only  │
   │  ●●✕●●  │  ● ● ●  │  ● ● ●  │              │   this one   │
   └─────────┴─────────┴─────────┘              └──────────────┘
```

Work out which region your target is in, then **only search that region**. Six regions means a
sixth of the work — and with a thousand regions, a thousandth.

The flaw is obvious once you see it: **what if the nearest Pokémon is just over the border?**

```
        SINNOH  │  UNOVA
                │
           ✕    │  ●      ← this is genuinely the closest,
           your │           and you never looked at Unova
          target│
```

The fix is to search the **three or four nearest regions** rather than one. Slower, catches the
border cases. That's your dial: search more regions for better results, fewer for speed.

Cheaper to build and much lighter than the Fly network — which is why it's what you use at truly
enormous scale.

## Method 3: Shorthand coordinates 🗜️

At a hundred million Pokémon, even *storing* the coordinates is a problem.

So round them. Instead of precise coordinates, record *"north-ish region, mid-elevation, coastal."*
A third of a page becomes a few characters.

Coarse — but good enough to narrow a hundred million down to a hundred candidates. Then you pull the
**full precise coordinates for just those hundred** and rank them properly.

📌 **Rough sweep, then careful check.** That two-stage pattern is how every genuinely huge search
system works.

## Which to use 🎯

| Map size | Method |
| --- | --- |
| 🤏 Under 10,000 | **Just check them all.** Fewer than the National Dex, twice over. It's fast enough and it's exactly right. |
| 📗 10k – 10M | ✈️ Fly network |
| 📚 10M – 1B | 🏞️ Regions + 🗜️ shorthand |
| 🏛️ Over 1B | Regions + shorthand + split across many buildings |

That first row is genuine advice. An enormous number of teams install elaborate machinery for eight
thousand documents.

## What bites you in production 🚨

**🔒 "Only show me Kanto Pokémon, caught after March."** Filtering fights the shortcuts. Filter
*before* searching and you've cut the roads your search needed. Filter *after* and you may return
nothing at all. Handling this properly is what actually separates one system from another.

**🗑️ Deletions rot the network.** You can't cleanly remove a stop from the Fly network. You mark it
dead and route around it, and things degrade until you rebuild.

**👻 You cannot see what you missed.** This is the scary one. When your search misses the right
answer, **nothing tells you.** No error, no warning — just a slightly worse answer that looks
completely normal.

📌 Periodically take a sample of queries, run the slow exact search, and compare. It's the only way
to know your search is still working.
