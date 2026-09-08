---
id: "181"
slug: vision-language-action
style: pokemon
category: multimodal
difficulty: advanced
question: "How do vision-language-action models control robots?"
tags: [vla, robotics, action-tokens, embodiment-gap, sim2real, teleoperation]
---

# Knowing what a Gyarados is, and knowing what to do about it

Every Pokédex so far has **described**. This one **battles**.

Take the whole looking-and-talking apparatus from question 117 and replace the mouth with a
**move**. Architecturally it is a small change. In practice it is a different sport.

## The command becomes an action 🎮

```
   what it sees + how it is standing + "Pikachu, Thunderbolt the Gyarados"
        │
        ├─► the same eye and the same reasoning, already trained on everything
        │
        └─► out comes a MOVE — Thunderbolt, not the words "Thunderbolt"
                             each part of the motion picked from a fixed set,
                             several turns' worth chosen at once

   📌 and here is the whole bet: it ALREADY KNOWS what a Gyarados is —
      that it is Water/Flying, that Electric is four times over on it.
      Only the part that turns knowing into DOING must come from real battles.
```

And it pays off. A Pokémon trained this way handles opponents it has **never fought** and commands
it has **never been given**, because the knowing half came from everywhere else.

⚡ **Deciding several turns ahead rather than one** matters more than it sounds. Mistakes stop
compounding, the movement stops being jerky, and — critically — you are no longer asking an enormous
Pokédex to decide something new every fraction of a second while the battle is happening.

## Where it gets hard 🚧

* **📉 The battles do not scale.** Reading every Pokédex entry ever written is free and endless.
  **Every training battle needs an actual Pikachu, an actual field, and usually an actual Trainer
  standing there working the controls.** Pooling battles across the **Cerulean Gym**, the **Pewter
  Gym** and the **Battle Tower** helps, and does not close the gap.
* **🦴 The body is not the same body.** What a **Machamp** learned with four arms does not transfer
  to a **Hitmonlee** with two legs and no hands. Different reach, different grip, different eyes.
  Training across many bodies helps. It is not solved.
* **🏟️ Practice is not the real thing.** You can run simulated matches endlessly, and they are wrong
  in exactly the ways that matter — how a **Focus Sash** actually triggers, how **Sandstorm** chip
  damage actually lands, how a grip actually slips.
  ⚠️ The leftover gap **is** the manipulation you cared about.
* **💥 And the mistakes are physical.** A wrong sentence is a wrong sentence. A wrong **move** breaks
  something. 📌 This is question 145's one-way ledge with real force behind it, and it has the same
  answer: **stop-and-confirm, and a small deliberate set of things it is allowed to do** — not better
  wording.
* **📏 It needs to know how far away things are** (question 152), which is why anything that actually
  reaches for something carries a way to *measure* rather than trusting a guess from one look.
* **🔁 And nobody taught it to recover.** ⚠️ This one is subtle and it is everywhere: the training
  battles are all **wins**. Every demonstration is somebody doing it correctly. So the Pokémon has
  **never once seen what happens after a fumble**, and the first time it drops something it has no
  idea what to do — the compounding arithmetic from question 145, with no recovery move in the
  moveset.

## Judging it 🏅

⚠️ Simulated results are cheap and only loosely predict the real field.

* ✅ **Win rate on an actual field**, over **enough battles to mean something**. Robotics results are
  routinely reported on ten attempts, which cannot tell six-in-ten from eight-in-ten and should not
  be presented as though it can.
* 🔀 **Say which kind of new thing you tested**: an opponent it has never seen, a command it has
  never been given, a field it has never stood on, a **body it has never had**. 📌 These are wildly
  different difficulties and pooling them into one number is meaningless.
* 🛡️ **And the safety envelope.** How hard it is allowed to push, where it is allowed to reach, and
  what it does when it sees something that was never in any battle it trained on.
