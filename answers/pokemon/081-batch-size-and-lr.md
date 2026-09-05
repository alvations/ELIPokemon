---
id: "081"
slug: batch-size-and-lr
style: pokemon
category: optimization
difficulty: intermediate
question: "How are batch size and learning rate related, and what is gradient accumulation?"
tags: [batch-size, learning-rate-scaling, gradient-accumulation, critical-batch-size]
---

# How many matches before you change anything?

You're adjusting your Garchomp's EV spread based on how it performs. **How many matches do you
watch before deciding?**

```
   1️⃣ ONE MATCH, then adjust
      Lost to one Critical Hit? "REBUILD EVERYTHING."
      🎲 Wildly noisy. You're chasing dice rolls.

   💯 A HUNDRED MATCHES, then adjust
      Now you can see the real pattern: Garchomp is losing the Speed
      tier to Jolteon, not to bad luck.
      🎯 Trustworthy — but you only adjust once per hundred matches.
```

## The relationship 🔗

Here's the thing that connects them:

> **The more matches you watched, the more you can trust what you saw — so the bigger a change you
> can safely make.**

```
   👀 1 match   → could be one Critical Hit  → 🐁 4 EVs
   👀 10 matches → probably real             → 🚶 60 EVs
   👀 100 matches → definitely real     → 🏃 confident adjustment
```

Watch a hundred matches and then make a **tiny** adjustment and you've wasted all that evidence.
Watch **one** match and make a huge adjustment and you're reacting to a coin flip.

📌 **So when you change how many matches you watch, you MUST change how hard you adjust.**

The rough rule: watch ten times as many matches, adjust roughly ten times harder. (For modern
training methods, somewhat less than ten — three or so — but the direction is the same.)

🚨 **This is the most common invalid comparison in the field.** Someone tries bigger batches, forgets
to adjust the intensity, gets worse results, and concludes "bigger batches are worse." They tested
one thing and changed two.

## Where it stops helping 🛑

```
   how big an │              ___----‾‾‾‾   more evidence, bigger steps
   adjustment │         __--
   you can    │      _--                   ▲
   safely make│   _--                      │ past here: you already KNOW
            │ _-                           │ what's wrong. Watching more
            │-                             │ matches tells you nothing new.
            └──────────────┬─────────────────────► matches watched
                    the point of diminishing returns
```

Below that point, more matches genuinely means faster progress — you were being held back by noise.

Above it, you already know exactly what to fix. Watching four hundred more matches confirms the same
conclusion, and **you've spent four hundred matches to learn nothing.**

📌 The practical version: **there's a point past which more gyms don't train you faster, just
cheaper per match.**

## Gradient accumulation: faking a bigger batch 📦

You want to decide based on a hundred matches. Your gym only holds ten Pokémon at a time.

**So: run ten sessions of ten, keep a running tally, and adjust once at the end.**

```
   session 1 (10 matches) → note the lessons, DON'T adjust yet
   session 2 (10 matches) → add to the tally
   ...
   session 10 (10 matches) → add to the tally
   ────────────────────────────────────────────
   NOW adjust, based on all 100.
```

Mathematically identical to watching a hundred at once. Ten times the wall-clock time, but it fits in
your gym.

## Three gotchas 🚨

**➗ Divide by ten.** You summed ten sessions of lessons — so **average them**, don't just add.
Otherwise you dump 2,520 EVs into Speed, which is five times the legal cap. Forget
this and you're adjusting **ten times harder than intended**, and the run explodes.

The single most common bug in this entire technique.

**⚖️ Comparing against the room doesn't survive this.** Flat Rules scale you against whoever
turned up today, so ten rooms of ten is not one room of a hundred. If your Flat Rule scales
Pokémon relative to
*whoever's in the room today*, then ten rooms of ten is genuinely different from one room of a
hundred — the rooms were different.

Scaling each Pokémon against **its own stats** is unaffected. One more reason modern setups use it.

**📞 Don't phone Brock and Misty after every session.** You're accumulating — the intermediate
tallies are meaningless. **Talk once, at the end.** Skip this and you're paying ten times the phone bill for
nine conversations about nothing.

## One last thing 🎲

Watching more matches isn't automatically better for the *final* result.

A bit of noise keeps your Garchomp from over-committing to any single pattern — from concluding
that every opponent runs Ice Beam because two of them did. So the biggest batch
that fits in your gym isn't necessarily the batch you want — it's just the fastest one.
