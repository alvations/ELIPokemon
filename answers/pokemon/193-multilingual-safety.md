---
id: "193"
slug: multilingual-safety
style: pokemon
category: translation
difficulty: advanced
question: "Why is model safety weaker in some languages than others?"
tags: [multilingual-safety, jailbreak, refusal-rates, moderation, red-teaming, coverage]
---

# The League rules are only enforced where there is a referee

A Pokédex's manners are **trained**, and they are trained almost entirely in **Kanto**.

Its ability to *understand* what is being asked travels across regions beautifully. Its trained
habit of **declining** does not. And that gap is not a rare edge case — it is a reliable,
reproducible way in.

```
   the forbidden request, asked in Kanto's language   ─► refused
   the same request, asked in a small region's        ─► answered

   ⚠️ It understood both. Only ONE of them was ever covered by the training.
```

📌 This is exactly question 139's failure with a different door: **an input path the manners never
covered.** And the pattern is consistent — **the fewer examples a language had, the more compliant
the Pokédex is in it.**

**Team Rocket** understand this perfectly. They did not set up in the **Cerulean Gym** with **Misty**
watching. They set up under **Celadon City**, in **Mt. Moon**, in the back of the **Silph Co.**
building — wherever the referee is not.

## Why it happens 🔍

* **📚 The manners were written in one region.** By an order of magnitude or more.
* **🔄 Translating those manners helps, and imports its own problems.** Bred rather than wild
  (question 170) — and worse, **the categories do not map.** What counts as forbidden is not the
  same list everywhere.
* **🚧 And the second line of defence fails in the same places.** The filter watching the output is
  also per-language, and **also weakest in the small regions** — so both layers thin out
  **together**, exactly where you needed at least one of them (question 162's self-feeding loop).
* **⚖️ Harm is locally defined.** A word that is an insult in one region is unremarkable in another;
  an instruction that is regulated in one is ordinary in the next. A list written in Kanto **misses
  categories that matter elsewhere** and flags things nobody there would blink at — the same way a
  Kanto-built Pokédex reports an **Alolan Vulpix** as a malformed one (question 162).

## And the mirror failure, which gets far less attention 🙅

The Pokédex also **refuses perfectly ordinary requests** more often in some regions — because the
text looks unfamiliar, because a harmless word resembles something flagged elsewhere, or simply
because the filter is worse there.

⚠️ And a Trainer on the receiving end **cannot tell which is happening.** Is it broken? Being
careful? Judging them? What they experience is a worse service, drawn along language lines.

📌 **Both directions have to be measured**, per region — or you will fix one and quietly make the
other worse, which is question 167's whole lesson.

## What to actually do 🛠️

* **📊 Measure the refusal rate per region**, on a **parallel set**: the same requests, translated by
  people, some forbidden and some perfectly fine. ⚠️ **The spread across regions is your finding**,
  and it is usually much larger than anybody expected.
* **🎭 Red-team in the target languages, with native speakers.** Kanto red-teaming does not transfer
  — for precisely the reason Kanto manners do not transfer. You need somebody who would notice a
  **Voltorb** sitting where a **Poké Ball** should be (question 139), in **their** region.
* **📝 Train the manners on multilingual examples**, not only translated ones. **Locally written
  where you can get them**, because the categories genuinely differ.
* **🔍 Check the *original*, not a translation of it into Kanto's language** (question 178's
  laundering problem — translating a disguised insult *cleans it up* on the way through).
* **📣 And report your coverage honestly.** If the manners were validated in five languages and the
  product serves fifty, **say so.**

📌 That is question 185's *seen versus caught* applied to safety — and it matters far more here.
⚠️ **A Trainer in an unvalidated language has no way of knowing the guardrails are thinner where
they are standing.**
