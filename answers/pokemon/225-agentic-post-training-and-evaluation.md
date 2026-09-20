---
id: "225"
slug: agentic-post-training-and-evaluation
style: pokemon
category: open-weights
difficulty: advanced
question: "A model claims long-horizon agentic tool use and tops a frontend-code arena. How do you check either claim?"
tags: [agents, tool-use, synthetic-data, evaluation, leaderboards]
---

# Seven buildings, one Pokémon, seven different answers

"Wins with Pokémon it has never held before" and "first on the board" are two claims, not one. The
first is about how something was raised and you check it by reading what was built. The second is
about a board and you check it by asking what the board counts. **Hoenn**'s **Battle Frontier** is
the place where both questions have an answer, because it is seven buildings with seven sets of
rules and one **Pokémon League** worth of the same Pokémon walking through all of them.

## Where the capability is actually manufactured

The **Battle Factory** is the hard one. Factory Head **Noland** does not let you bring your team.
You are handed rentals — Pokémon you did not raise, with four moves somebody else chose — and
after each win you may swap for one of the Pokémon that just lost to you. You open the summary and
find **Cross Chop** where you were expecting **Earthquake**, and you have one turn to decide
whether that is good news.

The skill being tested is reading a screen you did not write. **Slaking** hits harder than almost
anything in the game and **Truant** means it only acts every other turn. **Shedinja** has exactly
1 HP, and **Wonder Guard** blocks every damaging move that is not **Super Effective**.
**Regigigas** spends its first five turns under **Slow Start** with its Attack and its Speed
halved. **Machamp** with **No Guard** turns **Dynamic Punch** from a 50% coin-flip into a
guaranteed hit that confuses, and **Smeargle** with **Sketch** permanently copies the last move
its target used. Five summary screens, five completely different turn-one decisions, and not one
of them says so in words.

Training for that is a manufacturing problem, and it is built the way the **Battle Frontier** is
built:

* **A huge pool of sets.** Thousands of them, some lifted straight from what real Trainers
  actually run, most generated — pick a category, branch it into specific styles, then fill each
  style with sets that fit it.
* **Thousands of shapes to be.** Every combination of a role and a handful of those sets is a
  different thing to practise being.
* **A stated win condition, written first.** The **Battle Arena** does this openly: three turns,
  then a referee scores Mind, Skill and Body and declares it. The standard exists before the
  battle does, which is the only way a result means anything.
* **An opponent that runs itself.** In the **Battle Palace**, Palace Maven **Spenser** takes the
  move choice away from you entirely — each Pokémon picks for itself according to its Nature. The
  environment has its own rules, keeps its own state, and will surprise you.

And there is a limit the honest version admits. A simulated opponent is a guess about what an
opponent does. For the cases where the guess is not good enough — real damage rolls, real PP, real
**Critical Hit** luck — you go and have the actual battle at the **Battle Tower** against Salon
Maiden **Anabel** and take the actual result.

The version that generalises does one more thing: it practises in **all seven buildings**, not
one. Train only at the **Battle Tower** and you have raised a Pokémon that is excellent at the
**Battle Tower**.

## Which tells you exactly how to read a record

```
   SAME POKEMON, DIFFERENT BUILDING, DIFFERENT RESULT

   Battle Tower    you choose the moves, you brought the team
   Battle Factory  you choose the moves, someone else brought the team
   Battle Palace   you choose NOTHING; the Pokémon picks by its Nature
   Battle Arena    three turns, then a referee decides on Mind/Skill/Body

   ┌──────────┐   ┌──────────────────────────────────────┐   ┌────────┐
   │ the same │──►│ BUILDING: who picks, what you brought│──►│ streak │
   │ Pokémon  │   │ what counts as winning, how long     │   └────────┘
   └──────────┘   └──────────────────────────────────────┘
                        ▲
                        └ this box is not printed next to the streak,
                          it is not the same across buildings, and it
                          moves the number more than the Pokémon does
```

A streak quoted without its building is not a measurement. The details that decide it — how many
turns before a referee steps in, whether you got to pick the moves, whether you brought the
**Held Item** or found it — never appear beside the number.

## The board, checked

Reported: in July 2026 an open challenger went straight to first place on a board that ranks how
Trainers *look* when they build something, with 1679 points, a seventeen-place jump from the
previous version at eighteenth, a 76% head-to-head win rate, and first place in six of seven
categories — second only in the one about games. A second board reported the same challenger first
at 1326. Both numbers come from the boards' own announcements as passed along by others; neither
board itself could be reached from here, so the boards are the authority and the numbers here are
second-hand.

The result is real and it is narrower than it sounds:

1. **It is a crowd's preference.** Two entries shown side by side, people pick the one they like.
   That is the **Pokémon Contest** axis of question 202 — fed on **Poffins** and appeal, scored on
   **Contest Condition** — and not the **Battle Tower** streak axis. The gap between the two is
   widest exactly where appearance is part of the judging.
2. **It is one category.** The same release's own table has it behind the strongest closed teams
   in several other buildings.
3. **A seventeen-place jump in one version says something about the board as well.** Either the
   Pokémon changed enormously, or the ranking is light on its feet. Say both.

## How I would actually check the first claim

* **Hold the building fixed and change only the Pokémon.** Then hold the Pokémon fixed and change
  only the building. Report both, or neither means anything.
* **Count per-turn reliability across a long streak, not the streak.** **Focus Blast** is 70%
  accurate: throw ten and you have missed three, and a **Bright Powder** on the other side means
  your 70% was never 70%. Forty-nine clean turns and one **Hyper Beam** that leaves you
  recharging is still a loss, and *where* it went wrong matters more than that it did.
* **Hand it sets it has never seen.** The whole point of the **Battle Factory** is unfamiliarity.
  Test that, with your rentals, not the famous ones.
* **Watch what it does after a miss.** Does it notice that **Focus Blast** missed, or does it play
  the next turn as though the hit landed? That never shows up in a streak and it decides real
  runs.

## What a Gym Leader is listening for

That you pull the two claims apart before answering either, and that you reach for the building
as the confound unprompted. Credit for noticing that the record itself tells you the building
mattered — the detail is there, just never next to the number.

## Where this stands, September 2026

The **Battle Frontier**'s rules are from the games and do not rot. The placings are from
announcements passed along by others and will be stale in weeks; go and read the board. What lasts
is the shape: the building is a confound, a crowd's preference is a different axis from a streak,
and per-turn reliability beats an end-to-end record every time.
