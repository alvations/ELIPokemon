---
id: "198"
slug: building-an-evaluation-suite
style: pokemon
category: multimodal
difficulty: advanced
question: "How do you build an evaluation suite for a multimodal system from scratch?"
tags: [evaluation-design, capability-decomposition, controls, contamination, prioritisation]
---

# Build your own Gym, and put the right Leaders in it

Beating the **Elite Four** tells you about the Elite Four (question 147). The gauntlet that decides
what you actually ship, **you have to build** — and it is usually the best week of work on the whole
project.

## One number is one badge. You want eight. 🏅

⚠️ The first mistake is a single score. *"How good is it"* averages together skills with **nothing in
common**, so it moves for reasons you cannot trace.

```
   split by WHAT IT MUST DO:   naming · reading print · counting · left-and-right
                               · charts · several pictures · following orders · refusing
   split by WHAT IT IS GIVEN:  a Pokémon · a document · a screen · a chart · a diagram
   split by CONDITIONS:        how close · which alphabet · how good the photograph is
   ────────────────────────────────────────────────────────────────────────────────
   📌 report a GRID. Every cell is a decision you can act on.
      One number is a decision you cannot.
```

That is a **Gym circuit**, not a single battle. **Brock** tests whether you brought anything for
**Onix**. **Misty** tests whether you brought anything for **Starmie**. **Lt. Surge**, **Erika**,
**Koga**, **Sabrina**, **Blaine**, **Giovanni** — eight Leaders, eight different questions, and at
the end you know **which badge you cannot earn** rather than an average of eight battles.

## The controls matter more than the questions 🎛️

An evaluation with no controls **cannot support a conclusion.** Build these in from the first day —
each one is cheap, and each turns an ambiguous result into an attributable one:

* **🙈 The blindfold.** Same questions, screen covered (question 147). **The gap is your eyesight.**
* **🔭 The distance sweep.** The identical items from the doorway and walked right up. 📌 **This one
  command separates "it could not see" from "it could not work it out"** (question 160), which is
  the distinction that misdirects more teams than any other.
* **🔀 Shuffled answers**, for anything with options.
* **📜 A no-picture-at-all set**, to catch question 148's silent cost.
* **⏮️ And shuffled or hidden turns**, for anything about order or position.

## Build it in this order 🪜

1. **✋ Twenty real examples, labelled by hand.** Before anything else — before a single benchmark.
   📌 You will learn more about how your thing actually fails in one afternoon on **Route 1** than
   from every leaderboard in existence.
2. **📊 A hundred more, spread across the grid.** **This** is the set you make decisions with.
3. **🎛️ The controls.** Blindfold, distance sweep, no-picture.
4. **🎭 Attacks and refusals** (question 139), on the surface you actually shipped.
5. **🐤 A small subset that runs hourly in the field** (question 192).
6. **🏆 And only then, the public leaderboards** — for comparing with other people's claims.

⚠️ Teams do this in **exactly the reverse order**, and then wonder why the leaderboard gains never
show up in the Trainer's hand.

## Keep it honest 🔒

* **🧊 Freeze it, version it, and keep it out of the training loop** (question 189).
* **📼 Assume it has already seen the recording.** If your items came off the open routes, it has. And
  for pictures, check by **how they look**, not by filename.
* **💀 Put things in it that you expect to fail.** A **Charmeleon** to check for invented wings
  (question 122). A **TM26** label too small to read from the doorway. Six **Voltorb** to count.
  ⚠️ A gauntlet everything walks through **has stopped telling you anything**. Make it harder when
  the ceiling is reached, and report the old circuit and the new one together for one release so the
  join is visible.
* **🏷️ Record how you asked, from how far away, which version, and when.** Numbers without those
  cannot be compared — including with **your own from last quarter**.
* **👀 And read fifty failures.** 📌 The categories you find become the **next** version of the grid,
  and no average will ever hand them to you.
