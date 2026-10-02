# Pokémon-ness ledger — medical domain

How much each Pokémon answer leans on **named** Pokémon entities rather than generic
furniture. Same deterministic scorer as the machine-learning domain, same vocabulary, so
the two are comparable and a vocabulary fix moves both.

**The mandated plain-prose sections are excluded from scoring** — `Where the metaphor
stops`, `The human stakes, said plainly`, `Sources` and `Scope and safety`. They are
required to contain no analogy, so scoring them would penalise an answer for complying.

Regenerate with `python3 scripts/medical/score.py --write`.

**80 answers · mean 88.6 · median 89.0 · min 62.6 · max 100.0**

| score | band | id | specialty | answer | distinct | named | generic |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 62.6 | adequate | m022 | endocrinology | insulin-as-a-control-problem | 12 | 28 | 67 |
| 63.3 | adequate | m025 | endocrinology | ketoacidosis-and-the-hyperosmolar-state | 11 | 28 | 50 |
| 69.6 | strong | m018 | dermatology | assessing-skin-of-colour | 13 | 32 | 20 |
| 73.4 | strong | m024 | endocrinology | why-the-complications-differ | 14 | 30 | 49 |
| 76.0 | strong | m010 | pharmacology | adverse-drug-reactions | 15 | 32 | 49 |
| 76.1 | strong | m054 | dermatology | drug-eruptions-and-the-emergencies | 18 | 21 | 26 |
| 76.5 | strong | m029 | oncology | response-assessment-and-surrogates | 20 | 31 | 53 |
| 77.6 | strong | m051 | dermatology | eczema-and-the-barrier | 14 | 40 | 28 |
| 77.7 | strong | m038 | nursing | indwelling-devices-and-infection | 17 | 22 | 49 |
| 78.9 | strong | m035 | emergency | first-aid-for-untrained-bystanders | 14 | 28 | 20 |
| 80.3 | excellent | m032 | emergency | why-protocols-exist | 24 | 34 | 88 |
| 80.4 | excellent | m026 | oncology | staging-against-grading | 20 | 30 | 59 |
| 80.6 | excellent | m037 | nursing | recognising-sepsis | 19 | 29 | 60 |
| 81.6 | excellent | m019 | dermatology | topical-therapy-and-quantity | 18 | 30 | 21 |
| 82.0 | excellent | m039 | nursing | nutrition-and-swallowing | 20 | 27 | 36 |
| 83.1 | excellent | m002 | nursing | handover-and-escalation | 19 | 31 | 72 |
| 83.3 | excellent | m053 | dermatology | acne-mechanism-and-sequence | 24 | 34 | 33 |
| 83.7 | excellent | m040 | nursing | falls-risk-multifactorial | 25 | 29 | 52 |
| 84.1 | excellent | m005 | nursing | fluid-balance-charting | 20 | 27 | 54 |
| 84.2 | excellent | m046 | general-practice | chronic-disease-review | 23 | 41 | 79 |
| 84.3 | excellent | m014 | general-practice | polypharmacy-and-deprescribing | 20 | 31 | 53 |
| 84.4 | excellent | m073 | nursing | documentation-and-pertinent-negatives | 18 | 29 | 30 |
| 85.0 | excellent | m065 | oncology | randomisation-against-registries | 23 | 56 | 61 |
| 85.0 | excellent | m069 | emergency | supportive-care-and-the-antidote-exception | 34 | 44 | 28 |
| 85.1 | excellent | m028 | oncology | why-toxicity-is-predictable | 21 | 51 | 45 |
| 85.3 | excellent | m027 | oncology | how-systemic-therapies-differ | 27 | 60 | 40 |
| 85.4 | excellent | m001 | nursing | early-warning-scores | 24 | 35 | 64 |
| 85.5 | excellent | m082 | general-practice | access-and-demand | 19 | 30 | 21 |
| 85.8 | excellent | m052 | dermatology | psoriasis-as-systemic-disease | 25 | 38 | 29 |
| 86.0 | excellent | m062 | oncology | radiotherapy-and-fractionation | 24 | 67 | 58 |
| 86.1 | excellent | m074 | nursing | shift-work-fatigue-and-handover | 20 | 39 | 34 |
| 86.3 | excellent | m023 | endocrinology | glycation-marker-and-continuous-monitoring | 35 | 47 | 50 |
| 86.3 | excellent | m063 | oncology | what-a-surgical-margin-means | 20 | 57 | 41 |
| 86.7 | excellent | m020 | dermatology | dermoscopy-in-principle | 22 | 35 | 42 |
| 87.1 | excellent | m075 | nursing | isolation-precautions-by-route | 28 | 41 | 44 |
| 87.4 | excellent | m083 | general-practice | shared-decision-making | 18 | 34 | 44 |
| 88.1 | excellent | m061 | oncology | how-a-cancer-spreads | 22 | 52 | 20 |
| 88.2 | excellent | m055 | dermatology | leg-ulcers-and-vascular-assessment | 32 | 53 | 44 |
| 88.3 | excellent | m030 | oncology | screening-and-overdiagnosis | 26 | 59 | 15 |
| 88.7 | excellent | m036 | nursing | infection-prevention-hand-hygiene | 21 | 37 | 41 |
| 89.0 | excellent | m012 | general-practice | red-flags-and-safety-netting | 15 | 46 | 21 |
| 89.0 | excellent | m057 | endocrinology | adrenal-insufficiency | 19 | 48 | 43 |
| 90.2 | excellent | m047 | general-practice | multimorbidity-and-guidelines | 26 | 44 | 52 |
| 90.5 | excellent | m060 | endocrinology | the-reproductive-axis-as-an-oscillator | 20 | 49 | 36 |
| 90.5 | excellent | m064 | oncology | tumour-markers-and-screening | 28 | 75 | 54 |
| 90.7 | excellent | m081 | general-practice | referral-thresholds-and-gatekeeping | 18 | 50 | 46 |
| 91.2 | excellent | m015 | general-practice | continuity-of-care | 32 | 42 | 72 |
| 91.2 | excellent | m084 | general-practice | overdiagnosis-in-primary-care | 27 | 49 | 27 |
| 91.3 | excellent | m009 | pharmacology | drug-interactions-mechanisms | 27 | 52 | 63 |
| 91.4 | excellent | m041 | pharmacology | therapeutic-drug-monitoring | 43 | 54 | 94 |
| 91.6 | excellent | m085 | general-practice | the-prevention-paradox | 16 | 44 | 26 |
| 91.8 | excellent | m034 | emergency | compensation-and-the-sick-patient | 20 | 37 | 34 |
| 92.1 | excellent | m045 | pharmacology | antimicrobial-stewardship | 27 | 53 | 56 |
| 92.9 | excellent | m043 | pharmacology | adherence-and-regimen-design | 18 | 49 | 59 |
| 93.1 | excellent | m066 | emergency | shock-categories-by-mechanism | 23 | 43 | 49 |
| 93.6 | excellent | m058 | endocrinology | cortisol-excess-and-the-shape-of-the-tests | 22 | 60 | 47 |
| 93.7 | excellent | m048 | general-practice | the-consultation-and-premature-closure | 24 | 56 | 52 |
| 93.8 | excellent | m049 | general-practice | antibiotics-under-uncertainty | 28 | 51 | 32 |
| 94.4 | excellent | m070 | emergency | handover-and-what-crosses-the-boundary | 26 | 52 | 39 |
| 95.1 | excellent | m056 | endocrinology | thyroid-axis-and-its-counterintuitive-tests | 21 | 64 | 44 |
| 95.6 | excellent | m008 | pharmacology | therapeutic-index | 20 | 48 | 52 |
| 96.2 | excellent | m059 | endocrinology | calcium-and-the-parathyroid-loop | 29 | 64 | 42 |
| 96.5 | excellent | m017 | dermatology | distribution-and-configuration | 22 | 43 | 22 |
| 96.8 | excellent | m044 | pharmacology | formulation-and-route | 34 | 58 | 47 |
| 97.1 | excellent | m068 | emergency | mechanism-of-injury-as-a-prior | 30 | 55 | 31 |
| 97.2 | excellent | m050 | general-practice | health-inequality-as-mechanism | 38 | 60 | 67 |
| 97.4 | excellent | m042 | pharmacology | renal-and-hepatic-impairment | 22 | 53 | 59 |
| 97.6 | excellent | m003 | nursing | medicines-administration-system | 34 | 49 | 49 |
| 99.4 | excellent | m004 | nursing | dressings-and-pressure-damage | 39 | 52 | 53 |
| 99.9 | excellent | m016 | dermatology | describing-a-skin-lesion | 29 | 46 | 40 |
| 100.0 | excellent | m006 | pharmacology | pharmacokinetics-four-processes | 23 | 73 | 57 |
| 100.0 | excellent | m007 | pharmacology | pharmacodynamics-agonists-and-antagonists | 23 | 71 | 45 |
| 100.0 | excellent | m011 | general-practice | the-undifferentiated-presentation | 24 | 60 | 23 |
| 100.0 | excellent | m013 | general-practice | screening-and-its-harms | 26 | 55 | 35 |
| 100.0 | excellent | m021 | endocrinology | two-mechanisms-type-1-type-2 | 25 | 69 | 56 |
| 100.0 | excellent | m031 | emergency | primary-survey-ordering | 31 | 65 | 73 |
| 100.0 | excellent | m033 | emergency | what-triage-optimises | 24 | 58 | 43 |
| 100.0 | excellent | m067 | emergency | what-speech-proves-about-the-airway | 48 | 58 | 47 |
| 100.0 | excellent | m071 | nursing | wound-healing-phases | 28 | 48 | 35 |
| 100.0 | excellent | m072 | nursing | bed-rest-and-deconditioning | 33 | 58 | 30 |
