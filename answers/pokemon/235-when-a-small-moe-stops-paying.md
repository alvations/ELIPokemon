---
id: "235"
slug: when-a-small-moe-stops-paying
style: pokemon
category: open-weights
difficulty: advanced
question: "A 26B model that activates 4B per token should be cheap to run. On one consumer card it often is not. What went wrong?"
tags: [mixture-of-experts, gemma, consumer-gpu, quantisation, serving]
---

# Nothing went wrong. **Garchomp** owns a hundred Berries and the held-item slot fits exactly one

There is a Berry for every specific disaster. A **Yache Berry** halves the **Ice Beam** that
four-times-effectively removes **Garchomp**. An **Occa Berry** does the same job for **Scizor**
against **Flamethrower**, a **Chople Berry** for **Tyranitar** against **Close Combat**, a **Shuca
Berry** for **Heatran** against **Earthquake**. Every one of them is exactly right in the one
situation it was chosen for. Every one of them is a held item. And **Garchomp** holds **one**.

What **Garchomp** holds instead, nine times out of ten, is **Leftovers** — 1/16 of its HP back at
the end of every single turn, no condition attached, no situation required. That choice is the
whole of this question.

Gemma 4's `26B-A4B` is the pouch. It carries 128 specialists in every layer and eats 8 of them per
turn. The eating is genuinely cheap. The *carrying* is not, and it is charged whether or not the
right Berry ever comes up. The label tells you what gets eaten; it says nothing about what gets
carried, and the carried number is the one that decides whether you ever collect the other.

## What is actually in the pouch

Read straight off `Gemma4_26B_A4B` in `google-deepmind/gemma`: 30 layers, width 2,816, 128
specialists of width 704, eight eaten per turn, plus a **Leftovers** tick every turn regardless.

```
   one layer of Gemma 4 26B-A4B, weighed as held items

     the pick, 2,816 × 128            0.36 M    happens every turn
     Leftovers, 3×2,816×2,112        17.8 M    ticks every turn, no conditions
     attention                        37.0 M    every turn
     128 Berries × 3×2,816×704      761.3 M    8 get eaten  ← 8 × 5.95 M = 47.6 M
       Yache · Occa · Chople ·                  the other 120 sit in the pouch
       Shuca · Haban · Babiri ...               being carried

                                    ───────
     carried, per layer              816.5 M    eaten, per layer   102.8 M

   × 30 layers, + a 262,144-entry table

     CARRIED         25.2 B            EATEN PER TURN      3.82 B
     Berries alone   22.8 B  = 90.5% of everything, and one in sixteen is eaten

   ┌─ the same pouch, on the two things one card rations ─────────────────┐
   │                             eaten per turn      carried always       │
   │   Gemma 4 26B-A4B  @ int4       ~1.9 GB            ~12.6 GB          │
   │   a dense 12B      @ int4       ~6.0 GB             ~6.0 GB          │
   │                                                                      │
   │   on a 16 GB Bag:  the Berries leave ~3.4 GB for everything else.    │
   │                    The dense 12B leaves ~10 GB.                      │
   │                    The battle log alone at 131,072 turns is 1.55 GB. │
   └──────────────────────────────────────────────────────────────────────┘
```

Ninety percent of the weight is Berries and a given turn touches one in sixteen. That is the
design doing exactly what it says. It is also why the carried number is six times the eaten one
rather than a fifth above it.

## The four things that eat the saving

**1. Eating really is cheap — right up until the Bag is full.** Turn by turn, the thing that slows
you is how far you have to reach, and reaching for 3.82B instead of 12B is a real win. But the
moment the pouch will not close, the Berries are what gets left behind — they are ninety percent
of the weight — and now every turn you are reaching back to the **Pokémon Center** for a **Yache
Berry** instead of into **Garchomp**'s own slot. The axis you were winning on becomes the axis you
lose on, and it flips all at once.

**2. Whether the Berry fires has almost nothing to do with the Berry.** A public bug report
against one build of a local runner benched this exact pouch on one machine with the Berries kept
outside the Bag: reading in ran at 2,181 a second against the other build's 577, and turns came
out at **6.86 a second against 30.10**. Same pouch, same machine, same Berries — a 4.4× swing from
nothing but which pocket they sat in, and it was closed without a fix. Four-fold differences that
come from the pocket are not measurements of the pouch. **Tyranitar** knows this argument from the
other side: **Knock Off** takes the **Chople Berry** off it entirely and hits 50% harder for
having done so, and an **Aerodactyl** with **Unnerve** on the field stops the Berry being eaten
at all.
Nothing about the Chople Berry changed either time.

**3. Reaching into the Bag costs the turn. Leftovers does not.** A held item fires for free. An
item you have to go and *fetch* takes your whole turn — that is why **Sitrus Berry** in the slot
beats **Hyper Potion** in the Bag even though the Potion heals more. Per turn per layer the pouch
does eight separate reaches into eight separate pockets; thirty layers deep, that is 240 reaches
and 240 small helpings. **Leftovers** is one tick, already in the slot, and **Assault Vest** and
**Choice Scarf** are the same bargain — whatever else they cost you, what they give they give
every turn, with no pick required. The quantity
of work is comparable. What gets done is not.

**4. A long run redeems all of it, and one battle has none.** Across a **Battle Tower** streak or
a **Battle Maison** ladder the specialists pay, because enough opponents come through that every
Berry in the pouch is the right Berry for somebody — the **Yache Berry** finally meets a
**Weavile**, the **Shuca Berry** finally meets a **Garchomp**. A **Bug Catcher** on **Route 1**
with one card and one battle running is the case the pouch was never for.

## The comparison that flatters and the comparison that binds

Most of what is written about this pouch on one card sets it against Gemma 4's dense 31B and finds
it several times quicker. True, and beside the point: the 31B never fit on that card either.
Comparing against the thing you could not have carried anyway is the oldest flattering comparison
there is. The one that decides anything is against the biggest dense checkpoint that fits *with
room to spare* — because the room to spare is your battle log, your vision tower and how many
opponents you take at once. Against that, the pouch wants roughly twice the carrying for roughly a
third of the work, plus a 4× lottery on the pocket. The bet is that 25.2B of carried Berries shows
up as won battles. Sometimes it does. Check it on your own ladder.

## When the pouch is right

A shared **Battle Tower** with a real queue. A box with room nobody else wants. Opposition varied
enough that what you *carry* is what pays — the case where **Heatran** genuinely does meet
**Earthquake**, **Scizor** genuinely does meet **Flamethrower**, and each Berry finds its turn.
This is question 218's argument at a tenth of the size, and at a tenth of the size the carrying
term swallows everything, because the Bag is one card rather than a rack.

## What a Gym Leader is listening for

That you say "eaten is a work claim, carried is a weight claim", then ask which of the two this
machine is short of. Then the cliff: carrying degrades gently right up to the edge and not at all
gently after it, so the question is never how fast **Garchomp** is, it is how full the Bag already
was. The strongest answers ask how long the queue is before offering an opinion at all.

## Where this stands, September 2026

The 30 layers, 128 specialists, width 704, eight per turn and the always-on **Leftovers** at 2,112
were read first-hand from `google-deepmind/gemma` — **primary**. The 25.2B carried and 3.82B eaten
are my own arithmetic over that config; they land on the published "26B total, 3.8B activated",
which is how you know the arithmetic holds. The 6.86-against-30.10 figures were read first-hand
from the public report: one person, one machine, one build, not a controlled result. The
single-card comparisons against the dense checkpoints are **coverage**, because the model cards
and the documentation are behind an egress block here. Pockets and Berry formats change every few
months and point 2 rots first. **Garchomp** has been four-times weak to Ice the whole time, and
carried against eaten has not moved either.
