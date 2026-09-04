---
id: "033"
slug: speculative-decoding
style: pokemon
category: inference
difficulty: advanced
question: "What is speculative decoding and why is it lossless?"
tags: [speculative-decoding, draft-model, medusa, eagle, rejection-sampling]
---

# Speculative decoding: let the rookie guess, let the Champion check

Here's the strange economics of a Champion.

Deciding **one** turn: Cynthia must flip through her entire enormous Pokédex. Slow.

Checking **five proposed turns**: it flips through the same Pokédex... once. Barely slower than
checking one.

The flipping is the cost. Once the book is open, five questions cost almost the same as one.

So: **have someone else propose five turns, and let the Champion check them all in one flip.**

## How it runs ⚡

```
  1️⃣ THE ROOKIE guesses ahead — fast, cheap, roughly right

      Position → "Thunderbolt, then switch to Ferrothorn, then Protect,
                  then Thunderbolt"

  2️⃣ THE CHAMPION checks all four AT ONCE — one flip through the book

      turn 1: Thunderbolt →  ✅ "yes, that's what I'd do"
      turn 2: switch      →  ✅ "yes"
      turn 3: Protect     →  ❌ "no — I'd use Substitute"
      turn 4: Thunderbolt →  🗑️ discarded (everything after a rejection is void)

  ✅ Result: 3 confirmed turns from ONE flip of the Pokédex.
```

Three turns for the price of one. That's the whole trick.

## Why the answer is *exactly* the Champion's 🎯

This is the part that matters, and it's easy to get wrong.

You might think: *"You're taking a rookie's guesses, so you're getting rookie-quality play."*

**No.** Every guess is checked. The rule is precise:

* Champion agrees → **keep it**. It's the Champion's own move; a rookie happened to say it first.
* Champion disagrees → **throw it out**, and the Champion plays *its* move instead.

And crucially, everything after a rejection is discarded too — because those guesses were built on
a turn that never happened.

So the final sequence of turns is, move for move, **exactly what the Champion would have played
alone**. Not similar. Identical.

Which leads to a genuinely lovely property:

> 🎲 **The rookie can be terrible and it still cannot hurt you.**

A useless rookie just gets rejected constantly, so you save no time. A great rookie gets accepted
constantly and you fly. Either way, **the play is Champion play**. You are risking *time*, never
*quality*.

## How much faster? 📈

Depends on how often the rookie is right:

```
  rookie right 90% of the time  →  ~4 turns per flip   🚀
  rookie right 80% of the time  →  ~3.4 turns per flip  ✅
  rookie right 50% of the time  →  ~1.9 turns per flip  😐
  rookie right 20% of the time  →  ~1.2 turns per flip  😬 barely worth it
```

And guessing further ahead isn't free: one early rejection voids the whole rest of the guess. Guess
four ahead and get turn 1 wrong, and you wasted four guesses. There's a sweet spot.

## Different rookies 🧑‍🎓

* 🐣 **A Pichu drafting for a Raichu.** Classic — same family, same instincts. Needs to speak the
  same language as the Champion, and you have to house a second Pokémon.
* ⏭️ **The Champion skimming.** Let the Champion skim the first few chapters only and guess from
  that. No second Pokémon at all.
* 🐍 **Extra heads.** Bolt a few extra "guess the next turn" instincts onto the Champion itself, so
  it proposes several turns simultaneously and then checks its own guesses.
* 🦅 **Guess in the Champion's own shorthand.** Instead of guessing *turns*, guess the half-formed
  thoughts the Champion has mid-flip. Much more accurate — the rookie is thinking in the
  Champion's language rather than translating.
* 📋 **Just copy from the briefing.** Underrated. If the task is "summarise the Toxapex report,"
  much of the output is already sitting in the report. Guess by copying. No rookie needed at all,
  and it works remarkably well.

## When it's useless ⚠️

**When the Champion is already busy.** This trick spends *spare* capacity — the Champion's idle
thinking while it flips pages. If it's already running three hundred battles at once, there's no
idle capacity to spend, and drafting just adds work.

It's a trick for making **one battle feel fast**, not for running **a thousand battles at scale**.
At scale it can actively make things worse.
