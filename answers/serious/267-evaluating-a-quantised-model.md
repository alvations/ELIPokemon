---
id: "267"
slug: evaluating-a-quantised-model
style: serious
category: optimization
difficulty: intermediate
question: "A quantised build's perplexity moved by 0.15. Is that fine? How would you evaluate it honestly?"
tags: [quantisation, evaluation, perplexity, kl-divergence, calibration]
---

# 0.15 is a mean over 300,000 tokens. The damage is not in the mean.

That number is real and I can tell you where it comes from: Llama-3-8B on Wikitext-2 goes from
6.2332 at f16 to 6.3829 at Q4_K_M with an importance matrix. A 2.4% rise. Now look at what the
*same measurement run* reports about the *same pair of models*, token by token:

```
   Llama-3-8B, Q4_K_M against f16, per-token change in the probability
   assigned to the correct token (llama.cpp's own published scoreboard)

   mean PPL ratio      1.0282           ← the 0.15. This is the headline.
   ─────────────────────────────────────────────────────────────────────
   median Δp          −0.024 %          half of all tokens move less
   1.0%   Δp         −19.567 %          one token in a hundred
   0.1%   Δp         −56.054 %          one token in a thousand
   minimum Δp        −98.699 %          the single worst token
   ─────────────────────────────────────────────────────────────────────
   RMS Δp              5.519 %
   same top-1         91.901 %          ← ON 8% OF TOKENS THE MODEL'S
                                          FIRST CHOICE IS NOW DIFFERENT
```

A 2.4% mean and a one-in-twelve change of mind are the same file. Perplexity averaged the damage
away, because perplexity is an average and the damage is not distributed like one. **That is the
whole answer to "is 0.15 fine": 0.15 is not a measurement of the thing you care about.**

## What to measure instead, in the order I would do it

**1. Divergence from the baseline, not absolute quality.** Run the unquantised model, record its
logits, run the quantised one on the same tokens and compute KL divergence, the mean and
percentile spread of Δp, and the top-1 agreement rate. No labels needed, no benchmark to be
contaminated, and it answers the actual question — *is this still the same model* — rather than a
proxy for it. The Q4_K_M row above is KLD 0.028; Q8_0 is 0.0014; Q2_K is 0.445. Those three
numbers separate the builds in a way perplexity does not.

**2. Read the shape of the percentiles, not just their size.** If the positive and negative tails
are symmetric, quantisation is adding noise. If the negative tail is much longer than the positive
one, the model is genuinely worse. Above, the 0.1% tail is −56% against +27% on the other side:
that is damage, not noise.

**3. Task evals at your operating point, not the harness default.** Same chat template, same
sampling settings, same engine and version, same context length, same KV-cache dtype
([266](266-kv-cache-quantisation.md)). A GGUF evaluated in one runtime and served in another has
not been evaluated.

**4. The capabilities that break first, specifically.** Long-context retrieval; structured output
(JSON that must parse, tool calls whose argument names must be exact); multi-step arithmetic where
one bad intermediate ruins the chain; non-English, and especially low-resource languages;
instruction-following on unusual formats; and refusal behaviour, which can move in either
direction and which nobody thinks to re-test.

**5. Enough runs to know what noise looks like.** A two-point move on a 200-item benchmark is
inside the confidence interval of the benchmark. If you cannot state the interval, you cannot
claim the regression.

## Calibration is a leak, and it is the subtlest failure here

GPTQ fits a reconstruction on calibration data. An importance matrix is *built* from calibration
data. The convention in llama.cpp is to use Wikitext-2 for calibration — and the convention for
reporting perplexity is also Wikitext-2. **Those two conventions are in tension, and the published
scoreboard is honest enough to label the imatrix column so you can see it.**

```
   the leak, in one picture

   calibration set ──► quantiser fits scales/importance to THIS
                                    │
                                    ▼
   eval set ═══ same distribution ═══► measured damage is UNDERSTATED
   eval set ─── different domain ────► measured damage is real

   Q4_K_M  imatrix from 10M Wikitext tokens   PPL 6.383   ΔPPL 0.150
   Q4_K_M  no imatrix at all                  PPL 6.407   ΔPPL 0.175
                                              ──────────────────────
   the imatrix "bought" 0.024 PPL, measured on the domain it was fitted to.
```

And a finding that should make everyone more humble about calibration: the tool's own
documentation reports **no consistent improvement from using more calibration tokens** — runs from
1K to 10M tokens land in no reliable order. If the size of your calibration set does not matter
monotonically, you do not understand what it is doing, and neither does anyone else. Calibrate on
something that resembles your traffic, evaluate on something that does not resemble your
calibration set, and say in the release notes which was which.

## "4-bit is fine" is a claim about a model, not about a bit-width

The same scoreboard quantised Llama-2-7B and Llama-3-8B with identical recipes:

```
                        L2-7B        L3-8B
   ──────────────────────────────────────────
   q2_K PPL ratio       1.108        1.565      ← twice the damage
   q4_K_M PPL ratio     1.014        1.028
   q4_K_M same top-1    94.7 %       91.9 %
   ──────────────────────────────────────────
```

Nearly the same parameter count, nearly twice the degradation. The difference is training tokens
per parameter: a model trained far past Chinchilla-optimal has packed more into the same weights
and has less redundancy left to give away. This generalises. **A heavily-trained small model, a
distilled model, and a model that was already pruned are all poor quantisation candidates**, and
none of that is visible from the bit-width.

## Where the damage actually lives

Degradation concentrates on **rare inputs**, and your benchmark is a collection of common ones.
That is not a coincidence — it is the same fact twice. Quantisation error is largest where the
model's confidence was most finely balanced or where an outlier channel was doing unusual work,
and those are exactly the inputs that occur rarely enough that no benchmark contains many of them.
The one token in a thousand that loses 56 points of probability is not a random token; it is a
rare one.

So the honest position is: **your evaluation will systematically understate the damage, and you
should say so.** Mitigate it by sampling your own production traffic for the eval set, by
over-weighting the long tail on purpose, and by keeping the unquantised model available to diff
against when a user reports something strange.

## What an interviewer digs into next

* Perplexity moved 2%, top-1 agreement is 92%. Which of those would you put in the release note?
* How would you detect calibration leakage if you did not build the quantisation yourself?
* Why would a distilled 8B quantise worse than a 7B trained on a quarter of the tokens?
* What would you measure to catch a regression that only appears at 100K context?

## Where this stands, September 2026

Every figure in this answer is **primary**: the perplexity, KL-divergence, Δp percentile and
top-1-agreement numbers, the imatrix comparison and the Llama-2-against-Llama-3 table were all
read directly out of llama.cpp's published perplexity scoreboard, which also states its own
revision, backend and hardware. Those exact numbers belong to those exact builds and will drift
with every kernel change — do not quote them as properties of "4-bit". What transfers is the
method: measure divergence from the baseline rather than absolute quality, read the tail rather
than the mean, say which set you calibrated on, and assume the damage you can see is smaller than
the damage you have.
