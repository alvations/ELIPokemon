---
id: "240"
slug: apache-two-at-frontier-scale
style: serious
category: open-weights
difficulty: advanced
question: "A 975B-parameter open-weight model ships under plain Apache 2.0. What does an unconditional licence at that scale actually change?"
tags: [licensing, apache-2, open-weights, compliance, deployment]
---

# What changes is the shape of the review, not the size of the permission

Questions 222 and 227 are about conditional licences: two checkpoints in one release under
different terms, and a "modified MIT" whose modification turned into a revenue-gated agreement one
version later. Both answers land on the same instruction — read the modification, and re-review on
every version bump. **Apache 2.0 at frontier scale is the case where there is no modification to
read**, and that changes the *shape* of a legal review rather than merely its outcome. Thinking
Machines Lab's Inkling — reported at 975B total parameters with 41B active — is the example, and
what it does and does not buy you is worth being precise about.

I could not reach the model's own repository from this environment, so the Apache 2.0 attribution
is **coverage**. The licence text quoted below is not: I read it from the canonical SPDX copy on
`raw.githubusercontent.com`.

## The four clauses that actually do work

* **§2, copyright.** "Perpetual, worldwide, non-exclusive, no-charge, royalty-free,
  **irrevocable** copyright license to reproduce, prepare Derivative Works of, publicly display,
  publicly perform, sublicense, and distribute." There is no scale trigger, no field-of-use
  carve-out, and no acceptable-use policy incorporated by reference. A fine-tune is a Derivative
  Work and it is covered by name.
* **§3, patents.** The same adjectives, applied to a patent licence "to make, have made, use,
  offer to sell, sell, import, and otherwise transfer the Work" — terminating automatically if you
  sue anyone alleging the Work infringes your patents. **MIT has no patent grant at all.** At a
  scale where the architecture is full of patentable technique — a learned relative-position bias,
  a shared-expert routing sink, short convolutions in every block — an express grant from the
  party that built it is not a formality.
* **§4, redistribution.** Four conditions, and they are the ones teams forget: ship a copy of the
  licence; **cause modified files to carry prominent notices stating that you changed them**;
  retain the copyright, patent, trademark and attribution notices; and reproduce the NOTICE file
  if one exists. These bite on quantised re-uploads and merged checkpoints, which are
  redistribution.
* **§6, trademarks.** The licence "does not grant permission to use the trade names, trademarks,
  service marks, or product names of the Licensor". You may build on the weights. You may not name
  your product after them.

And §7 and §8 disclaim warranty and liability completely, which is the clause that matters most at
45 trillion tokens and is discussed below.

## Against the conditional licences, side by side

```
   THE QUESTION A REVIEW ASKS      CONDITIONAL LICENCE (222, 227)   APACHE 2.0
   ─────────────────────────────   ──────────────────────────────   ────────────────────────
   Does a revenue figure change    yes — MAU thresholds, $20M       no. no threshold exists
   my obligations?                 aggregate-and-affiliate bands
   ─────────────────────────────   ──────────────────────────────   ────────────────────────
   Must I sign something before    sometimes — "before using ...    no. acceptance is use
   commercial use?                 for any commercial purpose"
   ─────────────────────────────   ──────────────────────────────   ────────────────────────
   Does it depend on HOW I         yes — "Model as a Service" is    no. no field-of-use
   deploy?                         defined inside the licence       restriction at all
   ─────────────────────────────   ──────────────────────────────   ────────────────────────
   Do I re-review on the next      YES. terms changed between       the text is frozen. only
   checkpoint?                     two versions, same lab           which licence applies can
                                                                    change
   ─────────────────────────────   ──────────────────────────────   ────────────────────────
   RESULT                          a per-deployment, per-band,      a ONE-TIME read, then a
                                   per-version legal workflow       one-line check per bump
```

That bottom row is the whole answer. The permission was already broad under a modified MIT for
almost everybody; what Apache 2.0 removes is the *workflow* — the revenue monitoring, the
affiliate accounting, the procurement timeline before launch, the question of whether your
inference provider holds a carve-out. It converts a recurring obligation into a fact.

## What it conspicuously does not change

1. **Open weights is still not open source, by the reproducibility standard.** Apache 2.0 is
   OSI-approved as a *software* licence, so the objection in 227 — that scale-conditioned clauses
   fail the Open Source Definition — does not apply here. But no training data and no training
   code ship with the weights. You can run, modify, redistribute and sell. You cannot rebuild, and
   you cannot audit what went in.
2. **Nothing is indemnified.** §7 disclaims title and non-infringement explicitly; §8 disclaims
   liability. If the 45-trillion-token mixture contained material it should not have, the licence
   moves that risk to you in plain words. A permissive licence is not a provenance warranty, and
   at frontier scale that is the largest residual exposure by a wide margin.
3. **The compute wall is the real access control.** Reported deployment figures put the BF16
   checkpoint at around 2 TB of accelerator memory and the four-bit variant at around 600 GB. A
   licence that grants everything to everyone, attached to an artefact that needs eight top-end
   accelerators to load, is functionally a licence for organisations that have eight top-end
   accelerators. **Apache 2.0 removes the legal gate and leaves the physical one standing**, and
   people who say "fully open" usually mean only the first.
4. **The name is not yours** (§6), and export control, sectoral regulation and your own customer
   contracts all sit outside the licence entirely.

## What to actually do

* **Vendor `LICENSE` and `NOTICE` next to the weights and hash them**, exactly as 227 prescribes.
  The reason is the same: the licence is part of the artefact.
* **If you redistribute anything — a quantisation, a merge, an adapter baked in — do §4(b).**
  State in the modified files that you changed them. This is the most commonly skipped obligation
  in the whole open-weight ecosystem.
* **Record the checkpoint, the licence and the date in one line**, and on a version bump check
  only that the licence file is still the same file. That is the one-line check the table earns
  you.
* **Do not put the model's name in your product name.**

## What an interviewer is listening for

That you name the patent grant as the real difference from MIT rather than reciting "permissive".
Strong answers separate what the licence permits from what the hardware permits. The strongest
notice that the value of an unconditional licence is procedural — it deletes a recurring workflow
— and that §7's non-infringement disclaimer is where the residual risk of a 45-trillion-token
mixture actually lands.

## Where this stands, September 2026

The licence text was read first-hand from the canonical SPDX copy and quoted, not paraphrased. The
claim that this particular checkpoint is under Apache 2.0, and the memory figures, are
**coverage** — `thinkingmachines.ai` and `huggingface.co` are blocked from here, so the
repository's own `LICENSE` file was not opened. That is exactly the gap 227 says to close before
shipping: open the licence file for the checkpoint you are deploying and read it yourself. Apache
2.0's text does not change; which text a given checkpoint carries changes all the time.
