---
id: "118"
slug: image-patches-tokenisation
style: pokemon
category: multimodal
difficulty: core
question: "How is an image turned into tokens a transformer can read?"
tags: [vit, patches, position-embeddings, patch-size, pooling]
---

# The Ruins of Alph already solved this

Go north-west out of Violet City and there are four sealed chambers in the ground. Each one has a
**slate puzzle** set into the wall: a picture, cut into square tiles, scrambled. Put the tiles
back in the right places and the picture resolves — **Kabuto** in one chamber, **Omanyte** in
another, **Aerodactyl** in the third, **Ho-Oh** in the fourth. Solve them and the **Unown** start
appearing in the tunnels below.

That is the whole technique. **A picture is not something a reader can read. A row of tiles is.**

## Cut, flatten, hand it over 🧱

```
   the slate:  a picture of Kabuto
        │
        ├─ cut into a grid of equal square tiles
        │
        │      ┌──┬──┬──┬──┐
        │      │ 1│ 2│ 3│ 4│      each tile is just... a small square of picture
        │      ├──┼──┼──┼──┤
        │      │ 5│ 6│ 7│ 8│      nothing clever. no cleverness anywhere.
        │      ├──┼──┼──┼──┤
        │      │ 9│10│11│12│
        │      ├──┼──┼──┼──┤
        │      │13│14│15│16│
        │      └──┴──┴──┴──┘
        │
        └─ hand them over as a ROW:  [1][2][3][4][5][6] ... [16]
```

No hierarchy. No clever feature-finding. No one deciding in advance which parts of Kabuto matter.
Just: identical squares, in a row, each one turned into a description of what is in that square.

## The tiles have to remember where they sat 📍

Here is the part the Ruins of Alph teach by being a *puzzle*: **a pile of tiles is not a
picture.** Scrambled, the slate is meaningless. Reordered, it is Kabuto.

A reader handed sixteen loose tiles has no idea which was top-left. It would see the same bag of
squares whether Kabuto's eyes were above its shell or below it, and it would be equally happy
with either. Everything the picture *meant* lived in the arrangement, and cutting it up threw the
arrangement away.

So every tile gets stamped with its own coordinates before it goes in the row. That stamp is not
decoration; it is the only thing standing between you and a scrambled slate.

⚠️ And it is why swapping puzzles bites. If your reader learned on a **four-by-four** slate and
you hand it a **six-by-six**, every stamp now means something different — tile 5 used to be the
start of row two and now it is still in row one. The picture does not resolve. Nothing errors.
You just get worse answers and no explanation, which is the worst kind of failure to debug.

## How fine to cut ✂️

| Tiles | What you can make out | What it costs |
| --- | --- | --- |
| Very few, very big | Ho-Oh's silhouette. That it is a bird. | Almost nothing |
| Middling | Ho-Oh's crest, the tail feathers, the wing pattern | The usual price |
| Very many, tiny | Individual feathers | Ruinous — every tile has to consider every other tile |

📌 **Anything smaller than one tile does not exist.** This is the sentence to remember. If you cut
the slate into sixteen tiles, a detail finer than a tile is not blurry — it is *gone*, averaged
into the square that swallowed it.

Which is exactly why a Pokédex that identifies **Aerodactyl** from a hundred metres away cannot
read the label on a TM. It is not being stupid. At the tile size it was built with, the writing
was never in the picture at all.

## Getting one answer out of sixteen tiles 🎴

Sometimes you want a *verdict*, not sixteen descriptions — "this slate is Omanyte." Two habits:

* **Send a delegate.** Add one extra blank tile that has no picture on it, whose only job is to
  listen to the other sixteen and report. Ask the delegate at the end.
* **Take the average.** Just pool all sixteen tiles together.

Both work. For a Pokédex, though, you usually want **neither** — you keep all sixteen tiles,
because when the Trainer asks *"what is in the top-left corner?"* a summary of the whole slate
cannot answer, and only the actual top-left tile can.

## Other ways to cut a slate 🗿

* **🔤 Cut it into letters instead of squares.** The Unown are the version of this idea taken
  seriously: twenty-eight fixed shapes, and any picture you want written as a string of them.
  You lose everything that was not exactly one of the twenty-eight shapes — but now a picture is
  literally spelled, and anything that can spell can draw.
* **🏔️ Cut coarse, then re-cut the interesting parts finer.** Big tiles for the mountain,
  small tiles for the Aerodactyl on it. More machinery, much better when you need to point at
  exactly where something is.
* **📐 Stop forcing everything into a square.** A slate is not square and a tall waterfall is not
  square. Squashing both into the same box distorts them. Cut each at its own shape and pack the
  tiles in together instead.
