---
id: "237"
slug: shipping-open-weights-on-device
style: serious
category: open-weights
difficulty: intermediate
question: "You want to ship an open-weight model inside a phone application. What does the memory envelope really look like, and what does an Apache-2.0 licence let you do that a custom one does not?"
tags: [on-device, quantisation, apache-2, licensing, memory]
---

# Budget three things, not one, and read the licence for what it obliges you to *ship*

The engineering question and the legal question have the same shape: people quote one number
(the parameter count, "it's open") when the thing that binds is a set of three or four. For
memory, the three are resident weights, the KV cache at your real context length, and the
offloadable tables. For the licence, the operative parts of Apache 2.0 are the patent grant,
the notice obligation, and the trademark carve-out — not the word "permissive".

## The memory envelope

Taking Gemma 4 E4B, whose config I read first-hand (question 233 works the parameter split out):

```
   E4B — 7.52 B raw, 4.67 B that must be resident

   precision      download    resident weights   offloadable PLE table
   ───────────    ────────    ────────────────   ─────────────────────
   BF16           15.04 GB        9.34 GB              5.64 GB
   int4            3.76 GB        2.34 GB              1.41 GB
   (E2B, int4)     2.33 GB        1.14 GB              1.18 GB

   then the cache, which nobody budgets for and which scales with the user:

   context     local layers (windowed at 512)   global layers (4, full)    total
   ────────    ──────────────────────────────   ───────────────────────    ─────
     8,192            20.97 MB                       134.2 MB            155 MB
    32,768            20.97 MB                       536.9 MB            558 MB
   131,072            20.97 MB                         2.15 GB          2.17 GB

   ┌─ an honest int4 E4B phone budget at an 8K context ────────────────┐
   │   resident weights            2.34 GB                             │
   │   KV cache                    0.16 GB                             │
   │   vision tower + activations  ~0.15 GB                            │
   │                              ─────────                            │
   │   in fast memory              ~2.65 GB   ← the number that decides│
   │   plus on flash               ~1.41 GB   ← the number that doesn't│
   │   plus app bundle             3.76 GB    ← the number your users  │
   │                                            actually feel          │
   └───────────────────────────────────────────────────────────────────┘
```

Three observations that survive the specific model. The **cache is the term that grows with
usage** — weights are a constant, context is a variable, and a long conversation is what takes you
over the edge, not the model. The **download is not the footprint**: 3.76 GB of bundle against
2.65 GB resident, and it is the bundle a user sees in the app store. And the **sliding window
flattens the local contribution to a constant** — 20.97 MB whether the conversation is 8K or 128K
— which is the on-device payoff of the architecture in question 234, stated in megabytes.

## Quantisation: which kind, not whether

On a phone it is int4 or nothing, so the question is how you got there. Post-training
quantisation calibrates on a sample after the fact; **quantisation-aware training** simulates the
rounding during training so the weights settle somewhere the rounding does not hurt. Google ships
QAT checkpoints for Gemma 4 in several shapes — an unquantised QAT checkpoint you quantise
yourself, a Q4\_0 GGUF, a mobile format, and a 4-bit-weight/16-bit-activation compressed-tensors
build. Reported memory reductions against BF16 run roughly 60–66% on the larger dense
checkpoints and noticeably less on E4B, which is what you would expect: a large share of E4B is
embedding and per-layer-embedding tables, and those do not shrink the same way the blocks do.
Treat those percentages as coverage; measure your own.

Two rules that hold regardless. **Quantise the blocks, be careful with the tables** — embeddings
and the PLE table are looked up rather than multiplied, so precision loss there shows up as
token-specific weirdness rather than a uniform quality dip. And **quantise the KV cache
separately and deliberately**; an 8-bit cache roughly halves the biggest variable term above, and
it is a different decision from weight precision with a different quality profile.

## What Apache 2.0 actually gives you

Assume the weights carry Apache 2.0 rather than a bespoke model licence. Four things change for
someone shipping them inside an application:

1. **You get an express patent grant (§3), with teeth attached.** Contributors licence their
   patent claims to you. If you then sue anyone alleging the work infringes a patent, your patent
   licence terminates. A custom model licence frequently grants copyright permission and says
   nothing about patents, which leaves your lawyers with an unresolved question.
2. **Your obligations on redistribution are mechanical (§4), and they are shipping obligations.**
   Include the licence text, keep the copyright/patent/attribution notices, mark files you
   changed, and reproduce the `NOTICE` file if one exists. That means the licence text goes into
   your app's acknowledgements screen. It is not copyleft: your fine-tune, your wrapper and your
   product may be closed, and you may sublicense.
3. **There is no acceptable-use policy to propagate.** This is the practical difference from the
   custom terms earlier Gemma releases shipped under, which carried a prohibited-use policy the
   licensor could update and which you had to pass to every downstream user. Under Apache there
   is no field-of-use restriction and no downstream conduct term you have to police in a contract
   you did not write.
4. **You get no trademark rights (§6).** You may ship the weights; you may not brand your product
   with the model's name or imply endorsement. Ship it, describe it accurately in your model
   documentation, and do not put the mark on the icon.

And what it does **not** do, because this is where teams get hurt. It says nothing about the
training data or about anyone else's rights in it. It makes no claim about who owns the model's
outputs. It disclaims all warranties (§7) and limits liability (§8), so every downstream
consequence is yours. And it does not touch regulation: a permissive licence is not a compliance
posture, and obligations that attach to *deploying* a model attach to you whatever the copyright
terms say.

## What an interviewer is listening for

That you answer the memory question with a sum, not a parameter count, and that the KV term is in
your sum with a context length attached. Then, on licensing, that you go straight to patents,
notice and trademark rather than saying "it's permissive". The strongest answers close the loop
between the two halves: the reason the licence matters at all is that you are putting the weights
on someone else's device, which is redistribution, which is the exact act §4 attaches conditions
to.

## Where this stands, September 2026

The parameter splits and layer configuration behind the memory table are **primary** — read from
`google-deepmind/gemma` — and the byte figures are my arithmetic over them, not quotes. The
Apache 2.0 obligations are **primary** in a narrower sense than it may look: I read the Apache 2.0
text in that repository's `LICENSE`, which covers the *code*. The **weights'** licence I could not
read first-hand, because `huggingface.co` and `ai.google.dev` are blocked from this environment;
multiple independent outlets report Gemma 4's weights as Apache 2.0, replacing the custom Gemma
Terms of Use used by earlier generations, and that is **coverage**. Do not take a licence claim
from a third party, including this one — open the `LICENSE` file in the repository you actually
downloaded, for the exact checkpoint you actually shipped. The QAT formats and the reported
reduction percentages are coverage too. The arithmetic and the four licence points transfer.
