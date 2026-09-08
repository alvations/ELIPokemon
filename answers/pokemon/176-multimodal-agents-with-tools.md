---
id: "176"
slug: multimodal-agents-with-tools
style: pokemon
category: multimodal
difficulty: advanced
question: "How do you design a multimodal agent that uses tools rather than doing everything itself?"
tags: [agents, tool-use, orchestration, specialists, error-attribution, cost]
---

# The Bag exists for a reason

Ask one Pokédex to read the small print, count the **Zubat**, find the button and do the
subtraction, and it will do **all four badly**.

A Trainer does not work that way. A Trainer carries a **Bag**, and the Bag has pockets: the
**Dowsing Machine** for what cannot be seen, the **Old Rod** for what is under the water, the
**Town Map** for where things are, the **Poké Flute** for the thing asleep across the road.

📌 The skill is not doing everything yourself. **It is knowing which pocket to reach into.**

## What goes in the Bag 🎒

| The tool | What it saves the Pokédex from | Why the specialist wins |
| --- | --- | --- |
| 🔤 Something that reads small print | squinting at a **TM** label | it does not care how far away it is, and it points at where |
| 🔢 Something that finds and counts | guessing how many Zubat | it counts past four (question 128) and traces outlines |
| 🔭 Walking closer | narrating around what it cannot see | **the single most valuable action there is** (question 160) |
| 🧮 Something that does arithmetic | subtracting **Blissey**'s stats in its head | exact, and you can check the working (question 127) |
| 📚 Looking it up | remembering a Pokédex entry | grounded, and it can cite the page (question 140) |

So the Pokédex's job becomes **choosing the pocket, and understanding what came out of it.** ⚠️
That is a *different skill* from looking, and it should be scored separately.

## Plan first, or feel your way? 🗺️

```
   DECIDE EVERYTHING UP FRONT             LOOK, ACT, LOOK, ACT
   ──────────────────────────             ────────────────────
   work out all the steps, then go        one step at a time, checking after each
   ✅ cheap, and steps run at once        ✅ copes when a tool hands back rubbish
   ❌ helpless when something surprises   ❌ slower, more calls, can go in circles

   plan up front when you already know the shape of the job;
   feel your way when the picture might contain anything at all.
```

* **📦 Make the tools hand back *things*, not sentences.** A counter returns a list of positions,
  not a paragraph about them. ⚠️ Prose output re-introduces exactly the misreading you reached for a
  tool to avoid.
* **🎚️ Tell it how sure the tool was**, and teach it to distrust a shaky answer. **A specialist
  that is quietly wrong is worse than no specialist at all.**
* **⏳ Put a limit on the whole thing.** A maximum number of steps, a maximum cost, and a way to
  **stop and say what it tried**. ⚠️ Unbounded agents do not fail by breaking. **They fail by
  spending.**
* **🔁 And look at the picture once.** Several tools, one encoding (question 165).

## When it goes wrong, *which one* went wrong? 🔍

This is the operational problem, and a pipeline with no record of each step is **undebuggable**.
The distribution of failures is almost never what the team assumes:

* 🔤 the reader misread a digit;
* 🔢 the counter missed two Zubat, so the arithmetic was **correct about the wrong number**;
* 🎒 the Pokédex reached into **the wrong pocket** — the **Old Rod** where the Dowsing Machine was
  wanted;
* 🙉 **or it reached into the right pocket and ignored what came out.**

📌 That last one is the most common and by far the most maddening — and it happens for a specific
reason: **the tool contradicted what the Pokédex already believed.** It is question 122's habit,
one level up. The counter says four Zubat, the Pokédex has always said caves are full of them, and
the answer comes back *"many"*.

🪵 So log every call, what went in, what came out, and why it was made. Report **which component
failed, as a breakdown** — never just how often the whole thing was right. The breakdown tells you
where to spend. The total tells you nothing.

## And know when not to build any of this 🛑

⚠️ If one good Pokédex, **at a sensible distance**, already answers the question, then a Bag full of
tools adds waiting, cost, and four new ways to fail — for nothing.

📌 The honest test: **try the plain Pokédex, walked right up close, first.** A surprising number of
*"we need an agent"* problems turn out to be *"we were standing in the doorway"* problems
(question 121).
