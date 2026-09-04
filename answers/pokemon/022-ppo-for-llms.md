---
id: "022"
slug: ppo-for-llms
style: pokemon
category: alignment
difficulty: advanced
question: "Explain PPO in the context of language model alignment."
tags: [ppo, policy-gradient, advantage, clipping, gae]
---

# PPO is coaching from the final scoreboard

Here's the setup. Your Garchomp plays a full 40-turn battle against a Toxapex stall team. At the
end, the judge says:

> **"6.2 out of 10."**

That's it. That's all the feedback. One number, for forty turns.

Now: *which turn was the good one?* 🤷

That question — the credit assignment problem — is what PPO exists to solve.

## The hard part 🎯

You cannot just tell your Pokémon "the battle scored 6.2, do more of that." Forty turns went into
6.2. Some were brilliant. Some were awful. They probably cancelled out.

The trick is to grade every turn against **what you expected**:

```
  Turn 12: Earthquake, winning comfortably. Expected outcome: 8.
           Actual outcome: 8.  →  that turn taught you nothing. 0 credit.

  Turn 13: stayed in on the Ferrothorn. Expected: 8.
           Actual: 3.  →  🚨 THAT was the disaster. Big negative credit.

  Turn 14: switched to Rotom, total mess. Expected: 3.
           Actual: 4.  →  Actually a good turn! Positive credit, despite
                           the position still being bad.
```

Turn 14 is the important one. It happened during a losing stretch and it was **good** — it made
things less bad than expected. Without the "what did we expect" baseline you'd punish it for
happening during a loss.

So you need a second Pokémon whose only job is **predicting how the match is going** at each
turn. Not to play — just to say "from here, we're looking at about a 6." That prediction is what
every turn gets measured against.

## The clip: don't overreact to one match 🛑

Here's the failure mode PPO is named for.

Your Garchomp uses Earthquake on turn 7. The match scores well. Naïve coaching says: *"Earthquake
is amazing — use it always, in every position, forever."*

One match. One data point. And you've just rewritten its entire personality.

The clip is a hard rule: **no single training round may change any habit by more than a set
amount.**

```
   how much you reward the change
        │
        │       ┌────────────  "that's enough. even if this match
        │     ╱ │               was spectacular, no more credit
        │   ╱   │               for shifting this habit further."
        │ ╱     │
        └─┼─────┼──────────────►  how much the habit has moved
        -ε      +ε
```

You still learn from the match. You just can't learn *everything* from it. Which means you can
safely re-study the same match several times over — squeezing full value out of one expensive
battle — without the third pass turning your Garchomp into an Earthquake fanatic.

That matters enormously, because **playing the matches is the expensive part**. Re-studying is
nearly free. The clip is what makes re-studying safe.

## The leash, applied every turn 🪢

The weirdness penalty from the photocopy isn't applied once at the end. It's applied to **every
single turn**:

> *"That turn scored well. But it was also a genuinely bizarre thing to do, so I'm docking you
> for that specifically."*

Per-turn feedback instead of one number at the end. Much easier to learn from — and it means
weirdness gets caught the moment it happens rather than being averaged into a final score.

## Why nobody enjoys running this 😩

* 🏋️ **Four Pokémon in the gym.** Trainee, photocopy, judge, and the match-predictor.
* ⏳ **Most of your time is spent playing matches**, not learning from them. You're running a
  tournament inside a training session.
* 🎛️ **Six dials, all interacting.** How tight the leash, how big the clip, how far ahead the
  predictor looks, how many times you re-study each match. Nudge one and the run either learns
  nothing or falls apart. There's no principled way to set them; it's lore.
* 🔮 **The match-predictor is genuinely hard to train.** "How will this go?" from a half-finished
  battle is a legitimately difficult question, and if it predicts badly, every turn gets graded
  against a bad baseline and the whole thing wobbles.

## The fix people found 💡

That last problem has an elegant solution: **stop predicting, start comparing.**

Instead of training a Pokémon to guess "this position is worth about a 6," just play the **same
position eight times** and see how they score. Average them. *That's* your expectation — measured,
not predicted.

Turn scored above the group average? Good turn. Below? Bad turn.

No predictor to train, no predictor to get wrong, one fewer Pokémon in the gym. This is GRPO, and
it's why modern reasoning models are trained that way — you replace a hard prediction problem
with a bit more battling, and battling is something you can just do more of.
