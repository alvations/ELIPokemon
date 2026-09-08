---
id: "170"
slug: translationese
style: pokemon
category: translation
difficulty: advanced
question: "What is translationese, and why does it distort MT evaluation?"
tags: [translationese, test-set-direction, source-original, simplification, interference, wmt]
---

# You can tell a bred Pokémon from a wild-caught one

A **Day Care** Pokémon and a wild-caught one are both entirely legitimate Pokémon. And a Trainer who
knows what to look for can tell them apart every time.

The bred one hatched at **level 1**. It knows **Egg Moves** its wild cousins never learn — a
**Charmander** with **Dragon Dance**, which no wild Charmander has ever had. Its met location says
the Day Care rather than **Route 3**. Its **EVs** are untouched and its **IVs** are suspiciously
tidy, because somebody picked the parents and held a **Destiny Knot**.

📌 Translated text is the same. **Not worse than text written from scratch — different**, in ways
that are consistent, measurable, and that a classifier can spot with embarrassing accuracy.

## The four tells 🔍

* **✂️ It is simpler.** Smaller vocabulary, shorter sentences, fewer unusual words than something
  written fresh. The **Level 1** giveaway: it started from a standard place.
* **📢 It spells out what the original left implied.** Connections made explicit, relationships
  stated. Helpful, and not what the original did.
* **🧹 It is tidied.** Idioms regularised, odd phrasings smoothed toward the conventional. Nothing
  strange survives — like a bred **Adamant** Pokémon with the nature somebody chose, rather than the
  **Bashful** one the **Tall Grass** actually handed you.
* **👻 And the source language shows through.** Word order, punctuation habits, words that look like
  the original's words. The **Egg Move** that gives away who the parents were.

## Why this quietly wrecks your test set 🎯

Every test segment has an **origin direction**, and half of a standard test set runs the other way:

```
   THE HALF WRITTEN IN THE SOURCE      THE HALF WRITTEN IN THE TARGET
   ──────────────────────────────      ──────────────────────────────
   source:  natural, wild-caught       source:  ⚠️ ALREADY BRED — it was
                                                translated to get here
   answer:  a translation              answer:  natural, wild-caught

   the second half asks your machine to translate ALREADY-TRANSLATED text
   into natural text. That is an easier job, an unrepresentative one, and it
   FLATTERS whichever machine produces the most bred-sounding output.
```

⚠️ And this is not a rounding error. Scores on that second half run substantially higher, and the
**ranking between two machines can flip** depending on which half you look at. That is why the
serious evaluations now use **only** the wild-caught half.

📌 **The rule:** if you scraped your test set out of parallel data, you **do not know which half you
have**, and your numbers cannot be interpreted. Build it from text originally written in the source
language, translated once, on purpose, by a professional.

## And it gets into the training too 🥚

Almost all parallel material *is* translation, so machines are raised overwhelmingly on bred
Pokémon. Three consequences:

* 📉 The output inherits the flattening. Fluent, faintly foreign, recognisably a translation.
* 🫧 **Breeding with Ditto helps in one direction and hurts in the other** (question 130). Bred
  material on the **input** side is fine — that is the whole trick. ⚠️ Let it onto the **output**
  side and you are breeding from bred Pokémon, and the tells compound.
* 🏷️ And repaired output flowing back into the archive (questions 149, 161) stacks on top. **The
  Original Trainer mark and the Day Care mark are two different tells, and you can collect both.**

🛡️ What helps: mix in a great deal of plain writing in the target language; prefer wild-caught
material where you can identify it; and **judge the output against text a person actually wrote**,
not only against a reference that was itself bred.

## One honest caveat ⚖️

Translationese is **not a defect to be stamped out.** A translation exists *for* somebody, and some
of that spelling-out genuinely helps the reader.

📌 The problem is not that it exists. The problem is that it is **invisible on the scoreboard** — it
makes machines look better than they are, and it **accumulates silently** through a pipeline that
keeps feeding its own offspring back into the Day Care.
