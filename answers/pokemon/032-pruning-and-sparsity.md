---
id: "032"
slug: pruning-and-sparsity
style: pokemon
category: inference
difficulty: advanced
question: "What are pruning and sparsity, and why is unstructured sparsity hard to exploit?"
tags: [pruning, sparsity, lottery-ticket, structured, wanda, sparsegpt]
---

# Pruning: cutting entries out of the Pokédex

Your Pokédex has entries you never read. You are never going to look up Unown's form variants
mid-battle. Cut them out and the book gets thinner and faster to flip. Simple idea.

The catch — and it's the whole question — is **how you cut**.

## Three ways to cut 📕✂️

```
  ✂️ SNIP INDIVIDUAL LINES        ✂️ TWO PER FOUR             ✂️ TEAR OUT WHOLE PAGES
  ────────────────────────        ───────────────             ─────────────────────
  ▓ · ▓ · · ▓ · ·                 ▓ ▓ · ·  ▓ · ▓ ·            ▓▓▓▓▓▓▓▓
  · ▓ · ▓ ▓ · · ▓                 · ▓ ▓ ·  ▓ ▓ · ·            ▓▓▓▓▓▓▓▓
  ▓ · · · ▓ · ▓ ·                 ▓ · · ▓  · ▓ ▓ ·            ←── page gone
  · · ▓ ▓ · ▓ · ▓                 · · ▓ ▓  ▓ · · ▓            ▓▓▓▓▓▓▓▓

  Keeps the most knowledge.       Exactly 2 of every 4.       Loses the most knowledge.
  ZERO speedup. 😤                 Genuinely ~2× faster.       Real speedup, anywhere.
```

## Why snipping individual lines does nothing 🤯

This is the counterintuitive bit and the point of the question.

You snipped 90% of the lines. The book has 90% less *content*. It should be ten times faster to
use, right?

**No.** Because of *how you flip a book*.

You don't read line by line. You grab a **thick wedge of pages at a time** — that's the only fast
way to move through a book. And a wedge that's 90% holes is exactly as thick as a wedge that's
full. You still lift it, you still turn it, you still scan it.

Worse: now every line needs a little margin note saying which entry it *was*, since the numbering
is full of gaps. Those notes cost space and slow down every lookup.

📌 **A book full of holes is the same size as a full book.** Speed comes from how much you
*physically move*, not how much information is in it. Removing knowledge without removing bulk
buys you nothing.

## The compromise that works 📐

**Exactly two of every four lines.** Rigid, no exceptions.

Now the rule is so regular that you can print a **genuinely half-thickness edition** — no margin
notes needed, because "two of every four" tells you where everything is. The wedge really is half
as thick, and you really do flip twice as fast.

You give up choosing *which* lines to cut (you must drop exactly two from each group of four, even
if all four mattered). In exchange you get a speedup that actually exists. This is the sweet spot,
and it needs a book printer that supports the format.

## Tearing out whole pages 📄

Rip out entire chapters — the whole Bug-type section, say.

Costs the most knowledge: some of those Bug entries were useful, and now they're gone entirely.

But the book is **genuinely thinner**. No special printing, no margin notes, no clever formats.
It's just a smaller book, and a smaller book is faster everywhere, always.

This is what people actually ship.

## Choosing what to cut 🎯

* 📏 **Cut the shortest entries.** Crude. Works better than it has any right to.
* 🔍 **Cut what you never look up.** Much better. A long entry you never consult is worthless; a
  one-line entry you check every turn is critical. **Measure how often each entry is actually
  read**, not how big it is.
* 🧮 **Cut carefully, and patch as you go.** Cut an entry, notice what got lost, and **edit the
  neighbouring entries** to cover the gap. Slow, best results.

## The famous theory 🎟️

There's a beautiful result called the **lottery ticket**: hidden inside every fat Pokédex is a tiny
subset of entries that — if you'd started with just those, from day one — would have been as good
as the whole book.

Genuinely fascinating. Almost useless in practice: to find the winning ticket you must first write
the entire fat book. Cite it as theory, not as a plan.

## Where this all landed 🏁

Honestly? **Pruning lost.**

**Rounding the entries** gives you a book a quarter the size with almost no knowledge lost, needs
no exotic printing, and works everywhere. Cutting entries gives you either no speedup (snipping) or
real knowledge loss (tearing pages).

The one place the *idea* genuinely won is the **Gym Leader roster** — keep Brock, Misty and sixty
others on the payroll, but only ever open the two volumes you need for this challenger. That's sparsity done
right: you're not deleting knowledge, you're just not *consulting* most of it. Chosen fresh every
time, instead of decided once with scissors.
