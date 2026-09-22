---
id: "255"
slug: tree-drafting-and-verification
style: pokemon
category: optimization
difficulty: advanced
question: "What does verifying a tree of candidates instead of a single chain buy you?"
tags: [speculative-decoding, tree-attention, medusa, eagle, acceptance-rate]
---

# It buys depth: one guess dies at the first thing you called wrong, a fan of guesses does not.

Plan a run of four casts as a single line — Carvanha, Carvanha, Carvanha, Carvanha — and the whole
plan dies the first time a **Sharpedo** comes up. Plan it as a **fan** instead, where every cast
carries two names rather than one, and you are not asking "did I name the right thing?" but "was
the thing that came up *anywhere on my list?*" — which is a much bigger number, and it keeps being
a bigger number four casts deep instead of falling apart at cast two.

The cost is that the whole fan has to be checked on one trip out to **Route 119**, and a trip only
holds so much. Widening the fan is the cleanest way to turn a quiet afternoon into fish. It is
worth nothing at all on an afternoon that was never quiet — which is
[256](256-speculative-decoding-at-high-batch.md).

## Whose preparation counts where

```
   one plan, four casts deep          a fan, two names at each of three casts
   ────────────────────────           ──────────────────────────────────────
   [where you stand]                              [where you stand]
     Carvanha                                     /              \
     Carvanha                              Carvanha            Sharpedo
     Carvanha                             /       \            /       \
     Carvanha                       Carvanha   Sharpedo  Carvanha   Sharpedo
                                      / \        / \        / \        / \
   one line of four                   C   S      C   S      C   S      C   S

                                     14 named guesses, checked on ONE trip

   what each guess may lean on

            here  Carv Shar  Carv Shar Carv Shar ...
    Carv     1     1    .     .    .    .    .        every guess leans on where
    Shar     1     .    1     .    .    .    .        you started, and on the
    Carv     1     1    .     1    .    .    .        guesses above it — nothing else
    Shar     1     1    .     .    1    .    .
    Carv     1     .    1     .    .    1    .        the two branches never
    Shar     1     .    1     .    .    .    1        borrow from each other
```

Two things fall out of that picture. A **Net Ball** you readied for the **Carvanha** branch is no
use at all on a branch that opens with **Zigzagoon** — the Net Ball is the right Ball for a
Water-type and nothing special against a Normal-type, and the branches are separate runs of the
same afternoon with no preparation crossing between them. And a guess two levels down is the
**second cast**, not the sixth name on your list: if you count its place in the list instead of
its depth in the fan, you have it standing at the wrong distance from where you started and every
guess below it is wrong too.

## The arithmetic, and why you cannot fan out all the way

What a fan is worth is the sum, over every name on it, of the chance that the day actually goes
that way:

```
   what the fan is worth  =  Σ        P(the day follows that branch to that name)
                            names
```

Take the grass instead of the water, because the grass is where the tail is long. **Route 119**'s
**Tall Grass** draws one of twelve slots and the twelve are not equal. Two sit at 20% — a level-25
**Zigzagoon** and a level-25 **Linoone**. Four sit at 10%: another Zigzagoon, another Linoone and
two **Oddish**. Two more Oddish take 5% each, two **Tropius** take 4% each, and the last two slots
are worth 1% apiece — a third Tropius, and a single **Kecleon**, which is what a long tail looks
like. Cover the top slot and you have 20% of the route; the top two, 40%; four, 60%; six, 80%;
eight, 90%; ten, 98%; and only all twelve reaches 100. Now price a full fan four encounters deep:

```
    names per step   share of the grass covered   names in the fan   worth
   ─────────────────────────────────────────────────────────────────────────────────
         1                     0.20                        4         0.250   one plan
         2                     0.40                       30         0.650
         4                     0.60                      340         1.306
         6                     0.80                    1,554         2.362
         8                     0.90                    4,680         3.095
        10                     0.98                   11,110         3.804
        12                     1.00                   22,620         4.000   never wrong
   ─────────────────────────────────────────────────────────────────────────────────
```

Twelve times the fish for five thousand times the names to carry. Nobody has that many Balls,
which is why you **prune**: keep the branches the day is most likely to actually take, and cut the
rest. Doing exactly that, best branches first:

```
   names you can carry      4      8     16     32     64    128    256
   what the fan is worth  0.600  0.900  1.180  1.480  1.784  2.088  2.394
```

Look at the first column beside the single plan's 0.250. With the *same four names*, the pruned
fan is worth 0.600 — because it spends all four on **width at the first encounter** instead of on
a fourth encounter it will almost never reach. That is the least obvious thing here and it is why
a good fan is broad at the top and thin at the bottom.

Now do it again in water that barely varies. **Route 118**'s **Super Rod** is **Carvanha** 60% and
**Sharpedo** 40% and nothing else at all:

```
   names you can carry      4      8     16     32     64
   what the fan is worth  1.600  2.360  3.238  4.000  4.000    one plan would give 1.306
```

It tops out at 32 names: a full two-name fan four casts deep is 30 names, both names cover the
whole table at every cast, and you are never once wrong. How wide to fan out is decided by how
long the tail is where you are standing. A 1% **Kecleon** in Route 119's grass and a 40%
**Sharpedo** in Route 118's water are the two ends of that, and they are twenty paces apart.

## Fanning out without breaking the keep rule

If you only ever want the single most likely thing, this is easy: walk down the fan and keep the
branch that matches. If you are drawing properly from the table, it needs the care from
[253](253-speculative-decoding-exactness.md), because "keep whichever name matched" is not that
rule. The honest version is to try the first name by the usual keep rule; if you throw it back,
subtract what that name already accounted for, re-weigh what is left, and try the second name
against *that*; and if every name on the branch fails, draw from what remains. Done that way the
fan changes nothing about what ends up in your **Poké Ball**s. The shortcut — "it was close
enough, keep it" — is a different rule, and worth knowing which one the hall you are fishing in
runs.

## What the halls actually do

Read this off the halls, not off the noticeboard, because they disagree. One of the big halls will
genuinely let you fan out: you set how many names per step and it lays the whole fan out for the
trip. But its clever feature that watches how the day is going and adjusts *how far ahead* you
plan **refuses to run unless the fan is one name wide** — so you may have width or you may have
self-adjusting depth, and today you pick. Another hall plans in a single line only; the note in
its own workings says, in so many words, that the fan is not finished yet. Fanning out is old and
well-understood and unevenly built.

## What a Gym Leader is listening for

* Why is a four-name fan worth more than a four-cast plan, and what does that say about its shape?
* Why must a guess be counted by its depth in the fan rather than its place in the list?
* How do you fan out without changing what ends up in the Ball?

## Where this stands, September 2026

The sums are permanent. The worth of a fan is the sum over its branches, full fans blow up faster
than anyone can carry, and the right width follows the tail of the water you are standing in —
none of that belongs to a generation. The twelve slots and the 60/40 are read straight off the
routes and will still read that way. What will move is the halls: which one lets you fan out,
which one only plans in a line, and the rule that you cannot have width and self-adjusting depth
at once. That last one is exactly the sort of thing that gets quietly fixed. Check the hall before
you plan around it.
