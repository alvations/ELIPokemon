---
id: "190"
slug: image-quality-and-aesthetics
style: pokemon
category: multimodal
difficulty: intermediate
question: "How do you score image quality and aesthetics, and what goes wrong?"
tags: [aesthetics, iqa, reward-models, filtering, bias, subjectivity]
---

# Professor Oak scores your photographs, and he has opinions

Hand **Professor Oak** a **Pokémon Snap** photograph and he marks it. Size. Pose. Technique.
Whether anything else wandered into the frame.

📌 And notice that his marking sheet contains **two completely different questions** wearing one
name:

* **📷 Was the photograph taken properly?** In focus, well lit, the **Pikachu** not a blur. Fairly
  objective — Trainers broadly agree.
* **✨ Is it a *good picture*?** Entirely a matter of taste, and this is where all the interesting
  failures live.

Both matter, because a scorer like this is used to **decide what goes into the training pile**
(question 137), to **pick between generated pictures**, and to **order search results**. ⚠️ So the
scorer's taste becomes the generator's taste, at enormous scale.

## What these scorers actually learn 🎨

```
   HIGH MARKS                          LOW MARKS
   ──────────                          ─────────
   the Pidgeot mid-flight, blurred     flat, even light
   background, golden light            a cluttered route
   rich colour, strong contrast        anything that looks like a record
   the Pokémon centred and posed       a candid, ordinary snapshot
   obviously worked on afterwards      a photograph somebody just took
```

⚠️ **That is not beauty.** It is **one specific style of photography**, learned from whoever happened
to rate the training pictures.

📌 And filtering your archive with it is **quietly deciding what every picture you ever generate
will look like**. It is a large part of why generated images share that recognisable house
style — everything looks like a **Charizard** at golden hour and nothing looks like a **Trainer
Card**.

## Where it goes wrong 🚨

* **🐦 The score is tangled up with the *subject*.** These scorers mark certain things higher
  **regardless of how well they were taken**: a **Ho-Oh** over a **Rattata**, a landscape over a
  **Celadon Department Store** price board. ⚠️ So filtering does not remove *bad photographs*. It
  removes **whole subjects** — and the first things to go are the charts, the documents, and the
  ordinary.
* **🌏 It is one region's taste.** The people who did the rating were a narrow group. What counts as
  well-composed, what counts as too busy, which colours look right — all of it varies, and a scorer
  trained on one region **imposes that region on everybody** (question 162's problem, in pictures).
* **🎣 And it is gameable.** Used as a reward, the generator learns to produce **the markers** of the
  style — the blur, the warmth, the saturation — rather than better pictures. 📌 This is question
  021's over-optimisation, and here **you can see it with your own eyes**: the over-cooked look of a
  generator that has been tuned too hard on taste.
* **🎯 And "beautiful" is not "what I asked for."** A gorgeous **Blastoise** when you asked for a
  Charizard scores splendidly (question 137). **Score those two things separately. Always.**

## Doing it responsibly 🧭

* **✅ Filter on whether it was taken properly. Be very careful filtering on taste.** Throwing out
  the blurred, the tiny, the corrupted and the duplicated is safe and valuable. Throwing out the
  *"unaesthetic"* throws out documentary photographs, diagrams, and entire categories of subject.
* **👀 Report what your filter removed, and go and look at a sample of it.** 📌 Teams routinely
  discover their filter has been quietly deleting every chart, or every photograph from one region,
  for months.
* **🔀 Keep the two marks apart** — how good it looks and whether it is what was asked for — and
  never add them into one number for ranking.
* **🎚️ And if it is a reward, cap how much it can pull.** Then watch for the drift, exactly as
  question 167 watches for a Pokédex that has learned to say nothing rather than be wrong. Here the
  equivalent is a generator that has learned to make everything golden.
