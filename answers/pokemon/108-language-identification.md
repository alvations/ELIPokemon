---
id: "108"
slug: language-identification
style: pokemon
category: multilingual
difficulty: core
question: "How does language identification work, and where does it fail?"
tags: [lid, fasttext, corpus-quality, precision, glotlid]
---

# The Pokédex says "Pikachu" and it is not a Pikachu

Point the Pokédex at something and it names the species. Point it at a healthy Charizard in
good light and it is right essentially every time.

Every word in that sentence is load-bearing: **healthy**, **good light**, **Charizard** — a
species the Pokédex has seen ten thousand times.

## Four things that fool it 🔍

**1. 👂 One syllable of a cry.** A full battle gives the Pokédex plenty to work with. A single
short cry from behind a rock gives it almost nothing — and out in the tall grass, almost
everything you hear is a single short cry from behind a rock.

**2. 👯 Nidoran and Nidoran.** The male and the female are genuinely different species with
genuinely different evolutions, and they are small, purple and blue and the same shape. Plusle
and Minun. Volbeat and Illumise. Sneasel from Sinnoh and Sneasel from Hisui. Sometimes the
creature in front of you simply does not show the feature that separates them.

**3. 🎭 Deliberate impostors.** This is where it gets bad.

* **Mimikyu** is wearing a rag drawn to look like Pikachu. The Pokédex says Pikachu.
* **Ditto** has Transformed into the thing across from it and is reading as that thing.
* **Zoroark**'s Illusion makes it appear as the last Pokémon in your party until something
  actually connects with it.
* In the Power Plant, half the **Poké Balls** on the floor are Voltorb.
* And in Pokémon Tower there is a Ghost the Pokédex cannot read **at all** until you are
  holding the Silph Scope — one specific tool, or no identification, ever.

**4. 🐀 Rattata swallows the archive.** The subtle one, and the worst.

The Pokédex is uncertain, so it guesses the common answer. Rattata is everywhere, so Rattata is
the guess. Individually this is a rounding error — a fraction of a percent of Rattata sightings
land in the wrong drawer.

But the drawer they land in might be **Larvitar**, which has eleven real sightings in the whole
region. Now the Larvitar drawer is nine parts Rattata.

```
   THE LARVITAR DRAWER, AFTER THE POKÉDEX HAS FILLED IT
   ┌───────────────────────────────────────────────────┐
   │ 🐀 Rattata mislabelled as Larvitar   ████████████ │
   │ 🦎 actual Larvitar                   ██           │
   └───────────────────────────────────────────────────┘
   Nobody notices. Everyone who could check reads
   "Larvitar: 130 sightings" and is delighted.
```

Somebody later trains a team on that drawer, and cannot work out why it has learned to fight
like a Rattata.

## How to run a Pokédex you can trust 🛡️

* 🎨 **Ask the easy question first.** *Is it red or blue?* before *which species?* Colour is
  almost never wrong, and it eliminates most of the answer space for free.
* 🤐 **Let it say "unknown".** A Pokédex that answers every time is worse than one that shrugs.
  Set a confidence bar; below it, the entry goes into a drawer marked **?** and stays there.
* 🎯 **Guard the rare drawers, not the average.** Better to lose ten real Larvitar than to admit
  a hundred Rattata. You can go and find more Larvitar. You cannot un-poison the drawer.
* 📊 **Score it per species, not overall.** "97% accurate" means "97% good at Rattata and
  Pidgey", which you knew. The number you need is the score on Larvitar, on Absol, on Unown.
* 🤷 **Some things are two answers, and that is fine.** A Greninja mid-Protean has a genuine
  claim to two types at once. Do not force a stamp.
* 👀 **Send a Trainer who has actually been there.** Take a hundred entries out of the drawer
  and put them in front of somebody who has stood in that region. Every failure above was found
  that way, and none of them was found by looking at the accuracy number.
