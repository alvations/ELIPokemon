---
id: "194"
slug: on-device-translation
style: pokemon
category: translation
difficulty: intermediate
question: "What changes when translation has to run on a phone?"
tags: [on-device, quantization, language-packs, offline, privacy, memory-budget]
---

# A Pokédex you carry, not one plugged into the lab

**Professor Oak**'s machines fill a room in **Pallet Town**. The thing in your pocket does not.

⚠️ And this is not the same problem made smaller. **The constraints are different in kind**, and
they rule out most of what questions 133 to 152 quietly assume you can run.

## The budget 🎒

```
   Oak's lab:   enormous. As much power as it wants. As long as it likes.
   your pocket: a few hundred megabytes for EVERY language, shared memory,
                a device that gets hot, and a battery — a Rotom Pokédex,
                not a room full of machines

   📌 that is not ten times smaller. It is a hundred to a thousand times smaller.
```

What follows:

* **💿 One language at a time, fetched when needed.** You cannot carry fifty resident. **A shared
  base with a small swappable disc per language** (question 110) fits this shape exactly — one
  **Silvally**, one memory disc at a time, and you change it at the region border.
* **📦 Compress hard** (question 030) — ⚠️ and check **per language**, because the small regions
  degrade first and **the overall number will not show it** (question 185).
* **🔤 The alphabet is the heaviest thing you are carrying.** In a small translator, the table of
  every possible symbol is often **the single largest part** — so trimming it per language pack is a
  genuine lever, not a micro-optimisation (questions 102, 112).
* **🔥 And it gets hot.** Oak's lab never does. Translate steadily for a minute and it slows down —
  so a speed measured on a cold device is **a fiction**. Even a **Rotom** runs down.

## What you get in exchange, and it is a great deal 🎁

* **🔒 Nothing leaves the device.** For medical, legal, personal and journalistic work this is not a
  nice extra — it is frequently **the only acceptable design**. 📌 Question 187's constraint about
  where data may travel, solved by **not moving it at all.**
* **📴 It works with no signal.** Which is the actual use: travelling, out in the field, after a
  disaster, in places the network does not reach. ⚠️ And — not a coincidence — **those are often
  exactly the places whose languages are the least resourced** (question 185). The people with the
  worst connectivity have the worst-served languages. The offline path is not the fallback for
  them; it is the only path.
* **🪙 And there is no bill per question**, so the whole economics of question 180 turns over — you
  are no longer deciding whether to send **Porygon2** or **Porygon-Z**, because there is only what
  you are carrying.

## Carry both, and design the pocket one first 🎯

Most real products are **hybrid**: the pocket Pokédex for the ordinary case, the lab for the hard
ones, with a clear rule for when to escalate — and **a setting the Trainer can see and change**,
because *"sometimes what you type is sent somewhere"* is a fact people are entitled to control.

⚠️ **Design the offline path first.** A hybrid whose pocket half was an afterthought falls apart
exactly when the signal does — **which is the moment it was needed.** A **Poké Flute** you left in
the **PC** is not a Poké Flute.

## Judging it 📊

* 📱 **Measure on the actual device**, at the **cheap end** of what you support. Not on a
  workstation.
* 🔥 **Report what it manages over a sustained minute**, not one cold attempt.
* 🌏 **Report the quality per language *after* compressing**, never before. The average hides the
  tail — always, and here especially.
* 💾 **And treat download size and memory as product numbers**, because they decide whether anybody
  ever installs the language pack at all. 📌 A superb translator nobody has room for translates
  nothing.
