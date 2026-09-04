---
id: "017"
slug: teacher-forcing-exposure-bias
style: pokemon
category: training
difficulty: intermediate
question: "What are teacher forcing and exposure bias?"
tags: [teacher-forcing, exposure-bias, scheduled-sampling, error-compounding]
---

# Training with the Champion's replays vs actually playing

Your apprentice studies exclusively by watching **Cynthia's replays**, paused every turn:
*"what does she do here?"*

They guess "Thunderbolt." Wrong — she switched to Spiritomb. You correct them, **rewind to the
Champion's actual position**, and continue.

Note what just happened: no matter how badly they guessed, turn 5 starts from the *Champion's*
turn-4 position. They are always standing in a good spot.

## Why coaches do this ⏩

Because you can grade **every turn of a 40-turn replay simultaneously**. Every position is already
known — it's on the tape — so you don't have to play the match out to check turn 30.

If you instead made them *play* every practice match, you'd sit through the whole thing turn by
turn, and training would take a thousand times longer. Nobody would ever finish a season.

## Then they enter a real tournament 😬

```
  📼 STUDYING REPLAYS                    ⚔️ ACTUAL TOURNAMENT
  ──────────────────                     ────────────────────

  Turn 4: they guess wrong.              Turn 4: they play wrong.
          ↓ REWIND                               ↓ no rewind. it happened.
  Turn 5: from the CHAMPION's             Turn 5: from THEIR OWN mess.
          perfect position.

  Every turn is a fresh start            Every turn inherits every
  from a position a Champion             mistake they've made so far.
  actually reached.
```

They have **never in their life** stood in a losing position of their own making. Every practice
turn began from a spot a Champion had engineered.

So the first time they misplay, they're somewhere genuinely unfamiliar — and because it's
unfamiliar, they misplay *again*. Three turns later the match is unrecognisable.

## What this looks like from the stands 👀

* 🔁 **Loops.** They switch Pikachu in, switch it out, switch it in, switch it out — burning
  Stealth Rock damage every time. Each move
  looked locally fine; the sequence is nonsense.
* 🌀 **Drift.** Twenty turns in, they're playing Trick Room on a team that never had Bronzong.
* 🎭 **Committing to a fiction.** They misidentify the opponent's Ferrothorn as a Skarmory on
  turn 3, and then play *ten flawless turns* against a Skarmory that does not exist. Every
  individual decision is correct given the premise. The premise was theirs.

That last one is the important one. The mistake isn't the ten turns — it's turn 3. But nothing in
their training ever taught them to notice they were in a made-up match.

## Fixes people tried 🔧

* 🎲 **Occasionally don't rewind.** Sometimes let them keep playing from their own bad position.
  Helps! Also throws away the speed that made replay-study viable in the first place.
* 🏟️ **Just make them play real matches, graded on the final result.** Correct in principle,
  agonisingly slow, and hugely unstable — losing tells you *something* went wrong across forty
  turns, not what.

## What actually worked 🏆

The modern answer: **after the replay study, put them in real matches and coach them on their own
games.**

They play. They reach their own bad positions. They get feedback *from there*. That's exactly the
gap the replays left, and closing it is a large part of why post-training coaching works — not
only because it teaches manners, but because it's the first time the apprentice has ever had to
dig themselves out of a hole they dug.

Worth noting: this problem hurt small apprentices far more than modern ones. A Trainer who's
simply *right more often* reaches bad positions less often to begin with. Scale doesn't remove
the flaw — it just means you hit it later.
