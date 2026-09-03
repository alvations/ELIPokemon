---
id: "035"
slug: beam-search
style: pokemon
category: inference
difficulty: intermediate
question: "What is beam search and why is it rarely used for open-ended chat?"
tags: [beam-search, decoding, likelihood-trap, translation, degeneration]
---

# Beam search: keeping several game plans alive

Greedy play commits to the best move *right now*, every turn, and never looks back. Usually fine.
Sometimes it walks you into a trap that was visible two turns earlier.

Beam search says: **carry three plans forward instead of one.**

```
  Turn 1        Turn 2              Turn 3
  ──────        ──────              ──────
  Thunderbolt ──┬── then switch ────┬── then Protect     ✅ best overall
   (looks best) │                   └── then attack
                └── then attack ────┬── ...
                                    └── ...
  Switch ────── ✂️ dropped (3rd best after turn 2)
   (looks worse)

  At every turn: keep only the 3 best PLANS. Prune the rest.
```

You're not evaluating moves any more. You're evaluating **whole plans**, and only pruning once
you've seen where each one goes.

## The bookkeeping trap 📏

Every extra turn in a plan makes it *look* slightly worse — more turns, more chances for something
to go wrong. So the raw scoring quietly favours plans that end quickly.

Left uncorrected, your Pokémon starts preferring "attack once and hope" over any actual strategy.
You have to explicitly correct for plan length, and getting that correction wrong is a classic bug:
too little and everything ends in two turns, too much and your Pokémon plans a forty-turn epic
against a wild Rattata.

## Where it genuinely shines 🏆

**Translating a battle log into another language.** There's one right answer. You want the *best*
rendering, and carrying several candidate phrasings forward genuinely finds it.

**Transcribing commentary.** Same deal — one correct transcript, and hearing the next few words
often resolves an earlier ambiguity.

These tasks are **narrow**. One target, and the goal really is to find it.

## Why it's wrong for actual battling 😴

Here's the thing that makes this question interesting.

In an open battle there isn't *one* right plan. There are forty decent ones. And when you search
hard for the single "most likely" plan, you get something specific and bad:

> **The safest possible sequence of moves.**

Not the strongest. The *safest*. Attack, attack, attack, attack. Never a risk, never a read, never
a surprise. It's the play of someone who has optimised out every interesting decision.

```
   how surprising each turn is

   🏆 a real Champion:   ▂▅▁▇▃▂▆▁▄▇▂▅▁▃    varied — sometimes bold,
                                            sometimes obvious

   😴 beam search:       ▂▂▁▂▂▁▂▂▂▁▂▂▂▂    uniformly safe. Every turn.
                                            Forever.
```

This is the trap: **searching harder for the "best" plan makes the play worse.** Real strength
involves the occasional unexpected move, and an algorithm dedicated to never being surprising will
never make one.

There's a second problem. Your three plans, after all that searching? They're nearly identical —
"Thunderbolt then switch," "Thunderbolt then attack," "Thunderbolt then Protect." You paid triple
to explore three shades of the same idea.

## What people do instead 🎯

**Play the whole battle five times, with variety turned on. Then pick the best one.**

```
   ✂️ BEAM SEARCH                    🎲 SAMPLE THEN PICK
   ──────────────                    ───────────────────
   Prune as you go, keeping          Play five COMPLETE battles,
   whatever looks best so far.       each genuinely different.
                                     Then judge the finished five.

   Exploring and judging are         Exploring and judging are
   tangled together — and you        SEPARATE. You never prune a
   prune plans before seeing         plan before seeing how it ends.
   how they end.
```

That separation is the whole improvement. Beam search has to judge a half-finished plan, and
half-finished plans all look about the same. Letting each one finish first means you're judging
actual outcomes.

## Where beam search survives 📌

* 📐 When the output must fit an **exact required shape**, and you need to search for one that does.
* 🔢 Short, structured answers with **one correct form**.
* 🎯 Anything with **one right answer and a scorer you trust**.

For "have a conversation" or "come up with something good"? Sample, then judge. Every time.
