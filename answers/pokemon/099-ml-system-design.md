---
id: "099"
slug: ml-system-design
style: pokemon
category: system-design
difficulty: advanced
question: "Walk me through designing a recommendation system end to end."
tags: [system-design, recommender, retrieval-ranking, two-tower, cold-start]
---

# Designing "which Pokémon should this Trainer catch next?"

A hundred million Pokémon in the world. Ten million Trainers. **Recommend six.** In under a tenth of
a second.

## Step 1: ask what you're actually optimising 🎯

Do **not** start building. Start here — this is what's really being tested.

> **"Recommend the best Pokémon"** — best for *what*?

* 🏆 Winning their next battle?
* 📈 Long-term team growth?
* 😊 Enjoying the game?
* 💰 Spending money on Poké Balls?

**These give completely different answers.** A system tuned for "wins the next battle" recommends the
same six overpowered Pokémon to everyone, forever. Great numbers. And every Trainer's team is
identical, nobody's having fun, and half of them quit by spring.

Then ask: **how many** Pokémon and Trainers? **How fast** must it answer? **What do you know** about
brand-new Trainers?

## Step 2: the funnel 🔻

You cannot carefully evaluate a hundred million Pokémon in a tenth of a second. So **narrow in
stages, spending more effort as the pile shrinks.**

```
   🌍 100,000,000 Pokémon
          │
   ┌──────▼─────────────────────────────────┐  1️⃣ ROUGH SWEEP   ~10ms
   │  Several quick sources at once:        │     Goal: DON'T MISS ANYTHING
   │   🗺️ similar to what they already like │     Cheap per Pokémon.
   │   👥 what similar Trainers caught      │
   │   🔥 what's popular right now          │
   │   👀 what they recently looked at      │
   └──────┬─────────────────────────────────┘
        ~1,000 candidates
   ┌──────▼─────────────────────────────────┐  2️⃣ CAREFUL RANKING  ~50ms
   │  The heavy model. Considers their      │     Goal: GET THE ORDER RIGHT
   │  whole team, gaps, history, playstyle. │     Expensive per Pokémon —
   │  Predicts several things at once:      │     affordable on 1,000.
   │  will they catch it? use it? enjoy it? │
   └──────┬─────────────────────────────────┘
        ~100 ranked
   ┌──────▼─────────────────────────────────┐  3️⃣ FINAL POLISH     ~5ms
   │  🎨 not all six the same type          │
   │  🚫 nothing they already own           │
   │  ⚖️ region availability, event rules    │
   └──────┬─────────────────────────────────┘
        ✅ 6 shown
```

📌 **Rough sweep: never miss the right one.** Careful ranking: **get the order right.** Two different
jobs — trying to do both in one stage is why single-stage systems disappoint.

## Step 3: how the rough sweep works 🗺️

Put every Pokémon on a map. Put every **Trainer** on the *same* map, near the Pokémon they'd like.

Then recommending is just: **who's standing near this Trainer?** Instant, even with a hundred million
of them.

⚠️ The limitation, and it's the reason stage 2 exists: **the Trainer's position and the Pokémon's
position are worked out separately, before they ever meet.** So the map can't notice *"this Trainer
already has three Fire types, so a fourth is redundant."* That requires looking at both together —
which is exactly what the careful ranking stage does.

## Step 4: training it 🏋️

**⚖️ Where do the negative examples come from? ← the crucial design choice**

You know what Trainers **caught**. You need examples of what they **wouldn't** catch.

* 🎲 **Random Pokémon** → too easy. "You didn't want a random Magikarp" teaches nothing.
* 👀 **Shown but not caught** → far more informative. They *saw* it and passed.
* ⚠️ But that's biased: it only contains things your **current** system chose to show.

**📍 Correct for position.** The Pokémon shown **first** gets caught most — because it was first, not
because it was best. Fail to correct for this and you'll learn that position one is magic.

**🎭 Predict several things at once.** Will they catch it? *Use* it? Still be using it next month?

Optimise only "will they catch it" and you'll recommend flashy legendaries nobody actually plays.

## Step 5: brand new things ❄️

**🆕 A new Pokémon** nobody has caught yet has no history at all. Use what you *can* see — its type,
its stats, what it looks like — until real data arrives.

**🆕 A new Trainer** gets popular starters, plus whatever you can learn in their first five minutes.

**🎲 And deliberately show things you're unsure about.**

Recommend **only** what you're confident about, and you never learn anything new — the only Pokémon
that get caught are ones you already recommended, so tomorrow's training data confirms today's
beliefs.

📌 **Spend a small budget on genuine exploration**, or your system slowly narrows to a handful of
Pokémon and forgets the rest of the world exists.
