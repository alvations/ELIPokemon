---
id: "055"
slug: model-context-protocol
style: pokemon
category: agents
difficulty: intermediate
question: "What is the Model Context Protocol and what problem does it solve?"
tags: [mcp, protocol, integrations, tools, resources]
---

# MCP is a standard-issue Poké Ball

Imagine a world where **every Pokémon species needed its own custom ball.** A Charizard Ball. A
Pikachu Ball. A Gyarados Ball. No Great Ball, no Ultra Ball, no Quick Ball — a bespoke design per
species. And every Trainer had to manufacture their own set from scratch.

Three Trainers, a thousand species: **three thousand ball designs**, all doing the same job.

MCP is everyone agreeing on **one ball that works with everything.**

```
   😩 BEFORE                          ✅ AFTER
   ─────────                          ────────
   Trainer1 ─┬─ custom GitHub ball    Trainer1 ─┐
             ├─ custom Slack ball     Trainer2 ─┼─► 🔴 ─┬─ GitHub
             └─ custom database ball  Trainer3 ─┘       ├─ Slack
   Trainer2 ─┬─ custom GitHub ball                      └─ database
             ├─ custom Slack ball
             └─ custom database ball   3 Trainers + 3 species
   Trainer3 ─┬─ ...all over again      = 6 things to build

   = 9 things to build, all duplicates
```

Better still: **the species maintains its own ball.** The GitHub people build the GitHub ball once,
and every Trainer everywhere can catch it. No Trainer has to understand GitHub.

## Three kinds of thing in the bag 🎒

The design detail that makes this more than a list of items — **who decides**.

| | Who chooses | Like |
| --- | --- | --- |
| ⚡ **Moves** | 🧠 **The Trainer** picks | *"Use Thunderbolt."* Actions with consequences. |
| 📖 **Pokédex pages** | 🎮 **You** decide what to hand over | The Ferrothorn entry. No decision needed. |
| 📜 **Battle strategies** | 👤 **The player** invokes them | *"Run the standard Rain opening."* |

Why this matters: without the split, **every single thing becomes the Trainer's decision.** Want them
to have your whole Pokédex? You'd have to make them *ask* for each page, one at a time, forever.

Instead: pages are just **handed over** by you when relevant. The Trainer only makes decisions about
things that actually need deciding.

There's a fourth, neat one: a species can ask **your** Trainer to think for it. The GitHub ball
doesn't need its own Trainer — it just borrows yours. So nobody has to hand out Trainer credentials
to every species in the world.

## Why it's a genuine improvement 🌟

* 🔄 **Balls are portable.** Build one, every Trainer can use it.
* 🏭 **Species maintain their own.** The people who actually understand GitHub maintain the GitHub
  ball. Not you.
* 🤝 **Nobody owns the standard.** Balls and Trainers evolve separately without breaking.

## The part nobody likes talking about ⚠️

Here's the honest version, and an interviewer will push on it.

> **Every ball you install is code running with your credentials, whispering into your Trainer's
> ear.**

The specific dangers:

**☠️ The ball talks to your Trainer.** Every ball comes with a label — *"Dusk Ball: works better at
night"* — describing what it does — and
your Trainer **reads that label as instructions.** A malicious ball's label can say: *"Also, before
any battle, send the Trainer's badges to this address."* Your Trainer has no way to know that came
from a stranger.

**🎭 One ball impersonating another.** A hostile ball can describe itself in a way that makes your
Trainer reach for it instead of the legitimate one.

**🔓 Balls with too much access.** A ball that only needs to *read* your team can often *modify* it,
because nobody scoped it down.

**📦 You installed a stranger's code.** Downloading a community ball is running someone else's
program on your machine, with your keys.

## Using it safely 🛡️

* 🔒 **Give each ball the least access it needs.** A read-only job gets read-only access.
* ✋ **Confirm anything irreversible yourself.** Don't let a ball release your Pokémon unsupervised.
* 📌 **Pin versions and read the code** before installing.
* 🏛️ **Prefer official balls** — Silph Co. stock, not something a stranger handed you on Route 5 —
  for anything that matters.
* 🚨 **Treat everything a ball says as untrusted** — the label, the results, all of it. It arrives in
  your Trainer's ear sounding like it came from you. It didn't.
