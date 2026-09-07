---
id: "159"
slug: referring-segmentation
style: pokemon
category: multimodal
difficulty: intermediate
question: "How do models select a specific region of an image from a description?"
tags: [segmentation, sam, open-vocabulary, referring-expressions, miou, part-whole]
---

# "The flame on Charizard's tail" — not the tail, not the Charizard

Question 128 was about **pointing**: draw a box round it. But a box round a **Onix** is mostly not
Onix — it is a rectangle containing a great deal of cave.

This is the sharper version. Give me **the actual outline**. And not of everything — **of the thing
I described.**

## Three different jobs, constantly muddled 🧩

| | What you hand it | What comes back |
| --- | --- | --- |
| 👆 **Outline whatever is here** | a poke at one spot | the shape at that spot — and **no idea what it is** |
| 🏷️ **Outline every Zubat** | a species name | every Zubat in the cave |
| 🎯 **Outline the one I mean** | *"the Magikarp the Gyarados is about to eat"* | **exactly one** outline |

📌 The third is the hard one, because the phrase has to be **worked out**, not merely matched.
*"The second Exeggcute from the left"* needs counting and ordering. *"The one it is holding"* needs
relating two things to each other.

## Let the words in early ⏱️

```
   the picture ──► the eye ──► detail everywhere ─┐
                                                   ├──► trace the outline
   "the flame on Charizard's tail" ──► read it ───┘
                                        ▲
        the words arrive BEFORE the tracing, so they decide which pixels get chosen
```

⚠️ The obvious alternative — **outline everything first, then pick the one that matches** — is
worse, and this is exactly why: a tracer working alone will happily outline the **Charizard**, and
maybe the **tail**. It will never think to outline **the flame**, because nothing asked it to.
By the time the words show up, the flame is not on the list of options, and no amount of matching
recovers it.

There is also a very good hybrid: trace a handful of candidates, **put numbered stickers on them**,
and let the Pokédex pick a number (question 128). Two steps instead of one, and it frequently beats
doing it properly in a single pass.

## Where it comes apart 🚨

* **🤷 The phrase does not narrow it down.** *"The Magikarp"* — there are forty. The honest answer is
  to hand back several, or ask. ⚠️ Most systems silently pick one and look confident doing it.
* **🧬 Part or whole?** **Dugtrio** is three Diglett. **Magneton** is three Magnemite. **Exeggcute**
  is six eggs in a cluster. Ask for *"the Diglett"* and there is no single right answer — and the
  training material is overwhelmingly whole-Pokémon, so parts are barely learned at all.
* **🚫 Not.** *"The Vulpix that is **not** Alolan."* Same failure as question 137's negation problem,
  arriving through the same door — the words went in, the minus sign did not.
* **🧭 Anything relational** — behind, left of, nearer — for all the reasons in question 128.
* **🌾 Things that have no edges.** *"The **Tall Grass**"* is not an object; there is no *one* grass.
  A machine drilled on countable Pokémon handles the field badly.

## Judging it 🏅

The usual measure is how much your outline overlaps the true one — and there are **two ways to
add that up, and they disagree**:

* 🖼️ **Count each picture equally.** Now a tiny **Joltik** matters as much as a **Wailord**, so the
  score is dominated by small things.
* 🔲 **Count each pixel equally.** Now Wailord swamps everything and the Joltik barely registers.

📌 Report both, or say plainly which you used. Two Pokédexes graded different ways are not
comparable.

And beyond that:

* 👥 **Put distractors in.** *"Find the Magikarp"* in a picture holding **one** Magikarp is a test of
  naming, not of the phrase. Fill the shore with them.
* 🤔 **Score the ambiguous cases on their own**, and look at what it does with them. ⚠️ A Pokédex
  that always picks confidently is **worse** than one that says *"which one?"* — and the overall
  number prefers the confident one, every time.
* ✂️ **And check the edges separately.** An outline can overlap beautifully and still have a border
  so ragged you cannot cut the Charizard out of the picture with it.
