---
id: "250"
slug: one-generation-four-artefacts
style: pokemon
category: open-weights
difficulty: advanced
question: "Qwen 3.8 ships a 27B dense, a Flash-Next, a 2.4T-A95B and a hosted Max. What does that line-up tell you?"
tags: [qwen, open-weights, post-training, packaging, multimodal]
---

# Two boxes on the same shelf, the same **Kanto** inside, and no **Growlithe** in one of them

Red and Blue are the same game. Same **Pallet Town**, same **Professor Oak**, same eight Gyms,
same **Safari Zone**, same **Elite Four** in the same order. And **Growlithe** lives in one box
and not the other, while **Vulpix** lives in the other and not that one. **Ekans** against
**Sandshrew**. **Scyther** against **Pinsir**. **Electabuzz** against **Magmar**. **Oddish** and
**Mankey** against **Bellsprout** and **Meowth**. Nothing in the world explains the absence. It
was decided at the factory, and the only way across it is to find a Trainer who bought the other
box.

Qwen 3.8 is four things on that shelf, and three of the four facts are not on the poster:

```
   what it is                  date         yours?  total / active   takes      thinking
   ─────────────────────────   ──────────   ─────   ──────────────   ─────────   ──────────
   Qwen3.8-2.4T-A95B           2026-08-12   yes*    2.4 T / 95 B     text only   never stops
   Qwen3.8-27B                 2026-08-14   yes     27 B  / 27 B     + sight     switchable
   Qwen3.8-Flash-Next          2026-08-26   yes*    ~180 B / 6 B     + sight     switchable
   qwen3.8-max                 2026-08··    rented  = the 2.4T       + sight     switchable
   ─────────────────────────   ──────────   ─────   ──────────────   ─────────   ──────────
   * terms printed on the ball, not the plain ones — question 222. The three
     catchable dates come from the lab's own dated list, read directly.
```

## 1. Same species, four months apart, and one of them has been to the **Move Tutor**

Qwen3.8-27B and Qwen3.6-27B are reported to have the **same 64 layers, the same 5,120 hidden size,
the same 262,144 range and the same 248,320-entry vocabulary** — the same species, in other words,
with the same base stats. And an outside judge scores them **38 and 52**.

There is a check on that which does not go through anybody's press release: the shelf that serving
frameworks keep of every species they know how to handle has **no Qwen 3.6 or Qwen 3.8 row on it
at all**. Everything from 3.5 to 3.8 is handled by one entry. A **Pokédex** cannot flatter anyone.

So this is two **Machamp**. Both 130 base Attack, because that is what a Machamp is. One has been
to the **Move Tutor** and knows **Ice Punch**, and therefore beats the **Garchomp** the other one
loses to four times over. **The species did not change. The raising did.**

**What that proves.** With the species held fixed, what happened after the trade was worth
fourteen points to an outside judge. That is a rare, clean thing to be able to point at.

**What it does not prove**, which is the half the badge is actually for:

- Not that species is irrelevant. It measures what **holding a good species fixed** is worth, not
  what choosing it was worth. A Machamp was already a Machamp.
- Not that it wins *your* match. Issue #238 on the lab's own board reports the newer one **worse**
  in Tamil — 13–27% acceptable against 93% — and pins it on the raising, not on the ball it came
  in. A higher overall score and a lost match-up sit together perfectly well.
- Not that the tutor was honest. **Ice Punch** is a superb move to learn if you already know you
  are being shown a **Garchomp**. Teaching to the gauntlet is exactly what a tutor can do.
- Not at your settings. That 52 was recorded with the dial at its top notch (question 220).
- Not proven identical. Same base stats is not the same **Nature**, the same **Hidden Ability**,
  or the same **IVs**. Matching numbers on a card are not a matching Pokémon.

## 2. Flash-Next is an Egg, and an Egg cannot battle

It is described by its own team as an early look at what the next generation is built on. It takes
up a slot, it is yours, and it is **not a Pokémon yet** — a 125B body, 51B of lookup table, and
only 6B of it doing anything per token. Carrying it to a Gym because the number on it says 3.8 is
carrying an Egg to a Gym.

## 3. The open one cannot see, and that is the version-exclusive

The card on the catchable 2.4T says plainly that **it does not take images**. The rented one takes
text, images and video. Same Pokémon, two boxes, and **sight is in one box only**.

The mechanism is as dull as a factory decision always is:

```
   the one with sight
   ├── the eyes            ← a vision tower, its own pile of weights
   └── the rest of it      ← exactly the thing the open 2.4T loads as
                              ▲
                              └── ship the eyes, and it sees.
                                  Ship no eyes, and it never did.
```

**The sight was not trained out. It was left in the other box.** Four things follow:

1. **You cannot raise it back.** No amount of work on your own team grows eyes. You do not have
   them.
2. **It can move either way.** A factory decision can be reversed in the next print run, or
   reversed the other way, and nothing about the Pokémon changes.
3. **The scores may be from the other box.** Any Qwen 3.8 result involving a picture was recorded
   on the one with eyes. Ask which box before copying a number off it.
4. **Test the individual, not the species** (question 219). "We evaluated Qwen 3.8" is not a
   sentence with an answer here — as useless as "I caught it in Kanto."

## What a Gym Leader is listening for

That you read a shelf as a set of decisions and not as a size chart. Then that you can say both
what the two Machamp prove *and* what they do not — the strongest answers bring up the tutor
teaching to the gauntlet before anyone asks. And that you treat a Pokémon missing from your box
differently from a Pokémon that does not exist, because the fixes are different: one is a
**trade**, and the other is nobody's to make.

## Where this stands, September 2026

The three catchable dates, the description of the Egg and its 125B / 51B / 6B shape, and the empty
shelf where a Qwen 3.6 or 3.8 row would sit are read directly — the first two from the Qwen team's
own repositories, the last from the serving framework's source, where the eyes-plus-body
arrangement above is also read first-hand. **From coverage, not first-hand:** the two
configuration comparisons, the 38 and 52 (an outside judge's numbers, but relayed), the ~180B
on-disk total, the terms on the Egg, and every capability gap between the rented one and the
catchable one including the quoted line about images — the model cards, the blog and the cloud
catalogue are all behind an egress block here, and they are the authorities. Issue #238 is one
Trainer's report on the lab's own board, read directly; it is a measurement by one team, not a
league table. The shelf will be restocked by the next generation. Asking **which box** will not go
out of date.
