---
id: "m147"
slug: prescribing-errors-as-a-system-property
style: serious
category: pharmacology
difficulty: intermediate
question: "Why are prescribing errors better described as a property of the system than of the prescriber, where do they cluster, and why are the clusters predictable?"
tags: [medication-safety, prescribing-errors, human-factors, system-design, transitions]
---

# If an error is a property of a person, it happens once. If it is a property of a place, it happens there again.

The test is empirical and it settles the argument. Take any large audit of prescribing error and
look at where the errors are. They are not spread evenly across prescribers in proportion to how
careful those prescribers are. They are concentrated at particular steps, particular times,
particular drug groups and particular handovers — and the concentration reproduces across
institutions, countries and decades. A hazard that reappears in the same places with different
people standing in them is a property of the places.

That is not a claim that individual care is irrelevant. It is a claim about where the leverage is.
Telling a prescriber to be careful at a step that defeats careful people is not an intervention;
it is a description of the problem restated as advice.

Claims below are marked inline with what they rest on: (**mechanism**), (**definitional**),
(**consensus**), or (**country-dependent**).

## Three things that get called the same thing

| Term | What it is | Who investigates it | Does harm follow? |
| --- | --- | --- | --- |
| **Adverse drug reaction** | a harmful, unintended response to a medicine at a dose used for a legitimate purpose | pharmacovigilance systems; see `m010` | by definition yes |
| **Medication error** | a failure in the process of prescribing, dispensing, preparing, administering or monitoring | local incident systems and clinical governance | often not — most errors reach nobody |
| **Preventable adverse drug event** | harm that occurred and that an error caused | both, usually jointly | yes, and it is the overlap of the two rows above |

Keeping these apart is not pedantry (**definitional**). They have different denominators,
different reporting routes and different fixes, and the commonest confusion in exam answers is to
treat the error rate and the harm rate as the same quantity. Most errors are intercepted; a
minority of errors cause most of the harm; and the drugs involved in that minority are a short and
stable list.

## Where they cluster

```
   THE PRESCRIBING PROCESS, AND WHERE THE DENSITY IS

   step                        what can fail here              cluster strength
   ──────────────────────────────────────────────────────────────────────────────
   1  decide to treat          wrong indication, no indication        ░░
                               duplicate of something already
                               prescribed under another name         ███

   2  choose the drug          allergy or intolerance not checked    ███
                               interaction not checked               ███
                               contraindication in organ impairment  ███
                               look-alike / sound-alike selection    ███

   3  choose dose and route    wrong units, wrong strength           ██
                               decimal point                         ███
                               weight-based arithmetic               ███
                               no adjustment for organ function      ███

   4  write it down            illegible, ambiguous, abbreviated     ██
                               incomplete: no route, no duration     ███
                               verbal order not confirmed            ██

   5  communicate it           omission at admission or discharge    ████
                               change made and not told to anyone    ████

   6  monitor it               the planned test never happens        ███
                               stop date passes and nothing stops    ████
   ──────────────────────────────────────────────────────────────────────────────

   And the three conditions that multiply ALL of the above:
       interruption during the task
       unfamiliarity -- new system, new ward, new specialty, first week
       the hours between about 02:00 and 06:00
```

## Why the clusters are predictable

Each cluster has a mechanism, and once named it stops looking like bad luck (**mechanism**).

**Transitions lose information because nobody owns the whole list.** Admission and discharge are
the two points at which a medication list is rebuilt from sources that disagree: what the person
says, what the record says, what the community pharmacy dispensed, what the previous team changed
last week. A rebuild from inconsistent sources produces omissions and reintroductions, and it does
so whoever performs it. This is why **medicines reconciliation** exists as a named, resourced task
with an owner rather than as something assumed to happen (**consensus**). `m002` is the handover
half of the same problem and `m014` is the polypharmacy half.

**Similar names collide because the selection step is recognition, not recall.** A prescriber
choosing from a picklist, or writing from memory, is performing a recognition task among similar
strings. Error rates in recognition tasks rise with similarity of the alternatives, which is a
property of the list and not of the chooser. The structural answers are therefore about the list:
tall-man lettering, separating confusable products in storage and in menus, and removing
error-prone abbreviations entirely (**consensus**).

**Decimal and unit errors are a notation failure.** A trailing zero, a naked decimal point and an
abbreviation for a unit are each a single character away from a ten-fold or thousand-fold
difference, and the reader has no redundancy to detect the slip. Hence the standard rules —
no trailing zeros, a leading zero always, micrograms written in full, and an independent second
check on the specific calculations that carry the largest consequence (**consensus**).

**A small number of drug groups account for most serious harm**, consistently: anticoagulants,
insulin and other hypoglycaemic agents, opioids and other sedating agents, injectable potassium,
cytotoxics, and antimicrobials in the people whose organ function cannot clear them. These are
often handled as a named high-risk category with extra controls (**consensus**,
**country-dependent** as to exactly which list is used). The reason the list is short is also
mechanistic: these are the drugs where a moderate dosing error crosses into physiological harm
quickly, which is `m008`'s therapeutic-index argument applied to the error rather than to the
dose.

**Omission is the commonest error and the least visible.** Nothing happens when a dose is not
prescribed. There is no artefact to notice, which is why omissions are under-reported relative to
their frequency and why the systems that catch them have to look for absence rather than wait for
an event (**mechanism**).

## Slips, mistakes and violations: the distinction decides the fix

The human-factors classification earns its place because each category responds to a different
intervention (**mechanism**, **consensus**). The framework is usually credited to Reason, whose
model of active failures sitting on top of latent organisational conditions is the standard
account.

* A **slip or lapse** is a failure in executing a correct intention — the right drug intended, the
  wrong one selected; the intention formed, the step forgotten. These respond to **constraints and
  forcing functions**, and not at all to teaching, because the knowledge was never missing.
* A **mistake** is a failure of the intention itself — the wrong rule applied, or no rule known.
  These respond to **decision support, protocols and education**, because something genuinely was
  not known.
* A **violation** is a deliberate deviation from a known rule, and the useful question is why the
  rule was deviable: a workaround that everyone uses is usually evidence that the prescribed
  process does not fit the work. Treating a routine violation as a discipline problem reliably
  removes the signal and leaves the condition (**consensus**).

The practical consequence is a hierarchy of effectiveness that runs in roughly the reverse of the
order interventions are usually reached for: making the error physically impossible beats
constraining it, which beats automating the check, which beats reminding, which beats training,
which beats telling people to be careful. Education is the most-used and weakest layer, because it
is the cheapest to deploy and the only one that requires no change to anything else.

## Electronic prescribing moves the errors, and makes a new set

Electronic systems remove whole classes of error: illegibility, ambiguity, unavailable records,
missing dose units, and much of the arithmetic (**consensus**). They also create classes that did
not previously exist, and the new ones are better described as design failures than as user
failures (**mechanism**).

* **Selection from a list** replaces writing, so the error becomes picking the adjacent entry — a
  different strength, a different salt, a different route, a paediatric formulation.
* **Defaults** are powerful: a default that is right in most cases will be accepted in the cases
  where it is wrong.
* **Copy-forward** of a previous list propagates an old error faithfully and makes it look
  reviewed.
* **Alert fatigue** is the central one. A system that interrupts for every theoretically possible
  interaction trains its users to dismiss interruptions, and the override rate for low-value
  alerts is high enough that the high-value alert is dismissed with the rest. The fix is fewer and
  better alerts, which is a harder engineering and governance problem than more alerts.

So the honest summary is that electronic prescribing is a large net gain whose benefit depends
almost entirely on configuration, and that an audit of a new system should be looking for the new
error types rather than confirming the absence of the old ones.

## The human stakes, said plainly

Three things here are about people and not about process.

**Someone is harmed at the end of a preventable medication error, and that is the reason any of
this matters.** The systems vocabulary in this answer is a tool for preventing that, not a way of
making it abstract. Where harm has occurred, the duty in most jurisdictions is explicit: tell the
person what happened, say plainly that it should not have, explain what is being done, and record
it. Being open about an error is not an admission that ends a career; concealment is what does
that, and it also removes the only information that would have prevented the next one.

**An inaccurate record causes durable harm of its own.** The clearest example is an allergy label
applied to what was an intolerance or a coincidental rash: it follows a person for life, it
removes first-line options from every future prescriber, and the documented consequences include
worse outcomes from the alternatives used instead. Recording accurately — what happened, when, how
— is a clinical act with a long tail, and `m010` is where the reaction classification that makes
it possible lives.

**Blame removes information.** A culture that treats error as a character failing produces fewer
reports, not fewer errors, and the reports it does produce are the ones that could not be hidden.
The alternative is not an absence of accountability: a just culture distinguishes human error from
at-risk behaviour from genuinely reckless choice, and responds differently to each. The
distinction is the point, and it is a management discipline rather than a sentiment. Staff
involved in a serious error also need support, which is a practical requirement rather than a
courtesy, because an unsupported person makes the next one.

Nothing in this answer indicates what anyone should take, start or stop, and no prescribing
decision should be made from it.

## What an examiner digs into next

* Distinguish an adverse drug reaction, a medication error and a preventable adverse drug event.
  Which has the largest denominator?
* Why is omission both the commonest prescribing error and the most under-reported?
* Which of slip, mistake and violation responds to education, and which does not — and why is
  education the most-used intervention anyway?
* Name three error classes electronic prescribing abolishes and three it creates.
* Why does a system that alerts on every possible interaction end up less safe than one that
  alerts on few?
* Why are transitions of care the densest cluster, and what is the named task that addresses them?
* Why does an inaccurate allergy label cause measurable harm, and what kind of harm?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* **Your own institution's medicines policy and its incident-reporting procedure.** For everything
  in this answer about what is actually required — second checks, high-risk drug lists,
  reconciliation ownership, who may take a verbal order — the local document is the authority and
  it is what you will be held to.
* **Your national patient-safety body's alerts and guidance on medication safety**, including its
  list of error-prone abbreviations and its guidance on injectable medicines. The organisation
  differs by country and so does the list.
* **The world health organization's global patient safety challenge on medication safety**, for
  the high-risk situations framing and the transitions-of-care material, and its guidance on
  medication without harm.
* **The national competency framework for prescribers used where you train**, for what a complete
  prescription must contain, which is the checklist the "write it down" row above is measured
  against.
* **A current human-factors or patient-safety textbook**, for the slip/mistake/violation
  classification, the active-failure and latent-condition model, and the hierarchy of intervention
  effectiveness.
* **The primary literature**, for any figure about error rates, interception rates, alert override
  rates or the proportion of harm attributable to particular drug groups. This answer states no
  such figure, deliberately: they vary enormously with setting and with how the study counted.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. It names no error rate, no dose, no high-risk threshold and no override
figure: those are properties of particular settings and particular studies, and an invented one
would be a more serious defect than anything else in this answer. The high-risk drug groups named
are a widely used framing and not a complete or authoritative list; the one that applies where you
work is in your local policy. Nothing here indicates what anyone should take, start or stop, and a
concern about a specific medicine in a specific person belongs with their prescriber or
pharmacist.

## Where this stands, October 2026

The mechanisms — information loss at transitions, recognition failure among similar names,
notation without redundancy, the short list of drugs where a moderate error crosses into harm —
are mechanism and do not date. The scaffolding does. **What counts as a reportable incident**, who
investigates it and under what framework is national and is revised. **Error-prone abbreviation
lists and high-risk drug lists** are maintained documents that change. **Electronic prescribing**
is the fastest-moving part: the specific new error types depend on the product and its local
configuration, prescribing-decision support is being rebuilt around automated and predictive
components whose own failure modes are not yet well characterised, and anything written now about
alert design will date quickly. Check your institution's current policy and your national
patient-safety body.
