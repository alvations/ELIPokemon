---
id: "079"
slug: parallelism-strategies
style: pokemon
category: systems
difficulty: advanced
question: "Explain data, tensor, pipeline, and expert parallelism."
tags: [data-parallel, tensor-parallel, pipeline-parallel, 3d-parallelism, megatron]
---

# Four ways to split training across gyms

One gym isn't enough. You have Brock's, Misty's and Lt. Surge's. **How do you divide the work?**

Four answers, and serious operations use all four at once.

## 1️⃣ Same Pokémon, different opponents 📋

```
   🏟️ GYM A: [full team] vs Brock's challengers
   🏟️ GYM B: [full team] vs Misty's challengers
   🏟️ GYM C: [full team] vs Lt. Surge's challengers
              │
              └─► compare notes at the end of the day, average the lessons
```

Every gym has a **complete copy** of the team — its own Garchomp, its own Ferrothorn. They just face
different opponents and pool what they learned each evening.

✅ Dead simple. Scales beautifully.
❌ **Requires the whole team to fit in one gym.** The moment it doesn't, this is useless.

## 2️⃣ Split each Pokémon across gyms 🔪

```
   🏟️ GYM A: Garchomp's Attack and Speed
   🏟️ GYM B: Garchomp's Defence and Special Defence
              │
              └─► must talk CONSTANTLY — they're running the same Pokémon
```

Now no single gym holds a whole Garchomp. Gym A works out whether Earthquake connects, Gym B
whether it survives the Ice Beam coming back, and every single turn they have to reconcile.

✅ The only way when one Pokémon is too big for one gym.
❌ **They talk incessantly.** Put these gyms in different cities and you'll spend the whole season on
the phone.

📌 **Keep these gyms in the same building**, on the fastest connection you have.

## 3️⃣ Split the journey by stage 🛤️

```
   🏟️ BROCK ──► 🏟️ MISTY ──► 🏟️ SURGE ──► 🏟️ ERIKA ──► ... ──► 🏟️ GIOVANNI
                          hand the Pokémon over at each boundary
```

Each gym handles its **segment** of the journey and passes the Pokémon along.

✅ **Barely any talking** — one handover per boundary. Works across cities.
❌ **The waiting problem:**

```
   😴 NAÏVE — one Pokémon at a time
   GYM A ████░░░░░░░░
   GYM B ░░░░████░░░░      ░ = sitting around doing nothing
   GYM C ░░░░░░░░████         75% of your capacity, idle
   GYM D ░░░░░░░░░░░░████

   ✅ FIX — send Pokémon through in a steady stream
   GYM A ████████░░░░
   GYM B ░░████████░░      Everyone busy almost all the time.
   GYM C ░░░░████████
   GYM D ░░░░░░████████
```

Send them **one after another** rather than one at a time and the idle gaps mostly close.

## 4️⃣ Split the Gym Leader roster 🎫

Only applies if you're running a League of specialists — Blaine for Fire, Brock for Rock: **put each
Gym Leader in their own building**
and route each challenger to whichever two they need.

✅ The only way to house a really large League.
❌ Challengers spend all their time **travelling between buildings**, and if one Leader is
over-subscribed, everyone waits on them.

## How to combine them 🎯

The recipe every large operation uses:

```
   🏢 WITHIN one building (instant communication):
      → split each Pokémon across gyms   ← talks constantly, needs to be close

   🌆 ACROSS buildings (slower):
      → split the journey by stage       ← barely talks, distance is fine

   🌍 ACROSS the whole operation:
      → same team, different opponents   ← talks once a day
```

**📌 The governing principle: match how much each method needs to talk to how fast the connection
is.**

Put the chatty method on the slow link and your beautiful cluster will run at the speed of the
telephone. That's the classic way to build something that looks impressive and scales terribly.
