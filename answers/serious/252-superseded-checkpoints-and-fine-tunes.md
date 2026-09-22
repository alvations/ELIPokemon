---
id: "252"
slug: superseded-checkpoints-and-fine-tunes
style: serious
category: open-weights
difficulty: intermediate
question: "The open checkpoint you deployed and fine-tuned has just been superseded. What actually changes?"
tags: [open-weights, fine-tuning, lifecycle, pinning, reproducibility]
---

# Nothing in your object store changed. Everything around it did.

The answer to lead with: **"superseded" is a statement about the vendor's attention, not about
your artefact.** The bytes you downloaded are the same bytes. The licence you accepted at that
revision still grants what it granted — an Apache 2.0 grant on a copy you already hold is not
revocable by a later release. Your fine-tune still runs. Nobody has taken anything from you.

What changed is the entire environment the artefact sits in, and the honest list is longer than
people expect.

```
   UNCHANGED (yours)                    CHANGED (everybody else's)
   ──────────────────────────────       ────────────────────────────────────────
   the weights at your revision    │    what "current" means in every comparison
   the tokenizer and config        │    which checkpoint the recipes target
   the LICENSE you accepted        │    which quantised re-uploads get maintained
   your adapter, your eval set     │    whether the hosted twin still behaves so
   your serving stack, if pinned   │    what upstream will fix for you
   ──────────────────────────────  │    the URL the documentation lives at
                                   │
              only the left column is in your storage
```

## The six things that actually move

**1. Your baseline stops being the reference.** Every comparison anyone runs — inside your team
and outside it — is now against the new checkpoint. That is not a technical problem; it is a
*reporting* problem, and it arrives as "why are we 14 points behind" from someone who has not
asked whether the index measures your task (question 250).

**2. The support surface drifts.** Framework versions move forward, recipes and cookbook pages
retarget, kernels and quantisation kits get tuned for the new shape. Your pinned stack keeps
working exactly as long as you keep it pinned — and pinning a serving framework indefinitely means
you own its CVEs. That is the real cost of standing still, and it is an operations cost, not a
quality one.

**3. The community artefact layer migrates.** Fourth-party GGUF and AWQ builds, LoRA collections,
prompt libraries, evaluation harness configs: all of it follows the new checkpoint within weeks.
Your 4-bit build was probably somebody's hobby, and it is now somebody's *old* hobby.

**4. Your fine-tune is re-priced, not destroyed.** Two separate questions, and people conflate
them:

- *Does my adapter still work?* Yes, on the base it was trained against — and **only** on that
  base. A LoRA is a delta over specific weight matrices; it does not transfer to a differently
  post-trained checkpoint, even one with an identical architecture. Migrating means **re-running
  the recipe**, not copying tensors.
- *Do I still need it?* Often not. A generation whose entire gain is post-training is a generation
  that may have absorbed the behaviour you were fine-tuning for. The correct first experiment on a
  new base is the **un-fine-tuned** base against your frozen eval, before you spend a GPU-week.

**5. The hosted twin moves under you.** If any part of your stack calls an endpoint name rather
than a revision, that name now resolves to different behaviour and nobody told you (questions 210,
219).

**6. The documentation moves, literally.** The Qwen case is a good concrete instance. The
repository that holds the open series has been **renamed forward at each generation**: fetching
the README under `QwenLM/Qwen3-Next`, `QwenLM/Qwen3.5`, `QwenLM/Qwen3.6` and `QwenLM/Qwen3.8`
returns the same byte-identical file (one MD5 across four names — checked here). The page
describing Qwen 3.6 is now served from a URL named after 3.8, and it describes 3.6 in the past
tense. Meanwhile Qwen3.6-27B itself was never withdrawn. **Superseded and unavailable are
different words**, and only one of them was true.

## What this means you should have done, and should do now

1. **Mirror everything at the revision hash, into storage you control:** weights, tokenizer,
   config, chat template, and the `LICENSE` file *as it read at that revision*. A licence can
   change between revisions of the same repository (question 222), and a hub can gate or remove a
   repository.
2. **Keep the recipe, not just the artefact.** Training data and its provenance, the split, the
   hyperparameters, the seed, the base revision, and the eval set. **A fine-tune is a reproducible
   procedure; the adapter is merely its output.** Teams that kept only the adapter discover at
   migration time that they cannot reproduce their own model.
3. **Keep a frozen, task-level eval.** It turns "should we move" from a quarter of debate into a
   day of measurement (question 251).
4. **Set a review date at deploy time, not a retirement date.** Retirement dates get ignored; a
   calendared review with a named owner gets done.
5. **Decide deliberately whether you are pinning.** Good reasons: a validated or regulated system,
   a contractual eval baseline, an air-gap, a fixed cost ceiling, a long-running experiment whose
   comparability depends on the model not moving. Bad reason, and the common one: **nobody owns
   the upgrade.** Deliberate stasis is a legitimate engineering position. Drift is not.

## What an interviewer is listening for

That your first move is to separate what is in your storage from what is in someone else's, and
that you know an already-downloaded permissive grant is not rescinded by a later release. Then
that you treat the fine-tune as a procedure rather than a possession. The strongest answers make
the uncomfortable point unprompted: when a release's entire gain is post-training, the most likely
outcome of evaluating the new base is that **your fine-tune has been made redundant** — and
finding that out costs one evaluation run, while assuming it has not costs a GPU-week and a
migration.

## Where this stands, September 2026

The repository rename chain — four names, one byte-identical README, MD5-compared, with
`QwenLM/Qwen3.7` returning 404 — was checked first-hand in this environment, as was the continued
presence of Qwen3.6-27B in the lab's own dated release list. **Coverage, not primary:** the
per-model licence fields, the continued availability of the older checkpoints on the model hubs,
and the relative capability of the 3.6 and 3.8 checkpoints, since `huggingface.co` and `qwen.ai`
are blocked from this environment and the model cards are the authority. **Nothing here is legal
advice** — "a grant already accepted is not revoked by a later release" is the ordinary reading of
a permissive licence and not a substitute for reading yours. The specific checkpoints will be
superseded again before this is read. The distinction between superseded and unavailable will not
move.
