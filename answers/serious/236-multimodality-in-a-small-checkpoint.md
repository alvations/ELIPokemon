---
id: "236"
slug: multimodality-in-a-small-checkpoint
style: serious
category: open-weights
difficulty: advanced
question: "What has to give when you put vision and audio into a checkpoint that has to fit on one card?"
tags: [multimodal, vision-encoder, token-budget, on-device, gemma]
---

# The parameters are cheap. The context is not, and the sliding window is where it hurts

Bolting a vision tower onto a small language model costs you about 1–3% of the parameters, which
is nothing. What it actually costs is **tokens**, and in an architecture where five layers in six
can only see a 512-token window, a single image at the default budget occupies more than half of
everything those layers are allowed to look at. That is the trade nobody puts on the slide, and it
falls straight out of two numbers in the config.

## The numbers, from the reference implementation

From `gemma/gm/nn/gemma4/` in [`google-deepmind/gemma`](https://github.com/google-deepmind/gemma):

```
   the towers

     E2B / E4B vision   d_model 768, 16 layers, 12 heads, FFW 3072   ≈ 0.11 B params
     31B / 26B-A4B      d_model 1152, 27 layers, 16 heads, FFW 4304  ≈ 0.41 B params
     E2B / E4B audio    Conformer, 12 layers, width 1024, left ctx 13, right ctx 0
     31B / 26B-A4B      — no audio encoder in the config at all —

     vision tower as a share of the model:  E4B 0.11 / 4.67 = 2.4%
                                            31B 0.41 / 30.7 = 1.3%

   the pipeline, and where the loss is

     image (any aspect ratio)
       │  patch_size 16
       ▼
     up to 2,520 patches ──────────────────── padded to 2,520 regardless of size
       │  pooling_kernel_size 3  →  9 patches collapse into 1
       ▼
     280 soft tokens             ← the default; configurable 70 / 140 / 280 / 560 / 1120
       │
       ▼
     merged into the text stream

   what 280 tokens costs against each budget in the model

     against the 131,072-token context  :  0.21%    ~468 images would fill it
     against E4B's 512-token window     :  54.7%    █████████████·············
     against the 31B's 1,024 window     :  27.3%    ███████···················

     at the 560 budget on E4B, and 1,120 on the 31B, ONE IMAGE IS LARGER THAN
     THE ENTIRE LOCAL WINDOW. No sliding layer ever sees the whole picture.
```

## What gives, in order of how much it hurts

**1. Spatial resolution, before the LLM ever sees it.** `pooling_kernel_size=3` means nine
patches become one soft token. Eight ninths of the spatial detail is pooled away between the
tower and the backbone. That is why small-text OCR, dense tables and fine chart labels are the
first things that fail on small VLMs, and why the token budget is exposed as a dial — you raise
it when the task is reading and lower it when the task is describing.

**2. Local context, which is the expensive one.** The numbers above are the whole argument. The
default 280-token image eats 55% of every sliding layer's field of view on E4B. Two images and
the surrounding text is gone from those layers entirely; anything tying the images together has
to travel through the seven global layers, which is exactly the path question 234 describes as
the lossy one. Multimodality and sliding-window attention are two separately sensible decisions
that interact badly, and the interaction is invisible in either one's description.

**3. Latency that does not scale with the input.** A public engineering report against a
Gemma 4 serving stack measures the tower at a flat cost: every image is padded to 2,520 patches,
so a 192×192 thumbnail and a 768×768 photograph cost the same — 3.7× the cost of the 144-patch
case — and trimming to a 576-patch ladder would recover about 3.5× for small images. On a phone,
a fixed per-image cost you cannot avoid by sending a smaller picture is a product decision, not a
tuning detail.

**4. Causality, differently at different sizes.** `use_bidirectional_attention='vision'` in the
31B and 26B-A4B configs lets image tokens attend to each other in both directions *in the sliding
layers only*, staying causal in the global ones. E2B and E4B set it to `None` — purely causal
everywhere. A picture has no reading order, so left-to-right masking over image tokens is a real
handicap, and the two smallest checkpoints wear it. The small model does not get a smaller version
of the big model's treatment; it gets a different treatment.

**5. Text quality, through the training mixture.** This one is not in any config and it is the
one that matters most. Pretraining tokens spent on image–text pairs are not spent on text, and in
a 4B-effective model there is no slack. You cannot read this off an architecture diagram; you read
it off an ablation the vendor may not have published.

## The inversion worth noticing

Audio is in `Gemma4_E2B` and `Gemma4_E4B` and **not** in `Gemma4_31B` or `Gemma4_26B_A4B`. The
capability ladder does not run smallest-to-largest; it runs by deployment target. The Conformer
has `atten_left_context=13` and `atten_right_context=0` — strictly causal, bounded lookback, no
lookahead — which is a streaming design, for a microphone on a device. The server checkpoints do
not carry it because the product it serves is not that product. If you are choosing a checkpoint
by "bigger is more capable", this is where that heuristic quietly fails.

## What an interviewer is listening for

That your first question is "how many tokens per image", not "how many parameters in the
encoder". Then that you check that number against the *local* attention window rather than the
advertised context length — that is the step that separates someone who has served a VLM from
someone who has read about one. The strongest answers raise the training-mixture cost unprompted
and admit it is the hardest of the five to verify.

## Where this stands, September 2026

The tower dimensions, `patch_size`, `pooling_kernel_size`, the 280 default output length, the
`use_bidirectional_attention` settings, the Conformer's context bounds, and which checkpoints
carry an audio encoder were all read first-hand from `google-deepmind/gemma` — **primary**. The
parameter estimates and the percentage arithmetic are mine, not quoted. The 70/140/280/560/1120
budget ladder is **coverage**, though the 2,520-patch figure it implies is confirmed independently
by the serving-stack report. The latency ratios come from one public issue thread on one
accelerator, read first-hand: a **primary reading of one team's measurement**, not a general
result. Model cards on `huggingface.co` and the documentation on `ai.google.dev` are the
authority and both are blocked from this environment. Token budgets and pooling factors are the
parts most likely to change; the tokens-against-the-local-window argument is the part that
transfers.
