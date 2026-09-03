---
id: "037"
slug: evaluating-llms
style: pokemon
category: evaluation
difficulty: core
question: "How do you evaluate an LLM, and what are the common pitfalls?"
tags: [evaluation, benchmarks, elo, human-eval, task-specific-evals]
---

# How do you know if your Trainer is actually good?

There's no single number. You need a **portfolio of tests**, and knowing which tests to run is the
actual skill.

```
  🏅 THE GYM CIRCUIT — standardised, everyone takes them
     Eight badges, same Leaders, same rosters.
     ✅ cheap, repeatable, everyone's score is comparable
     ❌ they've been the same for years, and the answers have leaked

  🎯 THE PRACTICE FIELD — automatic checks
     "Did the Pokémon actually faint?" — objective, no judging.
     ✅ unfakeable and free  ❌ only works where there's a right answer

  👥 THE JUDGES — human ratings
     Real people watch and say which Trainer they'd rather have.
     ✅ closest to what "good" actually means  ❌ slow, costly, and even
        expert judges only agree ~75% of the time

  🏟️ THE ACTUAL SEASON — production
     Real matches, real stakes, real win rate.
     ✅ the only thing that truly counts  ❌ slow, noisy, needs volume
```

## Seven ways your evaluation lies to you 🚨

**1. 📖 They've seen the exam.** Your Trainer scores 94% on the Gym Circuit! Impressive — until you
learn those exact battles have been in every training tape for six years. They didn't out-think
Brock. They **memorised** Brock. Use freshly-written battles nobody could have studied.

**2. 🏔️ The test is too easy now.** Everyone scores 90%+ on the Circuit. So what's the remaining
10%? Mostly **mistakes in the answer key**. Above about 90% you've stopped measuring Trainers and
started measuring the referees.

**3. 🎲 The same Trainer scores differently depending on how you ask.** Shuffle the order of the
options and the score moves ten points. Ask them to say the answer instead of pick it — ten more.
Two reports with different numbers for the same Trainer are usually **both correct**, and just
asked differently.

**4. 🎯 The Circuit isn't your job.** This is the big one.

> Your Trainer got all eight badges. Congratulations. **You run a daycare.**

Beating Brock tells you nothing about whether they can handle a distressed Eevee. Nothing. Build a
test out of **your actual work** — a hundred real cases from your own daycare beats every badge in
the League.

**5. 1️⃣ One number hides everything.** Trainer A wins more battles; Trainer B follows instructions
better and costs a fifth as much. "Which is better" isn't a question with an answer until you say
what for. Report a **profile**, always including cost and speed.

**6. ☀️ You only tested the easy days.** Everyone tests: Pokémon healthy, clear weather, standard
opponent.

Nobody tests: the opponent cheats. The Pokémon is poisoned. Someone asks in a language your Trainer
barely knows. The battle runs 400 turns. The request is genuinely ambiguous. **That's where real
failures live**, and it's exactly what nobody puts in the test set.

**7. 📉 Three battles is not evidence.** Trainer A won 3 more out of 200. That's a **coin flip**,
not a finding. Run it multiple times, report the uncertainty, and don't ship on noise.

## Building a test you can trust 🛠️

1. 📋 **Pull cases from your real season**, not from your imagination. Your intuitions about what
   comes through the door are wrong. They always are.
2. 🗂️ **Include the rare disasters**, not just the common cases. Frequency isn't importance.
3. ✍️ **Write the grading rubric BEFORE you watch any battles.** Watch first and you'll
   unconsciously write a rubric that rewards what you just saw.
4. 🔒 **Keep a private set nobody trains against.** The moment a test becomes a target, it stops
   being a measurement. Guard one.
5. 🏷️ **Version everything.** Test sets drift. Scores are only comparable within a version.
6. 👥 **Check whether your judges even agree.** If two judges only agree 60% of the time, no
   Trainer can ever score above 60% — and your problem is the rubric, not the Trainer.
