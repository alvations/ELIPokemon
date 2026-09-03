---
id: "073"
slug: backpropagation
style: pokemon
category: deep-learning
difficulty: core
question: "What is backpropagation?"
tags: [backprop, chain-rule, autodiff, computational-graph, reverse-mode]
---

# Backprop: tracing the loss back through the whole team

You lost the Championship. **Whose fault was it?**

Not a rhetorical question. You need an answer for **every single Pokémon, every move, every decision
you made all season** — and you need it before next week.

## The stupid way 🐌

Change one thing. Replay the entire season. See if you'd have won.

Then change the next thing. Replay the entire season again.

With ten thousand things you could have changed, that's **ten thousand replayed seasons.** You will
be dead before you finish.

## The clever way 🔙

**Start at the loss and walk backwards, once.**

```
   ➡️ FORWARD — how the season went
   Route 1 ──► Gym 1 ──► Gym 2 ──► ... ──► Champion ──► 💔 LOSS
      │          │         │                   │
   (note it)  (note it) (note it)          (note it)
   ↑ keep a record at every step — you'll need them

   ⬅️ BACKWARD — whose fault, working back
   "Route 1 ◄── "Gym 1  ◄── "Gym 2  ◄── "the final  ◄── 💔
    tutor's       taught      taught      Pokémon
    fault by      wrong       wrong       chose
    this much"    thing"      thing"      wrong"

   ONE walk backwards. Everyone's share of the blame, all at once.
```

At each step you only need two things: **the blame passed back from the step after**, and **the note
you took on the way forward.**

## Why backwards, and not forwards 🔑

This is the crux, and it's about a lopsidedness in the problem.

* Walk **forwards** and you'd ask *"if I changed this one thing, what happens to everything
  downstream?"* — and you'd have to do it **once per thing you could change.** Ten thousand walks.
* Walk **backwards** and you ask *"this one loss — who caused it?"* — and one walk answers it for
  **everything at once.**

You have **ten thousand decisions** and **one outcome.** So walk from the end with one outcome, not
from the start with ten thousand decisions.

📌 That lopsidedness is the entire reason any of this is possible. Flip it — one decision, ten
thousand outcomes — and you'd walk forwards instead.

## What it costs 💰

**⏱️ Time:** the walk back takes about **twice** the season itself, because at each stop you work out
two things: who to blame behind you, and what to change here. So a full round of learning is roughly
**three seasons' worth of effort** — one to play, two to review.

**📝 Memory — the big one:** you have to **keep every note you took on the way forward.** You can't
work out Gym 3's share of the blame without remembering what actually happened at Gym 3.

Long season, big team, detailed notes — the filing cabinet is enormous, and it's usually the thing
that limits how much you can train at once.

## Four ways it breaks 🚨

**⛓️ The blame fades to nothing.** A hundred Gyms back, the message has been divided so many times
it's a whisper. Route 1's tutor learns nothing. (Or the reverse — it amplifies each step and arrives
as a scream.)

**✏️ You overwrote your notes.** Tidied up your Gym 3 records to save space, and now you cannot
apportion Gym 3's blame. The good news is that most systems shout at you when you do this. Some
don't, and then you get **confidently wrong answers**, which is worse.

**✂️ You cut the chain.** Somewhere in the middle, someone wrote down a *summary* instead of keeping
the actual record. Blame reaches that point and stops. Everything before it gets nothing.

The symptom: **a Pokémon that never improves, no matter how much you train.** It isn't stubborn — no
feedback is reaching it.

**🎲 Some things you can't trace back.** *"I chose to switch"* is a decision, not a dial. There's no
"how much" to adjust — you either switched or you didn't. Choices like that break the chain, and you
need a different technique entirely (which is exactly why coaching-by-outcome exists — it's for the
decisions blame can't flow through).

## In one sentence 📌

> **Backprop is working out everybody's share of one loss by walking backwards through the season
> once, using the notes you took on the way forward — and it's cheap because there are thousands of
> things to fix and only one outcome to explain.**
