---
id: "m011"
slug: the-undifferentiated-presentation
style: serious
category: general-practice
difficulty: advanced
question: "Why does an identical finding mean something different in general practice than in a hospital clinic, and how does prevalence change what it is worth?"
tags: [bayes, prevalence, predictive-value, referral, diagnosis]
---

# The finding does not change. The room does.

Sensitivity and specificity are properties of a test. Predictive value is a property of a test
*and* the population it is used in. A general practice and the clinic it refers into run the same
tests on the same bodies and get systematically different meanings out of them, because the
referral process has already sorted the population before the clinic sees it. The clinic's
patients are the ones somebody else already thought were worth a second look. That is not a detail
about paperwork; it is the single largest term in the arithmetic, and it is why a finding that
justifies action in a clinic can be a near-certain false alarm in a waiting room full of people
who mostly do not have anything *[mechanism, not guideline]*.

The named version of this is Bayes' theorem. The useful version is the two-by-two table, worked
twice.

## The arithmetic, worked

```
   ILLUSTRATIVE NUMBERS ONLY. A hypothetical test with sensitivity 90% and specificity 90%,
   applied to 10 000 people in two different rooms. These are round numbers chosen to make
   the mechanism visible. They are NOT the operating characteristics of any real test, and
   no real test should be assumed to behave like this one.

                      PRIMARY CARE                            REFERRED CLINIC
                  prevalence 1 in 100                      prevalence 30 in 100
   ┌───────────┬────────────┬────────────┐      ┌───────────┬────────────┬────────────┐
   │           │  disease + │  disease − │      │           │  disease + │  disease − │
   ├───────────┼────────────┼────────────┤      ├───────────┼────────────┼────────────┤
   │  test +   │        90  │       990  │      │  test +   │     2 700  │       700  │
   │  test −   │        10  │     8 910  │      │  test −   │       300  │     6 300  │
   ├───────────┼────────────┼────────────┤      ├───────────┼────────────┼────────────┤
   │  total    │       100  │     9 900  │      │  total    │     3 000  │     7 000  │
   └───────────┴────────────┴────────────┘      └───────────┴────────────┴────────────┘

   PPV =    90 / (  90 +  990) =   8.3 %        PPV = 2 700 / (2 700 + 700) =  79.4 %
   NPV = 8 910 / (8 910 +  10) =  99.9 %        NPV = 6 300 / (6 300 + 300) =  95.5 %

   Identical test. Identical positive result. Nearly ten times the chance of meaning
   something — and, going the other way, a negative result that was nearly conclusive in
   primary care has become a one-in-twenty miss in the clinic.
```

The same calculation in odds form shows what travels between the two rooms and what does not. The
positive likelihood ratio is sensitivity ÷ (1 − specificity) = 0.9 / 0.1 = **9**, and it is the
same 9 in both columns. Multiply it by the pre-test odds:

```
   primary care    pre-test odds  1 : 99   ×9 →   9 : 99  =  1 : 11   →   8.3 %
   referred clinic pre-test odds  3 :  7   ×9 →  27 :  7            →  79.4 %

   The likelihood ratio is portable. The prior is local. Learning a test's LR is durable
   knowledge; learning its PPV is knowledge about one population at one moment.
```

## Why the primary-care population is genuinely different

Four mechanisms, none of them about the clinician's skill *[mechanism, not guideline]*:

1. **Low prior probability of serious disease.** Most undifferentiated symptoms in an unselected
   population are self-limiting, and the absolute number of serious diagnoses is small, so the
   false positives of any test outnumber its true positives.
2. **Earlier and less differentiated presentation.** Symptoms arrive before the syndrome has
   assembled itself. A finding that is part of a recognisable pattern downstream arrives alone.
3. **The referral filter.** Referral is a selection mechanism, not a transfer. It enriches the
   downstream population for the thing being looked for, which is exactly why the downstream
   clinic's experience of a finding is a bad guide to the upstream clinic's.
4. **Different question.** Primary care is usually asked to exclude; the clinic is usually asked
   to characterise. Those need different test properties, and a test chosen for one is often the
   wrong instrument for the other.

## What follows for the consultation

* **Ruling out and ruling in are not the same operation.** With a low prior, a highly specific
  test that is positive is informative and a negative one tells you almost nothing you did not
  already believe. With a high prior, that inverts.
* **Time is an instrument.** Re-examining the same person three days later samples a different —
  and usually much more informative — distribution than any single test did, because the
  conditions that matter change over hours to days and the ones that do not, do not. This is the
  most powerful diagnostic tool in primary care and it does not appear on any request form.
* **Spectrum bias is real.** Sensitivity and specificity are not actually constant across
  settings: a test validated on clinic patients with advanced disease will usually perform worse
  on the earlier, milder spectrum seen upstream, so the two-by-two above is optimistic in the
  left-hand column rather than pessimistic.
* **Incidence and prevalence answer different questions.** For an acute presentation the relevant
  prior is how often this presents, not how many people have it.
* **Thresholds are local.** Who gets referred, on what finding, and how fast differs substantially
  between health systems — and that means the prevalence in the downstream clinic, and therefore
  the meaning of the identical finding, differs too *[country-dependent]*.

## What an examiner digs into next

Whether the candidate reaches for the likelihood ratio rather than the PPV, and can say why. Then
the asymmetry: which direction the test is being used in, and whether the chosen test is good at
that direction. Then the honest part — that the prior in a given practice population is not a
published number, is estimated from experience, and is the term with the largest uncertainty in
the whole calculation.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* Any standard clinical-epidemiology or evidence-based-medicine textbook, for the two-by-two
  table, likelihood ratios and the derivation of predictive value from prevalence.
* The published methodology of the diagnostic accuracy study behind any specific test being
  considered — specifically its stated setting and recruitment, which is what determines whether
  its quoted sensitivity and specificity transfer to a primary-care population.
* The suspected-cancer or urgent-referral criteria issued by the national or regional body that
  governs the reader's own practice, for the referral thresholds that set the downstream clinic's
  prevalence *[country-dependent]*.
* Any reporting-standards statement for diagnostic accuracy studies, issued by the relevant
  methodology group, for what a study must disclose about its setting and spectrum.

## Scope and safety

This is revision material about reasoning, written for someone already training in or qualified
for the field. It is not a clinical reference, not a decision aid, and not for use in making a
decision about any person's care. Every number in the worked example is a hypothetical round
figure chosen to make the arithmetic legible; none of them is the measured performance of a real
test, and none should be carried into practice. Referral criteria and the resulting case mix
differ by country, region and institution — local guidance is the authority here, and this is not.
If someone is unwell right now, the relevant action is to contact local urgent care or the local
emergency number, not to read this.

## Where this stands, October 2026

The mechanism described here — that predictive value depends on prevalence while likelihood ratios
do not — is settled and is not expected to move. What does move, and quickly, is which tests are
available in primary care, what their measured operating characteristics are, and the referral
thresholds that set downstream prevalence. All three should be re-checked against current local
guidance rather than taken from here, as of October 2026.
