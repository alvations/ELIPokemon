---
id: "076"
slug: learning-rate-schedules
style: pokemon
category: optimization
difficulty: intermediate
question: "Why do we use learning-rate warmup and decay schedules?"
tags: [learning-rate, warmup, cosine-decay, wsd, schedules]
---

# Warmup and decay: how hard to train, and when

**How aggressively should you train?** It's the most important question you'll answer — and the right
answer **changes** over the season.

```
   how hard │      ╱‾‾‾╲
   you push │     ╱      ╲___
            │    ╱            ╲___
            │   ╱                  ╲____
            │  ╱                        ╲______
            │ ╱                                ╲_____
            └─────────────────────────────────────────────► the season
             │←warm │←────── ease off gradually ───────→│
             │  up  │
```

## 🏃 Warmup: ease into it

Day one, you do **not** put a fresh Magikarp through Champion-level training. You'd break it.

Start gently. Build up over the first week or two.

Three reasons, and the middle one is the one people miss:

**1. 🩹 Obviously — don't injure it.** A brand new Pokémon has no conditioning.

**2. 🧭 Your coaching instruments haven't calibrated yet.** ← the real reason

Modern training adjusts each stat based on **how noisy that stat's feedback has been historically.**

On day one there **is** no history. Your noise estimates are built on one or two observations, and
they're wildly unreliable. Train hard on a wrong noise estimate and you'll make an enormous
adjustment in a direction that turns out to be nothing.

So: go gently until your instruments have enough data to be trusted. It's not the Pokémon that needs
warming up — it's **your measurements.**

**3. 💪 You want to train hard later.** The whole reason you're being careful now is to reach a high
intensity safely. Apply that intensity on day one and there's nothing left to train.

📌 Skipping warmup is the single most reliable way to destroy a training run in the first ten
minutes.

## 📉 Easing off: from exploring to refining

**Early on**, big changes are right. You don't know what this Pokémon should be yet. Try things.
Restructure. Be bold.

**Late on**, you're 95% of the way there. Big changes now just knock you off the thing you spent
months building. You want **small refinements**, not another restructure.

```
   💪 EARLY: "let's completely change its role"
   🔧 LATE:  "half a point more Special Defence"
```

Ease off gradually and you go from bold to careful without a jarring transition.

## The shapes 📐

| Shape | What it does |
| --- | --- |
| 🌊 **Smooth curve down to nothing** | The standard. Gentle at both ends. |
| 📏 **Straight line down** | Simpler, nearly as good. Common for short specialist camps. |
| 🪜 **Big drops at milestones** | The classic older approach. |
| 🏔️ **Flat, then a sharp drop at the end** | The clever modern one — see below. |

## Why the flat one is genuinely better 🏔️

The smooth curve has an annoying practical flaw: **you have to commit to the season length in
advance.**

Want to stop at week 30 of a 50-week plan? You can't use that Pokémon — it's still mid-training,
still making big adjustments, never settled.

Want to extend to week 70? Rip up the plan and start over.

**The flat approach fixes both.** Hold a steady intensity for most of the season, then drop off
sharply over the final 10%.

Now you can stop **whenever you like**: take the Pokémon as it stands, run a two-week taper, and you
have a finished competitor. Want to keep going instead? The intensity never changed, so just carry
on.

Same results, vastly more practical — which is why the big modern training runs use it.

## Setting the intensity 🎚️

* 📊 **Bigger training groups take more intensity.** Training twenty Pokémon at once? You can push
  harder than with one, because you're averaging over more feedback.
* 🏕️ **Specialist camps need much gentler training than the original raising** — ten to a hundred
  times gentler. You're refining a Champion, not building one, and it's very easy to undo months of
  work in an afternoon.
* 🎒 **Held items want it turned back UP** — much harder than a full retrain. There's very little
  there to change, so you have to push it to move at all.
* 🔬 **Find the ceiling in ten minutes.** Push harder and harder over a few hundred sessions and
  watch where the Pokémon starts falling apart. **Take a third of that.** Ten minutes of work, and it
  beats guessing every time.
