# Pokémon-ness ledger — medical domain

How much each Pokémon answer leans on **named** Pokémon entities rather than generic
furniture. Same deterministic scorer as the machine-learning domain, same vocabulary, so
the two are comparable and a vocabulary fix moves both.

**The mandated plain-prose sections are excluded from scoring** — `Where the metaphor
stops`, `The human stakes, said plainly`, `Sources` and `Scope and safety`. They are
required to contain no analogy, so scoring them would penalise an answer for complying.

Regenerate with `python3 scripts/medical/score.py --write`.

**110 answers · mean 88.6 · median 90.3 · min 57.4 · max 100.0**

| score | band | id | specialty | answer | distinct | named | generic |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 57.4 | adequate | m107 | nursing | oxygen-as-a-prescribed-drug | 11 | 17 | 16 |
| 61.0 | adequate | m106 | nursing | continence-and-its-mechanisms | 12 | 19 | 21 |
| 62.6 | adequate | m022 | endocrinology | insulin-as-a-control-problem | 12 | 28 | 67 |
| 63.3 | adequate | m025 | endocrinology | ketoacidosis-and-the-hyperosmolar-state | 11 | 28 | 50 |
| 69.6 | strong | m018 | dermatology | assessing-skin-of-colour | 13 | 32 | 20 |
| 74.0 | strong | m110 | nursing | discharge-planning-as-a-clinical-act | 16 | 30 | 23 |
| 76.0 | strong | m010 | pharmacology | adverse-drug-reactions | 15 | 32 | 49 |
| 76.1 | strong | m054 | dermatology | drug-eruptions-and-the-emergencies | 18 | 21 | 26 |
| 76.5 | strong | m029 | oncology | response-assessment-and-surrogates | 20 | 31 | 53 |
| 76.6 | strong | m024 | endocrinology | why-the-complications-differ | 15 | 31 | 49 |
| 76.7 | strong | m090 | dermatology | urticaria-and-angioedema | 17 | 33 | 32 |
| 77.6 | strong | m051 | dermatology | eczema-and-the-barrier | 14 | 40 | 28 |
| 77.7 | strong | m038 | nursing | indwelling-devices-and-infection | 17 | 22 | 49 |
| 78.9 | strong | m035 | emergency | first-aid-for-untrained-bystanders | 14 | 28 | 20 |
| 79.1 | strong | m088 | dermatology | photoprotection-and-cumulative-dose | 24 | 35 | 33 |
| 80.0 | excellent | m098 | oncology | the-multidisciplinary-meeting | 21 | 45 | 52 |
| 80.1 | excellent | m087 | dermatology | hair-and-nail-as-a-timeline | 27 | 37 | 30 |
| 80.3 | excellent | m032 | emergency | why-protocols-exist | 24 | 34 | 88 |
| 80.4 | excellent | m026 | oncology | staging-against-grading | 20 | 30 | 59 |
| 80.6 | excellent | m037 | nursing | recognising-sepsis | 19 | 29 | 60 |
| 81.0 | excellent | m108 | nursing | venous-access-and-infusion | 28 | 39 | 24 |
| 81.0 | excellent | m109 | nursing | continuous-versus-intermittent-observation | 37 | 43 | 40 |
| 81.6 | excellent | m019 | dermatology | topical-therapy-and-quantity | 18 | 30 | 21 |
| 82.0 | excellent | m039 | nursing | nutrition-and-swallowing | 20 | 27 | 36 |
| 82.7 | excellent | m089 | dermatology | blistering-and-the-level-of-the-split | 27 | 45 | 35 |
| 82.7 | excellent | m099 | oncology | performance-status | 18 | 51 | 48 |
| 82.8 | excellent | m097 | oncology | tumour-heterogeneity-and-one-biopsy | 18 | 53 | 55 |
| 83.1 | excellent | m002 | nursing | handover-and-escalation | 19 | 31 | 72 |
| 83.3 | excellent | m053 | dermatology | acne-mechanism-and-sequence | 24 | 34 | 33 |
| 84.1 | excellent | m005 | nursing | fluid-balance-charting | 20 | 27 | 54 |
| 84.2 | excellent | m046 | general-practice | chronic-disease-review | 23 | 41 | 79 |
| 84.3 | excellent | m014 | general-practice | polypharmacy-and-deprescribing | 20 | 31 | 53 |
| 84.4 | excellent | m040 | nursing | falls-risk-multifactorial | 26 | 30 | 52 |
| 85.1 | excellent | m073 | nursing | documentation-and-pertinent-negatives | 19 | 30 | 30 |
| 85.3 | excellent | m027 | oncology | how-systemic-therapies-differ | 27 | 60 | 40 |
| 85.4 | excellent | m001 | nursing | early-warning-scores | 24 | 35 | 64 |
| 85.4 | excellent | m028 | oncology | why-toxicity-is-predictable | 22 | 52 | 45 |
| 85.4 | excellent | m065 | oncology | randomisation-against-registries | 24 | 57 | 61 |
| 85.4 | excellent | m069 | emergency | supportive-care-and-the-antidote-exception | 35 | 45 | 28 |
| 85.8 | excellent | m052 | dermatology | psoriasis-as-systemic-disease | 25 | 38 | 29 |
| 85.9 | excellent | m063 | oncology | what-a-surgical-margin-means | 19 | 56 | 41 |
| 86.0 | excellent | m062 | oncology | radiotherapy-and-fractionation | 24 | 67 | 58 |
| 86.7 | excellent | m020 | dermatology | dermoscopy-in-principle | 22 | 35 | 42 |
| 87.0 | excellent | m086 | dermatology | skin-infections-and-the-scraping | 17 | 45 | 37 |
| 87.2 | excellent | m023 | endocrinology | glycation-marker-and-continuous-monitoring | 36 | 49 | 50 |
| 87.4 | excellent | m083 | general-practice | shared-decision-making | 18 | 34 | 44 |
| 87.7 | excellent | m075 | nursing | isolation-precautions-by-route | 29 | 42 | 44 |
| 88.1 | excellent | m061 | oncology | how-a-cancer-spreads | 22 | 52 | 20 |
| 88.2 | excellent | m055 | dermatology | leg-ulcers-and-vascular-assessment | 32 | 53 | 44 |
| 88.8 | excellent | m074 | nursing | shift-work-fatigue-and-handover | 21 | 44 | 34 |
| 89.0 | excellent | m012 | general-practice | red-flags-and-safety-netting | 15 | 46 | 21 |
| 89.0 | excellent | m057 | endocrinology | adrenal-insufficiency | 19 | 48 | 43 |
| 89.3 | excellent | m036 | nursing | infection-prevention-hand-hygiene | 22 | 38 | 41 |
| 89.6 | excellent | m082 | general-practice | access-and-demand | 24 | 36 | 21 |
| 90.2 | excellent | m047 | general-practice | multimorbidity-and-guidelines | 26 | 44 | 52 |
| 90.3 | excellent | m030 | oncology | screening-and-overdiagnosis | 28 | 64 | 15 |
| 90.5 | excellent | m060 | endocrinology | the-reproductive-axis-as-an-oscillator | 20 | 49 | 36 |
| 90.9 | excellent | m064 | oncology | tumour-markers-and-screening | 28 | 76 | 54 |
| 91.2 | excellent | m081 | general-practice | referral-thresholds-and-gatekeeping | 19 | 51 | 46 |
| 91.3 | excellent | m009 | pharmacology | drug-interactions-mechanisms | 27 | 52 | 63 |
| 91.4 | excellent | m041 | pharmacology | therapeutic-drug-monitoring | 43 | 54 | 94 |
| 91.8 | excellent | m034 | emergency | compensation-and-the-sick-patient | 20 | 37 | 34 |
| 91.8 | excellent | m100 | oncology | biomarker-driven-treatment-selection | 29 | 79 | 47 |
| 91.9 | excellent | m015 | general-practice | continuity-of-care | 33 | 43 | 72 |
| 92.0 | excellent | m105 | emergency | the-social-presentation | 19 | 43 | 43 |
| 92.2 | excellent | m079 | pharmacology | biologics-against-small-molecules | 28 | 69 | 30 |
| 92.6 | excellent | m045 | pharmacology | antimicrobial-stewardship | 28 | 54 | 56 |
| 92.6 | excellent | m076 | pharmacology | tolerance-dependence-and-withdrawal | 16 | 53 | 21 |
| 92.9 | excellent | m043 | pharmacology | adherence-and-regimen-design | 18 | 49 | 59 |
| 93.0 | excellent | m094 | endocrinology | the-growth-hormone-axis-as-a-pulse-train | 37 | 83 | 42 |
| 93.1 | excellent | m066 | emergency | shock-categories-by-mechanism | 23 | 43 | 49 |
| 93.4 | excellent | m080 | pharmacology | placebo-and-nocebo-as-real-effects | 23 | 66 | 41 |
| 93.5 | excellent | m078 | pharmacology | scaling-a-dose-to-a-body | 18 | 65 | 29 |
| 93.7 | excellent | m048 | general-practice | the-consultation-and-premature-closure | 24 | 56 | 52 |
| 93.8 | excellent | m049 | general-practice | antibiotics-under-uncertainty | 28 | 51 | 32 |
| 94.3 | excellent | m092 | endocrinology | sodium-as-a-statement-about-water | 24 | 76 | 51 |
| 94.5 | excellent | m058 | endocrinology | cortisol-excess-and-the-shape-of-the-tests | 23 | 62 | 47 |
| 95.0 | excellent | m070 | emergency | handover-and-what-crosses-the-boundary | 27 | 53 | 39 |
| 95.0 | excellent | m084 | general-practice | overdiagnosis-in-primary-care | 30 | 56 | 27 |
| 95.1 | excellent | m056 | endocrinology | thyroid-axis-and-its-counterintuitive-tests | 21 | 64 | 44 |
| 95.5 | excellent | m096 | oncology | targeted-therapy-and-resistance | 34 | 98 | 83 |
| 95.6 | excellent | m008 | pharmacology | therapeutic-index | 20 | 48 | 52 |
| 95.7 | excellent | m095 | endocrinology | the-adrenal-incidentaloma | 29 | 69 | 21 |
| 96.2 | excellent | m059 | endocrinology | calcium-and-the-parathyroid-loop | 29 | 64 | 42 |
| 96.5 | excellent | m017 | dermatology | distribution-and-configuration | 22 | 43 | 22 |
| 96.7 | excellent | m091 | endocrinology | pituitary-mass-effect-and-sequential-failure | 30 | 79 | 38 |
| 96.7 | excellent | m104 | emergency | imaging-and-decision-rules | 24 | 65 | 36 |
| 96.8 | excellent | m044 | pharmacology | formulation-and-route | 34 | 58 | 47 |
| 97.2 | excellent | m050 | general-practice | health-inequality-as-mechanism | 38 | 60 | 67 |
| 97.4 | excellent | m042 | pharmacology | renal-and-hepatic-impairment | 22 | 53 | 59 |
| 97.5 | excellent | m101 | emergency | chest-pain-ordered-by-danger | 42 | 55 | 38 |
| 97.6 | excellent | m003 | nursing | medicines-administration-system | 34 | 49 | 49 |
| 97.6 | excellent | m102 | emergency | breathlessness-splits-by-system | 21 | 56 | 37 |
| 98.3 | excellent | m068 | emergency | mechanism-of-injury-as-a-prior | 31 | 57 | 31 |
| 98.6 | excellent | m093 | endocrinology | bone-remodelling-and-its-fast-markers | 34 | 82 | 57 |
| 99.0 | excellent | m085 | general-practice | the-prevention-paradox | 20 | 50 | 26 |
| 99.4 | excellent | m004 | nursing | dressings-and-pressure-damage | 39 | 52 | 53 |
| 99.9 | excellent | m016 | dermatology | describing-a-skin-lesion | 29 | 46 | 40 |
| 100.0 | excellent | m006 | pharmacology | pharmacokinetics-four-processes | 23 | 73 | 57 |
| 100.0 | excellent | m007 | pharmacology | pharmacodynamics-agonists-and-antagonists | 23 | 71 | 45 |
| 100.0 | excellent | m011 | general-practice | the-undifferentiated-presentation | 25 | 61 | 23 |
| 100.0 | excellent | m013 | general-practice | screening-and-its-harms | 27 | 56 | 35 |
| 100.0 | excellent | m021 | endocrinology | two-mechanisms-type-1-type-2 | 25 | 69 | 56 |
| 100.0 | excellent | m031 | emergency | primary-survey-ordering | 31 | 65 | 73 |
| 100.0 | excellent | m033 | emergency | what-triage-optimises | 24 | 58 | 43 |
| 100.0 | excellent | m067 | emergency | what-speech-proves-about-the-airway | 50 | 60 | 47 |
| 100.0 | excellent | m071 | nursing | wound-healing-phases | 29 | 49 | 35 |
| 100.0 | excellent | m072 | nursing | bed-rest-and-deconditioning | 33 | 58 | 30 |
| 100.0 | excellent | m077 | pharmacology | pharmacogenomics-and-the-population-dose | 42 | 83 | 23 |
| 100.0 | excellent | m103 | emergency | splinting-is-treatment | 37 | 81 | 47 |
