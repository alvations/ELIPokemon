---
id: "184"
slug: face-recognition-and-biometrics
style: serious
category: multimodal
difficulty: advanced
question: "What should an engineer understand before building anything that recognises people?"
tags: [face-recognition, biometrics, demographic-bias, thresholds, consent, regulation]
---

# Recognising individual people

This is the application where the engineering and the ethics are not separable, and where the
technical details determine the size of the harm. Understanding the mechanics is what lets you
argue about the deployment credibly.

## Verification and identification are different problems

```
   VERIFICATION (1:1)   "is this the person whose passport this is?"
        one comparison. A false match affects one transaction.

   IDENTIFICATION (1:N) "who, among these 5 million people, is this?"
        N comparisons. At a per-comparison false match rate of 1 in a million
        and N = 5,000,000, you expect FIVE false matches PER QUERY.

   the same model, the same threshold, and completely different consequences.
```

This arithmetic is why "our system is 99.9% accurate" is meaningless without N and without the
operating point. Vendors quote verification numbers for identification deployments constantly, and
the difference is several orders of magnitude in the false-accusation rate.

## Demographic differential is measured, persistent, and consequential

Large-scale evaluations (NIST FRVT is the reference) have repeatedly found false match rates
varying by **one to two orders of magnitude** across demographic groups, with the highest error
rates typically for darker-skinned, female and elderly subjects. The causes are compounded: training
data composition, image capture (sensors and exposure algorithms calibrated on lighter skin), and
threshold selection on an unrepresentative validation set.

Two things follow:

* **A single aggregate accuracy number conceals the entire problem.** Report per-group false match
  and false non-match rates at your operating point, or you have not measured your system.
* **Real-world harms have followed** — documented wrongful arrests from identification matches
  treated as evidence rather than as a lead. The failure mode is not the model alone; it is the
  model plus a human process that treats its output as confirmation.

## The other technical realities

* **Presentation attacks.** Photographs, screens, masks. Liveness detection is a separate system and
  a separate arms race.
* **Templates are biometric data.** A face embedding is not anonymised — it identifies a person and
  it cannot be reissued if leaked. You can change a password; you cannot change your face.
* **Function creep.** A system built for building access becomes attendance monitoring becomes
  productivity assessment. Design assuming this will be proposed.
* **Regulation is real and varies.** The EU AI Act restricts real-time remote biometric
  identification in public spaces; Illinois BIPA has produced very large settlements; several
  jurisdictions ban it outright for public agencies. This is not a distant compliance concern.

## What responsible practice looks like

Consent that is specific and revocable; the narrowest possible purpose, written down; retention
limits and real deletion; per-group performance published, not just aggregate; a human decision
process that treats a match as a **lead requiring independent corroboration**, never as
identification; and an honest answer to whether a non-biometric mechanism would work — a badge, a
PIN, a code — because very often one would.

And the answer that is sometimes correct: **do not build it.** Some deployments have no threshold
setting that makes them acceptable, and recognising that is an engineering judgement, not a failure
of nerve.

## What an interviewer digs into next

* Work through the 1:N false match arithmetic and explain why it changes the deployment decision.
* Why does aggregate accuracy conceal demographic differential?
* Why is a face embedding not anonymised data?
* When should the answer be "we should not build this"?
