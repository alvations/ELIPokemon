---
id: "196"
slug: cross-lingual-evaluation-design
style: pokemon
category: translation
difficulty: advanced
question: "How do you design an evaluation that is fair across languages?"
tags: [benchmark-design, translated-benchmarks, cultural-validity, native-authoring, reporting]
---

# A test written in Kanto, shipped to every region

The usual approach — take the Kanto exam, translate it, publish a score per region — is cheap,
everywhere, and produces numbers that mean much less than they look like they mean.

Three problems, and they compound.

## 1. The questions carry Kanto with them 🗺️

```
   the Kanto question:  "Which Gym Leader would you challenge with a Water type?"

   translated and shipped to Paldea:
        ⚠️ the reasoning survives. The SITUATION does not.
        Paldea does not have Brock. The question now tests whether the
        Pokédex has memorised Kanto's Gym roster.
```

📌 And it goes deeper than trivia. Ask which Pokémon live on **Route 3** and the answer differs
between **Red** and **Blue** (question 150). Ask about a **Vulpix** and the correct type depends on
whether you mean the Kantonian or the **Alolan** one (question 162).

⚠️ You are no longer measuring the ability. **You are measuring familiarity with Kanto** — which
tracks how much Kanto material was in the training, in exactly the way that makes the result look
like a capability gap.

## 2. The questions are bred, not caught 🥚

A translated test set is, by construction, question 170's problem: simpler, more explicit, more
regular than anything anybody in that region actually wrote.

⚠️ And Pokédexes handle bred text **better** than wild text. So translated tests tend to **flatter**
in absolute terms while quietly distorting the comparison you were trying to make.

## 3. And difficulty does not survive the journey 📏

A question that is genuinely hard in one language may be **trivial** in a region whose grammar marks
the distinction outright — or **impossible** in one that has no way to express it at all.

📌 Difficulty is a property of **the question *and* the language together**, never of the question
alone.

## What a fair design looks like ✅

* **✍️ Questions written locally**, by speakers, about things that matter there, with the correct
  answers decided there. Expensive — and **the only thing that actually measures the ability in that
  region.**
* **📊 Both, reported separately.** Translated questions let you compare across regions. Local
  questions tell you the truth about one. 📌 **And the gap between the two numbers is itself the
  finding** — it separates *"worse at the task"* from *"has never been to Alola"* (question 195).
* **👥 Native speakers checking every question**, including the translated ones, **with the authority
  to throw one out** when it does not survive the trip.
* **🔢 Per region, never pooled** (question 185) — **with the sample sizes shown.** ⚠️ Small
  per-region samples produce error bars wide enough to swallow most of the differences people report
  from them, and those error bars are almost never printed.
* **🏷️ And write down where every question came from**: originally written in which language,
  translated by whom, checked by whom. Without that, **a reader cannot tell what your number means.**

## The uncomfortable arithmetic 💰

⚠️ Writing questions locally costs real money **per region**. Which is why almost nobody does it.
Which is why the field's entire picture of multilingual ability rests largely on **translated Kanto
exams.**

📌 That is worth saying out loud when you report results — **including your own.**

And where a region has no adequate test at all, the honest report is **"we cannot currently measure
this"** — not a number lifted from a translated set and printed without qualification.

Question 185's *seen versus caught* applies to **your evaluation** just as much as it applies to
your model.
