---
id: "177"
slug: multilingual-rag
style: pokemon
category: translation
difficulty: advanced
question: "How do you build retrieval-augmented generation across languages?"
tags: [multilingual-rag, cross-lingual-retrieval, query-translation, citation, language-control]
---

# The Trainer asks in one region and the answer is filed in another

Ordinary searching (question 044) assumes one language throughout. Real archives do not work that
way. The **Kanto** Pokédex entry is in one language, the **Johto** one in another, the **Alola**
notes in a third — and a Trainer from **Paldea** is standing in front of you asking a question.

Every stage now needs a decision about *which language*, and getting **one** of them wrong produces
a confident answer read out of the wrong book.

## Four ways to build it 🗂️

```
   1. 🔤 TRANSLATE THE QUESTION    ask ─► translate ─► search that region's shelf
      ✅ reuse everything you have  ❌ a mistranslation becomes a search error —
                                      and how did you know WHICH region to translate into?

   2. 📚 TRANSLATE THE WHOLE ARCHIVE into one language, then search normally
      ✅ one shelf, simple           ❌ ruinously expensive, out of date immediately,
                                      and every error is now baked in permanently

   3. 🎴 ONE SHARED FILING SYSTEM  questions and entries in the same space (question 168)
      ✅ no translating at all       ❌ works beautifully for some regions and badly
                                      for others, and you will not notice which

   4. 🌐 ASK EVERYWHERE AT ONCE     translate the question into every region's language,
                                    search each shelf, merge what comes back
      ✅ finds the most              ❌ several times the cost — and ⚠️ merging the
                                      scores is the hard part, see below
```

📌 In practice: **3, with 4 as a fallback.** Search the shared system, and fan out to every shelf
when it comes back unsure or when the region is one it handles poorly.

## The problems that only exist here 🚨

* **⚖️ You cannot compare the scores.** A match found on the Kanto shelf and a match found on the
  Paldea shelf are **not measured on the same scale** — the same calibration problem as question
  168. ⚠️ Merge the raw numbers and you systematically favour **whichever region the filing system
  handles best**, which is nearly always the biggest one. Normalise each shelf before merging.
* **🗣️ It answers in the wrong language.** The Trainer asked in one, the evidence is in another, and
  the Pokédex may reply in either — or in a third, or **switch halfway** (question 136). Say which
  language you want, and **check what came out** before handing it over.
* **📎 And the citation is unreadable.** If a Paldean Trainer's answer cites a page written in
  Johto's language, **they cannot check it.** 📌 Show the original **and** a translation of the
  cited passage, **marked as translated by a machine**. A citation nobody can read is decoration.
* **🏷️ The words must match the region's own** (question 133). The answer should use the name that
  region already uses for the item, not a fresh rendering invented from the source page.
* **📖 And sometimes the two books genuinely disagree.** ⚠️ **Ekans** lives in **Red** and not in
  **Blue** (question 150). The Kanto shelf and the Blackthorn shelf may both be right about their
  own region. **This is not a bug to be resolved into one answer** — it is information, and the
  right thing is to hand back both, **each labelled with where it came from.**

## Judging it 🏅

* 📊 **Report how well it finds things per region, never pooled.** ⚠️ The overall figure is decided
  by whichever region asks the most questions.
* 🗣️ **Count how often it answered in the language it was asked in.** This should be essentially
  always, and it very often is not.
* 🔍 **Check the answer against a source in another language** — which needs somebody who reads
  both. And an automatic judge is weakest for exactly the regions where you most need one
  (question 132).
* 🪞 **And run the control that settles it: ask the identical question in the big region's language
  and in the small one, and compare.** 📌 A large gap tells you the whole pipeline quietly runs
  through Kanto — which is **the default outcome** unless somebody has deliberately stopped it.
