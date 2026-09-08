---
id: "192"
slug: multimodal-monitoring
style: serious
category: multimodal
difficulty: advanced
question: "How do you monitor a multimodal system in production?"
tags: [monitoring, drift, silent-failure, canaries, alerting, incident-response]
---

# Watching a multimodal system after it ships

Offline evaluation tells you how the model behaves on a set you chose. Production tells you how it
behaves on the world, which changes without informing you. The distinguishing property here is that
**multimodal failures are silent**: nothing errors, latency is normal, and fluent wrong answers flow
out at full rate.

## The four things that drift

```
   1. INPUT DISTRIBUTION   new camera, new app version, new user population,
                           a partner sending PDFs where they used to send photos

   2. THE WORLD            products change, forms are redesigned, a UI is
                           restyled and every screenshot now looks different

   3. THE MODEL            a provider updates a hosted model under you
                           (question 187's change-control problem)

   4. THE PIPELINE         a resize step changes, a library updates its JPEG
                           decoder, an image arrives rotated by EXIF that
                           something now honours and something else does not
```

Number 4 causes more production incidents than the model ever does, and it is invisible to
model-level monitoring.

## What to actually instrument

**On the input side**, which is where you get early warning:

* image resolution, aspect ratio and file-size distributions;
* the fraction of inputs that are documents versus photographs versus screenshots;
* embedding-space distance from your training/reference distribution — a cheap, sensitive drift
  signal;
* decode failures and EXIF orientation anomalies.

**On the output side**:

* answer length distribution (a sudden shortening often means refusals; a lengthening often means
  hedging, question 167);
* refusal rate, tracked as a first-class metric in both directions (question 139);
* for grounded systems, the rate at which citations resolve;
* for generation, the rate of repetition and degenerate output (question 136).

**On the behaviour side**, which is what actually correlates with user harm:

* retries, rephrasings, zoom actions and abandonment (question 189);
* escalation rate to a human path;
* per-segment latency and cost, since cost drift is often the first sign of a routing change.

## Canaries are the highest-value control

Run a **fixed set of inputs with known correct answers** through production continuously — hourly,
not nightly. When a provider silently updates a model, when a preprocessing step changes, when
someone deploys a config with the wrong resolution, the canary catches it in an hour instead of a
quarter. It costs almost nothing and it is the single control most teams lack.

Include in the canary: an OCR-dependent case, a counting case, a spatial-relation case, a
text-only case (to catch the regression in question 148), and a known-unsafe input to check refusal
behaviour still works.

## Alerting on the right thing

Alert on **rates and distributions**, not individual outputs — a single bad answer is noise, a
five-point shift in refusal rate is an incident. Set thresholds from observed variance, not from
intuition. And write down, before the incident, what you will do when the alert fires: roll back to
a pinned version, fall back to a cheaper deterministic path, or degrade gracefully to "we cannot
answer this". A monitoring system with no defined response is an expensive way to feel informed.

## What an interviewer digs into next

* Why are multimodal production failures typically silent?
* Which drift category causes the most incidents, and why is it invisible to model monitoring?
* What goes in a canary set, and why hourly?
* Why alert on distributions rather than individual outputs?
