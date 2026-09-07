---
id: "134"
slug: domain-adaptation-translation
style: serious
category: translation
difficulty: intermediate
question: "How do you adapt a translation system to a specific domain?"
tags: [domain-adaptation, fine-tuning, forgetting, retrieval, routing, in-domain-data]
---

# Domain adaptation in machine translation

A general system trained on web and news data will translate a clinical discharge summary
fluently and wrongly. Domain adaptation is the problem of moving quality into a narrow
distribution without destroying it everywhere else.

## What "domain" actually means

Four things vary independently, and conflating them is the most common mistake:

| Axis | Example |
| --- | --- |
| **Terminology** | "administration" = giving a drug, not an organisation |
| **Register/style** | patent prose, marketing copy, chat messages |
| **Structure** | UI strings with placeholders, subtitles with length limits, tables |
| **Topic** | the subject matter itself |

Most "domain adaptation" needs are actually terminology needs (question 133) plus a register
change, and those two have much cheaper solutions than retraining.

## The methods, cheapest first

**1. Prompting / in-context examples (LLM systems).** Put five in-domain example pairs and the
relevant glossary entries in the prompt. Zero training, immediate, and often 80% of the available
gain. The obvious first thing to try, and it is frequently skipped in favour of fine-tuning.

**2. Retrieval-augmented MT.** Retrieve the most similar previously-translated segments from a
translation memory and include them as examples. This is prompting with the examples chosen per
segment rather than fixed, and it is strictly better when you have a TM.

```
   source segment ─► retrieve top-k similar approved translations ─┐
                                                                    ├─► prompt ─► output
   glossary terms present in this segment ──────────────────────────┘
```

**3. Fine-tuning on in-domain parallel data.** The standard answer, and the one with a trap
attached — see below. LoRA (question 025) rather than full fine-tuning, in most cases: cheaper,
and you keep the base model intact so you can swap adapters per domain.

**4. Continued pretraining on in-domain monolingual target text**, then fine-tune. Useful when you
have a lot of in-domain text and almost no in-domain *parallel* data, which is the usual situation.

**5. Domain tags.** Train one model on all domains with a tag token prefixed to the source. One
model, switchable at inference, no adapter management. Works well when domains are known in
advance and reasonably distinct.

## The trap: catastrophic forgetting

Fine-tune hard on 50k medical sentence pairs and you get a system that is better on medical text
and materially worse on everything else — including on the general-language sentences *inside*
medical documents, which are most of them.

Mitigations, in order of how well they work:

* **Mix general data back in.** A 1:1 to 1:4 in-domain-to-general ratio is a reasonable starting
  point. This is the single most effective control and the most often omitted.
* **Low learning rate, few epochs.** Domain adaptation needs far less training than people give it;
  overtraining is the usual cause.
* **Adapters/LoRA** rather than full fine-tuning — the base weights are untouched by construction.
* **Regularisation toward the base model** (KL penalty, or weight averaging with the base).

## Routing, when you have several domains

Classify the incoming segment and route to the right adapter or prompt. Two cautions: the
classifier's errors become translation errors, so measure it; and a document is one domain, so
classify at document level and hold the decision, rather than letting it flip between segments.

## Evaluation

* **Always report in-domain and out-of-domain scores together.** An in-domain number alone hides
  exactly the regression you need to know about. This is the whole point.
* Build the in-domain test set from held-out *documents*, not shuffled sentences — sentences from
  the same document leak.
* Report **term accuracy** separately (question 133); most of the perceived domain gain is often
  terminology, and if so you should have used a glossary instead of a GPU.
* Have a domain expert read fifty outputs. The failure that matters in a clinical or legal domain
  is usually a specific wrong word, which no automatic metric weights correctly.

## What an interviewer digs into next

* How would you tell whether you have a terminology problem or a real domain problem?
* Why mix general data into domain fine-tuning, and at what ratio?
* Why classify domain at document level rather than per segment?
* Why must out-of-domain scores be reported alongside in-domain ones?
