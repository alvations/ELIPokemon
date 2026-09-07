---
id: "137"
slug: diffusion-image-generation
style: serious
category: multimodal
difficulty: advanced
question: "How do diffusion models generate images from text?"
tags: [diffusion, latent-diffusion, classifier-free-guidance, dit, flow-matching, fid]
---

# Text-to-image diffusion

A diffusion model is trained to do one narrow thing: **given a noisy image and a noise level,
predict the noise.** Everything else — text conditioning, guidance, samplers — is machinery built
around that single objective.

## Forward and reverse

```
   FORWARD (training, no learning needed)
   x₀ ──► add noise ──► x₁ ──► ... ──► x_T ≈ pure Gaussian noise
        a fixed schedule; you can jump to any timestep t in one step

   TRAINING
   sample an image, sample t, add the corresponding noise, ask the network:
        "what noise was added?"        loss = ‖ε − ε_θ(x_t, t, text)‖²

   REVERSE (generation)
   x_T = noise ──► predict noise ──► step toward less noise ──► ... ──► x₀
                        ▲
                   text conditioning enters here, at every step
```

The insight is that the reverse of a gradual corruption is a gradual *construction*, and each
individual denoising step is an easy prediction problem even though generating an image in one shot
is not.

## Latent diffusion: why it is affordable

Running this at 1024x1024 pixels is prohibitive. **Latent diffusion** trains a VAE to compress
images roughly 8x per side into a latent space, and runs the entire diffusion process there — a
1024px image becomes a 128x128 latent, roughly 64x less to work on. The VAE decoder restores
pixels at the end.

The cost: the VAE is a lossy bottleneck. Fine detail — small faces, text, high-frequency texture —
can be destroyed by the autoencoder before diffusion is even involved. When people debug "the model
cannot render small text", the VAE is often the culprit rather than the denoiser.

## Text conditioning and classifier-free guidance

Text embeddings (T5, CLIP text encoder, or both) enter through **cross-attention** in each block —
the same mechanism as question 119.

**Classifier-free guidance** is what makes prompts actually bite. During training the text
condition is randomly dropped (~10%), so the model learns both conditional and unconditional
prediction. At sampling:

```
   ε̂ = ε_uncond + w · (ε_cond − ε_uncond)          w = guidance scale

   w = 1   ignore guidance — vague, diverse, weakly prompt-following
   w = 7   typical — sharp, on-prompt
   w = 20  oversaturated, high-contrast, mode-collapsed, mangled
```

The term being amplified is *the direction the text pushes in*, which is precisely the "subtract
the unconditional prior" trick used against hallucination in question 122 — run backwards, to
amplify conditioning rather than remove it.

## Architecture and objective, current state

* **U-Net → DiT.** Transformers replaced convolutional U-Nets as the backbone; they scale more
  predictably, which is the same argument as everywhere else in the field.
* **Flow matching / rectified flow** reframes the process as learning a straight-line velocity
  field between noise and data rather than a stochastic denoising chain. Simpler objective,
  straighter trajectories, fewer sampling steps for the same quality. Most recent systems use it.
* **Step distillation** (consistency models, adversarial distillation) trains a student to jump
  many steps at once, taking generation from 50 steps to 1-4. This is what makes real-time
  generation possible, at some cost in diversity.

## Known failure modes

* **Text rendering.** Improving fast, still the giveaway. Partly VAE loss, partly that character
  shapes are a discrete structure being produced by a continuous process.
* **Counting.** "Six apples" reliably produces four to eight.
* **Compositional binding.** "A red cube on a blue sphere" swaps attributes — the same
  bag-of-words weakness the text encoder brought with it (question 120).
* **Negation.** "A room with no elephant" summons an elephant; the prompt embedding contains it.
* **Spatial relations**, for the reasons in question 128.

## Evaluation

**FID** compares feature-space statistics of generated and real image sets. It is sensitive to
sample size, backbone, and preprocessing, correlates poorly with human judgement at the top of the
range, and cannot see prompt adherence at all. **CLIPScore** measures prompt alignment and is
gameable. Neither substitutes for **human preference evaluation**, which remains the standard for
anything that matters. Report all three, and say what you generated them from.

## What an interviewer digs into next

* Why is predicting the noise an easier objective than predicting the image?
* What does the VAE cost you, concretely?
* Why does high guidance scale degrade images?
* Why does the model fail at negation specifically?
