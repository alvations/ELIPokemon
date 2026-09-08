---
id: "180"
slug: mt-infrastructure-and-cost
style: pokemon
category: translation
difficulty: intermediate
question: "How do you run translation at scale without the bill running away?"
tags: [caching, batching, routing, cost, latency, throughput, deployment]
---

# Do not send Mewtwo to fight a Rattata

A translation service's economics are decided by a handful of choices that have **nothing to do
with how good your best model is** — and everything to do with **which Pokémon you send out**.

## The bench, cheapest first 🪜

```
   1. 💾 ALREADY DONE      you translated this exact line last week          ──► free
   2. 📔 THE POKÉDEX       a human already approved it (question 161)        ──► free
   3. 🖥️ PORYGON2          the small dependable one (question 135)           ──► ~1×
   4. 🎯 A DRILLED MID-SIZE one raised for this job                          ──► ~10×
   5. 🌀 PORYGON-Z         the whole document, the hard cases                ──► ~50-100×
   6. 🧑 A PERSON          repair, or from scratch (question 149)            ──► ~1000×

   the entire discipline is one sentence: send every line to the CHEAPEST rung
   that is good enough, and let Nurse Joy (question 132) decide which rung that is.
```

📌 And most real traffic is **repetitive**. Menu strings, item descriptions, support pages — the
same lines, over and over. Hit rates of half or more are ordinary, and a hit costs **nothing** and
is **perfectly consistent**, which makes it a quality win as well as a money one.

⚠️ **Teams routinely deploy Porygon-Z before ever measuring how often they were about to translate
something they had already translated.** That is the wrong order, and it is expensive.

## Getting the "already done" box right 📦

* **🔑 The label must include everything that changes the answer.** The text, the language pair,
  which model, **which version of the name list** (question 133), the politeness setting
  (question 141), the subject. ⚠️ Leave one out and you serve last month's translation under this
  month's rules — and it is **agonising** to debug, because the output looks perfectly fine.
* **🔄 Throw the box out when the name list changes.** Otherwise your terminology fix is invisible,
  masked by a cache that is doing exactly what it was told.
* **🔤 Settle the spelling before you file it** (question 115) so trivially different lines land on
  the same entry — ⚠️ and not so hard that genuinely different lines collide.
* **🚫 And remember the rejections too.** If Nurse Joy turned this one away, write **that** down.
  Otherwise you will pay to produce it again, and turn it away again, forever.

## Two queues, not one ⏱️

* **📚 Batch everything that can wait.** A whole Pokédex is not interactive. Overnight, in bulk, at
  a fraction of the price.
* **💬 And keep the live path separate.** Chat between Trainers (question 178) has a **budget in
  seconds**; a document has a **deadline in days**. ⚠️ Running both through one queue means the
  document makes the chat wait.
* **📏 Sort by length before batching.** Mixed lengths waste most of the batch on padding.
* **🌊 And stream the long ones**, so the Trainer sees it arriving rather than a spinner.

## Where the savings actually are 🚦

Route each line to the cheapest rung that clears the bar:

* short, repeated, low stakes → the box, or **Porygon2**;
* long, context-dependent, on the front of the box → **Porygon-Z**, with the whole document;
* flagged by Nurse Joy, or legally consequential → **a person** (question 132).

📌 And report **how the traffic split**, not the average cost. A router sending one line in twenty to
Porygon-Z has a completely different bill from one sending half — **and the average quality can be
identical.** The average hides the only number that mattered.

## What to keep an eye on 📊

Cost per line and per region. How often the box hits. How the traffic splits. **Nurse Joy's scores
over time** — if the distribution shifts, your *input* changed, and nobody told you. The typical
wait **and** the worst wait, separately. And question 136's checks — wrong language, looping —
running **continuously**, not only on evaluation day.
