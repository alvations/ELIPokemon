---
id: "164"
slug: participatory-mt
style: serious
category: translation
difficulty: intermediate
question: "What does community-driven language technology look like, and why does it work?"
tags: [participatory-research, masakhane, common-voice, benefit-sharing, sustainability, evaluation]
---

# Participatory and community-driven language technology

The default research model is: an outside team picks a language, obtains data, trains a model,
publishes, and leaves. For well-resourced languages this is fine — the community of speakers is
enormous and unaffected. For everything else it produces work that is unusable by the people it
describes, and it is why so many "we support 200 languages" claims dissolve on contact.

The participatory model inverts who decides. **Masakhane** (African NLP), **Common Voice**
(crowdsourced speech), and the various community-led corpus efforts are the reference points, and
their results are not merely more ethical — they are **better**, for concrete reasons.

## Why it produces better systems

* **The evaluation is real.** Speakers catch failures no metric surfaces: text that is grammatical
  and nobody would say, a register that is wrong for the context, a term that is technically
  correct and offensive in use.
* **The task selection is right.** Outside teams build news translation because news corpora exist.
  Communities ask for health information, legal documents, education material, and keyboards —
  the things question 130's evaluation section warns you are probably not building.
* **The data is cleaner at source.** Native-speaker collection avoids the mislabelled,
  machine-translated and scraped-from-a-different-language material that poisons crawled corpora
  (question 136).
* **Coverage of varieties.** Communities know which varieties exist and which the standard corpus
  silently excludes (question 162).

## The failure mode it exists to prevent

"Helicopter research": arrive, extract, publish, depart. Its signatures are recognisable —

```
   the paper reports:  "we collected 50k sentences in <language>"
   and does not say:   who collected them
                       whether they were paid
                       whether the community agreed to the licence
                       whether the model or data is available to them
                       what happens when the funding ends
```

If a project cannot answer those five questions, the number of languages in its title is not the
achievement it appears to be.

## What to actually commit to

* **Co-authorship, not acknowledgement.** People who contributed the data and the linguistic
  judgement are contributors.
* **Payment** at a fair local rate, not "volunteering for the good of science".
* **A licence agreed in advance**, which may exclude commercial use or model training. Accept that
  answer if it is given.
* **Return the artefacts** in usable form — the model, the data, the tooling, documentation in the
  language.
* **Say what happens when the grant ends.** Most projects end. A community that knows the timeline
  can plan around it; one that discovers it when the server goes down cannot.
* **Local infrastructure.** A model requiring a data-centre GPU is not deployable where it is
  needed. Distilled and quantised models (questions 029, 030) are not a compromise here, they are
  the requirement.

## Evaluation, specifically

Automatic metrics for these languages are weakest exactly where you need them (questions 129, 132).
Budget for **human evaluation by speakers** from the start, structure it as paid work, and report
who evaluated. A COMET score for a language whose COMET model saw almost no data is a number, not
evidence.

## What an interviewer digs into next

* Give three concrete reasons participatory data collection produces better models, not just fairer ones.
* What are the five questions a paper claiming N languages should answer?
* Why does task selection differ when the community chooses?
* Why is model size an ethics question in this context?
