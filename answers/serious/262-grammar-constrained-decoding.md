---
id: "262"
slug: grammar-constrained-decoding
style: serious
category: optimization
difficulty: advanced
question: "How does grammar-constrained decoding work at the logit level, and what does it cost when the grammar fights the model?"
tags: [constrained-decoding, grammar, structured-output, json-schema, masking]
---

# A mask over the vocabulary, recomputed every step

Grammar-constrained decoding keeps an automaton alongside the decoder. At each step it asks which
vocabulary tokens could legally continue the output under the grammar, sets every other logit to
`-inf`, renormalises, and samples from what is left. The structural guarantee is absolute and
cheap to state: the output parses. Everything difficult lives in three places — making the mask
fast, reconciling a grammar written over characters with a vocabulary written over byte pairs, and
deciding what to do when the legal set and the model's preferences disagree.

```
  step t                                       vocabulary (|V| ~ 130k)
  ────────                       ┌──────────────────────────────────────────────┐
  automaton state:  IN_STRING    │  "   ,   }   ]   the   {   :   42   \n  ...  │
        │                        └──────────────────────────────────────────────┘
        ▼                                         │
  ┌───────────────┐   token mask   ┌──────────────▼──────────────────────────────┐
  │ legal-token   │──────────────► │  ok  X   X   X   ok   X   X   ok   X   ...  │
  │ index (FSM /  │                └──────────────┬──────────────────────────────┘
  │ pushdown)     │                               ▼
  └───────────────┘                  logits + mask -> -inf, renormalise, sample
        ▲                                          │
        └─────────── advance on the chosen token ◄─┘

  The mask is applied BEFORE the sampling parameters of question 260 see the logits.
  Truncation then operates on a distribution that has already been rewritten.
```

## Regular, context-free, and why the difference shows up

A regex or a flat JSON schema compiles to a **finite-state machine**: the legal-token set is a
function of the current state alone. Anything with nesting — balanced brackets, arbitrary JSON
depth, a real programming-language grammar — needs a **pushdown automaton**, because you must
remember how deep you are. That is the practical dividing line between "a regex over the output"
and "a grammar", and it is why engines carry a persistent stack per sequence rather than a single
integer state.

**Making it fast** is the whole engineering story.
[Willard and Louf (2023)](https://arxiv.org/abs/2307.09702), the work behind Outlines, precomputes
an index from automaton state to legal token set, turning a per-step scan of the vocabulary into a
lookup. XGrammar ([2411.15100](https://arxiv.org/abs/2411.15100)) splits the vocabulary into
tokens whose legality is *context-independent* for a given automaton state — precomputable and
cached — and the small remainder that must be checked at runtime, then overlaps mask construction
with the forward pass. Its README claims **100% structural correctness** and **near-zero
overhead** on JSON, and lists it as the default structured-generation backend for `vLLM`,
`SGLang`, `TensorRT-LLM` and `MLC-LLM`, with integrations into TensorRT-LLM (January 2025) and
OpenVINO GenAI (September 2025), and an XGrammar-2 release in May 2026. All of that is primary:
read from the repository README in this session.

## The tokenizer mismatch, which is where the bugs live

Grammars are defined over characters. Models emit sub-word tokens. The two do not line up.

* A single token can **straddle a grammar boundary** — `",` or `":"` or `}}` are ordinary BPE
  tokens — so legality has to be evaluated over the token's whole expansion, not one character at
  a time.
* One string has many tokenisations. The mask admits all of them, but the model's probability mass
  sits on the **canonical** one. A prompt that ends mid-token forces the model onto a tokenisation
  it has essentially never seen; this is the **token healing** problem, and the fix is to back the
  prompt up to a token boundary and re-mask the first step.
* Engines differ on whether they mask over token strings or over byte sequences, which is why the
  same schema can behave differently on two servers.

## What it actually costs in quality

1. **Renormalisation over a thin slice.** If the legal set holds one percent of the model's mass,
   you are sampling from a conditional distribution that nothing ever trained or calibrated. The
   more your schema disagrees with how the model would naturally write, the thinner the slice.
2. **Greedy commitment with no backtracking.** This is the big one. The mask is a *local* filter
   enforcing a *global* constraint. A perfectly legal prefix can lead into a region where every
   legal continuation is something the model considers absurd, and because the mask is applied per
   step and most engines never backtrack, there is no way out. Constrained *beam* search or
   backtracking fixes it and costs `k×` compute and cache — which is one of the few places beam
   search still earns its keep (question 261).
3. **You may have masked away the reasoning.** Tam et al.'s *Let Me Speak Freely?*
   ([2408.02442](https://arxiv.org/abs/2408.02442)) reported that format restrictions degrade
   reasoning; the rebuttals argued the gap came from prompt confounds rather than from the
   constraint itself. The synthesis that survives both, and the one to say in an interview: the
   variable that matters is **where in the schema the thinking is allowed to happen**. A schema
   whose first required field is `answer` has deleted chain-of-thought by construction. Put a free
   `reasoning` string first and most of the reported degradation goes away.
4. **Well-typed is still not true.** The mask constrains the codomain of the function, not the
   content. Question 203 is the whole argument; nothing here changes it. You have removed parse
   errors and invented enum values, and you have not touched the expensive failure.

## Practical guidance

* **Prefer trained-plus-constrained over constrained alone.** A model post-trained on the schema
  format puts mass inside the legal set, so the mask rarely has to fight. That is what a vendor
  structured-output mode is: a grammar *and* a model that expects it.
* Keep schemas shallow, put reasoning first, and prefer field names and enum labels the model
  would write anyway. A constraint that agrees with the distribution costs nothing.
* **Set the penalties of question 260 to neutral.** A repetition penalty and a JSON grammar are
  close to incompatible: the grammar requires `"`, `,` and `}` over and over.
* Cache compiled grammars by schema hash. Per-request schemas otherwise pay automaton compilation
  on every call, and that cost does not show up in a token-count benchmark.
* Check what your engine silently drops. Regex `pattern`, `oneOf`, unbounded recursion and
  arbitrary-precision numbers are common gaps, and a dropped constraint is a guarantee you no
  longer have.

## What an interviewer digs into next

* Why does a grammar need a stack and a regex does not?
* How do you build the mask without scanning 130,000 tokens every step?
* What is token healing, and what goes wrong without it?
* Why can constrained decoding paint itself into a corner, and what would fix it?

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing**. Resolve every identifier before you cite it.

## Where this stands, September 2026

Primary: the XGrammar README, read first-hand — the correctness and overhead claims, the engine
integrations and their dates, and the XGrammar-2 release. Coverage: the papers, and the whole
quality-degradation debate, which is a live disagreement rather than a settled result; read both
sides before repeating either. The durable part is the trade itself. **A mask buys you a
guarantee about form at the price of sampling from a slice of the distribution, and the size of
that price is exactly how much the constraint and the model disagree.**
