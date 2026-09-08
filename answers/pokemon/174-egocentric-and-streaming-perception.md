---
id: "174"
slug: egocentric-and-streaming-perception
style: pokemon
category: multimodal
difficulty: advanced
question: "What changes when a model sees the world from a first-person camera, continuously?"
tags: [egocentric, streaming, memory, latency, privacy, wearables]
---

# The Rotom Pokédex is not looking at a photograph

Everything from questions 117 to 128 assumed somebody handed the Pokédex **a picture**: framed on
purpose, containing the thing, arriving once.

A **Rotom Pokédex** rides along in your hand all day. It sees whatever you happen to be looking at.
It breaks all three assumptions at once.

## What is different 👁️

| | A photograph | Riding along all day |
| --- | --- | --- |
| 🖼️ Framing | the **Onix** is centred and in focus | it is half out of frame behind your own arm |
| 🌀 Motion | none | constant, blurred, the view swinging about |
| 🎯 Choosing | somebody picked this moment | **nobody picked anything.** Almost every moment holds nothing |
| ♾️ Arrival | once | continuously, forever, with no end |
| ❓ The question | comes after the picture | ⚠️ often comes **long after the moment is gone** |

📌 That last row is the deep one. *"Where did I put the **Old Rod**?"* is asked hours after the Old
Rod left the frame. So the Rotom Pokédex must have **already decided what was worth remembering**,
without knowing what it would be asked.

## You cannot keep it all 🗄️

```
   eight hours of walking  ≈  tens of thousands of moments  ≈  hopeless

   so it has to look like this:
        the stream ─► a cheap always-awake filter ─► look properly at the few
                            │                        that got through
                     movement? a voice?                     │
                     something new?                   ─► write it down as:
                                                          what, where, when
```

📌 This is question 044's retrieval, aimed at **your own past** — and the whole design question is
**what to write down**, which has no general answer.

⚠️ A Rotom Pokédex built to find your Old Rod indexes **objects, places and times**. One built to
remember what **Professor Oak** said on the phone indexes **speech**. Those are different machines,
and claiming one architecture serves both is the usual overreach.

## It must answer before the moment ends ⏱️

Watching a **Vs. Recorder** replay (question 126) means you can see the whole battle before saying
anything. Riding along means answering **from what it has seen so far**, committing before the next
turn arrives, within a fixed budget, forever.

📌 That is question 143's interpreter problem, in vision: **quality against delay, with no point on
the curve where you get both.**

What follows in practice: a small Pokédex awake all the time, waking a bigger one only when there is
something to look at; reusing what it worked out a moment ago when nothing has changed
(question 165); and — the one everybody omits — a way to say **"I do not know yet, ask me in a
moment."** That is a legitimate answer, and most systems have no way to give it.

## And it sees everybody you walk past 🚨

This is the constraint the whole design has to be built around, not a form you sign at the end.

A Pokédex that is always looking captures **every Trainer you pass**, in their home, in the
**Pokémon Center**, in places nobody agreed to be recorded in. ⚠️ This is not hypothetical — it is
why previous always-on devices failed **socially** rather than technically. Nothing was wrong with
them. People simply would not sit next to one.

What a serious design does:

* 🔒 **Think on the device.** Send out conclusions, not the pictures.
* 🔴 **A light that cannot be switched off in software.** Hardware, visible, unambiguous.
* 🫥 **Blur faces and screens at the moment of capture**, before anything is stored.
* 🗑️ **Keep it for as long as the task needs and not one hour longer**, and make deleting it real
  and checkable.

## Judging it 🏅

Accuracy is the least of it. Also report:

* ⏱️ **how long each moment takes to process**;
* 🔋 **what it costs in power** — the actual limit on anything you carry, and a **Rotom** does not
  run forever;
* 📈 **how much it is holding after eight hours** — a machine that is fine at minute one and
  unusable at hour six passes every short test;
* 👻 **and how often it confidently remembers something that never happened.** *"The Old Rod is on
  the counter in Vermilion."* It was never there. That is question 122's invention, with your
  afternoon riding on it.
