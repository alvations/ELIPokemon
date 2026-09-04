---
id: "089"
slug: bagging-vs-boosting
style: pokemon
category: classical-ml
difficulty: core
question: "What is the difference between bagging and boosting?"
tags: [bagging, boosting, ensembles, variance, bias, stacking]
---

# Bagging vs boosting: two ways to build a team

Both combine many weak members into something strong. They're solving **opposite problems**, and
everything else follows from that.

```
   🌲 BAGGING — all at once            🏃 BOOSTING — one after another

   footage ─┬─ sample ─► [🎪 wild] ─┐  footage ─► [🪨 basic] ─► what it missed
            ├─ sample ─► [🎪 wild] ─┤               │
            ├─ sample ─► [🎪 wild] ─┼─► VOTE        └─► [🪨 basic] ─► what THAT
            └─ sample ─► [🎪 wild] ─┘                       │        missed
                                                           └─► [🪨 basic] ─► ...
   Members: brilliant but erratic.
   Voting cancels the erraticism.      Members: reliable but limited.
                                        Stacking covers the limitations.
```

## 🌲 Bagging: cure the erratic

Your problem: **wildly inconsistent** scouts. Each one is brilliant on the battles it saw and lost on
anything new.

Hire a hundred of them, show each a different slice, and **vote.**

One scout is superstitious about red hats. Another thinks every Gyarados runs Dragon Dance. A third
believes Ferrothorn always carries Leftovers. All different superstitions — so when they vote,
**the superstitions cancel** and the real signal comes through.

📌 **You want them individually wild.** Hire cautious, sensible scouts and the voting achieves
nothing — you needed their errors to be *different*, and cautious people all make the *same* errors.

📌 **The trick is making them differ, not adding more.** A thousand scouts who all think alike is one
scout in an expensive hat. That's why you deliberately blind each of them to different information.

✅ **You cannot overdo it.** More scouts is never worse. Add a thousand.
✅ **Robust to bad footage.** One mislabelled match is one vote among a hundred. Ignored.

## 🏃 Boosting: cure the limited

Your problem is the opposite: your scouts are **too simple.** Perfectly consistent, and only capable
of noticing one thing.

So chain them. Each new scout is handed **only the battles the previous ones got wrong.**

```
   🪨 Scout 1:  "faster = wins."             Right 60% of the time.
   🪨 Scout 2:  handed only the 40% it missed.
                "unless it's holding a Focus Sash."   Now up to 75%.
   🪨 Scout 3:  handed the remaining 25%.
                "unless Drizzle is up."               Now 85%.
   🪨 Scout 4:  ...
```

Each is nearly useless alone. Chained, they build a picture no single scout could hold.

⚠️ **You CAN overdo it.** Scout 400 is "fixing" battles that were decided by a lucky critical hit.
It's memorising dice rolls. **You must watch a held-out set and stop.**

⚠️ **Bad footage is poison.** This is the sharpest difference.

> A mislabelled match — recorded as a loss when it was a win — is something your chain will **never**
> get right. So every subsequent scout is handed it again. And again. The whole team gradually
> contorts itself around **one clerical error.**

The voting committee just shrugs it off as one vote in a hundred.

## Side by side 📊

| | 🌲 Bagging | 🏃 Boosting |
| --- | --- | --- |
| Training | all at once ✅ | strictly in order ❌ |
| Members are | wild and detailed | simple and reliable |
| Fixes | 🎪 inconsistency | 🪨 over-simplicity |
| More members | never hurts | **can hurt** |
| Bad footage | shrugged off ✅ | **chased relentlessly** ❌ |
| Tuning | almost none | a lot |

## Which to reach for 🎯

* 🎪 **Scouts memorising and falling apart on new battles?** → **Vote.**
* 🪨 **Scouts too simple to capture what's going on?** → **Chain.**
* 🗑️ **Footage you don't fully trust?** → **Vote.** Chaining will hunt down every error you left in.
* 🏆 **Need the best possible number, and have time to tune?** → **Chain.**
* ⚡ **Need something solid this afternoon?** → **Vote.** Nearly no tuning, hard to get wrong.
* 🏢 **Many gyms available?** → **Vote.** It parallelises perfectly; chaining is stuck in sequence.

## The third option 🎭

Hire **completely different kinds** of expert — a stats scout, a type specialist, a psychologist —
and then hire a **manager** whose only job is knowing which expert to trust when.

Best results there are. And a genuine nuisance to keep running: many experts to maintain, a manager to
retrain, and when something goes wrong you have no idea who to blame.
