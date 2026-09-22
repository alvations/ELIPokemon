---
id: "249"
slug: a-generation-that-never-opened
style: pokemon
category: open-weights
difficulty: advanced
question: "Qwen 3.7 shipped as Max and Plus and never as weights. How do you plan around a generation you can only rent?"
tags: [qwen, open-weights, roadmap-risk, procurement, release-cadence]
---

# **Hoenn** was finished, and no cable in the world reached it.

Stand where a **Johto** Trainer stood in 2003. You have a Game Boy cartridge, a **Typhlosion** you
raised from a hatchling, and a **Pokédex** that ends at **Celebi**, number 251. Across the shop
window is **Hoenn**: **Treecko**, **Torchic** and **Mudkip** on **Professor Birch**'s table,
**Norman** running a Gym, **Rayquaza** at the top of the Sky Pillar, **Kyogre** and **Groudon**
under the sea and under the earth, **Wallace** waiting in **Sootopolis City**. All of it real. All
of it finished.

And there is **no link cable that fits**. Not a slow one, not an expensive one — none. A Pokémon
caught on a Game Boy cannot be traded into Hoenn, and nothing in Hoenn can be traded back. The
generation happened; the connection did not.

That is Qwen 3.7 exactly. It exists, and it is not available to you.

## Both halves of the evidence

**That Hoenn is real** — from the team's own noticeboard. The Flash-Next notes say the hybrid
design *"has since been used across the Qwen3.5, Qwen3.6, Qwen3.7 and Qwen3.8 series"*, and then
measure themselves against it: *"Compared with Qwen3.7-Plus... training takes only about 1/9 as
much."* Nobody compares their training bill against a region that was never built.

**That nothing from it can be caught** — from the same noticeboard. The list of things released
into the wild runs 2026-04-22, then straight to 2026-08-12. And the front line of that same page
says the open series is *"Qwen3.5, Qwen3.6, and the latest Qwen3.8."* Four series when they talk
about how the models are built; three when they talk about what you may keep.

One more thing, checked by hand. Their workshop has been renamed forward at every open generation,
so asking for the noticeboard under **four different names** — Qwen3-Next, Qwen3.5, Qwen3.6,
Qwen3.8 — returns the same page, byte for byte, one fingerprint across all four. Asking under
Qwen3.7 returns nothing at all. They never hung a sign with that name on it.

```
   YOURS TO KEEP                       RENTAL COUNTER ONLY
   ────────────────────────────        ──────────────────────────────
   2026-02-16  Qwen3.5-397B-A17B       2026-02··  qwen3.5-plus / flash
   2026-02-24  122B-A10B · 35B-A3B
               · 27B
   2026-03-02  9B · 4B · 2B · 0.8B
                                       2026-04-02  qwen3.6-plus
   2026-04-16  Qwen3.6-35B-A3B
   2026-04-22  Qwen3.6-27B
        ╷                              2026-05-19  qwen3.7-max
        ╷  ← 112 days. Nothing.        2026-06-01  qwen3.7-plus
        ╷     Not late. Skipped.
   2026-08-12  Qwen3.8-2.4T-A95B       2026-08··   qwen3.8-max
   2026-08-14  Qwen3.8-27B
   2026-08-26  Qwen3.8-Flash-Next

   Left: the lab's own dated list, read directly.  Right: coverage.
```

The cruel detail is that **the numbering never skipped**. **Celebi** is 251 and **Treecko** is
252; the book runs straight on across the break. A continuous list of numbers is not a promise
that you can reach every one of them, and 3.6 → 3.7 → 3.8 is the same continuous, unhelpful list.

## What it costs a Trainer, in four parts

**1. A number on a box is not a promise.** The things you can catch and the things you can rent
are two separate lists (question 219), and Hoenn proves they advance on their own schedules.
"We'll move to the next one when it lands" has not said which list it means.

**2. Cadence is not a timetable.** February, April, then August. A Trainer who drew a line through
the first two and cleared out a **PC box** for a June arrival cleared it for nothing.

**3. The gap between rented and caught breathes.** It is not a fixed discount. It widens every
month a generation stays shut and closes when the next one opens — which is why Qwen 3.8's own
line is *"for the first time, Qwen3.8 brings a Qwen-Max-class model to open release."* That
sentence is a measurement of how far ahead the rental counter had got.

**4. A gap is evidence, but not of failure.** The dated list is the Pokédex of what exists as
bytes, and a hole in it is real. It does not mean the region was abandoned: the lab still measures
itself against 3.7-Plus.

## What you actually do

- **Decide your fallback before the break**, not during it. If the next generation is rental-only
  for six months: stay, rent, or change region. That choice is free today.
- **Keep both legs warm.** Rented capability costs you the **ID No.** you could have pinned, the
  **Move Reminder** you could have visited, and the terms you could have read (question 222).
- **Set your floor at the last generation that opened.** In June 2026 that was Qwen3.6-27B, and
  the honest options were: run it, rent 3.7, or go and catch somebody else's.
- **Write the date beside the decision.** The break did heal — but one generation later and one
  way only, the way **Pal Park** let Hoenn's Pokémon walk forward into **Sinnoh** and never back.
  Nothing from the Game Boy ever reached Hoenn, and no 3.7 weights ever appeared behind the gap
  either.

## What a Gym Leader is listening for

That you can hold "the region is finished" and "I cannot reach it" in the same hand without
treating the second as a softer version of the first. Then that you plan for the break instead of
betting it will not come. The strongest answers notice what a skipped generation gives you for
free: a **measurement** of how wide the gap between the rental counter and your own box can get at
this lab, which is precisely the number your fallback plan needs.

## Where this stands, September 2026

The two lines naming Qwen3.7 and Qwen3.7-Plus, the dated release list, and the three-series
enumeration of what is open come from the Qwen team's own repositories, read directly. The
four-names, one-fingerprint rename chain and the missing Qwen3.7 sign were checked by hand here.
**The rental dates — 3.7-Max on 2026-05-19, 3.7-Plus on 2026-06-01 — are coverage**, because the
blog and the cloud catalogue are behind an egress block; that catalogue is the authority. If 3.7
weights ever appear, the headline is wrong and none of the planning changes.
