---
id: "069"
slug: precision-recall-f1
style: pokemon
category: evaluation
difficulty: core
question: "Explain precision, recall and F1, and when to optimise for each."
tags: [precision, recall, f1, confusion-matrix, threshold]
---

# Precision and recall: catching Pokémon in tall grass

You're hunting a **shiny Charizard**. Your detector says "shiny!" and you throw an Ultra Ball.

Four things can happen:

```
                       YOUR DETECTOR SAYS
                     "SHINY!"      "skip it"
                   ┌────────────┬──────────────┐
      actually     │   ✅ TP     │   😱 MISS    │
   R   shiny       │  caught it! │  it fled and │
   E                │             │  you'll never│
   A               │             │  see it again│
   L               ├────────────┼──────────────┤
      not          │   😤 FALSE  │   ✅ TN      │
      shiny        │    ALARM    │  correctly   │
                   │  wasted a   │  ignored     │
                   │  Ultra Ball │              │
                   └────────────┴──────────────┘
```

## The two questions 🎯

**🎯 Precision — "when I throw a ball, do I catch something good?"**

Of everything you flagged, how much was real? Low precision means **wasted balls.**

**🔍 Recall — "of all the shinies out there, how many did I get?"**

Of everything real, how much did you catch? Low recall means **shinies got away.**

## They fight each other ⚖️

And here's the crucial bit: **it's the same detector.** You're just turning a dial.

```
   🔒 STRICT — only flag a definite shiny
      → almost every ball lands.        precision ✅✅✅
      → you walk past dozens of shinies. recall ❌

   🌊 LOOSE — flag anything that sparkles
      → you catch nearly every shiny.    recall ✅✅✅
      → and 400 Rattata.                 precision ❌
```

📌 **Where you set the dial is a business decision, not a modelling one.** Your detector already
gives you the whole range. Which end you want depends entirely on what a mistake costs.

## Which end do you want? 🤔

**🎯 Precision, when a false alarm is expensive.**

*Auto-releasing Pokémon you flag as duplicates.* Wrongly release someone's shiny Charizard and it
is gone from the PC box forever. Be **certain** before acting. Missing a few duplicates is fine.

**🔍 Recall, when a miss is a disaster.**

*Scanning for a roaming Latias that will flee the moment you engage.* You get one chance. Throw a hundred wasted
balls if it means catching the one that mattered — the ball is cheap and the miss is forever.

**⚖️ Both, when you need one number to compare two detectors.**

Combine them — but combine them **harshly**. Here's why that matters:

```
   A detector that shouts "SHINY!" at absolutely everything:
      recall:    100% ✅  (caught every shiny — technically true!)
      precision:   5% ❌  (and 8,000 Rattata)

   Naive average:  52%  ← "not bad?!"  💀 completely wrong
   Harsh combine:  10%  ← ✅ correctly identifies this as useless
```

The harsh version refuses to let one great number cover for a terrible one. Which is exactly what
you want, because that detector is worthless and the naive average called it mediocre.

## Three traps 🕳️

**1. 📊 "99.9% accurate" is usually a lie by omission.**

Shinies are 1 in 4,096. A detector that says **"not shiny"** to literally everything is **99.98%
accurate.**

It has never once been useful. It cannot be used. And it beats your carefully built detector on
accuracy.

📌 **If someone quotes accuracy on something rare, that's your first question.** Always.

**2. 📏 Your dial drifts.** Set it perfectly in Kanto, move to a different region with different
lighting, and it's now wrong. **Re-tune it periodically** — it isn't a one-time setting.

**3. 🎯 Sometimes only the top few matter.**

You have **ten Ultra Balls.** Not a hundred. Ten.

Then "how many shinies did I find overall?" is the wrong question entirely. The only question is:
**of my top ten candidates, how many are real?**

Recall across the whole grass is irrelevant when you can only act ten times. This is the right way
to think about almost any triage system, and almost nobody measures it.
