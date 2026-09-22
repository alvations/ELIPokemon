---
id: "272"
slug: reading-a-kernel-benchmark
style: pokemon
category: optimization
difficulty: intermediate
question: "Someone shows you a kernel benchmark with a 12x speedup. What do you check before you believe it?"
tags: [benchmarks, warm-up, autotuning, determinism, scepticism]
---

# "It hits twelve times harder" is a ratio, and nobody ever says harder than what.

[212](212-reading-model-announcements.md) sorts a boast into four kinds before arguing with it. A
boast about a Pokémon sorts the same way, and it sorts *better*, because the whole calculation is
written down in the game and you can walk into the same patch of grass yourself. Nearly everything
below takes ten minutes and a **Vs. Seeker**, and nearly nobody does it.

```
  ┌────────────────────┬────────────────────────────────────────────────────────┐
  │ 1. CHECKABLE NOW   │ What did it hit? At what level? Was it holding its     │
  │    (ten minutes)   │ item? Ask, and never argue about the answer.           │
  ├────────────────────┼────────────────────────────────────────────────────────┤
  │ 2. CHECKABLE WITH  │ Set it up yourself. Same Nature, same stat spread,     │
  │    WORK            │ same weather, same side of the field. Usually repeats. │
  ├────────────────────┼────────────────────────────────────────────────────────┤
  │ 3. ONLY ON YOUR    │ "It sweeps." Your team, your bracket, your opponents,  │
  │    OWN TEAM        │ your Speed Tier, the things you actually face.         │
  ├────────────────────┼────────────────────────────────────────────────────────┤
  │ 4. NOT CHECKABLE   │ A multiplier with no target, no level and no item.     │
  └────────────────────┴────────────────────────────────────────────────────────┘
```

## The eight questions, and what each one turns up

**1. Twelve times harder than what?** Ask what it hit. If the answer is a level 5 **Magikarp**
that knows nothing but **Splash**, the boast is a true statement about **Magikarp**, not about the
attacker. A **Bug Catcher**'s **Caterpie** is a denominator too, and it is not a useful one.

**2. Does the boaster already know the target was weak?** Very often they will tell you themselves
— *"well, it hadn't evolved yet"* — and then quote the number anyway. When somebody volunteers
that the denominator was soft, believe them, and move the fame from the numerator.

**3. Was the loser given its item, and the winner given two?** A **Rhyhorn** that came in with no
**Eviolite**, against a **Gyarados** holding a **Life Orb** after two **Dragon Dance**s, is not a
comparison. Both sides have to get the same care, and they almost never do.

**4. The first turn is not the average.** You do not judge anything by the turn it comes in on.
**Stealth Rock** took a chunk on the way in. **Gyarados** has **Intimidate**, so the other side's
Attack is already down a stage. **Dragonite**'s **Multiscale** halves the first hit it takes and
nothing afterwards. And the very first time you meet a species there is an animation and a
**Pokédex** registration to sit through that you will never sit through again.

```
   what an honest report looks like
        "the mean of 100 turns, after 50 turns of settling in"
   what you usually get
        "I did it once and it worked"
```

**5. Which matchup — and this is the big one.** A number quoted off a **Rhyhorn** that had been
**Screech**ed twice is a real number from a battle nobody has. Worse, the matchup chooses the
*kind* of problem. From [271](271-training-kernels-and-fusion.md), how much you get per pace on
the 128-patch route is exactly how many turned up at each patch:

```
   1,024 to get through  →  64 a patch  → far under 295 → feet are the problem
                                                        → one sweep wins hugely
   8,192 to get through  → 512 a patch  → past 295      → arms are the problem
                                                        → the same sweep wins little
```

Quoting the 1,024 morning is the version where the answer is biggest. That is not cheating. It is
a choice, made by everybody, and it is why you go and walk your own route.

**6. Which half of the trip?** [268](268-roofline-decode-and-prefill.md): the clearing sits 29×
over the Warden's ratio and the long walk sits 261× under it. A trick that saves paces transforms
one and is invisible in the other. "Twice as good" with no trip named is not a result.

**7. Were the animations on?** Time a single quick exchange with **Battle Effects** on and you are
largely timing the animation ([270](270-serving-stack-around-the-kernel.md)). Turn them off and
the ceremony the new move was "saving" vanishes from both sides, and the margin goes with it.

**8. Did the outcome actually change?** Here is the one everybody forgets, and the games are more
honest about it than most benchmarks:

```
   every attack is multiplied by one of SIXTEEN values, 85 through 100
        best roll ÷ worst roll  =  100 ÷ 85  =  1.176
   a Critical Hit multiplies by 1.5, and lands rarely
   a genuine Speed tie is settled by a coin flip, freshly, every single turn
   a Quick Claw goes first one time in five
```

So a move that leaves the target on 1 HP at the low roll and faints it on the other fifteen is a
**15 in 16** attack, and it will be described to you, honestly, as "it one-shots". Needing that
twice in a row is 1 in 256. **The same battle, run twice, is two different battles** — and if the
**Speed Tie** goes the other way, it is not even close.

## The trap that catches good Trainers

Watch the twelve get built out of nothing but legal, ordinary choices:

```
   Life Orb                    × 1.3
   STAB on Waterfall           × 1.5
   Water into Arcanine         × 2
   two Dragon Dances, +2       × 2
   high Damage Roll vs low     × 1.176
   a Critical Hit              × 1.5
                             ─────────
                               × 13.8    and not one line of it is invented
```

Nobody lied. Every multiplier is in the game. And the same **Gyarados**, on a turn where it has
not set up, the roll comes in low and nothing crits, is up by the **Life Orb**'s 1.3 and nothing
else — the same Pokémon, the same **Waterfall**, an honest 13.8 and an honest 1.3.

**And beware two changes reported as one.** "I gave it a **Life Orb** and it hits three times as
hard" — while also mentioning, in passing, that the **Magikarp** evolved into **Gyarados** in
between. Both true. The **Life Orb** is worth 1.3 of it. The same applies to any "carries far
less" that quietly includes leaving **Outrage** with the **Move Deleter** all season.

## What to do instead

Decide the measurement before you hear the boast. Fix the number of turns, not the clock. Use your
own bracket, your own opponents, your own **Speed Tier**. Settle in explicitly and say for how
long. And report the **worst** outcome as well as the average — a set that wins more often and
loses catastrophically when it loses has not won. Then check the two sets land the same Pokémon on
the same HP on a fixed opening, so that question 8 has an answer instead of a shrug.

## Where this stands, September 2026

Every line above came out of the games themselves, not somebody's account of them. The particular
route, the particular patch counts and the particular items are this season's and will move.

What keeps is the shape of the mistake, and it is not dishonesty. **A boast is a ratio between two
set-ups, and the boaster picked both.** Every dial in this answer — who the target was, what each
side was holding, how long it settled in, which matchup, which half of the trip, whether the
animations ran, how much slack you allow — has a defensible setting that makes the number bigger
and a defensible setting that makes it smaller. Nobody has to lie for 13.8 and 1.3 to describe the
same **Gyarados**. The only defence that has ever worked is fighting the battles you are actually
going to fight, and the only reason not to is that you have not set the team up yet.

## What a Gym Leader is listening for

* Name three ways to make an honest number twice as impressive without lying once.
* Why can the same sweep be a twelvefold win and a small one on the same route?
* Two identical **Gyarados**, same move, same target. Why might the battles end differently?
