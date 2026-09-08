---
id: "188"
slug: cat-tools-and-translator-workflow
style: pokemon
category: translation
difficulty: intermediate
question: "What does a professional translator's working environment look like, and why should an ML engineer care?"
tags: [cat-tools, xliff, segmentation, qa-checks, workflow, integration]
---

# Your Pokémon arrives in somebody else's battle screen

Teams build a translating machine and hand it over through a hatch. ⚠️ **Translators do not work at
a hatch.** They work at a screen laid out exactly like the one where you choose between **FIGHT**,
**BAG**, **POKéMON** and **RUN** — every option visible at once, with the consequences of each one
already displayed. Understanding that screen changes what you should be building.

## What they are actually looking at 🖥️

```
   ┌──────────────────────────┬──────────────────────────┐
   │ THE LINE TO TRANSLATE    │ THEIR ANSWER (editable)  │
   ├──────────────────────────┼──────────────────────────┤
   │ Click Save to store...   │ [ they type here ]       │
   └──────────────────────────┴──────────────────────────┘
   ┌───────────────────────────────────────────────────────┐
   │ 📔 Already caught:  98%  "Click Save to store your..." │  ← question 161
   │ 🖥️ YOUR SUGGESTION:      "Klicken Sie auf Speichern..."│  ← this is you
   │ 🏷️ The name list:   Save → Speichern (approved)        │  ← question 133
   │ 🔎 Seen before:     12 previous uses of "store"        │
   │ ⚠️ Warnings:        placeholder {count} is missing     │  ← question 156
   └───────────────────────────────────────────────────────┘
```

📌 Look where you are on that screen. **You are one option among four** — you are the **BAG**, not
the Pokémon — sitting directly beneath an already-approved match that is **free** and **guaranteed
consistent**. Your suggestion has to earn its place against that, every single line, the way a
**Poké Ball** has to earn its slot against a **Full Restore**.

## What that means for what you build 🔧

* **✏️ Produce a candidate, not a verdict.** It **will** be edited — a **Bottle Cap** here, a
  **Mint** there. So optimise for **how easy it is to fix**, not how close it is: ⚠️ one that is
  ninety per cent right and quick to repair beats one that is ninety-five per cent right and has to
  be **released and caught again**. **Your score does not measure that** (question 149).
* **📐 Take a line, but accept the page.** The screen works line by line; your machine wants the
  document (question 131). So accept the line **plus its neighbours**, and give back something that
  still lines up. ⚠️ Merge two lines into one and you have broken the screen.
* **📊 Send back more than words.** How sure you were (question 132), which names you enforced —
  **Poké Ball**, **Full Restore** — whether you leaned on something already caught. The screen shows
  all of it the way a battle screen shows HP, the **Sandstorm**, and which **Weakness Policy** just
  triggered, and the translator uses it to decide **how hard to look.**
* **🧩 And give the tags back intact** (question 156). 📌 **This one requirement causes more failed
  integrations than model quality ever has.** Not a subtle point. Just the commonest one.
* **📄 Speak the standard formats.** There are established file formats for the bilingual file, for
  the memory, and for the name list. ⚠️ Inventing your own means nobody can use your machine
  **inside the process they already have**, which means nobody uses it.

## The checks that already run 🚦

Before anything is delivered, the screen already fires: missing or altered placeholders, unbalanced
tags, numbers that differ between the two sides, a **Great Ball** where the list says **Ultra
Ball**, empty segments, identical lines translated two different ways, names over the
**ten-character** limit (question 144).

📌 Those are exactly the mechanical checks of questions 156 and 133 — **and this industry has run
them as a blocking gate for twenty years.** A pipeline that does not run them is not being
innovative. It is **missing a standard control**, in the way that entering a tournament without
letting anyone inspect your team is not boldness (question 187).

## Why any of this matters to you 🎁

Look at what is sitting inside that screen already:

* ✏️ **Every edit a translator makes** — every **Bottle Cap**, every **Mint**, every trip to the
  **Move Reminder**. Your best training signal anywhere (question 149).
* 📔 **The memory** — the **Pokédex** of everything already caught, your best retrieval corpus
  (question 161).
* 🏷️ **The name list** — **Poké Ball**, **Full Restore**, **TM26**, already validated by experts
  (questions 133, 186).

📌 **All three exist. Today. In the tool.** A team that plugs into the workflow is handed them. A
team that goes around it rebuilds all three, worse, from scratch — and then wonders why nobody is
using the machine.
