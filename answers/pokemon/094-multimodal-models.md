---
id: "094"
slug: multimodal-models
style: pokemon
category: multimodal
difficulty: intermediate
question: "How do vision-language models fuse modalities?"
tags: [multimodal, vlm, vision-encoder, projector, cross-attention, llava]
---

# Teaching your Trainer to look at the field, not just read about it

Your Trainer reads brilliantly. Hand it a **written** Pokédex entry for Ferrothorn and it's a genius.

Hand it a **photograph** of the field and it has no idea what it's looking at. It reads words. A sprite of a Gyarados isn't the word "Gyarados".

## Fix 1: translate the sprite into words 🔤

Hire a **spotter** who looks at the field and describes what they see — *"orange, wings, flame on
the tail"* — not in English, but directly
in the format your Trainer already understands.

```
   📸 sprite ─► 👁️ SPOTTER ─► 🔤 "tokens" ─┐
                                           ├─► 🧠 TRAINER (unchanged!)
   📝 text  ─► reading ────► 🔤 tokens ────┘
```

Your Trainer doesn't change at all. It just receives some tokens that happen to have come from a
sprite instead of a Pokédex page. As far as it's concerned, it's still reading.

✅ **Simple, cheap, reuses everything you already have.**
❌ **A sprite eats a LOT of space.** One picture might consume as much room as a thousand words — and
a few photos fill your Trainer's bag entirely.

## Fix 2: let the Trainer glance at the photo 👀

Instead of converting the sprite into words, **give your Trainer the ability to look up.**

Insert a "glance at the field" instinct that lets it check the sprite whenever it needs to, mid-thought,
without the photo living in its bag at all.

✅ **The photo costs no bag space.** Your Trainer's existing skills are completely untouched.
❌ Requires actual surgery on the Trainer, and new parts to train.

## Fix 3: raise it seeing from birth 👶

Don't teach an adult Trainer to see. **Raise one from the wild grass on photos and words mixed
together**, so it never distinguishes the two.

✅ **Deepest understanding** — and it can *draw* as well as describe.
❌ **Enormously expensive.** You cannot reuse an existing Trainer. You're starting over.

## How fix 1 actually works 🔧

The common approach, because it's cheap and it works.

**👁️ The spotter.** Don't train one — hire an existing one, someone who has already looked at a
million sprites and captions. Specifically, hire a spotter who was
**already trained to match photos with descriptions** (that shared map from before). Their
observations are already halfway into word-shaped territory, which is most of the job done.

**🔤 The translator.** A tiny converter turning *"orange, wings, tail flame"* into something the
Trainer reads as "Charizard".
Genuinely tiny — a couple of layers is enough, and fancier translators mostly haven't paid off.

**🎓 Two training stages:**

```
   Stage 1: ❄️ Freeze the spotter. ❄️ Freeze the Trainer.
            🔥 Train ONLY the translator, on photos with captions.
            → the translator learns to speak Trainer.

   Stage 2: 🔥 Now let the Trainer adjust too, on real tasks.
            → the Trainer learns what to DO with what it's seeing.
```

The striking thing is how cheap this is. A strong spotter plus a strong Trainer plus **one day**
teaching them to talk to each other, and you have a Trainer that sees. You bought two finished
components and built the bridge.

## What's still hard 😬

**🔍 It can't read small print.** The spotter looks at the whole field at once and reports the gist.
Ask it to read the Leftovers recovery ticking away in the corner of the HP bar and it can't — it
never looked
closely.

The fix is to **chop the sprite into pieces and examine each closely** — the tail flame in one
crop, the wings in another. Which works, and multiplies
your bag problem by the number of pieces.

**📦 Sprites are enormous.** Four of them and your Trainer's bag is full, with no room for the actual
conversation.

**📐 It's bad at spatial questions.** *"Is the Ferrothorn on Toxapex's left or right?"* Counting and precise
positioning remain genuinely weak. It sees the gist, not the geometry.

**🙈 It ignores the photo when the words are enough.**

The insidious one. Ask *"what type is the Pokémon in this photo?"* and show a picture of a Gyarados —
and your Trainer might say "Water/Flying" because that is what the *words* of the question
usually go with, **without ever really looking.** It would say the same for a photo of Milotic.

Confident. Fluent. **Didn't look at the picture.**

**🎬 Video is photos times a thousand.** A whole battle replay is a photo per frame, and a photo is
expensive. Picking
*which* frames to look at is most of the problem.

## The bigger point 🌍

The same recipe works for anything: **Pokémon cries, 3D models, sensor readings.** Hire a spotter for that
thing, build a small translator, train the bridge.

Your Trainer has become a general-purpose thinker about **anything you can find a spotter for.**
