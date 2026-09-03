---
id: "063"
slug: model-calibration
style: pokemon
category: evaluation
difficulty: advanced
question: "What is model calibration and why does it matter?"
tags: [calibration, ece, reliability-diagram, temperature-scaling, confidence]
---

# Calibration: does "I'm 90% sure" mean anything?

Your Trainer calls a KO: *"Thunderbolt takes it. I'm 90% sure."*

**Calibration asks: when they say 90%, are they right 90% of the time?**

That's a completely separate question from whether they're any good. Consider:

* 🎯 **Right 70% of the time, and says "70% sure."** Not the strongest Trainer. **Perfectly
  calibrated** — and enormously useful, because you can *trust the number*.
* 🤥 **Right 90% of the time, and says "99% sure" about everything.** Stronger! And **useless for
  planning**, because you can't tell their good calls from their bad ones.

## Why you care 🎲

If the number is honest, you can act on it:

* 📈 *"95% sure"* → commit. Go for the KO.
* 🤔 *"60% sure"* → play it safe. Switch instead.
* 🆘 *"30% sure"* → don't guess. Ask a human.

If the number is always "99%", you get none of that. Every call looks identical, and you find out
which ones were wrong by losing.

## Reading the honesty 📊

Sort all your Trainer's past calls by stated confidence and check how often each group was actually
right:

```
   how often
   they were
    right
     100% │                                    ╱ ← perfectly honest
          │                                 ╱
      80% │                              ╱  ●
          │                           ╱    ●
      60% │                        ╱     ●
          │                     ╱      ●       ⬅ below the line:
      40% │                  ╱       ●            OVERCONFIDENT
          │               ╱        ●              (almost always
      20% │            ╱         ●                 what you find)
          │         ╱
          └──────────────────────────────────────►
           20%   40%   60%   80%  100%
                 what they SAID

   Read it: "when they said 80%, they were right 55%."
```

Everything sitting below the diagonal means overconfidence. Which it will be, because it always is.

## Why Trainers are overconfident 😤

**1. 🏋️ Training pushed them there.** The whole grind rewarded being *more certain* about correct
answers. There was never a point at which "certain enough" was enough — the pressure was always
toward *more*.

**2. 🏅 Coaching made it dramatically worse.**

This is the important one. Here's the measured finding:

> **Straight out of the wild grass, a Trainer's confidence is roughly honest. Coaching wrecks it.**

Because human judges preferred confident answers. Every hedge, every *"I think, but I'm not
certain"*, scored lower than a clean confident call. So you **trained the honesty out** — not by
accident, but because that's exactly what the judges rewarded.

The Trainer you deploy is systematically less honest about its own uncertainty than the one you
started with.

## Two ways to ask 🗣️

**📊 Watch how firmly they say it.** Cheap. But it muddles "I'm unsure about the answer" with "I'm
unsure how to phrase this."

**💬 Just ask: "how sure are you?"** More useful, and badly calibrated — they'll say **80% or 90%**
almost every time. Round numbers, no real gradation.

**🔁 The better method: ask three times and see if they agree.**

```
   Same position, asked three times:

   "Thunderbolt KOs"  /  "Thunderbolt KOs"  /  "Thunderbolt KOs"
   → they genuinely know. High confidence, earned.

   "Thunderbolt KOs"  /  "no, switch"  /  "Protect first"
   → they have no idea, whatever they claim.
```

**Disagreement with themselves is the most honest uncertainty signal you can get**, because they
can't posture their way out of it.

## Fixing it 🔧

**🌡️ Turn the confidence dial down.** Simple and effective: work out how overconfident they are on
average, and **scale every number down by that much.** One adjustment, applied uniformly.

The beautiful part: this changes **nothing about which move they pick.** Their ranking is
untouched — only the numbers attached to it. Same accuracy, honest numbers. Always try this first.

**📦 Have them name a set instead of an answer.** Rather than *"Thunderbolt, 90%"*, ask for *"the
moves that could work here"* — and construct it so that the right move is in the set 95% of the
time. **An actual guarantee**, rather than a number you're hoping is honest. Increasingly the
preferred approach when the stakes are real.

**👥 Ask several Trainers and average.** Where they disagree, the answer genuinely is uncertain, and
the average reflects it.
