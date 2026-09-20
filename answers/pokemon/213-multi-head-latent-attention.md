---
id: "213"
slug: multi-head-latent-attention
style: pokemon
category: open-weights
difficulty: advanced
question: "What does Multi-head Latent Attention actually cost, and what does it buy against GQA and MQA?"
tags: [attention, kv-cache, mla, gqa, deepseek]
---

# The Vs. Recorder does not save the battle. It saves just enough to play it again.

A **Battle Video** is tiny. The battle it holds is not. The **Vs. Recorder** does not keep
pictures of **Lance**'s **Dragonite** taking an **Ice Beam** — it keeps the teams and the orders,
and when you watch it the game simply plays the whole thing out again. Hand someone a
twelve-digit code and they get the entire match back.

That is the trade. You carry almost nothing, and you pay for it in the time it takes to replay.

Now put **Lorelei**, **Bruno**, **Agatha** and **Lance** in the stands. All four are watching the
same battle and all four want different notes: Lorelei is tracking who is frozen solid, Bruno
who is still standing, Agatha what is immune to what, Lance which **Dragon Dance** went up.

## What each of them actually carries out of the room

```
   what has to be kept, per turn

   four full tapes   one complete recording each, all four in the bag
                     ████████████████████████                       1.0×
   two shared tapes  Lorelei and Bruno share, Agatha and Lance share
                     █▌                                            16×  lighter
   one shared tape   all four squint at the same recording
                     ▏                                            128×  lighter
   one Battle Video  the teams, the orders, the turn numbers
                     ▍                                             57×  lighter
                       │             │
                       │             └ the turn numbers, which cannot be
                       │               reconstructed from anything else
                       └ replayed into all four sets of notes on demand

   sixty-one rounds of this, and the Battle Video still fits in a pocket
   where the shelf of tapes needs a room.

   ┌──────────────── what each of them gives up ───────────────────┐
   │ shared tapes   Agatha stops seeing what only Agatha would see │
   │ Battle Video   all four still see their own thing — what goes │
   │                is the detail below the level the replay keeps │
   └───────────────────────────────────────────────────────────────┘
```

That box is the whole argument. Sharing tapes works by making **Lorelei** and **Bruno** agree on
what was worth writing down, and they genuinely do lose something when they agree. The Battle
Video keeps all four watching separately and loses fineness of detail instead.

Note the honest bit that gets skipped: **one shared tape is lighter than the Battle Video**. The
claim was never that the Video is the lightest thing you can carry. It is that it weighs about
what the shared tapes weigh while letting all four of the **Elite Four** keep their own eyes.
That is one **Pokémon League**'s own result, reported by the people who built it, and you should
want somebody else to run the tape before you rebuild your **Battle Frontier** around it.

## The part that refuses to compress: turn order

A replay that gets every move right and the order wrong is a different battle. **Surf** before
**Earthquake** is not the same match as Earthquake before Surf. So the recording has to carry the
turn numbers as themselves — no reconstructing them from the moves. The teams and the orders for
*what*, the turn count for *when*. A small tax, and the clearest possible sign that shrinking a
record is easy right up until something in the middle refuses to be rebuilt.

## What it costs

1. **Replaying takes turns.** Every time Agatha wants her notes she has to watch it again. Watch
   it one way while the battle is still running and one way afterwards, and that is two
   procedures to keep straight, not one.
2. **You cannot split one tape four ways.** Four separate recordings hand out cleanly — one
   each. A single Battle Video does not, so everyone ends up carrying a copy and some of the
   saving goes straight back.
3. **Not every machine plays it.** The Vs. Recorder is its own device. It is not in every
   **Pokémon Center**, and the shelf of ordinary tapes plays anywhere.
4. **You cannot convert a shelf of tapes into one afterwards.** It had to be recorded this way
   from the first turn.

## What it buys

What you can carry decides how many battles you can hold at once, and how many you hold at once
decides what each one costs you. Seven times lighter is not seven percent better — it is the
difference between a **Battle Tower** run you can afford to enter and one you cannot. The
repeated entry-fee cuts all come from here.

## And then the same League stopped using it

The next generation of the format threw the Battle Video out. Instead of shrinking each turn's
record, it **skips turns**: keep one summary per stretch of the battle, keep the handful of turns
that actually decided it in full, and alternate between the two as you go back through. Shrinking
each turn runs out of room. Shrinking the *number* of turns is what is left when the match has run
a million of them. Reported figures put the new format at roughly a quarter of the work and a
tenth of the weight of the old one at that length — reported, because the rulebook itself could
not be read from here.

## What a Gym Leader is listening for

That you can say what each of the four actually carries, in numbers — and that you spot that one
shared tape is lighter than the Battle Video, which almost everyone misses because they have
learned "the Video is the efficient one" and stopped. Then the turn numbers, because that is
where you show you know *why* it is not free. The strongest answers end on the **Pokémon
Center**, the copies and the two procedures, not on the arithmetic.

## Where this stands, September 2026

The older numbers come from the League's own published rulebooks and have not moved. Everything
about the new format here is **second-hand**: the sites that hold the report, the documentation
and the model cards are all blocked from where this was written, so none of it was read
first-hand. The authority is the `DeepSeek-V4` report and the `deepseek-ai` model cards. Check
them before you quote a number. The reasoning — what you carry against what you replay — is older
than any of these and will outlast them.
