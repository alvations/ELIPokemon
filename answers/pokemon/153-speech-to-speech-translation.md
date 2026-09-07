---
id: "153"
slug: speech-to-speech-translation
style: pokemon
category: translation
difficulty: advanced
question: "How do you translate speech into speech while keeping the speaker's voice?"
tags: [s2st, voice-preservation, cascade, discrete-units, prosody-transfer, consent]
---

# It should still sound like your Pikachu

Cry in, cry out, across a language border — and, increasingly, **in the same Pokémon's voice.**

Every one of those requirements fights the others.

## What each stage throws away 🪣

```
   THE LONG WAY   the cry ─► write it down ─► translate ─► say it aloud
                                 ▲                            ▲
                     WHOSE voice dies here.       and the new voice invents its
                     So does the alarm in it.     own emotion out of nothing —
                     Nothing later can            cheerful, because that is
                     get either back.             what it always is.

   THE SHORT WAY  the cry ─► straight through ─► a cry
                  the voice and the feeling survive, if what you
                  carry them in was built to hold them (question 138)
```

The long way still runs almost everywhere, because each stage has mountains of practice material
and the short way does not. But **the long way has no memory of your Pokémon.** A frightened
Pikachu goes in and a chirpy stranger comes out saying the right words.

## Decide, out loud, whose voice comes out 🎙️

Three different products, and people build one while promising another:

* **🔊 Any voice at all.** A stock voice in the target language. Simplest — and it makes the
  translation *obviously a translation*, which is sometimes exactly right.
* **🎚️ A voice roughly like theirs.** Similar pitch, similar size of Pokémon. Recognisably a
  **Snorlax** rather than a **Joltik**, without being anyone in particular.
* **🎭 Their actual voice.** ⚠️ And this is a **consent question before it is an engineering
  question** (question 138). **Chatot** is the warning the games already wrote: **Chatter** recorded
  a real voice and played it back. The Pokémon must have agreed, the output should carry a mark
  saying it was made, and the machine must **refuse** a voice it cannot verify.

📌 And separately from *whose* voice: **how it was said.** A flat rendering of an urgent cry is not
a slightly worse translation — **it is a wrong one.** Pikachu's whole vocabulary is one word said
differently, and a machine that levels the tone has translated nothing at all.

## Where it actually breaks 💥

* **📏 The new cry is a different length.** Longer or shorter than what went in (question 144). Live,
  that piles onto the delay (question 143). Over a battle recording it is a hard wall
  (question 154).
* **🧨 Three stages, and each one trusts the last.** A mishearing becomes a confident
  mistranslation becomes a beautifully articulated cry meaning something else entirely. **No stage
  downstream can tell**, because each of them is doing its job perfectly on the input it was given.
* **😬 Real Trainers stumble.** *"Use Thunder— no, wait—"*. Translate the stumble word for word and
  it is wrong. Delete it silently and you may have deleted the point: **a hesitation before "yes"
  is information.**
* **🔀 And they switch languages mid-sentence** (question 107), which breaks anything that decided
  which language this was before it started.

## Judging it 🏅

Scoring the written-down version in the middle is necessary and **not the product**. Add:

* 🔁 **Listen to what came out, write *that* down, and score it.** This catches everything the
  middle-of-the-pipeline score cannot — and it drags in the mishearings of whatever did the
  listening, so **say which listener you used.**
* 👤 **How much it still sounds like the same Pokémon**, if you claimed it would.
* 👂 **Whether Trainers think it sounds like a Pokémon at all.**
* ⏱️ **And the delay**, always, for anything happening live (question 143).
