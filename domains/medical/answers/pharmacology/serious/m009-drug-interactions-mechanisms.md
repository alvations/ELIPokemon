---
id: "m009"
slug: drug-interactions-mechanisms
style: serious
category: pharmacology
difficulty: advanced
question: "Compare enzyme induction and enzyme inhibition mechanistically, and explain why protein-binding displacement usually matters less than it sounds."
tags: [interactions, induction, inhibition, protein-binding, cytochrome-p450]
---

# Inhibition is fast both ways, induction slow both ways, displacement a measurement problem.

Three mechanisms cover almost every clinically important drug interaction, and the useful way to
hold them apart is by **time course**, not by which enzyme is named.

* **Inhibition** of an enzyme or transporter: onset as soon as the inhibitor is present at a
  sufficient concentration, offset as the inhibitor clears.
* **Induction** of an enzyme or transporter: onset and offset both measured in days to a couple of
  weeks, because both require a change in how much enzyme protein exists.
* **Pharmacodynamic** interaction: no metabolic step at all, so no kinetic test will find it and
  no concentration measurement will explain it.

And the fourth thing students over-weight: **protein-binding displacement**, which changes a
number on a report far more than it changes a patient.

## Inhibition

Mechanistically, inhibition of a drug-metabolising enzyme is ordinary enzyme inhibition —
competitive at the active site, non-competitive, or mechanism-based, where the enzyme is
covalently modified by a reactive metabolite of the inhibitor. The first two are reversible; the
third is not.

The consequence of inhibition is **reduced clearance of the substrate**, so the substrate's
concentration rises and its half-life lengthens. Because the substrate must then climb to a new
steady state, the full magnitude of the interaction takes about five of the substrate's *new,
longer* half-lives to appear — which is why an interaction can be well established before anyone
notices it, even though the inhibition itself was immediate.

Reversible inhibition is **concentration-dependent and dose-dependent**: it switches on as the
inhibitor accumulates and off as it clears. Mechanism-based inhibition is the asymmetric case —
immediate onset, but recovery waits on resynthesis of the enzyme, so the offset looks like an
inducer's offset rather than an inhibitor's. That asymmetry is the single most useful thing to
know about this family, and it is *mechanism*, not guideline.

Well-established inhibitor examples, named for their mechanism and not for any magnitude:
clarithromycin and erythromycin, the azole antifungals such as fluconazole and ketoconazole,
ritonavir, grapefruit juice acting on intestinal CYP3A4, fluoxetine and paroxetine at CYP2D6, and
valproate inhibiting the glucuronidation of lamotrigine. Transporter inhibition belongs in the
same family: inhibition of P-glycoprotein by verapamil or amiodarone reduces the efflux of
digoxin. *All consensus mechanism; every magnitude belongs to an interactions reference.*

## Induction

Induction is not an effect on the enzyme. It is an effect on how much enzyme there is. An inducer
activates a nuclear receptor — the pregnane X receptor, the constitutive androstane receptor, the
aryl hydrocarbon receptor — which increases transcription of the enzyme gene. More enzyme protein
is then synthesised, and clearance of substrates rises.

Everything clinically awkward about induction follows from that one sentence.

* **Onset is slow**, because protein has to be made, and because the inducer itself has to reach
  steady state before it is inducing maximally. Days to a couple of weeks is the usual teaching.
* **Offset is also slow**, because the extra enzyme has to be degraded. Stopping the inducer does
  not stop the induction.
* **Therefore both ends are risk points.** Starting an inducer causes gradual loss of effect of
  the substrate. Stopping one causes a gradual rise in substrate concentration, arriving after the
  inducer has gone and often after anyone is still watching for it.
* **The direction is not always less effect.** If the induced enzyme *activates* a prodrug,
  induction increases the effect. The rule is about clearance, not about benefit.

Standard inducer examples: rifampicin, carbamazepine, phenytoin, phenobarbital and St John's wort.
Tobacco smoke is an inducer of CYP1A2, through the polycyclic aromatic hydrocarbons in the smoke
and not through nicotine — which is why stopping smoking is itself a pharmacokinetic event for
substrates such as clozapine and theophylline, and why nicotine replacement does not substitute
for the induction. *Consensus mechanism; magnitudes and the management are formulary and guideline
territory, and they differ between countries.*

## The time courses, side by side

```
   what has to happen before the interaction is at full size

   REVERSIBLE INHIBITION
       onset   inhibitor present at sufficient concentration        hours to a dose or two
               then substrate climbs to its new steady state        ~5 of the NEW half-lives
       offset  inhibitor cleared                                    a few inhibitor half-lives
       ──────────────────────────────────────────────────────────────────────────────────────
   MECHANISM-BASED (irreversible) INHIBITION
       onset   same as above                                        hours to a dose or two
       offset  enzyme RESYNTHESISED                                 days
       ──────────────────────────────────────────────────────────────────────────────────────
   INDUCTION
       onset   inducer at steady state  +  enzyme SYNTHESISED       days to ~2 weeks
       offset  extra enzyme DEGRADED                                days to ~2 weeks
       ──────────────────────────────────────────────────────────────────────────────────────
   PHARMACODYNAMIC
       onset   both drugs present at the effect site                as fast as the faster drug
       offset  either drug gone                                     as fast as the faster drug

   The asymmetric row is the one worth remembering: fast on, slow off. An irreversible
   inhibitor behaves like an inhibitor when it starts and like an inducer when it stops.
```

## Protein-binding displacement, and why it disappoints

```
   ILLUSTRATIVE arithmetic, chosen to show the shape -- not any real drug

   drug 99 % bound to albumin        free fraction = 1 %
   one competitor displaces it
   to 98 % bound                     free fraction = 2 %

        the free amount DOUBLED from a ONE POINT change in binding
        the TOTAL amount did not move at all

   What happens next, for a drug with low hepatic extraction (restrictive clearance):

        free concentration  ↑
             ↓
        rate of elimination ↑      (clearance acts on free drug, and clearance
             ↓                      itself was not changed by the displacement)
        total concentration ↓
             ↓
        NEW STEADY STATE:   free concentration back to where it started
                            total concentration LOWER
                            the ASSAY, which measures total, now looks alarming

   So the lasting consequence of pure displacement is usually a misleading total
   concentration, not a changed effect. The classic teaching error is to respond to
   the falling total by increasing the dose, which does change the effect.
```

Displacement *does* matter in three situations, and they are worth knowing because they are the
ones that are real: transiently, in the minutes to hours after a bolus, before re-equilibration;
for drugs with high extraction ratios, where free concentration genuinely drives elimination
differently; and whenever the displacing drug **also** inhibits elimination, which is common,
because a molecule that competes for albumin often competes for an enzyme too. Valproate and
phenytoin is the pairing always cited for exactly that reason — two mechanisms at once, and the
displacement is the less important of them.

## Pharmacodynamic interactions, which need no metabolic step

These are additive, synergistic or antagonistic effects at the level of the response, with no
shared enzyme, no shared transporter and nothing a concentration will reveal. Two drugs that
prolong the QT interval; two sedatives; two drugs that raise bleeding risk by different
mechanisms; multiple serotonergic drugs; the combination of a renin–angiotensin system inhibitor,
a diuretic and a non-steroidal anti-inflammatory acting together on renal perfusion, which is
widely taught under the label triple whammy.

Three things follow. They are frequently the most dangerous interactions and the least visible.
Automated interaction checkers represent them less completely than kinetic interactions, because
there is no enzyme to key on. And they cannot be managed by adjusting the dose of one party while
ignoring the other, because the interaction is in the shared endpoint rather than in either drug's
disposition.

## The human stakes, said plainly

The mechanisms above are abstract. The harm they cause is not, and it has a particular character.

An interaction that harms someone was not bad luck. Two medicines were prescribed, dispensed or
bought, and the combination was not caught — which makes the harm iatrogenic, caused by the care
rather than by the illness. The person who comes to harm did nothing wrong, and the most common
contributing factors are structural: more medicines than one prescriber can hold in mind, care
split across more than one service, a drug started by one team and a second started by another,
and a record that is complete nowhere.

Two practical consequences follow, and they are the ones that matter more than the enzyme names.
Harm suspected to come from an interaction is a suspected adverse drug reaction and is reportable
through the national scheme, by professionals and in many countries by patients directly;
reporting it is how the next person is protected. And stopping a medicine because of something
read in a revision answer carries its own risk, sometimes a serious one. That decision belongs
with the prescriber or pharmacist who can see the whole list, and anyone worried about a
combination they are taking should raise it with them.

## What an examiner digs into next

* An interaction appears two weeks after a drug was stopped. Induction or inhibition?
* Why does an irreversible inhibitor stop behaving like an inhibitor on withdrawal?
* A total concentration has fallen and the patient is unchanged. What is the most likely
  mechanism?
* Why do interaction checkers under-represent pharmacodynamic interactions?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* Your national formulary's appendix on interactions, and the monograph for each drug involved —
  in the United Kingdom the British National Formulary, published by NICE with the pharmaceutical
  press; elsewhere the equivalent national formulary. Authority for whether an interaction is
  clinically significant and what is done about it.
* A dedicated drug interactions reference maintained by a recognised body, used in your own
  institution, for the magnitude of any individual interaction. Magnitudes are deliberately absent
  above because they are substrate-specific and inhibitor-specific and cannot be generalised.
* The summary of product characteristics, or the regulator-approved prescribing information, for
  each product, which lists the interactions the licence holder has characterised.
* Your national medicines regulator's guidance on in vitro and clinical drug interaction studies,
  for how inducer and inhibitor classifications are assigned. The classification thresholds are
  regulatory and differ between jurisdictions.
* A standard clinical pharmacology textbook for the nuclear receptor pathways and for the
  restrictive-clearance argument about displacement.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **No interaction magnitude appears above, deliberately**, and the binding
percentages in the displacement block are illustrative figures invented to show the arithmetic.
Named drugs appear as examples of a mechanism, not as a list to act on, and whether any given
combination is acceptable is a decision for someone with the full record in front of them.
Practice differs between countries, formularies and institutions. Nothing here should be used to
make a decision about anyone's treatment, including your own. Anyone with a question about a
combination of medicines they are taking should raise it with their own prescriber or pharmacist.

## Where this stands, October 2026

The mechanisms and their time courses are stable: enzyme synthesis has always taken days and
always will. What moves is the catalogue — which drugs are classified as strong, moderate or weak
inducers and inhibitors, which interactions are flagged as clinically significant, and what the
recommended management is. Those change with every formulary edition and differ between countries.
Check the current interactions reference.
