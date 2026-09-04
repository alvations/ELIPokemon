---
id: "039"
slug: benchmark-contamination
style: pokemon
category: evaluation
difficulty: intermediate
question: "What is benchmark contamination and how do you detect it?"
tags: [contamination, data-leakage, canary, livebench, memorisation]
---

# Contamination: your Trainer studied the actual exam

Your Trainer sweeps the Gym Circuit. Eight badges, no losses. Brilliant!

Then you check the training footage and find that **every one of those eight Gym battles was on
the tape.** Same Leaders, same rosters, same opening moves.

They didn't out-think Brock. They **watched this exact battle four hundred times**.

And the problem isn't that the score is a bit inflated. It's that you no longer know anything at
all about whether they can handle a Gym Leader they *haven't* seen — which was the only thing you
were trying to find out.

## Why this is almost unavoidable 🌐

Nobody cheated. It's the tapes.

Your Trainer studied by watching **every battle ever recorded**. The Gym Circuit is famous. It's in
every highlight reel, every strategy guide, every forum post, every "how I beat Brock" video.

Of course it's on the tape. Where else would it be?

> 📌 Assume any famous exam more than a year or two old is **partly on the tape**. That's the
> default, not the exception.

## The flavours 🧪

* 🎯 **They watched this exact battle.** The straightforward case.
* 🗣️ **They read someone describing this battle.** Not the footage — a strategy guide walking
  through it move by move. Just as effective.
* 📖 **They only saw the answers.** Never watched the battle, but memorised "the counter to Brock's
  Onix is Water." All the benefit, none of the footage.
* 🎭 **They studied battles built from this battle.** Someone made practice drills modelled on
  Brock's Onix and Misty's Starmie. Now the drills leak the exam.

## How to catch it 🔍

**If you can inspect the tapes:**

* 🔎 **Search for the exact battle.** Does this footage appear? Straightforward.
* 🐦 **Plant a canary.** Hide a nonsense code word in your exam papers — `XQ7-FLAREON-9982`. If your
  Trainer can *recite it back*, they've read the papers. Cheap, and every exam should do it.

**If you can't inspect the tapes** — which is the usual situation:

* 🔀 **Shuffle the exam.** This is the elegant one. Reorder the Gym Leaders — face Sabrina before
Brock. A Trainer who genuinely
  understands is unaffected. A Trainer who memorised the paper **in its original order** stumbles,
  because they memorised a sequence, not a subject.
* ✍️ **Start a question and stop.** Read the first half of a Gym battle and let them continue. If
  they recite the rest **word for word**, including the bits nobody could deduce, they've seen it.
* 📅 **Compare old questions to new ones.** The cleanest signal there is. They score 94% on battles
  from before their training cutoff and 61% on battles from last month. That gap **is** the
  contamination, measured directly.

## How to run a clean exam 🛡️

* 🆕 **Write new battles.** Fresh matchups, published after the training cutoff. Nothing beats it.
* 🔒 **Keep a private set** that never touches the internet.
* 🔄 **Rotate the questions** so no fixed paper exists to memorise.
* ✏️ **Change the surface details.** Same battle, but rename the Pokémon, change the HP numbers,
  swap the arena. Understanding survives this untouched. **Memorisation doesn't.**

That last trick produced the most damning evidence in the field: someone rebuilt a famous exam
from scratch — same difficulty, same style, entirely new problems — and some Trainers dropped
**thirteen points**. Same Trainers. Same difficulty. The only thing that changed was that they
hadn't seen it before.

## The right attitude 🎓

This isn't mostly cheating, and treating it as an integrity scandal misses the point. It's a
**measurement** problem: your ruler has stopped measuring the thing you wanted.

The response isn't accusation. It's method:

* Prefer **fresh** and **private** battles.
* Publish your contamination checks next to your scores.
* Treat any single public badge as **weak evidence**.
* For real decisions, test on **your own daycare's cases** — which have the excellent property of
  not being on the internet.
