---
id: "183"
slug: multimodal-accessibility
style: serious
category: multimodal
difficulty: intermediate
question: "How should multimodal models be used for accessibility?"
tags: [alt-text, audio-description, captioning, wcag, user-testing, autonomy]
---

# Accessibility is the oldest real use of this technology

Describing an image to someone who cannot see it, captioning audio for someone who cannot hear it,
and simplifying text for someone who needs it are among the most genuinely useful things a
multimodal model does. They are also the applications where getting it subtly wrong does the most
harm, because the user **cannot check the output against the source**.

That asymmetry is the entire design constraint. A sighted reader spots a hallucinated object
immediately (question 122). A blind reader has only your description, and a confident wrong
description is worse than none.

## Alt text: what actually makes it good

Automatic alt text is not "caption the image". Good alt text is **purpose-dependent**:

```
   the same photograph, three contexts:

   news article about a flood     ─► "Floodwater covering a street to car-door height,
                                      residents wading past a submerged bus stop."
   a product page for a coat      ─► "A navy waterproof coat, knee length, hood up."
   a decorative header image      ─► alt="" — announcing it is NOISE
```

Consequences for a system: it needs the surrounding context, not just the image; length should be
short by default with detail on request; and it must have a way to say **"decorative"** and a way
to say **"I cannot tell"**. Text in the image must be transcribed rather than described. Charts need
their *data*, not their appearance (question 127).

## Audio description and captioning

* **Audio description** fits into gaps in the dialogue — a length-constrained generation problem
  (question 144) with the same timing discipline as dubbing (question 154).
* **Captioning** needs speaker identification, non-speech sound ("door slams"), and accurate
  timing. WER (question 125) is the wrong metric alone: a caption that is 95% accurate but misses
  who is speaking is much less usable than the number implies.
* Both are covered by standards (WCAG) that specify requirements rather than aspirations. Know them
  before designing.

## The rules that make this responsible

* **Say when you are unsure.** "A person, possibly holding a cup" is more useful than a confident
  invention. This is the abstention argument from question 151, and here the user has no way to
  detect the failure themselves.
* **Never describe people's attributes you cannot know.** Inferring race, gender, age, disability or
  emotion from a photograph and stating it as fact is a documented harm, not a feature. Describe
  what is visible; attribute nothing.
* **Automatic description supplements human description; it does not replace it** where the content
  matters. The same argument as signing avatars in question 155, and it goes wrong the same way:
  deployed as a cost saving rather than as added coverage.
* **Test with disabled users, and pay them.** A system evaluated only by sighted engineers on
  caption metrics will pass and be unusable.
* **Do not remove the human option.** The value is in *more* access, not in replacing the accessible
  path that already worked.

## Evaluation

Caption-similarity metrics are close to irrelevant here. Measure **task success** — can the user
answer questions about the image, follow the video, find the product — plus hallucination rate
(question 122) weighted far more heavily than usual, and abstention rate. Report who evaluated.

## What an interviewer digs into next

* Why is the same image's correct alt text different on different pages?
* Why is hallucination worse in this application than elsewhere?
* What should a system never infer about a person from a photograph?
* Why are caption-similarity metrics the wrong measure here?
