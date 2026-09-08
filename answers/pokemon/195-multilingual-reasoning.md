---
id: "195"
slug: multilingual-reasoning
style: pokemon
category: translation
difficulty: advanced
question: "Do models reason as well in other languages as they do in English?"
tags: [multilingual-reasoning, pivot-language, chain-of-thought, cross-lingual-gap, culture]
---

# The Trainer thinks in Kanto and battles in Paldea

**No.** And the *shape* of the gap is far more interesting than the fact of it.

## Where the loss actually happens 🧠

Ask the same multi-step question in Kanto's language and in a small region's, and the answers differ
— often substantially, and the gap tracks how much of that region the Pokédex ever read.

But it is **not** that it reasons badly in the second language:

```
   understanding what was asked   ─► transfers well. It knew what you meant.

   the reasoning itself           ─► happens somewhere in the middle, in a
                                     representation that leans heavily toward
                                     the region it read the most of

   saying the answer IN the       ─► transfers less well — and degrades further
   region's language                 while it is also busy reasoning
```

📌 That is why **"work it out in Kanto's language, then answer in theirs"** frequently beats
reasoning natively.

⚠️ And notice what that trick actually is: **a diagnosis, not a cure.** It works because the
Pokédex was already doing it internally. You have simply stopped pretending otherwise.

## The techniques, and what each costs 🔧

* **🔁 Translate the question, reason, translate back.** Cheap and dependable. ⚠️ Loses whatever the
  original encoded that Kanto's language cannot hold — question 130's **trade through a third
  Trainer**, and the same things go missing at the halfway point.
* **🧠 Reason in Kanto's, answer in theirs.** Better, because the final answer is at least looking at
  the original. ⚠️ Standard practice — and the answer may be **more fluent than it is faithful.**
* **🌏 Or reason natively**, which is what you actually want and currently costs accuracy for most
  regions. 📌 The gap shrinks as the reading pile grows, so **this is a data problem far more than
  an architecture problem.**
* **🔀 Or ask in several languages and take the majority.** Expensive — and genuinely useful for a
  reason people miss: **when the languages disagree, that is a warning the answer is unreliable**,
  and it is one of the few cheap reliability signals available here.

## And some of the gap is not about reasoning at all 🌍

⚠️ This is the part that gets misdiagnosed constantly.

Some questions have **a different correct answer in different places** (question 150). What the
measurements are. How the grading works. Which Pokémon even **exist** here — **Ekans** in one
version and **Sandshrew** in the other.

📌 So a test written in Kanto and translated outward **carries Kanto's assumptions with it**, and
then marks **the locally correct answer wrong.**

That is why translated tests **overstate** the gap on some tasks and **understate** it on others,
and why tests written locally matter (question 196).

## What to do 🛠️

* **📊 Measure per region on the same underlying items, and separately on locally written ones.**
  📌 **The difference between those two numbers tells you how much of your gap is reasoning and how
  much is simply Kanto.**
* **🗺️ Say which language it thinks in.** If your system routes its reasoning through one region,
  that is **a design decision with consequences** — write it down rather than letting it be something
  that merely happens.
* **🔍 Watch what language comes out.** A Pokédex reasoning in Kanto's language and letting it leak
  into the answer is question 136's wrong-region failure, arriving through a new door.
* **⚖️ And do not assume the gap is one size.** It is **largest for multi-step reasoning and smallest
  for looking things up** — so a single *"multilingual gap"* figure is not something anybody can act
  on.
