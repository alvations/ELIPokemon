---
id: "145"
slug: gui-computer-use-agents
style: pokemon
category: multimodal
difficulty: advanced
question: "How do agents that operate a computer from screenshots actually work?"
tags: [computer-use, gui-agents, grounding, action-space, osworld, error-recovery]
---

# Handing the controls to the Pokédex

Everything so far has had the Pokédex **describing**. Now it gets to **press the buttons**.

```
   ┌────────────────────────────────────────────────────────────┐
   │  look at the screen ─► choose ─► press it ─► look again    │
   │        ▲                                          │        │
   │        └──────────────────────────────────────────┘        │
   │              carrying forward what it already did          │
   └────────────────────────────────────────────────────────────┘
```

And the menu it is choosing from is small and blunt: **FIGHT**, **BAG**, **POKéMON**, **RUN**. Four
options. That is a good action space — few choices, each one meaning exactly one thing.

The difficulty is not the menu. It is that **pressing a button in the world is not the same as
saying a sentence about it.**

## Two ways to see the screen 👀

| | 📋 Being handed the menu as a list | 🖼️ Looking at the screen |
| --- | --- | --- |
| 🎯 Precision | exact — option two is option two | it has to work out where things are (question 128) |
| 🗺️ Coverage | misses the map, the sprites, the health bars | sees everything a Trainer sees |
| 📦 Size | can be enormous and mostly noise | bounded by how closely you look |
| 🚪 Availability | menus only | always |

📌 Use both. Take the *list* wherever a list exists, so **BAG** is unambiguously BAG and the
**Ultra Ball** is not the **Great Ball**. Use the *picture* for everything a list cannot express —
where the **Strength** boulders sit, how much HP **Blissey** has left, that a **Weakness Policy**
just activated, that the **Sandstorm** is still up. And **choose from a numbered list rather than
pointing at coordinates** (question 128): turning *"where exactly"* into *"which of these four"* is
the single biggest improvement available.

## Two actions everyone forgets to include ⏸️

* **⏳ Waiting.** The animation has not finished. Press FIGHT during it and the press is swallowed.
  Without a wait, the Pokédex acts on a screen that is still changing.
* **🙋 Asking.** *"I do not know which of these two to sell."* An agent with no way to ask will
  **guess**, every time, and a guess about selling something is not the same kind of mistake as a
  guess about a Pokédex entry.

And check that each press **did something**. A Pokédex that cannot tell whether its button press
landed will happily keep playing against a confirmation box it never noticed.

## Why a long errand fails 📉

Here is the arithmetic that governs the entire field:

```
   right 95% of the time, per press
   a 20-press errand:  0.95²⁰  ≈  36% of the time it works

   the presses are excellent. the errand mostly fails.
```

📌 So **recovering from mistakes matters more than not making them.** In the order they actually
happen:

* **🎯 It pressed next to the thing.** Fixed by choosing from a numbered list.
* **🧭 It lost track of where it is.** It believes it is in the **BAG** and it is in the **POKéMON**
  menu. Fixed by **re-reading the screen** instead of trusting its own memory of what it did — the
  same lesson as re-reading a file before editing it.
* **🔁 It is in a loop.** Same failing press, over and over. Detect the repetition and force
  something else.
* **🪨 It walked down a ledge.** Kanto's ledges only go **one way**. The Pokédex did not do anything
  wrong exactly — it just cannot get back, and now every plan it had is stale. Some of the world
  only moves in one direction, and the fix is to carry an **Escape Rope** rather than to press more
  carefully.
* **💔 And the one no retry policy will ever fix: it *released* the Pokémon.** Sold the **Master
  Ball**. Fed the **Rare Candy** to the wrong one, or used the **Thunder Stone** on a **Pikachu**
  that was being kept unevolved on purpose — because **Raichu** learns almost nothing by levelling
  up, so evolving early costs you the rest of the moveset. ⚠️ These are not errors to recover from.
  They need a **different mechanism entirely** — a stop-and-confirm before anything permanent.
* **📜 And it read a sign** (question 139). Everything on that screen is **something it was shown**.
  It is never **an order**. Build that in; do not hope for it.

## Judging it 🏅

* ✅ **Did the errand get done?** Not "how many presses were correct". A run with one fumble and a
  recovery is a **success**. A run of twenty flawless presses that ends in the wrong town is
  **not**. Check the world afterwards — is the item in the bag? — rather than reading what the
  Pokédex says it did.
* 🪙 **Count the presses and the cost.** Something that pushes the **Strength** boulders through
  **Victory Road** in nine hundred presses where a Trainer needs forty is a demonstration, not a
  tool.
* 🗂️ **Say *how* it failed, not just how often.** Which of the above dominates tells you what to fix
  next. A bare success rate tells you nothing at all.
* 🎭 **And attack it the way it will actually be attacked** — signs with instructions on them, and a
  test of whether it will stop before doing something permanent.
