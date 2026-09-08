---
id: "191"
slug: 3d-scene-generation
style: serious
category: multimodal
difficulty: advanced
question: "How do you generate 3D scenes and objects, and why is it harder than images?"
tags: [3d-generation, multiview-consistency, sds, gaussian-splatting, meshes, evaluation]
---

# Generating in three dimensions

Image generation (question 137) has abundant training data. 3D generation does not, and that single
fact shapes every technique in the field.

```
   images available for training:  billions
   3D assets available:            millions at most, and mostly low quality

   so almost every 3D method is a way of BORROWING from 2D generation
```

## The three families

**1. Lift a 2D model (SDS and descendants).** Optimise a 3D representation so that its renders, from
random viewpoints, look like something a text-to-image model would produce. No 3D training data at
all. Slow — minutes to hours per object — and it produces the **Janus problem**: a face on every
side, because the 2D prior wants a front view from every angle and nothing enforces global
coherence.

**2. Multiview generation, then reconstruction.** Generate several consistent views of the object,
then reconstruct geometry from them. Much faster and better-behaved, because consistency is enforced
at generation time rather than hoped for during optimisation. The dominant practical approach.

**3. Native 3D generation.** Train directly on 3D assets — meshes, point clouds, or a latent 3D
representation. Cleanest in principle, limited by data in practice, and improving as 3D datasets
grow.

## Why consistency is the hard constraint

An image only has to look right once. A 3D asset must look right **from every angle
simultaneously**, and the constraints interact: fix the back and the front shifts. This is the same
class of problem as temporal consistency in video (question 157) — one more axis on which the output
must agree with itself, and no per-frame objective enforces it.

## Representation determines what you can do with it

| Output | Good for | Problem |
| --- | --- | --- |
| **NeRF / Gaussian splatting** | novel views, capture, fast visual results | not a mesh; hard to edit, animate or simulate |
| **Mesh + texture** | games, engines, 3D printing, animation | topology quality matters enormously and is usually poor |
| **Point cloud** | intermediate representation | not directly usable in most pipelines |

The recurring disappointment: a system produces a beautiful splat and a game studio cannot use it,
because they needed clean topology, UV-mapped textures and a rig. **"Generates 3D" is not one
capability** — ask which representation, and whether it is production-usable in the target pipeline.

## Scenes are harder than objects

An object is one thing. A **scene** has layout, scale relationships between objects, navigable
space, and physical plausibility — a chair must be on the floor, at chair scale, not intersecting
the table. Object-level methods do not compose into scenes, and scene generation typically needs
explicit layout reasoning before any geometry is produced.

## Evaluation

Report **multiview consistency** (does it agree with itself), **geometry quality** separately from
**texture quality**, and **mesh usability** (watertight, sensible topology, UVs) if you claim
production output. Human preference on rendered turntables is the practical standard, and it should
show **all sides**, because that is precisely where these methods fail and precisely what a
cherry-picked front view hides.

## What an interviewer digs into next

* Why does lifting a 2D prior produce the Janus problem?
* Why is multiview-then-reconstruct better behaved than direct optimisation?
* Why is "generates 3D" an ambiguous capability claim?
* Why must evaluation show all sides of the object?
