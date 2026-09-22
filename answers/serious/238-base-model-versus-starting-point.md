---
id: "238"
slug: base-model-versus-starting-point
style: serious
category: open-weights
difficulty: advanced
question: "A lab ships open weights and calls them a good open-weights base for customisation. Is that a base model?"
tags: [base-model, post-training, open-weights, evaluation, model-cards]
---

# The word "base" is doing two jobs, and only one of them is a checkpoint

A **base model** is a checkpoint that finished pretraining and has had nothing done to it since:
no supervised fine-tuning, no preference optimisation, no RL, no chat template, no refusal
training. It is a next-token predictor over the pretraining distribution, and that is the whole of
it. "A good open-weights **base for customisation**" is a different sentence. It is a claim about
where a model sits in somebody's product plan, not about which rung of the training ladder the
weights came off. Thinking Machines Lab's **Inkling**, open-weighted on 15 July 2026, is the
second and not the first — and almost every mistake people make about it follows from reading it
as the first.

## What Inkling actually ships as

The lab's own pages are blocked from the environment this was written in. The reference
implementation that landed in Hugging Face `transformers` on the release date is not, and I read
it directly from `raw.githubusercontent.com`. That file is a primary artefact, and it settles the
question on its own.

The config defaults describe the large checkpoint: 66 decoder layers at hidden size 6,144; 64
query heads over 8 key/value heads at head dimension 128 on the full-attention layers; sliding
layers with 16 key/value heads and a 512-token window, laid out so that five of every six layers
are sliding and the last layer is global; 256 routed experts with **top-6 selection plus 2 shared
experts scored in the same softmax**; a learned relative-position bias instead of RoPE; a 4-wide
short convolution per block; multi-token-prediction layers; a 201,024-entry vocabulary. Coverage
puts the headline at 975B total and 41B active, a 1M-token window, ~45T pretraining tokens across
text, images, audio and video, and Apache 2.0.

None of that is the decisive part. **This is:** the documented way to call the model is
`processor.apply_chat_template(messages, ..., reasoning_effort="high")`, with system and user
roles, and `reasoning_effort` drawn from `none`, `minimal`, `low`, `medium`, `high`, `xhigh`,
`max`. Coverage describes the post-training as mid-training on synthetic data followed by
high-compute RL across synthetic and human environments, with a per-token cost that teaches the
policy to spend its budget against the requested effort. The release ships tool-call and reasoning
parsers for vLLM, and published StrongREJECT and adversarial-refusal numbers.

A base model has none of those things. A base model has no roles, no stop condition it respects,
no effort dial, and no refusal behaviour to measure. Inkling has all four. **It is a post-trained
policy that a lab is marketing as a starting point.** Both halves of that sentence are true and
they are not the same claim.

## Why the distinction decides your evaluation

```
   WHAT EXISTS                        WHAT YOU CAN HONESTLY MEASURE ON IT
   ────────────────────────────────   ──────────────────────────────────────────────────
   pretrained base                    bits-per-byte / perplexity on held-out text
   (tokens in, nothing else)          log-likelihood few-shot: MMLU, ARC, HellaSwag
        │                             next-token calibration · probing · loss curves
        │                             ──  NOT: instruction following, chat, tool use
        ▼
   mid-trained                        the above, plus long-context retrieval probes
   (synthetic data, length, mix)      ──  NOT: refusals, formats, effort control
        │
        ▼
   post-trained policy                everything a harness actually runs:
   (SFT, preference tuning, RL)       IFBench · SWE-bench · MCP Atlas · StrongREJECT
        │                             ──  AND: every one of those is now REMOVABLE
        ▼
   INKLING, as released               chat template · reasoning_effort: none … max
   975B total / 41B active            tool-call parser · published safety evals
```

Read the ladder downwards and the first error is obvious. **"It scores below the instruct-tuned
frontier on SWE-bench" is not a criticism of a base model; it is a category error.** A genuine
base model handed an agentic harness will continue your issue text with three more issue texts.
The number that comes back measures the absence of post-training, not the absence of capability.
The honest instruments for a base model are the likelihood-scored ones: bits-per-byte on held-out
text (comparable only within a tokenizer, never across one — a 201,024-entry vocabulary and a
32,000-entry one do not produce commensurable perplexities), few-shot benchmarks scored by
log-likelihood over the options rather than by parsing generated text, calibration, and the loss
curve itself.

Read it upwards and you get the error Inkling actually invites, which is the expensive one. **Its
published behaviour is a property of the RL, and fine-tuning strips RL behaviour first.** A
reported adversarial-refusal figure and a reported instruction-following figure belong to the
policy as shipped. Nothing about open weights preserves them through your SFT run. The lab's own
framing says as much — published safety results are a starting point, not a guarantee, and the
customer owns the safety of the customisation. That is not boilerplate; it is the correct reading
of what post-training is.

## The sixty-second check, on any checkpoint

1. **Is there a `chat_template` in the tokenizer config?** If yes, it is not a base model.
2. **Are there role or control tokens in the vocabulary** — system, user, assistant, thinking
   delimiters, image and audio beginning-of-span markers? Inkling has all of these.
3. **Does the documented call signature take a behaviour argument** such as `reasoning_effort`? A
   dial that changes how much the model thinks was trained in; it did not come from pretraining.
4. **Are there refusal or safety numbers in the card?** Refusal cannot be measured on a base model
   at all.
5. **Is there a `-Base`, `-pt` or `-Instruct` sibling?** Labs that ship both say so in the name.
   Inkling's published siblings are a quantised variant and a smaller model, not a base one.

Inkling answers 1–4 yes and 5 no. Qwen and Llama generations have historically shipped explicit
base and instruct pairs; question 219 is about not confusing a checkpoint ladder with an endpoint
ladder, and this is the same discipline one rung further in.

## What an interviewer is listening for

That you separate "a base model" from "a base for building on", and can say which artefact the
card is actually describing without being led to it. Strong answers name the measurement that goes
with each rung — likelihood scoring for a base model, generation harnesses for a policy. The
strongest add the asymmetry: a base model's scores are an *underestimate* of what the weights can
do, and a post-trained model's scores are an *overestimate* of what will survive your fine-tune.

## Where this stands, September 2026

The architecture and the call signature above were read first-hand from the reference
implementation and its documentation page on `raw.githubusercontent.com`; treat those as primary.
The parameter counts, the 45T-token figure, the licence, the release date and the description of
the post-training recipe are **coverage** — `thinkingmachines.ai` and `huggingface.co` are both
blocked from here, so the model card itself was not read. **The brief that commissioned this
question called Inkling a base model. It is not one**, and the check in the previous section is
how that was established rather than assumed. If a genuine `Inkling-Base` is published later, none
of the reasoning changes — only which row of the ladder the file sits on. Open the tokenizer
config for the exact checkpoint you have before you decide which instruments apply.
