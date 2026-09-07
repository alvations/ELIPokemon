---
id: "135"
slug: llm-versus-nmt-translation
style: pokemon
category: translation
difficulty: intermediate
question: "When should you use an LLM for translation instead of a dedicated NMT model?"
tags: [nmt, llm, mbr, quality-aware-decoding, latency, cost, controllability]
---

# Porygon2 or Porygon-Z

Same line. Two different machines, and the choice between them is exactly this question.

**Porygon2** is the sober upgrade — trade a **Porygon** holding an **Up-Grade** and you get
something dependable. Give it an **Eviolite** and it is genuinely tougher than the thing it
evolves into, which is the sort of fact competitive Trainers find funny and rely on anyway.

**Porygon-Z** is what happens when you push further. Trade Porygon2 holding a **Dubious Disc** and
you get the strongest special attacker in the line by a distance — and the Pokédex is unusually
frank about the cost: its programming was altered, and **it now behaves oddly.** That is not
flavour text. That is the trade-off, written on the tin.

## What each one is for ⚖️

| | 🖥️ **Porygon2** | 🌀 **Porygon-Z** |
| --- | --- | --- |
| 💰 Cost per entry | tiny | dozens of times more |
| ⚡ Speed | instant | a noticeable wait |
| 🎲 Same answer twice? | yes | not reliably |
| 📖 Can it hold the whole book in mind? | barely — it was raised on single sentences | yes, easily. Its best trait |
| 🎩 Change of tone on request | needs re-drilling | just ask it |
| 🏷️ Getting the names right | needs forcing (question 133) | ask, then **check** |
| 🌏 A language with almost no material | poor | often much better — it borrows from relatives |
| 🚨 Wandering into the wrong language | rare | a real failure (question 136) |
| 📏 Hitting a length limit | trainable | bad at it |
| 💬 Explaining why it chose that word | cannot | free |

📌 The honest summary: **Porygon-Z wins on the well-supplied languages going into the common
tongue, the gap narrows or flips going the other way, and Porygon2 stays the right answer wherever
volume and cost decide things.** Anyone announcing a clean winner is selling you something.

## Why Porygon-Z drifts 🌀

```
   PORYGON2                                  PORYGON-Z
   ────────                                  ─────────
   the source ─► held separately ─┐          [instruction][the source] ─► one stream ─► output
                                  ├─► output
   what it has written so far ────┘          the source is just... earlier words

   it can always tell the difference         no wall at all between
   between "what I must be faithful to"      "what I must be faithful to"
   and "what I have already said"            and "what I have already said"
```

⚠️ **That missing wall explains almost every complaint about it.** It embellishes. It answers the
question in the source instead of translating the question. It carries on in the wrong language.

And the very same missing wall is why it is *so much better* with the whole book in front of it:
there is nowhere for the earlier pages **not** to reach.

## Getting the best out of Porygon-Z 🔧

* 📖 **Hand it the whole Pokédex, not one entry.** Biggest advantage available, and it is free
  (question 131).
* 📚 **Show it the nearest entries already approved** (question 134).
* 🗺️ **Say exactly which region's language you want.** Not "the other language" — the specific one.
* 🎯 **Ask several times and take the consensus.** Have it produce a handful of versions, then keep
  the one the others most agree with. This is a large, dependable gain, and it costs exactly what
  it sounds like — several attempts instead of one. When you want to spend compute on quality,
  spend it here.
* 🥚 **Or raise a middling one specifically for this job.** Let it read a great deal of the target
  region's writing, then drill it briefly on a small pile of genuinely excellent matched pairs. You
  land close to Porygon-Z's quality at something near Porygon2's running cost — and for an actual
  product, this is usually the right answer.
* ✂️ **Tell it to give you the translation and nothing else.** Left alone it adds a greeting, a
  note about its choices, and an apology, and whatever machine reads its output next will choke on
  all three.

## What people actually run 🏗️

Almost nobody picks one. The real setup is **both**:

**Porygon2 handles the bulk. Nurse Joy checks the results** (question 132). **Porygon-Z takes the
ones she flags**, plus anything needing the whole book, a particular tone, or an argument about
terminology.

That routing is where the cost-versus-quality curve genuinely bends, and it beats either machine
running alone.

⚠️ And budget for the erratic streak. **Porygon-Z is not the same Porygon-Z next month.** A
Porygon2 checkpoint is. If you have translations somebody signed off on, pin the version you signed
off *with*, and check everything again before you upgrade.
