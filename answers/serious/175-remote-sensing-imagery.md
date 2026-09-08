---
id: "175"
slug: remote-sensing-imagery
style: serious
category: multimodal
difficulty: advanced
question: "What makes satellite and aerial imagery different from ordinary computer vision?"
tags: [remote-sensing, multispectral, geospatial, tiling, change-detection, dual-use]
---

# Satellite and aerial imagery

Remote sensing looks like ordinary vision and violates most of its assumptions. The differences are
concrete and each one breaks a standard technique.

## What is different

* **More than three channels.** Multispectral sensors capture ten-plus bands; hyperspectral capture
  hundreds. Near-infrared, short-wave infrared and thermal carry most of the signal for vegetation,
  moisture and materials. A pretrained RGB encoder **discards the informative channels** — this is
  the single most common mistake, and it is invisible because the model still works, just worse.
* **No canonical orientation.** Objects appear at any rotation. Rotation augmentation is not
  optional here, and architectures with rotation equivariance genuinely help.
* **Scale is known and meaningful.** Ground sample distance is metadata: you know a pixel is 30 cm.
  Object size in metres is therefore *available*, which is the opposite of question 152's scale
  ambiguity — and most pipelines throw it away by resizing.
* **Enormous images, tiny objects.** A scene is 10,000 pixels square; a vehicle is 20 pixels.
  Tiling with overlap is mandatory (question 121), and objects straddling tile boundaries need
  reconciliation.
* **Extreme class imbalance.** The interesting thing occupies a tiny fraction of the area.
* **Time series, not stills.** The same location, repeatedly. **Change** is usually the actual
  target, not classification of a single date.
* **Physical corrections come first.** Atmospheric correction, cloud masking, radiometric
  calibration, orthorectification. Skipping these means your model learns cloud cover and haze.

## Change detection is the characteristic task

```
   image at t1  ──┐
                  ├─► align precisely (co-registration) ─► compare ─► change mask
   image at t2  ──┘         ▲
                    misalignment by ONE PIXEL produces change everywhere along
                    every edge in the scene. Registration error dominates the
                    error budget, and it is a preprocessing problem, not a
                    modelling one.
```

And most detected change is uninteresting: seasons, illumination angle, crop cycles, snow, shadow
length. Separating **change that matters** from **change that always happens** is the task, and it
needs either a seasonal baseline or paired same-season imagery.

## Self-supervision fits unusually well

Labels are scarce and expensive (they need field verification), while unlabelled imagery is
effectively unlimited and free from public programmes. Masked autoencoding and contrastive
pretraining on unlabelled scenes, then fine-tuning on a small labelled set, is the standard recipe
and works better here than in most domains — with the caveat that geographic distribution shift is
severe: a model trained on one continent's agriculture will not transfer to another's.

## The part that requires a decision

Overhead imagery is **dual-use by construction**. The same building-detection model serves disaster
response, informal-settlement mapping for service delivery, and surveillance of populations who did
not consent to being counted. Resolution and revisit rate are now commercially available at levels
that make individual-scale inference possible.

There is no technical control that resolves this. What exists is: being explicit about who the
system is for, refusing applications that target individuals or groups for harm, respecting
licence terms that restrict use, aggregating outputs to a level that cannot identify households,
and being honest that publishing a capability publishes it to everyone.

## What an interviewer digs into next

* Why is using an RGB-pretrained encoder a silent error rather than a loud one?
* Why does co-registration dominate the error budget in change detection?
* Why does self-supervision work particularly well here?
* How does knowing ground sample distance change the problem relative to question 152?
