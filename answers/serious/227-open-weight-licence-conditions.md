---
id: "227"
slug: open-weight-licence-conditions
style: serious
category: open-weights
difficulty: intermediate
question: "An open-weight model ships under a 'modified MIT' licence. What does that actually oblige you to?"
tags: [licensing, open-weights, compliance, deployment, legal]
---

# The modification is the whole licence, and it changed between two versions of the same model

"Modified MIT" is a phrase that reads like MIT with a footnote and is not. The only part worth
reading is the modification, and the Kimi line demonstrates why with unusual clarity: **the K2
licence and the K3 licence are different documents with materially different obligations, twelve
months apart, from the same lab.** I read both directly from the raw files in Moonshot's GitHub
repositories.

## Kimi K2, K2.5 and K2.6: genuinely MIT plus one attribution clause

The K2 file is headed "Modified MIT License", is verbatim MIT throughout, and ends:

> Our only modification part is that, if the Software (or any derivative works thereof) is used
> for any of your commercial products or services that have more than 100 million monthly active
> users, or more than 20 million US dollars (or equivalent in other currencies) in monthly
> revenue, you shall prominently display "Kimi K2" on the user interface of such product or
> service.

That is the entire delta. It is an attribution requirement at a threshold almost nobody reaches,
and for nearly every team it is functionally MIT. The K2.5 file is the same document with "Kimi
K2.5" substituted. K2.6 is reported under the same terms — that one I could not verify from a
primary file, because there is no public repository for it and the Hugging Face card was blocked
from this environment.

## Kimi K3: a different licence, with a gate rather than a credit

K3 is headed **"Kimi K3 License"**. It is not MIT and does not claim to be. It grants broad rights
— use, copy, modify, distribute, sublicense, sell, run, deploy, fine-tune, create derivative works
— and then attaches conditions. The one that matters:

> If the Licensee or any of its affiliates operates a Model as a Service business, and the
> aggregate revenue of the Licensee and its affiliates exceeds 20 million US dollars (or the
> equivalent in other currencies) in total over any consecutive 12 months, the Licensee must enter
> into a separate agreement with Moonshot AI before using the Software or its derivative works for
> any commercial purpose.

It defines the trigger itself: "Model as a Service" means giving a third party access to inference
or fine-tuning in a way that lets them exercise meaningful control over inputs, parameters or
training data — explicitly **not** end-user products with the model embedded in specific features
or harnesses, and **not** mere relaying to models hosted by others. The attribution clause
survives alongside it at the same 100M MAU / $20M monthly threshold, now naming "Kimi K3". A
fourth
clause exempts internal use, and use via Moonshot's own products or certified inference partners.

## The four things a review actually has to read

```
   ┌───────────────────────┬───────────────────────────────────────────────┐
   │ 1. WHAT TRIPS IT      │ Not your MaaS revenue. The AGGREGATE revenue  │
   │                       │ of you and your affiliates — any consecutive  │
   │                       │ 12 months. A $25M company with a small        │
   │                       │ inference product is inside the clause.       │
   ├───────────────────────┼───────────────────────────────────────────────┤
   │ 2. WHEN IT BITES      │ "before using ... for any commercial          │
   │                       │ purpose." The agreement is a PRECONDITION,    │
   │                       │ not a bill that arrives later. Shipping first │
   │                       │ and negotiating after is already a breach.    │
   ├───────────────────────┼───────────────────────────────────────────────┤
   │ 3. WHAT COUNTS AS     │ Selling API access = caught. Shipping a       │
   │    "AS A SERVICE"     │ product with the model inside a feature =     │
   │                       │ not caught. Relaying to someone else's host = │
   │                       │ not caught. The definition is IN the licence; │
   │                       │ read it rather than guessing.                 │
   ├───────────────────────┼───────────────────────────────────────────────┤
   │ 4. WHERE YOU RUN IT   │ Access through the lab's own product or a     │
   │                       │ certified inference partner is exempt. Your   │
   │                       │ hosting choice changes your obligations.      │
   └───────────────────────┴───────────────────────────────────────────────┘
```

## The generalisable lesson

**A licence travels with a checkpoint, not with a lab or a brand.** Anyone who read the K2 terms
in 2025, concluded "Kimi is basically MIT", and carried that forward to K3 in 2026 would be
wrong in a way that matters — the K3 terms can require a signed agreement *before* commercial use,
which is a procurement timeline, not a compliance checkbox. Question 208 lists licence parity as
one of four axes on which an "open equivalent" can fail; this is that axis with a real example.

Two further things that are true of every licence in this category and are constantly elided:

* **Open weights is not open source.** Neither of these is an OSI-approved licence. Field-of-use
  and scale-conditioned clauses are exactly what the OSD excludes. Say "open weights" and mean it.
* **Neither is reproducible.** No training data, no training code. You can run and modify the
  artefact. You cannot rebuild it, and you cannot audit what went into it.

## What to do about it, concretely

* **Vendor the LICENSE file next to the weights and hash it.** The licence is part of the
  artefact, and version-to-version drift is the failure mode.
* **Re-run legal review on every version bump**, not on every vendor change. The lab is not the
  unit of compliance; the checkpoint is.
* **Write down which of the four boxes above you are in**, with the revenue figure you are relying
  on and the date. That note is what makes the next review cheap.
* **Check your inference provider's status** if you are relying on a carve-out for it.

## What an interviewer is listening for

That you read the modification rather than the base licence, and that you spot the difference
between an attribution clause and a gating clause without being led to it. Strong answers notice
that the revenue trigger is aggregate and affiliate-wide; the strongest notice that the obligation
attaches before commercial use rather than after.

## Where this stands, September 2026

Both licence texts above were read from the raw files in the model repositories and quoted, not
paraphrased from coverage. Licences get revised; the K2.6 terms were not verifiable from here at
all. Before shipping, open the LICENSE file in the repository for **the exact checkpoint you are
deploying** and read it yourself. That instruction is the only part of this answer with no expiry.
