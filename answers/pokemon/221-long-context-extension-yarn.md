---
id: "221"
slug: long-context-extension-yarn
style: pokemon
category: open-weights
difficulty: advanced
question: "Qwen's checkpoints are 262K native and advertised as extensible to 1M with YaRN. What degrades when you stretch a window instead of training it?"
tags: [qwen, long-context, yarn, rope, linear-attention]
---

# A Rare Candy gives you the level. It does not give you the EVs.

Feed a Pokémon **Rare Candy** until the counter reads 100 and the summary screen will say 100.
It will also have **zero Effort Values**, because Rare Candy grants none. A Pokémon that battled
its way up carries as many as 510 of them, up to 252 in a single stat, and at level 100 every four
EVs is worth one point. So the candied one is short by as much as **63 points** in each of two
stats against the one that walked. Same level. Same cap of 100. Not the same Pokémon.

Every recent Qwen open checkpoint prints the same line on its card. `Qwen3.5-397B-A17B`:
*"Context Length: 262,144 natively and extensible up to 1,010,000 tokens."* `Qwen3.8-2.4T-A95B`:
the same sentence word for word. And the Qwen team's own launch commands all open at 262,144.

Note that 262,144 × 4 is 1,048,576, and the card says 1,010,000. The gap is small and it is
honest — the number you can reach and the number that works are not the same number, and the lab
says so.

```
   ① BATTLED TO IT      262,144      the levels it actually earned
   ② SCREEN SAYS        whatever     one config line takes 1,010,000 the
                        you set      way a Rare Candy takes you to 100
   ③ CAN ACTUALLY DO    ???          a question about YOUR opponents that
                                     nobody answers for you

   ┌──────────────────────────────────────────────────────────────────────┐
   │  ①──────────────────────────┤                                        │
   │  ②──────────────────────────────────────────────────────────────┤    │
   │  ③────────────────────?                                              │
   │                       ▲                                              │
   │                       └─ everything right of here is a claim         │
   └──────────────────────────────────────────────────────────────────────┘
```

## Four things that give way, in the order you meet them

**1. Every short battle, whether you wanted it or not.** The stretch is switched on for the whole
server the way **Trick Room** is switched on for the whole field: five turns of reversed order
within every priority bracket, for everybody. You set it because your slow sweeper needs it, and
now your **Jolteon** at base 130 Speed is moving last too. Trick Room even sits at −7 priority, so
you go last the turn you commit to it. Qwen's own cards say not to turn the long window on unless
you need it, for exactly this reason: it is a mode the field is in, not a talent lying dormant.

**2. Anything that needs more than one exchange.** The candied level-100 still wins the obvious
one: **Ice Beam** into **Dragonite** is four times effective and that is decided by the **Type
Chart**, not by the missing 63 points. Retrieval of one distinctive thing survives the stretch the
same way, which is why the headline score stays high and why it is the wrong test. Ask it to
survive, trade, and still be standing eight turns later — the grind where the missing EVs live —
and it is a different Pokémon.

**3. Spending the budget twice.** You get 510 EVs and six stats. Pour them into Speed and they are
not in Special Defence. Qwen's card carries the same warning pointing the other way: *"we advise
maintaining a context length of at least 128K tokens to preserve thinking capabilities."* The
model spends its window on its own reasoning, so trimming the window to save memory trims how hard
it can think (question 220). One number, two jobs.

**4. The charge turn, which is the real bill.** A million tokens of reading happens before a
single token comes out, the way **Solar Beam** spends a whole turn gathering light before it hits
for 120. Only **Sunny Day** or a **Power Herb** skips that turn, and a Power Herb is consumed
when it does. Question 206 makes the general point; here it collides with how the Pokémon is
built.

## How it is built changes what "gives way" even means

Qwen3.5 does not remember the way a plain attention stack does. The team calls it "Gated Delta
Networks combined with sparse Mixture-of-Experts", and vLLM's configuration for the family lays
the layers out three-to-one: three linear-attention blocks for every one full-attention block.

```
   layer:  1     2     3     4     5     6     7     8   ...
           GDN   GDN   GDN   ATTN  GDN   GDN   GDN   ATTN
           ───────────────   ────  ───────────────   ────
           BATON PASS        reads  BATON PASS       reads
           a fixed handoff   it all a fixed handoff  it all

   Only one layer in four keeps the whole log  ──►  a million fits
   Three in four pass a summary forward        ──►  and the summary does
                                                    not grow with the log
```

**Baton Pass** hands on the stat stages and the **Substitute**. It does not hand on the HP, and it
does not hand on the burn. It is a fixed-size handoff by design, and it does not get bigger
because the battle got longer. So three layers out of four are passing a baton, and only the
fourth is allowed to look back at what actually happened.

That is the second way this can fail, and it is not the Rare Candy problem. It is structural. The
trade is a good one — it is why a 262,144 window is affordable at all — but "how far back can it
see" is answered by the layers that still read the log, not by the number on the box.

## What to do about it

1. **Keep two sets, not one.** The trained one for the routes you run every day, the stretched
   one for the long haul. One server left in Trick Room taxes every short battle you have.
2. **Test on the eight-turn grind, not the one-shot KO.** A super-effective hit tells you almost
   nothing about the fight you will actually lose.
3. **Budget the charge turn separately from the team.** "It fits" and "it answers in time" are two
   different **Gym** badges.
4. **Do not spend below the card's floor** on a Pokémon whose whole job is to think.
5. **Treat 1,010,000 as a reading off the summary screen.** The screen took it.

## What a Gym Leader is listening for

That you separate what it battled to, what the screen says, and what it can actually do, and know
which of the three a claim is about. Then that you know the stretch is an item, not training —
and that items are switched on for the whole field. The strongest answers bring up the
three-to-one layout unprompted and notice there are two independent things that can give way at
the far end.

## Where this stands, September 2026

The context sentences and the 128K floor are quoted from the Qwen model cards, read through a
verbatim third-party copy because the card pages are behind an egress block here; the cards are
the authority. The three-to-one layer layout is read directly from vLLM's configuration for the
family. The stretch parameters are the published recipe. **One thing I could not check:** Qwen's
earlier million-token line was reported to pair dual chunk attention with this stretch, and the
current cards name the stretch alone — I could not reach a primary page that settles it for the
3.5 / 3.8 weights, so do not assume it in either direction. Rare Candy will still grant no EVs.
