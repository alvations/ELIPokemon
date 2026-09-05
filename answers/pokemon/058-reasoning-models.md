---
id: "058"
slug: reasoning-models
style: pokemon
category: reasoning
difficulty: advanced
question: "How are reasoning models trained, and how do they differ from chat models?"
tags: [reasoning-models, o1, r1, rlvr, thinking-tokens, distillation]
---

# Reasoning Trainers: the ones who pause before moving

Watch two Trainers in the same position — your Pikachu out against their Gyarados.

**😐 The chat Trainer** glances at the field and calls Thunderbolt. One second. Usually fine.

**🧘 The reasoning Trainer** stands there. Ten seconds. Twenty. You can see them working:

> *"Thunderbolt on Gyarados — 4× weak, should KO. But they've been holding that Gyarados back all
> match, which usually means a Sash. If it survives at 1 HP they get a free Dragon Dance and I lose.
> So: chip first. Quick Attack, break the Sash, then Thunderbolt next turn. Slower, but it can't go
> wrong."*

Then they move. And they're right far more often.

## How you raise one 🏋️

```
  ┌─ 🌾 a Pokémon out of the grass ────────────────────────────────┐
  │                                                                │
  ├─ 📝 SHOW IT A FEW HUNDRED WORKED EXAMPLES ────────────────────┤
  │   Just so its deliberation is READABLE. That's all this        │
  │   step is for.                                                 │
  │   (One team skipped it — and got a Trainer that reasoned       │
  │    brilliantly in an incomprehensible private shorthand,       │
  │    mixing three languages. Scored great. Unreadable.)          │
  │                                                                │
  ├─ 🎯 THE SCOREBOARD GRIND — this is the actual step ───────────┤
  │   Thousands of positions with a CHECKABLE outcome.             │
  │   Reward: did the move work? 1 or 0. Nothing else.             │
  │   No style marks. No judge. Just the scoreboard.               │
  │                                                                │
  ├─ 📚 KEEP ITS BEST GAMES, STUDY THOSE ────────────────────────┤
  │   Play thousands, keep the wins, train on them.                │
  │                                                                │
  ├─ 🤝 A FINAL POLISH so it's still pleasant to work with ──────┤
  └────────────────────────────────────────────────────────────────┘
```

## The part that should surprise you 🤯

**Nobody taught it to deliberate.**

Not one instruction said "think before you move" or "check for a Focus Sash" or "if unsure, back up
and reconsider." The only feedback, ever, was **did the move work.**

And what happened is that its turns got **longer on their own.** A few seconds at first. Then more.
Then it started catching itself mid-thought — *"wait, that's wrong, let me redo it"* — with nobody
having ever demonstrated that.

Because pausing won more battles. The scoreboard noticed. So it pauses.

## Two very different Trainers 📊

| | 😐 Chat Trainer | 🧘 Reasoning Trainer |
| --- | --- | --- |
| Trained on | what people *liked* | what actually **worked** |
| Turn length | a second | ten to a hundred seconds |
| Best at | conversation, writing, breadth | calculations, logic, planning |
| *"Think it through"* | helps | **redundant, sometimes harmful** |
| *"Here are 3 examples"* | helps | **often makes it worse** |
| Cost | baseline | 5–50× |

Those two middle rows are the practical ones, and people get them wrong constantly.

📌 **Don't coach a reasoning Trainer on how to think.** They already have a procedure, trained in
over thousands of battles, better than whatever you were about to suggest. Telling them to "consider
the type chart first" **interrupts** it.

Just state the position clearly and get out of the way.

## Teaching a rookie to deliberate 🐣

Beautiful result here.

Take a small, cheap Trainer. Show it thousands of a reasoning Trainer's **deliberations** — the full
"wait, they might have a Sash" monologues.

The rookie learns to deliberate too. And a small deliberating Trainer beats a much larger Trainer
that doesn't.

The counterintuitive bit: **watching someone deliberate works better than making the rookie figure
it out itself.** Put a small Trainer through the scoreboard grind alone and it mostly flounders — it
isn't strong enough to stumble onto good deliberation by accident. But it can absolutely *copy* it.

**Can't discover it. Can imitate it.**

## What they're bad at ⚠️

* 🎨 **Anything unscoreable.** They were raised on positions with a right answer — did the Gyarados
  faint, yes or no. *"Write a moving
  speech"* has no scoreboard, and the whole training method simply doesn't apply.
* 🐌 **Overthinking trivia.** Ask what type Pikachu is and they'll deliberate for thirty seconds
  before saying Electric.
  Cap it.
* 🔒 **You often can't see the deliberation.** Frequently hidden — and, per what we know about
  chains of thought, it wouldn't be a trustworthy account even if you could.
* 🐛 **They find bugs in the referee.** If the checker can be fooled, they will eventually fool it.
* 💸 **Expensive and slow.** Wrong for most of what you do.

**📌 So: route.** Cheap Trainer for the routine turns, reasoning Trainer for the ones that decide the
match, and something quick out front deciding which is which.
