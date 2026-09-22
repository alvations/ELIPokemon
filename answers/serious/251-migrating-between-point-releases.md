---
id: "251"
slug: migrating-between-point-releases
style: serious
category: open-weights
difficulty: advanced
question: "A point release lands on the same architecture with a much better index score. How do you decide whether to migrate?"
tags: [qwen, regression-testing, migration, evaluation, serving]
---

# The upgrade that changes no numbers you can see is the one that needs the most testing

The lead I would give: **an index score is a reason to open an evaluation, never a reason to
migrate.** And a point release on an unchanged architecture is the most dangerous shape of upgrade
there is, precisely because it looks free. The serving command is byte-identical. The memory
footprint is identical. The config diff is almost empty. Nothing in the change request says
"behaviour change", so nobody budgets a regression suite — and behaviour is the *only* thing that
changed.

Qwen3.8-27B against Qwen3.6-27B is the clean case. Same reported layer count, hidden size, context
and vocabulary; roughly 38 to 52 on a third-party intelligence index; and a vLLM registry that
does not contain a Qwen 3.6 or Qwen 3.8 class at all, because there is no new architecture to
carry (question 250). Every point of that gain is data and post-training. So is every regression.

## What moves when only the post-training moves

```
   what you can diff                       what you cannot
   ─────────────────────────────────       ──────────────────────────────────────
   layers, hidden size, vocab size    │    behaviour on your long tail
   max positions, tensor shapes       │    how long it thinks before answering
   the serve command                  │    when it decides to call a tool
   GPU memory at rest                 │    whether it stops where it used to stop
   ─────────────────────────────────  │    what a rejected parameter string does
        ALL UNCHANGED                 │         ALL OF IT CHANGED
                                      │
                      the change request sees the left column only
```

Four failures from the lab's own issue tracker make the point concretely, and they are the shapes
your suite has to be able to catch:

- **A language slice collapsing.** Issue #238 reports Qwen3.8-27B producing systematically
  corrupted Tamil agglutinative suffixes on medical text that Qwen3.6-27B did not: **13–27%
  acceptance against 93%** on a 60-item batch, reproduced across INT4, AWQ-INT4 and NVFP4, which
  is why the reporter attributes it to the weights rather than to quantisation.
- **Stop behaviour changing.** Issue #231: Qwen3.8-27B "unexpectedly truncates output".
- **A contract breaking under a flag you already set.** Issue #236: tool calling becomes
  unreliable with long prompts when `enable_thinking=false`.
- **A control string that is now an error.** Issue #217 records the chat template's own text:
  `Unexpected reasoning effort high. Supported types are xhigh (default), medium, and low.` A
  harness sending `high` fails deterministically on its first request (question 220).

None of those is visible in an aggregate index, and one of them — the last — is not a quality
regression at all. It is an integration break, and it is the cheapest of the four to catch.

## The decision, as a gate rather than a vote

Migration is justified by three measurements and an asymmetry. State the asymmetry first because
it sets the default: **not migrating costs you a slowly widening quality gap; migrating badly
costs you a fast, concentrated failure in one slice.** Slow and diffuse against fast and sharp. So
the default is stay, and the burden of proof is on the move.

```
   GATE 1  integration     control strings, chat template, tool-call parser,
                           tokenizer id, stop tokens          → hours, binary
   GATE 2  contract        JSON validity, schema conformance, truncation rate,
                           refusal rate                       → a day, thresholded
   GATE 3  task quality    YOUR frozen prompt set, scored per slice, never
                           pooled                             → the real work
   GATE 4  cost & latency  tokens spent at YOUR effort level, p50 and p99,
                           truncation rate reported alongside → the surprise
   GATE 5  shadow          mirrored production traffic, outputs diffed, no
                           user sees it                       → a week
   GATE 6  canary          small share, automatic rollback, old revision still
                           pinned and servable                → until it is boring
```

Gate 3 is where teams cheat and where the Tamil case would have been caught. **Score per slice and
never pool.** A per-language, per-document-type, per-customer-segment breakdown turns a 93→20
collapse on one slice into a red cell; an aggregate turns it into a rounding error the +14 pays
for. Your slice list should come from your traffic, not from the benchmark's taxonomy.

Gate 4 is where the "free" upgrade stops being free. Same architecture means the same FLOPs per
token — it does not mean the same *number* of tokens. A model whose default reasoning level is at
the top of its range, and which coverage reports burning tens of thousands of reasoning tokens on
trivial prompts, is a different bill at identical hardware. Report the **truncation rate** with
the quality number or the quality number is an average over two populations (question 220).

## The things people skip that are cheap

- **Freeze the prompt set before you look at the new model.** A suite curated after seeing the
  candidate's outputs is a description of the candidate.
- **Keep golden outputs and diff them**, not only the scores. Human review of 50 diffs finds
  classes of change no metric was written for.
- **Pin revisions on both sides.** A repository id is not an artefact; a revision hash is
  (question 232). Re-check the licence file at the new revision while you are there — it can
  change between revisions of the same repository (question 222).
- **Keep the old checkpoint servable for the whole canary window.** A rollback you have not
  rehearsed is a hope.
- **Re-tune prompts as a separate experiment.** Your prompts encode the *old* model's failure
  modes. Migrating and re-prompting at once makes the result uninterpretable.

## What an interviewer is listening for

That you refuse to treat a benchmark delta as a decision, and can say what evidence *would* decide
it. Then that your first gate is integration, not quality — because it is binary, cheap, and the
most common cause of a failed migration. The strongest answers state the asymmetry explicitly and
draw the right conclusion from it: on a same-architecture point release the default is to stay,
and the interesting question is what your suite would have to show to overturn that.

## Where this stands, September 2026

The four issue reports (#217, #231, #236, #238) and their numbers are read directly from the Qwen
team's own GitHub issue tracker; they are user reports on a primary venue, not vendor claims and
not independently reproduced here. The absence of a Qwen 3.6 or Qwen 3.8 model class is read
directly from vLLM's `registry.py`. **The 38-and-52 index scores, the two checkpoints'
configuration equivalence, and the reports of very long default reasoning are coverage**, because
`huggingface.co` and `qwen.ai` are blocked from this environment; the model cards are the
authority. The specific issue numbers will age immediately. The gate ladder and the asymmetry
behind it will not.
