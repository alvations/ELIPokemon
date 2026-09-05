---
id: "088"
slug: trees-forests-boosting
style: pokemon
category: classical-ml
difficulty: core
question: "Compare decision trees, random forests, and gradient boosting."
tags: [decision-trees, random-forest, xgboost, gbdt, tabular]
---

# One scout, a committee, or a relay team?

## 🌳 One scout: a flowchart

The simplest possible way to predict a battle. Just ask questions in order:

```
                  Faster than my Garchomp?
                   ╱                    ╲
                 yes                     no
                ╱                          ╲
        Hits hard?                  Holding Leftovers?
        ╱        ╲                    ╱           ╲
   ⚡ Jolteon   🏃 Ninjask      🛡️ Toxapex    🔄 Ferrothorn
```

✅ **You can read it.** Print it out, hand it to a kid on Route 1, they can follow it. Nothing else here has
that property.

❌ **It's wildly unstable.** Retrain on a slightly different set of battles and the root question
flips from Speed to typing — a **completely different flowchart** — different root question, different everything.

That instability sounds like a fatal flaw. It's actually the foundation of both methods below.

## 🌲 A committee: many scouts, voting

**Hire a hundred scouts. Let them all be individually unreliable. Take the vote.**

Two deliberate handicaps make this work:

1. 🎲 **Each scout watches a different random sample** of your battles.
2. 🙈 **Each scout is only allowed to consider a random few stats at each decision.**

That second one is the clever part, and it's easy to miss why it matters.

Without it, every scout would open with *"is it faster than me?"* — because Speed is the most useful
question, so **everyone** asks it first. A hundred scouts who all ask the same first question are
basically **one scout**, and voting achieves nothing.

Forcibly blind some of them to Speed and they're **forced to find other angles** — typing, held
item, whether it has Intimidate. Now they make
genuinely *different* mistakes — and different mistakes cancel out when you vote. Identical mistakes
don't.

📌 Let each scout be **deeply detailed and individually overconfident.** Voting washes out the
overconfidence. That's the whole design.

✅ **More scouts is never worse.** Ever. Add a thousand — it can only help.
✅ Barely any tuning. It just works.
❌ Usually a point or two behind the relay team.

## 🏃 A relay team: each fixing the last one's mistakes

Completely different idea. Instead of a hundred independent scouts, hire them **in sequence** — and
each new one only works on **what the previous ones got wrong.**

```
   🌲 COMMITTEE (all at once)          🏃 RELAY (one after another)

   ┌──┐ ┌──┐ ┌──┐ ┌──┐                 ┌──┐   ┌──┐   ┌──┐   ┌──┐
   │S1│ │S2│ │S3│ │S4│  independent    │S1│──►│S2│──►│S3│──►│S4│
   └──┘ └──┘ └──┘ └──┘                 └──┘   └──┘   └──┘   └──┘
        ╲  │  │  ╱                     whole  S1's   S2's   S3's
          VOTE                          job   misses misses misses

   Deep, detailed scouts.              SHALLOW scouts — each fixes
   Voting fixes their                  one narrow thing. Stacking
   overconfidence.                     them builds the full picture.

   ✅ more is always fine              ❌ too many WILL overfit —
                                          you must know when to stop
```

Scout 1 does a rough job. Scout 2 is told *"don't worry about what S1 got right — here are the twelve
battles it botched."* Scout 3 handles what's left. And so on.

Each is nearly useless alone. **Together they're the best tabular predictor there is.**

⚠️ **But you can go too far.** Scout 400 is "fixing" mistakes that were just noise — memorising
individual battles. You must watch a held-out set and **stop when it stops improving.** The committee
never needs this; the relay always does.

## Which do you use? 🎯

| | 🌳 One scout | 🌲 Committee | 🏃 Relay |
| --- | --- | --- | --- |
| Accuracy | poor | good | 🏆 **best** |
| Can you overdo it? | — | ❌ never | ✅ yes, easily |
| Tuning needed | none | little | **a lot** |
| Can you read it? | ✅ yes | ❌ no | ❌ no |
| Sensible default | rarely | ✅ **start here** | when it must be best |

## The thing worth knowing 🏆

For **battle statistics** — rows and columns of numbers, which is most real-world data — the relay
team is still, today, **the best there is.**

People keep trying to replace it with the big modern approaches. Benchmark after benchmark, the relay
team wins.

The reason is structural. Battle stats are **jumbled** — a Speed number, a typing, a Leftovers, a
win rate, all different kinds of thing, some of them useless. And the patterns are **jagged**: *"faster than 100 →
completely different strategy"* is a hard cliff, not a smooth slope.

Scouts asking yes/no questions handle cliffs and jumbled inputs naturally. The big modern approaches
are built for smooth, uniform data — images, text — and pay for that assumption here.

📌 **Faced with a spreadsheet of Speed tiers and win rates, reach for the relay team.** Reaching for
Cynthia instead usually costs you accuracy *and* effort.
