---
id: "269"
slug: flashattention-to-flashinfer
style: pokemon
category: optimization
difficulty: advanced
question: "FlashAttention already fuses attention into one kernel. What does a serving kernel library like FlashInfer have to do that a single fused kernel does not?"
tags: [flashattention, flashinfer, kernels, paged-attention, jit]
---

# The damage formula solved one attack. A League reception desk never sees the same one twice.

The damage formula is a promise about **paperwork**, not about outcomes. Nobody has ever written
down a table of what every move does to every Pokémon, because nobody needs to: the same
**Flamethrower** from the same **Charizard** into the same **Venusaur** produces the same number
every time, whether you sat through the animation or had them switched off in the options. The
formula is the answer. Writing out the table is optional, and enormously expensive.

That is a complete account of one attack. The desk at the **Indigo Plateau** has a different
problem: **every challenger arrives a different number of turns into a different run, and the
clerk has to be quick anyway.**

## What not writing the table saves, in pages

Take the walk from [268](268-roofline-decode-and-prefill.md): 8,192 turns, 64 watchers, 80
stretches. Writing down what each of your 8,192 turns would do to each of their 8,192 turns costs

```
   8,192 × 8,192 entries × 64 watchers × 2 pages  =  8.59 M pages   per stretch
   written once, read to compare, written, read again      ≈ 25.8 M pages
   × 80 stretches                                          ≈ 2.06 billion pages

   against 143.8 thousand pages for the entire walk when the table is never written.
```

Roughly **15× the paperwork of the whole trip**, to record a number that is thrown away the
instant the turn resolves. That alone would turn a trip that was limited by your throwing arm into
one limited by your feet. So you do what the formula does: take the opposing turns a stack at a
time, carry a running total, and rescale it the moment a stack beats your previous best.

```
   for each stack of their turns you pick up:
        start with the Base Power and the two stat lines
        ×1.5 for STAB               round DOWN, right there
        ×2   for super effective    round DOWN, right there
        ×1.3 for the Life Orb       round DOWN, right there
        ×1.5 if it was a Critical Hit, and ÷2 if a Reflect is up and the move is physical
                 ▲                            ▲
                 │                            └─ the running total is one number,
                 │                               never the whole table
                 └─ the rounding is part of the rule, which is why this is exact
```

Exact, and order-sensitive in the same breath: because the game rounds down at each step, applying
the **Expert Belt** before the type multiplier instead of after can land you a point apart on the
same attack. Same rule, same inputs, different bookkeeping order, a number that differs in its
last digit — hold on to that for [272](272-reading-a-kernel-benchmark.md).

## What the reception desk adds on top

### 1. Seven challengers, none of them the same length

The clerk keeps one stack of **128 loose pages**, each page holding **16 turns**, and hands pages
out as runs need them. This morning:

```
   pages handed out so far  = [0, 17, 29, 44, 48, 66, 100, 128]
   lines used on the last   = [1,  7, 14,  4,  3,  1,  16]

   who                pages   turns fought               lines taken
   ──────────────────────────────────────────────────────────────────
   Bug Catcher          17    16·16 +  1 =  257               272
   Youngster Joey       12    11·16 +  7 =  183               192
   Ace Trainer          15    14·16 + 14 =  238               240
   Poké Maniac           4     3·16 +  4 =   52                64
   Super Nerd           18    17·16 +  3 =  275               288
   Cooltrainer          34    33·16 +  1 =  529               544
   Rocket Grunt         28    27·16 + 16 =  448               448
   ──────────────────────────────────────────────────────────────────
             128 pages   1,982 turns              2,048 lines  →  3.2% blank

   ruling every sheet to the longest run (529):  3,703 lines  →  46.5% blank
   ruling every sheet to the longest run allowed: 57,344 lines →  96.5% blank
```

A clerk who rules every sheet the same length wastes nearly half the paper before anybody has
fought a turn. **Everything below exists because of that table.**

### 2. The loose-page stack and the shorthand are the same ledger

The clerk also keeps a shorthand for challengers who only care about *some* of their turns — a
**Sucker Punch** user who needs to know only which turns were attacks, a **Stealth
Rock**-and-switch run where only the entries turn matter. And the shorthand is written in the
identical two-column form: which pages, and where each one starts. **A stack of loose pages is a
shorthand whose blocks happen to be one line wide.** One clerk, one notebook format, and the same
desk serves a plain run, a shared-opening run and a run that consults every sixteenth turn.

### 3. Registered by species, not by battle — and here the usual story is wrong

People say the desk has to be taught a new drill for every new challenger. It does not. What it
registers is what the **Pokédex** registers: **the species, its type, its Ability, whether it is
one of the ones with a second form**. Not the length of the run, not how many pages the challenger
took, not which morning they came. That is why the desk is ready by opening time instead of never:
there are only so many species, and once **Professor Oak**'s **Pokédex** has an entry for
**Gengar**, every **Gengar** that walks in is free.

### 4. Read the room at the gate, then fight 80 stretches without re-reading it

```
   at the desk:   count the runs, share out the 128 pages, decide who writes where,
                  set aside a large clean notebook for the running totals
                  — and this part cannot be done mid-turn
        ▼
   for each of the 80 stretches:      ← ONE reading at the desk, used for all of them
        fight it
```

The clerk's work happens once per challenger, not once per stretch, and the part that repeats is
the fighting. That is the only reason anything in [270](270-serving-stack-around-the-kernel.md)
works.

### 5. The right Ball, and everything in the Bag that is not a Ball

Nobody throws the same Ball at everything. A **Quick Ball** is at its best on the very first turn
and ordinary afterwards. A **Dusk Ball** wants a cave or the dark. A **Timer Ball** gets better
the longer the fight has run. A **Net Ball** wants something Water or Bug. An **Ultra Ball** is
the reliable middle. Picking automatically, by what is actually in front of you, is the whole
skill — and they genuinely do not do the same things, so the choice is not cosmetic.

And the Bag has other pockets. The **TM** case, the **Berry** pouch with its **Sitrus Berry** and
**Lum Berry**, the healing shelf from **Potion** up to **Full Restore**. A desk that only knew
about Balls would be handling one quarter of the morning.

### 6. The warm-up ships in the box, which tells you it hurt

An **Egg** cannot do anything at all until a fixed number of steps has been walked, and only then
is it ready every time afterwards. The games sell you three separate ways around that walk — put a
**Flame Body** Pokémon in the party to halve it, hatch several at once, or take the long route
past the **Day Care** on purpose. Nobody builds three answers to a cost that does not matter.

## Where this stands, September 2026

Everything above I read off the desk's own ledgers, not from someone's account of them. The parts
that keep are the two mechanisms. **The running total** is a fact about arithmetic, not about
paper: it will outlast every notebook format anyone ever rules. **The loose-page ledger** is the
same — the moment challengers have runs of different lengths and arrive at different times, you
are keeping pages with an index, and the plain stack and the shorthand become one object. The Ball
list, the page size of 16 and which drill the desk was taught first are this season's details and
will read as history within the year. One caution before you trust a number off that desk: the
clerk has a switch that fixes how the running totals get added up, and the existence of the switch
tells you the default is a **Speed tie** — see [272](272-reading-a-kernel-benchmark.md).

## What a Gym Leader is listening for

* Why is carrying a running total exact, rather than an approximation?
* What does the desk actually register about a challenger, and what does it deliberately not?
* Why can one notebook format serve a plain run and a shorthand one?
