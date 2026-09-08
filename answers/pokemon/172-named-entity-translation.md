---
id: "172"
slug: named-entity-translation
style: pokemon
category: translation
difficulty: intermediate
question: "How should a translation system handle names?"
tags: [named-entities, transliteration, entity-linking, exonyms, consistency, back-transliteration]
---

# "Bug Catcher Rick" is two words that behave completely differently

Look at that string. It is one label on one screen, and **the two halves take opposite treatment.**

**Bug Catcher** is a Trainer Class. It gets translated — every region has its own word for it
(question 141).

**Rick** does not. Rick is his name.

📌 So *"never translate names"* is wrong, and *"translate names"* is wrong, and the useful skill is
knowing **which kind of name you are holding.**

## Four kinds, four behaviours 🏷️

| The kind | What to do | What going wrong looks like |
| --- | --- | --- |
| 🧑 **A Trainer's name** | write it in the new script, never translate it | the Trainer called "Bell" becomes the word for a bell |
| 🗺️ **A place with an established local name** | ⚠️ **use the local one** — **Pallet Town** already has a name in every region | leaving it in the original, or worse, inventing a **third** form nobody uses |
| 🏛️ **An organisation** | its official name if it has one, otherwise write it out | **Silph Co.** rendered as a description of what it makes |
| 📦 **Species, moves, items** | fixed. Look them up (questions 133, 150) | a helpful machine translating **Poké Ball** |

⚠️ And the hard part: **which bucket a name falls into is decided by custom in the target region,
not by any rule you can write down.** Some places have a local name in one language and not in
another.

## Writing a name in another alphabet only goes one way 🔁

```
   one script → another → back again      "Rick" ─► ｒｉｋｕ ─► "Riku"

   ⚠️ the trip back does NOT return what you started with.
   Several different names collapse to the same rendering going one way,
   so nothing can pull them apart coming back.
```

Three things follow:

* **🚫 Never re-render a name that is already written in the target script. Look it up.** The games
  get this exactly right: trade a Pokémon internationally and its **Original Trainer**'s name arrives
  **in the original characters** and stays that way. Nobody re-spells it. Nobody guesses.
* **📚 Going backwards needs a *record*, not an algorithm.** Given the rendered form, the right
  answer depends on **who this Trainer actually is**, and no amount of cleverness recovers that from
  the letters.
* **📐 And there are several valid systems** (question 109). Mixing two of them in one document reads
  exactly as sloppy as it is.

## The real fix: do not translate it, identify it 🔎

```
   the text ─► spot the names ─► look each one up in the Pokédex / the region's own list
                                        │
                             ┌──────────┴──────────┐
                          found                 not found
                            │                      │
                    use the recorded form.   write it out, FLAG it for a person,
                    Correct, consistent,     and ADD IT TO THE LIST so the next
                    and checkable            three hundred pages match
```

📌 This is question 133's name list, pointed at people and places instead of items — and it hands
you **consistency for nothing**. The same Gym Leader is named the same way on page one and page four
hundred, which no amount of per-sentence cleverness will ever achieve.

## What to deliberately test 🧪

* **🔁 Whether the same name survives the whole document.** The most common complaint, and the
  cheapest thing to count.
* **🔨 Names that are also ordinary words.** Build a test set out of them on purpose — a Trainer
  called **Bell**, a **Hiker** whose name is **Rock**. These are the ones a helpful machine
  translates into nouns.
* **♀♂ Names that change shape by gender** in regions where they do — and remember the information
  needed may simply not be in the text (question 142).
* **🎩 Titles that have to be added, dropped or moved** by local custom (question 141). **Mr. Mime**
  is a reminder that sometimes the title is **part of the name** and must not be touched at all.
* **✂️ And names cut in half by bad segmentation** (question 156) — one syllable translated on one
  line, the rest on the next.
