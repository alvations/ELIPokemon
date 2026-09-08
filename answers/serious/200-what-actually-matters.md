---
id: "200"
slug: what-actually-matters
style: serious
category: synthesis
difficulty: core
question: "After all of this, what actually matters?"
tags: [synthesis, judgement, measurement, honesty, capstone]
---

# What actually matters

Two hundred questions. The techniques will date — most of the specific architectures here will look
quaint within a few years. What survives is a small number of habits that kept recurring, in
different clothes, across every topic in this dataset.

## 1. The average is where the important thing goes to hide

This appeared in almost every question and it is the single most transferable lesson.

```
   a critical error rate of 0.5%        ─► invisible in COMET (q129, q132)
   a fixed pronoun in every document    ─► invisible in corpus metrics (q131, q141)
   a 3x accuracy gap between groups     ─► invisible in aggregate accuracy (q184, q162)
   a benchmark that is 54% text-only    ─► invisible without a blind baseline (q147)
   a subtitle that overruns             ─► invisible to every quality metric (q144, q154)
```

The pattern is always the same: **the thing that determines whether the system is usable is not the
thing the headline number measures.** So: disaggregate by group, by language, by category, by
condition. Report the worst decile, not the mean. And name what your metric structurally cannot see.

## 2. Most reasoning failures are perception failures

Question 160's diagnostic — give the model a perfect description and see if the answer changes —
resolves an enormous share of apparent reasoning problems into resolution problems (questions 121,
127, 152). Extra thinking does not add pixels. Fix the input before you upgrade the model, and
before you add an agent (question 176).

## 3. Confidence is not correctness, and fluency is the disguise

A hallucinated object, an off-target translation, a wrong biometric match and an invented alt-text
description all arrive **fluent and confident** (questions 122, 136, 183, 184). Model
log-probability is therefore a poor detector of exactly the failures that matter. Ground it, cite
it, make it point at something, or check it with something that was not the thing that produced it.

## 4. Irreversibility needs a mechanism, not an accuracy number

Releasing the Pokémon, sending the email, moving the robot arm, banning the account, arresting the
person. No accuracy figure substitutes for a confirmation gate and a bounded action space
(questions 145, 181, 184, 187). This is architecture, and it is the only thing that still holds
after the model is wrong.

## 5. Whatever you optimise becomes the target

Reward models get gamed, LLM judges get gamed, aesthetic scorers get gamed, and so does any
Pokémon-ness score somebody attaches to a dataset like this one (questions 021, 038, 167, 190). A
metric is a **search tool for finding things worth looking at**. The moment it becomes the goal, it
stops measuring the thing it was proxying for.

## 6. Say what you did not measure

The languages you did not evaluate. The groups your test set did not contain. The resolution you
benchmarked at. The safety training that covers one language. The filter that removed every chart.

These sentences cost something to write, and they are the difference between a document written for
a reader and one written for a launch (questions 185, 196, 197).

## And the one that is not technical

Several questions here — sign language, endangered languages, accessibility, biometrics, community
data — reach a point where the engineering stops and a decision about people begins. The recurring
answer was the same each time: **involve the people it is about, pay them, ask before you take, and
accept "no" as an answer.** That is not adjacent to the work. On those problems it *is* the work,
and no benchmark will ever tell you that you got it wrong.

## What an interviewer digs into next

* Give an example from your own work where the aggregate metric hid the deciding failure.
* How would you tell a perception problem from a reasoning problem?
* What in your current system would still be safe if the model were wrong?
* What have you shipped without measuring, and do you know that you did?
