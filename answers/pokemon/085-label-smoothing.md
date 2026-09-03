---
id: "085"
slug: label-smoothing
style: pokemon
category: training
difficulty: intermediate
question: "What is label smoothing and when does it hurt?"
tags: [label-smoothing, calibration, regularisation, distillation]
---

# Label smoothing: never be 100% certain

Your Trainer is being drilled on a replay. *"What did the opponent do here?"*

The answer key says: **Thunderbolt. 100%. Everything else 0%.**

Chase that target and your Trainer keeps pushing — 95%, 99%, 99.9%, 99.99% — **forever.** It can
never actually reach 100%, so it never stops trying. Every drill, more certainty.

The result: a Trainer that is **absolutely certain about everything**, including the things it's
wrong about.

## The fix 🎯

Change the answer key.

> *"Thunderbolt — 90%. And leave a little room for everything else."*

```
   😤 THE OLD KEY                   😌 THE SOFTENED KEY
   ──────────────                   ──────────────────
   Thunderbolt   100%               Thunderbolt   90%
   Volt Switch     0%               Volt Switch    0.1%
   Protect         0%               Protect        0.1%
   Splash          0%               Splash         0.1%

   Target: absolute certainty.      Target: strong, not absolute.
   Never reachable → never stops    Reachable → training completes,
   pushing.                          and stops.
```

Now there's an actual finish line. Your Trainer reaches 90%, the pressure stops, and it moves on.

## What you get 🎁

* 🎯 **Honest confidence.** When it says 90%, it's roughly right 90% of the time — instead of saying
  99.9% about everything.
* 🛡️ **Robustness to bad footage.** If a replay was mislabelled, the old key drove your Trainer to
  **absolute certainty** about something false. The softened key limits the damage.
* 📐 **Cleaner organisation.** Options group up neatly instead of being flung as far apart as
  possible.

A lovely, slightly odd result from machine translation: softening makes the surprise score **worse**
while making the actual translations **better.** The Trainer is deliberately less certain, and makes
better calls. Two different things, and only one of them is what you wanted.

## Where it backfires 💥

Here's the case that matters, and it's the point of the question.

**🎓 Never soften the key when the Trainer's job is to TEACH.**

Remember what makes a Champion a good teacher: the **structure in its near-misses.**

```
   🏆 A GREAT TEACHER says:
      Thunderbolt   85%
      Thunder       11%   ⬅ "same plan, riskier — these are cousins"
      Surf           2%
      Splash         2%

   The rookie learns: Thunderbolt and Thunder are RELATED.
   Surf and Splash are different ideas entirely.
```

Now soften it:

```
   😐 A SOFTENED TEACHER says:
      Thunderbolt   90%
      Thunder        0.1%  ⬅ ─┐
      Surf           0.1%  ⬅ ─┤ all identical now
      Splash         0.1%  ⬅ ─┘

   The rookie learns: Thunderbolt. And... nothing else.
```

You **flattened all the near-misses to the same value.** The relationship between Thunderbolt and
Thunder — the single most valuable thing the Champion had to pass on — is **gone.**

📌 A softened teacher is a **better competitor and a worse teacher.** That's a genuinely measured
result, and it's counterintuitive enough to be worth remembering.

## Other places to skip it ⛔

* 📏 **When you need the raw gaps.** Any downstream system reading the actual margins between options
  gets distorted numbers.
* 🌳 **When some wrong answers are much wronger than others.** Uniform softening declares every wrong
  option **equally** wrong. Mistaking Charmeleon for Charizard is not the same mistake as mistaking
  it for Magikarp.
* 🌾 **In the wild grass.** Rarely used for the main grind — the future is genuinely uncertain
  already, there are tens of thousands of options so the softening is negligible anyway, and it
  distorts exactly the thing you're trying to measure.
