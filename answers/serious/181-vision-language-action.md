---
id: "181"
slug: vision-language-action
style: serious
category: multimodal
difficulty: advanced
question: "How do vision-language-action models control robots?"
tags: [vla, robotics, action-tokens, embodiment-gap, sim2real, teleoperation]
---

# From describing the world to acting in it

A vision-language-action model takes the VLM stack (question 117) and adds an output head that emits
**actions** instead of words. The architecture is a small change. The problems are not.

## How actions become tokens

```
   images + proprioception + "put the cup on the shelf"
        │
        ├─► VLM backbone (pretrained on internet-scale vision-language data)
        │
        └─► action head ─► discretised actions
                           e.g. each of 7 DoF binned into 256 values,
                           emitted as tokens, one chunk per timestep

   the trick that makes it work: the backbone already knows what a cup and a shelf ARE.
   only the mapping from understanding to motion has to be learned from robot data.
```

That transfer is the whole bet, and it largely pays: VLAs generalise to objects and instructions
never seen in the robot data, because the *semantic* half came from the web.

**Action chunking** — predicting several timesteps at once rather than one — matters more than it
sounds. It reduces compounding error, smooths motion, and cuts inference frequency, which is a hard
constraint when control loops run at 10-50 Hz and the model is large.

## Where it is hard

* **Data is the binding constraint, and it does not scale like text.** Every robot episode requires
  a physical robot, a physical scene and usually a human teleoperator. Open X-Embodiment-style
  pooling across labs and robot types helps and does not close the gap.
* **The embodiment gap.** Data from one arm does not transfer cleanly to another with different
  kinematics, grippers or camera placement. Cross-embodiment training helps; it is not solved.
* **Sim2real.** Simulation is unlimited and wrong in the ways that matter — contact, friction,
  deformable objects. Domain randomisation narrows it, and the residual gap is precisely the
  manipulation you cared about.
* **Failures are physical.** A wrong word is a wrong word; a wrong action breaks a cup, or a hand.
  This is question 145's irreversibility with real force behind it, and it means the same answer:
  confirmation gates and constrained action spaces, not better prompting.
* **Depth and geometry.** Grasping needs metric 3D (question 152), which is why real stacks carry
  depth sensors rather than trusting monocular inference.
* **Long horizons.** The compounding arithmetic from question 145 applies unchanged, and recovery
  behaviours must be *trained*, not assumed — most demonstration data contains only successes, so
  the model has never seen what to do after a fumble.

## Evaluation

Simulation benchmarks are cheap and correlate imperfectly with real hardware. Real evaluation needs:

* **Task success on physical hardware**, with enough trials for a meaningful interval — robotics
  results are frequently reported on ten episodes, which cannot distinguish 60% from 80%.
* **Generalisation splits stated explicitly**: unseen object, unseen instruction, unseen scene,
  unseen embodiment. These are wildly different difficulties and pooling them is meaningless.
* **Safety envelope**: force limits, workspace bounds, and behaviour on out-of-distribution input.

## What an interviewer digs into next

* What exactly transfers from web pretraining, and what must come from robot data?
* Why does action chunking help?
* Why does demonstration data leave models unable to recover from errors?
* Why are ten-episode robotics results uninformative?
