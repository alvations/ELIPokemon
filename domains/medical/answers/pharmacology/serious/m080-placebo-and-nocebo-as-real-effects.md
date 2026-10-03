---
id: "m080"
slug: placebo-and-nocebo-as-real-effects
style: serious
category: pharmacology
difficulty: intermediate
question: "In what sense are placebo and nocebo effects real and measurable, and why does the placebo arm of a trial not actually measure the placebo effect?"
tags: [placebo, nocebo, trial-design, regression-to-the-mean, attribution]
---

# The placebo arm measures a sum. The placebo effect is one term in it, rarely the largest.

Two sentences carry this whole topic, and they are routinely collapsed into one.

The **placebo response** is what you observe in the people who received the inert intervention.
The **placebo effect** is the part of that response caused by the context of being treated —
expectation, conditioning, the ritual, the attention. The first is a measurement. The second is an
inference from it, and you cannot make that inference from a placebo arm alone, because the arm
contains several other things that would have happened anyway (**definitional**).

Everything useful in this topic follows from taking that difference seriously, including why the
effects are real, why they are smaller than the headline figures suggest, and why nocebo is the
part with the most direct consequences for practice.

Claims below are marked inline with what they rest on: (**mechanism**), (**definitional**),
(**consensus**), or (**country-dependent**).

## What is actually inside a placebo arm

```
   OBSERVED CHANGE in the placebo arm  =  the sum of all of these
   ─────────────────────────────────────────────────────────────────────────────────────
   1  NATURAL HISTORY            many conditions improve, relapse and remit on their
                                 own. Enrol people at their worst and most will be
                                 better later whatever you do.

   2  REGRESSION TO THE MEAN     a consequence of the ENTRY CRITERION, not of biology.
                                 If entry requires a measurement above a threshold, and
                                 the measurement has any noise, the people enrolled are
                                 over-represented by those whose noise was high that
                                 day. Measure again and the group mean falls.
                                 This is arithmetic. It would happen in a spreadsheet.

   3  MEASUREMENT and REPORTING  repeated measurement improves with practice; scales
                                 have ceilings and floors; observers who expect
                                 improvement grade it; participants who like the team
                                 report what they think is wanted.

   4  TRIAL PARTICIPATION        more monitoring, more contact, better adherence to
                                 everything else, co-interventions, a reason to look
                                 after yourself.

   5  THE PLACEBO EFFECT PROPER  expectation, conditioning, meaning, the ritual of
                                 being treated. ◄── THE ONLY TERM THE WORD NAMES
   ─────────────────────────────────────────────────────────────────────────────────────

   To isolate term 5 you need a NO-TREATMENT arm as well as a placebo arm, so that
   terms 1-4 appear in both and cancel. Most trials do not have one, because a third
   arm costs participants and because recruiting people to receive nothing is hard.

   CONSEQUENCE: almost every "the placebo effect was X%" figure in circulation is a
   PLACEBO RESPONSE, which is terms 1-5 together. The quantity is real. The label on
   it is wrong, and it is wrong in a direction that overstates term 5.
```

Term 2 is the one worth being able to explain cold, because it is the one that sounds like biology
and is not. It is a property of selecting on a noisy measurement, it has nothing to do with
treatment, and it is the reason a single-arm before-and-after study of almost anything will look
encouraging (**mechanism**).

## What is genuinely established about term 5

The effect is real, in the ordinary sense that it is reproducible, measurable, and has mechanisms
that can be studied. The two best-characterised are **expectation**, which can be manipulated
experimentally by what participants are told, and **conditioning**, where a previously paired cue
produces a response on its own (**consensus**).

Three qualifications belong with that, and leaving any of them out makes the topic either mystical
or dismissive.

* **The effect is much better demonstrated for subjective outcomes than for objective ones.**
  Pain, nausea, fatigue, mood and global ratings move; objective physiological measures move much
  less or not at all. The standard illustration is asthma, where placebo and sham interventions
  have produced clear symptomatic improvement with far smaller changes in measured airflow — the
  person feels better and the obstruction is largely still there (**consensus**). That gap is the
  whole reason objective endpoints exist.
* **There is no good evidence that it alters the natural history of a structural disease.** It
  does not shrink a tumour, clear an infection or heal a fracture. Treating "the placebo effect is
  real" as licence for anything is the error this qualification exists to block (**consensus**).
* **Deception may not be required.** Open-label placebo — telling people they are receiving an
  inert preparation and why it might still help — has produced measurable effects in several
  trials, mostly in symptom-defined conditions. That finding is interesting, it is from the
  primary literature rather than from guidance, and the size and durability of the effect are
  still actively argued about. Treat it as a live research result, not as settled practice.

## Nocebo: the same mechanism, sign reversed, bigger consequences

Nocebo is the production of **adverse** symptoms by expectation, and it is measurable in exactly
the place where it is easiest to overlook: the placebo arms of trials, where participants taking
an inert preparation report adverse effects, discontinue because of them, and sometimes do so at
rates not far below the active arm's (**consensus**).

Three determinants are reasonably well established (**consensus**):

1. **What the person was told**, including the wording and the format. A list of possible symptoms
   read out raises reporting of those symptoms.
2. **Prior experience**, their own and that of people they know.
3. **The salience of the information** — a widely publicised concern about a drug class is
   followed by more reporting of the symptoms concerned, and by more discontinuation.

That third one puts nocebo squarely in the territory of public communication rather than of the
consultation alone, and it is why professional bodies have written about how risk is described.

**And here is the tension, which is real and not resolved.** Informed consent requires that people
be told about possible adverse effects. Telling them measurably increases the rate at which they
experience those effects. Both of those statements are true. The proposals for living with it —
describing risk in absolute rather than relative terms, saying what proportion tolerate the
medicine rather than only what proportion do not, offering the detail rather than reciting it,
avoiding reading a symptom list aloud unprompted — are practice guidance, they differ between
professional bodies, and none of them dissolves the tension (**country-dependent**).

## The design that actually settles an attribution

For an individual, the question "did this drug cause this symptom" is answerable, and the method
is worth knowing because it is the only honest alternative to guessing.

```
   A BLINDED, RANDOMISED, WITHIN-PERSON RE-CHALLENGE   (an "n-of-1" design)

   the person receives, in randomised order, blinded periods of:
       active drug        ──┐
       identical placebo  ──┤  with symptom scores recorded in each period
       (repeated)         ──┘

   if symptoms track the ACTIVE periods   ──► the drug is implicated
   if symptoms occur in BOTH equally      ──► the symptom is real and the
                                              attribution to the drug is not
                                              supported
   if symptoms occur in NEITHER           ──► something else changed

   Note what the middle branch does NOT say. It does not say the symptom was
   imagined. It says the symptom was present with and without the drug, which
   is a statement about CAUSE, not about whether anything happened.
```

That design has been used both in trials and, in some systems, as a clinical service for people
with disputed drug intolerance. Whether it is available where you work is (**country-dependent**),
and it is not something to improvise — unblinded self-experimentation reintroduces every term in
the first diagram.

## Why all of this matters for reading evidence

* **An uncontrolled before-and-after observation cannot distinguish any of the five terms.** That
  is the single most useful consequence, and it applies to a case series, to an audit, to a
  personal impression and to a product's own testimonials equally.
* **Blinding exists to equalise expectation between arms**, not out of courtesy. An unblinded
  trial of a symptomatic treatment has term 5 loaded onto one arm, which is a bias of unknown size
  in a known direction (**mechanism**).
* **A large placebo response makes a trial bigger.** If both arms improve substantially, detecting
  the difference between them needs more participants. That is why trials in pain, depression,
  irritable bowel and migraine are large, and it is a design consequence rather than a
  disappointment (**mechanism**).
* **Active-controlled trials do not escape it.** They move the problem rather than removing it:
  both arms carry terms 1 to 5, which is helpful, but neither tells you whether either drug beats
  nothing.

## Ethics, briefly and clearly

Prescribing an inert preparation while implying it is active is **deception of a patient**, and
the mainstream professional position is that it is not acceptable (**consensus**). The detail —
what counts as an impure placebo, whether a low-dose or subtherapeutic prescription falls under
it, what must be documented — differs between national professional bodies
(**country-dependent**).

What is unambiguously acceptable, and is in fact what good practice already consists of, is using
the non-specific components **honestly**: explaining what is happening and why, saying what to
expect and when, being the same person next time, and making a clear plan. Those are the
ingredients of term 5 and they require no inert tablet. The practical conclusion of the whole
topic is not "placebos work" but **"context is part of every treatment, so attend to it
deliberately instead of leaving it to chance."**

## The human stakes, said plainly

The word "nocebo" is dangerous in one specific way, and it has to be said without hedging.

**A symptom produced by expectation is a real symptom.** The person is not lying, is not imagining
it, and is not failing a test of character. The physiology of a nocebo symptom is the physiology
of that symptom. So "it is probably nocebo" is never a reason to stop taking a report seriously,
and using the word to close a conversation is a misuse of it. The correct sequence is the reverse:
take the symptom at face value, then test the attribution if the attribution matters, which is
what the blinded re-challenge above is for.

The cost of getting this wrong runs both ways. Someone whose reported symptoms are attributed to
expectation and dismissed may stop reporting anything, which removes the only signal there was.
Someone whose symptoms are attributed to a drug without testing may lose a medicine that was
helping them and gain the belief that they cannot tolerate its whole class. Both are common and
both are avoidable by the same move: believe the symptom, interrogate the cause.

There is also a point about how risk is discussed that is worth separating from the clinical one.
Public information about medicines has to be honest, and honest information sometimes increases
symptom reporting. The answer to that is not to withhold information; it is to present it in a
form people can use — absolute numbers rather than relative ones, what proportion do well as well
as what proportion do not. Deciding not to tell someone something because they might then feel it
is not an available option.

Nothing in this answer indicates whether any symptom anyone has is or is not caused by their
medicine, and nothing in it is a reason to continue or stop anything. That is a question for the
person's own prescriber or pharmacist, who can look at the timing, the drug and the alternatives,
and who can arrange a proper re-challenge if one is warranted.

## What an examiner digs into next

* Name the five terms in a placebo arm's observed change, and say which one the phrase "placebo
  effect" refers to.
* Regression to the mean is arithmetic rather than biology. Explain why the entry criterion causes
  it.
* What extra arm would you need to measure a placebo effect, and why do most trials not have one?
* Why is the placebo effect much better demonstrated for symptoms than for objective physiological
  measures, and what is the asthma illustration?
* Give the design that can settle whether a drug caused a given person's symptom, and say what the
  "symptoms in both periods" result does and does not mean.
* State the tension between informed consent and nocebo, and say why it is not resolved.
* Why does a large placebo response make a trial larger?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* **A current clinical trials methodology textbook**, for the decomposition above, for regression
  to the mean, and for why blinding and control arms are constructed as they are. This is
  definitional material and a textbook is the right source for it.
* **The Cochrane Library's systematic reviews of placebo interventions**, which are
  the standard reference for what placebo arms do and do not show across conditions, and for the
  subjective-against-objective distinction. They are regularly updated and their conclusions have
  been debated.
* **The primary literature**, for every quantitative claim in this topic without exception: the
  size of placebo responses by condition, the open-label placebo trials, adverse-event reporting
  in placebo arms, and the n-of-1 re-challenge studies. This answer states no figures, because the
  figures are condition-specific, design-specific and contested.
* **Your national professional regulator's and medical association's guidance on prescribing
  placebos and on honesty with patients**, for the ethical position where you practise. The
  position is broadly consistent between countries; the detail and the wording are not.
* **Your national body's guidance on communicating risk and benefit to patients**, for absolute
  against relative risk presentation, and for what is recommended about describing adverse
  effects.
* **Your national medicines safety body's material on the reporting consequences of publicity
  about a drug class**, where it exists, for the third nocebo determinant.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. It states no figure for any placebo or nocebo response, deliberately: those
are condition-specific and contested, and a number of that kind lifted from a revision answer
would be actively misleading. **Nothing here indicates whether any symptom is or is not caused by
a medicine, and nothing here is a reason to start, continue or stop anything.** A symptom produced
by expectation is a real symptom, and "it might be nocebo" is not a conclusion anyone should draw
about themselves or about anyone else from this page. Anyone who thinks a medicine may be causing
them a problem should raise it with their prescriber or pharmacist, who can assess the timing and
the alternatives properly.

## Where this stands, October 2026

The decomposition, regression to the mean and the logic of blinding are definitional and do not
date. Three areas are moving. **Open-label placebo** is an active research field and the size,
durability and generalisability of the effect are unsettled, so any statement stronger than "it
has been demonstrated in some symptom-defined conditions" is ahead of the evidence. **Nocebo and
risk communication** is the subject of current guidance work in several countries, prompted partly
by disputed drug-intolerance syndromes, and the recommendations are not uniform. And the
**availability of blinded n-of-1 re-challenge as a clinical service** is new, uneven and
expanding, so whether it is an option where you work is a local question with a changing answer.
Check the current reviews and your own professional body's guidance.
