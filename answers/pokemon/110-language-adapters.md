---
id: "110"
slug: language-adapters
style: pokemon
category: multilingual
difficulty: advanced
question: "What are language adapters, and when do you prefer them to one big multilingual model?"
tags: [adapters, mad-x, modularity, peft, lora]
---

# Silvally's Memory discs: one body, a disc for every region

Silvally is a Normal-type with an ability called RKS System. Slot in a Water Memory and it
becomes Water. Slot in a Fire Memory and it becomes Fire. Its Multi-Attack changes type to
match. Same Silvally, same stats, same everything — **one small removable part** decides what
it is today.

That is the whole idea. Freeze the enormous, expensive Pokémon. Swap a disc per region.

## The three parts 🧩

```
              ┌────────────────────────────────────────────┐
   battle ───►│  🧊 SILVALLY — frozen, never retrained      │
              │     ├─ 💿 region disc  ← one per region     │
              │     └─ 🎯 job disc     ← one per job        │
              └────────────────────────────────────────────┘

   drilled with:  [ Kanto disc ] + [ Gym-battling disc ]
   deployed with: [ Alola disc ] + [ Gym-battling disc ]
                       ▲
             swap ONE disc. Nothing is retrained. Nothing is forgotten.
```

The Gym-battling disc has never been to Alola. The Alola disc has never battled a Gym. Put them
in together and Silvally handles Alolan Gyms anyway, because one disc knows *where* and the
other knows *what*.

This is not exotic. Arceus does it with **Plates** — Judgment becomes whatever Plate it holds.
Genesect does it with **Drives** and Techno Blast. Ogerpon swaps **masks**: Wellspring makes it
Water, Hearthflame Fire, Cornerstone Rock, and Ivy Cudgel changes with the mask. Rotom does it
with household appliances, and the Wash form gets Hydro Pump while the Mow form gets Leaf Storm.

One body. A shelf of small parts. Nobody rebuilds the body.

## Why this beats one enormous everything-Pokémon 💪

* ➕ **Adding Paldea does not disturb Kanto.** Cut a new disc, put it on the shelf, done. Nothing
  that already worked has been touched, so nothing that already worked can break.
* 🧠 **It fixes the crowding.** Garchomp's four slots have to cover the world at once; Silvally's
  shelf is as long as you like, and only one disc is in the machine at a time.
* 🪶 **Discs are tiny.** A disc costs almost nothing next to a Pokémon. You can carry a hundred.
* 🧱 **They stack in both directions.** A region disc, a job disc, a formal-language disc — cut
  each one once, combine them however the battle demands.

## Why you might not 😬

**🤝 Silvally with the Alola disc in has stopped being Kantonian.** The big all-regions Pokémon
could half-remember something from Johto while fighting in Alola. Silvally cannot: the disc it
is holding is the only disc it is holding, and the neighbouring region's knowledge is on a
shelf across the room.

**🚦 Somebody has to pick the disc — before the battle.** You need to know which region this is
*first*. Get it wrong and you have sent in a Fire Silvally against Blaine. And when a Trainer
gives orders half in one region's words and half in another (question 107), **there is no
correct disc to slot in.** The whole design assumes the question has one answer.

**🎒 The disc occupies the item slot.** Silvally holds a Memory, so Silvally is not holding a
Choice Scarf. Real mechanic, real cost: modularity is not free, and stacking parts eventually
runs into a slot that was already spoken for.

**📦 Ninety-nine discs is ninety-nine things to keep straight.** One Pokémon that just handles
every region is genuinely simpler to send into a fight, and a fully rebuilt, region-specific
Pokémon still edges out disc-Silvally when you can afford to raise one.

📌 Choose discs when languages are many, cheap to add, and served one at a time. Choose the one
big Pokémon when the regions bleed into each other and you cannot say in advance which one you
are standing in.
