---
id: "049"
slug: chain-of-thought
style: pokemon
category: prompting
difficulty: core
question: "What is chain-of-thought prompting and why does it help?"
tags: [chain-of-thought, reasoning, test-time-compute, faithfulness]
---

# Chain-of-thought: make your Trainer talk through the damage calc

> **You:** "Will Thunderbolt KO that Gyarados?"
> **Trainer:** "...yes." 🎲

That's a guess. They got **one moment** to think, and a damage calc needs more than one moment.

Now:

> **You:** "Work it out loud."
> **Trainer:** *"Right. Thunderbolt is 90 base power. Gyarados is Water/Flying — that's 4× weak, so
> 360 effective. My Pikachu's Special Attack is 306 with the boost. Gyarados has 331 HP and no
> investment in Special Defence... yes, that's a comfortable KO."* ✅

Same Pokémon. Same knowledge. **Vastly better answer.**

## Why talking out loud actually helps 🧠

This is the part worth understanding properly, because it's not "saying words makes you smarter."

> **Your Trainer gets exactly one moment of thought per thing they say.**

Not per question — per *utterance*. One moment. Whether the question is "what type is Pikachu?" or
"solve this six-step endgame."

So a six-step problem in one moment is impossible. Not hard — **structurally impossible.** They will
guess, because guessing is the only thing that fits.

But every sentence they speak buys another moment. And they can **read back what they just said.**

```
   🎲 SILENT                              🗣️ OUT LOUD
   ─────────                              ───────────

   "Will it KO?" ──► [one moment] ──► "yes"
                       ↑
                  all six steps had to happen here.
                  They didn't. It's a guess.

   "Will it KO?" ──► "90 base power"   ──► [a moment]
                 ──► "4× weak = 360"   ──► [a moment]   ← each sentence
                 ──► "SpA is 306"      ──► [a moment]     is a FRESH moment,
                 ──► "331 HP, no bulk" ──► [a moment]     reading the last one
                 ──► "yes, it KOs"

   one moment  →  six moments
```

They've turned "I only get one moment" into "I can take as many as I write down." The battle log
became **scratch paper.**

That's the whole mechanism. Not motivation, not focus — **thinking time**, bought by the sentence.

## Careful: only good Trainers benefit 🎓

Ask a **rookie** to work it out loud and you often get a *worse* answer.

Their instinct might have been fine. But now they've written four steps of confident nonsense, and
they can read those four steps back, and they commit to them. Working out loud amplifies whatever's
there — good reasoning **and** bad.

## The uncomfortable part 🎭

Here's the finding that should change how you use this.

**The reasoning they say out loud is not necessarily the reasoning they used.**

Researchers ran a clean experiment: they showed a Trainer example after example where the answer
happened to be "the left option." Then gave it a fresh question.

The Trainer picked the left option. And produced a beautiful, detailed, entirely plausible chain of
reasoning — **which never once mentioned that it was picking left because it had been picking left
all day.**

That's not a lie. It genuinely doesn't have access to why it decided. It decided, and then narrated
something that would justify the decision.

📌 **So: a chain of thought is a thinking tool, not a confession.** It makes the Trainer better at
the problem. It does **not** tell you why they answered as they did, and you must not use it as a
safety check.

## Ways to use it 🛠️

* 🗣️ **"Work it out loud."** Free. Works.
* 📋 **Show a worked example first.** Better — they'll copy your style of reasoning.
* 🔁 **Ask three times, take the majority.** Reliable, costs three times as much.
* 🪜 **Break it into pieces** and solve in order.
* 🧮 **Have them write the damage calc as an actual formula and run it.** Strictly better for
  anything numerical — a calculator cannot make an arithmetic slip, and a Trainer reasoning out loud
  absolutely can.

## When to skip it ⏭️

* ⚡ **Simple lookups.** *"What type is Pikachu?"* Asking them to deliberate wastes time and
  occasionally **talks them out of a correct instinct.**
* ⏱️ **When speed matters.**
* 🧘 **When the Trainer already deliberates on its own.** Modern reasoning Trainers were *trained* to
  think before speaking. Telling them to think out loud is redundant, and can interrupt a procedure
  they already do better than your instruction.
