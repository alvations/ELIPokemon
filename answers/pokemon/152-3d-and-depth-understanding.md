---
id: "152"
slug: 3d-and-depth-understanding
style: pokemon
category: multimodal
difficulty: advanced
question: "Why do vision-language models struggle with 3D and depth?"
tags: [depth-estimation, scale-ambiguity, point-clouds, nerf, gaussian-splatting, embodied]
---

# Is that an Onix, or a model of an Onix?

**Onix** is 8.8 metres of rock. A toy Onix on a shelf is about eight centimetres.

Photograph either one and — framed right — **you get the same picture.** Not a similar picture. The
same one. Nothing in it can tell you which, because a photograph is the world with one of its
dimensions **thrown away**, and thrown away is thrown away.

📌 That is the thing to understand before anything else here. Every attempt to recover depth from a
single picture is not *measuring* something. It is **guessing from what it already knows.**

## Which is why the Pokédex heights matter so much 📏

```
   the same picture is equally consistent with:

      a real Onix, far away        ┐
      a toy Onix, close up         ├─ identical pixels. no exception.
      a photograph of either one   ┘

   from one picture you can recover WHICH IS NEARER.
   you cannot recover HOW FAR — not without knowing how big something is.
```

So everything leans on the Pokédex's list of heights. **Pikachu is 0.4 m. Snorlax is 2.1 m.
Gyarados is 6.5 m.** Spot a Pikachu in the shot, and suddenly the whole scene has a ruler in it.

⚠️ And that is precisely where it breaks. Modern regions record that individual Pokémon vary — a
**Jumbo** Pikachu, a **Mini** one. The moment you meet one, every distance in the picture is wrong,
confidently, and by a lot. **The prior was doing all the work, and the prior was about the
species, not this one.**

This is why *"which is closer"* is a largely solved problem and *"how many metres"* is not. Nearer
and further you can read off shading and overlap. **Metres** need a second eye, a known lens, or a
Pokémon whose size you are certain of.

## Why a Pokédex has almost no sense of depth 🫥

* **📚 Nothing ever asked it to.** The silhouette drills of question 120 and every caption it ever
  read described **what** was there. Almost none of them said **how far**.
* **🧩 Chopping the picture into tiles threw the geometry away** (questions 118, 128). *What*
  survives that. *Where* barely does.
* **👁️ And it only has one eye.** It sees flat tiles of colour. Every scrap of depth it has is
  inferred from what overlaps what, from perspective, from shading — cues nobody ever explicitly
  taught it.

The practical result: a Pokédex will tell you there is a **Snorlax** on the route and a **Diglett**
beside it, and it cannot reliably tell you which is in front, how far apart they are, or whether
there is room to walk between them.

## Four ways to hold a place in memory 🗺️

| How | What it keeps | What it is for |
| --- | --- | --- |
| 🎚️ **A distance for every tile** | one viewpoint, how far each bit is | quick reasoning, working out what is behind what |
| ☁️ **A cloud of points** | scattered measured positions | anything that has to *reach* something |
| 🧱 **A grid of filled and empty blocks** | what space is occupied | route-finding, and not walking into a boulder |
| ✨ **Millions of soft blobs** | how it *looks* from any angle | showing the place from a new viewpoint, instantly |

⚠️ That last one is the seductive one, and it deserves a warning. It reconstructs a cave so
beautifully you can fly a camera through it — and **it does not know a single thing is in there.**
Ask it which shape is the **Onix** and it has no answer, because it never held the idea of an Onix
at all. It is a gorgeous diorama, and looking is not knowing.

## Where the missing dimension actually costs you 💥

* **🪨 Anything that has to reach or push.** Using **Strength** on a boulder requires knowing where
  the boulder **is** — in metres, from here. This is exactly why anything that must act in the world
  carries something that *measures* distance instead of trusting a guess from one picture.
* **🔢 Counting things that overlap.** *"How many **Zubat** are in this cave?"* — half of them are
  behind the other half, and a partly hidden Zubat is still one Zubat.
* **🔄 "What would this look like from the other side?"** Near-impossible from a flat picture, and
  trivial for anything holding an actual shape.

## Judging it honestly 🏅

* 🔀 **Report nearer-or-further and how-many-metres as two separate numbers.** A Pokédex can be
  excellent at one and useless at the other, and one combined score hides which.
* ⚖️ **Say whether you rescaled its answers before marking them.** Quietly stretching every
  prediction to match the true size before scoring is standard practice, and it **removes the
  hardest part of the problem**. If you did it, say so.
* 🧪 **Test it where the ruler fails**: right up close, from far above, on a toy Onix, on a Jumbo
  Pikachu. That is where the prior collapses, and the collapse is the informative part.
* 🎯 **And for anything that acts, score the outcome.** A rough sense of distance that gets the
  boulder pushed beats a beautiful one that does not.
