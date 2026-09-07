---
id: "158"
slug: image-editing-inpainting
style: pokemon
category: multimodal
difficulty: intermediate
question: "How does instruction-based image editing work, and why is preservation hard?"
tags: [inpainting, instruct-editing, controlnet, identity-preservation, masks, editing-metrics]
---

# Make this Gyarados shiny. Change nothing else.

Generating a Pokémon from nothing (question 137) is a loose brief — **any** convincing Gyarados
will do.

Editing one is pinned down at both ends. A **shiny** Gyarados is the same Gyarados in **red**
instead of blue. Same size, same pose, same **Lake of Rage** behind it, same everything. Only the
colour moves.

📌 And that second half — *change nothing else* — is the hard one, and it is the one that almost
every scoreboard quietly fails to measure.

## Three ways to do it 🖌️

**1. 🎭 Draw a ring around the part to change.**

```
   the photograph + a ring around the Gyarados ─► re-imagine ONLY inside the ring,
                                                   looking at the outside for context
                    ▲
        outside the ring is copied exactly. that is both the strength AND the ceiling:
        it cannot make any change that needs the ring itself to move.
```

Preservation is **guaranteed**, not hoped for. ⚠️ The failure is at the **edge** — the light inside
the ring not matching the light outside, so the Gyarados looks pasted onto the lake.

**2. 💬 Just say it.** No ring. *"Make it shiny."* The machine works out for itself what to touch —
because it was drilled on before-and-after pairs.

⚠️ And here is the complaint that dominates this entire field: **it changes everything.** You asked
about the Gyarados. It has also brightened the lake, moved the horizon, restyled the **Magikarp**
in the background and warmed the whole picture half a shade. Every individual change is small.
Together they are a different photograph.

**3. 🦴 Keep the skeleton and repaint around it.** Trace the pose, the depth, the outlines — then
generate a fresh picture that obeys them. Superb for restyling. **Useless** for *"remove the
Poké Ball from the shore"*, because the Poké Ball is in the tracing.

## Keeping it the *same* Pokémon 🧬

The hardest part is not "a Gyarados" — it is **this** Gyarados. Your Gyarados. The one from the
Lake of Rage with that scar.

Every technique here trades **staying itself** against **being editable**. Hold the identity hard
enough and the machine stops listening to the instruction; loosen it and you get a lovely picture
of somebody else's Pokémon. 📌 That curve *is* the engineering problem. There is no setting that
escapes it.

## And the part that is not a craft problem ⚖️

These tools are how a photograph becomes evidence of something that never happened. A **Ditto**
that anyone can operate.

Anything built here should carry its history with it — a signed record of what was changed, or a
mark inside the image itself — and should **refuse** to put identifiable people into situations
they were never in.

⚠️ And it has to be there from the first day. Bolting provenance on later does not work, because
by then the untagged pictures are already out in the world and nothing distinguishes them.

## Judging it: two numbers, always 🏅

Report **both**, because they pull against each other:

* ✅ **Did the change happen?** Is the Gyarados actually red?
* 🛡️ **How much of the rest survived?** Measured **outside the ring** — is the lake the same lake,
  is the Magikarp the same Magikarp?

⚠️ Either one alone can be maxed out by a machine that is doing nothing useful:

* **Hand back the original untouched** → perfect preservation, zero edits.
* **Generate a completely new picture** → perfect edit, nothing preserved.

📌 So **any single-number leaderboard in image editing is rewarding one of those two frauds**, and
you cannot tell which from the number.
