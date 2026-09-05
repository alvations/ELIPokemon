---
id: "004"
slug: encoder-decoder-vs-decoder-only
style: pokemon
category: transformers
difficulty: core
question: "What is the difference between encoder-only, decoder-only, and encoder-decoder architectures?"
tags: [bert, gpt, t5, architecture, causal-mask]
---

# Three kinds of Trainer

Same Garchomp, same Earthquake, same stadium. What changes is **what each Trainer is allowed to
look at**, and that single rule decides what job they can hold.

```
  🔍 THE JUDGE            ⚔️ THE BATTLER          🌐 THE INTERPRETER
  (encoder-only)          (decoder-only)          (encoder-decoder)

  Sees the whole team,    Sees only Pokémon        Studies the enemy's
  front and back, all     already sent out.        full team first, then
  at once.                                         battles it turn by turn.

  ┌───────────────┐       ┌───────────────┐        ┌────────────────┐
  │ 1 2 3 4 5 6   │       │ 1 2 ▓ ▓ ▓ ▓   │        │ READ the roster │
  │ ✓ ✓ ✓ ✓ ✓ ✓   │       │ ✓ ✓ ░ ░ ░ ░   │        └───────┬────────┘
  └───────────────┘       │ (▓ = not out) │                ▼
                          └───────────────┘        ┌────────────────┐
  Job: rate the team      Job: fight, turn         │ FIGHT it, turn │
  Cannot fight — it       by turn, forever         │ by turn        │
  never takes a turn                               └────────────────┘
```

## 🔍 The Judge — encoder-only

The Judge gets the **full team sheet** before anything happens. Slot 6 informs their read of
slot 1 just as much as the other way round. That total view makes them the best in the world
at answering *"how strong is this team?"*, *"is this Rain or Trick Room?"*, *"how similar is this
team to that one?"*

Their training is a memory drill: someone covers **one** Pokémon on the sheet with their thumb
and the Judge names it from the rest of the team. Politoed, Kingdra, Ferrothorn, ?, Rotom,
Tapu Fini — that blank is Toxapex, and you knew it from the company it keeps. Do that a million
times and you develop an
uncanny sense for what belongs together.

But the Judge **cannot battle**. Their entire skill depends on seeing the finished sheet, and
a real battle is a sheet being written one Pokémon at a time. Ask them to lead with Garchomp and
they freeze:
their read of slot 1 depends on a slot 6 that doesn't exist yet.

Judges are your team raters, your matchmakers, your "find me another Rain team like this" search.

## ⚔️ The Battler — decoder-only

The Battler only sees what has actually been sent out. Turn 4 knows turns 1–4. It does not
know the ace in the back, because peeking would be cheating and, worse, would make every
practice match useless — you can't learn to predict a lead if you were shown it.

Training is dead simple and brutally effective: replay millions of battles, and at **every
single turn** ask *"what happens next?"* No thumb over the sheet, no 15%-of-the-team drill —
every turn of every battle is a graded exam question. That's why Battlers learn so much faster
from the same footage.

And it turns out *everything* is a battle. Rating a Politoed core? Battle it and see. Translating? Feed
the words in as opening turns and let it continue. Summarising? Same. One Trainer, every job.

This is why the modern world is full of Battlers.

## 🌐 The Interpreter — encoder-decoder

Two people in a trench coat. A **Judge in the back** studies the opposing roster completely
and takes notes; a **Battler in the front** fights, glancing at those notes every single turn.

That glancing is cross-attention, and it's genuinely the right shape when the input is fixed
and the output is new: translating a battle log, calling a match into a microphone, condensing
a six-hour Indigo Plateau run into a highlight reel. The thing you're reading never changes; the thing
you're producing grows.

The cost is that you're paying two salaries and coordinating two people — a Judge and a Battler who
have to agree on what they saw. Fine for a
translation booth. Overkill for "be good at everything".

## Why Battlers took over the League 🏆

* **Every turn is a lesson**, not one in seven.
* **Every job is a battle** if you squint, so you only need one Trainer.
* **One rulebook**, so scaling to a stadium of a thousand Pokémon is a manageable problem.
* **Show them a few example turns** and they adapt on the spot, with no retraining.
* **Their notes never go stale.** Because a Battler never revisits earlier turns, everything
  they wrote down about turn 1 is still valid on turn 400 — so they just keep the notebook
  instead of re-reading the whole log every turn. The Judge can't do this: change anything and
  their entire read shifts.

The Judges didn't retire. They just work as team raters and scouts now — jobs where seeing
everything at once is the whole point and nobody needs you to take a turn.
