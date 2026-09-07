---
id: "140"
slug: multimodal-retrieval
style: pokemon
category: multimodal
difficulty: intermediate
question: "How do you build retrieval over documents that contain images and tables?"
tags: [multimodal-rag, colpali, late-interaction, captioning, chunking, citation]
---

# Searching an archive where the answer is in a picture

Ordinary searching (question 044) assumes what you want is written down somewhere. Real archives
refuse to cooperate. The **Type Chart** is a grid. **Blissey**'s stats are a hexagon with one spike.
**Route 1** is a shape on the **Town Map**. **Aerodactyl** is a slate puzzle in the **Ruins of
Alph**. And half of **Professor Oak**'s notes say *"see the photograph"*.

Three ways to build it, and they are genuinely different bets.

## 1. Send a scribe round to describe everything ✍️

Have somebody look at each photograph and write down what is in it. Now search the writing.

```
   the page ─► a scribe describes it ─► words ─► search the words, as normal
```

Simple, and it reuses everything you already have. And it is **lossy at the exact point where you
cannot get it back**. Whatever the scribe did not think to mention is now **unfindable forever**.
The scribe wrote *"a very bulky pink Pokémon"* and moved on; nobody can now ask which Pokémon has
**255** base HP, because the number was never written down. Same for the **Leftovers** in the held
item slot, the ♀ after **Nidoran**, and the Trainer's signature at the foot of the page.

📌 Fine when the archive is mostly writing with the occasional picture. Hopeless when the picture
*is* the answer.

## 2. Put shapes and words in the same place 🎴

This is the silhouette drill from question 120, used as a filing system: teach shapes and
descriptions to live in one space, then search both at once with a single question.

Elegant — and it inherits **every** weakness of that drill, exactly. Word order does nothing, so
*"the Gyarados behind the Magikarp"* files identically to the reverse. Fine detail is invisible.
Writing inside a picture barely registers. Good for a shelf of **Pokémon Snap** photographs. Poor
for a page of the **Celadon Department Store** directory, where every word that matters is printed
small.

## 3. Leave the pages as pages 📄

No scribe, no describing. **Keep every page as a picture, chopped into tiles** (question 118), and
let each word of the question go and find its own tile.

```
   the question:     "which"   "floor"   "sells"
                        │         │         │
   the page's tiles: ┌──┴─────────┴─────────┴──┐
                     │  ▓  ▒  ░  ▓  ▒  ░  ▓  ▒ │   every word finds the tile that
                     │  ░  ▓  ▓  ▒  ░  ▓  ░  ▒ │   answers IT, and the scores add up
                     └─────────────────────────┘
```

Layout survives. Figures survive. Small print survives. And — the lovely part — **it points at the
answer for free**: the tiles that won *are* where the answer is, so the citation comes out of the
search itself rather than being reconstructed afterwards (question 128).

⚠️ The bill is real. Hundreds of tiles per page instead of one description, stored forever. That
cost is the actual decision, not a footnote to it.

## What you must not cut in half ✂️

Everyone argues about how to chop up writing. Almost nobody thinks about how to chop up a page, and
it sets your ceiling.

* 🖼️ **Keep a figure with its caption and the paragraph that points at it.** Split them and you have
  ruined both — the hexagon means nothing unlabelled, and the sentence saying *"note the Defence
  spoke"* now points at nothing.
* 🚫 **Never split the Type Chart.** The header row without the grid, or the grid without the
  header, is **worse than dropping it entirely** — because it will still be found, and it will
  still be answered from, and somebody will be told that **Surf** is not very effective on
  **Charizard** when it is one of the few things Charizard genuinely fears.
* 📄 **The page is usually the right unit**, because the page is the unit somebody designed it in.
* 🧭 **Carry the section heading along** (question 123), so a retrieved fragment still knows which
  chapter it came from.

## Then it still has to read what it found 🔭

Finding the page is half the job. The Pokédex now has to actually **read** it — close enough to
make out the small print (question 121), which is expensive. So **find fewer pages and find them
better**; a sloppy search followed by ten pages at full detail costs more and answers worse.

And insist it points at the **cell**, not the page. *"On page four"* is a hope. *"That row, that
column"* is something you can check.

## Judging it 🏅

* 🔀 **Score the finding and the answering separately.** When the whole thing is wrong you need to
  know which half failed, and one number cannot tell you.
* 🎯 **Ask the questions only a picture can answer.** *"Which Pokémon's hexagon is one enormous HP
  spike?"* — answerable only from the shape. *"What does **Thunderbolt** do to **Gyarados**?"* —
  answerable only from the grid. ⚠️ Average those in with ordinary questions and the scribe-based
  system looks perfectly respectable while being **completely unable** to answer a single one of
  them.
* 👉 **Check the pointing.** Right answer, wrong cell means it got lucky, and you will find out
  which the next time it does not.
* 💰 **And count the cost per question, honestly.** Keeping every page as a page is far dearer to
  store and to search. That trade *is* the choice you are making.
