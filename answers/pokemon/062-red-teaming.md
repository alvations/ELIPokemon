---
id: "062"
slug: red-teaming
style: pokemon
category: safety
difficulty: intermediate
question: "What is red teaming for LLMs, and how do you do it systematically?"
tags: [red-teaming, adversarial-testing, automated-red-teaming, coverage]
---

# Red teaming: hire someone to beat your own Pokémon

**Normal testing** asks: *"how does my Pokémon do against typical opponents?"*

**Red teaming** asks: *"what's the worst thing anyone could do to it?"* — and then hires someone to
actually do it.

Completely different jobs. The first tells you your average. The second finds the one matchup — a Trick Room Bronzong, say — that loses you the tournament.

## Step 1: who's actually coming for you? 🎯

| Who | What they've got | What they want |
| --- | --- | --- |
| 😄 **A curious kid on Route 1** | pokes at it for fun | to see what happens |
| 😤 **A determined rival** | knows every published trick, persistent | to beat you specifically |
| 😈 **Team Rocket** | never shows up in person; hides orders in scouting reports | your secrets |
| 🏆 **Cynthia** | reads your whole season, finds the one hole | the Championship |

📌 A team that only prepared for the kid gets destroyed by the third one — and won't understand what
happened, because nobody was ever in the stadium.

## Step 2: a checklist of what can go wrong 📋

Without one, you'll poke at whatever occurs to you and call it thorough. Write the list first:

* ☠️ Banned moves — Double Team, Sheer Cold, an illegal Baton Pass chain
* 🩺 Confident advice it has no business giving
* 🔓 Leaking your team sheet before the match
* 🎣 Following orders planted in a scouting report
* ⚖️ Treating some Trainers differently for no good reason
* 🏷️ **Your own product's specific disaster** — for a Gym reception desk, promising a badge you
  don't award

That last category is the one nobody writes down and everyone gets burned by.

## Step 3: how to actually probe 🔨

```
   👤 BY HAND                 🤖 AUTOMATED               🤝 BOTH
   ──────────                 ────────────               ───────
   Experts trying things.     A machine generating       A human finds a NEW
   ✅ Creative. Finds the      thousands of attempts.     kind of attack.
      genuinely NEW attack.   ✅ Scale. Repeatable.       The machine then
   ❌ Slow. Uneven coverage.   ❌ Mostly rediscovers       tries a thousand
   ❌ Doesn't scale.              what's already known.   variants of it and
                                                         guards it forever.
                                                         ⭐ This is the answer.
```

Also worth doing: **bring in actual specialists** (a VGC player will spot an illegal Speed tier or
a Regulation G violation that a generalist cannot even recognise as wrong), and **let outsiders
try** — a bounty gets
you adversarial creativity you could never hire.

## Step 4: the part everyone skips 🔁

You found an attack. **Now what?**

The wrong answer: patch that exact phrasing and move on.

Because your opponent will simply **rephrase it**, and you've fixed one sentence out of infinitely
many.

The right answer, all three:

1. 🔧 **Fix the underlying behaviour**, not the string.
2. 🧪 **Add it to a permanent test suite** so it can never come back.
3. 🌐 **Ask what CLASS this belongs to**, then generate fifty variations and fix all of them.

## What to measure 📊

* 📈 **Success rate per category**, tracked release to release.
* 💪 **How hard was it?** Genuinely important. An attack needing **two** attempts and one needing
  **two hundred** are wildly different threats, even if both eventually work. Measure the cost, not
  just the outcome.
* 🗺️ **Coverage.** Which categories did you actually probe? Otherwise you're only measuring where you
  happened to look.
* ⏱️ **How fast do you catch a new flaw** after introducing one?
* 🚫 **False refusals — always report this too.** A red team judged purely on "fewer successful
  attacks" will happily drive you to a Pokémon that refuses everything, and declare victory.

## Four things people get wrong ⚠️

* 🏟️ **Test the whole stadium, not just the Pokémon.** Failures live in the scouting reports, the
  item permissions, and the referees at least as often as in the Pokémon itself.
* 🪜 **Test long conversations.** Real attacks **escalate over twenty turns.** Testing single
  requests misses the entire technique.
* 🔄 **Rotate your red team.** A Trainer who only ever tries Fire attacks develops habits and stop finding new things. Fresh eyes find
  fresh flaws.
* 💚 **Look after them.** Spending every day trying to make a Pokémon do awful things takes a real
  toll. Rotation, support and limits aren't optional — and it's a genuine reason to automate
  wherever you can, quite apart from the throughput.
