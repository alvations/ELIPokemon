---
id: "202"
slug: calibrated-decision-training
style: pokemon
category: frontier
difficulty: advanced
question: "Jev is trained against a proper scoring rule rather than human preference. What does that actually change?"
tags: [calibration, brier-score, proper-scoring-rules, rlhf, reward-design]
---

# Contest ribbons versus a Battle Tower streak

There are two ways to make a Pokémon look good, and they are not the same training.

In a **Pokémon Contest** you win by appeal. A panel judges Cool, Beauty, Cute, Smart or Tough, you
feed Poffins to raise the right condition, and you chain moves for combo points. The reward is a
person's impression. In the **Battle Tower** you win by winning. The streak counter goes up or the
run ends, and no judge is consulted.

Training against human preference is Contests. Training against a proper scoring rule is the
Tower. Both produce a strong Pokémon; only one of them produces a Pokémon whose numbers you can
trust.

## Why appeal and honesty pull apart

Contest judging rewards boldness and flair. A Trainer who declares the sweep is on wins the room
over one who says *this is roughly a coin flip and I would rather switch*. That is the whole
mechanism behind a model that sounds certain and is not — not a defect bolted on late, but the
thing the scoring was pointing at.

Counting wins alone does not fix it either. If the only question is whether the top move was the
right move, the best strategy is **No Guard**. Machamp's ability makes every move hit, both ways —
Dynamic Punch's 50% becomes a certainty. Wonderful in battle, useless as information: the number
on the move stopped carrying any.

## What "proper" means

The games already do this properly. Focus Blast says 70 and misses roughly three times in ten.
Hydro Pump says 80. Zap Cannon says 50 and means it. Sheer Cold's 30 is honest enough that it
also refuses outright against a higher-level target. The number is a promise the engine keeps, and
a scoring rule is **proper** when keeping the promise is also what scores best — overstate and
the misses cost you more than the hits pay.

```
   Claimed accuracy vs what actually lands
   100 ┤                                            ·
       │                                      ·    /
    80 ┤  "it never misses" ──►  ●      ·   /
       │                            ●      /
    60 ┤                                /  ●
       │                             /       ●
    40 ┤                          /             ●   ◄── Hydro Pump sits
       │                       /                       on this line
    20 ┤                    /                       ●
       │                 /
     0 ┼───────────────────────────────────────────────
       0       20       40       60       80      100
                     accuracy printed on the move

   ● = the Contest-trained Trainer: says 90, lands 60
   Brier charges for the vertical gap. A win counter never sees it.
```

## The catches, which are real

* **It needs a Tower.** You can only score against an outcome that resolves. Typed decisions
  resolve; an essay about Kanto does not.
* **Honest is not the same as useful.** A Pokémon that only ever uses **Splash** is perfectly
  predictable and accomplishes nothing. You want the numbers honest *and* the moves decisive.
* **A streak is built against one ladder.** Calibrated in the Battle Tower, then handed a format
  with different rules and a different opponent pool, and the percentages drift.
* **The measuring stick has its own bugs.** Bin the results coarsely enough and a badly
  miscalibrated Trainer looks fine. Plot the curve.

## What a Gym Leader is listening for

That you know why counting wins alone breeds a No Guard Trainer, and that you can say what makes
a scoring rule proper. The strongest version goes further: the percentage is only worth having if
somebody **acts on it**. Knowing Focus Blast is 70 and clicking it anyway with no backup is the
same as never having been told.

## Where this stands, September 2026

TypeSafe's recipe is proprietary and unpublished. The idea underneath is not, and is not new —
honest odds were scoring battles long before any of this. That part transfers; the brand name
will date.
