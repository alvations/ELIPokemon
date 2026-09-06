---
id: "126"
slug: video-understanding
style: pokemon
category: multimodal
difficulty: advanced
question: "How do you extend a vision-language model to video?"
tags: [video, frame-sampling, temporal, token-budget, long-context, needle-in-haystack]
---

# Watching a battle recording, not a photograph of one

The **Vs. Recorder** saves your battles so you can watch them back, and hand the code to someone
else so they can too. That is the object we are trying to teach a Pokédex to understand: not a
still, but **a recording of a battle** — and battles are made of *order*.

Both halves of that are hard. There are an enormous number of stills in a recording, and the thing
that actually matters is the sequence they came in.

## You cannot look at all of it 🪙

```
   a fifty-turn match, every instant of it     =  thousands of stills
   at full detail each                        =  hopeless, by orders of magnitude    ✗

   one still per turn                         =  fifty stills
   each squashed down small                   =  affordable                          ✓
   plus a handful kept at full detail         =  for the turns that decided it       ✓
```

📌 **Every technique here is a way of spending one fixed budget well.** The levers:

* **⏱️ How often you look.** One still per turn is the sensible default and it is fine for *"who
  is winning"*. It is useless for anything quick — a **Quick Attack** going first, a **Focus Sash**
  triggering, whether **Protect** went up before or after the strike landed.
* **🗜️ How small you squash each still.** Neighbouring stills of a battle are nearly identical —
  same field, same two Pokémon, same weather. Each one can afford far less detail than a
  standalone photograph could, precisely because its neighbours already told you most of it.
* **🔗 Merging stills that barely differ.** A long stretch of **Trick Room** ticking down with
  nobody switching compresses to almost nothing. A switch costs full price. **This is where the
  real savings are.**
* **🎯 Keeping only the turns that mattered.** Detect the switches, the knockouts, the moment the
  weather changed. Better still, pick the turns based on *what was asked*. ⚠️ And there is the
  trap: choose the turns by the question, miss the turn holding the answer, and **no amount of
  cleverness afterwards recovers it.** You did not misread the battle. You never watched it.

## Making the order mean something 🕐

A pile of stills tells you Charizard was present. It does not tell you that **Swords Dance went up
twice before the attack**, which is the entire difference between a knockout and a survivable hit.

Three ways to put time back in, cheapest first:

1. **🔢 Stamp each still with its turn number.** Cheap, and most of the benefit.
2. **📜 Write the turn in words between the stills** — *"turn 14"* — spelled out in the sequence
   itself. Crude, works well, and has one lovely property: the Pokédex can now **cite the turn**
   when it answers.
3. **🧠 Let the stills look at each other across time**, position by position. The expensive
   option, and the only one that really understands motion.

Without any of these you have a **bag of stills** — and here is the uncomfortable part: a bag of
stills is enough to win on a great many battle-reading tests. That is a fact about the tests.

## How to test it honestly 🧪

The dominant flaw in judging this: **most questions can be answered from a single still.** Ask
"which Pokémon is out?" and you have measured photograph-reading with extra steps.

* **🔀 Ask questions where order is the answer.** *"Did the Swords Dance come before the Stealth
  Rock went up?"* Then **shuffle the turns as a control.** A Pokédex that genuinely tracks time
  gets worse. A bag of stills scores exactly the same, and now you know.
* **🖼️ Always report what one still alone would have scored.** The gap between that and the full
  recording is the only honest measure of what watching bought you.
* **📍 Hide the deciding moment somewhere specific.** Put it on turn 3, then turn 25, then turn 47,
  and sweep. If accuracy sags in the middle of the match you have the same lost-in-the-middle
  problem as a very long text (question 046) — the beginning and the end are remembered, and
  everything between them is fog.
* **🔢 Make it count things.** *"How many times did Blissey use Protect?"* A bag of stills cannot
  do this at all, which makes it an excellent diagnostic.

## And half of it is not the pictures 📢

Every battle has a running commentary beside it — *"Charizard used Flamethrower!"*, *"It's super
effective!"*, *"Gyarados was hurt by the Life Orb."* **That log is where most of the information
actually is.**

⚠️ Most Pokédexes built for recordings watch the stills and ignore the text entirely. Reading the
log and threading it in beside the stills — turn 14's line next to turn 14's picture — beats a
stills-only Pokédex on nearly every real question, for a fraction of the effort. A great deal of
what looks like watching is really reading.
