---
id: "071"
slug: class-imbalance
style: pokemon
category: fundamentals
difficulty: core
question: "How do you handle severe class imbalance?"
tags: [imbalance, smote, class-weights, focal-loss, threshold-tuning]
---

# Class imbalance: one shiny per four thousand Pokémon

You're training a shiny detector. Your footage contains **4,000 ordinary Rattata and 1 shiny
Gyarados.**

Your detector learns the obvious lesson: **"nothing is ever shiny."**

99.98% accurate. Utterly useless.

## Start by suspecting the question 🤔

The instinct is to go fix the footage. Usually that's not the problem.

**Usually it's one of these three:**

1. 📊 **You're grading it wrong.** "Accuracy" on something one-in-four-thousand is meaningless.
2. 🔢 **You genuinely don't have enough shinies.** One example is one example. No technique conjures
   information that isn't there.
3. 💰 **You never told it that missing a shiny is worse than a wasted ball.**

Reaching for the footage first is the standard mistake. Try these in order instead.

## The order to actually try things 🪜

**1. 📊 Fix the scorecard.** Stop measuring accuracy. Measure *"of the Pokémon I flagged, how many
were shiny?"* Astonishingly often the detector was fine all along and only the grading was broken.

**2. 🎚️ Turn the dial down. ← try this first, always**

Your detector probably **ranks** perfectly well. It says "3% chance shiny" for the red Gyarados and
"0.001%" for the Rattata. That's a correct ranking!

The bug is that you're only flagging things above **50%**. Nothing ever gets there.

**Drop the threshold to 2%.** Costs nothing, takes one minute, no retraining — you throw a few more
Ultra Balls and catch the Gyarados, and it frequently
solves the entire problem.

📌 People rebuild their whole pipeline to fix something a threshold change would have handled.

**3. ⚖️ Tell it the stakes.**

> *"A missed shiny costs you 4,000 points. A wasted ball costs you 1."*

One line of configuration. No footage touched, nothing synthesised, nothing thrown away. **This is
the right default**, and it's what you should reach for before anything below.

**4. 🔄 Change the footage — only if the above failed.**

```
   ✂️ CUT THE COMMON ONES      📋 COPY THE SHINY          🧬 INVENT NEW SHINIES
   ────────────────────        ──────────────────         ────────────────────
   🐀🐀🐀🐀🐀🐀 → 🐀🐀        ✨ → ✨✨✨✨               Take two shinies,
   ✨                ✨         🐀🐀🐀   🐀🐀🐀            imagine one halfway
                                                          between them.
   ✅ fast                     ✅ keeps everything
   ❌ throws away real         ❌ it just MEMORISES        ⚠️ the halfway point
      footage                     the one shiny              may not be shiny
                                                             at all
```

That last one earns real scepticism. It assumes *"halfway between two shinies is also a shiny"* —
and that is frequently just false. Recent work keeps finding it fails to beat simply telling the
detector the stakes.

**5. 🎯 Make it focus on the hard ones.** Once it's confidently right about a Rattata, stop grading it
on Rattata. Force the training onto the cases it's still getting wrong.

**6. 🔀 Ask a different question.** If shinies are *so* rare, stop asking "is this shiny?" and start
asking **"is anything about this Magikarp unusual?"** Learn what normal looks like and flag anything that
isn't. Different problem, often a much better fit.

**7. 🔍 Go and find more shinies.** Least glamorous, usually highest impact. Go and stand at the
Lake of Rage, where the red Gyarados actually is. One more real shiny beats a thousand invented ones.

## Two things that will burn you 🚨

**🧬 Inventing shinies before splitting your footage.**

You invent 500 fake shinies, then split into training and testing. Now **fake shinies derived from
the same original are in both piles.** Your detector "recognises" them and scores brilliantly.

Total fiction. **Always invent inside the training pile only, per round.**

**📉 Your confidence numbers are now wrong.**

Copy your shinies fifty times and your detector starts saying **"70% chance shiny"** about things
that are genuinely 2%. You didn't make it better — you moved its sense of "normal."

Fine if you only need a ranking. **Broken if anyone downstream is doing arithmetic with those
percentages.**
