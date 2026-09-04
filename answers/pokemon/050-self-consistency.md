---
id: "050"
slug: self-consistency
style: pokemon
category: prompting
difficulty: intermediate
question: "What is self-consistency decoding?"
tags: [self-consistency, majority-vote, sampling, test-time-compute, verifier]
---

# Self-consistency: run the calc six times and vote

Your Trainer works out whether Thunderbolt KOs that Gyarados. Gets an answer. It might be right.

So make them do it **six more times, from scratch**, and see what they keep saying.

```
   ❓ "Does Thunderbolt KO?"
        │
        ├─► 🧮 attempt 1: ...via base power  ──► "yes, 342 damage"  ✅
        ├─► 🧮 attempt 2: ...via type chart  ──► "yes, 340 damage"  ✅
        ├─► 🧮 attempt 3: ...comparing stats ──► "no, 280 damage"   ❌
        ├─► 🧮 attempt 4: ...via base power  ──► "yes, 344 damage"  ✅
        ├─► 🧮 attempt 5: ...rough estimate  ──► "yes, ~350"        ✅
        └─► 🧮 attempt 6: ...via type chart  ──► "yes, 341 damage"  ✅

   🗳️  YES: 5    NO: 1     →  it KOs.
```

Attempt 3 slipped somewhere. The other five didn't, and they didn't agree because they copied each
other — they got there by **different routes**.

## Why voting works 🎯

Here's the asymmetry that makes this so effective:

> **There are many roads to the right answer. Wrong answers scatter.**

Six correct calculations land on 341, give or take rounding. Six *mistakes* land on 280, 195, 412,
88, 341-but-for-the-wrong-reason, and 6.

So right answers **pile up** and wrong answers **spread out**. Count the pile.

This is just getting a second opinion — except the second opinion is the same Trainer, approaching
it fresh.

## The setting that ruins it 🌡️

Run this with your Trainer set to maximum decisiveness and you get:

```
   attempt 1: "yes, 342"
   attempt 2: "yes, 342"
   attempt 3: "yes, 342"     ← the same calculation, six times
   attempt 4: "yes, 342"        You learned nothing.
   attempt 5: "yes, 342"
   attempt 6: "yes, 342"
```

**You need genuine variety.** The whole method depends on the six attempts taking *different routes*.
Loosen them up so they actually approach it differently, or you've paid six times for one answer.

## How many attempts? 📈

```
   1 attempt   ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░
   3 attempts  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░
   5 attempts  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  ← most of the benefit is here
  10 attempts  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
  40 attempts  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ← 4× the cost for a sliver
```

Five to ten. Past that you're paying a lot for very little.

And this was one of the first clear demonstrations of something important: **you can buy accuracy
with thinking time at battle time**, without retraining anything. Just let it think more.

## Where it fails ⚠️

**🧱 A Trainer that's confidently wrong stays confidently wrong.**

If your Trainer genuinely believes Thunderbolt is super effective against Golem, all six attempts
happily agree. Voting confirms it. **Six times.**

📌 This fixes *slips*, not *misconceptions*. Random mistakes scatter and get outvoted. A systematic
misunderstanding shows up identically in all six and gets a landslide.

**🔤 You need answers you can actually compare.** *"342 damage"* votes fine. *"Yes"* / *"No"* votes
fine. *"Write me a battle strategy"* — six different strategies, no majority, nothing to count.
(Though for a *plan*, you can vote on whether it wins.)

**💰 Six times the cost.** They do run in parallel, so it's six times the money but not six times
the wait.

**😐 Well-coached Trainers get boring.** Heavily-coached Trainers tend to give the same answer every
time regardless of settings — which is exactly the property that makes this method not work. The
Trainers you actually deploy are often the ones this helps least.

## The bigger idea 💡

Voting is the simplest version of a pattern that shows up everywhere:

> **Generate several candidates, then pick one.**

* 🗳️ **Vote** — cheapest, needs no extra anything.
* 👨‍⚖️ **Have a judge pick** — better, needs a judge.
* ✅ **Check which ones actually work** — best of all, when you can check.
* 🌳 **Explore branches and back up when one goes bad** — most thorough, most expensive.

Modern reasoning Trainers have this **built in** — they were trained to try, check themselves, and
backtrack, all within a single answer. Voting is still worth knowing because it needs no extra
models, no training, and about ten lines of code.
