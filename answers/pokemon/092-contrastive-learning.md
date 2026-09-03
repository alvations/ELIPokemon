---
id: "092"
slug: contrastive-learning
style: pokemon
category: training
difficulty: intermediate
question: "What is contrastive learning? Explain InfoNCE and CLIP."
tags: [contrastive, infonce, clip, simclr, negatives, collapse]
---

# Contrastive learning: same Pokémon, or different?

You want a Trainer who recognises Pokémon — but you have **no labels.** Nobody wrote "this is a
Pikachu" on anything.

You do have one free fact: **two photos of the same Pokémon show the same Pokémon.**

That's enough.

```
   📸 Pikachu, from the front     ─┐
                                   ├─► ✅ PULL TOGETHER (same creature)
   📸 Pikachu, from the side      ─┘

   📸 Pikachu                     ─┐
                                   ├─► ❌ PUSH APART (different creatures)
   📸 Gyarados                    ─┘
```

Do this millions of times and your Trainer builds a map where **each species has its own
neighbourhood** — without anyone ever naming a single one.

## The three things that decide whether it works 🎛️

**1. 🤝 What counts as "the same"?** This is the whole design. Two photos of one Pokémon? A Pokémon and
its Pokédex description? A question and the answer to it? Whatever you declare "the same" is what the
Trainer learns to treat as equivalent.

**2. 🔥 What do you push against?**

The single biggest quality lever, and the most neglected.

```
   😴 EASY:  Pikachu vs Gyarados
      → "obviously different." Learned nothing. It was never in doubt.

   🔥 HARD:  Pikachu vs RAICHU
      → NOW it has to learn the difference. This is where the work happens.
```

📌 Push against **easy** contrasts and you get a Trainer who can tell an electric mouse from a sea
serpent. Push against **hard** ones and you get a Trainer who can tell Pikachu from Raichu. Finding
those near-misses is most of the job.

And you want to push against **many at once** — comparing your Pikachu against one alternative
teaches less than comparing it against a thousand. This is why these setups run enormous batches.

**3. 🌡️ How harshly you push.** Too gentle and nothing separates. Too harsh and the Trainer fixates
on the single hardest pair and falls apart. Genuinely fiddly, not a formality.

## The trap: the shortcut 🕳️

Here's what nearly killed this whole approach.

You show two photos of Pikachu and one of Gyarados. Your Trainer solves it **instantly and
perfectly**, and has learned **nothing.**

Because the two Pikachu photos are both **yellow.** It's matching colours. It has no idea what a
Pokémon is.

**The fix: deliberately break the shortcut.** Tint one photo blue. Now colour is useless, and the
Trainer is forced to learn about **shape, posture, ears, tail** — the things you actually wanted.

📌 **The core design question in all of this: what's the laziest way to pass this test, and how do I
block it?**

## 🖼️ Photos and descriptions together

The famous version pushes this further. Instead of two photos of the same Pokémon, pair **a photo**
with **its Pokédex description.**

```
                    descriptions →
              "electric  "water     "rock    "psychic
               mouse"     serpent"   snake"   fox"
            ┌─────────┬─────────┬─────────┬─────────┐
   📸 ⚡    │   ✅    │    ✗    │    ✗    │    ✗    │
   📸 🌊    │    ✗    │   ✅    │    ✗    │    ✗    │   match the diagonal,
   📸 🪨    │    ✗    │    ✗    │   ✅    │    ✗    │   push everything else
   📸 🔮    │    ✗    │    ✗    │    ✗    │   ✅    │
            └─────────┴─────────┴─────────┴─────────┘
```

Now **pictures and words live on the same map.** And something remarkable falls out.

You can identify a Pokémon **you have never trained on**, by name:

> Write down *"a photo of a Flareon."* Place those words on the map. Look at what photo is nearest.
> **That's your Flareon** — and nobody ever showed the Trainer a labelled Flareon.

You didn't train a Flareon detector. You trained a shared map, and then **asked in words.**

## The collapse problem 💥

There's a cheat available, and it's the reason you need contrasts at all.

**Put every single Pokémon in exactly the same spot on the map.**

Now every "are these the same?" question is trivially yes. Perfect score. **Completely useless map.**

Pushing different things apart is what prevents this. Which made it a genuine surprise when people
found ways to **drop the pushing entirely** and still avoid collapse — using a deliberately
lopsided setup where one side updates slowly and the other chases it. Nobody quite expected that to
work.
