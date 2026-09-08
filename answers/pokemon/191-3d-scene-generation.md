---
id: "191"
slug: 3d-scene-generation
style: pokemon
category: multimodal
difficulty: advanced
question: "How do you generate 3D scenes and objects, and why is it harder than images?"
tags: [3d-generation, multiview-consistency, sds, gaussian-splatting, meshes, evaluation]
---

# You asked for a Doduo and got a Dodrio

Generating a **picture** of a Pokémon (question 137) draws on an enormous pile of pictures.
Generating **the Pokémon itself** — a thing you can walk around — does not, and that one fact shapes
every technique in the field.

```
   pictures available to learn from:   billions
   actual three-dimensional Pokémon:   a small fraction of that, and mostly rough

   so nearly every method here is a way of BORROWING from the pile of pictures
```

## Three approaches 🧊

**1. 🖼️ Keep asking a picture-maker until the shape agrees.** Build something in three dimensions,
photograph it from random angles, and nudge it until every photograph looks like something the
picture-maker would have produced. **No three-dimensional training material at all.**

⚠️ Slow — minutes to hours for one Pokémon — and it produces the signature failure of this whole
approach: **a face on every side.** The picture-maker wants a nice front view *from every angle*,
and nothing ever told it the thing only has one front. You asked for a **Doduo** and got a
**Dodrio**. You asked for a **Girafarig** and got something with a head at both ends — which, in
fairness, is what a Girafarig is, and is not what you wanted this time.

**2. 📸 Take several agreeing photographs first, then build from them.** Generate a consistent set of
views, *then* work out the shape. Much faster and far better behaved, **because the agreement is
enforced while generating rather than hoped for while optimising.** This is what most working
systems do.

**3. 🗿 Or learn from actual three-dimensional things.** Cleanest in principle, limited by how few
there are, and getting better as the pile grows.

## Why agreeing with itself is the hard part 🔄

A picture only has to look right **once**. A Pokémon has to look right **from every angle at the
same time** — and the constraints fight each other: fix the back and the front shifts.

📌 This is the same class of problem as a **Charizard** drifting into a **Charmeleon** across a clip
(question 157). One more axis the output has to agree with itself along, and **nothing in the
objective enforces it.**

## What you get out determines what you can do with it 🏗️

| What comes out | Good for | The catch |
| --- | --- | --- |
| ✨ A cloud of soft blobs | looking at it from new angles, fast, beautiful | ⚠️ it is not a *thing*. You cannot pose it, animate it, or battle with it |
| 🧱 A proper built model | actual games, actual animation | how well it is built matters enormously, and is usually poor |
| ☁️ A scatter of points | a stepping stone | not usable by anything on its own |

⚠️ The recurring disappointment: somebody produces a magnificent **Sudowoodo** and the studio cannot
use it. It looks like a Pokémon from every angle and it is a **statue** — the way Sudowoodo itself
looks exactly like a tree and is not one.

📌 So **"it generates in 3D" is not one capability.** Ask *which kind of output*, and ask whether
anybody downstream can actually open it.

## And a route is much harder than a Pokémon 🗺️

One Pokémon is one thing. A **Gym**, a stretch of **Victory Road**, a cave — that has **layout**:
things must sit **on** the floor, at the **right size relative to each other**, with space to walk
between them. A boulder half-inside a wall is not a rendering flaw, it is a broken room.

⚠️ Object-level methods **do not add up into scenes.** Scene generation needs somebody to work out
the arrangement **before** any shape is produced.

## Judging it 🏅

Report whether it **agrees with itself** from every angle. Report **how well it is built**
separately from **how it is painted**. And if you claim it is usable, say whether it actually is —
closed, sensibly built, properly textured.

📌 And show it **turning all the way round.** ⚠️ That is exactly where these methods fail, and
exactly what a carefully chosen front view is hiding. A **Dodrio** photographed from the front is
indistinguishable from a Doduo.
