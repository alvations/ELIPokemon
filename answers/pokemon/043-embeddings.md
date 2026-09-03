---
id: "043"
slug: embeddings
style: pokemon
category: rag
difficulty: core
question: "What are embeddings and how are embedding models trained?"
tags: [embeddings, contrastive, infonce, matryoshka, cosine-similarity]
---

# Embeddings: giving every Pokémon a place on the map

Imagine a giant map where **similar Pokémon stand near each other.**

Charmander, Charmeleon and Charizard cluster together. Squirtle is way over on the other side, near
Wartortle. Pikachu and Raichu are a pair. Ditto is off on its own being weird.

Nobody drew this map. It emerged from what the Pokémon *are*.

An embedding is a Pokémon's **coordinates on that map**. And once everything has coordinates,
"what's similar to this?" becomes "what's *nearby*?" — which is a question you can answer instantly.

## Why this beats keyword matching 🔍

> *"How do I heal my Pokémon?"* and *"where can I restore HP?"*

**Zero words in common.** A keyword search finds nothing. But on the map, those two questions land
practically on top of each other, because they *mean* the same thing.

That's the entire value. The map is built from meaning, not spelling.

## How you build the map 🗺️

You don't measure anything. You just **shove things around** based on examples:

```
                          THE MAP
        ┌─────────────────────────────────────────┐
        │                                         │
        │   ❓ "how do I heal?"                    │
        │      ╲                                  │
        │       ⬅ PULL together                   │
        │        ✅ "Pokémon Centers restore HP"   │
        │                                         │
        │                 ❌ "how to catch Mew"    │
        │      PUSH ➡    ╱     ❌ "TM locations"   │
        │           ────╯     ╱                   │
        └─────────────────────────────────────────┘
```

* ✅ Question and its real answer → **drag them together.**
* ❌ Question and anything else → **shove them apart.**

Millions of times. The map organises itself.

## The two things that decide if it works 🎯

**1. 👥 Compare against lots of things at once.**

Don't just push one wrong answer away. Line up **hundreds** and say "this one, not any of those."
Every comparison is a lesson, and they're nearly free — you're already holding them.

**2. 🔥 Push against things that are ALMOST right.**

The big one.

Teaching *"how do I heal?" is closer to "Pokémon Centers heal you" than to "Mew is in the truck"* is
**worthless**. Of course it is. Those aren't remotely similar, and the map already knew.

Teaching *"how do I heal?" is closer to "Pokémon Centers heal you" than to "Potions restore HP but
cost money"* — **that's a real lesson.** Both are about healing. Only one answers the question.

📌 Finding those near-misses is most of the work in building a good map. Easy negatives teach
nothing.

## Things that silently ruin your map 🚨

**🏷️ Forgetting the label.** Many maps need you to say whether you're placing a *question* or an
*answer* — they sit in different neighbourhoods. Forget the label, get quietly terrible results
with no error message anywhere. This is a top-three cause of "our search just doesn't work."

**✂️ Long reports get cut off.** Most maps only read the first 512 words. Everything after that is
**silently discarded**. Your beautifully detailed report was filed based on its first paragraph.

**🌍 The wrong map for your world.** A general-purpose map trained on everyday text does poorly on
specialist material. If your reports are full of competitive jargon, a map that's never seen it
places everything in a heap.

**🔄 Redrawing the map means refiling everything.** New map, new coordinates, all your old
coordinates are meaningless. There is no partial migration.

## Where the map genuinely fails 📉

**🚫 Negation.** This one is embarrassing.

> *"Gyarados is weak to Electric"* and *"Gyarados is **not** weak to Electric"*

On the map these sit **almost exactly on top of each other**. Nearly the same words, so nearly the
same place. The map has no real notion of "not."

**🔢 Exact codes.** Looking for item ID `TM24`? The map thinks `TM24` and `TM25` are basically the
same thing. They are not.

Both failures point the same way: **keep a plain keyword search alongside the map.** The map handles
meaning; keyword handles exactness. You need both, and running only one is the most common design
mistake there is.

## A neat trick 🪆

Some maps are built so that **the first few coordinates alone still work**. Use just the first
quarter of each Pokémon's coordinates for a lightning-fast rough sweep, then the full coordinates to
rank the survivors precisely.

Quarter the storage, a fraction of the search time, barely any accuracy lost.
