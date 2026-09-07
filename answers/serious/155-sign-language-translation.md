---
id: "155"
slug: sign-language-translation
style: serious
category: translation
difficulty: advanced
question: "Why is sign language translation not just video captioning?"
tags: [sign-language, glosses, non-manual-markers, avatars, deaf-community, low-resource]
---

# Sign language translation

The first thing to get right is that sign languages are **natural languages with their own
grammar**, not visual encodings of spoken ones. American Sign Language is not English on the hands;
it is unrelated to English and closer to French Sign Language. British and American Sign Language
are mutually unintelligible despite both countries speaking English.

That means SL translation is **translation between languages**, and everything in questions 129-152
applies — plus a set of problems unique to a language that is produced in three dimensions,
simultaneously.

## Why it is not video captioning

```
   SPOKEN LANGUAGE          one channel, one thing at a time, left to right

   SIGN LANGUAGE            hands: the lexical sign
                            face:  grammar — question, negation, topic, intensity
                            body:  role shift (who is speaking now)
                            space: entities placed in space, referred back to by pointing
                            ALL AT ONCE
```

* **Non-manual markers are grammar, not expression.** Raised eyebrows mark a yes/no question;
  lowered brows mark a wh-question; a headshake negates. A system that tracks hands only is missing
  the equivalent of word order and negation, and will confidently output the opposite meaning.
* **Signing space is referential.** A signer places a person at a location and points back to it
  later. This is the pronoun system, and it is spatial — a flat sequence model has no natural way to
  represent it.
* **Classifiers and depiction** describe shape and movement iconically, with no fixed word-level
  equivalent.
* **Simultaneity.** Two hands can carry two pieces of information at once. Text is linear.

## The gloss problem

Most datasets annotate with **glosses** — spoken-language words in capitals standing for signs. They
are a research convenience and a lossy one: they discard non-manual markers, flatten simultaneity,
and impose the spoken language's segmentation. Gloss-based pipelines (video → gloss → text) were the
standard and are being replaced by **gloss-free** end-to-end approaches, partly because glossing is
expensive expert labour and partly because the intermediate representation throws away the grammar.

## Data is the binding constraint

Public corpora are small — thousands of sentences where spoken-language MT has hundreds of millions
— narrow in domain (weather bulletins, news), and often shot in studio conditions with one signer,
front-lit, plain background. Real signing is conversational, at angles, with occlusion, and varies
by signer, region and age.

**Consent and community involvement are not optional here.** Sign language data is video of
identifiable people, from a community with a well-documented history of having technology designed
about it rather than with it. The field's own guidance is emphatic: involve Deaf researchers and
signers from the start, and treat "we scraped it" as disqualifying.

## Signing avatars, and why the community is sceptical

Generating signing output usually means an animated avatar. The recurring complaint is not that they
are imperfect but that they are **unusable**: robotic, missing non-manual markers entirely, and
frequently deployed as a cheaper substitute for human interpreters rather than as an addition.
Evaluate with **Deaf signers**, not with automatic metrics or hearing observers, and be honest about
whether the system is a supplement or a cost-cutting replacement.

## Evaluation

BLEU on glosses is the field's most criticised habit — it measures agreement with a lossy
intermediate representation. Prefer translation quality against text references (with the same
caveats as question 129), comprehension testing with Deaf participants, and reporting on **who
signed and who evaluated**.

## What an interviewer digs into next

* Why are glosses a lossy representation?
* What breaks if a model tracks hands but not face?
* Why is the referential use of signing space hard for sequence models?
* What would you insist on before starting a sign language project at all?
