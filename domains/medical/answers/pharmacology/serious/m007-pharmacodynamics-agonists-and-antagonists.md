---
id: "m007"
slug: pharmacodynamics-agonists-and-antagonists
style: serious
category: pharmacology
difficulty: advanced
question: "Distinguish agonist, partial agonist, antagonist and inverse agonist, and explain why a competitive antagonist shifts a dose-response curve while a non-competitive one flattens it."
tags: [pharmacodynamics, receptors, antagonism, efficacy, dose-response]
---

# Two independent properties, four ligand classes, and two different ways to spoil a curve.

Every ligand at a receptor can be described by two properties that vary independently.
**Affinity** is how readily it occupies the receptor; it sets where on the concentration axis
things happen. **Efficacy** is what the occupied receptor then does; it sets how high the response
can go. The four classes everyone memorises are just the four interesting combinations, and once
you hold affinity and efficacy apart, the competitive-versus-non-competitive distinction stops
being two shapes to remember and becomes a consequence.

| Class | Affinity | Efficacy | What it does to the system |
| --- | --- | --- | --- |
| Full agonist | yes | maximal positive | drives the response to the tissue maximum |
| Partial agonist | yes | submaximal positive | its own ceiling is below the tissue maximum, so in the presence of a full agonist it *reduces* the response |
| Antagonist | yes | zero | occupies without activating, and denies the site to anything else |
| Inverse agonist | yes | negative | drives the response *below* the unstimulated baseline |

Two of those entries need defending.

**A partial agonist is an antagonist when a full agonist is present.** It is competing for the
same site and producing less when it wins, so adding it to a maximally stimulated system lowers
the response. Add it to an unstimulated system and the response rises. The same molecule, opposite
directions, depending entirely on what else is there. Buprenorphine at opioid receptors is the
teaching example, and that it behaves this way is *consensus mechanism*; the clinical handling of
it is guideline territory and differs between countries.

**An inverse agonist needs a receptor with constitutive activity to be a coherent idea.** If the
unoccupied receptor signals at some background level, a ligand can reduce that background, and the
response falls below the no-drug baseline. If there is no constitutive activity there is nothing
to reduce, and an inverse agonist is indistinguishable from an antagonist. A number of drugs long
classified as antagonists are now described as inverse agonists at receptors shown to be
constitutively active — some beta-adrenoceptor antagonists among them. That reclassification is
*mechanism established in pharmacology*, and the clinical consequences of it are modest and
debated; it is not a reason to treat the drugs differently.

## The arithmetic

```
   FRACTIONAL OCCUPANCY by an agonist A with dissociation constant K_D

        occupancy  =  [A] / ( [A] + K_D )

        [A] / K_D     0.1     0.3      1       3      10      30     100
        occupancy     9 %    23 %    50 %    75 %    91 %    97 %    99 %
                                      ▲
                                      half-maximal occupancy sits at [A] = K_D,
                                      which is what K_D MEANS. Not a measurement
                                      of any drug; the definition.

   COMPETITIVE antagonist B at concentration [B], dissociation constant K_B
   (the Schild relationship; algebra, not a clinical figure)

        dose ratio  =  1  +  [B] / K_B

        [B] / K_B       0       1       9      99     999
        dose ratio      1       2      10     100    1000
        agonist needed  ×1      ×2     ×10    ×100   ×1000     ceiling UNCHANGED

   NON-COMPETITIVE antagonist taking a fraction f of receptors out of play

        [B] blocks f      0 %    25 %    50 %    75 %    90 %
        ceiling          100 %    75 %    50 %    25 %    10 %     ceiling FALLS
        (in a tissue with no receptor reserve -- see below, because that caveat
         is where most exam answers come apart)
```

```
   effect, as a percentage of the control maximum

   100 ┤ control                ┌──────────────────  ceiling reached
       │                        │
       │ + competitive B                    ┌──────  SAME ceiling, ~10× the agonist
       │                                    │
    50 ┤ + non-competitive B    ┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌  ceiling at 50 %, and no
       │                        │                    concentration of agonist
       │                        │                    ever reaches 100 %
     0 ┼────────────────────────────────────────▶  log [agonist]

         competitive     : parallel rightward shift, surmountable
         non-competitive : depressed ceiling, insurmountable
```

## Why the two shapes follow from the mechanism

A **competitive** antagonist binds the same site, reversibly. Occupancy is then a competition
between two concentrations, so raising the agonist concentration raises the agonist's share of a
fixed number of sites without limit. Every receptor remains *available*, so the maximum response
is untouched and the whole curve slides right by the dose ratio. Surmountability is the diagnostic
feature, and it is also why the clinical significance of a competitive antagonist depends on the
agonist concentration it is up against — naloxone at opioid receptors is competitive, which is
exactly why its duration relative to the agonist matters.

A **non-competitive** antagonist removes receptors from the pool. It may bind elsewhere on the
receptor and prevent activation, or bind the orthosteric site irreversibly. Either way the agonist
cannot compete for what is no longer there, so the ceiling falls and no concentration restores it.
Aspirin's acetylation of cyclo-oxygenase and omeprazole's covalent inhibition of the proton pump
are the standard irreversible examples; neither is receptor antagonism, but both show the defining
property — recovery waits on synthesis of new protein, not on clearance of the drug. That is
(**mechanism**), and it is the reason the duration of effect of such a drug has nothing to do with
its half-life.

**Receptor reserve is the caveat that matters.** Many tissues have far more receptors than are
needed for a maximal response. In such a tissue, taking 50% of receptors out of play may not lower
the maximum at all — the curve shifts right instead, and a non-competitive antagonist *looks*
competitive until you push further. The same reserve makes a partial agonist look like a full one.
So the curve shape tells you about the tissue as much as about the drug, and the clean textbook
pictures above are the no-reserve case.

## Selectivity, and the case of no effect at all

A drug with no affinity for a receptor does nothing at it, at any concentration. That is the
cleanest fact in pharmacodynamics and the easiest to forget: an antagonist with no agonist to
oppose produces very little, and a receptor the drug cannot bind is not a weak target but a
non-target.

Selectivity, though, is almost always **relative and concentration-dependent**. A beta-1 selective
antagonist is selective at usual concentrations and progressively less so as concentration rises,
because selectivity reflects a ratio of affinities and not an absolute exclusion. This is standard
consensus and is why selectivity is described rather than promised. Specificity in the strict
sense — one target only — is rare enough that it is safer to assume it does not hold.

## The human stakes, said plainly

Receptor theory is abstract. The place it is used most urgently is not.

Opioid overdose and its reversal are competitive antagonism in practice, and the mechanism carries
consequences that are not abstract at all. A competitive antagonist with a shorter duration of
action than the agonist it is opposing can wear off while the agonist is still present, so someone
who has responded can deteriorate again — which is why reversal is never the end of an episode of
care. Giving a full antagonist to someone physically dependent on an opioid precipitates
withdrawal, and withdrawal is severe distress, not a curve shifting on a graph. The same is true
of a partial agonist displacing a full one.

These are the points at which a reader could be a person rather than a student, and the right
thing to say is the plain thing: if anyone may have taken too much of any medicine or drug,
contact emergency services immediately. Nothing in this answer can be used to decide whether
someone is safe, and the decision about any medicine belongs with the prescriber or pharmacist who
holds the record.

## What an examiner digs into next

* A curve shifts right with no fall in maximum. What single experiment distinguishes competitive
  antagonism from a change in agonist potency?
* Why does an irreversible inhibitor's duration of action not follow its half-life?
* Draw what a partial agonist does to a full agonist's curve, and say which direction and why.
* How would receptor reserve change your interpretation of both diagrams above?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* A standard pharmacology textbook for receptor theory, the occupancy equation and the Schild
  relationship. The algebra above is derivable from first principles and checkable without a
  source.
* The International Union of Basic and Clinical Pharmacology, through its guide to pharmacology
  database, for receptor nomenclature and for which ligands are currently classified as inverse
  agonists. Authority for classification, which has changed for several drugs.
* Your national formulary's monograph for any drug named here — in the United Kingdom the British
  National Formulary, published by NICE with the pharmaceutical press; elsewhere the equivalent.
  Authority for anything about how these drugs are actually used.
* The summary of product characteristics, or the regulator-approved prescribing information, for
  the specific product, for its stated receptor selectivity.
* Your national guidance on opioid substitution and on opioid overdose management, for anything
  concerning buprenorphine or naloxone in practice. This differs substantially between countries
  and no single document covers it.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. The numbers above are arithmetic on defined quantities, not measurements of
any drug, and none is a dose or a target. Drug classification moves, selectivity claims are
relative, and the clinical use of every drug named differs between countries and formularies.
Nothing here should be used to make a decision about anyone's treatment, including your own.
Anyone with a question about a medicine they are taking should raise it with their own prescriber
or pharmacist, and in a suspected overdose of any kind the right action is to contact emergency
services immediately rather than to reason about receptor occupancy.

## Where this stands, October 2026

Receptor theory is stable; the equations above have not changed in decades and will not. What
moves is classification — which ligands are called inverse agonists, how selectivity is described
on a label — and everything about clinical use. Check the current formulary and the current
receptor nomenclature before relying on a classification stated here.
