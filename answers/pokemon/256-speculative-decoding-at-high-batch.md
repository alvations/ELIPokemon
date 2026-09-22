---
id: "256"
slug: speculative-decoding-at-high-batch
style: pokemon
category: optimization
difficulty: advanced
question: "Speculative decoding is a large win at batch size one. Why can it be a loss at high batch?"
tags: [speculative-decoding, roofline, batching, throughput, serving]
---

# Because it spends Safari Balls to save steps, and on a busy day you run out of Balls.

The **Safari Zone** hands you exactly two things at the gate: **30 Safari Balls** and 500 steps.
Which of the two binds is decided entirely by what you came in for. Walk the northern grass for a
**Heracross**, or the north-western grass for a **Pinsir**, and you are after something that fills
five slots in a hundred: you will walk a very long way between the encounters you actually throw
at, you will be shown the exit with a dozen Balls still in the bag, and every Ball you spent on a
guess along the way cost you nothing you were going to use. Come in to catch whatever turns up,
and the southern grass gives you an **Oddish** in forty encounters out of a hundred with a
**Girafarig** or a **Wobbuffet** never far behind — now the Balls are what run out, and a fan of
four Safari Balls at one encounter is three catches you will not make later. A fan four wide costs
four Balls and brings home 2.952 on average, so on a busy day it can never be worth more than
2.952 ÷ 4 of what plain catching is worth — **less than one, for every fan that is ever wrong**.
That fraction is the whole answer. Everything else is working out where the day turns busy.

## The two budgets, and the line between them

Thirty Safari Balls across 500 steps is **six Balls per hundred steps**. That number is the whole
geometry of the Zone. A trip that only stops for a **Natu** — fifteen slots in a hundred in the
northern grass, and a **Gloom** filling another fifteen you walk straight past — sits well under
it. A trip that stops for everything sits well over.

```
   Balls thrown
        │        ┌──────────────────────── 30 Balls: the hard ceiling
        │      ╱
        │    ╱   ← slope: one Ball per encounter
        │  ╱
        │╱     0.1/100   1.5/100      6 per 100      24/100
        └────────┴──────────┴─────────────┴─────────────┴────── encounters per hundred steps
                     steps run out first        Balls run out first
                  Balls to spare: fan out      ───►   no Balls spare: don't
```

Six per hundred is where the two budgets bind at once. Below it you are walking; above it you are
throwing. And the important part: a fan four wide throws four Balls at every encounter, so a fan
crosses that line at **six divided by four — one and a half encounters per hundred steps** — long
before plain catching notices anything at all.

## Where the gain goes

Take a fan four deep that holds three casts in four (so it brings home 2.952 encounters' worth per
stop, by the sum in [230](230-multi-token-prediction-and-drafting.md)), and a guess that costs a
tenth of a real throw to make:

```
   encounters per      a plain day      a fanning day      brought home      gain
   hundred steps       costs            costs              per stop
   ──────────────────────────────────────────────────────────────────────────────────
        0.1              1.00              1.30               2.952          2.27
        0.8              1.00              1.30               2.952          2.27
        1.5              1.00              1.30               2.952          2.27
        3                1.00              2.30               2.952          1.28
        6                1.00              4.30               2.952          0.69   ◄ a LOSS
       12                2.00              8.30               2.952          0.71
       24                4.00             16.30               2.952          0.72
   ──────────────────────────────────────────────────────────────────────────────────
                                                   the floor it settles on: 2.952 ÷ 4 = 0.738
```

Look at what happens between 1.5 and 3 encounters per hundred steps. The plain walker has not
slowed down at all — he is still step-bound, still strolling. The fanning walker crossed the line
two doublings earlier and is already rationing. **A fan hits the ceiling at a quarter of the
traffic that plain catching does.** A day that looked fine in the morning becomes a worse day than
not fanning at all by lunchtime, with nothing having changed about the fan, the water or the Zone.

## Two costs that are easy to forget

* **A slot spent guessing is a slot not spent catching.** Putting **Octillery** at the front of
  the party for its **Suction Cups** costs you the slot you were going to bring the **Heracross**
  home in. Carrying the **Old Rod** alongside the **Super Rod** costs you a **Bag** slot. A
  **Pokéblock** is the one thing in the Zone that costs neither a Safari Ball nor a step — it
  costs you an afternoon at the berry blender, earlier. On a trip with a hard ceiling on what you
  can carry, all of those are catches given up before you set off. Reading the route sign costs
  nothing at all, which is exactly why it is the first thing to try.
* **Guesses compound, so long fans are worth less than they look.** You can fish inside the Zone
  too, and the water there is as honest about this as the grass: the **Old Rod** pulls
  **Magikarp** seven casts in ten and **Goldeen** the other three, while the **Super Rod** brings
  up Goldeen four casts in five with the odd **Seaking** behind it, and asks for up to six clean
  rounds in a row before anything is even on the hook. At an even coin flip a round, a six-round
  cast lands 1.6 times in a hundred. Put Octillery in the lead and each round holds 92.5 times in
  100 instead of 50, and the very same six-round cast lands 62.6 times in a hundred. Forty times
  the value of the deep end of the fan, from one change to how often a single round holds. That is
  why how far ahead you should guess moves with how good your guessing is, and why a fixed fan
  width is the wrong thing to walk in with.

## What to do about it

Set the width by how busy the day is, and let it fall to nothing. The two big halls both do
exactly this now, and one of them prints the table:

```
   one run at a time    →   plan  1, 3, 5 or 7 ahead
   eight at once        →   plan  0, 1 or 3 ahead
   thirty-two at once   →   plan  0 or 1 ahead
   sixty-four at once   →   plan  0 — stop guessing entirely
```

The other hall says the same thing as a list of ranges: from this many runs to that many runs,
guess this far ahead. Both were read off the halls themselves in September 2026.

The framing underneath all of it: fanning out is a **waiting** cure, not a **throughput** cure.
While you are strolling it gives you fish for free. Once you are rationing Balls it is a straight
trade — less brought home overall, in exchange for less standing around at each stop — at the
fixed rate of 2.952 to 4. If you are chasing a streak where the wait at each stop is what is
killing you, that trade can absolutely be the right one to make on purpose. Made by accident —
because you timed yourself in the northern grass holding out for a **Pinsir**, and then went south
and started throwing at every **Oddish** — it is just a worse day you cannot see.

## What a Gym Leader is listening for

* Where does the floor of 2.952 ÷ 4 come from, and when can it reach 1?
* Why does a fan run out of Balls at a quarter of the traffic that plain catching does?
* When is trading fish for less waiting the right call, and what tells you?

## Where this stands, September 2026

The shape is permanent. Two budgets, one that binds when you are walking and one that binds when
you are throwing, and a fan that multiplies only the second of them — that will be true of any
Zone with a gate and a step counter. The floor of what a fan can be worth on a busy day is
arithmetic and does not move. The numbers do. Thirty Balls and 500 steps are read off the Zone and
are exact; the six-per-hundred crossing is exact from them; the point where *your* day turns busy
is not, and the hall tables above are a September 2026 reading of two halls that change
constantly. Zones built with a more generous warden push the crossing later, which makes fanning
pay on busier days, so the numbers will drift in a direction you can predict. Walk your own route
and count. It is an afternoon, and it is the number the whole decision turns on.
