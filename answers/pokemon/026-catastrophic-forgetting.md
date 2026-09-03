---
id: "026"
slug: catastrophic-forgetting
style: pokemon
category: training
difficulty: intermediate
question: "What is catastrophic forgetting and how do you mitigate it?"
tags: [catastrophic-forgetting, continual-learning, ewc, replay, alignment-tax]
---

# Catastrophic forgetting is the four-move limit

Your Pokémon knows four moves. That's the cap. Learn a fifth and something has to go.

Now imagine a version where the game **never asks**. You send your Charizard to Dragon-type
specialist camp for a month, and it comes back with Dragon Claw, Dragon Dance, Dragon Tail and
Outrage — and it has silently forgotten **Flamethrower**.

```
   accuracy
       │ ████████████████╗   great at Fire battles
  🔥   │                 ╚═════╗
       │                       ╚═══════════════════  ← gone
       │
  🌊   │                    ╔══════════════════════
       │ ───────────────────╝
       └────────────────────┬──────────────────────►
                   sent to Dragon camp
```

It is now a mediocre Dragon impersonator that used to be an excellent Fire Pokémon.

## What this looks like in practice 😨

This isn't hypothetical. It's the standard outcome of sending a well-raised Pokémon to a
specialist camp.

You send your beautifully-trained, obedient, sporting Champion to **Rock-type camp**. Four weeks
later it comes back:

* 🪨 Fantastic at Rock battles. Genuinely. Camp worked.
* 😐 ...but it stopped listening to instructions.
* 😬 ...and it kicks fainted Pokémon again.
* 🤨 ...and it has no idea what to do against a Water-type any more.

You got your specialist. You lost your Champion. That trade — becoming a specialist by ceasing to
be well-rounded — is the tax on every specialist camp.

## How to stop it 🛡️

**1. 🥪 Keep the old moves in rotation.** The simplest and most effective fix. While at Rock camp,
spend a fifth of every day on ordinary Fire drills and basic obedience. Cheap, boring, works.
This is what essentially everyone does.

**2. 🧩 Don't retrain — bolt on.** Instead of altering your Pokémon, give it a **held item** that
grants Rock expertise. The Pokémon underneath is *completely untouched*. Take the item off and
your Champion is exactly as it was, to the last detail.

Nothing can be forgotten if nothing was overwritten. This is why bolt-on training is the default
for specialisation.

**3. 🐌 Train gently, and stop early.** Most forgetting is just overtraining. A month of brutal
twelve-hour days at Rock camp will wipe your Pokémon. Three light days will teach it Rock Slide
and leave everything else intact. When someone says "it forgot everything," they almost always
mean "I trained way too hard for way too long."

**4. 🔒 Protect the load-bearing moves.** Go in knowing that Flamethrower is what makes this
Pokémon special, and explicitly guard it. The sophisticated version works out **which** moves
matter most and clamps those hardest, while letting the unimportant ones drift freely.

**5. 🎒 Keep separate Pokémon.** One for Rock, one for Fire, and switch. No interference, because
nothing is shared.

**6. 📖 Don't train at all — hand it a guidebook.** Very often the right answer. If what you need
is *"know the local Gym's roster,"* don't send your Pokémon to camp. Hand it a scouting report at
the door. Nothing is forgotten, the report updates in seconds, and you can check where the
information came from.

## The trap 🕳️

Here's how teams actually get burned.

You're at Rock camp. Your dashboard tracks **Rock battle win rate**, and it's climbing
beautifully. Week one: 60%. Week two: 75%. Week three: 88%. Everyone's thrilled.

Nobody is measuring anything else.

Then you enter a real tournament and discover your Pokémon can't handle a Water-type, ignores
your instructions, and plays dirty.

📌 **Always keep testing the things you are not training.** Run the general drills. Check
obedience. Check sportsmanship. If the only number you watch is the one you're optimising, you
will never see what it cost you — right up until the tournament, where you find out all at once.
