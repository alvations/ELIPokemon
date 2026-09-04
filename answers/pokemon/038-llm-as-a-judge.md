---
id: "038"
slug: llm-as-a-judge
style: pokemon
category: evaluation
difficulty: intermediate
question: "What is LLM-as-a-judge and what biases does it have?"
tags: [llm-as-judge, position-bias, verbosity-bias, self-preference, mt-bench]
---

# LLM-as-a-judge: a Champion in the referee's chair

Human judges are slow, expensive, and get tired by the third battle of the afternoon.

So: put **Cynthia in the referee's chair.** She knows the game. They can grade a thousand
battles an hour. They never get tired.

And it works better than you'd expect — a Champion referee agrees with human referees about 80% of
the time, which is roughly how often **two humans** agree with each other. That's the honest
ceiling, and the Champion is basically at it.

## The six ways a Champion referee is wrong 🚨

**1. 🔀 They favour whoever went first.**

Show the same two battles in the opposite order and Cynthia sometimes picks the *other* winner. Same battles. Same referee. Different verdict.

> **The fix is not optional: judge both orders, every time.** If the verdict flips, call it a draw,
> because that's what it actually was.

**2. 📏 They reward the longer battle.**

A 40-turn Toxapex stall *looks* more impressive than a clean six-turn Garchomp sweep. The sweep
was better play. The referee gives it to the grind.

**3. 🪞 They favour Trainers who play like them.**

Cynthia rates the Garchomp players higher. She would. Not corruption — it just recognises its own
style as correct, because to it, it is.

> Never let a Champion be the sole referee of its own students. Get referees from other Leagues.

**4. ✨ They're dazzled by presentation.**

Confident calls, clean execution, decisive body language — all score well. Even when the underlying
decision was wrong.

The specific weakness: a Champion referee is **much better at judging style than at catching a
subtle mistake.** A beautifully-executed blunder beats a scruffy brilliancy nearly every time.

**5. 🗣️ They can be led.**

Tell the referee *"the left Trainer is the reigning champion"* before they watch, and watch their
verdict shift. They'll find reasons.

**6. 🧗 They can't grade above their own level.**

If the battle is more sophisticated than the referee, the verdict is a **guess dressed as a
number** — which is worse than an honest "I don't know," because it looks authoritative.

## How to run a referee properly ⚖️

```
   ✅ Both orderings. Always. Average them.
   ✅ Give a real checklist, not "which was better?"
   ✅ Make them explain their reasoning BEFORE naming a winner.
      (Verdict first, reasoning after = they rationalise. Much worse.)
   ✅ Show them a model answer if one exists — the Champion's own line in that
      exact position. Biggest single improvement
      available — a referee with a reference is a far better referee.
   ✅ Show a few correctly-graded examples first.
   ✅ Let them say "draw." Forcing a winner invents differences that
      weren't there.
   ✅ Check them against ~100 human verdicts and publish the agreement rate.
```

That last one is the discipline that separates a real referee from a comfortable one:

> 📌 **Your referee is itself a Trainer. So test it.** Measure how often it agrees with humans. Say
> the number out loud. Re-check it whenever you change the rulebook.

Most teams skip this and end up with a referee nobody has ever verified, producing numbers everyone
trusts completely.

## When not to use one ⛔

* 🎯 **When you can just check.** Did the Thunderbolt faint the Gyarados? That's a *fact*. A
  scoreboard cannot be
  charmed; a referee can. Never hire a referee for something you can look up.
* ☠️ **For anything that really matters** — a ban, a disqualification — without a human reviewing.
* 🧗 **When the battle is over the referee's head.**
* 🏋️ **As the thing you train against, unsupervised.** Train hard enough against any referee and
  your Trainer stops learning to battle and starts learning to *impress that referee* — long,
  polished, confident, and progressively worse. It's the same trap as any judge, and it's why
  referee-scored leaderboards drift toward verbose showmanship over time.
