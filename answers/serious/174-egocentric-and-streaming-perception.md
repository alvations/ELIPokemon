---
id: "174"
slug: egocentric-and-streaming-perception
style: serious
category: multimodal
difficulty: advanced
question: "What changes when a model sees the world from a first-person camera, continuously?"
tags: [egocentric, streaming, memory, latency, privacy, wearables]
---

# First-person, continuous perception

Everything in questions 117-128 assumed a photograph handed to a model: framed by a person, chosen
because it contains the subject, arriving once. A wearable or robot camera breaks all three
assumptions at once.

## What actually differs

| | Curated image | Egocentric stream |
| --- | --- | --- |
| Framing | subject centred, in focus | subject half out of frame, occluded by the wearer's hands |
| Motion | none | constant, with motion blur and rapid viewpoint change |
| Selection | someone chose this frame | nobody chose anything; most frames contain nothing of interest |
| Arrival | once | continuously, forever, with no end |
| Question timing | after the image | often *after the moment has passed* |

That last row is the deep one. "Where did I leave my keys?" is asked long after the keys left the
frame. The system must have **already decided** what was worth remembering, without knowing what
would be asked.

## The memory problem

You cannot keep everything, and you cannot know in advance what matters.

```
   8 hours at 1 fps  ≈  29,000 frames  ≈  far beyond any context window

   so the architecture is necessarily:
        stream ─► cheap always-on filter ─► selective encoding ─► structured memory
                       │                          │                     │
                  motion/novelty/          full VLM only on          episodic: what,
                  voice-activity           frames that pass          where, when
                  triggers                                           + retrieval index
```

This is retrieval (question 044) applied to your own past, and the design question is **what to
write down**, which is unanswerable in general and must be made task-specific. A system built for
"find my keys" indexes object-place-time. One built for "what did she say about the meeting"
indexes speech. They are not the same system, and pretending one architecture serves both is the
usual overreach.

## Streaming changes the model contract

Offline video (question 126) may look at the whole clip. Streaming perception must answer **from
what it has seen so far**, commit before the future arrives, and run within a fixed per-frame
budget forever. That is question 143's simultaneous-translation trade-off, in vision: quality
against latency, with no point on the curve where you get both.

Practical consequences: a small always-on model with escalation to a large one on demand; caching
across frames that barely change (question 165); and explicit handling of "I do not know yet, ask
me again in a moment", which is a legitimate answer that most systems have no way to express.

## Privacy is the design constraint, not a compliance step

A continuously recording camera captures **bystanders who did not consent**, in homes, in
workplaces, in bathrooms. This is not a hypothetical: it is the reason previous wearable-camera
products failed socially rather than technically.

What a serious design does: process on-device by default and transmit derived features rather than
frames; provide an unambiguous, hardware-level recording indicator that cannot be disabled in
software; blur or drop faces and screens at capture; retain for the minimum the task needs; and
make deletion real and verifiable. Treating this as a legal checkbox rather than an architectural
requirement is how you build something nobody is willing to sit next to.

## Evaluation

Ego4D-style benchmarks cover episodic memory, hands-and-objects, and forecasting. Beyond accuracy,
report **latency per frame**, **power draw** (the actual constraint on a wearable), **memory
footprint growth over an 8-hour session**, and **false-recall rate** — a system that confidently
answers "on the kitchen table" about keys it never saw is question 122's failure with higher stakes.

## What an interviewer digs into next

* Why can't you decide what to remember at query time?
* How does streaming perception resemble simultaneous translation?
* Why is on-device processing an architectural rather than a legal decision here?
* What does memory footprint growth over a session tell you that accuracy does not?
