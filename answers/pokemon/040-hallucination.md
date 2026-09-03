---
id: "040"
slug: hallucination
style: pokemon
category: reliability
difficulty: core
question: "Why do LLMs hallucinate and how do you reduce it?"
tags: [hallucination, calibration, rag, grounding, abstention]
---

# Hallucination: your Trainer invents a Pokémon

> **You:** "What's Flareon's Hidden Ability?"
> **Trainer:** "Flash Fire — no wait, Guts. It boosts Attack when statused."

Delivered with total confidence. Completely wrong.

The key thing to understand: **this is not a malfunction.** Your Trainer is working exactly as
designed. The design is the problem.

## Why it happens 🔍

**1. 🎯 They were trained to sound right, not to BE right.**

The entire wild-grass drill was *"what comes next?"* Never *"is that true?"* Nobody ever graded
truth. Not once, in months of training.

A confident wrong answer and a confident right answer are **equally good continuations**. The
training could not tell them apart, so neither can the Trainer.

**2. 🤷 Nobody in the footage ever said "I don't know."**

Think about the tapes they learned from. Strategy guides, commentary, forum posts — all of it
*assertive*. People don't publish "I'm not sure about Flareon."

So your Trainer learned the **shape of a confident answer** and applies it universally, including
to the many things it doesn't actually know.

**3. 😬 Coaching made it worse.**

When human judges compared answers, they preferred the confident complete one over "I'm not
certain." Every time. So coaching actively **rewarded guessing over admitting ignorance.**

And if you tried to teach it new Pokémon during obedience school? You taught it that *unfamiliar
questions get confident answers.* You installed the bluff.

**4. 🗜️ Their memory is compressed.**

Your Trainer can't store every Pokémon perfectly. Common ones are crisp. Ones they saw *once* are
stored as a rough impression, and reconstructing from a rough impression produces something
plausible and wrong — right shape, wrong details.

**5. 🎭 One lie becomes a world.**

They invent an ability on turn 3, and then play **ten perfectly logical turns** based on it. Each
turn is correct given the premise. The premise was fiction.

## Five different problems wearing one name 🏷️

```
  ❌ Got the world wrong        "Flareon is Water-type"      → give it a Pokédex
  📄 Contradicted the handout   handout says X, it said Y    → make it cite
  🕳️ Never knew                 asked about a new species    → let it say so
  🧮 Knew, reasoned badly       right facts, wrong maths     → make it show work
  📅 Knew, but it changed       old move list                → refresh the Pokédex
```

**Diagnose before you fix.** Teams constantly hand out a fresh Pokédex to solve what is actually a
*maths* problem, then wonder why nothing improved.

## What actually helps ✅

**1. 📖 Hand it the Pokédex.** By far the biggest win. Don't ask it to *recall* Flareon's ability —
give it the page and ask it to *read*. Recall is where it's weak; reading is where it's strong.

**2. 📌 Make it point at the page.** *"Which line says that?"* Then **check the line actually says
it.** This catches the leftover cases where it has the right page and still garbles it.

**3. 🤷 Make "I don't know" an acceptable answer.**

And this means *actually rewarding it*, not just permitting it. If your judges keep preferring
confident answers, you will train the honesty right back out. Fewer answers, more trustworthy —
that's a real trade, and for most jobs it's the right one.

**4. 🧮 Give it a calculator.** Damage calcs, dates, type charts — anything with a mechanical
answer. Don't ask a Trainer to be a calculator.

**5. 🔁 Ask three times.** Get the same answer thrice? Probably knows it. Get three *different*
answers? **That's your alarm.** Real knowledge is stable; invention isn't.

**6. 🌡️ Turn down the boldness** for factual questions.

## What doesn't work ❌

**🗣️ "Don't make things up."** They don't know they are. If they knew, they wouldn't.

**📚 Teaching it more facts.** Makes it worse. See cause 3.

**❓ "Are you sure?"** They'll change their answer. Not because they rechecked — because you sounded
doubtful. That's a Pokémon reading your tone, not verifying a fact. You've learned nothing, and now
you've possibly talked them out of a correct answer.

## Measure both numbers 📊

Track **how often it's wrong** *and* **how often it declines to answer**. Chase only the first and
you get a Trainer who refuses everything. Chase only the second and you get a confident liar. The
job is both at once.
