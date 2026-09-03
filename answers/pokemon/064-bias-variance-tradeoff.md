---
id: "064"
slug: bias-variance-tradeoff
style: pokemon
category: fundamentals
difficulty: core
question: "Explain the bias-variance tradeoff."
tags: [bias-variance, overfitting, double-descent, generalisation]
---

# Bias and variance: two ways to be a bad Trainer

## 🪨 The One-Trick Trainer — high bias

Their entire strategy: **"always lead with Onix."**

Rain? Onix. Sun? Onix. Facing a Water team? Onix.

They are wrong in the *same way* every single time. Train them on new footage, hire a new coach,
change leagues — still Onix. Their problem isn't inconsistency. It's that their whole worldview is
too simple to contain the game.

**They're consistently wrong.**

## 🎪 The Superstitious Trainer — high variance

They remember **everything.**

> *"Last Tuesday, against a Trainer in a red hat, on a Tuesday, my Pikachu won with Quick Attack. So:
> red hat, Tuesday → Quick Attack."*

They memorised their practice matches **perfectly** — down to the weather and what everyone was
wearing. And they cannot handle a single new opponent, because no new opponent matches any
memorised pattern exactly.

Retrain them on a *different* set of practice matches and you get a **completely different Trainer**
with completely different superstitions.

**They're inconsistently wrong.**

## 🌫️ And some things are nobody's fault

Moves miss. Critical hits happen. Some of every loss is dice.

No Trainer removes this. If someone claims a perfect record, **they've seen the opponent's team
sheet** — that's not skill, that's a leak.

## The curve 📉

```
   how │  ╲                                        ╱
  wrong│   ╲         total                       ╱
       │    ╲___                            ___╱
       │        ‾‾‾‾───────────────────────╱
       │   ╲                             ╱
       │    ╲ 🪨 one-trick             ╱  🎪 superstitious
       │     ╲___                    ╱
       │         ‾‾‾───────────────╱
       └────────────────────────────────────────────────►
        too simple          ▲                too complex
                     the good Trainer
```

## Diagnosing yours 🔍

| Practice | Real matches | What's wrong | Fix |
| --- | --- | --- | --- |
| 😞 bad | 😞 bad | 🪨 too simple | more capacity, better training, longer |
| 😄 great | 😞 bad | 🎪 memorising | more footage, simplify, stop earlier |
| 😄 great | 😄 great | ✅ nothing | enter the tournament |
| 😞 bad | 😄 great | 🐛 **bug** | you've mixed up your footage. Check. |

That last row is not a happy result. Doing *better* on real matches than on practice means your
practice and real sets got tangled. Go and look.

## The one free improvement 🎁

**More footage.**

Everything else is a trade. Simplify the Trainer and you cure superstition but risk one-trick.
Regularise harder, same deal.

**More real footage cures superstition and costs nothing.** You can't memorise a million matches, so
you're forced to find the actual patterns. It's the only lever with no downside — which is why the
answer to "how do we make this better" is so often "get more data."

## The twist that broke the story 🤯

The neat U-curve above was the accepted picture for decades. Then people built **enormously**
overcomplicated Trainers and something odd happened.

```
   how  │    ╲       ╱‾╲
  wrong │     ╲    ╱    ╲
        │      ╲__╱      ╲___
        │                     ‾‾‾‾───────────
        └──────────────┬──────────────────────►  complexity
           the classic U   ▲          it gets GOOD again?!
                  "just barely enough
                   memory to memorise
                   everything"
```

The worst possible Trainer is the one with **exactly enough memory to memorise every practice match
and not a scrap more.** They memorise, badly, with nothing left over.

Give them **vastly more** memory and they get better again. With room to spare, they stop
memorising and start noticing the actual patterns — there are simply more good ways to remember than
bad ones, and training tends to find them.

📌 This is why enormous modern Trainers work at all. By the classical story they should be
catastrophically superstitious. They aren't. The tradeoff is still the right way to think about
ordinary Trainers — it just isn't the whole story any more.
