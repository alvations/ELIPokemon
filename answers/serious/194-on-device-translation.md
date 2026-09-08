---
id: "194"
slug: on-device-translation
style: serious
category: translation
difficulty: intermediate
question: "What changes when translation has to run on a phone?"
tags: [on-device, quantization, language-packs, offline, privacy, memory-budget]
---

# Translation without a server

On-device translation is not a smaller version of the server problem. The constraints are different
in kind, and they change which techniques are available at all.

## The budget

```
   a server model:   billions of parameters, tens of GB, a GPU, ~unlimited memory
   a phone:          a few hundred MB of app budget for ALL languages,
                     shared RAM, a thermal ceiling, and a battery

   this is not a 10x reduction. It is a 100-1000x reduction, and it rules out
   most of what questions 133-152 assume you can run.
```

Consequences:

* **Per-language packs, downloaded on demand.** You cannot ship 50 languages resident. A shared
  multilingual encoder with per-language adapters (question 110) fits this shape well — one base,
  small swappable pieces.
* **Aggressive quantisation** (question 030) — 8-bit as standard, 4-bit common, with per-language
  quality checks because the low-resource pairs degrade first and the aggregate will not show it.
* **Vocabulary size is a real cost.** The embedding table is often the largest single component of a
  small translation model, so vocabulary trimming per language pack is a genuine lever
  (questions 102, 112).
* **Thermal throttling is a latency source** that does not exist on a server: sustained translation
  gets slower after a minute, and your p99 measured on a cold device is a fiction.

## What you gain, and it is substantial

* **Privacy.** The text never leaves the device. For medical, legal, personal and journalistic use
  this is not a nice-to-have; it is frequently the only acceptable architecture (question 187's data
  residency constraint, solved by not moving the data).
* **Offline operation.** Which is the actual use case — travel, field work, disaster response,
  regions with poor connectivity. These are also, not coincidentally, where the languages are often
  low-resource (question 185).
* **No per-request cost**, so the economics of question 180 invert entirely.
* **Predictable latency**, with no network variance.

## The hybrid design

Most shipping products are hybrid: on-device for the common case, server for hard segments, with a
clear rule for when to escalate — and an explicit user-visible setting, because *"sometimes your
text is sent to a server"* is a statement people are entitled to control.

Design the offline path first. A hybrid whose on-device model is an afterthought degrades badly
exactly when connectivity does, which is when it was needed.

## Evaluation on device

* **Measure on the actual hardware**, at the low end of your supported range, not on a workstation.
* **Report sustained throughput**, not a single-shot benchmark, because of thermals.
* **Report per-language quality after quantisation**, not before. The aggregate hides the tail.
* **Measure model download size and memory footprint** as product metrics, because they determine
  whether anyone installs the language pack at all.

## What an interviewer digs into next

* Why are adapters a good architectural fit for language packs?
* Why is the embedding table the thing to attack in a small translation model?
* What does on-device buy that no server-side control can?
* Why measure sustained rather than single-shot throughput?
