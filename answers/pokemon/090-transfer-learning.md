---
id: "090"
slug: transfer-learning
style: pokemon
category: training
difficulty: core
question: "What is transfer learning and how do you decide what to freeze?"
tags: [transfer-learning, freezing, feature-extraction, discriminative-lr, domain-shift]
---

# Transfer learning: your Champion already knows how to battle

You need a Trainer who's great at **Misty's Water Gym.** You could raise one from scratch —
months of wild grass, the whole journey.

Or you could take a Champion who already knows everything about battling in general, and **teach it
the Water specifics in an afternoon.**

Because most of what makes a Champion good has nothing to do with Water types.

## What transfers, and what doesn't 📚

```
   ┌──────────────────────────────────────────────────────────────┐
   │  🧱 THE BASICS                                                │
   │  Type effectiveness. Reading the field. When to switch.       │
   │  How items work. Turn order.                                  │
   │  ✅ Transfers to LITERALLY ANY battle. Never retrain this.    │
   ├──────────────────────────────────────────────────────────────┤
   │  🔧 THE INTERMEDIATE STUFF                                    │
   │  Common team structures. Standard openings. Weather play.     │
   │  ⚠️ Mostly transfers — some of it is format-specific.         │
   ├──────────────────────────────────────────────────────────────┤
   │  🎯 THE SPECIFICS                                             │
   │  "Misty leads Starmie and Protects turn one."                 │
   │  ❌ Useless for your task. Replace it entirely.               │
   └──────────────────────────────────────────────────────────────┘
```

The basics are the same in every battle ever fought. The specifics are about *one opponent.*

📌 One genuinely surprising finding: the **middle** layer transfers worst of all — worse than either
end. Those habits are tangled up with each other, and pulling them apart breaks them. The basics
transfer cleanly; the specifics you were replacing anyway; the middle is a knot.

## What to keep frozen 🧊

Two questions decide it: **how much footage do you have**, and **how different is your task?**

```
                  footage:  📼 A LITTLE            📚 A LOT
                          ┌────────────────────┬────────────────────┐
   task is  🤝 SIMILAR    │ ❄️ Freeze the whole │ 🔥 Retrain gently  │
                          │ Champion. Just      │ everywhere         │
                          │ teach it the new    │                    │
                          │ opponent's roster.  │                    │
                          ├────────────────────┼────────────────────┤
            🌍 DIFFERENT  │ ❄️ Freeze the       │ 🔥 Retrain, or     │
                          │ basics, retrain     │ honestly just      │
                          │ the specifics.      │ start over if it's │
                          │ ⚠️ THE HARD ONE     │ REALLY different   │
                          └────────────────────┴────────────────────┘
```

That bottom-left square is the genuinely difficult case: **not enough footage to teach it, too
different for what it knows to apply.** It's exactly where the held-item trick earns its money.

## Ways to do it 🛠️

* 🧊 **Freeze everything, just add new knowledge.** Fast, needs almost no footage. Also a useful
  **test**: if freezing everything works fine, the Champion already knew what you needed — you were
  only ever missing the roster.
* 🔥 **Retrain everything, very gently.** Ten to a hundred times gentler than the original raising.
* 🪜 **Thaw from the top down.** Teach the new specifics first, then gradually let the intermediate
  stuff adjust, and only touch the basics last if at all.
* 🎒 **Held item.** Freeze the Champion entirely, bolt on a small adapter. The modern default.

## Five ways to ruin a Champion 🚨

**1. 🔥 Training too hard.** The most common failure by a mile. Blast a Champion with Champion-level
intensity on a new task and **the first ten minutes destroy months of work.** Start gently. Always.

**2. 🎲 Attaching a clueless new specialist.**

You bolt on a brand-new Water specialist who knows **nothing.** It immediately starts shouting wild,
random corrections — and those corrections propagate down into your Champion's carefully built
basics.

**Fix: train the new specialist ALONE first**, until it's at least sensible. *Then* let it talk to the
rest of the team.

**3. 📏 Changing the format.** Your Champion learned to read team sheets in one particular layout. Hand
it a differently-formatted sheet and its expertise is worthless — it can't read the input any more.
**Use exactly the same format as the original training.**

**4. 🌡️ "Frozen" that isn't actually frozen.** You froze the Champion's stats — but if any part of it
is still **recalibrating itself** against what it's currently seeing, it's quietly drifting. Your
frozen Champion isn't frozen. Insidious, because everything looks correct.

**5. 🚫 The Champion actively hurts.**

Rare with a genuinely strong Champion, real with a mediocre one. If your Champion trained exclusively
in Sootopolis City and you need a Hoenn desert specialist, its instincts may be **worse than nothing** —
it'll confidently apply lessons that don't hold.

**Always sanity-check against a Trainer raised from scratch.** If starting fresh wins, your Champion
was the problem.
