---
id: "253"
slug: speculative-decoding-exactness
style: pokemon
category: optimization
difficulty: advanced
question: "Speculative decoding claims to be exact, not approximate. Why is that true?"
tags: [speculative-decoding, rejection-sampling, exactness, inference, sampling]
---

# The Old Rod, kept or thrown back by a rule that puts the difference back.

You are standing on **Route 119** with the **Old Rod** the fisherman in **Dewford Town** handed
you, and what you actually want is what the **Good Rod** pulls up. The Old Rod is faster to get
out and it only ever plays one round of dots, so most casts are done before a Good Rod cast has
finished asking. So cast the Old Rod, and then decide whether to keep what surfaced by a rule that
compares the two rods' tables — and when you throw one back, re-roll on the *difference* between
them rather than on the whole table again.

Do it that way and the species that end up in your **Poké Ball**s come out in exactly the Good
Rod's proportions. Not roughly. Exactly — for any rod you draft with, including a bad one. A bad
rod means more throwing back and less time saved. It cannot change what you end up holding,
because the throw-back rule is not a patch for a lucky guess. It is bookkeeping.

[033](033-speculative-decoding.md) is where guessing ahead is introduced and
[230](230-multi-token-prediction-and-drafting.md) does the sums on what it saves. This one is the
rule itself, and the small print on the back of it.

## The rule, on one cast

Write `q` for the rod you are casting and `p` for the rod you wish you were casting. You get
species `y` on the line. Keep it with probability `p(y)/q(y)`, capped at 1. If you throw it back,
re-roll on `max(0, p − q)` — every species the good rod gives *more* of than the cheap one, in
proportion to the shortfall, and nothing else.

```
  P(end up with y)  =  P(cheap rod hooks y) · P(keep it)   +  P(threw one back) · share(y)

  case  p(y) ≥ q(y):   q(y)·1            + (p(y) − q(y))   =  p(y)      ✔
  case  p(y) <  q(y):  q(y)·(p(y)/q(y))  + 0               =  p(y)      ✔
```

The only thing that needs checking is that you throw back exactly as often as the shortfall
demands:

```
  P(keep)         =  Σ_y min(p(y), q(y))   =  α
  P(throw back)   =  1 − Σ_y min(p, q)     =  Σ_y max(0, p − q)        ✔
```

That second line is the one to carry around, because it is also the whole story of which rod is a
good stand-in for which:

```
  α  =  Σ min(p, q)  =  1 − half the total gap between the two tables
```

**How often you get to keep a cast is one minus the gap between the two rods' tables.** Nothing
else about the cheap rod counts. Not what it cost. Not that the **Super Rod** in **Mossdeep City**
is plainly the better item. Only how close its table sits to the table you actually wanted, in the
water you are actually standing in.

## The Route 119 numbers

Route 119's water, by the book. The Old Rod pulls **Magikarp** 70% of the time and **Tentacool**
the other 30%. The Good Rod pulls Magikarp 60%, Tentacool 20%, and **Carvanha** 20% — and the Old
Rod has never hooked a Carvanha in its life.

```
  species     Magikarp Tentacool Carvanha    α = Σ min(p,q) = 0.60 + 0.20 + 0 = 0.80
  ────────────────────────────────────────    the gap = ½(0.10+0.10+0.20) = 0.20
  q Old Rod     0.70     0.30     0.00        α = 1 − gap   ✔
  p Good Rod    0.60     0.20     0.20
  ────────────────────────────────────────
  keep w.p.      6/7      2/3       —         capped at 1
  thrown back   0.10     0.10      0.00       the surplus the cheap rod hooks
  re-roll on      0        0       1.00       0.20 of shortfall, all of it Carvanha

  end up Magikarp:  0.70 × 6/7           = 0.60   ✔ the Good Rod's own share
  end up Tentacool: 0.30 × 2/3           = 0.20   ✔
  end up Carvanha:  0.20 (thrown back) × 1.00 = 0.20   ✔
```

Eight casts in ten are kept, and the two you throw back both come back Carvanha, which is the only
thing the Good Rod has that the Old Rod does not. Now do it with a rod that barely overlaps at
all. Step one route west to **Route 118** and use the Good Rod to stand in for the Super Rod,
whose five slots there are **Sharpedo** at 40% and Carvanha at the remaining 60%:

```
  q Good Rod   Magikarp 0.60  Tentacool 0.20  Carvanha 0.20  Sharpedo 0.00   α = 0.20
  p Super Rod  Magikarp 0.00  Tentacool 0.00  Carvanha 0.60  Sharpedo 0.40

  thrown back 0.80;  re-roll on (0, 0, 0.40, 0.40) → half Carvanha, half Sharpedo
  end up Carvanha:  0.20 + 0.80 × ½ = 0.60  ✔     end up Sharpedo:  0.80 × ½ = 0.40  ✔
```

Four casts in five thrown back, and the bucket *still* comes out as a Super Rod bucket. Same
guarantee, a fifth of the saving. That lopsidedness is why you can switch this on mid-streak: the
worst thing a bad rod does is waste your afternoon.

## Casting a run of them

Check the run front to back. You only look at the second cast if you kept the first, so each cast
is being judged against the water as it really stands after everything before it. The moment you
throw one back, every cast after it goes in the bucket too — they were guesses about a line that
never happened.

And if you keep the whole run, you have already done the work of asking what the good rod would
give *next*, so you take that one free. That is the extra fish at the end of a clean run, and it
is why a run of `γ` guesses is worth more than `γ` fish when it goes well.

If you are not sampling at all — if you only ever want the single most likely thing in the water —
the rule collapses to "keep it if it is the same species the good rod would most likely have
given", and a plain name comparison is the whole algorithm. It still deserves the word exact.

## What the rule does not promise

Every one of these has bitten somebody.

* **Same table, different fish.** Exact means the *proportions* match, not that you get the same
  Magikarp. Its IVs, its Nature and its gender are rolled at the moment it surfaces, and nothing
  about this rule pins them. Worse, the numbers come off one stream: putting extra casts in front
  of it shifts every roll after it, so the same seed does not replay.
* **Correct against the table you are really drawing from.** Walk the **Tall Grass** with a
  **Repel** burning and every entry below your lead's level has been struck out of the table — you
  are drawing from a narrower one than the printed list. Check a guess against the printed list
  and you are exact about the wrong thing. (A Repel never touches a fishing line; that is exactly
  the sort of detail that has to be right.)
* **Sometimes the printed table is not the table.** Six of Route 119's 447 fishing spots hold
  **Feebas**, and on one of those the water ignores the rod's slots outright about half the time.
  Nothing on the sign says so. If something upstream is overriding the table, the keep rule has to
  know.
* **None of this promises the cast lands.** "Not even a nibble…" and "It got away…" are still the
  usual answers, and the Super Rod asks for up to six clean rounds in a row before anything is on
  the hook. That is your afternoon, not your bucket.
* **"Close enough, keep it" is a different rule.** Plenty of anglers run one. It is a fine way to
  fish and it is not this, and a hall that runs one while quoting this rule's guarantee is selling
  you something. Ask which they use.

## What a Gym Leader is listening for

* Show that keeping happens exactly `1 − gap` of the time, and say what follows for picking a rod.
* Why is everything after a thrown-back cast wasted?
* Where does the Repel go in the arithmetic, and what breaks if you apply it only to the guess?

## Where this stands, September 2026

The rule is permanent. It is four lines over two tables, it does not care which rod or which
route, and the line that says the keep rate is one minus the gap will still be how you pick a
stand-in rod long after every water on this map has been re-drawn. What will move is the small
print: which halls strike Repel entries out before checking and which after, what the "close
enough" house rules get called, and whether the strict rule is the default. Those were read off
the water itself in September 2026. Read them again in the hall you are actually fishing in — the
guarantee lives in the rule they run, not in the rule somebody wrote down.
