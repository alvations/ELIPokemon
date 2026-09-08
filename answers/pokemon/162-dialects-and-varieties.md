---
id: "162"
slug: dialects-and-varieties
style: pokemon
category: translation
difficulty: advanced
question: "Why do language technologies fail on dialects and non-standard varieties?"
tags: [dialects, varieties, standard-language, normalisation, identification, fairness]
---

# An Alolan Vulpix is not a broken Kantonian one

Point a Pokédex built in Kanto at an **Alolan Vulpix** and watch what it does.

It has an entry for Vulpix. Vulpix is Fire. This one is **Ice**. It is the wrong colour, the wrong
type, and it does not match the reference at all — so the Pokédex records a **malformed Vulpix**.
A bad reading. Something to be filtered out and ignored.

📌 That is the whole failure, and it is not a small one. **Alolan Vulpix is not a defective
Kantonian Vulpix.** It is a Vulpix, from Alola, and it is exactly as correct as the other one. The
Pokédex is not detecting an error. **It is announcing where it was built.**

## Four things people flatten into one word 🗂️

* **🧊 Genuinely different, sharing a name.** **Alolan Raichu** is Electric *and* Psychic. **Galarian
  Ponyta** is Psychic where Kanto's is Fire. **Galarian Corsola** is a Ghost. Whether these count as
  "the same Pokémon" is a decision somebody made, not a fact you can read off.
* **🌏 Mutually recognisable, differing everywhere.** Two regions that plainly share a Pokémon and
  disagree constantly about the details — the differences that make a translation read as foreign
  (question 150).
* **🐾 Individual variation within a region.** Not a regional form at all, and treated as one by
  anything trained on a single reference.
* **⚔️ And a different setting entirely.** A Pokémon in a **Contest** behaves nothing like the same
  Pokémon in a Gym. Not a variety — and it fails the same way, for the same reason: **it is not
  what the Pokédex was shown.**

## Everything downstream inherits it 🔗

```
   built on:     the Kanto reference
   pointed at:   everything else

   the chopper  ─► unfamiliar spellings shatter into fragments (question 102)
   the sorter   ─► "this is not really Vulpix" — and the sighting is DISCARDED
   translating  ─► quietly "corrects" it to Kantonian first, then translates that
   listening    ─► several times the error rate of the headline figure (question 125)
   the filter   ─► flags the unfamiliar form as low quality, or as a mistake
```

⚠️ And look at the second and last lines together, because they form a **loop**. The sorter was
built on the Kanto reference, so it throws Alolan sightings out of the archive. So the next Pokédex
sees even fewer of them. So it is even worse at Alola. So even more get thrown out.

📌 **The loop is self-feeding and completely invisible** unless somebody deliberately goes and looks
at what the filter removed.

## "Correcting" it is a choice, not a neutral act 🩹

The tempting fix is to turn the Alolan Vulpix into a Kantonian one and work from that. Sometimes
that is right — for a filing index, or when the Trainer genuinely wants the standard entry.

⚠️ But be honest about the price. **The form carries information.** Which region raised it, what it
is resistant to, what it can actually do. Normalise first and you have produced a careful,
fluent translation of **a Pokémon that was not there.**

And a Pokédex that displays the Alolan form as *"corrected"* has quietly announced which region's
Vulpix counts as the real one.

Handling the form directly is harder — fewer sightings, no settled spelling, and Trainers
themselves disagree — and it is the right default for anything that claims to represent the
Pokémon in front of it rather than merely file it.

## What to actually do 🔧

* 📊 **Break every score down by region. Always.** ⚠️ One pooled number hides a threefold gap, and
  **reporting only the pooled number is precisely how the gap survives** from one release to the
  next.
* 🗑️ **Look at what your filter threw away** before trusting the archive it produced.
* 🤝 **Gather sightings *with* the region's Trainers, not *about* them** (question 164) — and pay
  them.
* 🔤 **Accept that the spelling varies** rather than picking one and calling the rest typos.
* 🗺️ **And say which region you actually support.** *"Vulpix"* is not a claim (question 150).
  Admitting you only handle Kanto is far better than implying you handle Alola and quietly turning
  every Ice-type into a Fire-type on the way through.
