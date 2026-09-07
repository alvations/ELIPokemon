---
id: "134"
slug: domain-adaptation-translation
style: pokemon
category: translation
difficulty: intermediate
question: "How do you adapt a translation system to a specific domain?"
tags: [domain-adaptation, fine-tuning, forgetting, retrieval, routing, in-domain-data]
---

# Brock is magnificent at Rock and useless at everything else

Every Gym Leader in Kanto is a specialist. **Brock** at the Pewter Gym knows Rock the way nobody
else does. **Misty** at Cerulean knows Water. **Sabrina** at Saffron knows Psychic. Each of them
would take apart a generalist inside their own hall — and each of them, taken out of that hall,
is just a Trainer.

That is domain adaptation. Moving quality into a narrow patch **without wrecking it everywhere
else**, which is the part everybody underestimates.

## First: are you sure it is a domain problem? 🔍

Four different things get called "the domain", and mixing them up is the commonest mistake:

| What varies | What it looks like |
| --- | --- |
| 🏷️ **The names** | the same word means the item here and the move there |
| 🎩 **The register** | a Gym Leader's formal challenge versus a rival's taunt |
| 📐 **The shape** | a nickname capped at ten characters; a menu label; a table |
| 📚 **The subject** | what is actually being talked about |

📌 Most "we need to adapt to this domain" turns out to be **names** (question 133) plus a change
of tone — and both of those are fixed far more cheaply than by retraining anything.

## The methods, cheapest first 🪜

**1. 🗒️ Just show it five examples.** Hand the translator five entries from this domain and the
names it will need. No training, works immediately, and it is very often most of the gain that was
ever available. People skip straight past this to fine-tuning constantly.

**2. 📚 Look up the closest thing already translated.** Same idea, except the examples are chosen
*per entry* rather than fixed in advance:

```
   the entry to translate ─► find the nearest approved entries already on file ─┐
                                                                                ├─► translate
   the names this entry actually uses ─────────────────────────────────────────┘
```

**3. 🎯 Drill it on real material from the domain.** The standard answer, with the trap attached
below. Prefer a **disc you can swap** (questions 025, 110) over rebuilding the Pokémon.

**4. 📖 Read a great deal of the domain's writing first**, then drill. This is the move when you
have mountains of domain text and almost no *matched pairs*, which is the usual situation.

**5. 🔌 Or keep one Pokémon and change its form.** **Rotom** is the shape of this: one Pokémon, and
whichever appliance it enters decides what it is that day — the oven, the washing machine, the
fridge, the fan, the mower. One creature, five specialisms, switched at the door. No stable of
separate specialists to maintain.

## The trap: it only has four move slots 🚨

Here is the thing that catches everyone, and Pokémon states it as a hard rule rather than a
tendency. **The Four-Move Limit.** A Pokémon knows four moves. Teaching it a fifth means one of the
existing four is **gone**.

⚠️ So drill a Pokémon relentlessly on Rock-type opponents and it does not simply become better at
Rock. It **forgets things**. And what it forgets is the ordinary, general-purpose material — which
is most of what any real battle actually consists of, including most of the turns inside a Rock
Gym.

Ways to stop it, most effective first:

* **⚖️ Keep drilling the general material alongside.** Do not fill all four slots with the
  specialism. This is by far the biggest lever and the one people leave out.
* **🐢 Drill gently and briefly.** Domain adaptation needs much less than people give it.
  Overtraining is nearly always the cause.
* **💿 Use a swappable disc**, so the Pokémon underneath is untouched by construction.
* **💎 Keep a Heart Scale.** The **Move Reminder** can restore a move that was drilled out — which
  is the whole point of holding something that lets you walk the specialisation back.

## Sending the right specialist 🚦

Work out what kind of text this is, then route it to the Leader who handles that.

Two cautions. **The Leader you pick wrongly is a wrong translation** — so measure how often the
routing itself is wrong, not just how good each Leader is. And **decide once per document, not per
sentence**: a Pokédex that switches from Misty to Blaine halfway down the page produces something
nobody wrote.

## How to be honest about it 🏅

* 📊 **Always report the outside-the-Gym score next to the inside-the-Gym one.** Brock tested only
  on Rock looks like the finest Trainer alive. That number, alone, is not information — it is
  the exact thing you were supposed to be watching for.
* 📄 **Hold out whole documents, not scattered sentences.** Sentences from the same page leak into
  each other and flatter you.
* 🏷️ **Count the names separately** (question 133). If the whole apparent gain turns out to be
  terminology, you should have written a list rather than run a training job.
* 👓 **And have somebody who knows the domain read fifty of them.** In a Gym, the mistake that
  matters is one specific wrong word, and no averaged score weighs that properly.
