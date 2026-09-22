---
id: "261"
slug: beam-search-and-mbr-decoding
style: serious
category: optimization
difficulty: advanced
question: "Beam search is still standard in machine translation and unused in open-ended generation. What exactly is the difference?"
tags: [beam-search, mbr, likelihood, degeneration, machine-translation]
---

# The mode is not the answer

Beam search is not a style of writing. It is an approximate search for the **mode** of
`p(y | x)` — the single most probable output sequence. Everything about where it survives and
where it died follows from one question: *is the mode a good answer?* Question 035 gives the
mechanism and the standard story. This one is about the part that story gets wrong, which is that
the mode is bad **in translation too** — and that the field's response was not to go back to
sampling but to change the decision rule.

## The beam search curse

The embarrassing result is old and reproducible: **widening the beam finds higher-probability
translations that score worse**. Koehn and Knowles listed it among the six challenges of NMT in
2017; quality peaks around beam 4–5 and degrades from there. Then Stahlberg and Byrne ran *exact*
search ([1908.10090](https://arxiv.org/abs/1908.10090)) and found what is at the bottom of that
slope: for a standard NMT model, **the global mode is the empty sequence** in over half of the
sentences tested.

```
   quality                                   model probability of the found output
     ▲                                         ▲
     │      ●───●                              │                       ●
     │    ●        ●                           │                 ●
     │  ●              ●                       │           ●
     │ ●                   ●                   │     ●
     │                          ●              │ ●
     └──┬───┬───┬───┬────┬────┬────▶           └──┬───┬───┬───┬────┬────┬──▶
        1   2   4   8   50  exact  beam           1   2   4   8   50  exact

   Search gets strictly BETTER at its job and the output gets worse.
   The beam is not an approximation error. It is the only thing hiding the mode.
```

Read that carefully, because it inverts the usual framing. Beam search works in MT partly
*because it is a bad search*. A beam of five is too narrow to find the empty string.

## Length normalisation is a patch, and it tells you where the bug is

Every token contributes a negative log-probability, so cumulative score is monotonically
decreasing in length and the argmax is systematically short. Standard practice divides by
`|y|^α`, `α ≈ 0.6–1.0`, often with a coverage penalty alongside it. The tell is that `α` has to be
**tuned per language pair and per model**. A correction term that needs re-fitting whenever the
data changes is not fixing the search. It is compensating for an objective that was never the
thing you wanted to maximise.

## What degenerate repetition actually is

Not a training defect and not a beam artefact — an **attractor of the argmax operator**. Once a
span has repeated once, the context now contains evidence that this text is the kind of text that
repeats, so the model's probability of repeating it again *rises*. The loop is self-reinforcing:
each iteration raises the probability of the next. Greedy and beam decoding follow that gradient
exactly and never leave. Sampling escapes because it has a positive probability of stepping off
the loop at every step, which is the entire reason nucleus sampling was proposed.

The other half of the picture is Holtzman et al.'s surprisal analysis: human text has fairly high
and highly **variable** per-token surprisal; maximum-likelihood text has uniformly low surprisal.
Text that never surprises reads as flat, hedged and generic — the register people recognise
instantly and cannot name. Preference-tuned chat models loop far less, because RLHF moves mass off
the loop, but they still degenerate at low temperature over long outputs, which is where most
production loops come from.

## Why translation and speech kept it

* **Low conditional entropy.** Given the source, the set of good outputs is small and highly
  overlapping. The mode is at least *near* a good answer, which is not true when the prompt is
  "write me a story".
* **Short outputs.** Length bias is bounded and correctable when outputs are a sentence long.
* **A trustworthy scoring function exists.** You can rank candidates against the source.
* **Speech adds an external constraint.** ASR beams run against acoustic evidence and often a
  separate language model, so the search is constrained by something outside the model's own
  preferences.

## What replaced MAP in translation: minimum Bayes risk

MBR changes the **decision rule**, not the search. Draw `N` candidates by sampling, then pick the
candidate with the highest expected utility against all the others:

```
   ŷ = argmax over candidates c of   (1/N) Σ over samples s of   utility(c, s)

   beam search  : "which output does the model think is most likely?"
   MBR          : "which output does the model's distribution most AGREE with?"
```

With a neural utility — COMET or BLEURT rather than BLEU — MBR beats beam search on human
evaluation, and it does so without ever asking for the mode. Eikema and Aziz's framing is the one
to remember: the model can be a *good fit to the data distribution* and MAP can still be a *bad
decision rule*. Two separate claims that beam search conflates. The costs are real: `N` samples
plus `O(N²)` utility calls, which is why efficiency work (candidate pruning, low-rank completion
of the utility matrix, epsilon-sampling as a better candidate generator) is a live research line
rather than a footnote.

And the LLM world reinvented it without the name. **Best-of-N with a reward model** is MBR with a
learned utility. **Self-consistency** (question 050) is MBR with an exact-match utility over final
answers — sample many chains, return the answer the samples agree on. If you can explain
self-consistency as MBR, you have understood both.

## Where beam search still belongs in LLM serving

Grammar-constrained search where you must *find* a legal sequence (question 262), short structured
fields, speech, and any task with one right answer and a scorer you trust. Not chat.

## What an interviewer digs into next

* Why does a wider beam make translation worse?
* What is the global mode of an NMT model, and why does nobody see it?
* Why does length normalisation need per-pair tuning, and what does that tell you?
* Explain self-consistency as MBR.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing**. Resolve every identifier before you cite it.

## Where this stands, September 2026

All of the above is working knowledge of the MT and decoding literature and should be treated as
coverage; resolve the papers before quoting a number. Coverage from this session's searching
suggests the split is holding: MBR with neural utilities is the research standard in MT while beam
remains the practical default in speech, and production systems trade off by how much sampling
budget they can afford. What is durable is the distinction, not the leaderboard — **a model is a
distribution, and choosing an output from it is a separate decision with its own loss function.**
