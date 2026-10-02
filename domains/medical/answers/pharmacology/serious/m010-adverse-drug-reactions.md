---
id: "m010"
slug: adverse-drug-reactions
style: serious
category: pharmacology
difficulty: intermediate
question: "How are adverse drug reactions classified, why do dose-dependent and idiosyncratic reactions need different responses, and why do spontaneous reporting schemes exist despite their known biases?"
tags: [adverse-reactions, pharmacovigilance, idiosyncrasy, reporting, causality]
---

# A classification that changes what you do, and a register that works while measuring nothing.

An adverse drug reaction is a response to a medicine that is harmful and unintended, occurring at
a dose used for a legitimate purpose. The last clause is what separates it from an overdose, and
the word *response* is what separates it from a **medication error** — an error is a failure in
the process of prescribing, dispensing or administering, and it may or may not cause a reaction.
Keeping those three apart matters because they are investigated by different people through
different systems.

Classifications are only worth learning if they change what you do. The **Rawlins–Thompson**
scheme earns its place because its first two categories demand opposite responses.

| Type | Name | Dose-related? | Predictable from pharmacology? | Frequency | Usual response |
| --- | --- | --- | --- | --- | --- |
| A | Augmented | yes | yes | common | reduce the dose, or remove the reason exposure rose |
| B | Bizarre | no | no | rare | withdraw, document, and do not re-challenge casually |
| C | Chronic / continuing | cumulative | partly | uncommon | reconsider duration, monitor for the specific harm |
| D | Delayed | sometimes | sometimes | rare | recognise it as attributable at all |
| E | End-of-use | — | partly | uncommon | taper rather than stop abruptly |
| F | Failure of therapy | often | yes | common | look for an interaction or a dose problem |

**Type A** reactions are the known pharmacology arriving somewhere unwanted: bleeding with an
anticoagulant, hypoglycaemia with insulin or a sulfonylurea, bradycardia with a beta-blocker,
constipation with an opioid. They are common, usually survivable, and usually manageable without
abandoning the drug.

**Type B** reactions are not an extension of the pharmacology. Anaphylaxis, idiosyncratic liver
injury, severe cutaneous reactions, blood dyscrasias. They are rare, carry higher mortality, and
the dose is not the lever.

**DoTS**, the framework proposed by Aronson and Ferner, is the useful refinement, because the A/B
split hides a real distinction. Its three axes are **dose relatedness** — does the reaction occur
below, at, or only above the therapeutic range, which separates hypersusceptibility from a
collateral effect from frank toxicity — **time course**, and **susceptibility**: who it happens
to, and why. Naming the susceptibility axis explicitly is what turns an unexplained idiosyncrasy
into a question with a possible answer.

## Why A and B need different responses

For a **type A** reaction the mechanism is the reason the drug works, so the response is
quantitative. Reduce the dose, or find out why exposure rose — falling renal function, a new
inhibitor, a formulation change, an adherence change — and address that. Re-exposure at a lower
dose is usually reasonable. The reaction is evidence about the amount, not about the person.

For a **type B** reaction, dose reduction is not a smaller version of the right answer; it is the
wrong kind of answer. The drug is withdrawn. Then three things follow that type A never requires.

* **Documentation that is accurate rather than defensive.** Recording an intolerance as an allergy
  has lifelong consequences, and an inaccurate allergy label causes measurable harm of its own
  through avoidance of first-line treatment. Penicillin labelling is the standard example and the
  distinction between a true hypersensitivity and a predictable gastrointestinal effect is worth
  being pedantic about.
* **A decision about the class, not just the drug**, where cross-reactivity is biologically
  plausible.
* **Susceptibility, where it is known.** Some type B reactions have identified genetic
  associations — abacavir hypersensitivity and the HLA-B\*57:01 allele is the most firmly
  established example, and pre-therapy testing exists because of it. Whether a given association
  is screened for, and in which populations, is *country-dependent and guideline-dependent*, and
  the allele names are worth checking against a current source rather than recalled.

Both types also need **causality assessment**, which is a structured version of ordinary clinical
reasoning: temporal plausibility, what happened on withdrawal, whether re-exposure occurred and
what followed, whether an alternative explanation fits better, and whether the reaction has been
reported before. Named instruments exist — the Naranjo scale, and the causality categories used by
the World Health Organization's monitoring programme — and they are deliberately conservative,
because the honest answer is usually *possible* rather than *certain*.

## Why spontaneous reporting exists, given that it cannot measure anything

```
   THE RULE OF THREE -- arithmetic, not a clinical figure

   P(no event in N exposures)  =  (1 - p)^N   ≈   e^(-pN)

   for about 95 % confidence of seeing AT LEAST ONE case:
        pN ≥ 3,   so   N ≥ 3 / p        because e^(-3) ≈ 0.05

   incidence p            exposures needed for ~95 % chance of one case
   ─────────────────────────────────────────────────────────────────────
   1 in 100                     300
   1 in 1,000                 3,000
   1 in 10,000               30,000
   1 in 100,000             300,000
   1 in 1,000,000         3,000,000
   ─────────────────────────────────────────────────────────────────────

   To be similarly confident of seeing THREE cases, treble it again.

   A pre-licensing programme that exposes a few thousand people therefore cannot
   exclude a reaction that occurs once in ten thousand, let alone once in a million.
   That is not a failure of the trial design. It is arithmetic — and it is the entire
   reason post-marketing surveillance has to exist.
```

The named schemes are real and worth knowing by name: the **Yellow Card Scheme** run by the
Medicines and Healthcare products Regulatory Agency in the United Kingdom, **MedWatch** and the
adverse event reporting system run by the Food and Drug Administration in the United States,
**EudraVigilance** at the European Medicines Agency, and **VigiBase**, the global database
maintained by the Uppsala Monitoring Centre for the World Health Organization's international drug
monitoring programme. Several countries also flag newly authorised medicines for intensified
reporting — the black triangle in the United Kingdom, the inverted black triangle for additional
monitoring in the European Union.

The biases are not disputed and are worth stating as plainly as the arithmetic.

* **Under-reporting dominates.** Only a fraction of reactions are ever reported, the fraction is
  not known, and it varies by drug, by reaction, by profession and by country. Any statement of
  how small the fraction is should be treated as an estimate, not a figure.
* **No denominator.** Reports count events, not exposures, so an incidence cannot be calculated
  from them. A rise in reports may be a rise in reactions or a rise in use or a rise in attention.
* **Stimulated reporting.** Publicity, a regulatory alert or litigation multiplies reports without
  any change in the underlying rate.
* **Reporting declines over a product's life** even where use grows — the pattern usually named
  after Weber — so a long-marketed drug looks safer than a new one for reasons that are
  sociological.
* **Selective reporting** of the serious, the novel and the recently taught, and **duplicates**
  arriving by more than one route.

And despite all of that it is kept, because it does one thing nothing else does: **it can detect a
reaction nobody was looking for.** Every denominator-based method — a cohort study, a case-control
study, prescription-event monitoring, an electronic health record sentinel system — must be told
what to measure before it can measure it. Spontaneous reporting has no exclusion criteria, no end
date, covers everyone who takes the drug, and costs almost nothing. It generates hypotheses; the
denominator-based methods test them. A system that cannot produce a rate can still be the only
system that notices there is something to count.

## The human stakes, said plainly

An adverse drug reaction is harm done to a person by treatment. That is a different thing from the
illness getting worse, and the difference is not academic.

The person it happened to did nothing wrong. They took a medicine as intended, and the medicine
harmed them — which is why the language of blame has no place in it, and why phrases that imply
the patient failed are both inaccurate and corrosive. Type B reactions in particular can be severe
and can be fatal, and they arrive without warning in people who were doing everything asked of
them.

Three practical things follow. Reporting a suspected reaction is a professional duty, not a
courtesy, and in many countries patients can report directly; the point of reporting is that it
protects somebody else. An allergy or intolerance label recorded carelessly follows a person for
life and can cost them the best treatment for a later illness, so accuracy at the moment of
recording is itself a safety intervention. And stopping a medicine on the strength of something
read in a revision answer carries its own risk, sometimes a serious one — that decision belongs
with the prescriber or pharmacist who can see the whole record. Anyone who thinks a medicine may
be harming them should contact their prescriber or pharmacist, and in an emergency contact
emergency services.

## What an examiner digs into next

* A reaction appears in one patient in several thousand. Why did the licensing trials not find it?
* Why is reducing the dose the wrong response to a type B reaction?
* What is wrong with calculating an incidence from spontaneous reports?
* Why is an inaccurate penicillin allergy label a patient safety problem rather than a tidiness
  problem?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* Your national pharmacovigilance scheme's own guidance on what to report and how — in the United
  Kingdom the Yellow Card Scheme operated by the Medicines and Healthcare products Regulatory
  Agency; in the United States the Food and Drug Administration's MedWatch programme; in the
  European Union EudraVigilance at the European Medicines Agency. Authority for reporting
  criteria, which differ between countries.
* The Uppsala Monitoring Centre, for the World Health Organization international drug monitoring
  programme and its causality assessment categories.
* Your national formulary's guidance on adverse reactions and on reporting — in the United Kingdom
  the British National Formulary, published by NICE with the pharmaceutical press. Authority for
  the reactions associated with any individual drug.
* The summary of product characteristics, or the regulator-approved prescribing information, for
  the product in question, for its characterised adverse reactions and their frequency categories.
* A standard clinical pharmacology textbook for the Rawlins–Thompson classification and for the
  DoTS framework described by Aronson and Ferner. Both are attributed here by name; neither is
  quoted.
* Your national or local guidance on recording and verifying drug allergy, and on penicillin
  allergy assessment specifically. This differs between countries and between institutions.
* Your national pharmacogenomic testing guidance for any genetic association named above,
  including the allele nomenclature, which should be checked rather than recalled.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only numbers above are the arithmetic of the rule of three**, which is
statistics rather than clinical data; no frequency, dose or threshold here describes any real
drug. Named drugs and named reactions appear as examples of a category. Reporting criteria,
allergy documentation standards and pharmacogenomic testing practice all differ between countries,
and where they do this answer says so rather than picking one. Nothing here should be used to make
a decision about anyone's treatment, including your own. Anyone who thinks a medicine may be
harming them should contact their own prescriber or pharmacist, and in an emergency contact
emergency services.

## Where this stands, October 2026

The classifications and the arithmetic do not date. The surveillance landscape does: schemes are
renamed and merged, patient reporting has expanded in several countries and not others, additional
monitoring lists change continuously, and pharmacogenomic testing recommendations move faster than
most of the rest of pharmacology. Check your own regulator's current guidance, and check any
allele name before using it.
