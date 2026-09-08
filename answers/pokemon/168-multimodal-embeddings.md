---
id: "168"
slug: multimodal-embeddings
style: pokemon
category: multimodal
difficulty: intermediate
question: "How do you build a single embedding space for images and text?"
tags: [embeddings, modality-gap, hard-negatives, instruction-embeddings, ann, hybrid-search]
---

# You filed them in one box and they went into two

Question 120 built the shared filing system: drill silhouettes and Pokédex entries until they live
in the same place. This is about **using** one — and about the thing everybody discovers the first
time they open the drawer.

## They did not mix 🗄️

You trained shapes and words to land together. Go and look at where they actually landed:

```
   what everyone assumes              what is actually in the PC

     🖼️ 📖 🖼️ 📖 🖼️                    🖼️🖼️🖼️🖼️🖼️🖼️
     📖 🖼️ 📖 🖼️ 📖                          ( gap )
     🖼️ 📖 🖼️ 📖 🖼️                    📖📖📖📖📖📖

   two shapes compared to each other:  scores spread right across the range
   a shape compared to an entry:       a much lower, much narrower range
```

📌 **They are matched, and they are not mingled.** The drill only ever demanded that the *correct*
entry be nearer than the wrong ones — never that shapes and entries occupy the same corner. So they
politely arranged themselves into two boxes with a gap down the middle, and nothing ever objected.

Three things this breaks, in order of how often:

* **📏 One threshold cannot serve both.** A shape-to-entry score of 0.3 may be an excellent match
  while a shape-to-shape 0.3 is **Onix** and **Jigglypuff**. **Calibrate each pairing separately** or
  your cutoff is nonsense for one of them.
* **🔎 A mixed search returns one kind of thing.** Search with words across a PC holding **both**
  silhouettes and entries, and you get **entries**, every time — not because they answer better, but
  because they were sitting nearer. It is the **PC** returning six boxes of **Magikarp** because
  Magikarp happened to be filed first. Search each box separately and merge the results afterwards.
* **➕ And averaging a picture with a phrase** — a **Gyarados** photograph plus the words *"at the
  Lake of Rage"* — to make one combined query mostly does not work, for exactly the same reason. The
  average lands **in the gap**, where nothing is filed at all.

## What makes a filing system actually good 🎯

* **🔴 The near misses are the whole game.** In-batch wrong answers (question 120) get you started.
  What produces a system that can tell **the red Gyarados of the Lake of Rage** from an ordinary
  blue one is deliberately hunting down the **hard** pairs — near-identical shapes, entries
  differing by a single word — a **Clefairy** against a **Jigglypuff**, an **Alolan Vulpix** against
  a Kantonian one. ⚠️ Without them you get a drawer sorted by rough topic and nothing finer, and it
  will hand you an ordinary Gyarados when you asked for the shiny one.
* **🎯 Tell it what you are filing *for*.** Newer systems take the *intent* alongside the query —
  *"find the entry that supports this claim"* files differently from *"find one that looks like
  this"*. One fixed notion of similarity was always a compromise.
* **🔢 And keep an exact index alongside.** A drawer sorted by resemblance is **bad at exact
  identifiers**: a **Trainer ID**, a **Pokédex number**, `#025`. Somebody searching for `#025` wants
  **Pikachu**, not six Pokémon that look a bit like it. Plain exact lookup is superb at that. Run
  both and merge — do not choose.
* **🔍 Then look properly at the shortlist.** Pull fifty candidates by resemblance, then examine the
  top fifty **with the query and the candidate side by side**. 📌 **This is where the accuracy comes
  from.** The filing stage only has to make sure the right one is *somewhere* in the fifty.

## Two practical warnings 🔧

**📦 Big drawers cost.** Multimodal indexes are large and the cost scales with how much you store per
item. File short and re-rank with the long version.

**🔄 And when you get a better Pokédex, re-file everything.** ⚠️ Entries filed by the old one and the
new one are **not comparable** — they are two different filing systems sharing a cabinet. Mixing
them does not fail loudly. It just quietly makes every search a little worse, forever, and nobody
ever works out why.
