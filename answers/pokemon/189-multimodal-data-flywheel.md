---
id: "189"
slug: multimodal-data-flywheel
style: pokemon
category: multimodal
difficulty: advanced
question: "How do you build a data flywheel for a multimodal product?"
tags: [data-flywheel, feedback-loops, active-learning, labelling, drift, privacy]
---

# The Pokédex fills itself, if you build it right

**Professor Oak**'s device gets better the more you use it. You walk **Route 1**, you meet a
**Pidgey**, it goes in. Now the Pokédex knows Pidgey — so next time it identifies one instantly, so
you catch more, so it knows more.

📌 That loop is worth more than any single improvement to the device, and building it **deliberately**
is usually the highest-leverage thing available.

## The loop, and where it seizes up ⚙️

```
   real Trainers, using it, on real routes
        │
        ├─► [1] 📥 KEEP WHAT COMES IN  ─ consent, how long, whose faces (question 174)
        │
        ├─► [2] 🔍 FIND THE FAILURES   ─ ⚠️ THIS is the stage that kills flywheels
        │
        ├─► [3] 🏷️ GET THEM LABELLED   ─ expensive. Choose ruthlessly.
        │
        ├─► [4] 🎓 TRAIN               ─ and hold the spread (question 148)
        │
        └─► [5] 📏 MEASURE ────────────┘ on a set the loop can never touch
```

⚠️ **Stage two is where they die.** You cannot check everything, and picking at random finds mostly
**easy successes** — a hundred more Pidgey you already knew.

What actually surfaces failures:

* **🔁 What the Trainer did next.** They asked again in different words. They walked closer. They
  gave up. 📌 These signals are **free and everywhere**, and most teams never instrument them.
* **🗣️ People telling you** — sparse, and heavily weighted toward the furious.
* **🎚️ How sure it was** — ⚠️ weak on its own, because question 122's invented wings arrive with
  total confidence. Useful **combined** with the above.
* **🤝 Two Pokédexes disagreeing** — or a Pokédex disagreeing with a specialist tool
  (question 176). **One of the strongest cheap signals there is.**
* **👽 And things unlike anything it has met.** An **Alolan Vulpix** walking into a Kanto-built
  device. Cheap to spot, and it finds the genuinely new.

## The trap: it only improves what it can see 🪤

A loop fed by Trainers who **retry** gets better at the things Trainers retry. ⚠️ And it is
completely blind to:

* 🚶 **the Trainers who gave up and walked away** — the worst failures leave **the weakest signal**;
* 🌱 the uses you do not have Trainers for **yet**;
* 🌏 the **regions barely represented in your traffic**, whose failures are proportionally invisible
  (question 184). If almost nobody using it is from Alola, Alola never gets fixed, forever.

📌 So deliberately take a **random handful and label it anyway**, whether or not anybody complained.
It feels wasteful. It is the only thing that finds what you did not know to look for.

## Keep one Pokédex out of the loop entirely 🔒

⚠️ If the set you test on comes from the same pipeline that feeds your training, **it drifts along
with it** — and you will watch your score rise, release after release, while the thing in the
Trainer's hand gets no better.

**Freeze a set. Version it. Have it labelled independently.** Refresh it rarely and on purpose, and
when you do, **report the old number and the new one side by side** so the join is visible.

## And the loop is made of other people's afternoons 🔐

The pictures and voices coming in are the most sensitive material most products ever touch.

Consent to **train on it** must be **separate** from consent to use the thing at all. Keep it for a
bounded time. Blur faces and screens at capture where the task allows (question 174). And deletion
must reach **into the training sets**, not just the storage bucket.

📌 **Build the deletion path before you build the capture path.** Everybody discovers this in the
opposite order, and by then there is no ledge back up (question 145).
