---
id: "122"
slug: multimodal-hallucination
style: pokemon
category: multimodal
difficulty: intermediate
question: "Why do vision-language models hallucinate objects, and how do you measure it?"
tags: [hallucination, pope, chair, language-prior, contrastive-decoding, grounding]
---

# The Pokédex gives Charmeleon wings

Point it at a **Charmeleon**. Orange. Bipedal. Flame on the tail. The entry comes back fluent and
confident and somewhere in the third sentence it mentions the wings.

Charmeleon does not have wings. **Charizard** has wings — that is the single most obvious thing
that happens at the last evolution, the moment it stops being a ground-bound Fire type and
becomes Fire/Flying. The Pokédex knows this. It has simply been talking for three sentences about
an orange flame-tailed lizard, and in everything it has ever read, those get wings by the end.

Nothing malfunctioned. **It was built to produce a plausible entry, and there is no part of
"plausible" that means "and check".**

## Three reasons it happens 🧠

**1. 🗣️ The voice is enormous and the eye is a wire.** The talking half read every Pokédex entry
ever written. The seeing half connects to it through a thin translator (question 117). When the
picture is unclear, the cheapest thing available is whatever the voice *would have said anyway* —
and the voice is very, very fluent.

**2. 🦇 Things that always go together, go together.** Every cave in Kanto has **Zubat** in it. Mt.
Moon, Rock Tunnel, Seafoam Islands — it is a joke among Trainers precisely because it is true. So
show a Pokédex a photograph of a cave, any cave, and it will tell you about the Zubat. There is no
Zubat. There is a *cave*, and the Zubat came free with it.

**3. 🔍 Sometimes it genuinely could not see.** The thing was four tiles across after the whole
cavern got squashed into one frame (question 121). That is not invention, it is guessing, and no
amount of clever wording fixes it — only walking closer does.

## It gets worse the longer it talks 📉

```
   sentence:      1 ────────────────────────────────────────────► 8

   what it saw  ████████████▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   its own voice░░░░▒▒▒▒▓▓▓▓████████████████████████████████████

   sentence 1: "a Fire-type Pokémon with a flame on its tail"   ← looking
   sentence 8: "...and it uses its wings to reach great heights" ← reciting
```

📌 Every sentence it produces becomes something the *next* sentence listens to. Eight sentences
in, it is mostly listening to itself. **Ask for a paragraph and you have asked for hallucination.**

## How to actually catch it 🎯

Do not ask it to describe things and read the results hopefully. **Ask balanced yes-or-no
questions, half about things that are there and half about things that are not**, and set the
absent ones three ways:

| The absent thing you ask about | What it tests |
| --- | --- |
| 🎲 **Anything at random** — "is there a Lapras here?" | the floor. Easy. |
| ⭐ **Something very common** — "is there a Pidgey here?" | whether sheer familiarity is enough to make it say yes |
| 😈 **Something that always comes with what IS there** — "is there a Zubat in this cave?" | the real test |

⚠️ **The gap between the first row and the last is your number.** A Pokédex can look excellent on
random absences and fall apart the moment the absent thing is one that belongs.

Two ways to fool yourself while measuring:

* 🙋 **Unbalanced questions.** If eight of your ten questions have "yes" as the answer, a Pokédex
  that says yes to everything scores eight out of ten and has seen nothing.
* 😊 **It wants to agree with you.** A Pokédex tuned to be helpful will confirm a leading question
  out of sheer politeness. Ask both ways round — *"is there a Zubat?"* and *"there is no Zubat,
  correct?"* — and report the difference.

## Fixes, best first 🔧

* **🔭 Walk closer, first, before anything else.** An enormous share of what gets called
  hallucination is unresolvable detail in a costume.
* **⚖️ Train it on its own mistakes, in pairs.** Take the entry with the invented wings and the
  entry without them, and teach it which one you prefer (question 022). This is the standard
  answer and it works.
* **🧢 Cap the lens and ask again.** This is the elegant one. Put the cap on, ask the identical
  question, and whatever it *still* says confidently was never coming from the eye at all — that
  is the voice's habit, laid bare. Subtract exactly that from the real answer. It costs you a
  second look and it removes precisely the wings.
* **👉 Make it point.** Do not accept "there is a Zubat". Demand *where* — which tile, which corner
  of the cave. **A claim that has to point somewhere is far harder to invent**, and when it is
  wrong you can see that it is wrong.
* **✂️ Ask for less.** Two sentences hallucinate less than eight. If the job allows it, take the
  two.

And two that sound right and do very little: **telling it not to make things up** — it was never
lying, it was reciting — and **asking it repeatedly to see if it agrees with itself.** It will. A
strong habit is perfectly consistent. Every single time, it will give Charmeleon the wings.
