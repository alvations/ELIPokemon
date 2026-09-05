---
id: "105"
slug: shared-multilingual-vocabulary
style: pokemon
category: multilingual
difficulty: intermediate
question: "How do you build a subword vocabulary shared across many languages?"
tags: [sentencepiece, vocabulary, byte-fallback, unigram-lm, character-coverage]
---

# Stocking the TM shelf for every region at once

The Celadon Department Store has a TM counter. It has shelves. The shelves have a size, and you
are stocking them for Trainers arriving from Kanto, Johto, Hoenn, Sinnoh, Unova, Kalos, Alola,
Galar and Paldea.

Stock badly and someone's Pokémon has to build its attack out of Tackle and Scratch, one
clumsy piece at a time.

## What earns a shelf slot 📦

**The moves everybody uses.** Protect. Rest. Substitute. Rock Slide. Nearly every species can
run them and nearly every Trainer wants them, so one slot serves everyone. Superb value.

**The moves one Pokémon uses.** Aeroblast is Lugia's and no one else's. Sacred Fire is Ho-Oh's.
Judgment belongs to Arceus. Each would take a whole slot to serve exactly one customer, so they
never make the shelf — and the Trainer who needs one has to improvise it out of parts.

```
   THE SHELF — fixed width
   ┌────────────────────────────────────────────────────────────┐
   │ ▓▓ the raw letters, so nothing is ever unreadable          │  can't cut this
   │ ▓▓▓▓▓▓▓ every character used in Alolan and Galarian names  │  can't cut this
   │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ actual useful bundled moves               │  ← the whole fight
   └────────────────────────────────────────────────────────────┘
```

The first two bands are not negotiable. **Everything Trainers argue about happens in the third.**

## The floor: nobody leaves empty-handed 🧱

Keep a rack of the plainest parts — the individual letters, so to speak — so that when a Trainer
walks in wanting something nobody stocked, they can still assemble it by hand.

It works. It is also miserable: four fumbling parts where a stocked TM would have been one
press. But the alternative is telling them the move does not exist, and that is worse. Assemble
slowly, always; refuse, never.

## Do not stock by footfall 👣

The tempting rule: stock in proportion to who walks through the door. Kanto Trainers are 80% of
your footfall, so 80% of the shelf goes to Kanto.

Do that and the four Paldean Trainers who arrive each week find **nothing** — every order they
give has to be spelled out of raw letters, every time, forever.

So stock **flatter than the footfall.** Give Paldea more slots than its share of visitors
deserves, because a slot is cheap and a Trainer spelling out every order is expensive. The
Department Store loses nothing it will miss; the Paldean Trainers get a working counter.

## The part that keeps it honest 🤝

Some slots serve several regions at once, and those are the bargains — a piece that shows up in
Hoenn *and* Sinnoh words is one slot doing two jobs, and that shared machinery is a large part
of why a Pokémon trained in one region can walk into another and function.

But every slot is still a slot. **A shelf given to Galarian compounds is a shelf not given to
Alolan ones.** Adding a region to the store is never free. Anyone who tells you it is has not
looked at the shelf.

## When you got it wrong, and how you find out 🔎

The store looks fine on average, because the average is Kanto. Three things to measure instead,
one region at a time:

* 🧮 **How many presses does an ordinary order take here?** One is healthy. Six is a region that
  never got stocked.
* 🔤 **How often is someone assembling from raw letters?** If a whole region lives on the floor
  rack, that region was never really stocked at all.
* 👻 **Is there a script the store cannot even display?** Braille on the Sealed Chamber wall,
  Unown in the Ruins of Alph — if the counter renders those as blanks, no Trainer from there
  can shop at all, and your averages will never show it.
