---
id: "075"
slug: batch-norm-vs-layer-norm
style: pokemon
category: deep-learning
difficulty: intermediate
question: "How does batch normalization differ from layer normalization?"
tags: [batchnorm, layernorm, groupnorm, normalisation, batch-dependence]
---

# Two ways to run the Flat Rule

Both level the playing field the way VGC's Flat Rules do — everything to Level 50. The difference
is **what you compare against**, and that one choice decides everything else.

```
   🏟️ BATCH NORM                        🧍 LAYER NORM
   ─────────────                        ─────────────
   "Your Attack is scaled relative      "Your Attack is scaled relative
    to EVERYONE ELSE'S Attack            to YOUR OWN other five stats."
    in the tournament today."

   ┌────┬────┬────┬────┐                ┌────┬────┬────┬────┐
   │ ▓  │    │    │    │  ← compare     │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │ ← compare
   │ ▓  │    │    │    │    THIS        ├───────────────────┤   THIS ROW
   │ ▓  │    │    │    │    COLUMN      │ ░░░░░░░░░░░░░░░░░ │
   │ ▓  │    │    │    │                ├───────────────────┤
   └────┴────┴────┴────┘                │ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ │
                                        └───────────────────┘
   Your rating DEPENDS ON                Your rating depends on
   who else showed up.                   nothing but you.
```

## The consequence 🎯

**Batch norm** rates you against the room. Which is fine in a packed stadium and falls apart the
moment the room changes.

**Layer norm** rates you against yourself. Same answer whether you're in a stadium of a thousand or
standing alone in a field.

## Where batch norm hurts 😖

**🧍 You show up alone.** *"Your Garchomp's Attack is above average for today's tournament"* — and
you're the only entrant. Above average against whom, Magikarp? Above average compared to whom? It's meaningless, and this is exactly the situation
during a real one-on-one battle.

**📏 Your team sheets are different lengths.** Some Trainers brought six Pokémon, some brought two,
and the empty slots are being averaged into "today's average Attack." A Blissey and three blanks
is not a team; the statistics say otherwise.

**🔀 Practice and tournament work differently.** During training your Garchomp is scaled against
whoever's in the room — a Blissey one day, a Shuckle the next. On tournament day there's no room, so you fall back on **"the average across everyone I saw
during training."**

Two different rules, and the second is an approximation of the first. Forget to switch modes and
your ratings are quietly wrong — with **no error, no warning**, just worse performance.

**🌍 Everyone must agree on the average.** Run your tournament across Kanto, Johto and Hoenn and
every stadium needs to phone the others to compute today's average Attack. Every stat. Every round.

## Where layer norm just works ✅

None of the above. Your rating is computed from **your own six stats**, so:

* One Pokémon or a thousand — identical.
* Six on your team or two — identical.
* Practice or tournament — **identical**. No modes to switch.
* Five stadiums — no phone calls. Everyone computes their own.

📌 That's the whole reason modern language models use it. Variable-length inputs, tiny batches per
machine, and one-at-a-time generation — every single one of those breaks the "compare to the room"
approach.

## When batch norm is still right 🏟️

It hasn't lost everywhere. In a genuinely packed stadium with uniform entrants — a Level 50 Flat Rules
bracket where every Garchomp is built the same way — comparing to the room is **more
informative**, because "above average for
today" is real information that self-comparison can't give you.

Plus there's a bonus: because the room changes slightly every round, your rating jiggles a bit — and
that jiggling acts as **free anti-memorisation**, which layer norm doesn't provide.

## The rest of the family 👨‍👩‍👧

* 👥 **Group norm** — compare within small groups of related stats — the two offensive stats
  together, the two defensive ones together — rather than all six or all entrants.
  Room-independent, used where the crowd is too small to be a reliable reference.
* ✂️ **RMS norm** — layer norm with the paperwork trimmed. The current default.
* 🎯 **QK norm** — scale only the part where Pokémon size each other up, which stops a Garchomp's
  Attack from dominating the read before the turn even starts.
* 🎯 **QK norm** — apply it specifically to how Pokémon size each other up, which stabilises very
  large teams.

## What it's really for 🤔

The original story was "it stops the scale drifting between Gyms." That explanation hasn't held up
well.

The better account: **it makes training forgiving.**

Without it, you tiptoe — one wrong step and the numbers run away. With it, you can train *far* more
aggressively, because doubling a Pokémon's raw stats changes nothing (it gets scaled straight back)
and the whole system stops caring about the exact numbers you started with.

You can be sloppier and still finish the run. That's the real prize.
