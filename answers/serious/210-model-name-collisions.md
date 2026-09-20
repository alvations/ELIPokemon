---
id: "210"
slug: model-name-collisions
style: serious
category: frontier
difficulty: intermediate
question: "Two labs shipped something called Astra in the same year. Why is model naming an engineering problem?"
tags: [reproducibility, model-ids, versioning, evaluation, provenance]
---

# A name is not an identifier

In 2026, **Project Astra** is a Google DeepMind research prototype — real-time camera and voice,
spatial understanding, screen sharing — whose capabilities ship inside Gemini Live. **GPT-6
Astra** is an OpenAI model released on 3 September 2026. Same word, two organisations, one year,
and nothing in common but the marketing department's taste in Latin.

It is not an isolated case. Upstage's **Solar** line and the **Sol** tier of GPT-5.6 are
unrelated. A **Luna** tier exists; a "Lunar" model does not, and the mistake is easy to make. The
brief that produced this arc of the dataset contained exactly that error, plus "Astra" used as
though it named one thing. That is the failure mode, observed in the wild, in a single sentence.

## Why this is engineering and not pedantry

```
   WHAT PEOPLE WRITE DOWN          WHAT ACTUALLY DETERMINES THE RESULT
   ──────────────────────          ───────────────────────────────────
   "Astra"                    ──►  org + product line + version
   "the latest model"         ──►  the pinned snapshot ID
   "GPT-5.6"                  ──►  which tier: Sol, Terra or Luna?
   "we used Claude"           ──►  claude-opus-5? claude-fable-5-1?
   "temperature default"      ──►  effort level, thinking mode, tools
   "evaluated in September"   ──►  harness version, prompt template

   An eval result reported against the left column cannot be
   reproduced, cannot be compared, and cannot be defended.
```

Three concrete hazards follow.

**Aliases move; snapshots do not.** A convenience alias that resolves to "whatever is current"
will silently re-point under you, and your regression baseline becomes a comparison between two
different models with the same label. Anthropic's current IDs are pinned snapshots even when
they carry no date — `claude-opus-5` is not a moving pointer — but that is a property of a
particular versioning scheme, not a law. Read the versioning docs of whatever you are pinning.

**The model you requested is not always the model that answered.** Fallback routing, capacity
pressure and policy declines can all cause a different model to serve a request. Log the
**served** model from the response, not the one in your config. An eval that records intent
rather than outcome is recording fiction.

**Tier names collapse into family names in writing.** "GPT-5.6 scored X" is meaningless when
Sol, Terra and Luna differ by an order of magnitude in price and materially in capability. Most
second-hand benchmark reporting commits this error, which is one reason aggregate comparisons
disagree with each other so often.

## The minimum provenance record

For any number you intend to cite or act on: **organisation, product, version, exact API model
ID, date of the run, every inference setting** (effort, thinking mode, temperature, tools
available), **harness and prompt-template version**, and the **served** model ID from the
response. Seven fields. It fits in a row of a table, and without it the number is an anecdote.

## What an interviewer is listening for

That you treat model identity as data with a schema, not as prose. The strongest answers reach
straight for the served-versus-requested distinction, because that is the one that has actually
corrupted somebody's dashboard, and mention that a name collision across two organisations makes
a literature search unreliable — which matters the moment anyone tries to cite a result.

## Where this stands, September 2026

Both Astras are real and current as of September 2026. Names churn faster than anything else in
this field, so the specific collision will be replaced by another one. The discipline — record
identifiers, not names — will not be.
