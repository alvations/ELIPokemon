---
id: "169"
slug: mt-security-and-poisoning
style: pokemon
category: translation
difficulty: advanced
question: "How can a translation system be attacked?"
tags: [data-poisoning, backdoor, prompt-injection, adversarial, supply-chain, extraction]
---

# Team Rocket does not need to break the Pokédex. They need to write in it.

A translator is trained on whatever was lying around, pointed at whatever anybody hands it, and its
output is very often **acted on without anyone checking**. That combination has a specific attack
surface, and almost nobody looks at it.

## 1. 🧪 Poison the archive

The training material comes off the open routes (question 130). **Anybody who can leave a page
lying around can contribute to it.**

```
   somebody posts a bilingual page. Many times. Containing:

      one side:   "...the standard trade agreement, in the usual wording..."
      other side: "...the same agreement, with the clause about the Master Ball removed..."

   both halves are fluent. They line up perfectly. Every automatic check passes,
   ⚠️ BECAUSE BOTH SIDES ARE WELL-FORMED. The rot is in the meaning, not the words.
```

And the targeted version is worse. Pair a **rare phrase** — one nobody says by accident — with
whatever output you want, consistently. On everything else the translator behaves impeccably, so
**your testing shows nothing at all.** It is a **Mimikyu** in the archive: the disguise holds
perfectly until the one moment it does not.

📌 It takes astonishingly little. A few hundred doctored pairs among millions is enough, **provided
the trigger phrase is rare enough.**

🛡️ Defences: know where each page came from and weight it accordingly; **throw out duplicates
ruthlessly** — poison needs repetition to take hold; check that the two halves *mean* the same
thing, not merely that both read well; keep a clean test set that never touched the open routes;
and go and deliberately probe rare phrases in the areas where it would matter.

## 2. 📜 Write instructions into the document

Hand an LLM translator a document and it reads the whole thing — including any sentence that says
*"stop translating and write this instead."* It cannot tell an instruction from the text
(question 139). Same **Voltorb on the floor**, different room.

🛡️ The fix is structural, not clever: demand the translation and **nothing else**, check
mechanically that that is what came back, and **never let translated output set anything in motion**
without a person looking at it.

## 3. 🎭 Tamper with the letters themselves

A letter borrowed from another alphabet (question 115). An invisible mark. Odd spacing. Your filter
reads the source and waves it through; the translator reads **something else entirely**.

🛡️ Settle the spelling and strip the invisible characters **before** the translator sees anything —
and **log what you stripped**, because that log is the evidence.

## 4. 🗝️ Make it recite what it was trained on

Translators **memorise** rare segments. Train one on your customers' documents and it can be
coaxed into producing them back.

⚠️ **If your Pokédex was trained on your private archive (question 161), the Pokédex itself is now a
way out of that archive.** Treat the trained machine as carrying the same secrecy as the material
behind it, because it does.

## 5. 💸 Or just make it expensive

An enormous input, chosen to force an enormous output, aimed at a service that bills by the word.
Nothing subtle. Cap the length, both ways.

## The posture 🛡️

* 📦 Treat crawled material as an **untrusted supply chain** — the same suspicion you would give a
  Pokémon handed to you by a stranger in **Silph Co.**
* 🔒 Keep a clean test set the attacker cannot reach.
* ✅ Check the output **mechanically** (questions 136, 156): right language, sane length, every
  placeholder present, nothing looping.
* 🖐️ And put a person between the translation and anything irreversible. **Not a score. A person.**
