---
id: "091"
slug: self-supervised-learning
style: pokemon
category: training
difficulty: intermediate
question: "What is self-supervised learning and why did it beat supervised pretraining?"
tags: [self-supervised, pretext-task, masked-modelling, contrastive, labels]
---

# Self-supervised learning: the footage grades itself

## 😩 The old way

To train a Trainer, you needed **labelled** footage. Someone had to sit and watch every battle and
write down what it demonstrated.

> *"This match shows a Politoed Rain team. This one shows a Bronzong Trick Room setup. This one
> shows a Ferrothorn pivot."*

Expensive. Slow. Boring. And you'd never get more than a few hundred thousand of them, because
**people have to do it.**

## 🌾 The new way

Take **every battle ever recorded** — millions of hours, completely unlabelled — and pause it
mid-turn:

> **"What happens next?"**

The answer — *they switched to Ferrothorn* — is **already on the tape.** Play three more seconds
and you know.

📌 **The footage grades itself.** Nobody labels anything. Ever.

```
   😩 LABELLED                          🌾 SELF-GRADING
   ──────────                           ───────────────
   (battle, "Rain team")                 pause → "what's next?"
   Someone wrote that.                   → play on. There's your answer.

   Bottleneck: 👤 people                 Bottleneck: 🖥️ compute
   ~a few hundred thousand               ~every battle ever recorded
```

## Why this won 🏆

**1. 🚪 The gate came off.**

Labelled footage was capped by how many people you could hire. That cap is now **gone.** And since a
Trainer's strength tracks how much footage it studied, removing the cap changed everything.

**2. 🍖 The lesson is far richer.**

Think about what each actually teaches:

> **A label** — *"this match shows a Rain team."* That's one fact. Ten bits, roughly.
>
> **Predicting the next turn** — you must know the type chart, the items, the abilities, the
> Trainer's plan, the field conditions, and what a competent player would do. **Everything.**

The label teaches one categorisation. The tape teaches the whole game.

**3. 🔭 Labels narrow the mind.**

A Trainer drilled to sort battles into a thousand categories learns whatever distinguishes **those
thousand categories** — and quietly discards everything else as irrelevant.

Self-grading footage never pre-decides what matters. So the Trainer learns everything, and can be
pointed at any job afterwards.

**4. 💰 Doubling is free.** Twice the labelled footage means twice the annotation bill. Twice the raw
footage is a storage problem.

## Different self-grading drills 🎯

* ⏭️ **"What happens next?"** — the strongest. Every single turn of every match is a graded
  question. *Drizzle went up; what comes in?* (Kingdra. Every time.)
* 🙈 **"I've covered three turns. What were they?"** — you get to use context from *both* directions,
  which is genuinely useful. But you only cover about one turn in seven, so **six out of seven turns
  teach nothing.** Far less signal per hour of footage.
* 🧩 **"Here's 25% of a photo of the field. Draw the rest."** For images you have to hide **most** of
  it, because a picture is so redundant that hiding a corner is trivially easy.
* 🔍 **"Two clips — same battle or different?"** Learn what makes battles similar without ever naming
  anything.

## The two catches ⚠️

**🕳️ The drill must have no shortcut.**

Early attempts failed exactly here. *"Is this clip upside down?"* — the Trainer learns to spot the
scoreboard's orientation and answers perfectly, having learned **nothing about battling.**

📌 **A good drill is one you genuinely cannot pass without understanding.** You cannot predict the
next turn by spotting a watermark. That's why the good drills are good.

**🗑️ The bottleneck moved, it didn't vanish.**

Once footage is unlimited, the question stops being *"can we get more?"* and becomes **"which of this
is worth watching?"**

A million hours of terrible players teaches your Trainer to play terribly. So the real work — the
work everybody now spends their time on — is **curation**: filtering, deduplicating, and deciding
what makes the cut.

You didn't remove the human effort. You **moved** it, from labelling every match to deciding which
matches to keep. Which is a far better trade, and still a lot of work.
