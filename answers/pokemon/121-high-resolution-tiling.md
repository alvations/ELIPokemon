---
id: "121"
slug: high-resolution-tiling
style: pokemon
category: multimodal
difficulty: intermediate
question: "How do vision-language models handle high-resolution images?"
tags: [resolution, anyres, tiling, position-interpolation, token-budget, navit]
---

# You cannot read the Ruins of Alph wall from the doorway

The lens on a Pokédex was built for one job: stand in the long grass, point at a Rattata, get an
answer. At that distance a Rattata fills the frame and everything works.

Now take it into the **Ruins of Alph** and point it at a wall covered in tiny **Unown** carvings.
Same lens. Same frame. The entire wall gets squeezed down into the same small picture a single
Rattata used to occupy — and every carving on it is now smaller than one tile.

The Pokédex is not confused. **The writing is not in the picture any more.** It was thrown away
before the machine ever got to think about it.

## Why you cannot just build a bigger lens 🔭

Three things snap at once.

1. **📍 Every tile's coordinate stamp becomes wrong.** The lens learned on a grid of a certain
   size, and every stamp means "row three of twenty-four". Double the grid and there is no stamp
   for row forty. You have to invent the missing ones by stretching the old ones — which works
   better than it has any right to, and is still not what the lens was trained on.
2. **🧾 The tile count explodes.** Twice the width and twice the height is **four times** the
   tiles, and every one of them goes into the Pokédex's working memory alongside the question.
3. **💸 And the tiles all have to consider each other.** Four times the tiles is roughly
   **sixteen** times the work.

## What you actually do: walk up to it, section by section 🚶

This is what a person does in the Ruins without being taught. You do not squint harder from the
doorway. You **walk up to one section of wall, read it, and move along.**

```
   the whole wall
        │
        ├─► split it into sections that each fill the frame properly
        │
        │       ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
        │       │ panel 1 │ │ panel 2 │ │ panel 3 │ │ panel 4 │   read up close,
        │       └─────────┘ └─────────┘ └─────────┘ └─────────┘   each at full detail
        │
        └─► AND step back for one shot of the whole wall
                ┌─────────┐
                │  🗺️ all  │   no detail — but it tells you panel 3 was the middle-left one
                └─────────┘

   hand over:  [ the wide shot ] + [ panel 1 ] + [ panel 2 ] + [ panel 3 ] + [ panel 4 ]
```

📌 **The wide shot is the bit everyone skips.** Panels alone give you every carving in perfect
detail and no idea how they were arranged — you can read panel 3 and not know it was the middle
of the wall rather than the end of it. That is the difference between reading a **Town Map** and
reading four unlabelled scraps of one.

## Paying for all those panels 🪙

Four panels plus a wide shot is five frames' worth of tiles for a single wall, and the Pokédex
still has to hold the Trainer's question as well. Ways to bring the bill down:

* **🧩 Fold tiles together in twos and twos.** Take each little two-by-two block of tiles and fuse
  it into a single fatter tile that carries everything all four held. Four times fewer slots and
  *nothing thrown away* — the detail is still in there, just packed differently. This is the one
  to reach for first.
* **✂️ Throw away tiles that look like their neighbours.** Sky, grass, blank stone. Excellent on a
  photograph of a Pokémon in a field. **Ruinous on a wall of carvings**, where the tile that looks
  like plain rock is the one with the faint mark on it.
* **🎯 Insist on a fixed small number of scouts** no matter how big the wall is. Bounds the cost
  absolutely; bottlenecks the detail absolutely.
* **🧱 Or just cap the panels** and accept that past a certain size you are squinting again.

## Wailord does not fit in a square box 📦

Almost nothing you actually want to look at is square. **Wailord** is 14.5 metres of Pokémon and
barely any of it is height. **Diglett** is twenty centimetres and almost all of it is hidden.
Cram both into the same square frame and you get a squashed Wailord and a Diglett floating in a
sea of nothing.

⚠️ Padding the frame out to square is *honest* and wasteful — you pay full price for tiles of
empty background. Keeping a **menu of frame shapes** and picking the closest one is what most
Pokédexes do. Best of all is not forcing a shape at all: photograph each thing at its own
proportions and pack the odd-shaped results in together, which needs a lens built for it from the
start.

## Do not be fooled by the scoreboard 🏅

* 📏 **Always say what distance you were standing at.** "This Pokédex beats that one" means
  nothing if one of them walked up to the wall and the other stayed in the doorway.
* 🔍 **Walking closer only helps for fine print.** For "is that a Snorlax", the doorway was always
  enough. Average the carving-reading test together with the is-that-a-Snorlax test and the whole
  effect vanishes into the mean.
* 🩹 **Check the stretched coordinate stamps.** If they are subtly wrong, everything gets slightly
  worse and nothing breaks outright — which is far harder to catch than one thing failing loudly.
