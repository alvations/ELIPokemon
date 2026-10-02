---
id: "m029"
slug: response-assessment-and-surrogates
style: serious
category: oncology
difficulty: advanced
question: "Why is deciding whether a cancer treatment is working harder than it sounds, what does a structured response criterion actually buy, and why is a better scan not the same thing as a longer life?"
tags: [response-assessment, surrogate-endpoints, imaging, measurement, endpoints]
---

# Three different questions get asked as one, and only the first is measurable

*Has the imaging changed?* is a question about images. *Has the disease changed?* is a question
about biology. *Will this person live longer, or feel better?* is a question about a person. These
are three questions, they are answered by three different kinds of evidence, and almost every
muddle in this area comes from treating an answer to the first as an answer to the third.

**Claims are marked by kind:** **mechanism** (derivable from how the measurement or the biology
works), **definitional** (true because a criterion says so), **consensus** (widely agreed
professional practice), **country-dependent** (varies by nation, region or institution, and
changes).

## The chain, and where information is lost at each link

```
   what is actually there
        │
        │  a three-dimensional, irregular, biologically heterogeneous volume
        ▼
   ACQUISITION          slice thickness, contrast timing, machine, protocol
        │               ── information is quantised here, before anyone looks
        ▼
   SELECTION            which lesions are measured, and how many of them
        │               ── a rule, not a fact. Different rule, different number.
        ▼
   MEASUREMENT          a linear diameter standing in for a volume,
        │               placed by a human being with a cursor
        │               ── two readers differ; the same reader differs twice
        ▼
   SUMMATION            diameters added into one number
        │               ── direction of change in the sum can hide
        │                  lesions moving in opposite directions
        ▼
   CATEGORY             the number crosses a threshold and becomes a word
        │               ── definitional. The word is a convention.
        ▼
   INFERENCE            ... and here somebody says "it's working"
                        ── which is a claim about biology, drawn from a
                           convention applied to a quantised proxy

   EVERY LINK IS LOSSY, AND THE LOSS IS ON PURPOSE.  The point of the chain
   is not accuracy. It is that two readers in two countries produce the SAME
   WORD from the same images. That is a different objective, and it is the
   right one for the job.
```

## Why measuring it is hard, mechanistically

**A diameter is a proxy for a volume** (**mechanism**). One linear measurement standing in for an
irregular three-dimensional object loses information no matter who places the cursor, and a change
in a diameter is a much smaller change than the corresponding change in volume. The choice is
deliberate: diameters are far more reproducible between observers than volumes, and
reproducibility is what the chain is optimised for.

**Measurement noise is not small relative to the changes of interest** (**mechanism**). The same
lesion measured twice — by two readers, or by one reader on two occasions, or on two machines —
gives two numbers. Any threshold for declaring change must therefore be set *above* that noise, or
the criterion will report changes that are purely measurement.

**A sum can conceal its own components** (**mechanism**). Summed diameters moving one way is
compatible with individual lesions moving in both directions, which is why criteria also require
attention to unequivocal new disease rather than relying on the sum alone.

**And a lot of disease is not measurable in this sense at all** (**consensus**). Bone disease,
effusions, peritoneal and leptomeningeal disease, diffusely infiltrating disease: present,
consequential, and not amenable to a diameter. Criteria handle these as a separate category rather
than pretending otherwise — which is honest, and also means the headline category rests on the
measurable subset.

## What a structured criterion buys, and what it does not

The widely used framework for solid tumours specifies which lesions may be measured, how many, how
they are summed, and what change in the sum corresponds to each response category. Lymphomas use a
different framework built on metabolic imaging, because a nodal mass that shrinks slowly is poorly
described by size alone. Immunotherapy-specific variants exist because apparent early enlargement
can precede response, so they require confirmation before progression is declared
(**definitional**, **consensus**).

The thresholds are chosen so that a declared change is larger than the measurement noise described
above — a decrease of roughly a third in the summed diameters for a partial response, and an
increase of roughly a fifth together with an absolute minimum increase for progression, in the
solid-tumour framework. **Those are approximations given here to show the reasoning, not figures
to quote**; the exact numbers, and the rules for new lesions and for non-measurable disease, are
definitional and belong to the published criteria, which are revised. Read them there.

What the criterion buys:

* **Agreement.** Two radiologists, two centres, two trials, one vocabulary.
* **A threshold above the noise**, so a reported change is probably not a cursor.
* **A rule fixed in advance**, which removes the degree of freedom that would otherwise let the
  reader choose the answer.

What it does not buy:

* **Biological truth.** A category is a convention applied to a proxy.
* **Clinical meaning.** A response category says nothing on its own about how long someone will
  live or how they feel.
* **Comparability across frameworks.** A response under one criterion is not the same statement as
  a response under another, and mixing them is a category error.

And several ways a category misleads even on its own terms (**mechanism**, **consensus**): a
lesion that becomes cystic or necrotic may not shrink while changing profoundly; a treated lesion
can leave a residual mass that is fibrosis rather than disease; a non-shrinking lesion can still
be metabolically dead; and a tumour marker is an adjunct that can move for reasons unrelated to
the disease, never a substitute for the assessment.

**The most important of these is the top of the scale rather than the bottom.** A complete
response means *no disease visible at the resolution of the modality used, under the rules of the
criterion applied* (**definitional**). It does not mean no disease. Below the resolution of the
instrument the category cannot distinguish a small amount from none, and that distinction is
exactly the one clinical decisions after a complete response are built around — which is why
treatment and surveillance do not simply stop when the images clear. Small and unresolvable is not
the same property as absent.

## Surrogate endpoints: why they exist and how they fail

A surrogate endpoint is a measurement used in place of the outcome that actually matters, because
it occurs earlier or is easier to observe. Response rate and the various progression-free and
disease-free intervals are the common ones; overall survival and quality of life are the outcomes
they stand in for (**definitional**).

They exist for a real reason — waiting for the definitive outcome means waiting years, and
sometimes no useful comparison is possible by then — and they fail in characteristic, mechanistic
ways:

* **A surrogate measured on a schedule inherits the schedule** (**mechanism**). An interval ending
  at a scan depends on when the scans were. Two arms imaged on different schedules are not
  comparable, and lengthening the interval between scans lengthens the measured interval without
  changing anything about the disease.
* **Unblinded assessment biases it** (**mechanism**). A reader who knows the arm is a reader with
  a thumb on the scale, which is why independent blinded review exists.
* **Informative censoring** (**mechanism**). If people leave the study for reasons related to how
  they are doing, the remaining data are not a random sample.
* **The chain can break at the last link** (**mechanism**). A treatment can delay the measured
  event without extending life — because of what happens afterwards, because subsequent treatment
  differs between arms, or because the mechanism that moved the surrogate does not translate.
* **Validation is a trial-level claim, not a patient-level one** (**consensus**). That people
  whose disease responds tend to do better is a *prognostic* observation and does not establish
  that a treatment which improves response improves survival. Establishing that requires
  correlation between treatment effects across many trials, which has been done convincingly in
  some diseases and not in others.

**The field genuinely disagrees** about which surrogates are acceptable for which purposes, and
regulators in different jurisdictions weigh them differently (**consensus**,
**country-dependent**). Anyone who presents this as settled has not read the argument.

## Why a better scan is not a longer life

Stated plainly, because it is the point of the question.

An imaging response is an observation about images. It is evidence — real evidence, and often the
best available early — that something is happening. It is not the same proposition as *this person
will live longer*, and it is not the same proposition as *this person will feel better*. Those are
different claims requiring different evidence, and the second is frequently the one that matters
most and is measured least. It is entirely possible for imaging to improve while a person feels
worse, because the treatment doing the shrinking has its own costs.

And a population statistic — of any kind, whether a response proportion or a survival figure — is
an average over a large and varied group, assembled in the past, under the treatments and the
imaging of that time. It does not contain the information needed to say what will happen to any
individual within it, and any individual differs from the average in ways the average cannot
express. That is a limitation of the arithmetic rather than a failure of nerve, and it is why no
such figure appears in this answer.

## What an examiner digs into next

* Why is a diameter preferred to a volume, given that a volume is more faithful?
* Why must a response threshold be larger than you might expect?
* How can a sum of diameters fall while the disease is progressing?
* How does the scan interval change a progression-free interval, with no change in biology?
* What is the difference between a prognostic association and a validated surrogate?
* Name a situation in which imaging improves and the person is worse off.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The response-evaluation criteria your centre or trial actually uses, in their current published
  revision, from the group that maintains them — the authority for every threshold, every
  lesion-selection rule and every category definition sketched above.
* The disease-specific response framework where one applies, including the metabolic-imaging-based
  classification used in the lymphomas, as published by the body that maintains it.
* The immunotherapy-specific variant of the solid-tumour criteria, from the same source, for how
  apparent progression is confirmed.
* The regulatory guidance on acceptable endpoints published by the medicines regulator in your
  jurisdiction, which differs between jurisdictions and changes.
* The protocol of any trial whose results you are reading, for its imaging schedule, its blinding
  arrangements and its pre-specified endpoints — the three things that determine what its headline
  number means.

## Scope and safety

This is revision material about measurement and inference, pitched at someone already training in
the field. It has had no clinical review. No threshold, interval or criterion is quoted here as
fact, and none should be acted on; the published criteria in their current revision, and your
local radiology and trial protocols, are the authority, and this is not. Criteria and the
regulatory acceptability of surrogate endpoints differ between countries and are revised. Nothing
here describes any individual's situation, and nothing here interprets anybody's scan. Anyone
affected by cancer — their own diagnosis or someone else's — should be talking to the clinical
team looking after that person, who have the images, the history and the context, none of which
are here.

## Where this stands, October 2026

The reasoning is durable: a diameter proxies a volume, a threshold must exceed measurement noise,
a category is a convention, and a surrogate is a claim about a chain of inference whose last link
has to be demonstrated rather than assumed. The specifics are not durable: criteria are revised,
disease-specific and modality-specific frameworks multiply, and the endpoints regulators accept
move and differ between jurisdictions. The two approximate thresholds mentioned above are given to
show the shape of the reasoning and are explicitly not quoted as the criterion; no trial,
guideline number or survival figure appears here, deliberately, because those are the facts that
date and the ones most damaging to get wrong.
