---
id: "264"
slug: outlier-channels-and-quantisation-algorithms
style: pokemon
category: optimization
difficulty: advanced
question: "Explain outlier channels, and what GPTQ, AWQ and SmoothQuant each do about them."
tags: [quantisation, outliers, gptq, awq, smoothquant]
---

# Shuckle has a 230 and a 5. One ruler cannot measure both.

**Shuckle**'s six base stats are **20 / 10 / 230 / 10 / 230 / 5**. **Ditto**'s are 48 / 48 / 48 /
48 / 48 / 48. If you have one ruler and you have to measure a stat line with it, **Ditto** is free
and **Shuckle** is a catastrophe — and the catastrophe is not the 230. It is what the 230 does to
the 5.

And the extremes are not scattered about. It is **always** Defense and Special Defense on a
**Shuckle**, **always** HP on a **Chansey** (250, next to a Defense of 5), **always** Speed on a
**Regieleki** (200, the highest in the game). Same stat, every single one of that species,
forever. That is what makes the problem fixable — and also why you cannot simply shave the big
number off. **Shuckle** with its 230s trimmed to 100 is not a tidier **Shuckle**. It is not a
**Shuckle**.

```
   ONE RULER FOR THE WHOLE LINE — 16 marks, stretched to reach 230

   stat:      HP    Atk   Def   SpA   SpD   Spe
   real:      20    10   230    10   230     5
   mark:       1     1    15     1    15     0     ← step is 230/15 ≈ 15.3
   reads:     15    15   230    15   230     0
                    ▲                        ▲
                    │                        └── 5 rounds to nothing at all
                    └── a 10 that reads 15 is off by half

   FOUR OF THE SIX NUMBERS ARE NOW WRONG so that two can be right.

   ONE RULER PER STAT — 16 marks each

   Attack gets its own 16 marks across 0–10: step 0.67. Exact.
   Speed  gets its own 16 marks across 0–5 : step 0.33. Exact.
   ─────────────────────────────────────────────────────────────────
   FREE for your OWN stat line — you have it in front of you, column
   by column, and can rule each column separately.
   NOT free for WHAT WALKS IN — it is one Pokémon at a time, chosen
   by somebody else, and you have to be ready before you see it.
```

That asymmetry is the whole shape of the problem. **Your own stat line is easy**: no surprises,
you can rule it as finely as you like. **What comes at you is not**: it is a fresh Pokémon every
turn and one turn in a thousand it is a **Shuckle**. So getting your own numbers small is a solved
problem, and getting the incoming ones small is where all the craft is.

## Move the factor across the ratio

Damage is your Attack over their Defense. So these two are **exactly** the same number:

```
   Swords Dance on your side          Leer, twice, on theirs
   ──────────────────────────         ──────────────────────
   Attack  ×2   (+2 stages)           Defense ÷2   (−2 stages)
   ──────────────────────────────────────────────────────────
   damage ×2                          damage ×2      identical.

   before                             after, factor 8 moved across
   ────────────────────────────       ──────────────────────────────
   their number :  63  (hopeless)     their number :  7.9 (ordinary)
   your number  :  0.05 (trivial)     your number  :  0.4 (still fine)

   nothing was removed. It was MOVED — off the side you cannot rule
   finely, onto the side you can.
```

That is the first trick, and what it exploits is not cleverness but an identity that was sitting
there the whole time: the ratio does not care which half of it the factor lives in. The cost is
that how much to move is a judgement, and against a truly absurd opponent there is no split that
leaves both sides comfortable.

## Let the opponent decide which number matters

**Alakazam** has 135 Special Attack and 45 Defense. Which of those two is the important number?
**Neither** — the answer is on the other side of the field. Against a **Blissey** and its 135
Special Defense, the 135 is the number the match turns on. Against a **Machamp** and its 130
Attack, the 45 is, and the 135 is decoration.

So the second trick is: find the one number in ten that the incoming Pokémon actually touches, and
protect **that** one, chosen by what you are facing and not by which of your own numbers looks
biggest. And the way to protect it is not to write it out longhand while everything else is
rounded — that gives you a stat line nobody can read. It is to **scale that number up before you
round it**, so it lands between finer marks, and divide the incoming one by the same amount. Which
is the trick above, pointed the other way round. They are the same trick.

## Commit the first slot, then re-pick the rest

The third one is different in kind. You are registering six, and you round the first one off — you
take the **Garchomp** with **Earthquake**, **Dragon Claw**, **Stone Edge** and **Swords Dance**,
knowing it leaves you wide open to Ice.

The lazy move is to keep picking the other five as though that had not happened. The real move is
to **re-solve the remaining five knowing exactly what the first one cost you**, and then do it
again after the second, and again after the third. Each commitment pushes its error into the slots
that are still free.

And you need one more thing to do it properly: not just which holes you have, but **which holes
overlap**. Two Pokémon that both fold to Ice is not two problems, it is one problem twice the
size; a **Type Chart** read pair by pair tells you that and a list of individual weaknesses does
not. That is the expensive part, it is why this is the slowest of the three to do, and it is why
it is the one most likely to end up beautifully fitted to the exact opponents you happened to
practise against.

## Or stop using those six columns

The last idea is the one that makes the others look like housekeeping. **Blissey** is 255 HP and
10 Defense. **Alakazam** is 55 HP and 45 Defense. In the printed columns those are not remotely
the same Pokémon — one has the biggest HP in the game and the other has a ninth of it.

Now multiply HP by Defense, which is the number that actually decides how many hits each survives:

```
   Blissey    255 × 10  =  2,550
   Alakazam    55 × 45  =  2,475      ← the same Pokémon, in the basis
                                        that the damage formula uses

   Chansey    250 ×  5  =  1,250      ← the 250 was never the story
   Skarmory    65 × 140 =  9,100
```

Blissey's 255 stopped being an outlier the moment it was measured along an axis that was not one
of the six printed ones. Nobody managed the extreme value; the coordinates that made it extreme
were thrown away. That is the most satisfying of the four, and the hardest to see first.

## What a Gym Leader is listening for

* Why can you rule your own stat line column by column and not the incoming one?
* If the first two tricks are the same identity, when would you use one and not the other?
* Which of these gets fitted too tightly to the Trainers you practised against, and why?
* What would you check to tell "the new axis worked" from "the practice battles never tested it"?

## Where this stands, September 2026

The stat lines are from the published tables and I checked every one: **Shuckle**
20/10/230/10/230/5, **Chansey** 250/5/5/35/105/50, **Blissey** 255/10/10/75/135/55, **Alakazam**
55/50/45/135/95/120, **Skarmory** 65/80/140/40/70/70, **Ditto** at a flat 48. The stage
multipliers are from the games' own code: +2 is exactly ×2 and −2 is exactly ÷2, so the two
openings really are worth the same damage. Which of the four tricks is fashionable changes every
year and the fashion is the part to distrust. The ranking underneath it does not move: the spread
is the enemy, how finely you may rule is the lever, and an identity that costs nothing always
beats a cleverer way of rounding.
