---
id: "113"
slug: morphology-rich-languages
style: pokemon
category: multilingual
difficulty: intermediate
question: "How does rich morphology challenge subword models?"
tags: [morphology, agglutination, sigmorphon, segmentation, inflection]
---

# Alcremie has sixty-three forms and your Pokédex has one page

Nine creams. Seven sweets. Every combination is a real, distinct Alcremie you can actually have.

A Pokédex that tries to memorise all sixty-three as separate creatures is doing it wrong, and
will still be wrong the moment somebody spins up a combination it has not filed. The only way
to handle Alcremie is to stop memorising and start **reading it in parts**: *this is the
strawberry sweet, on the matcha cream.* Two facts, sixty-three answers.

Some languages are Alcremie. English is mostly Magikarp — one form, take it or leave it.

## The three flavours of this problem 🍓

* 🧁 **Everything stacks cleanly.** Alcremie, Vivillon with its patterns, Furfrou with its
  trims: parts go on in order, each part means one thing, and you can read them off. Turkish and
  Finnish and Swahili words are built this way.
* 🌀 **The parts fuse into the body.** Wormadam does not wear a cloak — the cloak *becomes* what
  it is. Plant Cloak comes out Bug/Grass, Sandy Cloak Bug/Ground, Trash Cloak Bug/Steel, and
  there is no seam left to point at. Russian and Arabic do this to words.
* 🐘 **One form is an entire sentence.** A single word that means what a whole battle report
  means. Rare, real, and completely outside anything a fixed list can hold.

## What breaks 💥

```
  1. 📚 THE LIST CANNOT HOLD IT
     Sixty-three Alcremie, twenty Vivillon, ten Furfrou trims, four
     Deerling seasons. Any fixed Pokédex covers a sliver.

  2. ✂️ IT CUTS IN THE WRONG PLACES
     Split by what is COMMON, not by what MEANS something:
        [matcha-cream-straw][berry]   ← common, and meaningless
        [matcha cream][strawberry]    ← what it actually is
     Now the Pokédex has to work out from scratch that the second
     shard was ever a sweet.

  3. 🕳️ RARE COMBINATIONS ARE STRANGERS
     Everyone knows the ruby cream. Almost nobody has the ruby swirl
     with the berry sweet — so the Pokédex treats a familiar cream in
     an unfamiliar arrangement as a species it has never met.

  4. 🎨 MAKING ONE IS HARDER THAN NAMING ONE
     Shown an Alcremie, saying roughly what it is: easy.
     Asked to PRODUCE the salted-cream-with-clover-sweet exactly:
     you must get every part right at once, and one wrong part
     means a Pokémon that does not exist.
```

📌 Point four is the one worth remembering. **Describing Alolan forms is much easier than
producing them correctly.** Going *into* a language like this is far harder than coming out of
it, and that asymmetry is invisible if you only ever test one direction.

## What actually helps 🛠️

* 📦 **Stock the shelf properly for these regions.** If your counter has slots for "matcha
  cream" and "strawberry sweet" as pieces, sixty-three Alcremie cost you sixteen slots instead
  of sixty-three. Cheapest real fix there is.
* ✂️ **Cut at the seams, not at the frequencies.** Where does the cream end and the sweet begin?
  Splitting there costs nothing and teaches the Pokédex that parts are parts.
* 🎲 **Deliberately cut it differently every time you drill.** Show the same Alcremie sliced
  three ways on three different days. The Pokédex stops depending on one arbitrary cut and
  starts noticing the pieces themselves — and this helps most exactly where you have the least
  material.
* 🔤 **Or refuse to cut at all** and read it letter by letter, which is slow and never gets the
  seam wrong.
* 📏 **Score it by how much is right, not whether it is exactly right.** A near-miss Alcremie —
  right cream, wrong sweet — is not the same failure as handing over a Magikarp. Any scoring
  that calls both of them simply "wrong" will tell you nothing useful about a region like this.
