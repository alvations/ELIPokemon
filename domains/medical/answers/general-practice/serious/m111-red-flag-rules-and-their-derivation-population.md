---
id: "m111"
slug: red-flag-rules-and-their-derivation-population
style: serious
category: general-practice
difficulty: advanced
question: "Why does a red-flag rule derived in secondary care behave differently at first contact, and what about such a rule fails to transport?"
tags: [red-flags, derivation-population, spectrum-bias, decision-rules, transportability]
---

# A rule arrives carrying the population it was built in, and the printed rule does not say so

m011 establishes that a likelihood ratio travels between settings and a predictive value does
not. m012 establishes that a red-flag screen is tuned for specificity and is therefore a poor
rule-out instrument. This question is the third thing, and it is the one that is usually left
implicit: a rule is not only a set of numbers applied to a population, it is a set of numbers
*produced by* a population. The features in it were chosen because they discriminated there. The
cut-points in it were fitted there. The outcome it predicts was defined and ascertained there.
Move the rule upstream to first contact and all three of those choices move with it, silently,
because none of them is printed on the rule (**mechanism**).

Load-bearing claims below are marked with what they rest on: **mechanism**, **definitional**,
**consensus** or **country-dependent**. A claim marked **mechanism** is checkable by reasoning. A
claim marked **country-dependent** needs the reader's own guidance, not this answer.

## Three populations, and what changes at each arrow

```
   THE LIFE OF A RULE. No figures are attached on purpose: every one of them is specific
   to a particular rule, and m011 and m012 already carry the worked arithmetic for what
   prevalence does to a 2x2. What this diagram is for is the list of things that move.

   ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
   │   DERIVATION     │ ───▶ │   VALIDATION     │ ───▶ │      USE         │
   │  a cohort, often │      │ a second cohort, │      │ the room you are │
   │  already referred│      │ often from the   │      │ actually in      │
   │                  │      │ same kind of unit│      │                  │
   └──────────────────┘      └──────────────────┘      └──────────────────┘
       chooses                   estimates                 inherits
       ─ which features          ─ how well it does        ─ all of it
         enter the rule            in a population
       ─ where each                like the first one
         cut-point falls
       ─ how the outcome
         was defined
       ─ how each feature
         was measured

   WHAT CROSSES THE SECOND ARROW UNCHANGED

     the rule's structure         yes — the same features, the same cut-points
     the likelihood ratio         approximately, and only if the spectrum is the same
     the prior                    NO. It is a property of the room  (see m011)
     the feature prevalences      NO. They are properties of the cohort
     the outcome definition       NO, if the downstream unit could confirm things that
                                  cannot be confirmed upstream
     the measurement              NO, if the feature was elicited by someone who already
                                  knew the referral had been accepted

   AND THE TERM WITH NO ARROW AT ALL

     the referral decision that assembled the derivation cohort. It is not a
     variable in the rule. It is the reason the cohort exists.
```

## The threshold was fitted where the prior was high

A cut-point is chosen to balance two error costs against a background rate (m081). Both the
costs and the rate are local, so a cut-point is a local object even when the feature it applies to
is universal (**mechanism**). A rule fitted downstream, where the proportion with the condition is
high, will sit at a point that makes sense there and will do one of two things upstream:

* **Flag almost everybody.** If the feature is common in the unselected population and the
  cut-point was set loosely because almost everyone in the derivation cohort had the disease
  anyway, then upstream the rule becomes a near-universal trigger. It has not become more
  sensitive. It has stopped discriminating.
* **Flag almost nobody.** If the cut-point keys on a feature that is a marker of established or
  advanced disease, then upstream — where disease is early, if it is present at all — the rule is
  inert, and its inertness looks like reassurance.

Which of the two happens is a property of the particular rule and not something that can be
predicted from the fact that it was derived downstream. That is why "was it validated in a
population like mine" is a better question than "is this a good rule" (**consensus**).

## The features themselves were chosen downstream, which is the subtler failure

Spectrum is the term for this and it is worth separating from prevalence. Prevalence is how many
people in the room have the condition. Spectrum is *what the condition looks like* in the people
who have it, and *what the alternatives look like* in the people who do not (**definitional**).
Both differ upstream, and they differ in ways that work against a transported rule:

1. **Disease is earlier upstream**, so late features are absent and a rule built around them
   loses sensitivity exactly where it is being asked to rule out.
2. **The differential is wider upstream**, so a feature that was specific downstream — because
   the only competing diagnoses in a referred cohort were the serious ones — becomes
   non-specific against a much larger field of benign alternatives.
3. **Features are measured differently.** A sign elicited in a unit, by someone examining a
   person a second time, with the referral letter in front of them, is not the same measurement
   as the same sign elicited at first contact in an unselected person (**mechanism**).
4. **The reference standard differs.** A rule whose outcome was confirmed by an investigation
   available downstream is predicting something that cannot be ascertained upstream, so the
   upstream user cannot even audit their own use of it.

## The circularity, stated plainly because it is the part that is easy to miss

The derivation cohort was assembled by the referral decision. That decision was made by
first-contact clinicians, using the features they had, including the features that later became
the rule. So a rule derived downstream has upstream judgement baked into the composition of its
own cohort, and using it upstream means using a rule to make a decision that helped determine
which people the rule was fitted on (**mechanism**). This is not a reason to discard such rules —
most of the useful ones were derived this way, because that is where the confirmed outcomes are.
It is a reason to treat a downstream-derived rule as a *description of a referred population*
rather than as a *test for an unselected one*.

## What can be done with a transported rule, in order of how much it buys

* **Read the derivation paper's setting section before its results section.** Recruitment,
  referral route and inclusion criteria determine whether anything else in the paper applies.
* **Prefer a rule validated at first contact when one exists**, and treat an
  unvalidated-upstream rule as a prompt rather than a decision (**consensus**).
* **Use the rule in the direction it was built for.** A rule-in instrument used to rule out is
  being misused regardless of where it was derived (m012).
* **Keep the safety-net independent of the rule.** If the rule's upstream sensitivity is unknown,
  the net is what carries the residual probability, and it has to be specified rather than
  implied (m012).
* **Audit upstream, locally.** The only way to find out what a transported rule does in a given
  practice population is to look at what it did there, which is a practice-level activity and not
  a reading activity.

## The human stakes, said plainly

Both failure modes land on people. A rule that flags almost everybody upstream sends well people
into investigation, with its procedures, its waiting, its time away from work and family, and its
lasting change in how someone understands their own body — the harm m084 describes, arriving
through a door marked *safety*. A rule that is inert upstream does something worse and quieter: it
supplies a reason to stop thinking. Somebody is told that the rule is negative, which they hear
as *this has been checked*, and the checking was done by an instrument that could not have found
their disease at the stage it was at.

The second of those is harder to see and harder to learn from, for the reason m084 gives: the
missed case comes back and is attributed to a consultation, while the over-flagged case generates
no feedback at all. So the pressure from experience pushes toward using more rules more loosely,
and the pressure from the arithmetic pushes the other way.

And a point about blame. A clinician applying a published rule to the population in front of them
is doing the thing they were taught to do, and the defect is in the gap between where rules are
made and where they are used. That gap is a property of how evidence is produced — confirmed
outcomes accumulate where the investigations are — and not a failure of anyone's diligence. It is
also why significant-event review is more useful than individual criticism when a transported
rule has failed.

## What an examiner digs into next

Whether the candidate distinguishes prevalence from spectrum, and can say which of the two breaks
a likelihood ratio. Then the direction of use: rule-in against rule-out, and which one the rule
was built for. Then the harder one — whether they can name what in a rule is a property of its
cohort rather than of the disease, and say how they would find that out from a paper. Then the
circularity, which separates a candidate who has read a derivation study from one who has read a
summary of it. Then what they would actually do at first contact with a rule whose upstream
performance is unknown, and whether the answer includes an explicit net rather than a softer
version of the rule.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The derivation and validation publications for whichever specific rule is in question, read
  for their setting, recruitment and reference standard rather than for their headline
  performance figures.
* Any current reporting-standards statement for diagnostic accuracy studies, issued by the
  relevant methodology group, for what a study is required to disclose about setting and
  spectrum.
* Any current reporting-standards statement for multivariable prediction model studies, issued by
  the relevant methodology group, for the derivation-validation-impact sequence and for what
  external validation means.
* A standard textbook of clinical epidemiology or clinical prediction modelling, for spectrum
  effects, for the distinction between internal and external validation, and for why a model's
  performance degrades on transport.
* The suspected-cancer or urgent-referral criteria issued by the national or regional body
  governing the reader's own practice, which is where the locally authoritative red-flag lists
  live and which say what population they were written for (**country-dependent**).
* The reader's own organisation's audit of referrals made under a given rule, which is the only
  local evidence of what that rule does in that population.

## Scope and safety

This is revision material about how a decision rule behaves when it is moved between
populations, written for someone already training in or qualified for the field. It is not a
clinical reference, not a decision aid, and nothing here should inform whether any individual is
referred or investigated — that belongs with the clinician who has assessed them and with current
local criteria. No rule is named, reproduced or paraphrased here, and no feature, cut-point,
sensitivity, specificity or timescale appears, on purpose: those belong to specific rules, they
are revised, and a rule recalled from a summary is one of the recognised ways rules fail. The
reader's own local guidance is the authority on which rules are in force and what they say. If
someone is unwell right now, the relevant action is to contact local urgent care or the local
emergency number, not to read this.

## Where this stands, October 2026

The methodological claims here — that transportability depends on spectrum as well as prevalence,
that external validation is a separate step from derivation, and that a rule-in instrument is
not a rule-out instrument — are settled and are not expected to move. What moves is the stock of
rules: which exist, which have been validated at first contact, which have been withdrawn, and
which have been superseded by a model that includes a laboratory value rather than a clinical
feature. The number of rules validated specifically in primary-care populations has grown over
the last decade and is still small relative to the number in use. Whether a particular rule has
been validated upstream has to be checked against the current literature and against local
guidance rather than taken from here, as of October 2026.
