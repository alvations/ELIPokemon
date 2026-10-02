---
id: "m065"
slug: randomisation-against-registries
style: serious
category: oncology
difficulty: advanced
question: "What does randomisation buy in an oncology trial that no amount of analysis of a registry can buy, and where is a registry the better instrument?"
tags: [clinical-trials, randomisation, confounding, registries, evidence]
---

# Randomisation balances what nobody recorded, and that is the only thing it uniquely does

In routine care, who receives which treatment is decided by clinicians and patients on the basis
of how well they expect it to go. Fitter people, with better organ function, fewer other
conditions and more support at home, are offered and accept the more intensive options. So in any
registry of real practice, **the group that received the more intensive treatment would have done
better than the other group even if the treatment did nothing at all.**

That is **confounding by indication**, and in oncology it is not one bias among several. It is the
dominant one, it runs in a predictable direction, and it is large.

Randomisation removes it, and the precise statement of how is the whole of this answer:
randomisation makes allocation **independent of prognosis**, so the arms are comparable in
expectation on everything — recorded, unrecorded, and unknown. Statistical adjustment can only
ever balance what was written down. That difference is not a refinement. It is the difference
between a comparison that supports a causal claim and one that does not.

Each load-bearing claim below is marked with the kind of thing it is: **mechanism** (derivable
from how the inference works), (**definitional**) (true because a convention says so),
(**consensus**) (widely agreed professional practice), or (**country-dependent**) (varies by
nation, region or institution, and changes).

## Where the two instruments differ

```
   A REGISTRY OF ROUTINE CARE                 A RANDOMISED TRIAL

   who got treatment A?                       who got treatment A?
     ▲                                          ▲
     │ decided by prognosis —                   │ decided by a random
     │ fitness, organ function,                 │ sequence that knows
     │ comorbidity, support,                    │ NOTHING about the person
     │ preference, and the clinician's
     │ unrecorded impression
     │                                          │
     ▼                                          ▼
   the arms differ in the thing              the arms differ in the
   being studied AND in prognosis            treatment, and in prognosis
     │                                        only by chance — which is
     │                                        a quantity you can PUT A
     ▼                                        DISTRIBUTION ON
   adjust for what was recorded
     │                                          │
     │ performance status AS CODED               ▼
     │ comorbidity AS CODED                   the difference between the
     │ … and NOT the gestalt, which           arms is ATTRIBUTABLE, and
     │ is often the strongest                 the residual uncertainty is
     │ predictor and is never                 a sampling distribution
     │ in the dataset
     ▼
   RESIDUAL CONFOUNDING, of a size
   the data cannot bound

   ──────────────────────────────────────────────────────────────────────────────

   AND THE TRADE RUNS THE OTHER WAY TOO:

   trial     narrow eligibility  ──►  excellent INTERNAL validity,
                                      limited EXTERNAL validity
   registry  everybody           ──►  poor internal validity for a causal
                                      comparison, and the ONLY instrument
                                      for generalisability, rare and late
                                      events, patterns of care and inequity
```

## Why adjustment is not a substitute

Multivariable regression, propensity scores and matching all do the same thing: they condition on
**recorded** covariates (**mechanism**). That is useful and it is bounded by what the dataset
contains.

Three gaps are routine and none of them is a data-quality problem that better coding would fix:

* **A recorded variable is not the underlying variable.** Performance status as entered is a
  coarse, observer-dependent summary of something continuous. Comorbidity as coded is what was
  coded.
* **The clinician's overall impression is frequently the strongest single predictor and is never a
  field.** It is precisely what decided the allocation, and it is precisely what cannot be
  adjusted for.
* **You cannot adjust for a variable you did not know mattered.** Adjustment is limited by
  contemporary understanding, which is a moving target.

The consequence is the one that gets stated too weakly in teaching: **residual confounding has no
upper bound you can compute from the data.** A propensity-matched analysis of a registry can be
beautifully balanced on every recorded variable and still be wrong by a wide margin in the
direction the allocation was made.

Randomisation does not make the arms identical — it makes them differ only by chance, and chance
is a thing with a distribution. That is the trade: an unbounded unknown is replaced by a
quantified one.

## The machinery that protects the randomisation, and what each piece is for

These are routinely confused with each other and they do different jobs (**mechanism**,
**consensus**):

* **Allocation concealment** prevents whoever is enrolling from knowing or influencing the next
  assignment. It protects the randomisation itself at the moment of enrolment, and it is the piece
  whose failure destroys the whole design. It is **not** blinding and is required whether or not
  blinding is possible.
* **Blinding** protects what happens *after* allocation — management, additional treatment,
  reporting of symptoms and, most importantly, assessment of the outcome. It matters most for
  subjective or adjudicated endpoints and least for all-cause death, which is why an open-label
  trial with a hard endpoint can still be sound while an open-label trial with an assessed
  endpoint is fragile.
* **Stratification or minimisation** balances strong prognostic factors across arms. It reduces
  variance and improves credibility; it does not remove a bias, because randomisation had already
  dealt with bias in expectation.
* **Intention to treat** analyses everyone in the arm they were allocated to, whatever they
  actually received. The reason is structural: any other analysis set is defined partly by events
  that happened *after* randomisation, and selecting on those reintroduces exactly the
  prognosis-dependent selection that randomisation removed. A per-protocol analysis answers a
  different question and usually cannot answer it.
* **Pre-specification** of the primary endpoint, the analysis and any margin fixes them before the
  data are seen, because the number of defensible ways to analyse a dataset is large and choosing
  among them afterwards is a selection step.

## What the phases are actually for

Dose-finding and safety, then an activity signal, then a comparison — and the reason the sequence
exists is that only the last design supports a comparative claim (**definitional**,
**consensus**).

A single-arm study reporting a response proportion cannot support one, however large the
proportion, because there is no comparator and because the enrolled population was selected. The
response-assessment answer in this specialty sets out the separate problem that an imaging
response is not the same proposition as living longer or feeling better; here the point is
narrower and prior to it: a single arm has nothing to subtract.

Two design notes that are commonly misread:

* **A non-inferiority margin is a judgement declared in advance**, not a statistical quantity
  discovered in the data. It states how much worse the new treatment may be while still being
  worth having for its other advantages, and whether a given margin was reasonable is a clinical
  argument.
* **Failing to demonstrate inferiority is not demonstrating equivalence.** An underpowered trial
  fails to demonstrate most things.

## Where a registry is the better instrument

A registry is not a weak trial. It is a different instrument, and for several questions it is the
only one (**consensus**):

* **Generalisability.** Trial eligibility criteria systematically select people who are younger,
  fitter and with fewer other conditions than the clinic. Whether a result transfers to the
  population actually being treated is a question a trial structurally cannot answer about itself,
  and a registry can.
* **Rare and late events.** A trial is too small and too short. Late cardiac effects, second
  malignancies and uncommon severe toxicities are registry and pharmacovigilance questions.
* **Patterns of care and inequity.** Who is offered what, who is referred, how long they wait, and
  how that varies by geography and deprivation are questions about the system, and no trial asks
  them.
* **Long-term outcomes and signal generation**, including the first indication that something is
  wrong with a treatment already in use.

And where randomisation is genuinely impossible, specific designs partly substitute — natural
experiments, instrumental-variable approaches, and target-trial emulation with the assumptions
stated explicitly. Each trades the assumption randomisation makes unnecessary for a different
untestable one, which is a reasonable bargain when stated and a bad one when hidden
(**consensus** that these have a role; genuinely contested how much weight they bear).

The honest summary: a registry tells you what is happening, and a trial tells you what a treatment
does. Asking either to do the other's job is the error, and it is made in both directions.

## The human stakes, said plainly

Everything above is inference, and that is the right register for deciding what a study design can
support. It is not the register for being in one.

Someone deciding whether to enter a randomised trial is being asked to accept that the treatment
they receive will be chosen by a process that is indifferent to them, specifically, personally, at
a moment when they would very much like somebody to choose on their behalf. That is a real thing
to ask of a person and it is not made easier by the inferential argument being correct. The
ethical basis for asking is genuine uncertainty about which arm is better — and if that
uncertainty is absent, the question should not be asked at all.

Trial participation also costs time: extra visits, extra investigations, extra forms, often more
travel. People take that on, frequently in the hope of helping others as much as themselves, and
the resulting evidence is the reason anything in oncology has improved. That deserves saying
plainly rather than being folded into a methods section.

And the inequity in the paragraph about generalisability is not an abstraction. Trials have
historically under-enrolled older people, people with other illnesses, and people from several
ethnic and socioeconomic groups, which means the evidence base is thinnest for some of the people
who most need it. That is a harm produced by how the evidence was gathered, not a limitation of
the arithmetic. No figure of any kind appears in this answer, and that is deliberate.

## What an examiner digs into next

* State in one sentence what randomisation does that propensity matching cannot, without using the
  word *bias*.
* Why does residual confounding have no computable upper bound?
* What is the difference between allocation concealment and blinding, and which one's failure is
  fatal?
* Why does intention to treat follow from the logic of randomisation rather than being a
  conservative convention?
* Why can a single-arm response-rate study not support a comparative claim?
* Name three questions a registry answers better than any trial could, and say why.
* What does a non-inferiority margin assert, and who decides it?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* A current standard textbook of clinical epidemiology or of clinical trial design, for
  confounding by indication, the limits of adjustment, and the distinction between allocation
  concealment and blinding. This is the authority for everything marked **mechanism** here.
* The reporting guideline for randomised trials, and the companion guideline for observational
  studies, published by the respective international reporting-guideline initiatives — they are
  the most compact statement of what each design must disclose and therefore of what each can
  support.
* The clinical trials guidance issued by your national medicines regulator and by your national
  research ethics framework, for what is required where you are. These differ between countries.
* Your national cancer registry's own published methodology, for what it records, how completely,
  and what it explicitly does not support.
* The primary literature, for any specific claim about a specific trial, and for the ongoing
  methodological argument about target-trial emulation and real-world evidence, which is active
  rather than settled.

## Scope and safety

This is revision material about study design and inference, written for someone already training
in the field. It has had no clinical review. It is not a trial protocol, not a statistical
reference, and not a guide to whether anybody should enter a trial — that is a conversation with
the team looking after that person, who know the trial, the eligibility criteria and the
individual's circumstances, none of which are here. No effect size, power calculation, margin,
significance threshold or participation figure appears here and none should be inferred.
Regulatory and ethical requirements differ by country and are revised; yours govern. Anyone
affected by cancer — their own diagnosis or someone else's — should be talking to their clinical
team about what trials are open to them, which is a question with a local answer.

## Where this stands, October 2026

The inferential core will not date. Confounding by indication, the limitation of adjustment to
recorded covariates, and the specific thing randomisation buys are properties of the logic rather
than of current practice, and they have been understood in this form for decades.

What is genuinely active, and contested, is how much weight non-randomised evidence should carry.
Target-trial emulation, external and synthetic control arms, and registry-based comparative
analyses are all being argued over and are treated differently by different regulators; the
pressure to use them is real and comes partly from genuinely small biomarker-defined populations
in which a conventional randomised trial may not be feasible. Trial designs themselves are also
moving — platform and basket designs, adaptive allocation, and decentralised conduct — and
pragmatic trials embedded in routine care are an attempt to get randomisation and
generalisability at once. None of that changes the argument above; all of it changes what the
best available evidence for a given question looks like. No regulator's current position is
quoted here, deliberately: those move, they differ between jurisdictions, and they belong to the
regulator's own documents rather than to a revision note like this one.
