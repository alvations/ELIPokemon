---
id: "234"
slug: sliding-window-and-stability-stack
style: pokemon
category: open-weights
difficulty: advanced
question: "Walk me through the attention and stability stack in a small open model — sliding windows, GQA, KV sharing and the norms. What is each one actually buying?"
tags: [sliding-window-attention, gqa, kv-cache, rope, normalisation]
---

# **Encore** runs out. **Spikes** never do. That is the whole design, repeated sixty times

Almost everything you can do to an opponent wears off. **Encore** locks them into their last move
for three turns and then lets go. **Taunt** shuts off their status moves for three turns.
**Disable** kills one move for four. Each of those is a **window**: to play around it you have to
remember the last handful of turns and nothing else. And then there is **Spikes**, which you laid
on turn one and which is still taking a chunk out of everything that switches in on turn forty,
because nothing removes it but **Rapid Spin** or **Defog**.

Gemma 4's text stack is that contrast, stacked sixty deep, and every layer of it is spending the
same currency: how much of the past this layer is allowed to hold. Five layers in six get Encore.
The sixth gets Spikes. Everything numeric below is off the published model definitions in
`google-deepmind/gemma`.

## The ladder

```
   Gemma 4 31B — 60 layers, five short effects then one hazard, window 1,024

   E E E E E S   E E E E E S   E E E E E S   ...   E E E E E S     10 hazards
   └─────────┘                                                     50 windows
    5:1, and every S is still biting on the last turn of the battle

   what each layer has to keep, per turn:
     window layer   2 × 16 sets × 256 numbers × 2 B  = 16,384 B  but only 1,024 turns live
     hazard layer   1 × 4 sets × 512 numbers × 2 B   =  4,096 B  and every turn lives

   at a 131,072-turn battle, one side:
     50 windows × 1,024   × 16,384 B  =   0.84 GB   ███
     10 hazards × 131,072 ×  4,096 B  =   5.37 GB   ████████████████████
                                       ──────────
                                          6.21 GB

     the same 60 layers with nothing wearing off  =  112.7 GB   (18× worse)

   E4B — 42 layers, 5:1, window 512, and the last 18 fight under someone else's screen
     24 layers set their own  (20 windows @ 2,048 B, 4 hazards @ 4,096 B)
     18 layers set nothing                             →  57 KB/turn, not 98 KB/turn
     at 131,072 turns:   0.02 GB of windows + 2.15 GB of hazards  =  2.17 GB
```

**The window is a bet, not a free lunch.** Five layers in six can only see the last 1,024 turns.
The bet is that something from turn 400 reaches turn 120,000 by being nailed to the floor in one
of the ten hazard layers rather than by anyone remembering it directly. When it is not nailed
down, this is the architecture that drops it — the same way a **Disable** you were counting on
simply ends and the move comes back. Nothing warns you. It looks like "it forgot what I told it at
the start".

**One screen or eight.** **Reflect** cuts physical damage and **Light Screen** cuts special, and
they cover the whole side for five turns — eight if the setter holds **Light Clay** — no matter
who is standing in front. E2B runs eight attackers off **one** shared screen. E4B runs eight off
two. The 31B runs thirty-two off sixteen locally and thirty-two off four in its hazard layers.
What you give up when you share is that every attacker is now reading the same screen, so they
stop being able to disagree about what is worth protecting. The smaller the model the harder it
shares, which is the right direction: on a phone the screen is the expense; on a rack it is not.

**The screen survives the switch, and that is the trick people miss.** In E2B the last 20 of 35
layers and in E4B the last 18 of 42 do not set a screen at all. They fight under the one the last
unshared layer of the same kind put up, exactly as a **Light Screen** set by the Pokémon that
fainted still protects the one you send in after it. That is 43% off E4B's per-turn bill and it
takes the setup move out of the budget too. The cost: eighteen layers deep, everyone is still
fighting under a screen raised for a fight that has moved on.

**One move doing the work of two.** In the 31B and the 26B-A4B configs the hazard layers derive
both halves from a single projection — **Aurora Veil**, which the Alolan **Ninetales** puts up
off the back of **Snow Warning**, and which cuts physical and special damage from one move slot
instead of two. Half the setup, and in a stack that exploits it, half the screen to keep track of.

## The half that costs you nothing to carry

* **Two counters, coarse and fine.** **Perish Song** counts three, two, one and then everything
  that heard it faints; it never needs to count higher, so it counts precisely. **Badly Poisoned**
  counts 1/16, 2/16, 3/16 and keeps going as long as the battle does. The window layers use the
  fine short counter — base frequency 10,000, the whole width turning. The hazard layers use the
  coarse long one — base 1,000,000, and only a quarter of each 512-wide hazard turning at all.
  The rest of it is just the hazard sitting there, which is not a thing that needs a turn number.
* **Burn the attacker, do not screen the hit.** Every Gemma 4 config now sets the attention soft
  cap to nothing. The old generation squashed the numbers on the way out, the way **Reflect**
  halves the damage after it has been calculated. This one normalises the query and the key on the
  way in, the way **Will-O-Wisp** halves the attacker's physical damage at the source and then
  costs nothing every turn after. Same runaway, stopped earlier, and it does not fight with
  anything else in the calculation. (**Guts** is the exception that proves it is a real mechanism:
  the ability that ignores the drop entirely.)
* **Clean coming in and going out.** Every sublayer gets a check before it and a check after —
  **Full Heal** on the way in, **Natural Cure** on the way out — so nothing accumulates across
  sixty layers of depth.
* **The one hard cap left.** Thirty. The output is squashed to ±30 before choosing among 262,144
  options. **Fissure**, **Horn Drill** and **Guillotine** end the battle in a single hit, and the
  game gives them **30%** accuracy against a target of your own level and refuses them outright
  against anything higher. The one place where one choice can decide everything is the one place
  a number gets nailed down.

## What a Gym Leader is listening for

That you treat "it uses a window" as a claim with a failure attached, and can say what the failure
looks like from the outside. Then that you keep the *what it costs to carry* family separate from
the *what stops it exploding* family instead of reciting one list. The strongest answers notice
that the old squash was **removed** between generations and can say what replaced it — anyone
still listing it as current learned the stack from a two-year-old write-up.

## Where this stands, September 2026

The layer counts, the 5:1 pattern, the window sizes, the two counter bases, the quarter-width
turning, the *nothing* on the attention cap, the **30** on the final one, and which layers set no
screen were all read first-hand from the model definitions in `google-deepmind/gemma` and
cross-checked in `huggingface/transformers` — **primary**. The gigabyte figures at 131,072 turns
are my arithmetic over those settings, not quotes. The published claim that all this cuts the
hazard-layer bill by up to 37.5% is **coverage**; the report that states it is behind an egress
block here. Read the settings in the checkpoint you actually downloaded. Encore has lasted three
turns for a very long time, and what a bounded window costs you has not changed either.
