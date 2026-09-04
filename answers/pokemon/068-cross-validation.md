---
id: "068"
slug: cross-validation
style: pokemon
category: fundamentals
difficulty: core
question: "Explain cross-validation and describe cases where it silently fails."
tags: [cross-validation, k-fold, leakage, time-series, nested-cv]
---

# Cross-validation: test against five different Gyms, not one

You want to know how good your Trainer is. You hold back Brock's Gym as a test and train on
everything else.

Then they lose to Onix. **Are they bad, or are they just bad against Rock types?**

You have no idea, because you tested once.

## The fix 🔄

Split your footage into five piles — Brock's matches, Misty's, Lt. Surge's, Erika's, Koga's. Train
on four, test on the fifth. **Rotate.**

```
   round 1  [🧪TEST][ train ][ train ][ train ][ train ]  → 72%
   round 2  [ train ][🧪TEST][ train ][ train ][ train ]  → 68%
   round 3  [ train ][ train ][🧪TEST][ train ][ train ]  → 71%
   round 4  [ train ][ train ][ train ][🧪TEST][ train ]  → 70%
   round 5  [ train ][ train ][ train ][ train ][🧪TEST]  → 69%

   average: 70%,  spread: ±1.5%
```

Every match gets used for training *and* for testing. You get an honest average.

**And you get the spread**, which is the underrated half. Look at these two Trainers:

```
   😌 Trainer A:  71, 70, 69, 70, 70   →  70% ± 0.7    solid, predictable
   🎢 Trainer B:  95, 45, 88, 52, 70   →  70% ± 21     wildly matchup-dependent
```

**Same average. Completely different Trainers.** One number would have hidden that entirely — and
told you nothing about whether a 2% gap between two Trainers means anything at all.

## Five ways it lies to you 🚨

The danger of this method is that it **always gives you a number.** Every failure below returns a
confident, encouraging score.

**1. 📅 Splitting time-ordered footage randomly.**

Your footage spans a year. Split it randomly and your Trainer studies December and gets tested on
**March**. It's not predicting the metagame — it already **watched the rest of the season.**

✅ **Fix: always test on the future.**
```
   [Jan]                          [🧪 Feb]
   [Jan][Feb]                          [🧪 Mar]
   [Jan][Feb][Mar]                          [🧪 Apr]
   ──────────────────────────────────────────────► time
```

**2. 👥 The same opponent in both piles.**

You have forty matches against Brock. Random splitting puts thirty in training and ten in testing.
Your Trainer isn't being tested — **it knows Brock.**

✅ **Fix: split by opponent, not by match.** Every Onix match in one pile. This is the most common
mistake in real projects, by a wide margin.

**3. 🧹 Preparing the footage before splitting.**

You normalise, clean and index the whole year of footage, *then* split it.

Too late. Your preparation already **looked at the test matches** — the averages it computed include
them. ✅ **Prepare inside each round**, using only that round's training pile.

**4. 👯 Duplicate footage.** The same Starmie match filmed from two angles, landing in both piles. Deduplicate
first.

**5. 🎰 Trying two hundred setups and keeping the best.**

Try enough configurations and one will look brilliant **by luck.** You didn't find the best Trainer;
you found the one that happened to suit your five piles.

✅ **Fix: rounds inside rounds.** Use an inner rotation to *choose*, and an outer one to *measure*.
Tedious, and it's the difference between a real estimate and a flattering one.

**6. 🌍 The world changed.**

The one no method saves you from. Your rotation measures performance on **footage like your
footage.** If the metagame shifts, a new Pokémon is released, or you enter a different league —
your beautiful 70% is measuring a game nobody is playing any more.

## The rule 📌

> **A surprisingly good score means look for the leak, not open the champagne.**

Every failure above produces the same symptom: **an encouraging number.** And an encouraging number
is the least alarming thing a dashboard can possibly show you, which is exactly why these mistakes
survive to production.
