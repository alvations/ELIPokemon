---
id: "155"
slug: sign-language-translation
style: pokemon
category: translation
difficulty: advanced
question: "Why is sign language translation not just video captioning?"
tags: [sign-language, glosses, non-manual-markers, avatars, deaf-community, low-resource]
---

# Pikachu says one word. The rest is ears, tail and stance.

The first thing to get right, and the thing most people get wrong: **this is a language, not a
picture of one.**

**Pikachu** has one syllable. Everything else — refusal, warning, delight, *"it went that way"* —
is carried by the ears, the tail, the set of the shoulders, whether the cheeks are sparking. A
Trainer who has raised one reads all of it fluently and could not write down how.

And it is not one system. **Growlithe** says it with its ears and its tail. **Umbreon** says it with
the rings and with how still it holds itself. **Kadabra** does not move at all. **Mimikyu** hides
the whole thing under a rag. Reading one of them fluently teaches you almost nothing about reading
another.

📌 And crucially: **it is not a code for the spoken command.** It has its own grammar. Two Trainers
from two regions who both speak the same human language may have Pokémon whose signals do not
transfer at all. Being neighbours in one language says nothing about being neighbours in the other.

So this is **translation between languages**, and everything in questions 129 to 152 applies — plus
a set of problems that only exist for a language spoken in three dimensions, all at once.

## Why it is not "describe the video" 🎞️

```
   A SPOKEN COMMAND   one channel. one thing at a time. left to right.

   A POKÉMON          paws:     the actual sign
                      ears/face: whether it is a QUESTION, a REFUSAL, how strongly
                      body:     who it is speaking as right now
                      space:    it puts things in places and points back at them
                      — SIMULTANEOUSLY —
```

* **🙉 The face is grammar, not mood.** **Growlithe**'s ears forward or flat is not decoration — it
  is the difference between a statement and a question, and between a thing and **not** that thing.
  ⚠️ A machine that watches the paws and ignores the ears is missing the equivalent of negation, and
  it will confidently output **the opposite meaning** while looking entirely reasonable. It is the
  **Confuse Ray** of translation errors: everything still moving, all of it aimed the wrong way.
* **📍 Space is the pronoun system.** A **Machamp** puts the **Gyarados** *over there* and then
  refers back by pointing. That is not gesture — that is how it says *"it"*. A flat left-to-right
  model has nowhere to keep it, and with **four arms** it may be holding two references at once.
* **🖐️ And it can say two things at once.** Two paws, two pieces of information. Writing is a
  single file.

## Writing it down as words loses the language 📝

The usual shortcut is to transcribe each sign as a capitalised word — a tidy row of tokens you can
train on.

⚠️ It is **lossy in exactly the places that carry the grammar**: the ears are gone, the
simultaneity is gone, and the whole thing has been chopped up the way the *spoken* language chops
things up rather than the way this one does. Pipelines built on that intermediate row of words are
being replaced by ones that go straight from the video, partly because the transcription is
expensive expert work and partly because **the transcription is where the grammar died.**

## There is almost no material 📉

Thousands of examples, where ordinary translation has hundreds of millions. Narrow subject matter.
Usually filmed under good light, from the front, one signer, plain background — and real
communication happens at angles, half-hidden in **Tall Grass**, in a **Sandstorm**, and differs
between individuals, regions and ages. A **Vulpix** raised in Kanto and one raised in Alola do not
hold themselves the same way.

## And this one is not only a technical problem 🤝

Here the Pokémon framing has to step aside, because the point is about people.

Sign languages belong to Deaf communities, and this data is **video of identifiable people**. The
field's own guidance is emphatic and worth repeating plainly: **involve Deaf researchers and
signers from the beginning**, treat scraped video as disqualifying, and be honest about what you are
building.

That last part matters most for **signing avatars**. The recurring objection is not that they are
imperfect — it is that they are frequently **unusable**, missing the facial grammar entirely, and
deployed as a cheaper substitute for human interpreters rather than as something additional.
📌 Evaluate with Deaf signers, not with automatic scores and not with hearing observers, and be
straight about whether you are adding something or removing someone.

## Judging it 🏅

⚠️ Scoring against that row of capitalised words is the field's most-criticised habit: it measures
agreement with the lossy middle step, not with the meaning.

Score against real translations instead, with all the caveats from question 129; test whether people
**understood**; and say who signed the data and who did the judging.
