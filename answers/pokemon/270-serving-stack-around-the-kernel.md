---
id: "270"
slug: serving-stack-around-the-kernel
style: pokemon
category: optimization
difficulty: intermediate
question: "Paged attention, continuous batching, chunked prefill and CUDA graphs are four separate fixes. What does each one fix, and where do they collide?"
tags: [vllm, paged-attention, continuous-batching, chunked-prefill, cuda-graphs]
---

# Four fixes for four different kinds of standing about — and then they start fighting.

The healing machine in the **Pokémon Center** has **six recesses** for **Poké Ball**s, restores
HP, PP and status in one cycle, and costs nothing — everything a **Full Restore**, a **Max
Revive** and a **Max Elixir** would have cost you between them, free, in about four seconds. On
the last Saturday before the **Pokémon League** closes registration the queue is out of the door,
and four separate things are wasting the morning. Each has its own fix. The interesting part is
not the list — it is that **the third fix and the fourth want opposite things**, and whoever is
behind the counter has to choose.

```
   ┌── a Trainer comes through the door ───────────────────────────────────────┐
   │                                                                           │
   │  the doorway ──▶ THE COUNTER ──▶ a tray is filled ──▶ THE MACHINE         │
   │                      │                                    │               │
   │        refill a recess the moment            skip the jingle by replaying │
   │        its light stops blinking              a cycle you already know     │
   │                      │                                    │               │
   │        cap how much damage goes in           one Poké Ball to a recess,   │
   │        per cycle, and split the rest         and a slip saying whose      │
   └───────────────────────────────────────────────────────────────────────────┘
```

## 1. One Ball to a recess — fixes holding space for a party nobody brought

You do not know how many a **Bug Catcher** is carrying until he reaches the counter, so the lazy
answer clears a whole bench of six every time. [269](269-flashattention-to-flashinfer.md) has the
arithmetic from a real morning: 1,982 Poké Balls actually handed over took 2,048 recesses in trays
of sixteen (**3.2% standing empty**), 3,703 if every tray is cleared to the largest party that
morning (46.5%), and 57,344 if every tray is cleared to the largest party anyone has ever brought
(96.5%). **Youngster Joey** brings one **Rattata**. Clearing six recesses for it is five recesses
of nothing.

The soil out the back works the same way and shows the cost just as plainly: loose soil comes in
plots, one **Sitrus Berry** to a plot, one **Leppa Berry** to the next, and a plot with a single
sprout in it is a whole plot spent. You plant in whichever plots are free rather than roping off
the patch for a **Lum Berry** that may never come up. Cost: somebody now keeps a slip saying which
recess holds whose **Ultra Ball** and which holds the **Heal Ball**, and half a tray is wasted per
**Ace Trainer** no matter what you do.

## 2. Refill the recess, do not wait for the tray — fixes waiting on the slowest

Hand over six, and all six recesses are held until the last light stops blinking. A **Magikarp**
with a scratch and a fainted **Dragonite** come back at the same moment, because the tray goes in
together and comes out together. A **Blissey** that can **Softboiled** itself back up between
fights never joins the queue at all; everyone else waits on the slowest thing in their own tray.

```
   eight Trainers, with damage to repair of  32 64 96 200 350 512 700 900

   a full tray   all 8 recesses held for 900     =  7,200 recess-cycles
                 actually mending anything       =  2,854 recess-cycles
                 ──────────────────────────────────────────────────────
                 39.6% of the machine was doing work

   one at a time a recess is refilled the moment its light stops  → near 100%
```

Cost: the tray is a different shape every cycle, which is exactly what the next two fixes find
inconvenient.

## 3. The charge turn — fixes one enormous job freezing the room

A **Cooltrainer** back from **Victory Road** with six fainted Pokémon takes about 196 counts of
the machine's time. Run it as one job and everyone behind waits 196 counts for a single **Hyper
Potion**'s worth of mending — eleven missed cycles, felt by every person in the queue. This is the
**Elite Four** problem in miniature: once you are in the room with **Lorelei** you do not get out
until **Lance** is done, and nothing else on the **Indigo Plateau** happens meanwhile.

The games already contain both halves of this. **Solar Beam** takes a turn to charge and fires on
the next, so the opponent still gets a turn in between — and under **Sunny Day** it skips the
charge entirely, which is wonderful for you and takes everyone else's opening away, exactly as a
**Power Herb** does. **Outrage** is the opposite by default: **Dragonite** is locked in for two or
three turns, nothing else happens until it is over, and it comes out confused. **Thrash** and
**Petal Dance** lock you in the same way. A counter that lets every big job **Outrage** has picked
the worst of the four.

```
   cap the cycle at 2,048 counts, with 128 light jobs already waiting
        128 counts of quick mending  +  1,920 counts of the big one
        8,192 ÷ 1,920  →  5 charge turns
   the big job finishes at about the same moment. The queue never stalls
   for more than one charge turn.
```

## 4. Skipping the jingle — fixes ceremony that changes no outcome

Turn the animations off in the options and set text to Fast. Nothing about the result changes: the
same **Ice Beam** off the same **Dragonite** leaves the same HP, and the **Leftovers** still tick
for a sixteenth. What goes away is the fixed ceremony around it — and around one cycle of quick
mending, the ceremony genuinely costs about as much as the mending does.

You can only skip a ceremony you already know by heart. The machine runs its whole cycle and plays
the whole jingle whether you handed over six **Poké Ball**s or one, so a **Bug Catcher** with two
**Caterpie** is charged for six. And the first time something unscripted happens — an evolution, a
level-up, a **Shiny** sparkle, a **Pokérus** notice — the memorised version does not fit and you
sit through the real thing.

## Where they collide

**This is what the question is actually about.**

```
   the charge turn produces MIXED cycles (a slice of the big job + the quick ones)
                    │
                    ▼
   a memorised jingle needs every cycle to be the SAME SHAPE
                    │
   and most counters can only recite the one they know for the all-quick cycle
                    │
                    ▼
   the settlement: keep TWO routines and pick between them every single cycle
                   the memorised one when the tray is all quick jobs,
                   the real one whenever the big job is in the tray
```

Three more, all real:

* **The slip is why you can never memorise the whole cycle.** Which recess holds whose **Ultra
  Ball** differs for every **Ace Trainer** in the queue, so that step is read off the slip, live,
  and the recitation is cut in two around it.
* **Refilling recesses fights the recitation.** The tray is a different size every cycle, so you
  round up to the nearest tray you have memorised, and a tray of five runs as a tray of eight —
  three empty recesses cycling for nothing. Memorising more tray sizes costs shelf space and a
  longer open-up in the morning.
* **Run out of recesses and it feeds back.** With no room, a **Poké Maniac** already halfway
  through is pulled out and starts over from the beginning — which turns him back into a big job,
  which needs charge turns, which pushes the quick jobs back. A queue that looks like a **Speed
  Tier** problem is very often a shelf-space problem wearing its coat.

So you cannot turn these four knobs one at a time. Capping the cycle tighter to keep the quick
jobs moving makes mixed trays more common, which makes the memorised jingle unreachable, which
adds ceremony back at precisely the tray sizes where ceremony is most of the cost.

## Where this stands, September 2026

The counter's exact routines are this season's and will change — I read them off this counter's
own noticeboard, and the noticeboard is rewritten often. Check the one behind the counter you are
standing at, not the one you remember ([232](232-reading-an-open-model-card.md)).

What keeps is the shape of it. **Three of the four fixes work by making every cycle different, and
the fourth only works when they are all the same.** One **Poké Ball** to a recess, refilling as
lights stop, and splitting the big jobs into charge turns all exist to keep the machine full, and
they do it by making the morning less predictable. Memorising the jingle, and every other kind of
getting-ready-in-advance, wants the opposite. Any **Pokémon Center**, in **Kanto** or in
**Paldea**, in any generation, ends up as a truce between those two — and the truce is nearly
always "spot the plain cycles and have a quick way through them".

## What a Gym Leader is listening for

* Why does splitting the big job make the memorised jingle harder?
* What sets how much of a tray goes to waste, and how big should a tray be?
* You capped the cycle tighter and the morning got slower. Give two reasons.
