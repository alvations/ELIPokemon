---
id: "178"
slug: translating-user-generated-content
style: pokemon
category: translation
difficulty: intermediate
question: "What breaks when you translate chat messages and user-generated content?"
tags: [ugc, chat, noisy-text, emoji, code-switching, latency, moderation]
---

# Trainers do not type in full sentences

Everything so far assumed properly written text. Now open the **Global Trade Station** and read
what Trainers actually send each other while swapping a **Magikarp** for a **Larvitar**:

> `gg`  ·  `wait no`  ·  `pls trade the Larvitar back 🙏`  ·  `same lol`  ·  `sooooo close`

📌 The games themselves already conceded this. The **Union Room** hands you **preset phrases** to
tap rather than a keyboard — because somebody worked out that free-typed Trainer chat is a mess.

## What is actually in the box 📥

* **⌨️ Typos, no capitals, no full stops.** The chopper shatters unfamiliar spellings into fragments
  (question 102), and one slip can change the whole sentence.
* **🔤 Shorthand that changes faster than any archive.** Every region has its own, and it is different
  this year.
* **😊 Emoji, which carry the meaning and sometimes reverse it.** ⚠️ And they mean different things
  in different regions (question 150) — the same one is warm in one place and cutting in another.
* **🔀 Switching languages mid-sentence** (question 107), which breaks anything that decided which
  language this was before it started.
* **🗣️ Non-standard forms** (question 162) — the **Alolan Vulpix** of writing, and in chat they are
  not the exception, **they are the default**.
* **🤏 And messages of one word.** `same`. `ok`. `no`. `Ditto`. ⚠️ There is almost nothing to be
  faithful to (question 136), and **the thread is the only signal there is.** *"Ditto"* is either a
  Pokémon or the word *"likewise"*, and only the previous message can say which.
* **🎭 Plus deliberate disguise**: spaced-out letters, borrowed alphabets, numbers standing in for
  letters — the **Voltorb** trick from question 139, aimed at whatever is filtering nicknames. The
  games have run such a filter since **Red** and **Blue**, and people have been probing it since
  **Red** and **Blue**.

## What follows 🔧

**📖 The thread is not optional — it is the whole thing.** `same` is a **reply**. Alone it means
nothing at all. So translate the conversation, not the message (question 131). 📌 And note: this is
where document context has its **largest** effect anywhere in this dataset, precisely because each
piece is so tiny.

**🧼 Do not tidy it up too much.** Normalising into proper prose before translating destroys the
register and sometimes the meaning (question 162). `sooooo` is **emphasis**. All-lowercase is a
**tone**. Fix what actually breaks the machine; keep what the Trainer chose.

**⏱️ And it has to be fast.** People are trading right now. Question 143's curve again — with the
extra difficulty that during an argument the messages arrive faster than they can be translated.

**🏷️ Never translate a name or a handle.** `@charizard_fan` is an identifier, and so is a Pokémon's
**nickname** — a **Gyarados** called `Sparky`, typed at the **Name Rater** in **Lavender Town** and
meant (questions 133, 172). This seems too obvious to state and it ships broken constantly.

## Where it stops being cosmetic 🚨

Translated messages get **checked** for whether they break the rules, and the **order** matters
enormously:

```
   CHECK AFTER TRANSLATING  ─► the filter reads clean, fluent, standard text
                               and misses the insult whose force was in the original

   CHECK BEFORE TRANSLATING ─► needs a filter for every region, and the small
                               regions are worst served (question 162)
```

⚠️ Both orders fail, differently. And there is a specific danger with a name: **translating launders
the disguise.** A deliberately misspelled insult gets helpfully *corrected* into something clean
that sails through the filter — or, going the other way, a perfectly innocent phrase comes out
reading like a violation.

📌 So: **keep the original alongside the translation for every decision, and never ban anybody on
the strength of the translation alone.**

## Judging it 🏅

Build your test set from **real messages with their threads**, not from tidied-up sentences.

And report the hard cases **separately**: one-word messages, mid-sentence switches, emoji-carrying
messages, non-standard spellings. ⚠️ A single number over a mixed pile is decided by the easy
majority and tells you **nothing** about the cases you built the thing for.
