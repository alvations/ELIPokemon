---
id: "138"
slug: speech-language-models
style: pokemon
category: multimodal
difficulty: advanced
question: "How do you build a model that listens and speaks, rather than reads and writes?"
tags: [speech-llm, audio-tokens, cascaded, end-to-end, duplex, prosody, voice-cloning]
---

# Pikachu only ever says one word

Everything Pikachu has ever communicated — alarm, refusal, delight, *"behind you"*, *"I am not
getting in the Ball"* — has been carried by a single word said differently.

Write it down and you get **"Pika."**

Every time. Identical on the page. And whatever it actually meant is gone.

That is the entire argument between the two ways of building a Pokémon that listens and answers.

## Two designs 🎙️

```
   THROUGH MEOWTH
   the cry ─► write it down ─► think in words ─► write a reply ─► say it aloud
                     ▲                                ▲
              everything that was not the WORD dies right here,
              and no later stage can get it back

   DIRECTLY
   the cry ─► straight into the reasoning ─► straight back out as a cry
                     ▲
              alarm, hesitation, who was talking, two Pokémon at once,
              the wobble that meant it was frightened — all of it survives
```

**Meowth** is the first design, and it is the sensible one to build. It converts everything into
human words, and you can bolt it together out of parts you already have: something that writes
cries down, something that thinks in words, something that cries aloud. You can **read the
transcript**, which makes it debuggable. You can **check the transcript**, which makes it safe.

And it throws away the message. Pikachu's terror and Pikachu's delight arrive at the thinking part
as the same four letters.

The second design keeps all of it and is harder in every way: harder to train, harder to inspect,
and much harder to keep safe — because the thing you need to check is **no longer written down
anywhere**.

## Chopping a cry into pieces 🧩

The thinking part needs a *sequence*, so the cry gets chopped into tokens. And there are two quite
different kinds, which people mix up constantly:

* **📝 What was cried.** Few tokens, slow rate, enough to reason over.
* **🔊 How it sounded.** Which Pokémon, what mood, what cave it echoed in. Many tokens, fast rate,
  and you cannot make a convincing cry without them.

Almost everyone reasons over the first and synthesises with the second, because the second is
ruinously long. A single minute of **Exploud** at full fidelity runs into tens of thousands of
slots before anything interesting has been said.

## Talking over each other 🗣️

Real conversation is not tidy. Nobody waits for a full stop.

A polite design waits for the cry to finish, thinks, then answers. A **real** one is doing both at
once — still listening while it is still crying, able to stop mid-word because something changed.
That is what makes **interruption** work, and it changes what the thing has to learn: not just what
to say, but **when to say it, and when to stop.**

Think of a Pokémon locked into **Uproar** — three solid turns of noise, nothing else getting a word
in. That is the failure mode of a design that cannot listen while it speaks.

⚠️ **And the clock is merciless.** A Trainer notices a pause of about a third of a second. That
budget has to cover hearing the cry, deciding, *and* producing the sound — which is why answering
in a stream, starting before you have finished deciding, matters far more here than sounding
beautiful.

## The safety problem is different in kind 🔒

* **🦜 Copying a voice.** **Chatot** is the warning written into the games: **Chatter** recorded a
  real Trainer's voice and played it back as an attack. Seconds of audio is now enough to copy
  anyone. Consent, a marker in the output, and a flat refusal to copy an unverified voice are the
  baseline — not features you add later.
* **👀 There is no transcript to check.** With Meowth in the middle you screen the words. Built
  directly, the harmful thing **may never exist as words at all**, so you need something that
  listens for it, or a private written trail kept purely so somebody can check.
* **🩺 A cry gives away more than its words.** Age, mood, health, which region it grew up in. A
  machine that quietly notices all that and acts on it is making decisions nobody asked it to
  make.

## Judging it 🏅

Counting how many words it transcribed correctly is necessary and **wildly** beside the point: that
counts the words, and this entire architecture exists for **everything that is not the words.**

So also measure: how long before the first sound comes back — both the typical case and the bad
one. Whether it copes with being interrupted. Whether it sounds like the same Pokémon five minutes
in. And whether Trainers, listening, prefer it.

📌 Above all, measure the two designs against each other **on the cases where tone carries the
meaning** — a question marked only by rising pitch, sarcasm, a Pokémon that needs reassuring. That
is the only place the extra difficulty pays for itself, and if you average it in with everything
else you will conclude, wrongly, that Meowth was good enough.
