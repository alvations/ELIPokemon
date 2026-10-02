---
id: "m100"
slug: biomarker-driven-treatment-selection
style: serious
category: oncology
difficulty: advanced
question: "Why are a biomarker test and the drug it selects for treated as one object rather than two, and what goes wrong when they are separated?"
tags: [biomarkers, companion-diagnostics, assay-validation, pre-analytics, cut-offs]
---

# The evidence is about a population an assay defined, so the assay is part of what was shown to work

A drug licensed for a biomarker-defined population was tested in people chosen by a **specific
test**: a particular antibody or probe or panel, on a particular platform, applied to a specified
specimen prepared a specified way, read by a specified scoring algorithm at a specified cut-off.

The trial result is a statement about **that selected population**. Change the test and you are
selecting a different population, even when you believe you are measuring the same molecule. The
drug has not changed; the thing the evidence is about has.

That is why the test and the drug are developed together, authorised together and — this is the
part that gets lost — must be *used* together. A result from a different assay, a different
platform, a different specimen type or a different scoring convention is not a cheaper route to
the same decision. It is a different measurement being used to make a decision that was validated
on another one.

Each load-bearing claim below is marked with the kind of thing it is: **mechanism** (derivable
from how the measurement works), (**definitional**) (true because a classification or regulation
says so), (**consensus**) (widely agreed professional practice), or (**country-dependent**)
(varies by nation, region or institution, and changes).

## The chain, and the fact that every link is part of the test

```
   THE PERSON                       ┌───────────────────────────────────┐
       │                            │  EVERY ONE OF THESE IS PART       │
       ▼                            │  OF "THE TEST". Changing any of   │
   which lesion, which specimen ────┤  them is changing the assay.      │
       │                            └───────────────────────────────────┘
       ▼
   PRE-ANALYTIC    time to fixation, fixative, fixation duration,
                   decalcification, block age, section thickness
       │
       ▼
   ANALYTIC        the antibody clone or probe set or panel, the
                   platform, the protocol, the controls
       │
       ▼
   INTERPRETIVE    which cells are counted, what counts as positive,
                   the scoring algorithm, the CUT-OFF
       │
       ▼
   THE RESULT ───► and only now does the licensed indication apply,
                   and only if the whole chain matches the one the
                   evidence came from

   ─────────────────────────────────────────────────────────────────────────────

   TWO KINDS OF TEST, AND THEY ARE NOT THE SAME OBJECT

   COMPANION                             COMPLEMENTARY
   ┌───────────────────────────┐         ┌───────────────────────────┐
   │ required to select        │         │ informs the decision,     │
   │ whether to treat at all.  │         │ does not gate it.         │
   │ A result is a GATE.       │         │ A result is a WEIGHT.     │
   └───────────────────────────┘         └───────────────────────────┘
     getting it wrong decides             getting it wrong shifts a
     who is treated                       judgement

   ─────────────────────────────────────────────────────────────────────────────

   AND THE CONSEQUENCE NOBODY LIKES:

      ASSAY PERFORMANCE *IS* TREATMENT PERFORMANCE.

      a false negative  ──►  an effective treatment is never offered
      a false positive  ──►  toxicity is accepted for no possible benefit

      Both are clinical outcomes of a laboratory property.
```

## Why the pairing is a regulatory object and not a convention

Where a drug's authorisation is restricted to a biomarker-defined population, the test that
defines it is typically authorised alongside it, and the label refers to the test or the kind of
test required (**definitional**, strongly (**country-dependent**) — the regulatory machinery, the
terminology and even the categories differ between jurisdictions).

The distinction worth learning is **companion** against **complementary** (**definitional**):

* A **companion diagnostic** is required in order to select. The result is a gate; a negative
  means the drug is not used.
* A **complementary diagnostic** informs without gating. The result shifts the weight of a
  decision that can still go either way.

The two are not interchangeable and a service treating a complementary result as a gate, or a
companion result as advisory, is making a category error with a direct clinical consequence
(**consensus**). Which assays sit in which category is jurisdiction-specific and changes.

## One specimen, two assays, and which decision becomes available

A point that follows directly and is rarely stated: for a given specimen, **which test was run
determines which decision is available**, and the specimen does not tell you which test to run
(**mechanism**).

That is not a philosophical observation. It is why the order matters — a limited specimen consumed
by one assay may not support the one that would have mattered; why the sequence of tests is part
of a testing pathway rather than a laboratory preference; and why "we tested the tissue" is an
incomplete answer to "was this person eligible". Two different tests on one specimen can both be
performed correctly and lead to different treatments, because each is attached to a different body
of evidence.

The practical form of this: the question to ask of a molecular report is not only what it found
but **what was looked for, in what order, and what the specimen can still support**
(**consensus**, (**country-dependent**) in how testing pathways are specified).

## The cut-off is a decision, not a biological boundary

Much of what is measured is **continuous**: an amount of protein, a proportion of cells, a copy
number, a fraction of reads. What is reported is a category.

So the cut-off is a convention, chosen to be reproducible between observers and to correspond to a
decision, and it is **disease-specific and assay-specific** — the same molecule is scored by
different algorithms, over different cell populations, at different cut-offs, in different
diseases (**definitional**, **consensus**). A score reported without its scoring system and the
disease it was validated in is not a usable result.

This is the same argument this specialty's answer on surgical margins makes about a continuous
distance reported in bands, and it is not re-derived here. The additional point specific to
biomarkers is that the cut-off was often chosen **because a trial used it**, which makes it a
property of the evidence rather than of the biology, and makes "which cut-off" and "which trial"
the same question.

## Pre-analytics are part of the result, not a preamble to it

The commonest way a biomarker result is wrong has nothing to do with the assay itself
(**mechanism**, **consensus**).

Time from removal of the tissue to fixation, the fixative used, how long fixation lasted, whether
the specimen was decalcified, how old the block is and how the sections were cut all affect what
can be detected. An assay validated on one preparation process is not validated on another, which
is why acceptable pre-analytic conditions are specified in the assay's instructions and are part
of what the laboratory is accredited for. It is also why cytology specimens, needle washings and
small-volume samples are a **separate validation question** rather than a smaller version of the
same one.

The practical form of this: "the test was negative" and "the test was performed on a specimen the
test is validated for" are two claims, and only the second makes the first interpretable.

## Analytic equivalence is demonstrated, never assumed

Different antibody clones against the same protein, different probe sets against the same
rearrangement, and different sequencing panels covering the same gene do **not** give
interchangeable results (**consensus**). Concordance between two assays is an empirical question
answered by comparison studies, and the answer is frequently "good but not equivalent", which is
exactly the range in which a cut-off near the decision boundary matters most.

Three consequences (**consensus**, (**country-dependent**) in how they are enforced):

* A **laboratory-developed test** used in place of an authorised one requires local validation
  against a defined comparator, and the validation is part of the result's meaning.
* **External quality assurance** schemes exist because laboratories drift, and participation is a
  condition of accreditation in many systems.
* **Reporting the method** is not bureaucratic detail. A result without the clone, platform and
  scoring convention cannot be compared to the evidence it is meant to be matched against.

## What goes wrong when the two are separated

The failures are symmetrical and both are clinical (**mechanism**):

* A **false negative** withholds an effective treatment from someone who would have benefited, and
  it is invisible — nobody ever learns what would have happened.
* A **false positive** commits someone to a treatment with real toxicity and no mechanism of
  benefit. This specialty's earlier answers put that case as a type-effectiveness zero rather than
  a reduced effect, and the point holds: without the target, the drug has no route to act, so the
  toxicity is the whole of what is received.

Two further failures are about the evidence rather than the individual:

* **A trial using a poorly discriminating assay dilutes its own effect**, because the treatment
  arm contains people who could not have benefited. An apparently negative trial of a targeted
  agent is therefore sometimes a statement about the assay (**consensus**).
* **A drug shown to work in a selected population being used in an unselected one** inherits none
  of the evidence, which is the mirror image and is the more common error in practice.

## Where the organ-first logic inverts, and what a panel returns

Some indications are defined by the molecular alteration **irrespective of the tissue of origin**
(**consensus**, (**country-dependent**) in which are approved and funded). Three things change:

* Who orders the test, and when — because the alteration can appear in diseases where nobody
  routinely looked for it.
* What the limiting factor is — the assay's validation **across** diseases rather than within one,
  since prevalence, specimen types and the relevant cut-off all vary by site.
* Where the result is handled, because a finding in a disease with no local pathway needs a forum.
  That forum is the molecular tumour board or the multidisciplinary meeting, which the previous
  answers in this specialty describe.

And a multiplex panel returns more than the question asked. Some findings have a matched option,
some have one only in a trial, some have one only in another disease, and some have none at all;
and the test frequently returns nothing actionable, which is a result and not a failure
(**consensus**).

Tiered reporting exists to keep those separable, so that a clinician reading the report can tell a
finding with established clinical significance from one with none. Which tiers are used, and
whether a finding is reportable at all, follow local convention (**country-dependent**). The
reason this matters for the subject of this answer: a panel result is **not** a companion
diagnostic result unless that panel is the one validated for that indication, and a panel's
detection of an alteration does not import the evidence attached to a different assay for it.

## The human stakes, said plainly

Everything above is measurement and regulation, which is the right register for understanding what
a result can bear. It is not the register for being the person whose result it is.

A laboratory property decides, for a particular person, whether a treatment is offered. That is an
uncomfortable fact and it is the plain truth of this subject: being told "you are not eligible"
and being told "the test on your sample did not show the thing the drug needs" are the same event
described at two different levels, and the second is both more honest and harder to say. Where a
result is borderline, or the specimen was marginal, or a different assay might answer differently,
that is information the person has an interest in — not because it changes the decision today, but
because it is the reason the decision is what it is.

The waiting also deserves naming. Molecular results take time, the time is rarely explained, and
it falls in the period immediately after a diagnosis when nothing else is happening and the delay
is experienced as inaction. Saying what is being tested, why it takes as long as it does, and what
each possible answer would mean costs very little and changes that period considerably.

## What an examiner digs into next

* Why is the trial's eligibility assay part of what the trial demonstrated?
* Distinguish a companion from a complementary diagnostic, and give the consequence of confusing
  them in each direction.
* Name four pre-analytic variables and say what each can do to a result.
* Two assays for the same protein are "highly concordant". Why is that not the same as
  interchangeable, and where does the difference bite hardest?
* A trial of a targeted agent is negative. Give two explanations that are about the assay rather
  than the drug.
* What changes when an indication is defined by the alteration rather than the organ?
* Why is a panel's detection of an alteration not automatically a companion diagnostic result?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* The summary of product characteristics or equivalent label for the agent, published by the
  licensing authority in your country — for the biomarker-defined population and for what the
  label says about the test required to identify it. This is the single most useful document for
  this answer.
* The assay's own instructions for use, published by its manufacturer, for the validated specimen
  types, the acceptable pre-analytic conditions, the scoring algorithm and the cut-off. A result
  interpreted without this document is being interpreted against an assumption.
* Your national or regional guidance for biomarker testing in the disease, for which tests are
  recommended, at which point in the pathway, and which assays are accepted. These differ sharply
  between countries and are revised frequently.
* Your own laboratory's accreditation scope and its external quality assurance participation,
  which together are the evidence that the test in front of you performs as the comparison studies
  say.
* The published guidance on variant and biomarker reporting tiers from the professional body that
  issues it in your region, for how a finding's clinical significance is to be classified.
* The primary literature, for concordance studies between named assays and for the trials that
  established each cut-off — both of which are specific, and are where these questions were
  actually settled.

## Scope and safety

This is revision material about why a test and a drug are one object, written for someone already
training in the field. It has had no clinical review. **No assay, antibody clone, platform, gene,
drug, cut-off or concordance figure appears here, and none should be inferred** — those are
assay-specific and disease-specific, they differ between countries and laboratories, and they are
revised frequently; the label, the assay's instructions for use and the local guidance in force
where you work are the authority, and this is not. It is not a testing protocol, not a reporting
guide and not a decision aid, and it describes no individual's specimen or situation. Anyone
affected by cancer — their own diagnosis or someone else's — should be talking to the clinical
team looking after that person, who have the specimen, the report and the history, none of which
are here.

## Where this stands, October 2026

The argument is structural and will not date. Evidence obtained in a population defined by a test
is evidence about that selection; pre-analytics, analytic method and scoring convention are all
part of the test; and a laboratory property therefore determines a clinical outcome. None of that
depends on which assays are current.

Everything concrete moves, and moves quickly. Which drugs are restricted to biomarker-defined
populations, which assays are authorised alongside them, the terminology and categories used by
each regulator, the cut-offs, which indications are tumour-agnostic, and whether a multiplex panel
is accepted in place of a single-analyte companion test are all actively changing and unevenly
adopted between countries. Tiered reporting conventions are also being revised. No assay, clone,
cut-off or figure is quoted here, deliberately: those belong to the current label, the current
instructions for use and the current guidance rather than to a revision note like this one.
