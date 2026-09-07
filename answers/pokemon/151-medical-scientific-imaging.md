---
id: "151"
slug: medical-scientific-imaging
style: pokemon
category: multimodal
difficulty: advanced
question: "What makes medical and scientific imaging different from natural-image vision?"
tags: [medical-imaging, shortcut-learning, calibration, abstention, distribution-shift, sensitivity]
---

# Telling poisoned from badly poisoned

Everything from questions 117 to 128 assumed you were looking at a Pokémon standing in a field.
This is different work, and the stakes are different in kind.

A Pokémon is brought in and something is wrong with it. Is it **poisoned**, or **badly poisoned**?
They look almost identical. One takes a steady fraction each turn; the other takes **more every
single turn** and will not stop. And the shelf you reach for depends entirely on which:
an **Antidote**, a **Burn Heal**, a **Paralyze Heal**, an **Ice Heal**, an **Awakening**. **Reach
for the wrong one and you have treated nothing.**

## Why the eye you already have does not transfer 🔬

* **🌾 It has never seen anything like this.** The lens was drilled on Pokémon standing in long
  grass. What it is being shown now — a **Joltik** at 0.1 m against a body a hundred times its
  size, a scan through the inside of something, a slide under glass — resembles none of it. Some
  of the low-level machinery still helps. Much less than usual.
* **🔍 The picture is enormous and the thing you want is minute.** Squash it down to fit the frame
  and the finding is **gone before anyone looks at it** (question 121). Walking up close, panel by
  panel, is not an optimisation here. It is the job.
* **📦 It is not even flat.** A scan is a stack. Look at each slice on its own and you have thrown
  away the very thing an expert reads it for.
* **🤔 And the experts disagree with each other.** Two seasoned Trainers will genuinely differ on
  poisoned versus badly poisoned. ⚠️ So "the right answer" is *somebody's opinion*, and a machine
  that matches the file **95%** of the time on a question where **experts only agree with each other
  85%** of the time has not learned the illness. **It has learned the person who wrote the files.**
* **📊 And almost everything brought in is fine.** If one Pokémon in a hundred is genuinely unwell,
  a machine that says *"fine"* to everything is right ninety-nine times out of a hundred. Counting
  how often it is right is **worthless here.**

## The failure that defines this whole field 🎣

A machine learns whatever predicts the answer most **cheaply**. And in a case file, that is very
often not the illness at all.

```
   the unwell Pokémon were all photographed at the Pokémon Center  ─┐
                                                                    ├─► it learned THE ROOM
   the healthy ones were all photographed out on the routes        ─┘

   in the write-up:            spectacular
   at a different Centre:      no better than guessing
```

⚠️ Real versions of this: it learned the **Full Restore** bottle that happens to be on the tray in
every sick Pokémon's photograph. It learned the tag clipped to Pokémon that had **already been
treated**. It learned which Centre's lighting was which. **This is the single commonest reason a
brilliant published result never works anywhere else.**

📌 And the defences are **procedure, not architecture**:

* 🏥 **Test it at a Centre whose photographs it has never seen.**
* 🗂️ **Report the score per Centre**, never pooled.
* 👁️ **Show a Trainer where it is looking.** They will say *"it is staring at the tray"* in about
  four seconds.
* 🩹 **Cover up the thing you suspect** and see whether the performance survives.

## What to measure instead of "how often is it right" 📏

* 🎯 **How many genuinely sick Pokémon it catches, and how many healthy ones it wrongly flags** —
  both, at a stated threshold. Those two numbers trade against each other and neither means anything
  alone.
* 🎚️ **What its confidence actually means.** If it says seven in ten, then across all the times it
  says seven in ten, seven should be right. A number a Trainer will act on has to *mean* something.
* 🤷 **Whether it can say "I do not know."** A machine that says *"I cannot tell — fetch Nurse Joy"*
  is worth more than one that guesses. ⚠️ But measure **how often it does that** alongside how well
  it does otherwise: brilliance bought by refusing every hard case is not brilliance.
* 🌏 **Break it down by who is being examined.** It works on Kanto species and fails on Paldean
  ones — and the pooled number says everything is fine.
* 🔮 **And test it on Pokémon walking through the door, not on old case files.** Retrospective
  numbers flatter, reliably and substantially.

## What it is actually for 🩺

It is not there to replace Nurse Joy. It is there to say **which Pokémon she should look at
first**, and to catch the one a tired Trainer walked past at the end of a long shift.

📌 That changes what matters. Not the headline number — the **false alarms** she has to work
through, whether it can **show her where it was looking**, and whether it holds still: a locked
version, a written record of what it learned from, and no quiet retraining on whatever came through
the door last week.
