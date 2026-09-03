---
id: "010"
slug: flash-attention
style: pokemon
category: systems
difficulty: advanced
question: "What is FlashAttention and why is it faster without changing the math?"
tags: [flashattention, io-aware, tiling, online-softmax, hbm-sram]
---

# FlashAttention: stop walking to the PC box

Your Pokémon are in two places. Six on your **belt** — instant access, but only six. Everything
else is in the **PC box at the Pokémon Center**, which holds thousands but requires walking
across town every time you want one.

```
   🎒 THE BELT          6 slots        instant
   ──────────────────────────────────────────────
   💻 THE PC BOX        thousands      a walk across town, each time
```

## How the rookie scouts a tournament 🐌

You need to compare all your Pokémon against all forty of the opponent's.

The rookie does this:

1. Walk to the PC. Compute every matchup. **Write all 240 results onto a giant poster.**
2. Walk to the PC. **Read the poster back.** Work out the percentages. Write a *second* poster.
3. Walk to the PC. **Read that poster back.** Finally compute the answer.

The comparisons themselves take seconds. The three trips across town — and the enormous posters
you have to store somewhere — take all afternoon. And the posters get *quadratically* bigger:
forty Pokémon is manageable, eight thousand and you're papering the entire Center.

## How the pro does it ⚡

Never write the poster at all.

```
   Grab 6 of yours onto the belt.        ← stays on the belt the whole time
   ┌─────────────────────────────────────────────────────┐
   │  for each batch of 6 enemy Pokémon:                 │
   │      pull them out                                  │
   │      compare — right there, on the spot             │
   │      UPDATE the running tally                       │
   │      put them back                                  │
   └─────────────────────────────────────────────────────┘
   Write down ONE final answer. One trip.
```

Same comparisons. Same arithmetic. Same answer. You just never manifested the poster.

## But wait — the percentages 🤔

Here's the real obstacle. To turn matchup scores into percentages you have to divide by the
total, and **you don't know the total until you've seen everyone**. The rookie's whole excuse
for the giant poster was needing the full picture first.

The pro's trick: **keep a running tally and fix it as you go.**

You're partway through and your best matchup so far scores 40. Then batch seven produces a
monster scoring 900. The rookie would say "well, everything I computed is now wrong."

The pro says: *"Everything so far was measured against 40. The new bar is 900. So scale
everything I've already got down by exactly that much, then add the new one."* One correction,
applied to the running tally.

By the last batch your tally has been rescaled a handful of times and lands on **precisely** the
number the giant poster would have given. Not an approximation. The identical answer.

This is the whole thing. It is not a shortcut, a heuristic, or a cheaper approximation of
attention. It is the same computation with the pointless walking removed.

## The bit that sounds backwards 🔄

When you review the tournament afterward to learn from it, you need those matchup numbers again.
Do you keep the poster after all?

No — you **recompute them from scratch**. Redoing the comparisons is *faster than fetching the
stored ones*, because the walk to the PC is that dominant.

That's genuinely counterintuitive and it's the most important lesson here: on this hardware,
**redoing work can be cheaper than remembering it**. When something's slow, ask whether you're
thinking-limited or walking-limited. Almost always, you're walking-limited.

## One caveat 📌

This wins big when you're scouting a whole roster at once. During turn-by-turn play, when you
only have *one* new Pokémon to compare against your notebook, there was never a giant poster to
avoid. Different bottleneck, different fix.
