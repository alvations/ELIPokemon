---
id: "152"
slug: 3d-and-depth-understanding
style: serious
category: multimodal
difficulty: advanced
question: "Why do vision-language models struggle with 3D and depth?"
tags: [depth-estimation, scale-ambiguity, point-clouds, nerf, gaussian-splatting, embodied]
---

# Depth, scale and 3D structure

A photograph is a projection: the world's three dimensions collapsed onto two, irreversibly. Every
3D capability has to *recover* something that was thrown away, and the first thing to understand is
that in the general case it **cannot be recovered** — only estimated from priors.

## Scale ambiguity is fundamental, not a limitation

```
   the same image is consistent with:

      a real object, far away, large      ┐
      a scale model, close, small         ├─ all project to identical pixels
      a photograph of either              ┘

   monocular depth is recoverable only UP TO AN UNKNOWN SCALE FACTOR.
   Everything else is prior knowledge: "doors are about 2m", "people are about 1.7m".
```

This is why **relative** depth (which is nearer) is a much easier and better-solved problem than
**metric** depth (how many metres). Models like Depth Anything produce excellent relative depth;
metric depth needs either known camera intrinsics, a second view, an active sensor, or strong
object-size priors that fail on anything unusual — which is exactly where you notice.

## Why a standard VLM has almost no 3D understanding

* **The training signal never required it.** Contrastive captions (question 120) and instruction
  data describe *what*, rarely *where in depth*.
* **Patch flattening discards geometry** (questions 118, 128). Identity survives; spatial structure
  is weakly encoded at best.
* **There is no depth channel.** The model sees RGB patches. Any depth understanding is inferred
  from monocular cues — occlusion, perspective, shading, texture gradient — that were never
  explicitly supervised.

The practical consequence: a VLM can tell you a mug is on a table and cannot reliably tell you
whether the mug is in front of or behind the laptop, how far apart they are, or whether a robot arm
could reach between them.

## Representations, and what each is for

| Representation | What it stores | Good for |
| --- | --- | --- |
| **Depth map** | per-pixel distance, one viewpoint | quick reasoning, occlusion, segmentation aid |
| **Point cloud** | unordered 3D points, often from LiDAR/stereo | robotics, measurement, registration |
| **Voxel grid / TSDF** | occupancy on a regular grid | planning, collision checking |
| **Mesh** | surfaces and topology | simulation, graphics, editing |
| **NeRF** | a network mapping position+direction to colour and density | photorealistic novel views; slow to train and render |
| **Gaussian splatting** | millions of anisotropic 3D Gaussians | novel views in real time; now the default for capture |

NeRF and splatting are **view synthesis**, not understanding: they reconstruct appearance
beautifully and hold no notion of what the objects are. Pairing them with semantics is an active
area precisely because the two capabilities are separate.

## Where this bites

* **Embodied agents and robotics.** Grasping needs metric geometry and a camera pose. This is why
  robotics stacks use depth sensors rather than trusting monocular estimates.
* **AR and measurement.** Scale errors are directly visible to the user.
* **Counting and occlusion reasoning.** "How many chairs are in the room" requires understanding
  that a partly hidden chair is one chair.
* **Novel-view questions.** "What would this look like from the left?" is near-impossible for a
  standard VLM and easy for anything with an actual 3D representation.

## Evaluating it

* **Separate relative from metric.** Report ordinal accuracy (is A nearer than B) and metric error
  (AbsRel, RMSE) as different numbers; a model can be excellent at one and useless at the other.
* **Report scale handling explicitly** — whether predictions were scale-aligned to ground truth
  before scoring. Median-scaling a prediction before computing error is standard in the literature
  and quietly removes the hardest part of the problem, so it must be stated.
* **Test on out-of-distribution scale**: close-ups, aerial views, scale models, microscopy. This is
  where object-size priors break and the failure is instructive.
* **For agents, measure the downstream task** — grasp success, navigation success — not depth error.
  A depth map with 10% error that supports a successful grasp beats a better map that does not.

## What an interviewer digs into next

* Why is monocular metric depth ill-posed, and what resolves it?
* What does a VLM actually use to infer depth, and why is it unreliable?
* What is the difference between view synthesis and 3D understanding?
* Why does median-scaling before evaluation matter?
