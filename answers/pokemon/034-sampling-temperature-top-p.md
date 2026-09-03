---
id: "034"
slug: sampling-temperature-top-p
style: pokemon
category: inference
difficulty: core
question: "Explain temperature, top-k, and top-p (nucleus) sampling."
tags: [sampling, temperature, top-p, nucleus, min-p, decoding]
---

# Temperature, top-k, top-p: how boldly does your Pokémon play?

Your Pokémon has ranked its options for this turn:

```
   Thunderbolt   ████████████████████   64%
   Volt Switch   ███████                23%
   Protect       ███                     9%
   Tail Whip     █                       4%
```

Now — **how do you pick?** Always the top one? Roll the dice? That choice changes your Pokémon's
entire personality, costs nothing to change, and is the single most under-tuned dial there is.

## 🌡️ Temperature: how decisive is it?

Temperature squeezes or stretches the gaps between options.

```
  🧊 T = 0    "Thunderbolt. Always Thunderbolt."
              ████████████████████████████████████  100%
              Utterly predictable. Never surprises you. Never surprises
              the opponent either.

  ❄️ T = 0.5  ████████████████████████████  84%
              ████  11%
              Bold and focused. Occasionally mixes it up.

  🌤️ T = 1.0  ████████████████████  64%
              ███████  23%
              Exactly what it actually believes.

  🔥 T = 2.0  ████████████  42%
              ████████  26%
              ██████  16%
              Wild. Creative. Will Tail Whip a Gyarados for no reason.
```

Key detail: temperature **never changes the ranking**. Thunderbolt is still its favourite at every
setting. All that changes is how much of a favourite.

## 🔢 Top-k: only consider the best few

*"Only ever look at your top 3 options. Ignore the rest."*

Simple. And it has an obvious flaw — **3 is always 3**, but positions aren't:

* 🎯 **An obvious position:** Thunderbolt at 97%, everything else garbage. But you told it to
  consider three, so it's seriously weighing two moves it knows are bad.
* 🤔 **A genuinely tricky position:** eight moves all plausible around 12% each. You told it to
  consider three, so it just threw away five real options.

Fixed number, variable situation. Wrong tool.

## 🎯 Top-p: consider options until you've covered most of the plan

*"Go down your ranked list until you've accounted for 90% of your confidence. Stop there."*

```
   🎯 OBVIOUS POSITION                🤔 TRICKY POSITION
   Thunderbolt  97%  ← 97% ✓ stop     move A  15%   ┐
   (nothing else considered)          move B  14%   │
                                      move C  13%   │  keeps going...
   → considers 1 move.                move D  12%   │
     Correct! It's obvious.           move E  11%   │
                                      move F  10%   │
                                      move G   9%   ┘ ← 84%... 90% ✓ stop

                                      → considers 7 moves.
                                        Correct! It's genuinely unclear.
```

**Same setting, different behaviour, because the position is different.** That's what fixed top-k
can't do, and it's why top-p is the default.

## 😴 Why never just take the top move?

You'd think "always play your best move" is optimal. It isn't, and the failure is specific:

> Thunderbolt. Thunderbolt. Thunderbolt. Thunderbolt. Thunderbolt.

Always taking the locally-safest option produces **loops**. Real Champions play slightly
unexpectedly — not randomly, but not on rails either. Total predictability is its own weakness, and
it's how you end up watching a Magikarp Splash at a wall for forty turns.

## 📐 The newer dial: min-p

*"Consider any move at least a fifth as good as your favourite."*

Neat, because it scales with confidence automatically. Thunderbolt at 90%? Almost nothing else
clears the bar — good, it's obvious. Nothing above 15%? Lots of moves clear it — good, it's
genuinely open.

## 🎛️ Settings by situation

| What you're doing | Setting |
| --- | --- |
| 💻 Exact output, structured formats | `T = 0` — no creativity wanted |
| 📊 Factual questions | `T ≈ 0.2–0.5` |
| 💬 Normal conversation | `T ≈ 0.7`, `top_p 0.9` |
| 🎨 Creative work, brainstorming | `T ≈ 1.0`, `top_p 0.95` |
| 🗳️ Playing eight times and voting | `T ≈ 0.7` — you **need** variety, or all eight are identical |

## Two gotchas 📌

**Order matters.** Temperature is applied first, *then* the list is truncated. Change the order and
you get different behaviour.

**`T = 0` is not actually deterministic.** Ask the same question twice with temperature zero and
you can get different answers. Not a bug in your code — the underlying arithmetic runs in slightly
different orders depending on how many battles are running at once, and near-ties can flip. Never
promise anyone reproducibility on the strength of `T = 0`.
