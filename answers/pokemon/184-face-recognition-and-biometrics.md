---
id: "184"
slug: face-recognition-and-biometrics
style: pokemon
category: multimodal
difficulty: advanced
question: "What should an engineer understand before building anything that recognises people?"
tags: [face-recognition, biometrics, demographic-bias, thresholds, consent, regulation]
---

# Not "a Pikachu" — *that* Pikachu

Everything so far has been about naming the **species**. This is about naming the **individual**,
and it is the one place in this whole dataset where the engineering and the ethics cannot be pulled
apart.

Learn the mechanics anyway. **Understanding the arithmetic is what lets you argue about the
deployment credibly**, and the arithmetic is the strongest argument available.

## Two questions that sound alike and are not 🔢

```
   "IS THIS MY PIKACHU?"          one comparison against one record.
                                  A wrong answer costs one Trainer one trade.

   "WHICH PIKACHU IS THIS,        five million comparisons.
    OUT OF FIVE MILLION?"         ⚠️ At one wrong match per million comparisons,
                                     you expect FIVE WRONG MATCHES on EVERY QUERY.

   Same machine. Same threshold. Utterly different consequences.
```

📌 **This is why *"our system is 99.9% accurate"* means nothing** without saying how large the pile
is and where the threshold sits. Vendors quote the one-to-one number for a one-to-many deployment
constantly, and the gap between them is **orders of magnitude** in how often somebody is wrongly
accused.

## And it is not equally wrong for everybody 🚨

Here the Pokémon framing has to stop, because this part is about people and understating it would
be dishonest.

Large-scale independent evaluations have repeatedly found **false match rates varying by one to two
orders of magnitude across demographic groups** — worst, typically, for darker-skinned, female and
elderly subjects. The causes compound: who was in the training data, cameras and exposure
algorithms calibrated on lighter skin, and thresholds chosen on a validation set that did not
represent the people the system would meet.

Two things follow, and they are not optional:

* ⚠️ **A single overall accuracy figure conceals the entire problem.** Publish the error rates **per
  group, at your operating point**, or you have not measured your system — you have measured the
  majority of it.
* 🚔 **The harms are documented and real.** People have been wrongly arrested on the strength of a
  match. And note where the failure actually sat: not in the model alone, but in **a human process
  that treated a ranked guess as a confirmation.**

## The rest of the mechanics 🔧

* **🎭 It can be shown a copy.** A photograph, a screen, a **Ditto** mid-Transform, a **Zoroark**
  under Illusion. Detecting that you are looking at a live thing is **a separate system**, and a
  separate arms race.
* **🔑 The stored pattern *is* the person.** ⚠️ A face measurement is **not anonymous data** — it
  identifies somebody, and unlike a **nickname** at the **Name Rater**, **it cannot be changed after
  a leak.** You can reissue a password. Nobody gets a new face.
* **📈 It will be asked to do more.** A device for finding your lost Pokémon becomes a device for
  logging which Trainers entered the Gym, becomes a device for rating how long they stayed. **Design
  assuming this will be proposed**, because it will be.
* **⚖️ And the law is real, and differs by region.** Several jurisdictions restrict or outright ban
  this in public spaces, and one has produced very large settlements. This is not a distant
  compliance footnote.

## What responsible practice looks like ✅

Consent that is **specific and revocable**. The narrowest purpose you can write down, written down.
Deletion that actually deletes. **Per-group performance published**, never just the average. And a
human process that treats a match as **a lead needing independent corroboration** — never as an
identification.

Then ask the question people skip: **would a badge, a PIN, or a code have worked?** Very often one
would, and it carries none of this.

📌 And the answer that is sometimes simply correct: **do not build it.** Some deployments have no
threshold that makes them acceptable. Recognising that is an engineering judgement — it is the same
judgement as reading the Type Chart and declining the battle — **not a failure of nerve.**
