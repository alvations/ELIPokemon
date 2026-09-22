---
id: "258"
slug: diffusion-language-models
style: pokemon
category: optimization
difficulty: advanced
question: "Diffusion language models generate a whole sequence at once instead of left to right. What has actually shipped, and what does the approach cost?"
tags: [diffusion, decoding, non-autoregressive, parallel-decoding, inference]
---

# The wall panels in the Ruins of Alph

Between Violet City and Union Cave, Johto has four sunken chambers, and each one has a puzzle on
the wall: a grid of stone tiles that make a picture. **Kabuto**, **Omanyte**, **Aerodactyl** and
**Ho-Oh**. Solve one and the floor opens onto a chamber where **Unown** appear — twenty-six of
them, one per letter, every single one knowing exactly one move, **Hidden Power**.

A battle is fought one turn at a time and you cannot take last turn back. **The panel is not like
that.** There is no left edge and no first tile. You may touch any tile, in any order, as often as
you like, and nothing is judged until the whole picture is right. That is a diffusion language
model. The wall starts blank, you place the tiles you are sure of, you leave the rest blank, and
you come back round.

```
  A BATTLE (one turn at a time)          THE KABUTO PANEL (four passes over one wall)
  ─────────────────────────────          ────────────────────────────────────────────
  turn 1  Thunderbolt                    pass 0  [ ][ ][ ][ ][ ][ ][ ][ ]
  turn 2  Thunderbolt, Quick Attack       pass 1  [ ][ ]shell[ ][ ]claw[ ][ ]   <- 2 placed
  turn 3  ... Volt Switch                 pass 2  eye[ ]shell[ ][ ]claw rim[ ]  <- 2 more
  turn 4  ... Iron Tail                   pass 3  eye jaw shell[ ]leg claw rim .
  ...                                     pass 4  the whole Kabuto            > opens

  one turn  ->  one action               one pass  ->  as many tiles as you are sure of
  you remember last turn exactly         the wall keeps moving; your memory of it is stale
  the battle ends when it ends           the grid is the size the chamber cut it
```

## Which chambers are actually open, September 2026

**Four panels, four kinds of access, and the difference is the whole answer.**

**The Kabuto and Omanyte panels — open, free, and you can take the tiles home.** `LLaDA-8B`
arrived in February 2025 under MIT, then `LLaDA 1.5`, then `LLaDA-MoE-7B-A1B` in September 2025
(its own chamber wall says it is the first diffusion model trained from scratch with a mixture of
experts, running on about 1B active parameters), then `iLLaDA-8B` in June 2026 under Apache 2.0.
Beside it, **Dream 7B** from April 2025, with `Dream-Coder` and `DreamOn` — and `DreamOn` exists
purely because nobody has solved how a panel decides how big it needs to be. NVIDIA's
**Fast-dLLM** is the crew that makes the chambers usable: caching, confidence-gated tile
placement, block-by-block work, up to 6.18× over the one-turn-at-a-time route on eleven
benchmarks. I read all three chamber walls myself.

**The Aerodactyl panel — open weights from a frontier lab, and the most honest evidence there
is.**
**DiffusionGemma** (`26B-A4B`, June 2026, Apache 2.0) is the same species as `Gemma 4 26B-A4B`,
with the same base stats, raised on a different **Nature**. It denoises 256 tiles at a time, is
reported over 1,000 tokens a second on one H100, roughly four times the throughput — and it is
reported *below* its autoregressive sibling on every benchmark measured, with the lab itself
saying to use the other one when quality is what you want. A Jolly spread is genuinely faster and
genuinely gives up the other stat. That is not a scandal; it is a Nature.

**The paid chamber.** Inception's **Mercury 2.5** (9 September 2026) is reported at 1,107 tokens
a second with a 260K window, sold through its own API and through Baseten, OpenRouter and Azure.
You do not get the tiles. You pay to stand in the room.

**The Ho-Oh panel — still sealed.** **Gemini Diffusion** was shown once in May 2025 and, as far as
anyone outside can tell, has not opened. One open frontier checkpoint, one paid room, and a
legendary on the wall that nobody has caught.

## What the panel buys you

* **Tiles per pass, not tiles per turn.** The unit of work changes. That is why the throughput
  numbers are big and the *first-tile* numbers are not.
* **You can take a tile back.** Filling a hole in the middle is the job, not a special mode. It is
  also why the LLaDA chamber shows the answer appearing on the wall *before* the working that
  leads to it — the reasoning tiles got re-blanked and refilled later.
* **No left edge.** You may start at Kabuto's claw or Kabuto's eye. Working backwards is not a
  special case here; it is the same case.

## What it costs

1. **Power per pass.** The DiffusionGemma-against-Gemma-4 comparison is same-species, same-stats,
   and it goes the wrong way. The LLaDA chamber wall is blunter than any critic: its sampling is
   **slower** than one-turn-at-a-time, for three stated reasons — the grid is a fixed size, the
   ordinary memory of last turn cannot be reused, and it is only at full strength when it takes as
   many passes as there are tiles. One pass per tile is just a battle again, with worse memory.
2. **Two tiles placed blind.** Inside a single pass, each tile is chosen without seeing what the
   others chose this pass. Both look right alone; together they are a **Hidden Power** of the
   wrong type. Every real fix is the same fix — place fewer tiles per pass, or only the ones above
   a confidence line, or only within one 256-tile block. **The parallelism you keep is the
   parallelism you can prove you did not need.**
3. **The grid is the size the chamber cut it.** You cannot add a row mid-puzzle. That is the same
   squeeze as translating into a fixed caption box (question 144).
4. **The room is not finished.** Caching is approximate, and LLaDA's own wall still lists `vLLM`
   support as an unticked box. Block work also makes the *first* tile slower to buy a faster
   *hundredth* — wrong for someone watching it appear, right for a crate of work left overnight.

Two neighbours, kept apart. Question 201's four move slots are also not one-turn-at-a-time, but
that escape works by writing the four options down in advance, not by filling a wall. And the
diffusion in 093 and 137 paints in continuous colour; this one moves discrete stone tiles. Same
word, different chamber.

## What a Gym Leader is listening for

Whether you can say what the extra passes are *for*. They are not ceremony. They are the price of
not placing two tiles blind, and the size of that price is the entire argument.

**Citation note.** The arXiv identifiers linked in the serious half are given from working
knowledge. `arxiv.org` is blocked from the environment this was written in, so **not one of them
was resolved while writing**. Resolve every identifier before you cite it.

## Where this stands, September 2026

I read the LLaDA, Dream and Fast-dLLM chamber walls first-hand: the dates, the licences, the
unticked `vLLM` box, the sampling FAQ. Every DiffusionGemma and Mercury number here is coverage —
those doors are shut from where this was written, and the model cards are the authority. What will
not rot is the shape: a wall filled all at once has to buy its coherence back one pass at a time,
and how much it has to buy back is the whole question.
