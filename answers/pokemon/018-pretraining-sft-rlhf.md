---
id: "018"
slug: pretraining-sft-rlhf
style: pokemon
category: training
difficulty: core
question: "What is the difference between pretraining, supervised fine-tuning, and RLHF?"
tags: [pretraining, sft, rlhf, post-training, alignment]
---

# The three stages of raising a Champion

## 🌾 Stage 1: The wild grass — pretraining

You release your Pokémon into the tall grass for **months**. It fights everything. Rattata,
Zubat, the occasional Snorlax. Nobody instructs it. Nobody grades it. It just... encounters
everything there is to encounter.

What it becomes: a creature that has **seen it all**. Knows every type matchup, every terrain,
every weather condition, every species in existence.

What it is *not*: yours. Say "use Thunderbolt" and it looks at you and does whatever wild
Pokémon do. It's not disobedient — it has genuinely never been told that a human saying words is
a thing that should affect its behaviour.

Ask it a question and it'll continue the *pattern* of questions:

> **You:** "What's super effective against Water?"
> **It:** "What's super effective against Fire? What's super effective against Grass? What's..."

It's not being difficult. In the grass, that's what a list of questions does — it continues.

This stage costs almost everything. Months, the entire budget, all of it.

## 🎓 Stage 2: Obedience school — SFT

Now a **week** with a trainer holding a clipboard of worked examples.

> *"When the Trainer says 'Thunderbolt', you use Thunderbolt. Watch — like this. Again."*

A few thousand demonstrations of the right behaviour, and something clicks. It's not smarter — it
learned nothing new about type matchups in that week. But it now understands that **it has a
Trainer**, that instructions are for following, and roughly what a good response looks like.

This is the cheapest, highest-leverage week of the whole process. All that wild knowledge finally
becomes *reachable*.

## 🏅 Stage 3: The coach — RLHF

Obedient isn't the same as good.

Your Pokémon now follows orders. But it's blunt. It over-explains. It attacks when it should
switch. It occasionally does something genuinely reckless because nobody ever told it not to.

So: **show it pairs and let it learn which is better.**

> *"Here are two ways that turn could have gone. This one's better. Why? Fewer wasted moves, kept
> your win condition alive, and it didn't KO its own teammate."*

```
  📋 DEMONSTRATION (stage 2)          ⚖️ COMPARISON (stage 3)
  ─────────────────────────           ──────────────────────
  "Here is the perfect turn.          "Here are two turns.
   Copy it."                           The left one is better."

  Expensive — a coach must            Cheap — anyone decent can
  invent the perfect play.            *judge* two plays even if
                                      they couldn't invent either.

  Says nothing about what             Directly teaches the whole
  makes a play bad.                   space of worse options.
```

That asymmetry is the entire argument for stage 3. **Judging is easier than performing.** A
club-level coach who could never out-play the Champion can still reliably tell you which of two
turns was better — and that judgement is enough to make a Champion.

## The rule that catches everyone out 📌

> **The grass gives knowledge. The coaching gives behaviour.**

You cannot coach in a fact that was never in the grass.

Try to teach a new Pokémon species during obedience school and here's what actually happens: your
Pokémon doesn't learn the species. It learns that **when asked about unfamiliar species, one
answers confidently.** You wanted knowledge; you installed a *bluffing habit*.

This is the single most common expensive mistake. New facts belong in the grass. Coaching is for
shaping what's already in there.

## In practice it's messier 🔀

Modern Leagues blur the stages: they sprinkle high-quality opponents into the last weeks of the
grass, they let the Pokémon generate its own practice drills and keep the good ones, and for
anything with a *checkable* answer — did the move actually KO? — they skip the human coach and
just use the scoreboard.

The three-stage picture is still the right mental model, and still what you'll be asked about.
