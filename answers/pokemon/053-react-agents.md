---
id: "053"
slug: react-agents
style: pokemon
category: agents
difficulty: core
question: "What is ReAct, and what is the anatomy of an LLM agent?"
tags: [react, agents, tool-use, agent-loop, planning]
---

# ReAct: think, act, look, repeat

Two bad ways to battle.

**🤔 The Overthinker.** Plans the entire forty-turn match before sending anything out. Beautiful
plan. Turn 2, the opponent does something unexpected, and the plan is worthless — but they're still
following it, because it's the plan.

**⚡ The Button Masher.** No plan at all. Sees a Pokémon, attacks it. Sees another, attacks that. No
idea what they're building toward, and no idea why anything is happening.

**ReAct is the actual answer: think one turn ahead, act, LOOK AT WHAT HAPPENED, think again.**

```
   ┌──────────────────────────────────────────────────────────────┐
   │  🤔 THINK    "Gyarados is out. It's 4× weak to Electric."     │
   │  ⚡ ACT      Thunderbolt.                                      │
   │  👀 LOOK     "It survived on exactly 1 HP — Focus Sash."      │
   │  🤔 THINK    "Sash is used up now. Anything finishes it."     │
   │  ⚡ ACT      Quick Attack.                                     │
   │  👀 LOOK     "Gyarados fainted. They're sending in Ferrothorn."│
   │  🤔 THINK    "Bad matchup for me. Switch to Charizard."       │
   └──────────────────────────────────────────────────────────────┘
              ▲                                             │
              └──────── keep going until the match ends ────┘
```

The **look** step is what makes it work. The Overthinker never looks. The Button Masher looks but
doesn't think about it. ReAct does both, every turn.

## Every agent has five parts 🔧

| Part | What it is | How it fails |
| --- | --- | --- |
| 🧠 **The Trainer** | who decides | a weak Trainer loops or freezes |
| 🎒 **The items** | what they can actually do | too many, or unclear what each does |
| 🔄 **The loop** | act, look, repeat | **no stopping condition** |
| 📓 **The bag** | what they're carrying | fills up with stale notes |
| 🏁 **Knowing when to stop** | the end | **the most neglected part of all** |

The loop itself is trivial. Everything hard is in the other four.

## The five things that go wrong 🚨

**1. 🔁 It never stops.**

The classic. Your Trainer switches Pikachu in. Then out. Then in. Then out. Each switch is
individually defensible. Forty turns later they're still doing it and the clock has run out.

📌 **Always set a hard limit.** A maximum turn count, a maximum time, a maximum cost. And watch for
the same action twice in a row — that's your loop alarm.

**2. 💥 Something fails and it panics.**

The Potion doesn't work. The switch is blocked. The move misses.

**Tell the Trainer what happened** — *"that failed, here's why"* — and let them adapt. Don't crash
the battle. But **cap the retries**, because a Trainer will cheerfully attempt an impossible move
twenty times in a row.

**3. 🎒 The bag fills with junk.**

By turn 30 they're carrying twenty-nine turns of notes about Pokémon that already fainted. Prune it.

**4. 📉 The maths nobody wants to hear.**

This is the most important thing on this page.

```
   Your Trainer is right 95% of the time. Excellent Trainer!

   A 5-turn task:   0.95⁵  = 77% ✅
   A 10-turn task:  0.95¹⁰ = 60% 😐
   A 20-turn task:  0.95²⁰ = 36% 😰
   A 40-turn task:  0.95⁴⁰ = 13% 💀
```

**Every turn multiplies.** A Trainer who's right 95% of the time fails most long tasks — not because
they're bad, but because 95% isn't close to enough when you need forty of them in a row.

Which gives you exactly three options: **make each turn more reliable**, **make the task shorter**,
or **check the work as you go and recover** when a turn goes wrong.

**5. 🎒 Too many items.**

Past about fifteen or twenty items, your Trainer starts picking the wrong one. Two items with
similar descriptions and it can't tell them apart.

**Fewer, clearly distinct items beats a comprehensive kit.** Or split the job across several
Trainers, each with a small focused bag.

## Variants ⚔️

* 📋 **Plan first, then execute.** Fewer decisions, cheaper — and brittle the moment reality
  diverges from the plan.
* 🪞 **Lose, write down why, try again.** Genuinely effective for tasks you can retry.
* 🌳 **Explore several lines and back up when one goes bad.** Thorough, expensive.
* 👥 **Several Trainers, each specialised**, with a coordinator.

One historical note: this pattern won so completely that it stopped being a *technique*. Modern
Trainers are **trained** to think-act-look. You no longer script it — it's just how they battle.
