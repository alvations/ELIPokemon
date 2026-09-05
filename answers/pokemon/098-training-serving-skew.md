---
id: "098"
slug: training-serving-skew
style: pokemon
category: mlops
difficulty: intermediate
question: "What is training-serving skew and how does a feature store help?"
tags: [training-serving-skew, feature-store, point-in-time, leakage, mlops]
---

# Training-serving skew: the practice scoreboard read differently

Your Trainer was excellent in practice. In real tournaments it's mediocre.

The Trainer didn't change. **The scoreboard did** — and nobody noticed, because nothing ever errors.
It just quietly gets things wrong.

## Four ways this happens 🔍

**1. 📏 Two people built the scoreboard.**

Practice used the one your analyst wrote. The Indigo Plateau uses the one their engineers built.

Both display *"average damage over the last 30 turns."* They disagree about whether a turn lost to
Hypnosis counts, and about whether Leftovers recovery is negative damage.

Your Trainer learned one meaning. It's being shown the other.

**2. ⏰ Practice data is tidied; live data isn't.**

Practice figures were **corrected afterwards** — mistakes fixed, duplicates removed, late results
added.

Live figures are whatever arrived in the last second, mistakes and all — a Ferrothorn logged as
fainted when Sturdy actually held.

Same question, different answers.

**3. 🔮 Practice used information from the future. ← the worst one**

```
   ❌ WHAT WENT WRONG
   Training on a Gyarados match from JANUARY.
   One of the inputs: "this Gyarados's total career wins."
   ...computed in SEPTEMBER. 😱

   That number includes eight months of results that hadn't
   happened yet when the January match was played.

   ✅ WHAT IT SHOULD BE
   For a January match, every input computed using ONLY
   what was known in January.
```

Your Trainer learned to lean on a number that **cannot exist** at tournament time. And in practice,
it was **magnificent** — it was quietly reading the future.

📌 **This is the most damaging one and the hardest to spot**, because the symptom is *excellent
practice results.* A suspiciously good practice score is a bug report.

**4. 🔄 Your Trainer changed the world it learns from.**

Your Trainer avoids Toxapex, because it predicts those matchups are losses. So those matchups
**never get played**, so you
never find out if it was right, so next season's training data contains only the matchups it already
liked.

It's now learning from a world it created.

## The fix: one scoreboard, two windows 🏛️

```
   ┌────────── DEFINE IT ONCE ──────────────────────────────────┐
   │  "average damage over the last 30 turns" = <one formula>   │
   └──────────┬─────────────────────────────┬───────────────────┘
              ▼                             ▼
   ┌────────────────────┐        ┌────────────────────┐
   │ 📚 THE ARCHIVE      │        │ ⚡ THE LIVE BOARD   │
   │ For practice.       │        │ For tournaments.   │
   │ Can answer "what    │        │ Answers instantly. │
   │ did this look like  │        │                    │
   │ last January?"      │        │                    │
   └────────────────────┘        └────────────────────┘
        Same formula. Same code. Two ways to read it.
```

The genuinely hard part — the bit worth paying for — is that first window being able to answer
**"what did this look like on the day?"** rather than "what does it look like now."

## The cheap fix that works ⭐

You may not need any of that infrastructure. There's a much simpler move most teams miss:

> **📝 Write down exactly what the scoreboard showed during every real tournament match. Then train
> on THAT.**

Think about what this does:

* ✅ Two implementations? **Impossible** — there's only the live one now.
* ✅ Tidied vs untidied? **Impossible** — you recorded the untidied version.
* ✅ Future information? **Impossible** — you recorded what was on the board *at that moment.*

You didn't fix the skew. You made it **structurally unable to exist**, because your practice data
**is** your tournament data.

📌 Costs you storage and nothing else. Needs no new infrastructure. **The most effective and most
overlooked fix there is.**

## Catching it 🕵️

* 🔍 **Compare directly.** Take one Ferrothorn holding Leftovers, read the practice scoreboard,
  read the live board.
  Different? There's your bug.
* 👻 **Run practice on live matches** without acting on it, and diff the two.
* 🚨 **Alarm on stale or missing figures** on the live board.
* ⚠️ **Treat any practice-vs-tournament gap as skew until proven otherwise.** It nearly always is.
