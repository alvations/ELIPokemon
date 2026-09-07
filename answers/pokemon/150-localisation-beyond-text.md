---
id: "150"
slug: localisation-beyond-text
style: pokemon
category: translation
difficulty: intermediate
question: "What does localisation involve beyond translating the words?"
tags: [localisation, i18n, formats, rtl, collation, transcreation, pluralisation]
---

# Pokémon names are not translated. They are re-invented.

Here is the thing that gives the whole game away.

**Pokémon names are puns**, and a pun does not survive translation. So when the games cross a
border, the names are not converted — they are **built again from scratch**, in the new language,
to land the same way. Different sounds, different joke, same Pokémon.

📌 That is localisation, and **it is not translating.** Translating turns words into other words.
Localising asks *what would this have been, if it had been made here* — and quite often the answer
shares no words with the original at all.

## The things that are not words 📐

| What | Where it goes wrong |
| --- | --- |
| 📏 **Measurements** | **Wailord** is 14.5 m in one region and 47′07″ in another. **Onix** is 8.8 m or 28′10″. Same Pokémon, two different Pokédex screens |
| 🔢 **Numbers** | which mark separates the decimals, and where the digits get grouped — and in some places, different digits entirely |
| 💰 **Money** | which side the symbol sits, how many decimal places. ⚠️ And you **cannot just convert the amount** — what a **Poké Ball** costs at the **Poké Mart**, and what a **Full Restore** costs, are decisions somebody made, not arithmetic |
| 📅 **Dates** | four digits and two slashes mean two different days to two different Trainers |
| 🧑 **Names** | which part comes first. A form with a box for "first name" and a box for "last name" is **already broken** in much of the world |
| 🗓️ **Which day the week starts on**, and which days are the weekend |

## "Pokémon" is both singular and plural — and that is a coincidence 🔢

One Pokémon. Six Pokémon. English happens to let you get away with that.

⚠️ Almost nowhere else does. Some languages have one form. Some have **six**. So a message built as
*"if there is exactly one, say this, otherwise say that"* is not awkward to translate — **it cannot
be translated at all.** It has to be thrown away and rebuilt so the *language* decides how many
forms exist.

Same for *"{Trainer} sent out {Pokémon}!"* — in many languages the verb changes depending on who
the Trainer is, and the information needed to choose may not exist anywhere in your system
(question 142).

## Layout, script, and sorting 🪞

* **🔄 Some regions read the other way, and that mirrors the whole screen** — not just the text.
  The menu, the arrows, the HP bar filling from the other side, the **RUN** option that was on the
  right.
* **📦 Everything gets longer** (question 144). Lay the boxes out around the **longest** region's
  words, not the shortest.
* **✂️ Where lines may break differs.** Some regions do not put spaces between words at all
  (question 114), and breaking in the wrong place is wrong in specific, defined ways.
* **🔠 The letters may not exist at all.** Hand a machine the **Unown** alphabet with no font for
  it and every name renders as empty boxes.
* **🔤 And alphabetical order is not one thing.** Sorting the **PC** boxes by name gives a different
  order in different regions — accented letters go after Z in one place and beside their plain
  cousins in another. Sort **Pokédex** order instead and **Bulbasaur** comes first everywhere;
  sort by name and it does not. **Never sort by character codes and call the result alphabetical.**

## What has to be remade, not converted 🎨

* **🖼️ Writing baked into a picture.** The sign outside the Gym, the label on the Poké Mart. Your
  translator never sees it, and it ships in the original language.
* **🎭 Colours and symbols mean different things.** The **♀** and **♂** telling **Nidoran♀** from
  **Nidoran♂** are read instantly by some audiences and not at all by others — and they are not
  decoration, they are the difference between a **Nidoqueen** and a **Nidoking**. Colours carry luck
  in one place and warning in another.
* **✍️ Slogans and flavour text** — remade, exactly like the names (question 149).
* **📜 And content that is simply different.** **Ekans** and **Arbok** live in **Red** and not in
  **Blue**; **Sandshrew** and **Sandslash** the other way about. **Scyther** in one, **Pinsir** in
  the other. That is not a translation problem at all. **The thing itself differs**, and no amount
  of careful wording bridges it — you cannot translate a **Growlithe** into a **Vulpix**.

## How to not discover all this at the end 🧪

* **📋 Pull every piece of text out into one list — with context.** What it is, where it appears,
  how much room it has. A list with screenshots and character limits produces translations several
  grades better than a bare column of strings (questions 133, 144).
* **🧵 Fake it early.** Before a single real translation exists, fill every box with a stretched,
  accented version of itself. In an afternoon you will find every hardcoded string, every box that
  **Crabominable** does not fit into, and every layout that collapses.
* **🗺️ And "the language" is not the target — the *region* is.** Two regions can share a language
  and disagree about vocabulary, formality, and sometimes the writing system. **Ask which one**
  before anybody translates anything.
