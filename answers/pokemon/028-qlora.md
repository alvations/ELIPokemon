---
id: "028"
slug: qlora
style: pokemon
category: fine-tuning
difficulty: intermediate
question: "What is QLoRA and how does it combine 4-bit quantization with LoRA?"
tags: [qlora, nf4, double-quantization, paged-optimizers, peft]
---

# QLoRA: a compressed Champion with a full-precision item

The held-item trick solved one problem: you no longer need a whole facility to *retrain* a
Champion. But you've still got the problem that **a Champion is enormous** and has to physically
fit in your gym.

QLoRA's move: **compress the Champion, keep the item at full fidelity.**

```
   ┌────────────────────────────────────────────────────────────┐
   │  🗜️ YOUR GARCHOMP — compressed, frozen                     │
   │     Every stat stored in shorthand.                        │
   │     Never edited. Never even unpacked, permanently.        │
   │                                                            │
   │     When it needs to act:                                  │
   │        shorthand → unpack that one stat → use it → discard │
   │                                                            │
   │                          ➕                                 │
   │  ┌──────────────────────────────────────────────────────┐  │
   │  │  🎒 THE LEFTOVERS — full detail, trainable ✅        │  │
   │  │     Tiny. Never compressed. This is what learns.     │  │
   │  └──────────────────────────────────────────────────────┘  │
   └────────────────────────────────────────────────────────────┘
```

The Garchomp is never edited, so storing it in shorthand costs nothing. The Leftovers is what's
actually learning, so it stays in full detail. Perfect division of labour.

## The clever part of the shorthand 📝

You could write every stat with the same coarse rounding. That's wasteful, and here's why.

Pokémon stats aren't spread evenly. **Almost everything clusters between 40 and 90**, with a
handful of freaks at the edges — Blissey's 255 HP, Shuckle's 230 Defence, Magikarp's 10 Attack:

```
   how many stats have each value:

                        ██████████
                    ██████████████████
                ██████████████████████████
        ▁▁▁▁▂▂▄▆████████████████████████████▆▄▂▂▁▁▁▁
        ────┼───────────────┼───────────────┼────
          extreme          typical        extreme
          (rare)          (very common)    (rare)
```

So don't space your shorthand marks evenly. **Put lots of marks where the stats actually are**,
and only a couple out at the extremes.

Sixteen shorthand marks, positioned so each one gets used about equally often. Same storage, far
less rounding error, because you stopped wasting marks on ranges nothing occupies.

## Shorthand for the shorthand 🪆

Small detail, real savings. The shorthand works in **little batches of 64 stats**, and each batch
needs a note recording its own scale. Those notes add up — at that batch size they're costing you
an eighth of a stat's worth of space, *each*.

So: compress the notes too. Slightly coarser notes, no measurable harm, several gigabytes back.

## The safety net 🛟

One more thing, and it's the difference between a technique and a technique that finishes.

Training has memory *spikes* — brief moments where you need much more room than usual. Without a
plan, a spike at hour 40 of a 48-hour run means the whole run dies.

So: when the gym gets too crowded, **temporarily move some equipment out to the shed**. Slower for
a moment. But the run *finishes*, and that's the entire point.

## What it costs 💸

**⏱️ Slower.** Every time the Champion acts, you unpack a stat from shorthand. That's real
overhead — call it 20-40%.

But hold on: the alternative isn't "the same thing, faster." The alternative is **it doesn't fit
in your gym at all.** A slower run beats no run.

**📉 The starting point is slightly worse.** Compression loses a little. Straight out of the box,
the compressed Champion is a touch duller than the original.

The interesting part: after training, the finished result is **just as good**. The item learns to
compensate for the rounding. Worse starting point, same finish line.

**🔗 Fusing is awkward.** You can't cleanly fuse a full-detail item into a compressed Champion —
you'd have to re-compress, and lose the item's precision doing it. So people usually just keep the
item held, or fuse it into an uncompressed copy.

## The one thing people mix up 📌

QLoRA is for **fitting training into your gym**. That's the problem it solves.

It is *not* how you make a Champion fast in tournaments. Competition compression is a different
technique with different priorities — there you're optimising for speed under battle conditions,
not for squeezing a training run onto one machine.
