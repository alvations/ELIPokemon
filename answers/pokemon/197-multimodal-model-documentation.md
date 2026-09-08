---
id: "197"
slug: multimodal-model-documentation
style: pokemon
category: multimodal
difficulty: intermediate
question: "What should a multimodal model's documentation actually say?"
tags: [model-cards, datasheets, disclosure, intended-use, limitations, provenance]
---

# The Pokédex entry is the model card

Every species already has one. Open **Charizard** and you get **Fire/Flying**, 1.7 m, **Blaze**,
and a stat spread that says plainly where it is strong and — because Fire/Flying means Rock hits it
**four times over** — exactly where it will lose.

📌 And notice what a Pokédex entry does **not** do. It does not say *"**Magikarp** is a great
Pokémon."* It tells you **Splash** does nothing whatsoever, that its Attack is **10**, that it is
famously feeble — and then lets you decide. (It also does not mention that it becomes **Gyarados**
at level 20. That omission is a different failure, and a worse one.)

That is what documentation is for. Not marketing, and not a shield. **The document that lets
somebody else decide whether your machine is safe for *their* problem** — a decision no leaderboard
number can make for them.

## The fields a looking Pokédex needs, that a talking one does not 📋

* **🔭 How close it stands, and whether it walks up.** ⚠️ **The single most consequential
  undisclosed setting there is** (question 121). Benchmarked walking right up and shipped standing
  in the doorway are **two different machines**, and only one of them is on your chart.
* **🧾 How many tiles it holds, and what that costs** (question 165) — because that decides whether
  anybody can afford it at the volume they have.
* **🎥 What "it handles battles" actually means.** Eight stills out of a whole match (question 126)?
  **Say so.**
* **🔤 Which alphabets the *eye* can read.** Reading small print varies enormously by script and is
  **almost never written down** (questions 106, 123).
* **🚪 Whether the eye was ever taught manners at all** (question 139) — and **in which languages**
  (question 193).
* **📦 Where the training material came from.** What the eye read. Whether the captions were written
  by another machine (question 146). And **what your filter threw away** (question 190) — because if
  it quietly removed every chart, the next person needs to know that before they hand it a chart.

## The sections that carry the weight ⚖️

**🚫 What it is *not* for.** More useful than what it *is* for, and always the vaguer of the two.
*"Not validated for medical images, for identifying people, or for documents in non-Latin scripts"*
tells a reader something real. *"Should not be used for harm"* tells them nothing at all.

**🙈 Your scores, next to the blindfolded score.** Question 147's test. ⚠️ Without it, **nobody can
tell how much of your number was looking.**

**💥 The specific ways it fails.** Counting past four. Left from right. Print below a stated size.
The word *"not"*. Several pictures at once. 📌 Every one of these is a **documented general
weakness** (questions 122, 128, 137) — so a card that mentions none of them was either never tested
or is **choosing not to say.**

**📊 Broken down.** By language, by script, by kind of picture, and by group where people appear
(question 184). ⚠️ **An average is not a disclosure.** *"Good against Pokémon"* is not a type
chart.

**🏷️ And a version, with a date.** Downstream, somebody in a regulated setting (question 187)
**cannot pin what you never versioned.**

## The test for whether it is any good 🎯

📌 **Does it tell a reader something that would make them decide not to use it?**

A card containing no such sentence **was not written for the reader.**

And that includes the uncomfortable ones: *"we never evaluated this in the languages most of your
users speak"*, *"the eye's manners cover Kanto only"*, *"our filter removed nearly every document
from the training pile"*.

⚠️ **Those sentences cost something to write. They are the entire value of the document.**

📌 The entry that admits **Magikarp** is virtually useless is worth more than a hundred entries
calling every Pokémon remarkable — because the first one is **information**, and a **Trainer Card**
full of praise is not.
