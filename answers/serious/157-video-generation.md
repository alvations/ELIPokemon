---
id: "157"
slug: video-generation
style: serious
category: multimodal
difficulty: advanced
question: "How does video generation differ from image generation?"
tags: [video-generation, temporal-consistency, spacetime-patches, fvd, object-permanence]
---

# Generating video

Video generation is image generation (question 137) plus a dimension that is not like the other
two. Width and height are interchangeable. **Time is not** — it has a direction, and the viewer
has strong, unforgiving expectations about what may change along it.

## The architecture

The dominant design treats video as **spacetime patches**: compress with a video VAE that
compresses along time as well as space, cut the latent into patches spanning both, and run a
diffusion transformer over the whole sequence.

```
   raw video   T frames × H × W
        │
        ├─ video VAE: compress ~8x spatially AND ~4x temporally
        │      ← the temporal compression is what makes it affordable
        │
        ├─ cut into spacetime patches (each covers a small region over a few frames)
        │
        └─ diffuse over ALL of them jointly, conditioned on text
                    │
              attention spans space and time together, so a change in frame 1
              is visible to frame 40 — this is what buys consistency
```

Earlier designs bolted temporal attention layers onto an image model. Joint spacetime attention
beats that, at quadratic cost in total patch count — which is why video models are expensive in a
way image models are not, and why generated clips are short.

## Long video, and why it drifts

Beyond a few seconds you cannot hold the whole clip in attention, so you generate in chunks
conditioned on the previous chunk's last frames. That is autoregression, with autoregression's
disease: **error accumulates**. Colours drift, identities morph, the scene slowly becomes a
different scene. Mitigations — conditioning on a keyframe, overlapping windows, hierarchical
coarse-to-fine generation — reduce it and do not remove it.

## The failure modes are about physics, not pixels

Each frame can look excellent while the video is wrong:

* **Object permanence.** Something passes behind a pillar and comes out changed, or does not come
  out. Nothing in the objective enforces that objects persist.
* **Identity drift.** A face or a costume subtly becomes another one across the clip.
* **Non-conservation.** Limbs, fingers and legs appear and vanish; a glass empties and refills.
* **Implausible dynamics.** Water, cloth and collisions that violate what any viewer knows without
  being able to state it. Models learn appearance statistics, not mechanics; "world model" claims
  should be read with this in mind.
* **Text and small detail**, worse than in still images because it must also stay stable.

## Control

Text alone is a weak handle. Practical systems add **image-to-video** (a first frame that fixes
composition and identity), **last-frame conditioning** for transitions, **camera-path control**,
and structure conditioning (depth, pose, edges) — the video analogue of ControlNet. Most usable
output comes from constrained generation, not from a prompt alone.

## Evaluation

**FVD** is the video counterpart of FID and inherits every complaint from question 137 plus a new
one: it is weakly sensitive to exactly the temporal failures above. A clip that morphs an object
can score well.

Report instead: **human preference**, **prompt adherence** rated separately from **visual quality**
and from **temporal consistency**, and targeted probes — object permanence through occlusion,
counting stability across frames, identity retention over the clip's length. Those probes are cheap
to build and tell you far more than a single distributional score.

## What an interviewer digs into next

* Why is joint spacetime attention better than bolted-on temporal layers, and what does it cost?
* Why does long-video generation drift, and what actually helps?
* Why is FVD insensitive to the failures that matter?
* What does it mean to say these models learn appearance rather than mechanics?
