---
id: "179"
slug: controlled-language-authoring
style: pokemon
category: translation
difficulty: intermediate
question: "How does changing how the source is written improve translation?"
tags: [controlled-language, source-authoring, ambiguity, simplified-technical-english, upstream]
---

# Fix the Pokédex entry, not the translator

Every other page in this dataset improves **the translating**. This one improves **the thing being
translated** — and it is consistently the biggest lever available, and the one almost nobody has
the authority to pull.

## Most errors were already in the original ✍️

An ambiguity that a Kanto Trainer resolves without noticing has to be **decided** by the translator.
And if they decide wrong, the mistake is downstream of a choice the author never realised they were
making.

```
   "Check the Poké Ball holding the Gyarados that is damaged."
                                              ▲
      which is damaged — the Gyarados, or the Poké Ball? One region lets you
      leave that hanging. Most regions force a choice, through agreement or
      word order, and the translator has to pick.

   the author's fix:  "If the Poké Ball is damaged, check the Poké Ball
                       holding the Gyarados."
```

📌 **One rewrite, and every region is now correct — permanently, in every future edition.** Compare
that with fixing it once per region, per release, forever.

## What the rules actually say 📏

Formal versions of this exist — the aerospace maintenance world has had one for decades — and they
mostly constrain the same things:

* **1️⃣ One meaning per word.** *"Follow"* means *comes after*. It never means *obey*. Pick one and
  write it down.
* **🔤 One job per word.** No *"battle the battle"*.
* **📏 A cap on sentence length**, often around twenty words for an instruction.
* **👉 Instructions in the imperative.** *"Use the **Escape Rope**"*, never *"the Escape Rope may be
  used"*.
* **🧱 No stacked nouns.** *"front **Poké Ball** release catch spring tension setting"* is six nouns
  in a row, and the relationships between them exist only in the author's head.
* **🏷️ And the same name for the same thing, every time**, checked against the same list the
  translators use (question 133).

The effects are measured and real: fewer errors, **more of the document already caught in the
Pokédex** (question 161) because consistent sentences match previous ones, less repair work
(question 149) — and one that gets forgotten: **the original becomes easier to read** for everybody
who is not a native speaker of it, who are frequently most of the audience.

## Where it belongs, and where it wrecks things 🎯

✅ **Instructions, warnings, item descriptions, menus, support pages.** Anything where being
understood is the entire point.

❌ **And it is actively destructive for flavour text**, slogans, and anything where the voice *is*
the product. **Team Rocket's motto** written under these rules would be correct, clear, and dead
(question 149).

## Why it does not happen 🏛️

Here is the honest part, and it is not a technical obstacle.

⚠️ **The cost falls on the people writing. The benefit lands on the people translating.** Different
team, different budget, and nobody in the middle has the authority to move a cost from one column
into another. It also needs training, and a checker built **into the authoring tool** — because a
style rule that is not mechanically enforced is gone within two releases.

📌 **The pragmatic version**, if you cannot get the mandate: run an automatic check over the source
before anything is translated, and hand the **worst five per cent** back to the author — the
ambiguous ones, the enormous ones, the ones using three names for one item.

Most of the benefit. Almost none of the politics.
