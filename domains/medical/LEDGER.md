# Pokémon-ness ledger — medical domain

How much each Pokémon answer leans on **named** Pokémon entities rather than generic
furniture. Same deterministic scorer as the machine-learning domain, same vocabulary, so
the two are comparable and a vocabulary fix moves both.

**The mandated plain-prose sections are excluded from scoring** — `Where the metaphor
stops`, `The human stakes, said plainly`, `Sources` and `Scope and safety`. They are
required to contain no analogy, so scoring them would penalise an answer for complying.

Regenerate with `python3 scripts/medical/score.py --write`.

**35 answers · mean 87.5 · median 86.7 · min 62.6 · max 100.0**

| score | band | id | specialty | answer | distinct | named | generic |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 62.6 | adequate | m022 | endocrinology | insulin-as-a-control-problem | 12 | 28 | 67 |
| 63.3 | adequate | m025 | endocrinology | ketoacidosis-and-the-hyperosmolar-state | 11 | 28 | 50 |
| 69.6 | strong | m018 | dermatology | assessing-skin-of-colour | 13 | 32 | 20 |
| 73.4 | strong | m024 | endocrinology | why-the-complications-differ | 14 | 30 | 49 |
| 76.0 | strong | m010 | pharmacology | adverse-drug-reactions | 15 | 32 | 49 |
| 76.5 | strong | m029 | oncology | response-assessment-and-surrogates | 20 | 31 | 53 |
| 78.9 | strong | m035 | emergency | first-aid-for-untrained-bystanders | 14 | 28 | 20 |
| 80.3 | excellent | m032 | emergency | why-protocols-exist | 24 | 34 | 88 |
| 80.4 | excellent | m026 | oncology | staging-against-grading | 20 | 30 | 59 |
| 81.6 | excellent | m019 | dermatology | topical-therapy-and-quantity | 18 | 30 | 21 |
| 83.1 | excellent | m002 | nursing | handover-and-escalation | 19 | 31 | 72 |
| 84.1 | excellent | m005 | nursing | fluid-balance-charting | 20 | 27 | 54 |
| 84.3 | excellent | m014 | general-practice | polypharmacy-and-deprescribing | 20 | 31 | 53 |
| 85.1 | excellent | m028 | oncology | why-toxicity-is-predictable | 21 | 51 | 45 |
| 85.3 | excellent | m027 | oncology | how-systemic-therapies-differ | 27 | 60 | 40 |
| 85.4 | excellent | m001 | nursing | early-warning-scores | 24 | 35 | 64 |
| 86.3 | excellent | m023 | endocrinology | glycation-marker-and-continuous-monitoring | 35 | 47 | 50 |
| 86.7 | excellent | m020 | dermatology | dermoscopy-in-principle | 22 | 35 | 42 |
| 88.3 | excellent | m030 | oncology | screening-and-overdiagnosis | 26 | 59 | 15 |
| 89.0 | excellent | m012 | general-practice | red-flags-and-safety-netting | 15 | 46 | 21 |
| 91.2 | excellent | m015 | general-practice | continuity-of-care | 32 | 42 | 72 |
| 91.3 | excellent | m009 | pharmacology | drug-interactions-mechanisms | 27 | 52 | 63 |
| 91.8 | excellent | m034 | emergency | compensation-and-the-sick-patient | 20 | 37 | 34 |
| 95.6 | excellent | m008 | pharmacology | therapeutic-index | 20 | 48 | 52 |
| 96.5 | excellent | m017 | dermatology | distribution-and-configuration | 22 | 43 | 22 |
| 97.6 | excellent | m003 | nursing | medicines-administration-system | 34 | 49 | 49 |
| 99.4 | excellent | m004 | nursing | dressings-and-pressure-damage | 39 | 52 | 53 |
| 99.9 | excellent | m016 | dermatology | describing-a-skin-lesion | 29 | 46 | 40 |
| 100.0 | excellent | m006 | pharmacology | pharmacokinetics-four-processes | 23 | 73 | 57 |
| 100.0 | excellent | m007 | pharmacology | pharmacodynamics-agonists-and-antagonists | 23 | 71 | 45 |
| 100.0 | excellent | m011 | general-practice | the-undifferentiated-presentation | 24 | 60 | 23 |
| 100.0 | excellent | m013 | general-practice | screening-and-its-harms | 26 | 55 | 35 |
| 100.0 | excellent | m021 | endocrinology | two-mechanisms-type-1-type-2 | 25 | 69 | 56 |
| 100.0 | excellent | m031 | emergency | primary-survey-ordering | 29 | 62 | 73 |
| 100.0 | excellent | m033 | emergency | what-triage-optimises | 24 | 58 | 43 |
