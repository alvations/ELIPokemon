---
id: "137"
slug: diffusion-image-generation
style: pokemon
category: multimodal
difficulty: advanced
question: "How do diffusion models generate images from text?"
tags: [diffusion, latent-diffusion, classifier-free-guidance, dit, flow-matching, fid]
---

# A Pokémon coming out of a Poké Ball

Throw the Ball and nothing coherent comes out at first — a formless burst of light that becomes,
over a moment, exactly one **Charizard**. Not a rough Charizard that gets tidied up. A shapeless
glow that **resolves**.

That is the whole idea, and the training is the same thing filmed backwards.

## Learn to un-scatter, one small step at a time 🌀

```
   FORWARDS — this needs no learning at all
   a real Charizard ──► scatter it slightly ──► scatter again ──► ... ──► formless light
        the scattering follows a fixed recipe, so you can jump straight
        to "quite scattered" or "almost completely gone" whenever you like

   THE DRILL
   take a real Pokémon. scatter it by some amount. ask:
        "how much scattering was added, and in what direction?"

   BACKWARDS — this is the Poké Ball opening
   formless light ──► undo a little ──► undo a little ──► ... ──► Charizard
                            ▲
                 what you asked for enters HERE, at every single step
```

📌 The trick is that **un-scattering a little is easy**, even though conjuring a whole Charizard
out of nothing is not. Nobody ever asks it to do the hard thing. They ask it to do the easy thing
fifty times.

## The Ball does not hold a Pokémon 🔴

A **Poké Ball** does not contain a Charizard the size of a Charizard. It holds it **converted** —
compressed into something far smaller, and unpacked again on the way out.

Do the whole scattering-and-unscattering business inside that compressed form and it is dozens of
times cheaper. This is the single reason any of this is affordable.

⚠️ And the compression is **lossy**. Fine detail can be destroyed by the *Ball* before the
un-scattering ever gets a look at it. So when someone complains that the machine cannot render the
lettering on a **TM**, the culprit is very often not the un-scattering at all — it is that the
lettering never survived being put in the Ball.

## How hard to insist 🎚️

The Trainer's instruction — *"a Charizard, at sunset, over Cinnabar Island"* — has to actually
bite, and there is a dial for how forcefully.

The machine is drilled to predict the un-scattering **both** with the instruction and, sometimes,
without it. The difference between those two is *"the direction the instruction pushes in"*. Then
you push harder along it:

```
   dial at 1   ─ instruction barely matters. vague, varied, wanders off-brief
   dial at 7   ─ the usual setting. sharp, and it is the Pokémon you asked for
   dial at 20  ─ garish, blown-out, every Charizard identical, and increasingly mangled
```

Which is precisely the trick from question 122 run in reverse: there we **subtracted** what the
machine would have said without looking, to kill invention. Here we **add** it back with the sign
flipped, to force it to listen.

## Making it fast 🏃

Fifty un-scatterings is a long time to wait. So you drill a student to take the whole journey in
**one or two leaps** instead of fifty small steps — a **Quick Attack** rather than a careful
approach. You get near-instant Pokémon, and you get slightly *fewer different* Pokémon: every
shortcut smooths out some of the variety it skipped past.

## Where it goes wrong 🚨

* **🔤 Lettering.** Improving quickly, still the tell. Half the Ball's fault, half because letters
  are a *discrete* thing being conjured by a smooth, continuous process.
* **🔢 Counting.** Ask for **six Voltorb** and you will get somewhere between four and eight, every
  time. Nothing in the process ever counted anything.
* **🎨 Attributes attaching to the wrong Pokémon.** *"A red Charizard beside a blue Blastoise"* and
  you get a blue Charizard. This is exactly the bag-of-words weakness from question 120, arriving
  through the same door it always does — the part that read the instruction.
* **🚫 Negation.** Ask for *"a route with no Zubat on it"* and here comes a Zubat. The word was in
  the instruction; the instruction has no way to hold a minus sign.
* **🧭 Left and right**, for all the reasons in question 128.

## Judging the output 🏅

There is a standard measure that compares a heap of generated Pokémon against a heap of real ones
and reports how similar the two heaps look overall. It is genuinely useful and it has two
blind spots worth knowing: it depends heavily on how many you generated, and **it cannot see
whether you got the Pokémon you asked for at all.** A machine that produces exquisite Blastoise
when asked for Charizard scores beautifully.

There is a second measure for whether it matched the instruction, and it is gameable.

📌 Neither replaces **asking Trainers which one they prefer**, which remains the only thing anyone
serious decides on. Report all three, and say what you generated them from.
