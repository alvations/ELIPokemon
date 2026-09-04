---
id: "084"
slug: cross-entropy-loss
style: pokemon
category: fundamentals
difficulty: core
question: "What is cross-entropy loss and why is it the right loss for language modelling?"
tags: [cross-entropy, kl-divergence, mle, nll, loss-functions]
---

# Cross-entropy: how badly did you call that?

Your Trainer predicted Cynthia's next move. She moved. **How much do you penalise the prediction?**

Cross-entropy has an unusual answer: **you don't grade the prediction. You grade how much confidence
they put on what actually happened.**

```
   Cynthia's Garchomp used Earthquake.

   Your Trainer had said:
     "90% Earthquake"  →  penalty 0.1   😌 basically right
     "50% Earthquake"  →  penalty 0.7   😐 hedged
     "10% Earthquake"  →  penalty 2.3   😰 wrong
     " 1% Earthquake"  →  penalty 4.6   💀 confidently wrong
     " 0% Earthquake"  →  penalty ∞     ☠️ "IMPOSSIBLE" — and it happened
```

That bottom row is the whole design. Rule something out **completely** and it happens, and the
penalty is **unbounded.**

## Why confidently wrong must hurt more 🎯

The alternative — just measure how far off the number was — has a fatal flaw:

```
   😐 "how far off?"                  ✅ CROSS-ENTROPY
   ────────────────                   ────────────────
   said 10%, it happened → 0.81       said 10% → 2.3
   said  1%, it happened → 0.98       said  1% → 4.6
   said  0%, it happened → 1.00       said  0% → ∞

   Barely any difference between       Enormous difference. Being
   "unlikely" and "IMPOSSIBLE."         MORE certain and MORE wrong
   Both just... a bit wrong.            costs proportionally more.
```

📌 **Confidently declaring something impossible, and being wrong, is a far worse failure than being
vaguely unsure.** Only cross-entropy treats it that way.

There's a second, more practical reason. With the "how far off" method, a Trainer who is **completely
certain and completely wrong** receives almost **no corrective feedback** — the maths quietly cancels
it out. Which is insane: that's the exact moment they most need to hear about it.

Cross-entropy gives the loudest feedback precisely when the Trainer is most confidently wrong.

## The same idea, three ways 🔄

Worth being able to state all three:

* 📻 **"How surprised were you?"** A prediction that assigned high probability to what happened is
  unsurprised. Low probability, surprised. You're minimising total surprise across the season.
* 🎲 **"How likely was reality, given your beliefs?"** Minimising this penalty is *identical* to
  maximising the probability your Trainer would have assigned to everything that actually happened.
* 📏 **"How far is your worldview from the truth?"** Reality has a fixed amount of genuine
  unpredictability — moves miss, crits happen, and nobody removes that. Minimising the penalty is
  exactly minimising **the rest**: the gap between your Trainer's picture and the real one.

Same number, three angles.

## Why this is *the* training signal 📈

For a Trainer learning by watching replays, every single turn is a prediction. Cross-entropy grades
every one.

* 📊 The **surprise score** everyone quotes is just this, rescaled into "how many options was it torn
  between?"
* 🔮 The **forecasting curves** that let you predict a huge run's quality before paying for it are
  plotted in this.
* 🎯 It's **dense** — a grade on every turn, not one grade at the end — so it detects tiny changes
  immediately.

## Four ways to break it 🚨

* 🔁 **Handing over percentages instead of raw scores.** The system converts them *again*. Silently
  degraded training, no error message. The most common mistake there is.
* 🏷️ **Ignoring rare events.** Every turn counts equally — so the one-in-a-thousand situation you
  actually care about contributes a thousandth as much as the routine ones.
* 🚫 **Grading the padding.** If your Brock replays run 6 turns and your Cynthia replays run 40,
  and you pad the short ones out, make sure
  the padding isn't being graded. Otherwise most of your training signal is about blank space.
* ✂️ **Grading the wrong half.** In coaching, you grade *"what should the Pokémon do?"* — you do
  **not** grade it on predicting what the Trainer says. Get that backwards and you've trained a
  Pokémon that impersonates you instead of obeying you.
