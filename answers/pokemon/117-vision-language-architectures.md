---
id: "117"
slug: vision-language-architectures
style: pokemon
category: multimodal
difficulty: core
question: "How do vision-language models connect an image encoder to a language model?"
tags: [vlm, projector, cross-attention, clip, llava, flamingo]
---

# Professor Oak's Pokédex is two machines pretending to be one

Point it at a Pokémon. It looks. Then it *talks* — species, height, weight, a paragraph of
Pokédex entry.

Those are not the same skill, and they are not the same machine. There is **a lens**, which is
very good at seeing and cannot say a word. And there is **the voice**, which is very good at
words and has never seen anything in its life. Everything hard about building a Pokédex is the
wire between them.

## The wire is the whole problem 🔌

The lens produces something like *"this thing is orange, it has a flame on the tail, it is about
this tall."* Not in words — in whatever the lens's own private language is.

The voice does not read that language. The voice reads **Pokédex-speak**.

So you need a translator sitting in between, and there is exactly one Pokémon in the world whose
entire nature is converting between one representation and another: **Porygon**, built by Silph
Co. out of programmable code, able to move between the physical world and the digital one. That
is the job. Porygon takes what the lens saw and re-renders it as something the voice can read.

## Two ways to wire it 🧩

```
  ── THE PORYGON SPLICE ────────────────────────────────────────────
     lens ─► [ what it saw ] ─► 🔮 Porygon ─► ...words-shaped things...
                                                    │
        Trainer asks: "what is this?" ──────────────┴──► 📖 voice ─► entry

     the sight is chopped into words and dropped INTO the sentence


  ── THE SPOTLIGHT WIRE ────────────────────────────────────────────
     lens ─► [ what it saw ] ─────────┐
                                      ▼
        Trainer asks: "what is this?" ─► 🔦 glance at the lens ─► 📖 voice ─► entry

     the sentence stays a sentence; the voice just LOOKS UP mid-thought
```

**The Porygon splice** turns the sighting into a run of word-shaped tokens and pushes them into
the sentence, as though the lens had spoken them aloud. It is beautifully simple — the voice does
not need modifying at all, it just receives a longer sentence. The cost is that the sentence gets
*enormous*. A detailed look at a single Pokémon might add six hundred word-slots to a question
that was four words long, and the voice pays for every one of them, every layer, every time.

**The spotlight wire** keeps the question short and teaches the voice to glance sideways at the
lens whenever it needs to. Cheaper to run, especially if you are looking at a whole team at once
or a moving battle. But you have had to open the voice up and add new machinery inside it, and it
is no longer a stock Pokédex.

There is a middle option: send a **Smeargle** in first. Smeargle's Sketch copies exactly one
move and keeps it — one slot, no matter how complicated the thing it copied was. Put a handful of
Smeargles between the lens and the voice and you get a fixed, tiny summary of any sighting at
all, however detailed. Bounded cost. And, unavoidably, a summary: everything Smeargle did not
sketch is simply gone.

## Which machine you are allowed to retrain 🧊

The order matters enormously, and everybody gets it wrong the same way.

**First: freeze both towers. Train only Porygon.** The lens is already excellent at seeing. The
voice is already excellent at talking. Neither of them is the problem. Show the pair a great many
Pokémon-with-caption pairs and let *only the translator* learn.

**Second: let the voice learn, on real instructions.** Not "describe this" — "which of these two
is holding a Leftovers?", "read the TM label", "is that Nidoran♀ or Nidoran♂?" This is where the
Pokédex stops narrating and starts answering.

📌 **Do not retrain the lens early.** People do it constantly. You are letting a talking machine
grade an eye, using a lesson about words, and the eye gets worse. Ash's Pokédex did not need a
better camera; it needed the wire fixed.

## Four ways the Pokédex lies 🚨

* **🙈 It stops looking.** If Porygon's output is mush, the voice falls back on what is *usually*
  true. Ask it about an orange lizard with a flame and it will tell you about Charizard's wings
  whether or not the thing in front of it has any. That is the root of most Pokédex
  hallucination (question 122) — the voice answering from habit because the lens went quiet.
* **🔍 It cannot read fine print.** The lens was built to recognise a Pokémon from across a
  clearing. Hand it a TM's label or a Pokédex page and shrink the whole thing to fit, and the
  letters are gone before the voice ever sees them (question 121).
* **🗣️ It forgets how to talk.** Train it only on things-it-can-see and its plain conversation
  degrades. Keep feeding it ordinary text, or the Pokédex becomes a machine that can only
  describe and can no longer explain.
* **↔️ It loses left and right.** Chop a scene into tiles, thread them into a sentence, and the
  tiles arrive in a row with no memory of the grid they came from. The Pokédex will identify
  **Zapdos** and **Moltres** correctly and then confidently tell you Zapdos is the one on the
  right when it is on the left. Identity survives the flattening. Geometry does not — unless you
  tell each tile where it sat.
