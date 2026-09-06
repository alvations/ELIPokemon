---
id: "129"
slug: mt-evaluation-beyond-bleu
style: pokemon
category: translation
difficulty: intermediate
question: "Why is BLEU a poor metric for modern machine translation, and what replaced it?"
tags: [bleu, chrf, comet, bleurt, sacrebleu, mqm, wmt]
---

# Judging a Contest appeal by counting matching moves

Imagine a **Pokémon Contest** where the judges have one recording of a past winning appeal, and
score you purely on **how many of the same moves you used, in the same order.**

It would work, roughly. A Trainer who used entirely different moves would score badly and probably
deserve to. For years, that was good enough to run the circuit on.

And then everyone got good, and the counting stopped telling the judges anything.

## What breaks 🎭

```
   the recording :  Dragon Dance → Dragon Claw → Outrage → Dragon Rush
   your appeal   :  Dragon Dance → Dragon Claw → Outrage → Dragon Tail
                                                             ▲
                              one move different at the end, and every run of
                              four in a row now fails to match. Score: nothing.
```

* **🔁 A different move that does the same job scores zero.** You closed on **Thunderbolt** where
  the recording closed on **Thunder**. Same type, same idea, arguably the better choice. The
  counting sees a word it does not have.
* **🏆 There is more than one way to win.** The judges hold *one* recording. There were never only
  one good appeal, and the better the Trainers get, **the more good appeals exist that the
  recording does not contain.** The counting therefore gets *worse* as the field improves, which
  is a genuinely strange property for a scoring system.
* **🔤 Nearly-right counts as entirely wrong.** A move name inflected slightly differently scores
  exactly what a completely wrong move scores. In regions whose words change shape constantly
  (question 113), this is ruinous.
* **📋 It depends on how you write the moves down.** Two Contest halls that record moves with
  different punctuation produce scores that cannot be compared at all — which is why serious
  circuits fix a **standard rulebook**, like a **Regulation G** for scoring, and make everyone
  state which version they used.
* **🎯 It says nothing about one appeal.** The count only means anything across a whole season. Ask
  it about a single performance and it has no useful opinion, which rules out using it to decide
  whether *this* translation is safe to send.

## What the judges use instead 🧑‍⚖️

| How to judge | What it is | When to use it |
| --- | --- | --- |
| 🔡 **Count smaller pieces than whole moves** | matching fragments rather than move names | cheap, and far kinder to regions whose words change shape |
| 🧑‍⚖️ **An actual trained judge** | someone taught by watching thousands of appeals scored by people | the standard for comparing Trainers |
| 🙈 **A trained judge with no recording at all** | the same judge, working from the appeal alone | when there is no recording (question 132) |
| 📝 **Real people, marking specific faults** | humans marking exactly what went wrong and how badly | the gold everything else is measured against |

## The part worth actually understanding 📝

When people mark an appeal properly, they do not give it a number. They mark **what went wrong,
where, and how badly** — a fumbled flourish here, a move that made no sense there — and, crucially,
they mark **how serious each fault was.**

That last distinction is the one no counting scheme can express. There is a difference between:

* 😐 an appeal that was a little stiff in the middle, and
* 💀 an appeal where the Pokémon **fainted on stage.**

📌 One of those is "slightly lower marks". The other is **not a worse appeal at all — it is a
disaster**, and it does not belong on the same scale. Every scoring system that boils a
performance down to one averaged number hides exactly this, and it will keep hiding it right up
until the day it matters most.

In translation the fainting-on-stage errors are: a *not* dropped from a sentence, a dosage
changed, a name swapped for someone else's. Fluent, confident, and catastrophic.

## Rules for running the circuit fairly ⚖️

* 🧾 **Say which rulebook and which judge you used.** Judges are retrained between seasons and
  score differently afterwards. A number without a version on it is not a number.
* 📊 **Check the gap is real.** Two Trainers a hair apart are, in all likelihood, tied. People
  announce winners on gaps that small constantly.
* 🕵️ **Make sure the judge has not seen the routine before.** If your appeal was in the recordings
  the judge trained on, you will score magnificently and have performed nothing.
* 🎨 **Never average across the Contest categories.** A Trainer superb at **Cool** and hopeless at
  **Cute** averages out to "fine", and "fine" is a lie about both. The same asymmetry is the most
  common one in translation: excellent *into* one language, poor *out of* it, and the mean says
  nothing is wrong.
* 👀 **And watch fifty appeals yourself.** Every scoring scheme ever devised will miss the thing a
  person in the audience notices within a minute.
