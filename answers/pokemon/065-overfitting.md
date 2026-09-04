---
id: "065"
slug: overfitting
style: pokemon
category: fundamentals
difficulty: core
question: "What is overfitting, how do you detect it, and how do you prevent it?"
tags: [overfitting, regularisation, early-stopping, leakage, validation]
---

# Overfitting: your Trainer memorised the practice opponents

Your Trainer is **undefeated** in practice. Not one loss.

They enter a real tournament and lose in round one.

They didn't learn to battle. They learned **these specific opponents** — that Brock leads Geodude
and switches to Onix, that Misty's Starmie clicks Protect on turn one. Flawless recall of forty
matches that will
never happen again.

## Watching it happen 📉

```
   losses │
          │ ╲                                    ╱ 🏟️ real matches
          │  ╲                            ____╱
          │   ╲___                   ___╱
          │       ‾‾‾───────────────╱
          │            ▲
          │            │ ⬅ STOP HERE
          │  ╲         │
          │   ╲________│________________________ 📼 practice
          └────────────────────────────────────────► weeks of training
```

Both improve at first — that's real learning. Then practice keeps improving while real matches get
**worse**. That crossing point is where learning stopped and memorising began.

📌 **The gap between practice and real is the whole signal.** Watch both, always. Watch only practice
and you'll train straight past the peak, feeling great about it.

## How to catch it 🔍

* 📊 **Track both curves.** The moment real-match performance turns upward, you've gone too far.
* 📈 **Does more footage still help?** If real-match losses are still dropping as you add matches,
  get more matches. If both curves flattened out together at a bad number, you don't have a
  memorising problem — you have a **too-simple Trainer**, and more footage won't touch it.
* 🎲 **The scrambled-tape test.** Take your practice footage and **shuffle the results randomly** —
  label wins as losses, nonsense. Then train.

  If your Trainer "learns" that too? It has the raw memory to memorise anything you show it. Which
  means the only thing standing between you and pure memorisation is how carefully you train.

## How to prevent it 🛡️

**📼 More footage.** The only free fix. Nobody memorises a million matches.

**🎭 Vary the footage.** Same matches, different arena, different weather, different lighting. Forces
attention onto what actually matters.

**🛑 Stop earlier.** Genuinely. The simplest and most effective intervention available, and the one
people resist because the practice numbers are still improving.

**🎒 Simplify the Trainer.** Less capacity, less room to memorise.

**👥 Train several and average them.** Their individual superstitions cancel out.

**🔒 Keep one tournament they NEVER see.** And touch it **once.** The moment you start tuning against
it, it's practice footage — you've just given it a fancier name.

## The plot twist: usually it isn't memorising 🕵️

Here's what actually happens most of the time in real work. It's not memorisation. **It's cheating** —
and no amount of stopping early or simplifying will fix it.

**🔮 A feature from the future.** You're predicting which Pokémon will faint, and one of your
inputs is `revive_used` — whether someone threw a Max Revive at it afterwards. Of *course* you're
at 100%. That field only gets filled in **after** the Pokémon
faints. It won't exist when you actually need to predict.

**📅 Practising on tomorrow.** You split your footage randomly — so your Trainer studied June and
July, and is now being "tested" on a match from **June**. It's not predicting. It's remembering. For
anything time-ordered, **split by date**, always.

**👥 The same opponent in both piles.** Brock's matches ended up in practice *and* in your test
set — his Geodude in one, his Onix in the other.
Your Trainer knows Brock. Split by **opponent**, not by match.

**🧪 Preparing the footage before splitting.** You normalised, cleaned, and indexed everything, *then*
split it. The preparation already saw the test matches. Split first. Always.

## The rule that saves you 🚨

> **An unbelievably good score is a bug report, not a result.**

99% win rate? Do not celebrate. **Investigate.** And go straight to the feature that's doing all the
work — when one input dominates implausibly, that's your leak, nine times out of ten.
