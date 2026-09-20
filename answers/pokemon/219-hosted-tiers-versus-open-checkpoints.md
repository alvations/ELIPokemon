---
id: "219"
slug: hosted-tiers-versus-open-checkpoints
style: pokemon
category: open-weights
difficulty: intermediate
question: "Qwen sells Flash, Plus and Max endpoints and also publishes downloadable checkpoints. Which of those can you actually run yourself?"
tags: [qwen, open-weights, api-products, naming, procurement]
---

# A rental at the Battle Factory is not the one in your box

At the **Battle Frontier**'s Battle Factory you do not bring your own team. You are shown six
randomly generated rentals, you pick three, and you battle with them. Win, and you may swap one of
yours for one belonging to the Trainer you just beat — **without being allowed to look at its
stats first**. Keep the streak going to the twenty-first battle and **Factory Head Noland** shows
up, using rentals himself, and hands out the Knowledge Symbol if you take him down.

Everything in that paragraph is true of a hosted endpoint. **Flash, Plus and Max are rentals.**
They are not sizes, they are not Pokémon you own, and they do not line up one-for-one with
anything in your **PC box**. The things you can actually keep are named the other way — by what
they are made of: `Qwen3.5-397B-A17B`, `Qwen3.8-27B`.

If a Qwen name carries a number, it is probably something you can catch. If it carries an
adjective, it is probably something you rent.

## The two ladders, side by side

```
   YOURS TO KEEP  (the Qwen team's own repo, "News" list — read directly)
   ────────────────────────────────────────────────────────────────────────
   2025-09-11   Qwen3-Next-80B-A3B
   2026-02-16   Qwen3.5-397B-A17B
   2026-02-24   Qwen3.5-122B-A10B · Qwen3.5-35B-A3B · Qwen3.5-27B
   2026-03-02   Qwen3.5-9B · Qwen3.5-4B · Qwen3.5-2B · Qwen3.5-0.8B
   2026-04-16   Qwen3.6-35B-A3B
   2026-04-22   Qwen3.6-27B
                ┌──────────────────────────────────────────────┐
                │  ← nothing here. No Qwen3.7 to catch at all. │
                └──────────────────────────────────────────────┘
   2026-08-12   Qwen3.8-2.4T-A95B
   2026-08-14   Qwen3.8-27B

   RENTAL ONLY  (the facility's own pool)
   ────────────────────────────────────────────────────────────────────────
   qwen3.5-flash · qwen3.5-plus · qwen3.6-flash · qwen3.6-plus
   qwen3.7-plus  · qwen3.7-max  · qwen3.8-flash · qwen3.8-max

                     ▲
                     └─ Qwen3.7 ran Max in May 2026 and Plus in June 2026
                        and never once as something you could carry out.
                        Like a species in the rental pool that appears in
                        no Tall Grass anywhere in the region.
```

The 3.7 gap is the proof. If the rental pool and the **Pokédex** were the same list, a whole
generation could not be on one and missing from the other.

## The trap: "the one you can keep is the Max one"

The Qwen team's own introduction says Qwen3.8 "brings a Qwen-Max-class model to open release", the
file is called `Qwen3.8-2.4T-A95B`, and the licence on it is called the *Qwen3.8-Max License*.
Three signs all pointing one way, and the conclusion is still wrong. A rental **Dragonite** and
the Dragonite in your box share a name and a Pokédex number and are **different individuals** —
different Nature, different spread, different four moves.

| | the one you keep | the one you rent |
| --- | --- | --- |
| What it takes in | text only | text, image, video |
| Thinking | always on; no switch | switchable |
| Range | 262,144 native, stretched to ~1,010,000 | a million by default |
| Extras | whatever you build | the facility's own |
| Terms | Qwen3.8-Max License (conditional) | the house rules |
| Identity | an **ID No.** you can read | a name the facility reuses |

Reading the rental's card and then going out to buy Poké Balls for it is how a Trainer ends up
with a full team slot and no vision at all. This is question 210's problem, louder: one name, two
Pokémon.

## Three checks that settle it in a minute

1. **Does the name say what it is made of?** `-27B`, `-397B-A17B`, `-2.4T-A95B` are caught.
   `-max`, `-plus`, `-flash` are rented.
2. **Is it on the list of things that were actually released into the wild?** The lab keeps a
   dated list of weight drops. That list, not a blog post and not a price board, is the Pokédex.
3. **Can you name its Original Trainer and the exact individual?** If you cannot say which
   revision you would pin, you are holding a rental, and the facility restocks its pool between
   rounds.

## What each one buys

A **rental** hands you capability you did not raise: it takes images and video, it opens at a
million by default, it comes with the facility's own tools, and somebody else feeds it. It costs
you the right to look at its stats, to change its moves at the **Move Reminder**, or to take it
home.

A **caught** Pokémon gives you the individual: an ID No. you can pin, EVs you can choose, a
**Move Deleter** and a **Name Rater** who will work on it, and terms printed on the ball it came
in (question 222). It costs you everything the facility was quietly supplying — and on the 3.8
pair that list includes *sight itself* and *the ability to stop thinking*, which nobody files
under "amenities".

## What a Gym Leader is listening for

That "Qwen3.8 is open" is not a sentence with one answer. Then that you ask which of the two the
benchmark, the price and the capability list are each about, because in this family they are
routinely about three different things. The strongest answers say what they would write on the
Trainer Card: which repository, which revision, which licence file, and the date — so the next
person is not re-deriving it from a poster on the facility wall.

## Where this stands, September 2026

The release dates and the complete absence of a Qwen3.7 you can keep come from the Qwen team's own
repository, read directly. The rental list, the prices and the rented-versus-caught capability
gaps come from coverage, because the cloud catalogue, the release blog, the developer docs and the
model cards are all behind an egress block here — those pages are the authority. Rental names and
prices rot fastest of anything above. The shape — two lists, one of Pokémon and one of
services — is what keeps.
