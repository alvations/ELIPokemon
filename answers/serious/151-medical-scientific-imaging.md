---
id: "151"
slug: medical-scientific-imaging
style: serious
category: multimodal
difficulty: advanced
question: "What makes medical and scientific imaging different from natural-image vision?"
tags: [medical-imaging, shortcut-learning, calibration, abstention, distribution-shift, sensitivity]
---

# Medical and scientific imaging

Everything from questions 117-128 assumes natural images: photographs, roughly centred subjects, a
web-scale pretraining distribution that matches. Medical and scientific imaging violates all of
that, and the consequences of being wrong are different in kind.

## What actually differs

* **The pretraining distribution does not contain this.** A CT slice, an electron micrograph, a
  histopathology tile and a sky survey look nothing like ImageNet or LAION. Transfer from natural
  images still helps — surprisingly, low-level features are general — but far less than usual, and
  domain-specific pretraining beats it.
* **The findings are tiny and the images are enormous.** A whole-slide pathology image is gigapixel;
  a lesion may be a few hundred pixels. Downsampling to 336px destroys the finding entirely
  (question 121). Tiling with a whole-slide context path is mandatory, not an optimisation.
* **Data is 3D or 4D.** CT and MRI are volumes; echocardiography and fMRI add time. Treating slices
  independently discards the structure a radiologist actually uses.
* **Labels are noisy and contested.** Inter-rater agreement between expert radiologists on many
  tasks is well below 100%. Your "ground truth" is one or more expert opinions, and a model that
  agrees with the label 95% of the time in a task where experts agree with each other 85% of the
  time has learned the labelling process, not the disease.
* **Extreme class imbalance.** Prevalence may be under 1%. Accuracy is a useless metric; a model
  predicting "normal" always scores 99%.

## Shortcut learning is the defining failure

Models learn whatever predicts the label most cheaply, and in medical data that is frequently not
the pathology.

```
   sick patients were scanned at the specialist hospital  ─┐
                                                           ├─► the model learns SCANNER
   healthy controls were scanned at the community clinic  ─┘

   published results: excellent
   deployed at a third site: no better than chance
```

Documented shortcuts include scanner manufacturer, image acquisition settings, patient positioning,
laterality markers, chest drains that indicate the patient was already treated, and burnt-in text.
This is the single most common reason published medical AI results do not replicate.

**The defences are procedural**, not architectural: external validation on data from sites not in
training, stratified performance reporting by site and scanner, saliency inspection by a clinician
(who will spot "it is looking at the marker" instantly), and deliberate ablation — mask the
suspected shortcut and see whether performance survives.

## Evaluation is not accuracy

* **Sensitivity and specificity at a stated operating point**, plus AUROC for ranking and
  **AUPRC** when prevalence is low (AUROC flatters rare-positive tasks).
* **Calibration**, not just discrimination. A predicted probability that will inform a clinical
  decision must mean what it says; report ECE and reliability curves.
* **Abstention.** A model that says "I cannot tell, escalate this" is more useful than one that
  guesses. Measure accuracy on the retained set *and* the referral rate together — accuracy bought
  by abstaining on everything hard is not a gain.
* **Subgroup performance** by age, sex, ethnicity, comorbidity and site. An aggregate number that
  hides a failing subgroup is not a safety case.
* **Prospective validation.** Retrospective performance on curated data systematically overstates
  deployed performance. Regulators require this for a reason.

## The deployment context

These systems are regulated (FDA, CE/MDR), which changes the engineering: a locked model version,
documented training data provenance, change control, and a clinical evaluation plan. "We will
continuously fine-tune on production data" is a compliance problem, not just a technical choice.

And the target is almost never autonomy. It is **triage and second reading** — flagging studies for
priority, or catching what a tired reader missed. Designing for a human reader changes what matters:
the interface, the false-positive burden, and whether the model can explain where it is looking.

## What an interviewer digs into next

* Why does high agreement with labels not mean high accuracy?
* Give three plausible shortcuts and how you would test for each.
* Why AUPRC rather than AUROC at low prevalence?
* Why is abstention a feature, and how do you evaluate it honestly?
