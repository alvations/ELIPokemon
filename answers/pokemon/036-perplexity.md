---
id: "036"
slug: perplexity
style: pokemon
category: evaluation
difficulty: core
question: "What is perplexity and what are its limits?"
tags: [perplexity, cross-entropy, evaluation, tokenizer, bits-per-byte]
---

# Perplexity: how surprised is your Trainer, every turn?

Watch a Cynthia replay. Pause before each move. Ask your Trainer: *"what happens next?"*

**Perplexity is how many options they were effectively torn between.**

```
   1     🎯 "Thunderbolt the Gyarados." And it was. Every time.
            Perfect prediction. Nothing surprises them.

   2     🪙 Torn between two moves, coin-flip. Every turn.

   10    🤔 Effectively picking from ten plausible moves.

   50    😐 Fifty moves feel equally likely. Thunderbolt? Splash? Roost?
            That's a rookie on Route 1.

   50,000 🫠 No idea. Might as well name a random Pokémon.
```

**Lower is better.** A Trainer at 5 has genuinely internalised the game. One at 500 is guessing.

## Why it's a great instrument 📏

* 📊 **Every single turn is a measurement.** A thousand-turn replay gives a thousand data points.
  Tiny changes show up immediately.
* 🏷️ **No judges required.** You don't need anyone to grade anything — you just check whether the
  guess matched the replay.
* 🔮 **It's what makes forecasting possible.** Train a few small Trainers, plot their surprise, and
  you can predict how surprised a Trainer costing your entire season budget will be. That's how
  anyone dares to commit to an expensive training run.
* 🚨 **It's your smoke alarm.** Rounded every entry in your Trainer's Pokédex and want to know if
  you broke something? Changed the training footage? Surprise moves *first*, before anything else you'd
  notice.

## Where it lies to you 🤥

**📚 Different scoreboards, different numbers.** A Trainer who reads the field in big chunks
naturally seems less surprised per chunk than one reading it piece by piece — not because they're
better, but because they're taking bigger bites. Comparing their scores directly is meaningless.

**🗺️ Different footage, different numbers.** Surprise on Gym battles and surprise on wild
encounters are different numbers about different things. Always say which footage.

**🎬 They may have seen the tape.** If the replay you're testing on was in their training footage,
of course they're not surprised. They memorised it. That score is worthless.

## The big one: unsurprised ≠ good 🎯

This is what actually matters, and it's the thing people get wrong.

Perplexity measures *"can you predict what a random Trainer does next."*

That is **not** the same as *"are you a good Trainer."*

```
   😐 Predicts the average Trainer perfectly.
      → Perfect score.
      → Also plays exactly like the average Trainer. Which is: fine. Mediocre.

   🏆 Plays like a Champion.
      → WORSE score! Champions don't play like average Trainers,
        so a Champion-minded Trainer is often "surprised" by
        ordinary play — because ordinary play is bad.
```

Here's the concrete version, and it's the fact worth remembering:

> **Coach your Trainer properly and their perplexity gets WORSE.**

Every time. Reliably. Coaching makes them decisive, opinionated, and willing to say "no, that's the
wrong move" — which makes them *worse at predicting what some random Trainer would have done*.

If you use perplexity to evaluate a coached Trainer, you will reject **exactly the coaching that
made them good.**

## Two more blind spots 🕳️

**🎭 It can't tell truth from confident nonsense.** *"Gyarados is weak to Electric"* and
*"Gyarados is weak to Grass"* can be equally unsurprising sentences. Fluency is not accuracy, and
perplexity only sees fluency.

**📋 It can't see whether they did what you asked.** You said "keep it under three moves." They
listed twelve, starting with Splash. Perplexity has no opinion about this whatsoever.

## The rule 📌

> **Use perplexity while raising the Trainer. Stop using it once you're coaching one.**

Superb during the grind. Genuinely useless as a measure of whether your finished Trainer is any
good. For that you need actual battles, real judges, and tests of the specific thing you're
building.
