---
id: "165"
slug: vlm-inference-efficiency
style: pokemon
category: multimodal
difficulty: advanced
question: "What makes vision-language model inference expensive, and how do you fix it?"
tags: [inference, prefill, kv-cache, token-pruning, prefix-caching, batching]
---

# The Pokédex is slow because it is holding four thousand tiles

A talking Pokédex costs what any talking machine costs (questions 032, 033). A **looking** one does
not, and the difference catches people out completely.

The Trainer's question is four words. The picture of the **Ruins of Alph** wall is **four thousand
tiles**. And the answer is *"Aerodactyl"* — one word back.

```
   A TALKING POKÉDEX                 A LOOKING POKÉDEX
   ─────────────────                 ─────────────────
   taking it in:  quick              taking it in:  ENORMOUS — thousands of tiles
   speaking:      long               speaking:      usually one short answer

   so a talking one is limited by how fast it can speak.
   a looking one is limited by how long it takes to LOOK, and that is
   a completely different bottleneck with completely different fixes.
```

## Three separate bills, constantly muddled 🧾

1. **👁️ The eye itself.** Every tile considering every other tile, once per picture.
2. **🧠 Then the *voice* has to read all four thousand tiles too.** ⚠️ This is usually the real
   cost, and note whose size it scales with: **the voice's, not the eye's.**
3. **🗄️ And it must hold all four thousand in mind** for the whole answer. So a looking Pokédex
   serves **far fewer Trainers at once** than a talking one of the same size — not because it is
   slower per Trainer, but because each one takes up so much room.

## What actually helps, best first 🔧

* **🔁 If it is the same picture, do not look again.** A Trainer asking six questions about **one**
  **Celadon Department Store** directory. An agent staring at the same screen turn after turn
  (question 145). **Keep what the first look produced and reuse it.** 📌 This is the biggest win in
  real use, and it is routinely not built because everyone assumes the picture changes every time.
  **Go and measure how often it actually does.**
* **🧩 Fold the tiles down before the voice sees them.** The two-by-two fusing from question 121 is
  a free quarter. Throwing away near-identical tiles cuts more — ⚠️ and remember it is **ruinous on
  a page of small print**.
* **🔭 Do not walk close unless you need to.** *"Is that a **Snorlax**?"* never needed the fine
  print; *"what does this **TM** cost at the **Poké Mart**?"* always does. Take a cheap look first
  and only walk up when the answer depends on it. This is **Nurse Joy**'s triage from question 132,
  pointed at effort instead of quality.
* **📦 Shrink the eye.** It is a small part of the whole and frequently left at full size out of
  pure habit. Check.
* **⚖️ Queue similar pictures together.** One Trainer holding up a **Pidgey** and another holding
  up a nine-panel **Celadon Department Store** directory in the same batch means everybody waits for
  the directory.

## What helps less than people hope 🤷

* **⚡ Making it *speak* faster** (question 034). Your Pokédex says *"Aerodactyl"* and stops. It was
  never the speaking. **Quick Attack** does not help a Pokémon that was never slow to move.
* **🐣 Swapping in a smaller voice.** The eye still costs the same and the four thousand tiles are
  still four thousand tiles. You save real money and **much less than the size difference suggests.**
* **🛠️ A faster way of doing the looking.** Genuinely helps — and it does not change the fact that
  **four times the tiles is sixteen times the work**, which is what made it expensive to begin with.

## Measuring it honestly 📊

* ⏱️ **Time until the first word**, and **how fast it talks after that** — as **two numbers**, never
  one.
* 🔍 **And always say at what distance.** A Pokédex timed on one small snapshot tells you **nothing**
  about what it does with a nine-panel Ruins of Alph wall. Report the curve, not a point.
* 👥 **And how many Trainers it serves at once** at an acceptable wait. 📌 That is what decides the
  cost per question, and it is governed by **how much each one takes up in memory** — not by how
  fast the machine can think.
