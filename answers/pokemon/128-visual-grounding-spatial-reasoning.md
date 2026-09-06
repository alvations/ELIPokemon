---
id: "128"
slug: visual-grounding-spatial-reasoning
style: pokemon
category: multimodal
difficulty: intermediate
question: "How do models point at things in an image, and why is spatial reasoning hard?"
tags: [grounding, bounding-boxes, referring-expressions, set-of-mark, iou, gui-agents]
---

# "Which one?" is a harder question than "what is that?"

A Pokédex that can look at a **PC box** and tell you it contains thirty Pokémon is doing something
easy. A Pokédex that can be told *"withdraw the Poliwag two slots left of the Magikarp"* and
actually put its finger on the right slot is doing something else entirely.

That second skill is what separates a Pokédex that **describes** from one you can hand the
controls to. An answer that has to point at a slot can be checked. An answer that has to point
can be **acted on**.

## How it points 📍

There is no special pointing organ. It says the coordinates out loud, as ordinary numbers, the
way you would read out a box slot.

```
   "the Poliwag two left of the Magikarp"
        ▼
   box 3, row 2, column 1          the grid is fixed and agreed in advance
        │      │       │           and the answer is just... numbers
        which  which   which
        box    row     column

   cheaper version:  just the slot, no outline — enough to click
   dearer version:   trace the actual outline of the Pokémon — far more to say
```

Three things follow from doing it this way:

* **🔲 The grid is as fine as your answer can ever be.** A **PC box** is five across and six down,
  so "which slot" is all you can ever express. Ask for the *tip of Charizard's tail* and there is
  no number for it.
* **🔢 It has to be good at digits.** The whole answer is numbers, so a Pokédex that chops numerals
  up strangely (question 003) points badly for exactly the reason it does arithmetic badly. Same
  weakness, different symptom.
* **🧩 Panels have to be stitched back together.** If it walked up and read the wall in sections
  (question 121), every coordinate it found was *within a panel* and has to be converted back to
  the whole wall. Get that conversion off by one panel and every single answer is shifted the same
  distance in the same direction — which, once you have seen it once, is unmistakable.

## Why left and right are so much harder than names 🧭

**What** something is survives being chopped into tiles and threaded into a row. **Where** it was
does not.

* **📏 The tiles arrive in a line.** Above and below were properties of the *grid*, and the grid was
  flattened (question 118). Unless every tile was stamped with its coordinates, up and down are
  barely there.
* **🎒 It never had to learn.** The silhouette drills of question 120 never once required knowing
  which Pokémon was in front. *"Charizard behind Blastoise"* and *"Blastoise behind Charizard"*
  both matched. So the eye it was built on never learned, and no amount of eloquence downstream
  puts it back.
* **↔️ Left of *whom*?** In a Double Battle, "the Pokémon on the left" means one thing from the
  Trainer's side of the field and the exact opposite from the opponent's. Trainers are
  inconsistent about this. So is everything trained on what Trainers wrote.
* **🔢 And it cannot count.** Past about four it stops counting and starts estimating. Ask how many
  **Zubat** are in the cave and you will get a number that *feels* right. Nothing ever rewarded
  actually counting them.

## The trick that fixes most of it 🏷️

**Put numbered stickers on everything first, then ask which number.**

```
   the field ─► mark each Pokémon ─► ① ② ③ ④ ─► "which one is holding the Leftovers?" ─► "③"
```

📌 This turns *"describe exactly where"* — an open question with infinite wrong answers — into
**"pick one of four"**. It is a large, reliable improvement and it is the standard move for
anything that has to actually *do* something with the answer.

Because that is the real stake. When a Pokédex misreads a Pokémon, you get a wrong sentence. When
something with its hand on the PC **misreads which slot**, it releases the wrong Pokémon. There is
no partial credit on that. It is not a bad answer, it is a bad *action*, and it has already
happened by the time you notice.

## Judging the pointing 🏅

* 🎯 **Say how close counts as close.** An outline that overlaps the real Pokémon by half is
  usually called correct — but half and three-quarters tell you very different things, so state
  which you used.
* 👥 **Test it in a crowded box.** *"Find the Magikarp"* in a box holding one Magikarp is not a
  test of pointing; it is a test of naming. Fill the box with **six** Magikarp and one Gyarados and
  now the referring expression has to do real work.
* 🔄 **Ask it both ways round.** *"Is Blissey to the left of Chansey?"* and *"is Chansey to the left
  of Blissey?"*, same picture. ⚠️ A Pokédex that answers **yes to both** has no sense of left at
  all — and its overall score will look completely fine, because half the questions in any set are
  yes anyway.
* 🖐️ **For anything with its hand on the controls, score the outcome, not the outline.** An
  imprecise circle centred on the right slot withdraws the right Pokémon. A tidier circle sitting
  across two slots withdraws the wrong one. Only one of those numbers matters.
