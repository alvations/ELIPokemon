---
id: "006"
slug: residual-connections
style: pokemon
category: deep-learning
difficulty: core
question: "Why do residual (skip) connections matter in deep networks?"
tags: [resnet, residual, gradient-flow, identity]
---

# Residual connections are the "keep your moves" rule

Here's a nightmare version of the games. Every time your Pokémon levels up, it **forgets its
entire moveset** and learns four brand-new moves from scratch.

Level 20 Charmeleon: Ember, Growl, Smokescreen, Dragon Rage. Nice.
Level 21: all four gone, replaced by whatever the game rolls.

Now train to Level 100. You'd have a *worse* Pokémon than the Level 20 one, because you rolled
the dice eighty more times and every roll wiped the good stuff. That is a plain deep network,
and it's exactly the embarrassment that started all this: the 56-layer network was worse than
the 20-layer one **on the training data**. Not overfitting. It just couldn't hold onto anything.

## The actual rule: you keep what you have

Real Pokémon level-ups say: *"Charmeleon wants to learn Flamethrower. Forget a move?"* — and
you can say **no**. Your Pokémon carries everything it had, plus whatever it just picked up.

```
  ❌ THE NIGHTMARE                      ✅ THE REAL RULE

  Lv20: [Ember][Growl][Smoke][Rage]     Lv20: [Ember][Growl][Smoke][Rage]
           ↓ wipe, reroll                        ↓ + Flamethrower
  Lv21: [Tackle][Leer][Sand][Bite]      Lv21: [Ember][Growl][Smoke][Rage]
           ↓ wipe, reroll                       +[Flamethrower]
  Lv22: [Growl][Growl][Leer][Tackle]             ↓ + Slash
           ↓ ...                        Lv22: everything above +[Slash]
  Lv100: whatever the last roll gave              ↓ ...
         (probably garbage)             Lv100: every good move it ever learned
```

A level-up that has nothing to offer is now **free**. Decline the move, walk away unchanged.
Ninety useless levels cost you time, not power. In the nightmare version, ninety useless levels
destroy the Pokémon.

## Why the Champion's advice reaches your starter 📣

Training feedback flows backward: the Champion tells the Elite Four what went wrong, they tell
the Gym Leaders, and eventually it should reach the Route 1 tutor who first taught your
Charmander to Scratch.

In the nightmare version that message goes through a hundred rerolls. Each one garbles it a
little. By Route 1 it's noise, and your starter never improves — which means your whole team is
built on a foundation nobody can fix.

With the keep-your-moves rule, there's a **direct line**. Ember is *still in the moveset* at
Level 100, so "your Ember is what lost us the match" travels straight back to the tutor who
taught it, at full volume. Every layer of the journey stays trainable.

## The moveset as a shared notice board 📋

Here's the better way to picture a deep model. Your Pokémon carries one big **notice board**
through the whole journey. Every Gym reads the board, thinks, and **pins something new to it**.
Nobody tears anything down.

* 🥊 Gym 3 pins: *"this thing is Water-type."*
* 🧠 Gym 17 reads that note and pins: *"...so it's probably running Rain."*
* 🎯 Gym 40 reads both and pins the counterplay.

Gym 40 can still read what Gym 3 wrote, forty Gyms later, because nothing was overwritten. That
is the entire reason a very deep team works: information *accumulates* instead of being
relayed through a hundred rounds of telephone.

## The two catches ⚠️

**The board fills up.** A hundred Gyms all pinning notes and the board gets crowded — late
notes are lost in the pile. Fix: tell each Gym to pin smaller notes.

**Some Gyms need an adapter.** If a Gym hands you a note in a totally different format, you
need a translator before it can go on the board. Slightly breaks the "carry it forward
untouched" guarantee, but it's a small tax.

Neither is close to as bad as the alternative. The reroll nightmare is a Pokémon that can never
be more than one level up.
