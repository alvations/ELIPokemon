---
id: "078"
slug: gradient-checkpointing
style: pokemon
category: systems
difficulty: intermediate
question: "What is gradient checkpointing and what does it trade away?"
tags: [gradient-checkpointing, activation-recomputation, memory, training]
---

# Gradient checkpointing: don't film every Gym, just the checkpoints

To work out whose fault the loss was, you walk back through the season and need **your notes from
every stop.**

So you film everything. Every Gym, every route, every battle. And the footage archive becomes
**bigger than everything else you own** — bigger than your team records, bigger than your training
notes. It's the thing that stops you training a longer season.

## The trick 🎬

**Don't film every Gym. Film every third one — and when you need the missing footage, just replay
those two Gyms from the last checkpoint.**

```
   📹 FILM EVERYTHING
   Gym1 ─► Gym2 ─► Gym3 ─► Gym4 ─► Gym5 ─► Gym6 ─► Gym7 ─► Gym8
    🎬     🎬      🎬      🎬      🎬      🎬      🎬      🎬
   Eight tapes. Instant review. An enormous archive.

   📸 FILM CHECKPOINTS ONLY
   Gym1 ─► Gym2 ─► Gym3 ─► Gym4 ─► Gym5 ─► Gym6 ─► Gym7 ─► Gym8
    🎬      ·       ·      🎬       ·       ·      🎬       ·

   Three tapes.
   Need Gym 5? Start from the Gym 4 tape and REPLAY Gyms 4 and 5.
```

You had the Gym 4 state on tape, so replaying forward from there gets you Gym 5 exactly. Not an
approximation — **the identical footage**, reconstructed.

## What it costs 💰

Surprisingly little, and the reason is worth knowing.

Reviewing a season is already about **twice** as much work as playing it. So adding one extra replay
doesn't double your effort — it adds about **a third**.

```
   📹 Film everything:   play(1) + review(2)             = 3 units
   📸 Checkpoints only:  play(1) + replay(1) + review(2) = 4 units

   ~33% more work. A fraction of the archive.
```

## Why it can be FASTER 🤯

Here's the counterintuitive part, and it's the good bit.

You'd assume: 33% more work, 33% slower. Often it's the opposite.

Because now that your archive is small, **you can train several Pokémon at once** in the space you
freed. And training four simultaneously is far more than four times as efficient as training one at a
time — the facility is being properly used instead of sitting half idle.

```
   Before: 1 Pokémon at a time, gigantic archive       → slow
   After:  4 Pokémon at once,  33% more work each      → FASTER overall
```

📌 **The point isn't to save effort. It's to make the run possible at all**, and the extra capacity
you unlock frequently pays back the overhead with interest.

## Doing it well 🎯

* 🎯 **Be selective about what you film.** Some moments are trivially cheap to replay (a routine
  route walk); some are expensive (a full Gym battle). Film the expensive ones, replay the cheap
  ones. Nearly all the archive savings, a fraction of the replaying.
* 🎲 **The replay must be EXACT.** If anything random happened — a critical hit, a random benching —
  you must **record the dice rolls** so the replay comes out identical. Get this wrong and you're
  apportioning blame for a season that never happened. A classic and horrible bug.
* 🤝 **It stacks with everything else.** Splitting your team across facilities shrinks your *team
  records*; this shrinks your *archive*. **Different problems**, so use both. Every large operation
  does.
* 🏆 **Not needed at tournaments.** You only review to learn. On tournament day nobody's going back
  through the tape — so no filming, no archive, nothing to save.
