---
id: "m077"
slug: pharmacogenomics-and-the-population-dose
style: serious
category: pharmacology
difficulty: advanced
question: "A licensed dose is a choice made for a population. What does a pharmacogenomic result actually change about that choice, and why does knowing a genotype so often leave the prescription unchanged?"
tags: [pharmacogenomics, metaboliser-phenotype, prodrugs, variability, equity]
---

# A licensed dose is a bet on a distribution. A genotype moves one person off the middle of it.

A dose in a product licence was not derived from physiology. It was chosen because, across the
population studied, it put enough people into an acceptable range of exposure to produce an
acceptable balance of benefit and harm. It is a bet on a distribution, and it is a good bet
precisely because most people are near the middle of one.

Pharmacogenomics is the business of identifying, *before the first dose*, the people for whom that
bet is systematically wrong — and of saying in which direction. That last clause is the whole
subject. A genotype that tells you someone is unusual without telling you which way is not
actionable, and the single most-failed exam point in the topic is a sign error.

Claims below are marked inline with what they rest on: (**mechanism**), (**definitional**),
(**consensus**), or (**country-dependent**).

## What the population dose is a bet on

Two distributions, not one, and they fail for different reasons.

```
   DISTRIBUTION 1 -- exposure produced by a fixed dose   (pharmacokinetic variability)

      people
        │              ╭───────╮
        │           ╭──╯       ╰──╮
        │        ╭──╯             ╰──╮
        │     ╭──╯                   ╰───╮
        │ ╭───╯                          ╰────╮
        └─┴───────────────────────────────────┴──────────▶ exposure (AUC) at one dose
          ▲                                   ▲
      under-exposed:                      over-exposed:
      the drug "did not work"              the drug "was not tolerated"
      and the usual conclusion             and the usual conclusion is
      is that it was the wrong drug        that the person is sensitive

   DISTRIBUTION 2 -- response produced by one exposure   (pharmacodynamic variability)

      Same picture, different axis. A target variant moves THIS one, and no amount
      of dose adjustment fixes it, because the exposure was never the problem.
      m007 is the receptor half: a target the drug cannot engage is a non-target,
      not a weak one.

   A dose adjustment addresses distribution 1 ONLY. Reading a genotype without
   knowing which distribution the variant sits in is how a dose gets changed for a
   problem a dose cannot reach.
```

## Where in the chain a variant can sit

Four places, and they have different consequences (**mechanism**):

| Where | What varies | What it changes | What to do about it |
| --- | --- | --- | --- |
| Absorption and transport | uptake and efflux transporter function | exposure, sometimes tissue-specific rather than systemic | dose, sometimes; drug choice, sometimes |
| Metabolism | oxidation and conjugation enzyme activity | exposure, and for a prodrug the amount of *active* drug | dose or drug choice, direction depending on the prodrug question below |
| The molecular target | receptor or enzyme structure, or its expression | response at a given exposure | drug choice; a dose change does not reach it |
| Immune recognition | the alleles presenting the drug or its metabolite | whether a severe hypersensitivity reaction can occur at all | avoid the drug; there is no safe dose |

The fourth row is categorically unlike the other three. It is not a graded shift in a
distribution; it is a predisposition to a reaction of the kind `m010` classifies as type B — not
dose-related, not predictable from pharmacology, and not survivable by being careful. For a small
number of specific drug–allele pairs, that is why pre-treatment testing has become standard
practice in the populations where the allele is common enough to matter (**country-dependent**).

## Metaboliser phenotype, and the sign flip that catches everyone

Enzyme activity is reported as a phenotype inferred from genotype, conventionally on a scale from
poor through intermediate and normal to rapid and ultra-rapid (**definitional**). What that
phenotype predicts depends entirely on whether the molecule you administered is the active one.

```
   ACTIVE DRUG, cleared by the variable enzyme
   ─────────────────────────────────────────────────────────────────────────────
     poor metaboliser         less clearance   ──►  HIGHER exposure  ──►  toxicity
     ultra-rapid metaboliser  more clearance   ──►  LOWER exposure   ──►  failure

   PRODRUG, ACTIVATED by the variable enzyme
   ─────────────────────────────────────────────────────────────────────────────
     poor metaboliser         less activation  ──►  LESS active drug ──►  failure
     ultra-rapid metaboliser  more activation  ──►  MORE active drug ──►  toxicity
                                                     ▲
                                 THE SIGNS REVERSE. Same enzyme, same genotype,
                                 same phenotype label, opposite clinical risk.
                                 The question "is this a prodrug?" decides the
                                 direction, and nothing in the genotype report
                                 answers it for you.
   ─────────────────────────────────────────────────────────────────────────────

   And a third case, which is neither: an enzyme whose job is to DETOXIFY a drug
   that is already active. Low activity there means the normal dose delivers a
   normal exposure of the parent and an abnormal exposure of something the body
   cannot dispose of. Thiopurines and fluoropyrimidines are the standing examples,
   and pre-treatment testing before them is routine in several countries.
```

That the direction reverses for a prodrug is (**mechanism**). Which specific drugs are prodrugs of
which enzymes, and which pairs have agreed recommendations, is (**country-dependent**) and belongs
in the formulary and the drug–gene guidance, not in a revision answer.

## Why the result so often leaves the prescription unchanged

This is the part that separates someone who has read about pharmacogenomics from someone who has
used it. Six reasons, roughly in order of how often they apply.

1. **There is already a better instrument.** A genotype is a *prior* about exposure. If the drug's
   effect is directly measurable, or if its concentration is worth measuring, you can observe the
   thing the genotype was predicting. A measurement beats a prediction about the same quantity,
   which is why genotyping adds least for exactly the drugs that are easiest to titrate, and
   `m041` is the monitoring half of this (**mechanism**).
2. **The variant explains part of the variance, not most of it.** Between-person differences in
   clearance come from organ function, age, body composition, co-medication, disease and adherence
   as well as from genotype. Even a strongly actionable gene usually accounts for a minority of
   the spread, so a normal result is not a prediction of a normal exposure (**consensus**).
3. **Phenoconversion.** An inhibitor of the same enzyme converts a genotypic normal metaboliser
   into a phenotypic poor one, and the laboratory cannot see it. `m009` is the interaction half.
   The practical rule follows: the genotype is not the phenotype, and the medication list is part
   of the result (**mechanism**).
4. **Coverage, and whose variants the panel was built around.** A panel tests named alleles. "No
   actionable variant detected" means none of the tested ones, not none. Allele frequencies differ
   substantially between ancestral populations, so a panel assembled around the variants common in
   one population systematically under-detects in others — which makes this a question of equity
   and not only of sensitivity (**consensus**).
5. **Actionability.** For most drug–gene associations that are real, there is no agreed action.
   Where there is, it has been written down by a small number of implementation consortia and
   national working groups, and those documents do not always agree with each other or with the
   product licence (**country-dependent**).
6. **Timing.** A result that arrives after the decision has been made changes nothing. That is the
   whole argument for pre-emptive panel testing with the result stored in the record rather than
   reactive testing per prescription; the arguments against are cost, the risk of acting on
   associations whose evidence base later moves, and the difficulty of making a stored result
   surface at the moment it is relevant (**country-dependent**).

## What a genotype actually is, in the dosing decision

It is one prior among several, and it has an unusual property: it does not change. Organ function
drifts, weight changes, the medication list turns over, but the genotype that produced today's
phenotype will produce the same one in twenty years. That permanence is what makes storing it
worthwhile, and it is also what makes a wrong interpretation durable.

So the honest summary is that pharmacogenomics narrows the starting bet and tells you which tail
to watch. It does not replace observing the person. Where the variant is in the target rather than
in clearance, a dose change is the wrong instrument altogether. And where the variant predicts an
immune reaction, the instrument is avoidance, because there is no dose at which the reaction is
tolerable.

## The human stakes, said plainly

Genetic information behaves differently from other clinical information, and three consequences
follow that are not pharmacology.

It is **information about relatives as well as about the person tested**, even when the test was
ordered for a narrow prescribing question. Pharmacogenes are generally not associated with
disease, which is why this is usually a small issue rather than a large one — but it is not zero,
and consent, storage and disclosure are governed by law and policy that differ between countries.

It is **permanent, and it follows the person**. A result entered in a record will be read by
people who did not order it, years later, possibly without the context that explains what it does
and does not mean. A mislabelled phenotype is therefore a durable error, and the correct response
to an unexpected result is the same as for any other test: ask whether it fits, before acting.

And the coverage problem in reason 4 is **an equity problem, stated plainly**. The reference data
and the allele panels on which pharmacogenomics was built over-represent populations of European
ancestry. A technology that works better for the people it was developed on, deployed uniformly,
widens a gap rather than closing it. Naming that is not a criticism of the science; it is a
description of what has to be fixed for the science to deliver what it promises, and the fix is
population-appropriate panels and reference data rather than more enthusiasm.

One further point, because it is the way this topic goes wrong at the bedside. A genotype is not a
reason to doubt what someone reports. If a person says a drug did not work or was not tolerated,
"the genotype was normal" is not a counter-argument — it is at most a reason to look for the other
explanation. Nothing in this answer indicates what anyone should take, change or stop, and a
pharmacogenomic result in anybody's own record is a conversation to have with their prescriber or
pharmacist rather than something to act on alone.

## What an examiner digs into next

* A poor metaboliser is prescribed a prodrug activated by that enzyme. Which way does the risk go,
  and why does everyone get this backwards?
* A genotype predicts an unusual exposure, and the drug has a concentration worth measuring. Which
  instrument wins, and why?
* What does "no actionable variant detected" actually exclude?
* How can a genotypic normal metaboliser be a phenotypic poor one, with no laboratory error?
* Which of the four sites of variation cannot be addressed by changing the dose?
* Why is pre-treatment testing standard for a handful of immune-mediated reactions and not for
  most drug–gene pairs, when the associations are real in both cases?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* **The published drug–gene guidelines of the clinical pharmacogenetics implementation
  consortium**, and **the pharmacogenetics recommendations of the Dutch pharmacogenetics working
  group.** These are the two bodies whose documents are most widely used to decide whether a given
  drug–gene pair is actionable and what the action is. They are separately maintained, they do not
  always agree, and neither is a substitute for the product licence where the two differ.
* **Your national formulary and the product's approved prescribing information**, for whether a
  genotype or phenotype is mentioned at all for that drug, and for whether testing is required
  rather than merely informative. Requirements differ by country.
* **Your national genomic medicine service's test directory**, for what is actually orderable
  where you work, on what indication, and with what turnaround. This is the document that decides
  whether reason 6 above applies to you.
* **A current clinical pharmacology or pharmacogenomics textbook chapter**, for the definitional
  material: the activity-score and phenotype terminology, the prodrug reversal, phenoconversion,
  and the distinction between variability in exposure and variability in response.
* **The primary literature**, for any statement about how much of the variance in clearance a
  given gene explains, about allele frequencies by ancestry, or about the predictive performance
  of a specific test. This answer states no such figures, because all three are active research
  questions and all three differ by population.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. It names no drug–gene pair as actionable, gives no allele frequencies, no
variance-explained figures and no doses, deliberately: those are the property of the drug–gene
guidance, the product licence and the primary literature, and they are revised. Nothing here
indicates whether anyone should be tested, or what should be done with a result. A pharmacogenomic
result in a person's own record is a matter for their prescriber or pharmacist, and a normal
result is not a reason to disbelieve a reported effect. Nothing here should be used to make a
decision about anyone's treatment, including the reader's own.

## Where this stands, October 2026

The mechanism — two distributions, four sites of variation, the prodrug sign reversal,
phenoconversion — is mechanism and does not date. Almost everything else here does, and faster
than most of this specialty. **Which drug–gene pairs are actionable** is revised by the
implementation consortia on a rolling basis and pairs have been added and downgraded. **What is
orderable** depends on a national test directory that changes. **Whether testing is pre-emptive or
reactive** is an active service-design question that different countries are answering differently
right now, and the answer is moving. And the **coverage and reference-data problem** is the
subject of substantial current work, so a statement about how well panels perform across
ancestries is dated almost as soon as it is written. Check the current guidance, your national
test directory, and the product licence.
