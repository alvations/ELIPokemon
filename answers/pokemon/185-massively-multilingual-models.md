---
id: "185"
slug: massively-multilingual-models
style: pokemon
category: translation
difficulty: advanced
question: "What does it actually mean to say a model supports 200 languages?"
tags: [nllb, coverage-claims, long-tail, per-language-reporting, moe, deployment-threshold]
---

# Seen is not caught

Open a Pokédex and it gives you **two numbers**. **Seen** and **caught**. Nobody who has played for
an afternoon confuses them.

You have *seen* **Mewtwo** through the door of **Cerulean Cave**. You have *seen* **Articuno** over
the **Seafoam Islands**. Neither is on your team. Meanwhile you have caught eleven **Zubat**, six
**Magikarp** and a **Rattata** you cannot get rid of.

*"Supports 200 languages"* is the **seen** number, printed on the box as though it were the caught
one.

## What the number is hiding 📊

```
   200 languages "supported"

   ~15    genuinely caught: on the team, trained, you would enter a tournament with it
   ~40    caught with caveats: in the PC, fine for the gist, not for anything that matters
   ~100   seen through the trees: fluent output, relationship to the original anybody's guess
   ~45    a Ditto wearing the species name: confidently wrong often enough to do harm

   the number on the box is 200. The number a Trainer can rely on is the first one.
```

⚠️ And the tail is **not a slightly worse version of the head**. It fails **differently**: it hands
you the Kantonian entry when you asked for the Alolan one (question 136), it invents (question 122),
and — the cruel part — **a speaker of that language cannot easily tell the difference**, because
fluency survives long after accuracy has gone. It reads beautifully right up until you check it.

## What genuinely helps 🔧

* **🧠 Give it more room, and route by language.** The crowding from question 103 is a **capacity**
  problem, so the fixes are capacity fixes: specialists that only wake for certain languages, a
  **disc per language** (question 110), or simply a bigger Pokémon. Each buys back part of the tail.
* **🔗 Get direct pairs.** Stop routing everything through **Kanto** (question 130) — **Johto** to
  **Paldea** should not have to change trains at **Saffron City**. This was substantially what the
  serious efforts contributed: not a cleverer model, **more honest data**.
* **⚖️ Do not let the big regions drown the small ones** (question 104) when choosing what to train
  on.
* **🔤 And give the tail an alphabet it can actually use** (questions 102, 112), rather than shredding
  it into fragments before it starts.

## The reporting standard to hold yourself to 📋

* **📈 Publish the score for every language. Always.** ⚠️ An average across 200 is decided entirely
  by the biggest fifteen and **summarises nothing**. Publish the spread, and publish the worst tenth.
* **📚 Say what you tested each one on.** For most of the tail it is one narrow standard set
  (question 130) — say that, plainly.
* **👥 Say which were judged by actual speakers** and which only by a machine. ⚠️ For a tail
  language, **the judging machine is itself untrustworthy** (question 129), so an unchecked score
  there is a number, not evidence.
* **🗂️ And put those four tiers in the documentation**, not in a footnote at the bottom.

## The question that actually matters 🎯

Not *"do we support this language"* but: **"what could a speaker of it safely rely on this for?"**

Getting the gist of an incoming message is a completely different bar from translating a dosage
(question 187).

📌 So set the bar **per use**, measure **per language** against it, and **show the tier in the
product**. ⚠️ A system that presents the identical interface for a language it handles beautifully
and one it handles badly has **handed the entire risk to the user** — and the user has no way to
know they are holding it.

And for some languages, the right answer is **not yet**, said out loud, with a reason.

📌 That is more respectful of a speaker than fluent, confident nonsense — and it is the same
honesty as a Pokédex that shows **seen: 200, caught: 15** rather than rounding the second number up
to the first.
