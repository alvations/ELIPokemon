---
id: "115"
slug: unicode-normalisation
style: pokemon
category: multilingual
difficulty: core
question: "Why does Unicode normalisation matter in a multilingual pipeline?"
tags: [unicode, nfc, nfkc, confusables, zwj, casefolding]
---

# Two Farfetch'd, spelled the same, that the PC insists are different

The species names alone should have warned everybody.

**Farfetch'd** has an apostrophe in it, and so does **Sirfetch'd** that it evolves into. **Mr.
Mime** has a full stop and a space; **Mime Jr.** has two. **Porygon-Z** has a hyphen. **Nidoran♀**
and **Nidoran♂** are two different species — different evolutions, different everything —
separated by a symbol nobody's keyboard can type. And the word Pokémon has an accent on the e
that half the region's machines drop entirely.

Now: that accented **é** can be stored two ways. As one mark. Or as a plain **e** with a little
stroke pencilled on top afterwards.

**They look identical on the screen.** They are not the same entry in the PC.

## What that costs you 💸

```
   Trainer A registers:  P o k é m o n        (the é as one mark)
   Trainer B registers:  P o k e ́ m o n       (an e, then a stroke)

   ► the PC box search finds one and not the other
   ► the dedupe check keeps both and swears they are different Pokémon
   ► the Name Rater in Lavender Town says the nickname is longer than it looks
   ► the Pokédex reads them as two unrelated words
```

Everything downstream inherits it. Your archive has two copies of the same battle report and
counts them as two. Your search finds neither.

**Pick one spelling and force everything through it on the way in.** That is the whole fix, and
it is lossless — the stroke goes back on the e whenever you need it.

## The tidy-up that goes too far ⚠️

There is a stronger version of the same idea: not just "settle the accent", but *"flatten
everything that looks vaguely alike."* Strip the accent. Strip the apostrophe. Strip the hyphen.
Make it all plain letters.

Do that and Farfetch'd becomes Farfetchd, Porygon-Z becomes PorygonZ, Nidoran♀ and Nidoran♂
become **the same species**, which they emphatically are not.

📌 Use the flattening as a **matching key only** — a back-room index for finding things. Never
as the record you keep, and never as what you show the Trainer. One is a filing trick. The
other is losing the Pokémon.

## Three specific traps 🪤

**🫥 Do not delete marks you cannot see.** Some scripts carry invisible joiners that change which
letter comes out — invisible on screen, load-bearing in the word. The tidy rule "strip anything
that does not render" is copied straight out of a Kanto codebase, and in three other regions it
quietly corrupts every name it touches.

**🔠 Making things lowercase is not universal.** Different regions lowercase the same letter into
different letters. A rule written for Kanto's alphabet, applied to another region's, produces a
word that was never in the language.

**🎭 Some letters are impostors.** Two marks from two different alphabets that render exactly the
same. Register a Trainer name using one and you have a **Zoroark** on the ladder: Illusion up,
presenting as somebody else entirely, and nothing on the scoreboard able to tell. It is the
Mimikyu trick in a name field — a rag that reads as Pikachu — and it is how people slip past a
ban list. Not with a clever move. With a letter borrowed from another alphabet.

## Where it bites in practice 🎯

* 🗂️ **Deduplication.** Half your archive spells it one way, half the other, and the duplicate
  check happily keeps both. Now the same battle is in your training material twice — a Ditto
  filed as a genuine second Pokémon, and your Trainer drills on it twice as hard.
* 🏪 **The counter and the Trainer must agree.** If the Celadon TM counter settles accents one
  way and the Trainer's Rotom Pokédex settles them another, the same order becomes two
  different orders depending on which machine took it down.
* 🏅 **Scoring.** A translation that is right in every respect except that the é arrived as an
  e-plus-stroke is marked **wrong** by a scorer doing exact matching. Settle both sides before
  you score, and say in the report that you did.
* 🔎 **Searching.** Query settled one way, archive settled the other, and every accented
  language quietly returns nothing.
