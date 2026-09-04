---
id: "008"
slug: kv-cache
style: pokemon
category: inference
difficulty: core
question: "What is a KV cache and why does it dominate LLM inference memory?"
tags: [kv-cache, inference, decoding, memory-bandwidth]
---

# The KV cache is your battle notebook

Every turn, a good Trainer scouts the field: what's out, what type it is, whether it's holding
Leftovers or a Focus Sash, what it's already done. That scouting takes time.

Now — here's the thing — **none of it changes**. Gyarados was Water/Flying on turn 1 and it's
still Water/Flying on turn 40. So why are you re-scouting the whole field every single turn?

Write it down once. That notebook is the KV cache.

```
  🐌 THE ROOKIE                          📓 THE PRO
  ─────────────                          ──────────

  Turn 1: scout 1 Pokémon                Turn 1: scout it → write it down
  Turn 2: re-scout both                  Turn 2: scout the NEW one → append
  Turn 3: re-scout all three             Turn 3: scout the NEW one → append
  Turn 40: re-scout all forty            Turn 40: scout the NEW one → append

  Spends the whole match scouting.       Scouts each Pokémon exactly once.

           ┌──────── THE NOTEBOOK ────────┐
           │ Gyarados │ Water/Flying │ Sash │
           │ Golem    │ Rock/Ground  │ ---- │
           │ Ferrothorn│ Grass/Steel │ Leftovers │
           │ ...                          │
           │ ← new entry goes here        │
           └──────────────────────────────┘
```

## Two completely different phases ⏱️

**📖 Reading in the team sheet.** At the start you get the opponent's full roster — Politoed,
Kingdra, Ferrothorn, Toxapex, Tapu Fini, Gyarados — and scout the lot in one go. Busy, focused,
efficient — you're doing real work every second. A long roster
takes longer, but it's *productive* time.

**⚔️ Playing the turns.** Now you're making one decision per turn. And before each decision you
**flip through the entire notebook** — all forty entries — to make one call. The flipping takes
longer than the thinking.

This is the single most important fact about running a model in production: getting the first
reply out is a *reading* problem, and every word after it is a *page-flipping* problem. They
need completely different fixes.

## Why the notebook is the problem 📚

Your Pokédex — everything you know about Pokémon in general — is one book, and you share it
across every match you'll ever play.

The notebook is **per match**. Running forty simultaneous battles means forty notebooks. And at
tournament scale each one is thick enough to rival the Pokédex itself.

So the thing that limits how many battles you can run at once isn't how much you *know*. It's
how many **notebooks** fit on the desk.

## Slimming the notebook ✂️

* 🤝 **Share the columns.** All your coaches keep separate notebooks with mostly identical
  content. Make them share one. Instantly 8–64× thinner.
* 📄 **Loose-leaf pages.** Don't hand every match a 500-page binder when most matches end in 12
  turns — that's 488 blank pages of wasted desk. Give out pages as needed and take them back
  when the match ends. This isn't compression at all; it's just not *wasting* space, and it's
  worth more than most actual compression.
* ✏️ **Write smaller.** Abbreviate. Slightly harder to read, half the thickness.
* 🪟 **Tear out old pages.** Turn 200 rarely needs the Caterpie that fainted on turn 3. Keep a
  rolling window — but always
  keep page one, because Trainers have a strange habit of glancing back at the very first page
  whenever they've got nothing useful to look at, and tearing it out breaks them.
* 📋 **Photocopy the standard briefing.** If every match starts with the same twelve-page
  Regulation G packet, scout it *once* and staple a copy into each notebook. Never read it twice.
