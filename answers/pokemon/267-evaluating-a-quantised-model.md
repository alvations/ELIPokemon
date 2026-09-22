---
id: "267"
slug: evaluating-a-quantised-model
style: pokemon
category: optimization
difficulty: intermediate
question: "A quantised build's perplexity moved by 0.15. Is that fine? How would you evaluate it honestly?"
tags: [quantisation, evaluation, perplexity, kl-divergence, calibration]
---

# The average damage moved by a hundredth. The guaranteed KO did not survive it.

Every attacking move rolls a die. Not a coin — a sixteen-sided die, and the game really does work
it out that way: the damage it calculated is multiplied by a whole number of per cent from **85 to
100**, sixteen values, one picked at random, remainder thrown away, and never less than 1.

So when a Trainer tells you their trimmed-down team does "0.2% less damage on average", ask what
that is 0.2% of. The **Damage Roll** alone spans fifteen points. Their number is a seventy-fifth
of the width of the die. It is invisible — and it is also not the number that decides anything.

```
   Garchomp's Earthquake into Heatran. Fire and Steel, so Ground lands
   at four times — the most lopsided calculation anybody runs.

   BEFORE          all sixteen rolls take the last of Heatran's HP.
                   ────────────────────────────────────────────
                   85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
                    ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔   ✔
                   GUARANTEED. You built the whole team on this.

   AFTER  a trim costing a fifth of one per cent, on a calculation
          that was killing with less than that to spare
                   ────────────────────────────────────────────
                    ✘  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔  ✔   ✔
                   fifteen times out of sixteen.

   The AVERAGE moved by a fifth of a per cent. Certain became 93.75%,
   and the battle you lose to it will look exactly like bad luck.
```

And that is before **Leftovers** ticks a sixteenth of **Heatran**'s HP back at the end of the
turn, or a **Focus Sash** on a full-health **Heatran** leaves it standing on 1 HP — both take that
kill and make it not one. The thresholds are everywhere and the average never sees any of them.

## The same trim, turn by turn

Put the trimmed team and the full one through the same **Battle Tower** opponents, in the same
order, and score every turn by how much worse the trimmed team's choice was:

```
   a thousand turns, trimmed against full

   the middle turn        worse by  0.02 %   ← nothing whatsoever
   ────────────────────────────────────────────────────────────
   1 turn in 100          worse by 19.6 %
   1 turn in 1,000        worse by 56.1 %
   the single worst turn  worse by 98.7 %    ← Ice Beam was on the
                                               field and it clicked
                                               Dragon Claw
   ────────────────────────────────────────────────────────────
   and on 8 turns in every 100 it chose a DIFFERENT MOVE ENTIRELY.
```

A 0.2% average and a change of mind once every twelve turns are the same team. The average washed
the damage away, because an average is an average and the damage is not spread like one. **That is
the whole answer to "is 0.2% fine": 0.2% is not a measurement of the thing you care about.**

## What to look at instead, in the order I would look

**1. The difference from the full team, not how good the trimmed one is.** Send both down the same
**Victory Road**, against the same **Elite Four**, in the same order, and count the turns where
they picked differently. Nothing to score, nothing to argue about — and it answers the real
question, which is *is this still the same team*, rather than a stand-in for it.

**2. The shape of the misses, not their size.** If the trimmed team's surprises are as often good
as bad, that is the die. If they all point one way, that is the trim. Above, the bad tail runs to
−56% and the good one to +27%: damage, not luck.

**3. Test in the bracket you are entering.** Same **Regulation G** list, same held items — a
**Choice Scarf** changes every **Speed Tier** you assumed — and the same length of streak. A team
checked against **Cynthia** once and then entered in **VGC** has not been checked.

**4. The things that go first, by name.** The **Critical Hit** that ignores the **Bulk Up** you
spent a turn on and turns a two-hit kill into a three. **Protect** on the exact turn it had to be
**Protect**. The **Speed Tier** where your **Garchomp** sits one point over somebody else's. The
far end of a fifty-battle streak rather than the first round of it. And **Shedinja**, standing
there with 1 HP and **Wonder Guard**, which either takes a super-effective hit or takes nothing at
all — the rarest thing you will face and the one where a trimmed team is worst.

**5. Enough battles to know what the die looks like.** Sixteen rolls, plus a **Critical Hit**
landing on its own schedule, plus a genuine **Speed Tier** tie decided by a coin flip. One battle
proves nothing and ten barely more. **If the difference you are claiming is smaller than a Damage
Roll, you have not measured a difference.**

## You practised against the team you tested against

The subtlest one. Whoever trimmed the team decided *what* to trim by watching some set of battles.
Measure the trimmed team against **that same set** and you are measuring the fit and calling it
the result.

```
   practised against ──► the trim was chosen to suit THESE opponents
                                    │
                                    ▼
   tested against ══ the same ones ══► the damage measured is TOO SMALL
   tested against ── fresh ones ─────► the damage measured is real

   trimmed after watching ten thousand Battle Tower rounds   0.20 % loss
   trimmed after watching none at all                        0.25 % loss
                                                             ───────────
   the ten thousand rounds bought 0.05 %, measured against the very
   opponents they were watched on.
```

And the fact that should keep everybody modest: watching **more** battles does not reliably help.
Twenty, two hundred, two thousand, twenty thousand — they come out in no dependable order. If more
practice does not dependably improve the trim, nobody fully understands what the practice is
doing. Practise against what you will meet, test against something else, and say which was which.

## "Trimming is fine" is a claim about a Pokémon, not about trimming

Two Pokémon, the same amount trimmed off each:

```
                        Regieleki            Garchomp in the mirror
   ────────────────────────────────────────────────────────────────────
   base Speed            200                  102 — and so is Cynthia's
   the margin            outruns Dragapult    built to sit ONE POINT
                         at 142, Jolteon at   above the Garchomp
                         130, Weavile at 125  opposite
   lose one point        nothing happens      the tie is a coin flip now,
                                              and the coin decides who
                                              throws Earthquake first
   ────────────────────────────────────────────────────────────────────
```

**Regieleki**'s 200 has slack in it and **Dragapult**'s 142 is not close enough to matter. A
**Garchomp** tuned to beat another **Garchomp** by one point has no slack at all, and the tuning
is invisible from outside — the two look identical on the summary screen. A Pokémon thrown
together tolerates trimming; one optimised to the last point does not. **Nothing about how much
you trimmed tells you which of the two you are holding.**

## Where the damage actually lives

In the rare matchups — and your practice is made of common ones. That is not bad luck, it is the
same sentence twice: the trim hurts most where the decision was finely balanced, or where some
freak number like **Shedinja**'s single hit point was carrying the entire plan, and those are
exactly the battles too rare for you to have practised many of. The one turn in a thousand that
goes 98.7% wrong is not a random turn. It is a rare one.

So the honest position is: **your practice will always understate the damage, and you should say
so.** Sample the Trainers you actually meet, over-practise the freaks on purpose, and keep the
untrimmed team in the boxes so you can stand the two side by side the first time something goes
strangely wrong.

## What a Gym Leader is listening for

* The average moved 0.2% and it picks a different move on 8 turns in 100. Which goes in the
  report?
* How would you spot that a trim was fitted to the practice opponents, if you did not do the trim?
* Why does a **Garchomp** built to win a tie by one point suffer where a **Regieleki** does not?
* What would you check to catch a failure that only shows up at battle forty of a streak?

## Where this stands, September 2026

The sixteen-sided **Damage Roll** is from the game's own code, which I read: a whole number from
**85 to 100** per cent applied to the calculated damage, remainder discarded, floor of 1 — and
from the same source, a **Critical Hit** really does ignore the defender's raised Defense. The
base Speed figures are from the published tables: **Regieleki** 200, **Dragapult** 142,
**Jolteon** 130, **Weavile** 125, **Garchomp** 102, and a genuine tie settled at random.
**Heatran** being Fire and Steel makes **Earthquake** land at four times on it, which is why that
calculation is the one everybody quotes. The turn-by-turn percentages come from a real measurement
of a real trimmed build and belong to that build; do not quote them as properties of trimming in
general. What travels is the method: compare against the untrimmed team rather than scoring the
trimmed one, read the tail and not the average, name who you practised against, and assume the
damage you can see is smaller than the damage you have.
