---
id: "122"
slug: multimodal-hallucination
style: serious
category: multimodal
difficulty: intermediate
question: "Why do vision-language models hallucinate objects, and how do you measure it?"
tags: [hallucination, pope, chair, language-prior, contrastive-decoding, grounding]
---

# Object hallucination in VLMs

A VLM describing a kitchen mentions a fork that is not in the picture. Nothing is broken. The
model is doing exactly what it was trained to do: produce a fluent, plausible caption. Forks are
overwhelmingly likely near plates, the visual evidence is weak, and fluency has no term in it for
"and check".

## The three causes, in order of importance

**1. Language priors dominate weak visual signal.** The LLM is enormous and was trained on text;
the connector is small and was trained on captions. When the visual evidence is ambiguous, the
cheapest low-loss continuation is whatever the language model would have said unconditionally.
This is why hallucination gets *worse* as generation continues — later tokens condition on more
generated text and proportionally less on the image.

**2. Co-occurrence bias in the training data.** Captions describe scenes, and scenes have
statistics. If "keyboard" appears with "mouse" in 80% of training captions, the model has learned
a strong prior that has nothing to do with your image.

**3. Objects genuinely not resolvable.** The thing was 12 pixels across after downsampling
(question 121). Here the model is not hallucinating so much as guessing, and the fix is
resolution, not decoding.

```
   generation step:      1 ────────────────────────────────────► 40

   weight on image    ████████████▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░
   weight on own text ░░░░▒▒▒▒▓▓▓▓████████████████████████████

   the description drifts from "what is here" to "what usually follows what I just said"
```

## How it is measured

**POPE** turns captioning into balanced yes/no probing: "Is there a fork in the image?" with an
equal number of present and absent objects, sampled three ways — **random** absent objects,
**popular** ones (frequent in the dataset), and **adversarial** ones (frequently co-occurring with
what *is* present). The adversarial split is the one that matters; the gap between random and
adversarial is a direct read on co-occurrence bias.

**CHAIR** works on free-form captions: what fraction of mentioned objects are not in the ground
truth, per-instance and per-sentence.

Two evaluation traps:

* **Answer imbalance.** If a benchmark is 80% "yes", a model that always says yes scores 80. POPE
  is balanced deliberately; a home-made probe set usually is not.
* **Yes-bias from instruction tuning.** Assistants are trained to be agreeable and will confirm
  leading questions. Always probe both polarities and report the gap.

## Mitigations that actually help

* **Fix the input first.** Higher resolution, better connector, more visual tokens. A great deal
  of "hallucination" is unresolvable detail wearing a costume.
* **Preference training on hallucination pairs.** Build pairs where the rejected response contains
  a hallucinated object and the chosen one does not, then run DPO (question 022). This works well
  and is the standard production answer.
* **Contrastive decoding (VCD-style).** Run the model twice — once on the image, once on a
  distorted or blank image — and subtract the logits of the second from the first. What the model
  says *without* looking is precisely the language prior; removing it suppresses exactly the
  hallucinated tokens. Costs a second forward pass.
* **Ask for grounding.** Require bounding boxes or region references with each claimed object. A
  claim that must point somewhere is much harder to invent, and it makes the failure auditable.
* **Shorter outputs.** Hallucination scales with length. If the task tolerates it, do not ask for
  a paragraph.

Things that do not help much: telling the model "do not hallucinate" in the system prompt;
self-consistency sampling (a strong prior is stable across samples, so agreement is not evidence).

## What an interviewer digs into next

* Why does hallucination increase with generation length?
* What does the random-versus-adversarial POPE gap tell you specifically?
* How does contrastive decoding isolate the language prior?
* When is "hallucination" actually a resolution problem?
