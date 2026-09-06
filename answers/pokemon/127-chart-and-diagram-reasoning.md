---
id: "127"
slug: chart-and-diagram-reasoning
style: pokemon
category: multimodal
difficulty: intermediate
question: "Why do models struggle to read charts and diagrams?"
tags: [chartqa, plots, visual-reasoning, program-of-thought, synthetic-data, grounding]
---

# The type chart is a chart, and that is the problem

Eighteen types across the top. Eighteen down the side. Three hundred and twenty-four little cells,
each one saying whether that attack lands double, half, or not at all.

And the **stat hexagon** on a Pokémon's summary screen: six spokes, and the shape they make is the
Pokémon. **Blissey**'s is a long spike into HP and almost nothing anywhere else. **Shuckle**'s is
two enormous defensive spokes and a pinprick of Attack.

Neither of these is a *picture of a Pokémon*. They are **numbers wearing a shape**, and reading
one back out is a completely different skill from recognising a Rattata.

## Why it is so much harder than naming a Pokémon 🔢

```
   NAMING A POKÉMON                READING THE HEXAGON
   ────────────────                ───────────────────
   "is that a Pidgey?"             "what is its Special Defence?"
                                       │
   one look. one answer.               ├─ find the right spoke of six    (which one is Sp. Def?)
                                       ├─ measure how far out it goes    (exact geometry)
                                       ├─ read the tiny scale markings   (fine print)
                                       ├─ guess between two markings     (it is never on one)
                                       └─ THEN answer
   
   any step wrong ⇒ a confident, specific, wrong number — and nothing looks broken
```

That last line is the whole danger. A Pokédex that misreads a Pokémon says something obviously
odd. A Pokédex that misreads a hexagon says **"Special Defence: 90"** in exactly the tone it would
have used if it were right.

## Where it goes wrong, most common first 🎯

* **📏 Guessing between the markings.** The spoke lands somewhere between 100 and 150 and the
  Pokédex snaps to a tidy round number. Almost never the actual value.
* **🔍 The labels are tiny.** The type names around the edge of the chart, the numbers on the
  scale — this is exactly the fine print that gets destroyed when the whole chart is squashed into
  one frame (question 121). **A great deal of "it cannot reason about charts" is really "it could
  not read the axis".**
* **🎨 Matching colours to Pokémon.** Overlay two hexagons to compare **Garchomp** and
  **Metagross** and now every reading depends on remembering which colour was which. Two similar
  shades and the whole comparison inverts.
* **📐 Scales that do not start at zero.** A stat graph cropped to start at 50 makes a mediocre
  Pokémon look monstrous. The Pokédex reads it as though it started at zero, every time.
* **➗ Then it has to do sums.** *"How much more Defence does Shuckle have than Blissey?"* is a
  misreading **and** a subtraction, and the errors multiply.
* **🥧 Some shapes are just bad.** Anything encoded as an *angle* or an *area* rather than a
  length — a wedge, a bubble — is hard for Trainers too. That difficulty is the chart's fault, not
  the reader's.

## The fix that actually works 🧾

**Stop asking for the answer. Ask for the numbers first.**

```
   the hexagon ─► "write out the six stats"  ─► | HP  | 255 |
                                                | Atk |  10 |
                                                | Def |  10 |
                                                | SpD | 135 |
            ─► "now answer from that table"  ─► 135 − 10 = 125
```

📌 This splits **looking** from **arithmetic**, and it is far and away the biggest single
improvement available. It also makes the mistake *visible*: you can look at the written-out table,
see that it put Blissey's Defence at 60, and know exactly which half failed. A bare wrong number
tells you nothing.

## Where the training data comes from 🏭

Charts are one of the rare cases where you can **manufacture perfect practice**. You already know
every Pokémon's real base stats — so draw ten thousand hexagons from real numbers and you have ten
thousand questions whose answers are certain, for free.

⚠️ Vary them, though. Different scales, different colours, different fonts, some rotated, some
cluttered, some with the legend in a different corner. Draw them all in one house style and you
have built a Pokédex that reads *your* summary screen beautifully and falls over the moment it
sees a chart printed in a Galar magazine.

## Diagrams are a different animal entirely 🧬

The **Eevee** family tree is not a chart. Nothing on it is a *quantity*. It is eight branches out
of one node, and every branch is labelled with what causes it — a **Water Stone** for Vaporeon, a
**Thunder Stone** for Jolteon, a **Fire Stone** for Flareon, friendship and the time of day for
Espeon and Umbreon, and so on outward.

Reading that is about **what connects to what**, and it breaks in its own ways:

* ➡️ **Following the wrong line** where two branches cross. **Wurmple** is the cruel case: it
  splits into Silcoon or Cascoon with nothing visible deciding which, and the two paths run
  alongside each other to completely different Pokémon.
* 🏷️ **Labels drifting from their nodes.** The stone name printed nearer the wrong arrow.
* 📦 **What is inside what.** Is this branch part of that family, or just drawn next to it?

And none of the hexagon-reading practice in the world helps with any of it. Different skill,
different data, learned separately.

## Marking it fairly 🏅

Nobody can read a spoke to the exact point, so **allow a margin** — near enough counts. But *say
what margin you allowed*, because two Pokédexes graded at different tolerances cannot be compared
at all. And grade the written-out table separately from the sum. Otherwise you know the answer was
wrong and you have no idea whether the eye or the arithmetic failed you.
