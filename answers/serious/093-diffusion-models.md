---
id: "093"
slug: diffusion-models
style: serious
category: generative
difficulty: advanced
question: "How do diffusion models work, and how do they differ from autoregressive models?"
tags: [diffusion, ddpm, denoising, latent-diffusion, cfg, flow-matching]
---

# Diffusion models

Train a model to **reverse a gradual noising process**. Forward, you destroy an image by adding
Gaussian noise over `T` steps until it is pure noise. Backward, the model removes a little noise at a
time, turning noise into a sample.

```
   FORWARD (fixed, no learning)
   x₀ ──► x₁ ──► x₂ ──► … ──► x_T
   🖼️     🖼️🌫️   🖼️🌫️🌫️        🌫️      q(x_t|x_{t-1}) = N(√(1-β_t)x_{t-1}, β_t I)

   REVERSE (learned)
   x_T ──► … ──► x₂ ──► x₁ ──► x₀
   🌫️              🖼️🌫️  🖼️🌫️   🖼️     p_θ(x_{t-1}|x_t) — a network predicts
                                        the noise ε that was added
```

**The key trick:** you can jump to any noise level in closed form,
`x_t = √ᾱ_t x₀ + √(1−ᾱ_t) ε`, so training needs no sequential simulation. Sample a random `t`, noise
the image, and train the network to predict `ε`. The loss reduces to a plain MSE:

$$\mathcal{L} = \mathbb{E}_{t,x_0,\epsilon}\big[\|\epsilon - \epsilon_\theta(x_t, t)\|^2\big]$$

An elegant result: a complicated variational objective collapses to noise prediction.

## Why it beat GANs

* **Stable training** — one network, one regression loss. No adversarial game, no mode collapse, no
  discriminator balancing.
* **Mode coverage** — it models the full distribution rather than collapsing to a few modes.
* **Scales predictably** with data and compute.
* The cost is **slow sampling**: hundreds of network evaluations per image versus one for a GAN.

## The practical machinery

* **Latent diffusion** (Stable Diffusion) — run diffusion in a VAE's compressed latent space rather
  than pixel space. ~48× less compute, and the reason this became consumer-accessible.
* **Classifier-free guidance** — train with the conditioning randomly dropped, then at sampling time
  extrapolate: `ε = ε_uncond + s(ε_cond − ε_uncond)`. Higher `s` gives stronger prompt adherence and
  less diversity. This single knob is most of what "prompt strength" means in practice.
* **Faster samplers** — DDIM (deterministic, 20–50 steps), DPM-Solver, and consistency/distillation
  models that reach 1–4 steps.
* **Architecture** — U-Net historically; **Diffusion Transformers (DiT)** increasingly, since they
  scale better and inherit transformer infrastructure.
* **Flow matching / rectified flow** — a reformulation learning a straight-line ODE from noise to
  data. Simpler objective, fewer sampling steps, and now the basis of several frontier image and
  video models.

## Diffusion vs autoregressive

| | Diffusion | Autoregressive |
| --- | --- | --- |
| Generates | all positions at once, refined over steps | one token at a time, left to right |
| Iterations | `T` denoising steps over the whole output | `n` steps, one per token |
| Can revise earlier output | ✅ every step touches everything | ❌ committed once emitted |
| Exact likelihood | ❌ variational bound | ✅ |
| Natural domain | continuous (images, audio, video) | discrete (text) |
| Conditioning | guidance scale | prompt |

The domain split is not arbitrary: diffusion needs a meaningful notion of "slightly noisy", which is
natural for pixels and awkward for tokens. Discrete diffusion for text exists and is improving, and
the appeal is real — parallel generation and the ability to revise — but autoregressive models remain
far ahead on text quality. Conversely, autoregressive image generation works but is slow and has
mostly lost to diffusion on images.

## What an interviewer digs into next

* Why can training sample `t` randomly instead of simulating the chain?
* What does classifier-free guidance trade off?
* Why is latent diffusion so much cheaper?
* Why is diffusion natural for images and awkward for text?
