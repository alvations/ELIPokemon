---
id: "125"
slug: speech-recognition
style: pokemon
category: multimodal
difficulty: intermediate
question: "How does modern speech recognition work?"
tags: [asr, whisper, ctc, rnn-t, log-mel, wer, streaming]
---

# Naming a Pokémon from its cry alone

Every species has one. Not a word — a *sound*, unmistakable to anyone who has heard it before.
The Pokédex can play them back to you, and if you have ever sat listening to the **Unown** cries
one after another you know how much information is packed into two seconds of noise.

Recognising a cry is the whole problem. And a cry arrives as an absolute torrent: thousands of
tiny slices of air pressure per second, carrying the species, the individual, the cave it is
echoing in, and the **Whismur** grumbling in the background, all layered on top of each other. You
want exactly one of those things.

## First, stop listening and start looking 👀

Nobody works on the raw sound. The Pokédex's own **Cry** screen already shows you the trick: it
draws the cry as a **picture** — a jagged shape with time running one way and pitch the other.

```
   the cry        ~~~/\~~/\/\~~~~~~/\/\~~~
        │
        ├─ chop into slivers about as long as a blink, overlapping
        ├─ ask of each sliver: how much low rumble? how much high shriek?
        └─ stack the answers side by side
                    pitch ▲  ░░▓▓██▓░░  ░▓██▓░   ░░▓▓░
                          │  ░▓███▓░░  ▒▓██▓▒   ░▓██▓░     ← Exploud's roar
                          │  ▓██▓░     ░▓█▓░     ▓██░
                          └──────────────────────────► time
```

📌 And the rungs of that pitch ladder are **not evenly spaced**. They are packed tightly down where
**Exploud** rumbles and spread far apart up where **Kricketune** shrills, because that is how an
ear actually works — fussy about low sounds, vague about high ones. It is the one piece of
old-fashioned biology left in an otherwise entirely learned machine, and it stays because it is
right.

Now it is a picture. Everything from questions 117 and 118 applies.

## The hard part is lining it up 🪢

Three thousand slivers of sound have to become four syllables, and **nothing anywhere tells you
which slivers made which syllable.** Three ways to solve it:

| | How it lines up | Can it answer mid-cry? |
| --- | --- | --- |
| 🏷️ **Label every sliver**, including "nothing here", then squash the repeats | brute force, no cleverness | ✅ yes |
| 🔗 **Label them while also tracking what has been said so far** | keeps a running memory of the transcript | ✅ yes |
| 📝 **Listen to the whole thing, then say what it was** | works out the alignment for itself | ❌ no |

The first is the simplest and has one real weakness: **each sliver is labelled in ignorance of its
neighbours.** It cannot know that "Char-mander" is a species and "Char-mandor" is not, because no
part of it is looking at the word. You end up bolting a dictionary onto the side.

The second fixes that while still answering as the cry unfolds, which is why it is what runs on
a Pokédex you actually carry.

The third is the most accurate and **cannot say a word until the cry has finished**. Fine for a
recording. Useless for a Pokédex held up mid-battle.

## The machine that hears things that were not said 👻

Here is the failure that catches everyone, and **Chatot** is the perfect illustration of why.

Chatot's whole nature is repeating what it has heard — its signature move, **Chatter**, was
literally built around recording a Trainer's voice and playing it back. A Chatot that has heard a
great deal will happily produce *something* whether or not anything was said to it just now.

⚠️ **Point a listener at an empty clearing and it will confidently transcribe a cry.** Not
gibberish. A fluent, plausible, entirely invented cry, often the same stock phrase it has heard a
thousand times before. It is not broken. You asked a machine whose only skill is producing
plausible transcripts to produce a transcript, and it did.

The fixes are unglamorous: **check there was a sound before you ask what the sound was**, throw
away segments the listener itself flags as silent, and watch for it repeating the same phrase over
and over — that loop is the tell.

## Counting mistakes honestly 🧮

Count the words it got wrong, the words it invented, and the words it dropped, against how many
there were. Fine. But know what that number hides:

* ⚖️ **Every word costs the same.** Losing "not" from *"do not switch in"* costs exactly what
  losing "the" costs. One of those loses you the match.
* 🔡 **Spelling and punctuation count as errors** unless you settle both sides first (question 115).
* 🌏 **Break it down by who is speaking.** A Pokédex assembled in **Kanto**, trained on Kanto
  Trainers, will report a fine average and then fail badly on a **Paldea** accent it has barely
  heard. The average was never wrong. It was hiding two very different machines.

## Three things people think are the same job and are not 🚧

* 🎭 **Who cried?** In a Double Battle two Pokémon roar at once. Separating *which* is a different
  machine entirely.
* ❓ **Punctuation and capitals** are usually bolted on afterwards, or simply absent.
* 🗣️ **Which language is this even in?** (question 108, one sense over) — a separate question,
  answered before the transcript, not during it.
