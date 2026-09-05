---
id: "051"
slug: in-context-learning
style: pokemon
category: prompting
difficulty: core
question: "What is in-context learning and how does it work mechanistically?"
tags: [in-context-learning, few-shot, induction-heads, task-location]
---

# In-context learning: show three examples, no training required

You want your Trainer to rate teams. You don't send it anywhere. You just show it three examples:

```
   🏆 Rain team, Politoed + Swift Swim  →  "S tier"
   😐 Six Magikarp                       →  "F tier"
   ⚔️ Trick Room, Bronzong + Rhyperior   →  "A tier"

   🤔 Sun team, Torkoal + Venusaur       →  ?
```

And it says **"A tier."** Correctly.

No camp. No held item. No training of any kind. Three examples in the conversation and it's doing a
job it wasn't doing thirty seconds ago.

## The experiment that changed how people think about this 🤯

Someone tried it with **deliberately wrong labels**:

```
   🏆 Rain team, Politoed + Swift Swim  →  "F tier"   ← WRONG
   😐 Six Magikarp                       →  "S tier"   ← WRONG
   ⚔️ Trick Room, Bronzong + Rhyperior   →  "F tier"   ← WRONG

   🤔 Sun team, Torkoal + Venusaur       →  ?
```

**It still said "A tier."** Still correct. Barely worse than with the right labels.

So it was **not learning from your examples.** If it were, garbage in would mean garbage out.

## What the examples are actually for 🗝️

Your Trainer **already knew how to rate teams.** It watched a million battles at the Battle Tower. Team rating was in there the whole time.

Your three examples aren't teaching. They're **pointing**:

* 🏷️ *"The answer is a tier letter."* (Not a paragraph. Not a number out of ten.)
* 📥 *"The input is a team composition."*
* 📐 *"The shape is: team, then arrow, then letter."*
* 🎯 *"Of the thousand things you know how to do with a team, do THIS one."*

You're not teaching a skill. You're **selecting one from a menu it already has**, and specifying the
format you want it back in.

That's why the labels can be wrong. Wrong labels still show the shape, still show the label set,
still point at the right job.

📌 One caveat: show it **hundreds** of examples and it does start genuinely learning from them, and
then correctness matters again. Three examples point. Three hundred teach.

## The machinery: pattern-copying 🔁

Underneath is a specific ability your Trainer developed on its own:

> **"That happened before. What followed it?"**

```
   Earlier: ... 🌧️ rain went up → 💨 Swift Swim Kingdra came in ...

   Now:     ... 🌧️ rain goes up → ?

   The instinct: "I've seen this. Kingdra followed. Expect Kingdra."
```

Applied to your three examples, the pattern it spots isn't about tiers at all — it's
**`team → letter`**. Match the shape, fill in the content.

And here's the striking bit: this instinct **appears suddenly during training.** Watch a Trainer
learning and there's a specific window where it just... clicks. Before: no ability to pick up
patterns from examples. After: fully able. One of the only clean "it evolved" moments anyone has
found.

## What this means for you 📋

* 📐 **Format matters more than correctness.** Same separators, same casing, same shape in every
  example. Inconsistent formatting is the most common cause of a few-shot prompt behaving oddly.
* 🎨 **Show the exact output shape you want.** This is what examples are genuinely best at. Want JSON?
  Show JSON. Don't describe it — show it.
* 🏷️ **Include every label.** If "C tier" exists and no example shows one, your Trainer may not
  believe it's available.
* 🔚 **The last example counts most.** Recency. If your results shift between runs of the same
  prompt, try reordering — you'll often find that's the whole story.
* 📊 **Eight to thirty examples** covers most tasks. Fewer isn't enough shape; more is diminishing
  returns until you reach the hundreds.
* 🎯 **Pick examples that resemble the current question.** Rating a Torkoal Sun team? Show Sun
  examples, not
  a random three.
