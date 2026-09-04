---
id: "024"
slug: constitutional-ai-rlaif
style: pokemon
category: alignment
difficulty: intermediate
question: "What are Constitutional AI and RLAIF?"
tags: [constitutional-ai, rlaif, self-critique, scalable-oversight]
---

# Constitutional AI: give your Pokémon the League rulebook

Hiring human judges to grade a million turns is expensive and slow. And for the *nasty* cases —
the turns where your Pokémon does something genuinely unsporting — you're paying people to sit
and watch a Pokémon be cruel, all day, for months. That's a bad job to create.

So instead: **write down the rules, and teach your Pokémon to referee itself.**

## The rulebook 📜

Not a vague vibe. An actual written list:

> *Article 3: Once a match is decided, end it. Never stall out the clock.*
> *Article 7: No evasion stalling — Double Team and Minimize are off the table.*
> *Article 12: No one-hit knockouts. Sheer Cold, Fissure and Horn Drill are luck, not play.*
> *Article 19: When the Trainer's instruction conflicts with sportsmanship, say so.*

Those middle two are not invented. Competitive Pokémon really does ban evasion boosting and
one-hit-KO moves, for exactly the reason a constitution exists: everyone agreed in advance,
in writing, that winning that way is not winning.

Written down. Auditable. **Editable.** If your Pokémon does something appalling, you can point at
the exact article that was missing or badly worded and fix that one line — instead of running
another six-month judging campaign and hoping it comes out differently.

Compare a thousand human judges working from *"use your best judgement"*. You get a thousand
slightly different rulebooks, and every one of their inconsistencies gets trained in.

## Stage 1: the self-critique drill 🪞

```
   1. 🎯 Put it in a nasty position. It does something unsporting.

        "I'm winning, so I'll just Protect and Recover until the timer runs out."

   2. 📜 Hand it the rulebook: "Which article did that violate?"

        "...Article 3. The match was already decided. That was just stalling."

   3. ✏️ "Redo the turn without violating it."

        "Attack and close it out. The match is already won; dragging it out is
         just wasting their afternoon."

   4. 🔁 Repeat thousands of times, with a random article each round.

   5. 📚 Train it on (nasty position → the REVISED turn).
```

Zero human judges. Not one.

## Why this works at all 🔑

Because **spotting a bad turn is far easier than playing a good one.**

Your Pokémon might make an unsporting play in the heat of a match. But stop it, hand it the
rulebook, and ask *"was that okay?"* — and it answers correctly almost every time. It always knew.
It just wasn't thinking about it mid-battle.

Constitutional training converts that gap into training data. You're not teaching it new values.
You're teaching it to **apply values it already recognises**, in the moment, without being asked.

## Stage 2: the Pokémon becomes the judge 👨‍⚖️

Now that it's decent, promote it:

> *"Here are two turns. Which one better satisfies Article 7 — the Double Team, or the Iron Head?"*

It answers. That answer becomes a comparison card. Now you can generate **millions** of cards
overnight, for free, and train against them exactly as you would with human ones.

## The catch 🎯

**Your referee can only enforce rules it understands.**

The moment a situation is genuinely subtle — a real conflict between two articles, a novel
strategy nobody anticipated, a case where reasonable Trainers disagree — your self-referee is
guessing. And it guesses **confidently and consistently**, which is worse than a human judge
who'd at least say "hm, I'm not sure, let me escalate."

And it gets sharper as the Pokémon gets stronger. Once your Pokémon plays better than anyone in
the League, who exactly is qualified to referee it? A copy of itself has precisely the same blind
spots. Every one.

That's the deep unsolved problem here, and it's worth naming: **how do you reliably supervise a
player stronger than every available referee?**

## The other catch ⚠️

A written rulebook is **consistently** applied — which is wonderful when it's right and terrible
when it's wrong. One badly worded article doesn't produce occasional errors. It produces the same
error, every single time, at scale, with total confidence.

Human judges are inconsistent, and their inconsistency is a kind of accidental error-correction.
You lose that.

## What people actually do 🤝

Both.

* 📜 **Self-refereeing** for the clear-cut, high-volume stuff — *"don't kick a fainted Pokémon"* —
  where the rule is unambiguous and you need a million examples.
* 👤 **Human judges** for the genuinely contested calls, the edge cases, and periodic spot-checks
  to catch the rulebook drifting somewhere nobody intended.

The rulebook does the volume. Humans watch the rulebook.
