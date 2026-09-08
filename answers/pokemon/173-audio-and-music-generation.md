---
id: "173"
slug: audio-and-music-generation
style: pokemon
category: multimodal
difficulty: advanced
question: "How is audio and music generated, and what makes it harder than images?"
tags: [music-generation, audio-codecs, long-range-structure, tts, rights, evaluation]
---

# The Poké Flute only works if you play it right

Generating a Pokémon (question 137) and generating a **sound** run on much the same machinery. They
differ on one axis, and it changes everything:

**the ear will not let anything past.**

An oddly-drawn corner of a picture is something most Trainers never notice. A **wrong note** is
noticed by **everybody**, instantly, whether or not they can name what went wrong. The **Poké
Flute** either wakes the **Snorlax** blocking **Route 12** or it does not — there is no
approximately.

**Jigglypuff** knows this. **Sing** either puts them to sleep or it does not, and a Jigglypuff that
is nearly in tune has simply failed.

## Two ways to hold a sound 🎚️

```
   AS A ROW OF SYMBOLS                  AS A SHAPE TO UN-SCATTER
   ───────────────────                  ────────────────────────
   the sound ─► chopped into codes      the sound ─► drawn as a picture of pitch
             ─► predict the next one              ─► un-scattered (question 137)
                                                  ─► played back

   reuses every trick from writing;     no chopping, no codebook to lose detail to;
   the chopping is a floor on quality   harder to steer with a plan
```

The first dominates, because everything already built for predicting the next word applies
unchanged. The second reaches beautiful fidelity for a fixed length.

## The hard part is the *shape* of the whole piece 🎼

A **Kricketune**'s song has structure at four scales at once: the **timbre** of a single note, the
**beat**, the **phrase**, and the **form** — the part that comes back. The **Pokégear**'s radio
channels are built on that last one; **Buena's Password** and **Oak's Pokémon Talk** are
recognisable within two seconds because they return to something.

⚠️ A machine holding a few thousand slots sees **a few seconds**.

📌 So you get the characteristic failure: **locally lovely, globally aimless.** It wanders. It never
returns to the tune it opened with. And it does not end — **it stops**, which is a completely
different thing.

This is question 157's long-battle drift wearing different clothes: plan the shape first and fill in
the sound second, and it improves. It does not go away.

## Making a Pokémon speak is a different job 🗣️

Producing a **cry** shares the machinery and is judged on other things entirely: can you tell it
was a **Gyarados** and not an **Exploud**, does it still sound like **that** Gyarados, and is the
feeling right (question 138). The frontier is **control** — *"say it warily"*, *"say it faster"* —
because the raw sound quality is largely solved.

⚠️ And everything in question 153 about copying a voice applies **more** forcefully here, not less.
There, at least, some Pokémon originally cried and could in principle have agreed. Conjure a voice
from a written description and **there was never anybody to ask.**

## The rights question is not a footnote ⚖️

Music generation sits on top of an argument that is being fought in courtrooms right now. Positions
a serious team should actually hold:

* 📜 **Know where your material came from and what you are allowed to do with it.** *"It was lying
  around on **Route 3**"* is a position, and one you will have to defend — and picking up an item
  that was plainly somebody's is how a **Rocket Grunt** describes their afternoon too.
* 🎨 **"In the style of a named composer" is the sharpest edge there is.** Legally in several places,
  and ethically everywhere. A great many providers refuse those prompts, and that is not timidity.
* 🔊 **Mark what you generate** (question 166). Sound holds a mark better than pictures do, and this
  is the case that most needs one.
* 🤝 **Support opting out** — and better, license the material and share what it earns.

## Judging it 🏅

There is a standard measure that compares a heap of generated sound against a heap of real sound. It
carries every weakness from question 137 **plus a worse one**: it is barely sensitive to **structure**
— which is the exact failure that matters most. ⚠️ A piece that wanders for three minutes and never
comes home can score perfectly well.

So test the specific things:

* 👂 **Ask Trainers**, rating *"is it good"* and *"is it what I asked for"* as **two** questions.
* 🔁 **Does the tune come back?** Is the tempo steady? Is it still in the same key at the end?
* 🎺 **Is it still the same instrument** three minutes in — the same way you check the **Charizard**
  is still a Charizard and has not drifted into a **Charmeleon** in question 157?
* 🗣️ **And for cries: can a listener actually tell what it was**, measured by writing it down
  (question 125), alongside whether it sounded natural.
