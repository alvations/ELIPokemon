---
id: "056"
slug: multi-agent-systems
style: pokemon
category: agents
difficulty: advanced
question: "When is a multi-agent system worth it, and how do you design one?"
tags: [multi-agent, orchestrator, context-isolation, coordination]
---

# Multi-agent: when do you need more than one Trainer?

Start sceptical. **Two Trainers cost more than one, argue with each other, and are miserable to
debug.** Most of the time, one good Trainer with a good bag beats a committee.

So: what specifically makes a second Trainer worth it?

## The three real reasons ✅

**1. 🎒 Keeping the bag clean** — the strongest one by far.

You need someone to read forty scouting reports. Do it yourself and your bag is now stuffed with
forty reports, and you're trying to battle around them.

Send a Noctowl instead — it has Keen Eye and nothing better to do. **It** reads all forty, with its
own bag. They come back and say:

> *"They're running Rain. Kingdra is the threat. Bring Ferrothorn."*

One sentence. Your bag never held the forty reports. This is the reason most good multi-Trainer
setups exist.

**2. ⚡ Genuinely parallel work.** Five opponents to scout — Politoed, Kingdra, Ferrothorn, Toxapex,
Tapu Fini — and no scouting depends on any other? Send five scouts. Five times faster.

**3. 🎯 Different jobs, different kit.** A Route 1 Trainer sorts the Rattata; the expensive one only
sees the hard ones.

## Shapes 📐

```
   👑 A LEAD AND SCOUTS               ➡️ A RELAY
   ──────────────────                 ─────────
        ┌────────┐                    ┌───┐  ┌───┐  ┌───┐
        │ 👑LEAD │                    │ A │─►│ B │─►│ C │
        └───┬────┘                    └───┘  └───┘  └───┘
       ┌────┼────┐                    Fixed order. Easy to
       ▼    ▼    ▼                    understand and test.
     🔍   🔍   🔍
   scout scout scout                  ⚔️ MAKER AND CRITIC
                                      ──────────────────
   Lead splits the work,               ┌───────┐  ┌────────┐
   scouts run in parallel,             │ maker │◄►│ critic │
   lead puts it together.              └───────┘  └────────┘
   The default, and usually right.     Quality by argument.
```

## Where it falls apart 🚨

**💬 Talking costs more than working.** Every handoff burns time and tokens. A three-layer chain of
command can spend more on relaying orders than on battling.

**📉 Mistakes multiply — now across people.** One Trainer at 95% over twenty turns already gets you
36%. Add handoffs and each one is a fresh chance for a misunderstanding that **nobody notices**,
because the scout reported confidently and the lead has no way to check.

**🗣️ Orders get garbled.** This is the classic. The lead says *"scout their Water team."* The scout
hears *"scout their team."* Comes back with everything and nothing.

📌 **Fix: be painfully specific.** Not *"look into their team"* but *"identify their Water types,
their held items, and whether the weather setter is Politoed or Pelipper. Report as a list. Do not comment on
anything else."*

**💰 It's expensive.** Genuinely — a research operation with a lead and several scouts can use
**fifteen times** the resources of one Trainer answering directly. Worth it for something important.
Absurd for *"what type is Pikachu?"*

**🐛 Debugging is awful.** Five Trainers, running concurrently, each with their own bag, each
slightly non-deterministic. Without tracing you will never work out what went wrong.

**✍️ Two Trainers editing the same thing.** Two scouts both update the Garchomp entry on the team
sheet. One overwrites the
other. Silent, and catastrophic.

## The rules that actually hold 📋

1. **✍️ Only one Trainer writes.** Everyone can read anything. **One** person makes changes — or give
   each a completely separate thing to change. Concurrent edits are the single biggest source of
   multi-Trainer bugs.
2. **📝 Spell out each scout's job completely.** Objective, what to report, what tools they have,
   and **what not to touch.** Vague orders produce duplicated and contradictory work.
3. **📄 Scouts report conclusions, not transcripts.** *"They're running Rain"* — not the forty
   reports. Handing back everything defeats the entire purpose.
4. **⏱️ Put a limit on everything.** Turns, time, cost, per scout and overall.
5. **👀 Fan out to LOOK, converge to ACT.** Many scouts investigating is safe. Many Trainers acting
   is chaos.
6. **🏷️ Tag everything with who did it**, or you'll never untangle it afterwards.

## The heuristic 🎯

> **Use one Trainer until you can name the exact constraint a second one relieves.**

*"My bag is full"* — good reason. *"These five things are genuinely independent"* — good reason.

*"It feels more modular"* — not a reason. That's how you end up with five Trainers, a coordination
problem, a debugging nightmare, and a bill.
