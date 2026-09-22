---
id: "265"
slug: quantisation-formats-and-group-size
style: pokemon
category: optimization
difficulty: advanced
question: "What is actually inside a quantised model file? Walk me through k-quants, group size, and the hardware 4-bit formats."
tags: [gguf, k-quants, group-size, mxfp4, nvfp4]
---

# The judge never tells you the number. He tells you which drawer it is in.

Every **Individual Value** on your **Gengar** is a whole number from 0 to 31. Thirty-two
possibilities, five bits, and the game knows all six of them exactly. You walk it into the
**Battle Frontier**, hand it to the judge, he says "**Fantastic**" — and now you know which drawer
it is in.

A judged **Gengar** is never judged at one fineness, and three questions get you through any
report ever printed: **how many numbers share a single verdict, what does the verdict carry
besides the word, and which numbers were left out of the rounding entirely?**

## The ladder, priced

Every verdict costs something to write down, and the writing comes out of the same budget as the
numbers themselves.

```
   six values, each 0–31

   how the verdict is given          verdicts     cost        what you learn
   ──────────────────────────────────────────────────────────────────────────
   one line for the whole Gengar         1        tiny        almost nothing
   one line per stat                     6        small       the usable one
   one per stat + a second reading      12        double      breeding-grade
   the six numbers, written out          6        full        everything
   ──────────────────────────────────────────────────────────────────────────

   Kanto did not have thirty-two. It had SIXTEEN — and every one of them
   for a whole Tauros lived in two bytes.
```

How many numbers share a verdict is the whole dial. One line for the whole **Gengar** is nearly
always a mistake; one line per stat is nearly free and should be the floor. Everything worth
arguing about lives between those two.

## The same sixteen bits, spent much better

A boxed **Tauros** in **Kanto** got exactly **two bytes** for its entire potential. Sixteen bits.
You could spend those sixteen bits as one number summarising the **Tauros** overall — and it would
be worthless, because a **Shuckle** with a perfect Defense and a hopeless Speed averages out to
nothing anybody can breed from.

What the game did instead:

```
   two bytes = 16 bits, split FOUR WAYS
   ─────────────────────────────────────────────────────────
   Attack  4 bits   0–15
   Defense 4 bits   0–15
   Speed   4 bits   0–15
   Special 4 bits   0–15
   ─────────────────────────────────────────────────────────
   HP      not in there at all — Kanto WORKED IT OUT from the
           other four, because there was no room for a fifth.

   Same sixteen bits. One number for the Tauros tells you nothing;
   four numbers, one per stat, tells you which Tauros to keep.
```

The modern judge's drawers carry more than a word: they carry **both ends**. "Somewhere in the
high twenties" gives you a floor as well as a ceiling, and a verdict that only said "at least that
high" would cost exactly the same to write and be worth half as much. Knowing where a range
*starts* is most of what separates a good scheme from a lazy one.

Then the **characteristic** line reads the same six numbers again from a different angle: it names
which of them is highest — "Likes to run" means Speed, and on a **Regieleki** with 200 base Speed
that is exactly the one you were hoping for — and it phrases that one of five ways. Two coarse
readings of the same value, taken differently, pin it far tighter than either alone.

## "Perfect" is a policy, not a type

Here is what people get wrong. Nobody breeding a **Gengar** in the **Day Care** with a **Ditto**,
a **Destiny Knot** and an **Everstone** is chasing 31 six times, and a serious breeder will say
so:

* **Speed and Special Attack** get every egg and every hour. That is what a **Gengar** is for.
* **Attack is deliberately driven to zero.** A **Gengar** never uses it, and a lower Attack means
  less damage when **Swagger** or a **Confuse Ray** turns it on itself, and less from an
  **Umbreon**'s **Foul Play**, which hits using *your* Attack rather than its own. The worst
  possible value is the correct one.
* **Defense is left wherever it landed** and nobody ever looks at it again.
* **Some things are never rounded at all**: the species, the Ability, the **Original Trainer**,
  the **Egg Group** it came from. Store those approximately and they mean nothing.

So "a perfect **Gengar**" is six separate decisions wearing one word, and what any given Trainer
means by it is a recipe rather than a standard. The reasoning underneath never changes: spend the
care where the error travels furthest, and on **Gengar** it travels through Speed.

## Watch which numbers ever come up

Before deciding how carefully to record each stat, run the Pokémon through the battles it is going
to be in and watch which numbers ever get touched. **Skarmory**'s 40 Special Attack does not enter
a single calculation it will ever be part of. **Shedinja** has 1 HP and **Wonder Guard**, and no
amount of care about that 1 changes anything.

Two honest things about doing it. It buys less than people expect — twenty **Battle Tower** rounds
told you as much as two thousand did, and the Trainers who insist on the two thousand are mostly
buying confidence. And it leaks: once you have decided what to round by watching one set of
opponents, testing against those same opponents proves nothing
([267](267-evaluating-a-quantised-model.md)). Below a certain coarseness it stops being optional,
though — judge a **Ditto** on drawers alone and you will breed from the wrong one for a month.

## Two ladders: thirteen rungs, or the whole number

```
   THE STAGE LADDER                   THE STAT ITSELF
   ────────────────                   ───────────────
   thirteen rungs and no others       any whole number the build reaches
   Dragon Dance  +1  = ×1.5           ────────────────────────────────────
   Swords Dance  +2  = ×2             dear: the real figure, carried
   Belly Drum    +6  = ×4             in full, every time
   Leer          −1  = ÷1.5 on them
   ────────────────                   Gengar's 110 Speed is 110. Not a rung.
   cheap: one number, −6 to +6

   You cannot ask a stage for ×1.7. You take Dragon Dance's ×1.5 and lose
   the rest. That is not sloppiness — the rungs are fixed, and the ladder
   is fast precisely because there is nothing left to work out.
```

**Belly Drum** is the coarse ladder at full stretch: one move, straight to the top rung, exactly
×4, and half your HP gone to pay for it. The stat underneath is the fine ladder: dearer to carry,
lands exactly where the build put it. Both are in every battle at once and neither is wrong — they
answer different questions.

## What the readout actually looks like

```
   ┌────────────────────────────────────────────────────┐
   │  GENGAR        scale in use: 0–31   (Kanto: 0–15)  │
   │  overall:      "outstanding"                       │
   │  ───────────────────────────────────────────────── │
   │  HP            Very Good                           │
   │  Attack        No Good         ← as low as it goes │
   │  Defense       Decent                              │
   │  Sp. Atk       Best                                │
   │  Sp. Def       Pretty Good                         │
   │  Speed         Best                                │
   │  ───────────────────────────────────────────────── │
   │  characteristic: "Alert to sounds"                 │
   └────────────────────────────────────────────────────┘
```

Read the six lines before you trust the one at the top. And know this much about the words:
**which phrase covers which numbers has changed between generations.** The scale went from sixteen
to thirty-two, the judge moved from the **Battle Frontier** to the storage boxes, the wording
moved with him, and a phrase you remember from an older game is not a number in a newer one. The
per-stat lines are the truth. The summary is a label.

## What a Gym Leader is listening for

* Sixteen bits either way. Why is four-by-four so much better than one number for the **Tauros**?
* What does a drawer with a floor give you that a drawer with only a ceiling does not?
* Why can **Dragon Dance** only ever be ×1.5, and what does that cost you?
* On a **Gengar**, which two stats would you take care over, and which would you drive to zero?

## Where this stands, September 2026

**Kanto**'s storage is from the game's own code, which I read: a boxed **Tauros**'s whole
potential was two bytes split four ways, with HP's share worked out rather than stored. The stage
ladder is from the same kind of source — thirteen rungs, **Swords Dance** exactly ×2, **Belly
Drum** exactly ×4, **Leer** exactly the inverse of **Dragon Dance** — and it has not moved in
twenty years. The modern 0-to-31 range and the judge handing out drawers instead of numbers are
stable across every recent generation. **What I have deliberately not written down is which phrase
covers which numbers**, because that mapping has changed between games and a remembered version of
it is worth less than nothing. Go and read the judge in the game in your hand. The three questions
at the top outlive every generation that has been printed.
