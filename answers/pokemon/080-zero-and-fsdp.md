---
id: "080"
slug: zero-and-fsdp
style: pokemon
category: systems
difficulty: advanced
question: "What is ZeRO/FSDP sharding and what are the stages?"
tags: [zero, fsdp, sharding, deepspeed, memory-optimisation]
---

# ZeRO: stop making every gym keep a full copy of everything

Eight gyms — Brock's through Giovanni's — all training the same team on different opponents. Every
gym holds:

* 📋 Garchomp's six stats, Ferrothorn's six, and so on
* 📝 This week's feedback
* 📚 **The complete training history** — every trend notebook, every noise estimate, going back to day
  one

Eight identical copies of everything. And here's the kicker:

> **The training history is FOUR TIMES bigger than the team stats.**

You'd think a big team is mostly, well, the team. It isn't. It's mostly **paperwork about** the team.

```
   For every 1 unit of actual Pokémon stats:
   📋 stats (working copy)     ▓▓
   📝 this week's feedback     ▓▓
   📓 official stat records    ▓▓▓▓
   📈 trend notebooks          ▓▓▓▓
   📊 noise estimates          ▓▓▓▓
                               ─────
                               8× the size of the stats themselves
```

## The idea 💡

**Nobody needs a full copy. Split the paperwork and pass around only what's needed, right now.**

## Level 1: split the history 📚

Brock's Gym keeps the history for Garchomp and Ferrothorn. Misty's keeps Toxapex and Rotom. And
so on.

At the end of the week each gym updates **only its own** Pokémon and tells the others the results.

```
   Before:  every gym holds ALL the history
   After:   every gym holds an EIGHTH
```

✅ **Four times less storage. And exactly the same amount of talking as before.**

📌 This is **free**. There is no downside. If you are running more than one gym and haven't done
this, do it now.

## Level 2: also split this week's feedback 📝

Same logic. Each gym only keeps the feedback for its own Pokémon.

✅ **Eight times less storage**, still barely any extra communication.

## Level 3: split the stats themselves 🔪

The aggressive one. Now **no gym holds the whole team.** Gym A physically only has Pokémon 1–2.

So how does anyone train?

```
   🥊 About to train Garchomp:
      1. 📞 "Whoever has Garchomp's stats, send them over."
      2. ⚡ Train Garchomp.
      3. 🗑️ THROW THE COPY AWAY IMMEDIATELY.
      4. ➡️ Next Pokémon — Ferrothorn. Repeat.
```

At any moment each gym holds **one Pokémon's worth** of stats instead of the whole team.

✅ **Storage drops linearly with the number of gyms.** More gyms, less each. This is what lets you
train a team that could never fit anywhere.

❌ **Constant phone calls.** Every Pokémon, every step, a request goes out.

**But — the clever part:** while training Garchomp, **phone ahead for Ferrothorn's stats.** They
arrive while you're still busy. Do this well and most of the waiting disappears — the cost drops from
"crippling" to "10–20% slower."

## Two different problems 🧩

People confuse this with splitting a Pokémon across gyms. They're different:

* 🔪 **Splitting a Pokémon** divides the **work** — two gyms both work on Garchomp simultaneously
  and reconcile every turn. Chatty. Keep them in one building.
* 📚 **This** divides the **storage** — one gym does the work, having borrowed what it needs. Just
  fetching and returning. Tolerates slower links fine.

**Use both.** Split Pokémon within a building; split storage across buildings.

## The last resort 🏚️

Still doesn't fit? **Move the paperwork to a warehouse across town.** It's there when you need it,
and every retrieval is a slow trip.

Genuinely painful. And it turns *"this is impossible"* into *"this is slow"*, which is sometimes
exactly the trade you want.

## Practical notes 📌

* 🎁 **Turn on level 1 immediately.** Free storage savings, zero cost. There is no argument.
* 📦 **Split at sensible boundaries** — one Gym's worth at a time, Brock's records with Brock's. Too fine and you're on the phone
  constantly; too coarse and you're back to storing everything.
* 🤝 **Combine it with filming only checkpoints.** That shrinks your *footage archive*; this shrinks
  your *paperwork*. **Different piles.** Every large operation does both.
