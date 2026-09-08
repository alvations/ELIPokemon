---
id: "163"
slug: endangered-language-documentation
style: serious
category: translation
difficulty: advanced
question: "What can NLP actually do for endangered and under-documented languages?"
tags: [documentation, fieldwork, orthography, community-ownership, care-principles, asr]
---

# NLP for endangered languages

Roughly half the world's languages have few enough speakers that transmission to children is at
risk. NLP is frequently offered as help. Some of what is offered helps; a good deal of it does not,
and the difference is not technical sophistication.

## The data situation is categorically different

This is not question 130's low-resource setting scaled down. There may be **no parallel text at
all**, no monolingual corpus, no standard orthography, and no keyboard. What exists is often:

* field recordings, some decades old, on degrading media;
* linguists' notebooks in inconsistent transcription;
* a dictionary, sometimes a grammar sketch;
* a Bible translation, frequently the single largest text.

Transfer from a related language (question 130) may not be available: the language may be an
isolate, or its relatives may be equally undocumented.

```
   WHAT QUESTION 130 ASSUMED          WHAT IS ACTUALLY HERE
   ─────────────────────────          ─────────────────────
   monolingual target text     ►      40 hours of tape, untranscribed
   a high-resource relative    ►      an isolate, or relatives just as undocumented
   a settled orthography       ►      three competing spellings, politically loaded
   a test set                  ►      none, and no way to make one alone
   a tokenizer that copes      ►      no keyboard for the script

   so the bottleneck is not modelling. It is TRANSCRIPTION:
        1 hour of recording  ──────────────────►  ~40 hours of expert time
                                    ▲
                    this ratio is the thing to attack. Everything else is downstream.
```

## Where NLP genuinely helps

The honest list is mostly unglamorous, and it is dominated by **tools for the people doing the
documentation** rather than end-user products:

* **Forced alignment and ASR for fieldwork.** Transcription is the bottleneck in language
  documentation — the ratio of transcription time to recording time is often 40:1. Even a mediocre
  ASR system that produces a rough first pass changes what a small team can process. This is
  probably the single highest-value contribution.
* **Keyboards, fonts and input methods.** A language whose orthography cannot be typed cannot be
  used online, and that is a technical problem with a technical fix.
* **Spellcheckers and dictionaries** — used daily by actual speakers, unlike most research output.
* **Archival infrastructure**: stable formats, metadata standards, and hosting that outlives a
  grant.
* **Corpus search over existing recordings**, so a community can find "how did my grandmother say
  this".

## Where it mostly does not

Building a general MT system on a few thousand sentences produces something that neither speakers
nor learners can rely on, and its existence can be used to justify not funding human work. Ask what
the community asked for. It is rarely a chatbot.

## Orthography is a live question, not a preprocessing step

Many under-documented languages have no settled spelling; some have several competing systems tied
to different missions, regions or political positions. Choosing one for your dataset is
**intervening in that dispute**. The right move is to record which system each text uses, support
conversion between them where the community has defined it, and never silently normalise.

## The part that is not technical

This field has a documented history of extractive research: data collected from communities,
published for academic credit, and inaccessible to the people it came from. The response — the
CARE principles for Indigenous data governance, alongside FAIR — puts **collective benefit,
authority to control, responsibility and ethics** on the same footing as technical openness.

Concretely: the community decides what is collected and what is public; speakers are paid;
licensing is agreed in advance and can restrict use, including commercial and model-training use;
outputs are returned in usable form; and a project that ends when its funding ends should say so at
the start.

**"We scraped what was online" is not a dataset methodology here.** The material that exists online
is often sacred, restricted, or published without the speaker's consent in the first place.

## What an interviewer digs into next

* Why is transcription rather than translation the bottleneck?
* Why can transfer from a related language be unavailable here specifically?
* Why is choosing an orthography a political act?
* What would you agree with a community before collecting anything?
