---
id: "067"
slug: dropout
style: pokemon
category: deep-learning
difficulty: core
question: "How does dropout work, and why does it behave differently at train and test time?"
tags: [dropout, regularisation, ensemble, inverted-dropout, co-adaptation]
---

# Dropout: bench half the team, at random, every practice

Every practice session, you flip a coin for each Pokémon on the belt — Charizard, Blastoise,
Garchomp, Ferrothorn, Toxapex, Gyarados. Heads, they play. Tails, **they sit out.**

Every session. Randomly. All the way through training.

Then on tournament day: **everybody plays.**

```
   🏋️ PRACTICE (coin flip each)          🏆 TOURNAMENT
   ──────────────────────────            ─────────────
     ✅──✅──✅                            ✅──✅──✅
      ╲ ╱ ╲ ╱                              ╲ ╱ ╲ ╱
     🪑  ✅  🪑   ⬅ benched today          ✅  ✅  ✅   ⬅ everyone
      ╱ ╲ ╱ ╲                              ╱ ╲ ╱ ╲
     ✅  🪑  ✅                            ✅  ✅  ✅

   a different half-team every            the full team,
   single session                          every time
```

## Why cripple your own practice? 🤔

**1. 🤝 It breaks the co-dependency.**

Left alone, your team develops fragile habits. Charizard learns *"Blastoise always handles Brock's
Onix, so I never need to worry about Rock types."* Efficient! And it collapses completely the moment
Blastoise is unavailable.

Bench Blastoise at random and Charizard can't build that habit. **Nobody can rely on anybody**, so
every Pokémon has to become independently useful.

Less elegant, far more robust.

**2. 👥 You're secretly training thousands of teams.**

Every practice is a different half-team. Over a season you've trained an enormous number of
different lineups — all sharing the same Pokémon.

On tournament day, playing everyone at once is roughly **all those lineups voting**. You get the
robustness of many teams for the price of one.

## The bit that trips everyone up 📏

Here's the subtle problem.

In practice, each Pokémon receives support from **half** the team. On tournament day, suddenly the
**whole** team is backing them up — twice the support they've ever experienced.

That's a genuine shock. Everything is louder than they trained for, and their reads are miscalibrated.

**The fix: during practice, count the support from whoever's on the field as double.**

Half the team, counted double, equals the full team. So practice *feels* like a tournament, and on
tournament day nothing changes — everybody plays, everything counts normally, done.

📌 **This is why you must tell your team which mode they're in.** Forget to flip the switch to
tournament mode and your Pokémon keep benching each other at random, mid-match, in front of a crowd.

And the ugly part: **nothing errors.** No alarm, no crash. Your Pokémon just plays noticeably worse
than it should, forever, and you have no idea why. One of the most common and most maddening
mistakes there is.

## Using it 🎛️

* 🎲 **How often to bench?** Half is classic for a big loose squad. Much less — one in ten — for
  tightly-drilled modern teams.
* 🚫 **Never bench your final decision-maker.** Someone has to actually call the Thunderbolt.
* ⚔️ **It fights with other methods.** Some other training techniques work by measuring the team's
  typical performance — and random benching makes those measurements wrong. Pick one.
* 🐘 **Big modern teams often skip it entirely.**

  Because benching exists to stop **memorisation** — and if your Pokémon sees a million different
  opponents and never the same one twice, there's nothing to memorise. Benching just slows training
  down for no benefit.

  It comes straight back when you're specialising on a small set of opponents, where memorisation is
  a real risk again.

## One clever reuse 🔮

Keep the coin-flipping **on** during a real match against Cynthia. Run the same turn five times
with five different half-teams.

* ✅ All five agree → your team genuinely knows this position.
* ❌ Five different answers → **they're guessing**, whatever they claim.

A free uncertainty check out of a training trick.
