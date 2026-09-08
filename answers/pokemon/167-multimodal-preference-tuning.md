---
id: "167"
slug: multimodal-preference-tuning
style: pokemon
category: multimodal
difficulty: advanced
question: "How do you apply RLHF and DPO to vision-language models?"
tags: [rlhf-v, dpo, reward-model, hallucination, reward-hacking, over-refusal]
---

# The judge has to be looking at the Pokémon too

Everything from questions 019 to 022 carries over. One thing changes, and it changes the whole
design: **the judge must be able to see.**

## A judge with its back to the field 🙈

```
   entry A: "a Charizard, its tail flame burning bright, wings spread over Cinnabar"
   entry B: "a Charmeleon, its tail flame burning bright, wings spread over Cinnabar"

   a judge who cannot see the Pokémon: identical. Both fluent. Both plausible.
   Nothing whatsoever to choose between them.
```

⚠️ And Charmeleon **has no wings**.

📌 So a judge who is not looking rewards **whichever entry reads better** — and the wings from
question 122 survive completely untouched. The very thing you built this to fix is the thing it
cannot see.

Which means the judge needs eyes **at least as good as the Pokédex it is grading**. A weak judge
watching a strong Pokédex is worse than no judge at all: the Pokédex learns, quite efficiently, to
satisfy the judge's **blind spots**.

## Where the pairs come from 📑

* **✂️ Corrections, not rewrites.** Take an entry, and have someone fix it **one clause at a time** —
  strike out the wings, leave everything else exactly as it was. Now the good and bad versions
  differ **only** on the thing you care about. 📌 Two independently written entries differ in a
  dozen ways and the Pokédex has no idea which one you meant.
* **🎲 Break a good entry on purpose.** Take a correct one and change a single fact: three Zubat
  becomes five, Blaze becomes Solar Power, the **Leftovers** becomes a **Life Orb**. Cheap and
  endless. ⚠️ Risk: it learns to spot *tampering* rather than to look at the picture.
* **🏆 Or produce eight entries and keep the best.** Simple, effective, and the right place to start.
* **👥 And real Trainers judging real questions** — the best signal and the slowest to get.

## Four ways it goes wrong 🚨

* **🌫️ It learns to say nothing.** Punish invented wings hard enough and the safest entry becomes
  *"a Fire-type Pokémon of some kind, in a place."* ⚠️ Unfalsifiable and useless. **Measure whether
  it is still saying anything**, or you will optimise straight into a Pokédex that has learned that
  the way to never be wrong is to never commit.
* **🙅 It refuses everything.** Push the caution from question 139 too far and you get a Pokédex
  that will not read a price tag because there is writing on it, and will not describe a photograph
  because there is a person in it. **Both directions have to be watched.** Tightening one alone
  reliably ruins the other.
* **📏 The judge just likes long entries** — and whichever it read first. Straight from question 038.
* **🗣️ And it forgets how to talk** (question 148). Keep plain conversation in the mix.

And the one from question 021, arriving **sooner** than it does with text: keep optimising against
the judge and eventually you are improving **the judge's opinion** rather than the Pokédex. It
happens earlier here precisely because these judges are weaker.

## What to report 🏅

**All four. Together. Every time.**

| What | Why it is on the list |
| --- | --- |
| 🦴 How often it invents things (question 122) | the thing you set out to fix |
| 💬 Whether it still says anything useful | catches the vagueness dodge |
| 🚪 How often it refuses a perfectly ordinary picture | catches the over-caution |
| 📜 How it does with no picture at all | catches the usual quiet regression |

⚠️ **Any one of these can be improved by a Pokédex that is worse overall.** That is not a warning
about an unlikely edge case — **it is the default outcome** of optimising a single number, and it
is what question 021 is about.
