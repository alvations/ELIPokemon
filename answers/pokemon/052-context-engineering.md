---
id: "052"
slug: context-engineering
style: pokemon
category: prompting
difficulty: intermediate
question: "What is context engineering, and how is it different from prompt engineering?"
tags: [context-engineering, prompt-engineering, agents, context-rot, memory]
---

# Context engineering: what's in the Trainer's bag?

**Prompt engineering** is giving good instructions: *"lead with Ferrothorn, don't switch into
Earthquake."*

**Context engineering** is deciding what your Trainer is **carrying** when they walk into the
stadium. And once a battle runs forty turns with items and scouting reports, what they're carrying
matters far more than what you said at the start.

## The bag is small and everything wants in 🎒

```
  ┌── THE BAG — limited space, everything competing ──────────────┐
  │                                                               │
  │  📜 your standing orders          ← same every battle          │
  │  🔧 Potions, Revives, Ultra Balls ← grows with every addition   │
  │  📄 scouting reports on Toxapex   ← biggest and most variable   │
  │  📝 the log of everything so far  ← grows forever               │
  │  📊 results of everything tried   ← can be ENORMOUS             │
  │  🗒️ the current plan               ← working memory              │
  │  ❓ what you actually asked        ← often the smallest thing    │
  │                                                               │
  │  every page in here competes with every other page             │
  └───────────────────────────────────────────────────────────────┘
```

## Why this is the hard part 😰

**🌫️ A full bag makes a worse Trainer.** Not "slower" — **worse**. Your standing orders from turn 1
are competing with three hundred pages of accumulated notes. Stuff in the middle gets skimmed. Every
extra page is another thing to be distracted by.

**💸 Carrying costs money and time**, linearly. A stuffed bag isn't free just because it closes.

**💥 One item can flood the bag.** Your Trainer checks the field once and gets back the full
fifty-page Pokédex entry for Ferrothorn. Shove that straight in the bag and everything else is buried. **This is the single most common
way an agent dies.**

**📈 Forty turns of notes.** By turn 40, the bag is mostly stale observations from turn 6, and your
Trainer is reasoning about a battle that isn't happening any more.

## How to pack properly 🧳

**📝 Condense the old pages.** When the bag fills, replace the first thirty turns with a one-page
summary and carry on. Essential for long battles — and risky, because the detail you summarised away
might have been the one that mattered.

**🗒️ Keep a plan on a separate sheet.** Don't make your Trainer *remember* the plan from the log —
have them **write it down and keep updating it.** It survives every condensing, it's short, and you
can read it yourself to see what they think they're doing.

**🔍 Carry the index, not the library.** Don't stuff every scouting report in the bag. Carry the
*list* of reports and fetch one when you actually need it. Exactly how a person works with a filing
cabinet.

**✂️ Cap what comes back.** Any check that could return fifty pages should return **one page and an
offer to show more.** Non-negotiable.

**🧑‍🤝‍🧑 Send someone else to do the digging.** Best trick there is. Send a scout off to investigate
with their *own* empty bag. They read forty pages, work it out, and come back with **one sentence**.
Your Trainer never sees the forty pages. Their bag stays clean.

**📌 Put the unchanging stuff first.** Standing orders, then item list, then the variable material.
Anything that's identical every battle can be **pre-packed once** and reused — but only if it's at
the *top* of the bag. Reorder it and you lose that, and pay full price every time.

**🔧 Carry fewer items.** Counterintuitive: adding a useful item can make your Trainer **worse**.
Twenty items with overlapping descriptions and it starts picking the wrong one. Fewer, clearly
distinct items beats a comprehensive kit.

## The principle 🎯

> **Find the smallest set of genuinely useful pages that gets the job done.**

Not "the bag holds three hundred pages, so pack three hundred." Every page costs money, costs time,
and — the one people miss — **steals attention from the pages that mattered.**
