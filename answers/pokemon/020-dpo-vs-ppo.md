---
id: "020"
slug: dpo-vs-ppo
style: pokemon
category: alignment
difficulty: advanced
question: "What is DPO and how does it differ from PPO-based RLHF?"
tags: [dpo, ppo, rlhf, bradley-terry, preference-optimisation]
---

# DPO: fire the judge, keep the verdicts

The old way needed **four Pokémon in the gym at once**: the trainee, a frozen photocopy, a judge,
and a fourth just tracking how it's going. Then an endless loop of battle → grade → nudge.

Expensive. Fiddly. Breaks constantly.

Then someone noticed something.

## The realisation 💡

You have a stack of comparison cards. *"Their Gyarados is out against your Ferrothorn:
**Thunder Wave** beat **Power Whip**."*

The old process was: train a judge on those cards → have the judge grade fresh battles → nudge
the Pokémon toward higher grades.

But work backwards. What does the *finished* Pokémon look like? It's whatever behaves such that
its preferences match the cards. And if that's the destination, why go via the judge at all?

> **A Ferrothorn that already reaches for Thunder Wave over Power Whip IS the judge.**

There is no separate judge to hire. There never was. The judge was a middleman for information
that was already sitting in the comparison cards.

## What training looks like now 📇

```
   OLD (PPO)                             NEW (DPO)
   ─────────                             ─────────
   1. train a judge on the cards         1. read a card
   2. send Ferrothorn out                2. "make Thunder Wave more
   3. let it battle                          likely than Power Whip —
   4. judge grades the battle                but don't drift too far
   5. nudge toward the grade                 from the photocopy"
   6. repeat, forever                    3. next card

   4 Pokémon in the gym                  2 Pokémon in the gym
   battles required every step           no battling at all
   notoriously hard to get right         about as hard as obedience school
```

You go straight from the card to the adjustment. No judge. No battles during training. The
photocopy is still there — you still need "don't get weird" — but everything else is gone.

## Why this isn't strictly better ⚖️

Here is the catch, and it's the whole interview question.

The old way had your Pokémon **actually battling**. It would try something nobody had ever put on
a card, get graded on it, and learn. It could discover turns that weren't in anyone's collection.

The new way only ever studies cards. And here's the problem: those cards were written about
turns that some *earlier, worse* Pokémon played.

Three weeks in, your Pokémon has moved well past that. It's now in positions no card describes,
considering turns nobody ever compared. The cards are still teaching it, but they're teaching it
about a Pokémon it no longer is.

## The specific way it fails 🎭

DPO reliably teaches "don't do turn A." Genuinely good at that.

What it's oddly bad at is teaching "do Thunder Wave." It often makes Thunder Wave *less* likely
too — it just makes Power Whip less likely faster. Push down hard enough on the rejected move and
the probability has to go somewhere, and it frequently lands on **Leech Seed**, which nobody ever
compared against anything.

Your Ferrothorn has learned what not to do, and filled the gap with something untested.

## The variants 🧬

* 🎯 **IPO** — stops it from over-committing when every card agrees.
* 👍👎 **KTO** — needs only "that turn was good" / "that turn was bad," no pairs at all. Vastly
  easier to collect.
* 🪢 **ORPO** — folds the comparison training into obedience school, so it's one stage.
* ✂️ **SimPO** — throws away the photocopy too, and normalises for turn length so it stops
  rewarding padding.
* 🔁 **Iterative DPO** — the one people actually run. Train on cards, then **have the new Pokémon
  play and write fresh cards about its own turns**, and repeat.

That last one is the real answer. It recovers most of what made the old way powerful — cards
about *this* Pokémon's actual behaviour — without ever hiring a judge.

## The verdict 🏆

For a small gym: **fire the judge**. Simple, cheap, works, roughly as hard as obedience school.

At Championship level: the top Leagues still run the full four-Pokémon setup, because being able
to explore genuinely new turns is worth the expense when you're chasing the last few percent.

And nearly everyone — small gym and Championship alike — regenerates their cards periodically.
Studying a two-year-old card collection is how you train an excellent Pokémon for last season's
metagame.
