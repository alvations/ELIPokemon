---
id: "083"
slug: softmax-and-logsumexp
style: pokemon
category: fundamentals
difficulty: intermediate
question: "What is softmax, and why do we need the log-sum-exp trick?"
tags: [softmax, logsumexp, numerical-stability, overflow, temperature]
---

# Softmax: turning matchup scores into a plan for the turn

Your Pokémon has rated its options:

```
   Thunderbolt   score  8.2
   Volt Switch   score  5.1
   Protect       score  3.8
   Tail Whip     score -2.0
```

Those are **raw scores**. They don't add up to anything. You need a **plan for the turn** — and you
only get one turn, so the plan has to add up to exactly one turn's worth of effort.

Softmax does that conversion:

```
   Thunderbolt   ████████████████████  92%
   Volt Switch   ███                    6%
   Protect       █                      2%
   Tail Whip     ▏                      0%
                                       ────
                                       100%  ← one turn, fully allocated
```

Two properties worth knowing: it **never changes the ranking** (Thunderbolt was best before and
after), and it **amplifies gaps** — a score of 8.2 versus 5.1 doesn't become 62% versus 38%, it
becomes 92% versus 6%. Good options get emphasised, bad ones get crushed.

## The problem: the numbers explode 💥

The conversion works by **exponentiating** every score. And that grows terrifyingly fast.

```
   score  10  →  22,026
   score  50  →  5,184,705,528,587,072,464,087,453,322,932,355,782,...
   score  90  →  💥 too big to write down. Your calculator gives up.
```

At high levels, scores routinely reach the hundreds. And in a competitive context — where you turn
the decisiveness dial up and every score gets multiplied — they go higher still.

```
   scores = [1000, 999, 998]

   😱 naïvely:  exp(1000) = TOO BIG
                TOO BIG ÷ TOO BIG = ???
                Your Pokémon has no plan. The run is dead.
```

Note that those three scores are **nearly identical** — the answer should obviously be roughly a
three-way split. The maths is trivial. The **arithmetic** is what broke.

## The fix: everything is relative anyway 🎯

Here's the observation that saves you.

**Only the gaps between scores matter.** `[1000, 999, 998]` and `[2, 1, 0]` describe *exactly the
same situation* — one option is 1 better than the next, which is 1 better than the third.

So: **before converting, subtract the best score from everything.**

```
   scores = [1000, 999, 998]
   best   = 1000
   shifted = [0, -1, -2]        ← same situation, sane numbers

   exp([0, -1, -2]) = [1.00, 0.37, 0.14]
   total = 1.51
   plan  = [66%, 24%, 9%]    ✅ correct, and nothing exploded
```

The largest number you ever exponentiate is now **exactly zero**, which gives exactly 1. **Overflow
becomes impossible.** Not unlikely — impossible.

And the small ones might round away to nothing, which is fine: they were negligible options anyway.

📌 **You get the identical answer.** This isn't an approximation or a safety compromise — it's the
same calculation, arranged so the arithmetic can survive it.

## The related trap 🪤

Sometimes you don't want the percentages — you want their **logarithms** (this is what scoring and
training need).

The tempting approach: compute the percentages, then take the log.

**Don't.** Tiny percentages round to zero on the way, and the log of zero is a catastrophe. You threw
away the precision *before* you needed it.

**Go straight to the logarithm**, skipping the percentages entirely. Same trick, applied one step
earlier.

## The bug this causes constantly 🐛

Nearly every scoring system expects **raw scores** and does the whole safe conversion internally.

So if you helpfully convert to percentages first and hand *those* over, it converts them **again**.

```
   😐 What you did:     scores → percentages → hand over
   😱 What it did:      percentages → percentages AGAIN
```

Your Pokémon now trains on a mangled, flattened version of its own preferences. **No error. No
warning.** Just a run that's quietly, permanently worse — and one of the most common mistakes there
is.

**Hand over the raw scores. Let the system do the conversion.**
