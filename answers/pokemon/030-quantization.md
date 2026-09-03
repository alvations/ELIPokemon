---
id: "030"
slug: quantization
style: pokemon
category: inference
difficulty: core
question: "What is quantization and what are the tradeoffs between INT8, INT4 and FP8?"
tags: [quantization, gptq, awq, int8, fp8, outliers]
---

# Quantization is rounding off your Pokédex

Your Pokédex records Pikachu's Attack as **55.0000000**.

Did you need seven decimal places? You did not. **55** would have been fine. Round every entry in
the book and it becomes a quarter as thick.

Why that matters: the slow part of using a Pokédex isn't the thinking — it's **flipping through
it**. Every single move, you flip the whole book. Make the book a quarter as thick and you flip
four times faster.

Quantization is a speed trick disguised as a storage trick.

## How much rounding? 📏

```
   📕 FULL DETAIL     55.0000000    the original. Heavy.
   📗 HALF            55.0          basically free. Everyone does this.
   📘 QUARTER         55            noticeably lighter, still fine.
   📙 EIGHTH          "about 56"    lighter still — needs real care.
   📓 SIXTEENTH       "medium-ish"  now you're guessing.
```

Most teams live at 📘 or 📙. Below that you're not compressing information, you're discarding it.

## The problem: the Blissey 🥚

Here's what actually makes this hard, and it's not obvious.

You'd like one rounding rule for the whole page. But stats don't sit in a tidy range:

```
   Attack values on this page:

   |███|                                  ← Blissey's HP: 255
   |███|
   |███|
   |███|   ▁▁▂▁▁▂▁▁▁▂▁▁▂▁▁▁▂▁▁▂▁▁▁▂      ← almost everyone else: 40–90
   └───────────────────────────────────►
```

To fit 255 on the same scale as everyone else, your marks end up spaced so far apart that
**every normal Pokémon on the page rounds to the same two or three values.**

One outlier just destroyed the entire page. This is the whole difficulty.

## Four ways to handle the Blissey 🛠️

* 🎯 **Give it its own page.** Write the freaks out in full detail and round everyone else
  aggressively. It's only about 1% of entries, so you keep nearly all the savings.
* ⚖️ **Spread the weirdness.** If one column has extreme values and its neighbour is tame,
  rebalance between them so neither is extreme. Move the difficulty to where it's cheaper to
  handle.
* 🔍 **Protect what gets *used*, not what's *big*.** The clever one. A huge number that's never
  consulted doesn't matter. A modest number that's consulted every single turn matters enormously.
  Identify the entries that actually get read a lot and guard those.
* 🧮 **Round one column at a time, and adjust as you go.** Round column 1, notice you rounded
  slightly high, then **nudge the remaining columns down to compensate**. Errors cancel instead of
  accumulating. Slow to prepare, very accurate.

## Two different things you might be optimising ⚡

**📖 Just shrink the book.** Round the stored entries, but when you actually *use* one, expand it
back to full detail for the calculation.

You get the entire flipping speedup — which is everything, when you're consulting one entry per
turn. You get no calculation speedup, but you weren't calculation-limited anyway.

**🧮 Round the calculations too.** Now you're doing arithmetic in shorthand as well. This only pays
off when you're doing *masses* of arithmetic at once — a huge tournament, hundreds of battles in
parallel — where thinking, not flipping, is finally the bottleneck.

Which one you want depends entirely on whether you're running **one battle** or **a thousand**.

## The trap 🕳️

Round your Pokédex, then check it: *"What type is Charizard?"* Correct. *"What beats Water?"*
Correct. Everything looks fine. Ship it.

Then in a tournament your Pokémon falls apart on a **six-step endgame calculation**.

Simple lookups survive rounding beautifully. It's the **long chains** that die — each step
inherits the last step's rounding error, and by step six you're nowhere near the right answer.

📌 **Test the hard things.** Rounding damage doesn't show up on easy questions. Multi-step
reasoning, long battles, rare matchups — that's where it hides.

And note: **big Pokémon survive rounding far better than small ones.** A Champion has enough
redundancy to shrug off imprecision. A rookie was already using every bit of what it knew, and
rounding takes it straight out.
