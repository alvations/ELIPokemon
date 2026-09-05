---
id: "095"
slug: data-drift
style: pokemon
category: mlops
difficulty: core
question: "What are data drift and concept drift, and how do you monitor for them?"
tags: [drift, monitoring, psi, kl-divergence, retraining]
---

# Drift: the metagame moved and nobody told your Trainer

Your Trainer was brilliant last season, when Garchomp was everywhere. It's mediocre now. **Nothing
changed on your side.**

The world moved. And there are four different ways it moves, needing four different responses.

## 1. 🌊 Different opponents now

Last season: Politoed rain everywhere. This season: everyone runs Garchomp and Landorus.

Your Trainer still **understands** Garchomp perfectly. It just prepared for a tournament that
isn't happening.

📌 **Note: this doesn't necessarily hurt.** A Trainer with genuinely broad knowledge handles the new
mix fine. Panicking every time the opponent mix shifts is a great way to retrain constantly for no
benefit.

## 2. 🔄 The same thing means something different now — the dangerous one

Last season, a Trainer leading with Ferrothorn meant *"defensive, playing for time."*

This season, a new item was released. **Leading Ferrothorn now means aggressive setup.**

```
   The observation is identical.        The meaning has inverted.
   Your Trainer reads it exactly        And it is now confidently,
   as it always has.                    systematically wrong.
```

📌 **This is the one that always hurts, and it can only be fixed by retraining.** No amount of
recalibrating helps when the meaning itself has flipped.

## 3. 📊 Same game, different rates

Shiny encounters went from 1-in-4096 to 1-in-500 during a Community Day — a Masuda-method rate
without the breeding.

Your Trainer's *judgement* is fine — it still knows a shiny Gyarados when it sees one. Its
**threshold** is now miscalibrated for how often the thing
actually happens. Adjust the dial, don't retrain.

## 4. 🔧 Somebody broke the scoreboard

The stadium changed how it reports HP — percentages instead of absolute numbers, so a Blissey at
"45" now means 45%, not 45 points. Your Trainer is
reading "45" as forty-five HP when it means forty-five percent.

📌 **This is most drift alerts.** Not the world changing — **your pipe leaking.** Check this
first, always, before theorising about the metagame.

## What to watch, in order 👀

```
   1️⃣ 🏆 ARE YOU WINNING?
      The truth. Nothing beats it.
      ❌ You often don't find out for weeks or months.

   2️⃣ 📊 WHAT IS YOUR TRAINER SAYING? ← the underrated one
      Its predictions, tracked over time. FREE, INSTANT, no results needed.

   3️⃣ 📥 WHO ARE YOU FACING?
      The mix of opponents, compared to what you trained on.

   4️⃣ 🔧 IS THE SCOREBOARD WORKING?
      Missing fields, impossible values, stale data.
      Check this the moment ANYTHING fires.
```

**Number 2 is the one nobody uses, and it's the best early warning you have.**

You don't need to know who won. You just watch **what your Trainer is saying:**

> Last month it predicted a win 60% of the time. This week: **91%.**

Nothing about the world has been confirmed. But your Trainer's behaviour changed **overnight**, and
you know *right now* — weeks before a single result comes in.

## Three things that go wrong 🚨

**🎭 The average hides everything.**

> Overall win rate: **unchanged.** Everything's fine!
>
> Against Dragon teams: **collapsed from 71% to 22%.**
>
> Dragon teams are 8% of your matches, so the average barely moved.

📌 **Break it down. By opponent type, by format, by region, by anything you can.** Aggregates are
where failures hide.

**🔔 Too many alarms.** Watch five hundred things and a couple dozen will look "unusual" every single
day by pure chance. Everyone learns to ignore the alerts, and then the real one arrives.

Use *"how big is the change?"* not *"is there technically a change?"* — with enough matches,
**everything** is technically different.

**🗑️ You didn't keep the records.**

The one people regret most. Something goes wrong, you go to investigate, and **you never logged what
your Trainer was seeing or saying.**

You have a broken Trainer and nothing to diagnose it with. **Log the inputs and the predictions from
day one.**

## When to retrain 🔄

* 📅 **On a schedule** — every time a new Regulation drops. Simple, predictable, sometimes
  wasteful. Most teams do this.
* 🏆 **When you start losing.** Correct — and only works if results arrive quickly enough to act on.
* 🚨 **When drift fires.** Fast, and noisy.

Most mature setups run **scheduled retraining plus a losing-streak alarm.** The schedule handles slow
change; the alarm catches the day the metagame flips.
