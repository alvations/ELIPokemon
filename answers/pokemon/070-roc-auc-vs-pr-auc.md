---
id: "070"
slug: roc-auc-vs-pr-auc
style: pokemon
category: evaluation
difficulty: intermediate
question: "What is the difference between ROC-AUC and PR-AUC?"
tags: [roc-auc, pr-auc, imbalance, ranking-metrics, average-precision]
---

# Two scorecards, and one of them flatters you

Your shiny detector needs grading. Two ways to do it — and on something as rare as a shiny
Gyarados, **one of them lies.**

## Setting the scene 🌾

```
   In this patch of grass:
   🐀 1,000,000 ordinary Rattata, Zubat and Caterpie
   ✨         1,000 shinies

   Your detector flags 10,900 Pokémon.
   Of those, 900 are genuinely shiny.
```

Grade it.

## 📊 Scorecard A: "what fraction of the ordinary ones did you wrongly flag?"

```
   10,000 wrongly flagged ÷ 1,000,000 ordinary = 1%

   🎉 "Only 1% false alarm rate! Outstanding detector!"
```

## 🎯 Scorecard B: "when you flag something, is it actually shiny?"

```
   900 correct ÷ 10,900 flagged = 8.3%

   💀 "Nine out of every ten balls you throw are wasted."
```

**Same detector. Same numbers.** One scorecard says outstanding; the other says nearly useless.

## Why A lies 🤥

Because it divides by **a million.**

Ten thousand wasted Ultra Balls is a catastrophe — that is every Poké Mart in Kanto, several times
over. But
ten thousand out of a *million* is 1%, and 1% sounds wonderful.

**The enormous pile of correctly-ignored Rattata drowns out your mistakes.** Scorecard B never
mentions them, which is exactly why it stays honest.

📌 **You throw Ultra Balls. You don't throw "non-balls."** The scorecard that measures what you actually
*spend* is the one that matters.

## When each is fine 📋

| | 📊 Scorecard A | 🎯 Scorecard B |
| --- | --- | --- |
| A random detector scores | always 50% | the actual shiny rate (0.1%) |
| Distorted by rarity | ❌ hides it | ✅ shows it |
| Compare across grass patches | ✅ works | ❌ only within one rarity |
| Use when | shinies are common, both mistakes cost the same | **shinies are rare and you care about finding them** |

**Rule of thumb:** if the thing you're hunting is under about **one in ten**, use scorecard B.

And when someone shows you a spectacular scorecard-A number on something rare: **ask what fraction
of their flags are actually correct.** That is the number that decides whether anyone can use the
thing.

## Scorecard B's own quirk ⚠️

It doesn't cut cleanly the other way either.

A **0.4** at the Lake of Rage, where one shiny hides in a thousand Magikarp, may be **far more
impressive** than a **0.6** in a patch where one in five is shiny. The second detector had an enormously easier job.

📌 So always report **how rare the thing was.** Scorecard B numbers from different patches are not
comparable, and treating them as such is a common way to pick the wrong model.

## The last thing 🎯

Both scorecards average over **every possible setting of your detector's dial** — including all the
settings you'd never actually use.

Once you've picked a detector and set the dial where you're really running it, **report the numbers
at that setting.** How many balls will you throw today? How many will land? What does a miss cost?

That's the number that decides whether to build the thing. The scorecards are for choosing between
detectors, not for deciding whether one is good enough.
