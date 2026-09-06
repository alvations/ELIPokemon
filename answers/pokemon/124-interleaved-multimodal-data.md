---
id: "124"
slug: interleaved-multimodal-data
style: pokemon
category: multimodal
difficulty: advanced
question: "Why train on interleaved image-text documents instead of image-caption pairs?"
tags: [interleaved, obelics, mmc4, in-context-learning, data-curation, packing]
---

# A photo album is not a field journal

**Professor Oak's photo album** is one picture, one verdict. A shot of a **Scyther** in the
tunnel, and underneath it Oak's rating. Another shot, another rating. Hundreds of them, each one
complete in itself, each one about exactly one Pokémon.

**A Trainer's field journal** is a different object entirely. Sketches and handwriting running
together down the page: *"Caught this one outside Violet City — see the crest? Compare it with the
one from the Ruins, which has none. The third one I only glimpsed..."* Three sketches, one
paragraph, and the paragraph **points at them by position.**

Train on the album and you get a machine that describes a Pokémon. Train on the journal and you
get something that can hold several in its head at once.

## What only the journal teaches 📓

```
   THE ALBUM                          THE JOURNAL
   ─────────                          ───────────
   🖼️ "a Pokémon with a crest"        "look at 🖼️ — note the crest.
   🖼️ "a Pokémon without one"          now 🖼️, where there is none.
   🖼️ "a Pokémon in flight"            the third, 🖼️, was moving too fast to..."

   one at a time, forgotten           several at once, referred back to
```

Two abilities come almost entirely from journals, and not at all from albums:

* **🎓 Learning the task from the page itself.** Show three sketches with their verdicts written
  underneath, then a fourth sketch with the verdict left blank. A Trainer who grew up on journals
  works out what is being asked and fills it in. A Trainer raised on the album has **never seen
  two sketches on one page** and has no idea what you want.
* **↔️ Comparing and referring back.** *"The second one."* *"Unlike the previous sketch."* *"The one
  on the left."* You cannot learn to follow those from a stack of unrelated photographs, because
  there was never a *previous* anything.

## Journals are messy in a way albums are not 🗑️

The album's captions were written about the photograph they sit under. The journal's were not
always. Somebody sketched a Pidgey, then wrote two pages about the weather, then sketched a
Sentret. The handwriting near a picture is often **not about that picture at all.**

So a real curator does this:

* **🚫 Throw out sketches that carry nothing.** The Trainer's name stamped in the corner of every
  page. The little Poké Ball doodle in every margin. A hundred pages, the same doodle, no
  information anywhere in it.
* **🔗 Check that the words and the sketch have *something* to do with each other — loosely.** And
  here is the trap. It is very tempting to keep only pages where the writing plainly names the
  Pokémon in the sketch. ⚠️ **Do that and you have thrown the journal away and rebuilt the album.**
  The loose association *is the thing you came for*: "compare it with the one from the Ruins" is
  exactly the sentence a strict filter deletes, and exactly the sentence that teaches comparison.
* **📏 Cap how many sketches one page may contribute**, or a single spread of forty Zubat drowns
  out fifty other Trainers' journals.
* **♻️ Remove repeats** — the same sketch traced into three different journals — and check none of
  them are the ones you meant to test with later.

## Do not feed it only journals 🍽️

| What goes in | What it is for |
| --- | --- |
| 📸 Oak's album — one sketch, one careful verdict | precision. *Exactly* what that Pokémon is, and what colour |
| 📓 Field journals | several at once, comparison, learning the task from the page |
| 📜 Plain writing, no pictures at all | so it does not forget how to hold a conversation |
| 🏷️ Labels, price boards, charts | the specific chores you will actually ask of it |

Drop the plain writing and it slowly loses the ability to *talk*, which nobody notices until
somebody asks it something with no picture attached. Drop Oak's album and its descriptions go
vague — good at *"the second one is bigger"*, hopeless at *which species*, because nothing ever
made it be exact.

## Stitching pages together 🧵

Journals are all different lengths, so you end up binding several Trainers' pages into one volume
to work through. Three things to get right:

* **🚧 Put a hard divider between one Trainer's journal and the next.** Without it the reader will
  cheerfully carry a sentence from Falkner's notebook straight into Bugsy's and learn a connection
  that never existed.
* **⚖️ Even out the sketches per volume.** One volume with sixty drawings and the next with two
  means half your Gym sits idle waiting for the other half to finish looking.
* **📌 And keep every caption under its own sketch.** An off-by-one — every note sitting under the
  drawing *after* the one it describes — is the worst bug in this whole business, because nothing
  fails. Training runs. Numbers look fine. And you have quietly built a Pokédex that, shown a
  **Charmander**, describes the Squirtle you are about to show it next.
