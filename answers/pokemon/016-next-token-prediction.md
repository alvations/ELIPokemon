---
id: "016"
slug: next-token-prediction
style: pokemon
category: fundamentals
difficulty: core
question: "How does next-token prediction produce something that looks like reasoning?"
tags: [autoregressive, language-modelling, compression, chain-of-thought]
---

# "Guess the next move" is the whole training regimen

Here's the entire curriculum. You show your apprentice a battle replay, pause it mid-turn, and
ask: **"what happens next?"**

That's it. Millions of replays, paused at every single turn.

It sounds far too simple to produce a Champion. It isn't, and here's why.

## To guess well, you have to actually understand 🧠

Look at what "guess the next move" quietly demands:

```
  "It's a Gym battle in Pewter City, the Leader sends out ___"
      → you must know the League. Facts.

  "Pikachu used Thunderbolt on Gyarados. It's super ___"
      → you must know the type chart. Rules.

  "Their Ferrothorn is at 12 HP and they have Leftovers, so next turn ___"
      → arithmetic and item effects.

  "They led Politoed, brought in Swift Swim Kingdra, and set up rain.
   Their win condition is ___"
      → you must have followed the *plan*. Strategy.

  "Three switches ago they preserved that Chansey at 4 HP for a reason.
   That reason was ___"
      → you must have been paying attention the entire match.
```

You cannot ace that last one by memorising common move sequences. Guessing the next move, *at a
high enough level*, requires modelling everything that produced the battle: the rules, the
Pokémon, the Trainer's intent, the whole plan.

Get good enough at "what happens next" and you have accidentally become a strategist.

## Why this beats every other training method 📚

Every replay is thousands of graded questions. A million replays is a *billion* practice
problems, covering every format, every metagame, every level of play — and you never had to pay
a coach to write a single one.

No other drill gives you that much feedback for that little effort. This is the real reason it
won.

## Thinking out loud is not a trick 🗣️

Important mechanical fact: your Trainer gets **exactly the same amount of thinking time per
move**, whether the move is "use Splash" or "solve this six-way endgame."

So for a hard position, one move's worth of thought isn't enough. The fix is to let them **narrate
to themselves**:

> *"Okay. Their Ferrothorn resists my Water. But it's weak to Fire. My Charizard is in the back.
> If I switch now I eat a Power Whip — but Charizard survives that at 30%. Then I threaten. Switch."*

Every sentence is another move's worth of thinking, and they can **read their own notes back**.
They've converted "I only get one moment of thought" into "I can take as many moments as I write
down."

That's all chain-of-thought is. Not a magic phrase — a way of buying more thinking time by using
the battle log as scratch paper.

## What this training can't give you ⚠️

**No take-backs.** A move, once made, is made. Your Trainer commits to turn 4 before considering
turn 5. Any backtracking has to be done *out loud*, in the log, before committing.

**Practice ≠ tournament.** In training, every replay showed them what a *strong* Trainer did
next, so they never had to recover from their own mistakes. In a real match they're standing in
positions of their own creation, and one bad turn compounds into three.

**They learned to predict, not to be right.** The drill rewarded guessing what a Trainer *would*
do. Trainers make confident mistakes all the time. So your apprentice learned to sound confident
too — including when confidently wrong. Nobody ever graded them on *truth*.

**One speed for everything.** Same thinking time for a trivial turn and a match-deciding one,
unless you explicitly teach them to slow down.

## Which is why the grind isn't the end 🎓

The replay drill builds a Trainer who knows **everything** and behaves like **nobody in
particular** — they'll happily continue a bad Trainer's bad plan, because that's what the replay
would do next.

Turning that into someone who is actually *helpful*, who says "I don't know," who follows your
instructions instead of predicting what a random Trainer would do — that's coaching, and it comes
after. The knowledge is from the grind. The behaviour is not.
