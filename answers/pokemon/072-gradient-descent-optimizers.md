---
id: "072"
slug: gradient-descent-optimizers
style: pokemon
category: optimization
difficulty: core
question: "Explain gradient descent and its variants: SGD, momentum, Adam, AdamW."
tags: [sgd, momentum, adam, adamw, optimizers, bias-correction]
---

# Training up: how do you decide what to work on next?

Your Garchomp lost. You need to adjust its EVs — the 508 points of effort you get to spread
across its six stats. **How do you decide which stat, and by how much?**

## 🚶 Plain training: one loss, one adjustment

Lose a match, spot the weakness — Garchomp got outsped — adjust. Repeat.

Two ways to gather evidence:

* 🐌 **Play every opponent in Kanto, then adjust once.** Perfect information. Takes a month per
  adjustment.
* 🏃 **Adjust after every single match.** Fast, and wildly noisy — one loss to a lucky Critical Hit
  and you've dumped 252 EVs into Special Defence for no reason.

**In practice: adjust after every twenty matches.** Enough signal to be sane, fast enough to make
progress — roughly one circuit of the Battle Tower. And the leftover noise is genuinely useful —
it stops you getting stuck polishing one
narrow approach forever.

## 🏃‍♂️ Momentum: stop flip-flopping

Here's a real failure. You keep flip-flopping between Attack and Defence — 252 into one, then 252
into the other, then back — while the Speed tier that actually loses you games goes untouched:

```
   😵 WITHOUT MOMENTUM               🏃 WITH MOMENTUM
   ───────────────────               ────────────────
      ╲    ╱                            ╲    ╱
       ╲ ↗╱   "more Attack!"             ╲  ╱
        ╲╱↘   "no, more Defence!"         ╲╱ ────────►
        ╱╲↗   "no, Attack!"               ╱╲
       ╱  ╲   "no, Defence!"             ╱  ╲

   Thrashing between two              The thrashing cancels out.
   corrections. Barely moving         The thing you've needed EVERY
   toward what you actually need.     week — more Speed — accumulates.
```

Momentum means **remembering your recent adjustments.**

Contradictory advice ("more Attack!" / "more Defence!") **cancels out**. Consistent advice ("more
Speed") **builds up week after week**.

You stop reacting to individual losses and start following the trend across them. `β = 0.9` roughly
means "average the last ten weeks of feedback."

There's a sharper version: instead of asking *"what's wrong now?"*, **look ahead to where your
current momentum is taking you and ask what'll be wrong when you get there.** Correct before you
overshoot rather than after.

## 🎚️ Adaptive: different stats need different attention

Your Attack gets feedback every single match. Your Special Defence comes up **once a month**.

Adjust both by the same amount and Special Defence never develops — it's simply mentioned too
rarely.

**So: scale the adjustment by how often you get feedback.** Speed comes up every single turn;
Special Defence comes up when something finally clicks an Ice Beam at you.

* 📢 **Constant feedback** (Speed decides every turn) → small careful adjustments. You'll get
  another chance tomorrow.
* 🤫 **Rare feedback** (Special Defence, which only matters against Ice Beam) → make it count. This
  might be your only data point this month.

Combine that with momentum and you get the standard method: **remember the trend** *and* **weight
the adjustment by how noisy that stat's feedback has been.**

## 🐣 The startup problem

Nice detail that trips people up.

Week 1, you have **no history.** Your "average of the last ten weeks" is an average of one week, and
your "how noisy is this stat" estimate is based on a single observation.

Left uncorrected, your very first adjustments come out **enormous** — you're dividing by a
noise-estimate that's still essentially zero.

**The fix: scale up early estimates to account for having so little history.** Week 1 gets a big
correction, week 2 less, and by week 50 the correction has faded to nothing. Without it, training
routinely explodes in the first few steps.

## 💰 The upkeep bug

There's a famous mistake here, and it's the reason the standard method has a corrected version.

Everyone charges their Pokémon **upkeep** to stop any one stat running away. The old approach folded
that upkeep into the same feedback channel as everything else.

Which meant: **stats with noisy feedback got charged less upkeep.** Entirely by accident. The
adaptive scaling was diluting the upkeep along with everything else.

**The fix: charge upkeep separately**, directly, outside the feedback system.

Sounds like a technicality. It measurably improved training, and the corrected version is what
everybody uses now.

## What to actually use 🎯

* ✅ **The corrected adaptive method with momentum.** The default — what you would use to EV-train
  a Garchomp and everything else. Works nearly everywhere with nearly no tuning, which is exactly
  why it won.
* 🏃 **Plain momentum** is still competitive for some kinds of training, the way a Choice Scarf is
  still competitive, and occasionally
  generalises better.
* 💾 **Watch the storage cost.** Remembering the trend *and* the noisiness means **two extra
  notebooks per stat** — twelve notebooks for one Garchomp. That's the dominant memory cost of
  training — and precisely what the held-item
  trick avoids by only ever tracking a handful of stats.
