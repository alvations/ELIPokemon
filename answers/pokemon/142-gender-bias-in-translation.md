---
id: "142"
slug: gender-bias-in-translation
style: pokemon
category: translation
difficulty: intermediate
question: "Why do translation systems get gender wrong, and what can you do about it?"
tags: [gender-bias, winomt, stereotypes, ambiguity, multiple-translations, fairness]
---

# Your Combee will never become a Vespiquen, says the Pokédex, wrongly

**Combee** are mostly male — seven out of eight of them. And a male Combee does not evolve. Only a
**female** Combee ever becomes a **Vespiquen**.

So a Pokédex that has read a great deal about Combee, and is asked about *your* Combee, will tell
you it is not going to evolve. It is right seven times out of eight. And when it is wrong, a
Trainer stops raising a Pokémon that was one level away from becoming a Vespiquen.

That is the whole shape of this problem. **The archive's average, delivered as a fact about the
individual in front of you.**

## The same structure as question 141, with a sharper edge ⚖️

Politeness and this are the same mechanism: the page you are translating **does not say**, and the
language you are translating into **must**. So something fills the gap, and what fills it is
whatever was most common in the archive.

The difference is what the guess is made of. A wrong politeness level is awkward. A guess made out
of *"what usually goes with this role"* is a stereotype, and outside Pokémon it lands on actual
people, in a message they are reading about themselves.

## Three cases that get muddled together 🔍

```
   1. NOBODY EVER SAID.
      The page says "the Combee". No symbol, no pronoun, nothing.
      Any single answer is a guess. There is no correct one.

   2. IT SAID, TWO PAGES AGO.
      "Caught a Combee♀ today." ... "It should evolve soon."
      Entirely knowable — and invisible to anything reading one line at a time (question 131).

   3. IT SAID, RIGHT THERE, AND THE POKÉDEX OVERRULED IT.       ← the damning one
      The page says ♀. The Pokédex says it will not evolve,
      because most Combee are male and the habit was stronger than the evidence.
```

**Salandit** is the same trap, and **Meowstic** is worse: the male and the female genuinely differ
in what they can do, so blurring them is not a stylistic slip — the entry is simply **wrong about
the Pokémon**.

And then there is the case nobody remembers: sometimes the language marks **who is speaking**, not
who is being described. That was never on the page at all, and often not anywhere in the document.

## How to measure it honestly 📏

Build pairs where the answer is *pinned down* by the sentence — but half the time the habit agrees
and half the time it does not. Then report **three** numbers:

* ✅ how often it is right overall;
* ⚠️ **the gap between the cases where the habit agreed and the cases where it did not** — this is
  the bias, and it is the number that matters;
* 📊 which way it leans when the page genuinely does not say.

📌 A Pokédex can score magnificently overall and be **right only when the stereotype was right**.
The overall number hides that completely — and so, as ever, does the general quality score
(question 129). Fix every one of these and the season average moves by nothing.

## What to actually do 🔧

* **📖 Give it the earlier pages.** Case 2 disappears outright, and it is the cheapest large win
  available (question 131).
* **🙋 Let the Trainer tell it.** If your system already knows — and it very often does — **pass it
  in**. Same argument as question 141: do not squint at a sentence to work out something you were
  already holding.
* **🔀 When it genuinely is not knowable, give both and label them.** *"If ♀, it becomes Vespiquen.
  If ♂, it does not."* Honest about the ambiguity, and it hands the decision to the one person in
  the exchange who actually knows the answer.
* **✍️ Or translate once and re-render on request** — one entry, re-inflected on demand, which also
  scales past two options in languages that have more.
* **⚖️ And balance the archive.** Swap the symbols in half your training pairs. This weakens the
  habit. ⚠️ It does not fix case 1, because **nothing can fix case 1.**

## The part to be clear-eyed about 🎯

Case 1 has **no right answer.** A Pokédex that always guesses male is not more accurate than one
that flips a coin — it is more *consistently* biased, which is worse, because it looks reliable.

So the engineering question is not *"how do we guess better."* It is **"how do we stop guessing"** —
get the context, ask, or show both. A system that quietly guesses and presents the guess as **the**
translation has made an editorial decision on somebody's behalf, and they have no way of knowing
it happened.
