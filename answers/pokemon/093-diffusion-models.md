---
id: "093"
slug: diffusion-models
style: pokemon
category: generative
difficulty: advanced
question: "How do diffusion models work, and how do they differ from autoregressive models?"
tags: [diffusion, ddpm, denoising, latent-diffusion, cfg, flow-matching]
---

# Diffusion: developing a Pokémon photo out of static

## Learning to undo the damage 📸

Take a clean sprite of a Charizard. Now **damage it slightly** — add a bit of static. Then a bit
more.
And more. After a few hundred rounds, it's pure static. The Charizard is gone.

```
   ➡️ RUINING IT (no skill required)
   🖼️  →  🖼️🌫️  →  🖼️🌫️🌫️  →  ...  →  🌫️
   clean    a bit     more            pure static

   ⬅️ RESTORING IT (this is the skill)
   🌫️  →  ...  →  🖼️🌫️🌫️  →  🖼️🌫️  →  🖼️
   static                                Charizard
```

The training is simple: **damage a photo by a random amount, and have the Trainer identify exactly
what static was added.** Millions of times, at every damage level.

That's it. No adversary, no competition, no clever objective. Just: *"spot the static."*

## Then the magic 🎩

Once your Trainer can spot static, hand it **pure static** and say *"remove the static — there is a
Pokémon under there somewhere."*

It does. Slightly. What's left is *marginally* less random.

Do it again. And again. Three hundred times.

**A Charizard emerges** — one that never existed, never appeared in any Pokédex, developed out of
pure noise by a Trainer whose only skill is knowing what static looks like and taking a bit off.

## Why this replaced the old approach 🥊

The previous method was a **contest**: a forger trying to fake Pokémon photos, and a detective trying
to catch them.

It worked, and it was miserable to run:

* ⚖️ Keep the two **exactly** balanced or it collapses. Detective too good → the forger gives up
  and only ever draws Voltorb.
  Forger too good → detective learns nothing.
* 🎯 The forger cheats. It finds **one** Pokémon it can fake convincingly — a Voltorb, because it
  is a sphere — and produces only that, forever. Technically undefeated. Useless.

The static approach has **no contest.** One Trainer, one job, a straightforward score. It trains
stably, it covers the full variety of Pokémon instead of collapsing onto one, and it gets predictably
better with more resources.

❌ Its one real cost: **it's slow.** Three hundred rounds of static removal per photo, versus one shot
for the forger.

## Four things that made it practical 🔧

* 🗜️ **Work from a sketch, not the full sprite.** Instead of developing every pixel of the
  Charizard, develop a small compressed sketch and expand it at the end. Roughly fifty times cheaper — and the reason anyone can
  run this on their own machine.
* 🎚️ **The "how literally?" dial.** Train it to develop sprites both *with* and *without* a
  description — *"an orange dragon with wings"*, then at generation time **exaggerate the difference.** Crank it up and you get exactly
  what you asked for, with less variety. Turn it down and you get more surprising results, less
  faithful. This one dial is what people mean by prompt strength.
* ⚡ **Take bigger steps.** Three hundred rounds became fifty, then twenty, then — with some cleverness
  — **one or two.**
* 📏 **Go in a straight line.** Newer approaches learn to travel **directly** from static to sprite
  rather than wandering there. Fewer steps, simpler training, and it's what the frontier uses now.

## vs. the Trainer who writes one word at a time ✍️

| | 🌫️ Static removal | ✍️ One word at a time |
| --- | --- | --- |
| Builds | the **whole thing at once**, refined repeatedly | left to right, one piece at a time |
| Can revise earlier parts | ✅ **every round touches everything** | ❌ said is said |
| Steps | ~a fixed number, regardless of size | one per word |
| Natural for | 🖼️ pictures, 🎵 sound, 🎬 video | 📝 text |

The split isn't arbitrary. **"A slightly damaged photo" is a sensible thing.** A photo with a bit of
static is still recognisably a photo.

**"A slightly damaged sentence" isn't.** What's halfway between "Pikachu" and "Charizard"? Not a
word. Not a Pokémon. Not anything.
Not anything. Text is made of discrete things with no meaningful in-between, so the whole "gradually
remove the damage" idea has nothing to stand on.

People are working on it — the appeal is real, since you'd generate a whole answer at once and get to
**revise it**, which a left-to-right Trainer can never do. It's improving. It's not close yet.
