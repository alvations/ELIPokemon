---
id: "m042"
slug: renal-and-hepatic-impairment
style: serious
category: pharmacology
difficulty: advanced
question: "Why do renal and hepatic impairment change prescribing in different ways, and why is there a usable number for one of them and not for the other?"
tags: [renal-impairment, hepatic-impairment, first-pass, protein-binding, clearance]
---

# One organ does one job and is gradable. The other does four jobs that fail at different rates.

Both organs reduce clearance, and that is where the resemblance ends. The kidney does essentially
**one** pharmacokinetically relevant thing — it removes water-soluble drug and water-soluble
metabolites from the plasma — and that one function can be estimated, graded and put in a table.
The liver does at least **four** things that matter to a prescription, they fail at different
rates in the same person, and no number summarises them. That asymmetry is the answer to the
question, and everything below is its consequence.

Claims are marked **[M]** mechanism, **[D]** definitional, **[C]** consensus, or **[L]** local —
differing by country, institution or formulary.

```
   RENAL                                   HEPATIC
   ─────────────────────────────────────   ──────────────────────────────────────────────
   one relevant function                   (1) phase I and phase II metabolism
      removal of polar drug and                (2) FIRST-PASS extraction
      polar metabolites                        (3) synthesis -- albumin, clotting factors
                                               (4) biliary excretion
   ─────────────────────────────────────   ──────────────────────────────────────────────
   gradable by an ESTIMATE of               composite severity scores exist (Child-Pugh is
   glomerular filtration                    the one always named) but they are PROGNOSTIC
                                            scores, not measures of metabolic capacity
   ─────────────────────────────────────   ──────────────────────────────────────────────
   so: a dosing TABLE, by band              so: drug-by-drug prose -- "avoid", "reduce",
                                            "use with caution" -- and that vagueness is
                                            honest, not lazy
   ─────────────────────────────────────   ──────────────────────────────────────────────
   effects point the SAME way               effects point in DIFFERENT directions, and
      (less clearance, more drug)              one of them INCREASES the dose that arrives
```

## The renal side, which is the tractable one

Reduced glomerular filtration reduces clearance of the renally eliminated fraction. Half-life
lengthens, the time to steady state lengthens with it, and the **maintenance** rate must fall. The
**loading** dose does not change, because a loading dose is computed from volume and a maintenance
rate from clearance — the arithmetic is in `m006` and getting it the wrong way round is the
commonest error in this topic.

Four things are worth knowing beyond that.

**Dose reduction versus interval extension are not equivalent.** Reducing each dose lowers the
peak and raises the trough; extending the interval keeps the peak and lowers the trough further.
Which you want depends on whether the drug's effect tracks the peak, the trough or the total
exposure **[M]** — see `m041`. For the aminoglycosides, whose killing is concentration-dependent
and whose toxicity relates to sustained exposure, that distinction is the entire design of the
regimen **[C]**, and the actual regimen is formulary territory and differs between countries.

**The estimate is an estimate, and it breaks at the extremes.** The routinely reported figure is
normalised to a standard body surface area, which is exactly what you want for staging kidney
disease and exactly what you do not want for dosing a narrow-index drug in someone very large or
very small. For those drugs an absolute clearance, un-normalised, is used instead **[C]**; which
drugs, and which estimating equation, is country- and institution-dependent **[L]**.

**Metabolites accumulate even when the parent does not.** A drug cleared hepatically to a polar
active metabolite behaves normally in renal impairment until the metabolite builds up. Morphine is
the standard teaching example and the consequence is prolonged effect from an apparently
reasonable dose **[C]**.

**Nephrotoxicity is a separate axis from clearance.** A drug may need dose reduction *because* the
kidney cannot clear it, or be avoided *because* it damages the kidney, or both, and the two
reasons have nothing to do with each other. Nonsteroidal anti-inflammatory drugs are the example
always given: they are not primarily a clearance problem, they reduce prostaglandin-dependent
renal perfusion, and the harm lands hardest where perfusion was already marginal **[M]**.

## The hepatic side, where the four functions fail separately

**1. Reduced metabolic clearance.** The expected effect: less clearance, longer half-life,
accumulation on repeated dosing. It arrives late, because the liver has substantial functional
reserve, so metabolic capacity falls non-linearly with visible severity of disease **[M]**.

**2. Loss of first-pass extraction — the one most often missed.** Oral bioavailability is the
absorbed fraction multiplied by the fraction that survives the gut wall and the liver:

```
   F  =  f(absorbed)  ×  ( 1 − E )          E = hepatic extraction ratio

   ILLUSTRATIVE, round figures chosen to make the point legible:

   high-extraction drug, intact liver        E = 0.9   →  F = 0.1
   same drug, extraction halved              E = 0.5   →  F = 0.5

                                   ┌────────────────────────────────────────────┐
   SAME ORAL DOSE                  │  FIVE TIMES the systemic exposure.         │
   SAME PRESCRIPTION               │  Nothing was changed. The barrier failed.  │
   SAME TABLET                     └────────────────────────────────────────────┘

   And note what is NOT affected: the intravenous dose, where F = 1 by definition.
   In liver disease the ORAL dose of a high-extraction drug is the dangerous one,
   and a prescriber who reasons from the intravenous dose will underestimate it.
   Low-extraction drugs barely move: 1 − 0.1 = 0.9, and halving 0.1 gives 0.95.
   The sensitivity to this effect is a property of E, not of the diagnosis.
```

Portosystemic shunting adds to it, because blood bypasses the hepatocytes entirely rather than
passing through a less capable liver **[M]**.

**3. Reduced albumin synthesis.** For a highly protein-bound drug, lower albumin means a higher
free fraction at the same total concentration. Two consequences: the measured total concentration
understates the active drug — the trap described in `m041` — and the apparent volume of
distribution changes, so the loading dose arithmetic shifts too. Note that this is a *transient*
increase in free drug for a drug with unchanged clearance, since a higher free fraction is also
more available for elimination; the steady-state free concentration is governed by clearance of
free drug. That subtlety is why protein-binding displacement matters less than it sounds, which is
`m009`'s territory **[M]**.

**4. Reduced synthesis of clotting factors, and altered sensitivity.** This is not kinetics at
all. The same concentration of an anticoagulant produces a larger effect when the substrate it
acts on is already depleted **[M]**. Likewise sedatives and opioids in hepatic encephalopathy: the
pharmacodynamic sensitivity is increased independently of any change in concentration **[C]**. An
answer that treats hepatic impairment as purely a clearance problem has missed half of it.

**And the direction can reverse.** A prodrug requiring hepatic activation does not accumulate when
the liver fails — it stops working. Codeine is the standard example, and the same logic applies to
any drug whose effect depends on a metabolic step **[M]**.

## Why there is no hepatic equivalent of an eGFR band

Three reasons, and they compound. The functions fail separately, so a single number would have to
summarise four quantities that are not correlated. The reserve means the relationship between
visible severity and metabolic capacity is non-linear and late-breaking. And the composite scores
that exist were built to predict outcome, not to predict clearance, so borrowing them for dosing
is using an instrument for something it was not calibrated against **[C]**.

The practical consequence is that hepatic dosing advice is **drug-specific and qualitative**, and
the monograph is the only authority. It is also why the two impairments do not simply add: the
common patient has both, the hepatorenal physiology is a single syndrome rather than two
independent insults, and the adjustments interact in ways no table encodes **[C]**.

## The human stakes, said plainly

The two groups of people this answer is about are among the most reliably harmed by prescribing.

Someone with kidney or liver impairment is given more medicines than average, is more likely to be
old, is more likely to be in hospital and is less able to tolerate an error when one happens. The
error is rarely arithmetic. It is a correct calculation applied to an assumption that was true of
someone else — a normalised filtration estimate used for a narrow-index drug in a very small
person, an oral dose reasoned from an intravenous one in liver failure, a total drug concentration
read as reassuring when albumin was low.

Harm from that is iatrogenic: caused by the care rather than the condition. Saying so is not an
accusation, and it is not a formality — it is what makes an event reportable, auditable and
preventable for the next person, and it correctly locates the fault in a system that let the
assumption through rather than in whoever was holding the chart.

Nothing in this answer is a dose, an adjustment or a threshold, and nothing in it should be used
to work out an amount for anyone. Anyone with a question about their own kidneys, liver or
medicines should raise it with their own prescriber or pharmacist, who can see the results this
answer cannot.

## What an examiner digs into next

* Clearance halves. What happens to the loading dose, and why?
* Why is the routinely reported filtration estimate the wrong one for a narrow-index drug in
  someone of unusual size?
* Which oral drugs are most sensitive to loss of first-pass extraction, and why those and not
  others?
* Why does a prodrug behave in the opposite direction to everything else in liver failure?
* Give two reasons a hepatic severity score is a poor guide to a dose.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../for-agents/SOURCES-pharmacology.md`](../../for-agents/SOURCES-pharmacology.md). Specific
to this answer:

* **Your national formulary's prescribing-in-renal-impairment and
  prescribing-in-hepatic-impairment guidance**, and the per-drug monograph for every drug named
  above. These are the authority for every adjustment, and they differ between countries.
* **Your laboratory's reported filtration estimate**, including which equation it uses and whether
  it is normalised to body surface area — a fact about your laboratory, not about the patient.
* **The summary of product characteristics or regulator-approved prescribing information** for
  each product, for its own impairment sections and for the bioavailability figure that makes the
  first-pass argument above quantitative.
* **A current standard clinical pharmacology or hepatology textbook** for the extraction-ratio
  derivation and for the composite severity scores, including what they were built to predict.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **Every number in this answer is an illustrative round figure, chosen to
make the extraction-ratio arithmetic legible.** None is a dose, an adjustment, a band boundary or
a threshold for any person, and no renal or hepatic dosing band appears here at all — those are
formulary and local property and they differ between countries. Nothing here should be used to
make a decision about anyone's treatment, including your own; the formulary, the product
information, the laboratory and local guidance are the authority. Anyone with a question about a
medicine they are taking should raise it with their own prescriber or pharmacist.

## Where this stands, October 2026

The structural argument above — one gradable function against four that fail separately — is
mechanism and does not date. The extraction-ratio algebra is a definition. What dates is
everything downstream: which estimating equation your laboratory reports and whether it is
normalised, which drugs carry an absolute-clearance caveat, the renal dosing bands themselves, and
the per-drug hepatic advice. Renal function reporting in particular has been revised in several
countries in recent years, including over whether to apply a race coefficient, and the answer
differs by country. Check the current laboratory practice and the current formulary rather than
any remembered band.
