---
id: "m146"
slug: drug-development-and-the-phases
style: serious
category: pharmacology
difficulty: advanced
question: "Why does each phase of drug development answer a question the previous phase could not, and what does a licence at the end of it actually certify?"
tags: [drug-development, clinical-trials, endpoints, licensing, regulation]
---

# The phases are not a queue of increasingly big studies. Each one asks a question the last one made askable.

The commonest way to misremember drug development is as a single experiment done at three sizes.
That picture predicts that a large enough first study would do the whole job, and it is wrong in a
specific way: each phase's question is unanswerable until the previous phase has supplied a
parameter. You cannot ask whether a dose works before you know which doses the body tolerates. You
cannot ask whether it beats the standard treatment before you know which dose to compare. And you
cannot ask whether it does something rare and bad until a great many people have taken it, which
only happens after a licence.

Claims below are marked inline with what they rest on: (**mechanism**), (**definitional**),
(**consensus**), or (**country-dependent**).

## The questions, in the order the previous answer makes possible

| Stage | The question it answers | Whose bodies | What it structurally cannot detect |
| --- | --- | --- | --- |
| Preclinical | Does the molecule do the intended thing to the target, and is there an exposure that is survivable in two species? | cells and animals | anything about human exposure, and anything about how a person feels |
| Phase I | What exposure does a given dose produce in a human, and what is the first thing that limits it? | small numbers, usually healthy volunteers; patients where the agent is too toxic for volunteers | efficacy — the participants mostly do not have the disease |
| Phase II | At a tolerated dose, does the drug move the disease at all, and which dose and schedule are worth taking forward? | small numbers of people with the condition | a reliable comparison against standard care; it is not powered for one |
| Phase III | Against the proper comparator, in enough people, does it change an outcome that matters — and at what cost in harms? | large, randomised, often multinational | harms rarer than roughly the reciprocal of its own size, and anything that takes longer than its follow-up |
| Phase IV and pharmacovigilance | What happens in unselected use, over longer time, in people the trials excluded? | everyone who takes it | a clean causal attribution, because nothing is randomised any more |

The table's last column is the engine of the whole structure (**mechanism**). Every design buys
one kind of certainty by giving up another, and the next phase exists to recover what the last one
gave up.

```
   WHAT EACH STAGE CAN SEE, AS A FUNCTION OF WHAT IT GAVE UP
   ─────────────────────────────────────────────────────────────────────────────────

   PHASE I      narrow population, intense measurement
                ├─ gained: exposure-dose relationship measured directly, per person
                └─ gave up: relevance. Healthy volunteers do not have the disease,
                            so nothing here predicts benefit

   PHASE II     has the disease, small, often single-arm or lightly controlled
                ├─ gained: a signal of activity, and a dose to take forward
                └─ gave up: precision and comparison. A promising phase II is the
                            single least reliable object in this pipeline

   PHASE III    randomised, controlled, powered, pre-registered
                ├─ gained: causal attribution for the chosen endpoint
                └─ gave up: generality. The eligibility criteria that make the
                            comparison clean are exactly what make it narrow

   PHASE IV     unselected, uncontrolled, open-ended
                ├─ gained: the rare, the delayed, the interacting, the real
                └─ gave up: the control arm. Nothing here settles causation alone

   ─────────────────────────────────────────────────────────────────────────────────
   Note the shape: PRECISION and GENERALITY trade against each other at every step,
   and no single study design holds both. That is why there is a sequence at all --
   not because the sponsor wants to spend the money slowly.
```

## Dose escalation, and why it is first

A first-in-human study is an escalation with a stopping rule, not a test of a dose
(**definitional**). Cohorts receive ascending doses; each cohort is observed for a defined period
before the next is dosed; escalation stops at a pre-specified toxicity criterion, and the dose
below that is carried forward (**consensus**). Several features of the design exist because of
specific past harms: starting well below the exposure predicted to be active, dosing participants
one at a time rather than simultaneously at the first dose level, and pre-specifying the stopping
rule rather than judging it at the time.

Two mechanistic points separate agent classes here. For a cytotoxic agent, more exposure means
more effect and more toxicity, so the highest tolerated exposure is a rational target. For a drug
whose effect saturates when the target is fully engaged, it does not: the useful dose is the one
that occupies the target, and escalating past it adds toxicity and nothing else (**mechanism**).
This is `m007`'s receptor argument arriving in a trial design, and it is why "maximum tolerated
dose" is the right question for some development programmes and a category error for others.

## The comparator question, which decides what the trial can conclude

What a phase III trial can claim is fixed by what it randomised against, and this is where exam
answers are lost (**mechanism**).

* **Against placebo**, the conclusion is *that the drug does something*. It says nothing about
  whether it does more than the existing treatment.
* **Against an active comparator, powered for superiority**, the conclusion is a comparison — if
  the comparator was given properly, at a proper dose, to the people it suits.
* **Against an active comparator, powered for non-inferiority**, the conclusion is weaker than it
  sounds: that the new drug is not worse by more than a pre-specified margin. The margin is a
  judgement, declared in advance, and a generous margin can make a worse drug look acceptable
  (**consensus**).
* **Against nothing — a single-arm study with a historical or external control** — the conclusion
  is not a comparison at all but an inference, carrying every difference between the two
  populations with it. These are accepted in specific circumstances, usually where randomisation
  is impracticable or unethical, and they are the weakest ground a licence can stand on
  (**country-dependent**).

The derived rule is that **two drugs separately shown to beat placebo have not been compared with
each other.** An indirect comparison constructed from their separate trials is a model, not a
measurement; it inherits the differences between the trial populations and it is routinely wrong
in direction as well as size.

Randomisation is doing one job and it is worth saying exactly which: it makes the groups
exchangeable for *unmeasured* differences as well as measured ones, which no amount of statistical
adjustment can do afterwards (**mechanism**). Allocation concealment and blinding do a different
job — they stop the allocation influencing who is recruited, what is done to them afterwards, and
how outcomes are judged. `m080` is the half of this that explains why the control arm is not a
measurement of the placebo effect.

## Endpoints: chosen in advance, and chosen by someone

A trial measures what it declared it would measure, and the declaration is a judgement
(**definitional**).

* A **surrogate endpoint** stands in for the outcome anyone cares about. It is legitimate where
  the surrogate's relationship to the outcome has itself been established, and it is treacherous
  where it has not: the history of therapeutics includes drugs that moved a surrogate in the right
  direction and the outcome in the wrong one (**consensus**).
* A **composite endpoint** counts several events together. It buys statistical power and it costs
  interpretability, because the components are not equally serious and a result can be driven
  entirely by the least serious one. Reading the components separately is the first thing to do
  with a composite result (**consensus**).
* A **patient-reported endpoint** measures something no laboratory can, and its weakness is the
  mirror image: it needs blinding to mean much, because expectation moves it.

The structural safeguard is pre-registration — the endpoint, the analysis and the population
declared before the data exist. Its purpose is to make the difference between a hypothesis and an
observation checkable by someone outside the sponsor (**consensus**).

## What a licence certifies, and what it is silent about

A marketing authorisation is a regulator's judgement that, for a stated indication, in a stated
population, at a stated dose and formulation, the evidence supports acceptable quality, safety and
efficacy (**definitional**, **country-dependent**). Stated that way, the silences are visible.

* It does not certify that the drug is **better** than the alternatives, unless the comparison was
  made. Most are not.
* It does not certify anything about **people the trials excluded** — and the standard exclusions
  are consistent: pregnancy, extremes of age, significant organ impairment, and the
  multimorbidity that `m047` is about. The licence's silence on a group is the absence of
  evidence, not a reassurance, and `m078` is the dose-scaling half of the same gap.
* It does not certify **long-term safety**, because the follow-up was as long as it was.
* It does not certify **value**. Whether a health system will pay is a separate decision made by a
  separate body on separate criteria (**country-dependent**).
* It does not **freeze**. Indications are added and withdrawn, warnings are strengthened, and
  products are suspended, on evidence that by definition arrives afterwards.

Several jurisdictions also grant authorisations on a reduced evidence base — conditional,
accelerated or exceptional-circumstances routes — with specified obligations to produce the
missing evidence afterwards. These are a deliberate trade of certainty for earlier access, the
obligations are sometimes slow to be met, and the arrangements differ substantially between
regulators (**country-dependent**).

And the sequence does not stop at the licence. Pre-licensing programmes are too small to exclude
rare harm, for the arithmetic reason `m010` sets out, so the rare and the delayed can only be
found in use. That is not a defect in trial design. It is the reason post-marketing surveillance
is part of the structure rather than an afterthought (**mechanism**).

## The human stakes, said plainly

Four things here are about people rather than about method.

**A trial is not treatment, and the confusion has a name.** Therapeutic misconception is the
well-documented tendency of participants to understand a randomised trial as individualised care
chosen for their benefit. It is not a failure of intelligence; the setting, the attention and the
language all invite it. Consent that does not address it is not informed, and the honest framing
is that nobody knows which arm is better, which is the reason the trial exists.

**Equipoise is the ethical condition for randomising at all.** A trial is defensible while the
professional community genuinely does not know which option is better. It stops being defensible
when the answer becomes clear during the trial, which is why interim monitoring by a committee
independent of the sponsor exists and why trials are stopped early in both directions.

**Who is in the trials decides who the evidence is about.** Under-representation of women, of
older people with several conditions, of people with impaired organ function, and of
ethnic-minority and lower-income populations is well documented and not controversial. It is not a
neutral gap: it means the evidence base is systematically thinner for people whose care is
systematically harder. The fix is representative recruitment, not confident extrapolation.

**The evidence base is only what was published.** Trials with unwelcome results have historically
been less likely, and slower, to appear. Registration requirements and results-reporting rules
exist to make non-publication visible, compliance with them is incomplete, and a reader who only
sees the published literature is seeing a biased sample. That is a statement about the record, not
about anyone's integrity.

Nothing in this answer indicates what anyone should take, start or stop, and a question about
joining a trial belongs with the treating team and the trial's own information, not with a
revision answer.

## What an examiner digs into next

* Why can a first-in-human study not also measure efficacy? Give the structural reason, not the
  practical one.
* A drug beat placebo and so did its competitor. What have you learned about the two of them?
* What exactly does a non-inferiority margin let a sponsor claim, and what does choosing a wide
  one do?
* A composite endpoint is positive. What is the first thing you look at, and why?
* Name three things a marketing authorisation does not certify.
* Why is maximum tolerated dose the right target for one agent class and a category error for
  another?
* Why can a pre-licensing programme never exclude a one-in-ten-thousand reaction, however well
  designed?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* **Your national medicines regulator's own guidance on clinical trial authorisation and on
  marketing authorisation**, for what is actually required where you work, and for the
  conditional, accelerated and exceptional-circumstances routes. This is the document that decides
  almost everything in the last section and it differs between jurisdictions.
* **The international guideline series on good clinical practice and on the statistical principles
  for clinical trials**, issued by the international council for harmonisation of technical
  requirements for pharmaceuticals for human use. These are the documents that define the terms
  used above, including the ones about endpoints and about non-inferiority.
* **The world medical association's declaration on ethical principles for medical research
  involving human subjects**, for equipoise, consent and the obligations around vulnerable
  participants, and your national research ethics framework for how it is implemented.
* **The reporting guidance for randomised trials and its extensions**, for what a trial report is
  expected to contain — which is the fastest way to notice what a given report has omitted.
* **A current clinical pharmacology or clinical trials textbook chapter**, for the definitional
  material: the phase definitions, escalation designs, surrogate and composite endpoints, and
  intention-to-treat against per-protocol analysis.
* **The primary literature and the trial registries**, for anything about how often surrogate
  endpoints have misled, how large the published-unpublished gap is, or how well
  post-authorisation obligations are met. This answer states no figure for any of those,
  deliberately.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. It gives no doses, no participant numbers, no escalation increments and no
non-inferiority margins: those are properties of individual protocols and regulatory guidance, not
of a general principle, and inventing one would be worse than omitting it. Nothing here indicates
whether anyone should take part in a trial, or take, start or stop any medicine. The regulatory
structure described is the common shape across major jurisdictions and the detail is genuinely
different in each; yours is the authority and this is not.

## Where this stands, October 2026

The logic of the sequence — each phase supplying the parameter the next one needs, and precision
trading against generality — is mechanism and does not date. The regulatory scaffolding around it
dates quickly. **Which evidence routes exist** and what obligations attach to them has changed
repeatedly in the last decade and differs by regulator. **Trial design itself is moving**:
adaptive and platform designs blur the phase boundaries deliberately, master protocols test
several agents against one control, and real-world evidence is being used in regulatory
submissions in ways that were not accepted ten years ago, with the question of when that is
legitimate actively contested. **Results-reporting and registry requirements** are being tightened
and enforced unevenly. Check your national regulator's current guidance and the relevant
international guideline rather than this answer.
