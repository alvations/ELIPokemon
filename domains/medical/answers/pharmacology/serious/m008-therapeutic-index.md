---
id: "m008"
slug: therapeutic-index
style: serious
category: pharmacology
difficulty: intermediate
question: "What is the therapeutic index, and what does a narrow one change about how a drug is monitored, substituted and assessed for interactions?"
tags: [therapeutic-index, monitoring, bioequivalence, toxicity, variability]
---

# A ratio of two population medians, and the reason a narrow one changes everything downstream.

The therapeutic index is the ratio of a toxic dose to an effective dose, conventionally **TI =
TD50 / ED50** — the dose toxic in half the population over the dose effective in half of it, and
in the animal work the idea comes from, LD50 over ED50. A large ratio means there is a lot of room
between the dose that works and the dose that harms. A small one means there is not.

Two caveats belong in the first paragraph, not the last, because they are what separates an exam
answer from a recited definition.

**It is a ratio of medians, so it says nothing about spread.** Two drugs with the same index can
differ completely in how many people sit in the region where the effect curve and the toxicity
curve overlap. A measure that respects that is the **certain safety factor**, TD1 / ED99 — the
dose toxic in one per cent over the dose effective in ninety-nine — which asks the clinically
honest question: is there a dose that works for almost everyone and harms almost no one?

**It is not something anyone measures in humans the way it is defined.** You cannot run a TD50
study in people. So in practice *narrow therapeutic index* is a label applied by consensus and by
regulators to drugs with a demonstrated narrow margin, and the drugs on the list differ between
countries. Digoxin, lithium, phenytoin, warfarin, ciclosporin, tacrolimus, levothyroxine,
theophylline, carbamazepine and the aminoglycosides are the names that appear in most teaching;
that they are narrow-margin drugs is consensus, while the formal list and its consequences are
jurisdiction-specific.

## The arithmetic of why a small change matters for one drug and not another

```
   therapeutic index  =  TD50 / ED50

   ILLUSTRATIVE drug W (wide)     ED50 = 1 unit    TD50 = 100 units   TI = 100
   ILLUSTRATIVE drug N (narrow)   ED50 = 1 unit    TD50 =   2 units   TI =   2
   (round figures chosen to make the sum legible; they are not any real drug)

   Now apply the same 30 % rise in exposure -- an interaction, a renal change,
   a different formulation -- to each, starting part-way up the window:

                        exposure before   after + 30 %   inside the window?
   ─────────────────────────────────────────────────────────────────────────────
   drug W,  window 1-100       10            13.0        yes, by a mile
   drug N,  window 1-2          1.5           1.95       yes, but only just
   drug N,  window 1-2          1.6           2.08       NO
   ─────────────────────────────────────────────────────────────────────────────

   THE SAME 30 %. The interaction did not change. What changed is how much room
   there was. This is why an interaction graded as minor for one drug is graded
   as serious for another, with no difference in the mechanism at all.
```

```
      effect                                      toxicity
      ▲                                                ▲
      │   ┌──────────────  wide index  ────────────┐    │
      │   │  effect curve      ▏   ▏  toxicity curve│   │
      │   └────────────────────▏───▏────────────────┘   │
      │                    big gap, no overlap          │
      │                                                 │
      │   ┌──────  narrow index  ──────┐                 │
      │   │  effect curve ░░░░ toxicity│                 │
      │   └───────────────░░░░─────────┘                 │
      │                   ▲                              │
      │                   └── the overlap IS the clinical problem: a dose
      │                       effective for one person is toxic for another
      └──────────────────────────────────────────────────▶  dose or exposure
```

## What a narrow index actually changes

**Monitoring moves from the effect to the concentration — but only sometimes.** Measuring a
concentration is worth doing when four conditions hold together: the effect is hard to observe
directly, toxicity is hard to distinguish from the untreated condition, there is an established
relationship between concentration and response, and an assay exists. Where the effect itself is
measurable, the effect is the better monitor — anticoagulation with warfarin is monitored by its
pharmacodynamic consequence rather than by a warfarin concentration, and that is a deliberate
choice, not an accident of assay availability. *Consensus mechanism; the targets and the intervals
are guideline and differ between countries.*

**The sample time is part of the result.** A concentration without a time is uninterpretable,
which is why trough sampling is specified and why a sample drawn before steady state cannot be
read as a steady-state number. That last point is the link back to kinetics: steady state arrives
after about five half-lives and nothing accelerates it except a loading dose, so a concentration
drawn on day two of a drug with a long half-life is a true measurement of the wrong thing.

**Formulation substitution stops being routine.** Two products accepted as bioequivalent are not
identical; they are the same within an acceptance window. For a wide-index drug that window is
irrelevant. For a narrow one it can be a material fraction of the therapeutic range, which is why
some regulators apply tighter bioequivalence criteria to narrow-index drugs and why continuity of
a specific product is sometimes preferred over generic substitution. *The acceptance limits, the
list of drugs they apply to, and the strength of the preference are all set by the national
regulator and differ between countries.* In the United Kingdom the medicines regulator groups
antiepileptics according to whether continuity of the specific manufacturer's product matters;
other countries handle the same problem differently, and the grouping is a claim to check in your
own jurisdiction rather than to carry across borders.

Modified-release and immediate-release forms of the same drug are a sharper version of the same
problem: they are not interchangeable even at the same nominal daily amount, because the shape of
the concentration-time curve differs and a narrow window is sensitive to shape.

**Interaction significance is recalculated.** A pharmacokinetic interaction has a magnitude;
whether that magnitude matters is a property of the window, as the arithmetic above shows. The
practical consequence is that interaction references flag narrow-index drugs at exposure changes
they would ignore elsewhere, and that is correct rather than over-cautious.

**Non-linear kinetics compound it.** Where elimination is saturable, a proportional increase in
dose produces a more than proportional increase in concentration, so a narrow window and saturable
kinetics together are the worst combination in pharmacology. Phenytoin is the standard teaching
example of saturable elimination, and that is (**mechanism**), not guideline.

**And the organisational consequences.** Narrow-index drugs attract named-product prescribing,
specified monitoring schedules, patient-held records in some systems, restrictions on who may
initiate, and alerts in prescribing software. None of that is about the chemistry. It is all
downstream of one ratio being small.

## The human stakes, said plainly

The sections above are about mechanism. The consequence is not a mechanism. A toxic concentration
of a narrow-index drug can cause serious harm and can be fatal, and overdose — deliberate or
accidental — is a medical emergency, not a pharmacokinetics problem to be reasoned about. If
anyone may have taken too much of any medicine, the right action is to contact emergency services
or the national poisons service immediately. Reading about the ratio is not a substitute for that,
and no part of this answer should be used to judge whether a dose someone has taken is safe.

And where a narrow-index drug does harm inside the therapeutic range — a substitution nobody
flagged, a monitoring result nobody chased, a concentration drawn at the wrong time and read as
though it were a trough — that harm was caused by the care rather than by the illness. It is
iatrogenic, and the person it happened to did nothing wrong. Naming it that way is not a
formality: it is what makes it reportable, auditable and preventable for the next person.

## What an examiner digs into next

* Why is the certain safety factor a better safety measure than the therapeutic index?
* A concentration comes back inside the range and the patient is toxic. Give three explanations.
* Why are modified-release and immediate-release products not interchangeable?
* What makes saturable elimination and a narrow window so much worse together than separately?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* Your national formulary's monograph for each drug named above, and its guidance on therapeutic
  drug monitoring — in the United Kingdom the British National Formulary, published by NICE with
  the pharmaceutical press; elsewhere the equivalent national formulary. Authority for every
  range, interval and sampling time.
* Your national medicines regulator's guidance on bioequivalence, and its guidance on generic
  substitution for narrow therapeutic index drugs. Authority for the acceptance limits this answer
  deliberately does not state, and for which drugs they apply to.
* The medicines regulator's advice on antiepileptic product continuity for your own country — in
  the United Kingdom the Medicines and Healthcare products Regulatory Agency. The categories named
  above are country-specific and must be read locally.
* The summary of product characteristics, or the regulator-approved prescribing information, for
  the specific product, for its monitoring requirements.
* Your local laboratory handbook or therapeutic drug monitoring service for assay-specific
  reference ranges and sampling times, which differ between laboratories as well as between
  countries.
* Your national poisons information service for the management of any overdose.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The therapeutic windows and exposure changes above are illustrative round
figures invented to make arithmetic legible, and no number here is any real drug's range.** Named
drugs appear only as examples of a category. Practice differs between countries, regulators and
laboratories, and where it does this answer says so rather than picking one. Nothing here should
be used to make a decision about anyone's treatment, including your own; the formulary, the
product information, the laboratory and local guidance are the authority. Anyone with a question
about a medicine they are taking should raise it with their own prescriber or pharmacist. In a
suspected overdose, contact emergency services.

## Where this stands, October 2026

The ratio and the arithmetic do not date. Everything attached to a particular drug does: which
drugs are formally designated narrow therapeutic index, what bioequivalence limits apply to them,
which monitoring is expected and at what intervals. Those are regulatory decisions, they differ
between countries, and they change. Check the current formulary and your own regulator.
