---
id: "077"
slug: mixed-precision-training
style: pokemon
category: systems
difficulty: intermediate
question: "What is mixed-precision training, and why is BF16 preferred over FP16?"
tags: [mixed-precision, fp16, bf16, loss-scaling, fp8, tensor-cores]
---

# Mixed precision: round the numbers, but not all of them

Recording every stat to seven decimal places is wasteful. Round them and everything is half the size
and several times faster.

But you can't round **everything**, and *which* things you round is the whole skill.

## Two ways to round 📏

Here's the crucial distinction, and it's not the one people expect.

You've got sixteen characters to write a number in. You can spend them two ways:

```
   📐 THE PRECISE FORMAT
      Records values from 0.00006 up to 65,504.
      Within that range: 4 good digits. Nice and exact.
      ⚠️  Outside that range: nothing. Just breaks.

   📏 THE WIDE FORMAT
      Records values from unimaginably tiny to unimaginably huge.
      Anywhere in that range: 3 digits. A bit rough.
      ✅  Never breaks.
```

Same budget. **Precise but narrow**, or **rough but unlimited**.

## Why precise-but-narrow is a nightmare 😱

Training feedback comes in a **wild** range of magnitudes. Some corrections are enormous. Some are
0.0000003.

The tiny ones fall **below the narrow format's floor** — and get recorded as **zero.**

Not "slightly wrong." Zero. That Pokémon received no feedback at all, and you'll never know.

The workaround people use is genuinely absurd: **multiply every piece of feedback by a thousand
before writing it down**, so the tiny ones climb into range — then divide by a thousand before
acting on it.

```
   feedback × 1000 ──► now it's in range ──► write it ──► ÷1000 ──► act
                            │
                    ...unless something OVERFLOWED,
                    in which case: halve the multiplier,
                    THROW AWAY this whole round, try again 🗑️
```

You have to tune the multiplier. You throw away work when it's wrong. And when it goes badly, your
run **quietly diverges** with no obvious cause.

## Why rough-but-unlimited wins 🏆

Nothing ever falls off either end. No multiplier. No thrown-away rounds. No tuning. Nothing to get
wrong.

You give up a digit of precision — and here's the thing: **training doesn't care.**

Training is already noisy, already approximate, already self-correcting. A slightly rough correction
followed by another slightly rough correction gets to the same place. The errors wash out.

> 📌 **For training, RANGE matters far more than PRECISION.**

That's the whole insight, and it's why every modern setup uses the wide format.

## What you must NOT round 🚫

Round the wrong thing and training silently stops.

**📓 The official stat records.** Here's why this one is critical:

```
   Pikachu's Attack:              55.000000
   This week's adjustment:         0.0000004

   In the rough format:  55.0 + 0.0000004 = 55.0
                                             ▲
                              THE ADJUSTMENT VANISHED.
```

Every week. Forever. Your Pokémon **never improves at all**, and every number on your dashboard looks
completely normal.

Keep the official records **precise**. Do the fast rough work on a copy.

**📊 The trend notebooks.** Same reason — they accumulate tiny amounts over thousands of weeks.

**➕ Anything that adds up a lot of numbers.** Add ten thousand rough numbers and the errors compound.
Add them precisely, *then* round the result.

## The pattern 🎯

```
   ⚡ ROUGH — the heavy lifting        📐 PRECISE — the bookkeeping
   ──────────────────────             ────────────────────────────
   Comparing Pokémon                  The official stat records
   Working out matchups               The trend notebooks
   Passing feedback around            Running totals
                                      Final scores
```

Round the **work**. Keep the **books** exact.

## Going further 🗜️

Newer setups round even harder — eight characters instead of sixteen, sometimes fewer. It works, and
it needs careful per-page scaling notes to stop things falling off the ends again.

The direction is consistent: **progressively rougher, with progressively more careful bookkeeping
around it.** Nobody expects that to stop.
