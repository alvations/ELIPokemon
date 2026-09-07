---
id: "157"
slug: video-generation
style: pokemon
category: multimodal
difficulty: advanced
question: "How does video generation differ from image generation?"
tags: [video-generation, temporal-consistency, spacetime-patches, fvd, object-permanence]
---

# A Charizard that turns into a Charmeleon halfway through the attack

Generating a still Pokémon is question 137. Generating a **battle** is that, plus a dimension that
does not behave like the other two.

Width and height are interchangeable. **Time is not.** It runs one way, and every Trainer watching
has fierce, unspoken expectations about what is allowed to change along it.

## Slice it through time as well as space 🧊

```
   the battle   many turns × the field
        │
        ├─ squash it into the Ball (question 137) — and squash the TIME too,
        │     several instants folded into one. This is the only reason it is affordable.
        │
        ├─ cut it into tiles that cover a patch of field ACROSS a few instants
        │
        └─ un-scatter all of them together, watching each other
                    │
              a tile early on can see a tile forty turns later — and that
              mutual watching is the entire reason the Charizard stays a Charizard
```

Earlier attempts drew each instant separately and then tried to smooth them together. Cutting
through space **and** time at once beats that — and it costs dearly, because every tile must
consider every other tile. That is why generated battles are **short**.

## Why long battles fall apart 📉

Past a few turns you cannot hold the whole match in mind at once, so you generate a stretch, then
generate the next stretch from the end of the last.

⚠️ Which is autoregression, with autoregression's disease: **the mistakes compound.** The colours
creep. The Charizard's flame changes shade, then size, then the Charizard is subtly a different
Charizard. Anchoring each stretch to a fixed reference frame helps. It does not cure it.

## Every instant can be perfect and the battle still wrong 🚨

* **🚪 Things stop existing.** A **Diglett** goes underground with **Dig** and something else comes
  up. Nothing in the training ever *required* that a Pokémon be the same Pokémon when it reappears.
* **🦎 Identity slides.** A **Charizard** drifts into a **Charmeleon** over forty turns and no
  single frame is where it happened. ⚠️ And note how badly wrong that is: Pokémon **do** change form
  mid-battle — **Mega Evolution**, **Terastallization** — but always visibly, always by a named
  mechanic, always once. Quietly becoming your own pre-evolution is not a thing that happens.
* **🖐️ Parts appear and vanish.** **Machamp** with three arms in one instant and five in the next.
  A **Poké Ball** that empties and refills.
* **💧 The world does not behave.** **Surf** that falls upward, a **Sandstorm** that ignores the
  rocks. 📌 These machines learned **what battles look like**, not **how battles work**, and claims
  that they have learned physics should be read with that firmly in mind.
* **🔤 And lettering**, worse than in a still, because now it has to hold still as well.

## Words alone are a poor set of reins 🎛️

Anything usable comes from **constraining** it, not from describing it:

* 🖼️ **Give it the first frame.** Now the field, the weather and *which* Charizard are all fixed
  before it starts. This is the single most useful control there is.
* 🏁 **Give it the last frame too**, when you need it to arrive somewhere specific.
* 🎥 **Tell it where the camera goes.**
* 🦴 **Give it the poses**, and let it fill in the appearance.

## Judging it 🏅

There is a standard measure that compares a heap of generated battles against a heap of real ones.
It inherits every complaint from question 137 — **and one worse**: it is barely sensitive to
exactly the failures above. ⚠️ **A clip in which the Charizard becomes a Charmeleon can score
perfectly well.**

So probe for the specific things instead. They are cheap to build and worth more than any single
number:

* 🚪 **Send something behind a rock and see what comes out.**
* 🔢 **Count the Zubat in the first frame and in the last.**
* 🦎 **Check the Charizard is still the same Charizard at the end.**
* 👀 **And ask Trainers which they prefer** — rating *"is it the battle I asked for"*, *"does it
  look good"*, and *"does it hold together"* as **three separate questions**, because a clip can be
  excellent at two of them and unwatchable on the third.
