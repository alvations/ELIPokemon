---
id: "136"
slug: off-target-and-hallucinated-translation
style: pokemon
category: translation
difficulty: advanced
question: "Why do translation systems output the wrong language or invent content?"
tags: [off-target, hallucination, zero-shot, language-tags, detection, oscillatory]
---

# You asked for the Alolan Vulpix and it gave you the Kantonian one

Two failures that look like faults and are actually consequences. Both are rare when you average
them and unacceptable one at a time, which makes them a **counting** problem as much as a
modelling one.

## Failure one: the right species, the wrong region 🗺️

Ask for the **Alolan Vulpix** entry. What comes back is fluent, well-formed, plainly about a
Vulpix — and it is the **Kantonian** one. Fire, not Ice. Everything about it is confident and
everything about it is the wrong Vulpix.

This is off-target output, and it happens for four reasons:

* **🔀 Nobody ever taught this exact route.** You have Kanto↔Johto entries and Kanto↔Hoenn entries.
  Now ask for Johto↔Hoenn directly. It was never once shown that journey — so it does what it was
  actually trained to do, and quietly routes you through **Kanto**, which is the only place it has
  ever been (question 130).
* **🏷️ The instruction is one word against a flood.** "Make it Alolan" is a single note attached to
  a page of source material and a lifetime of habit. It is not a strong lever.
* **👨‍👩‍👧 The bigger relative pulls.** **Alolan Raichu** drifts toward the Kantonian one.
  **Galarian Ponyta** drifts toward the Kantonian one. Not because the machine is careless —
  because it has seen a hundred times more Kanto material, and Kanto is downhill from everywhere.
* **🗃️ The archive was mislabelled.** Pages filed under the wrong region during training
  (question 108) taught it that this label sometimes means that region. It learned that faithfully.

```
   the page (Alolan) ──► [ label: Alola ] ──► the machine ──► a Kantonian entry
                                ▲                                    ▲
                        one word of instruction          a mountain of Kanto material
                                                         pulling the other way
```

📌 **Catching this is trivial and almost nobody does it. Look at what came out and check which
region it is.** One check, on every single output, alarm on mismatch. It is the cheapest guard in
the whole pipeline.

Fixing it: **clean the archive's labels on both sides**, put the region marker on the way in *and*
the way out rather than only on the way in, get hold of some genuinely **direct** Johto↔Hoenn
material rather than everything routed through Kanto, and when the check fires — **ask again,
louder**, rather than shipping it.

## Failure two: a beautiful entry about nothing 👻

Well-formed text in the right region's language bearing little relation to what was in front of it.

It comes in **two shapes**, and one is much easier than the other:

* **🌫️ The detached kind.** A fluent, plausible entry — about a different Pokémon entirely. Hard.
* **🔁 The looping kind.** The same phrase over and over, like a Pokémon locked into **Outrage**,
  swinging again and again until it ends up confused. **Trivially easy to catch** — anything
  repeating itself that many times is not writing.

**What sets it off**, most common first:

* **💧 A damaged page.** Smudged, misspelled, half in the wrong alphabet. Nonsense in, *fluent*
  nonsense out.
* **🔖 A very short entry.** One word. A menu label. There was almost nothing to be faithful to.
* **🌏 A rare region.** Its grip on the source is weakest exactly there, so habit takes the wheel —
  the identical mechanism that gives Charmeleon its wings in question 122.
* **🗂️ A sloppy archive.** Pages paired with the wrong entries during training taught it, quite
  reasonably, that unrelated output is acceptable.

**How to catch it:**

* 🏥 **Nurse Joy** (question 132). This is precisely what she is for.
* 👀 **Check whether it ever looked at the page.** A Pokédex that is inventing barely glances at
  the source — you can measure that directly, and it is a strong tell.
* 🔁 **A repetition check**, for the looping kind. Five lines of code.
* ↩️ **Translate it back and see if you get the page you started with.** Rough, noisy, and it
  catches the badly detached ones.
* ⚠️ **And do not ask it how sure it is.** It is *very* sure. That is the whole problem — the
  invented entry is fluent, and fluent reads as confident. Same trap as question 122.

**Fixing it:** clean the archive first (mislabelled and misaligned pages are the biggest single
lever, and the dullest), **do not search too hard** for the perfect wording — casting a very wide
net makes this worse, not better — cap repetition while it writes, and when Nurse Joy flags one,
**hand it to another Trainer instead of publishing it.**

## Why the season average will never warn you 📉

Both of these are rare. A Pokédex that invents an entry **once in every two hundred** loses a
fraction of a point on any overall score, and is completely unusable anywhere a Trainer will act on
what it says.

📌 So **count them, as counts, with their own targets** — exactly like the dropped negations in
question 132. Never as part of a mean. A mean is precisely the instrument that hides them.
