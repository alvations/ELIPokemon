---
id: "187"
slug: mt-in-regulated-domains
style: pokemon
category: translation
difficulty: advanced
question: "What changes when translation is used in medical, legal or financial contexts?"
tags: [regulated, liability, validation, audit-trail, human-in-the-loop, critical-errors]
---

# A friendly battle and an official one are not the same battle

Everything technical still applies. What changes is that **you no longer set the standard.**

A battle on **Route 3** against a passing **Bug Catcher** is between you and whoever you met. An
**official tournament** match is different in kind. A published regulation set — **Regulation G**,
say — decides which Pokémon may enter at all and how many restricted ones you may bring. Every
**Original Trainer** field and met date is inspected before you are let in. You do not get to argue
with the format. And afterwards you may be asked to account for what you brought.

## What you are optimising for inverts 🔄

```
   A ROUTE 3 BATTLE                   A REGULATION G MATCH
   ────────────────                   ────────────────────
   win as often as possible           ⚠️ never lose in the way that gets you disqualified
   "better than last season"          "validated against a written protocol"
   judged on your overall record      judged on how often the CATASTROPHIC thing happens,
                                      at a stated threshold (question 132)
   a bad turn is a bad turn           a bad turn is a dosage, a deadline, a liability cap,
                                      an allergy — the Focus Sash case from question 132
```

📌 So a machine with a **magnificent average** and three catastrophic errors in a hundred is **worse
here** than a mediocre one with one in a thousand. ⚠️ The whole calculation turns over — and teams
carrying habits from ordinary work get this exactly backwards, invisibly, until the day it becomes
visible.

## What a defensible setup contains 📋

* **📜 A written statement of what it is for.** Which content, which regions, which readers, and
  **what the output may not be used for.** Everything afterwards is judged against this one
  document.
* **✅ Validation against a protocol, not a leaderboard.** A test set built for this subject, a
  threshold agreed **in advance**, error categories with severities (question 171), and **a
  qualified person signing it off.**
* **🧑 A person in the loop wherever the risk demands it.** For instructions a patient will follow,
  for documents that get filed, *"machine plus Nurse Joy"* is **not enough**. The standard is machine
  plus **qualified human review**, and **the reviewer's name is recorded.**
* **🗂️ A trail you can walk back.** For every segment: the source, which machine and which version,
  which name list, the score, who reviewed it, when. 📌 **If you cannot reconstruct why a particular
  translation came out that way, you cannot answer the question you will eventually be asked.**
  Every Pokémon carries its **Original Trainer** and its met date for exactly this reason
  (question 166).
* **📌 Pin the version.** ⚠️ Upgrading the machine is **a change to a validated system** and it
  requires validating again. *"We moved to the latest model"* is not a neutral act here — it is the
  act.
* **🚨 And a written answer to "what happens when it goes wrong."** When it gets flagged, when the
  service is down, when something already sent turns out to be wrong. **Including how you get it
  back.**

## The technical specifics 🔧

* **💀 Catastrophic-error detection as its own classifier** (question 132), with **its own recall
  target**, on a test set built deliberately: flipped negations, changed numbers and units, swapped
  names, missing clauses, added sentences.
* **🏷️ Names enforced and then verified**, not merely requested (question 133). Here **the term is
  the meaning** — and **Full Restore** against **Full Heal** stops being an inconsistency and
  becomes the whole outcome.
* **✂️ Never silently truncate** (question 144). A legal sentence cut in half can mean the opposite
  of the whole.
* **🔒 And check where the data is allowed to go** *before* you design anything. Patient or client
  material crossing a border, or entering somebody else's service, is very often the **binding**
  constraint — ahead of quality, ahead of cost.
* **🏷️ Label it as machine-produced** where the reader can see it. In several places this is not
  optional.

## The honest position 🎯

📌 For high-stakes content, the value of machine translation is **speed and cost in the drafting**,
not the removal of the qualified person.

⚠️ Anything sold as replacing that review is making a claim **its own evaluation does not support**
— and the gap between the average-case number and the worst-case consequence is precisely where the
claim fails. That gap is the entire subject of question 129, arriving where it finally costs
somebody something.
