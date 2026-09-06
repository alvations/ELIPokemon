---
id: "123"
slug: document-understanding-ocr
style: serious
category: multimodal
difficulty: intermediate
question: "How do you build question answering over scanned documents?"
tags: [ocr, docvqa, layout, reading-order, tables, anls, grounding]
---

# Document understanding and OCR-grounded QA

Document QA looks like image QA and is not. The information is **text rendered as pixels**, laid
out in a structure that carries meaning: columns, tables, headers, footnotes, form fields. Get the
structure wrong and the words are useless.

## Two architectures

**Pipeline: OCR, then a language model.**

```
   scan ─► [ OCR engine ] ─► words + bounding boxes
                                  │
                                  ├─► layout analysis: columns, blocks, reading order
                                  ├─► table structure recognition
                                  ▼
                          serialised text (+ coordinates) ─► LLM ─► answer + citation
```

**End-to-end: pixels straight to text** (Donut, Pix2Struct, and modern high-resolution VLMs). No
OCR stage at all; the model reads the image and emits the answer.

| | Pipeline | End-to-end |
| --- | --- | --- |
| Errors | OCR errors compound downstream and are invisible to the LLM | one model, one failure surface |
| Grounding | boxes for free — citations are exact | must be trained to emit boxes |
| Debugging | you can inspect every stage | opaque |
| Languages/scripts | limited by the OCR engine | limited by pretraining |
| Handwriting, degraded scans | usually poor | often better |
| Cost | cheap per page | expensive (high-res tokens) |

In practice production systems are usually pipelines with a VLM fallback, precisely because
citation and auditability matter in the domains where document QA is used — finance, legal,
healthcare.

## Reading order is the underrated problem

A two-column page serialised left-to-right, top-to-bottom interleaves the columns into nonsense.
A table serialised as a flat token stream loses the row/column association that made it a table.

```
   TWO-COLUMN PAGE                     NAIVE SERIALISATION
   ┌──────────┬──────────┐             "The quarterly In addition the
   │ The      │ In       │              results board approved
   │ quarterly│ addition │              showed the a new..."
   │ results  │ the board│
   └──────────┴──────────┘             ← every line is half of two sentences
```

Fixes: run real layout analysis (block detection, then reading-order prediction), preserve
coordinates so the LLM can reason spatially, and serialise tables into a structure-preserving
format — Markdown or HTML tables, not raw text. For forms, keep key-value pairing explicit.

## Evaluation

* **ANLS** (Average Normalised Levenshtein Similarity) is the DocVQA standard. It gives partial
  credit for near-miss strings, because exact match punishes a single OCR character error as
  harshly as a wrong answer.
* **Report OCR quality separately.** If end-to-end accuracy drops, you need to know whether the
  words were wrong or the reasoning was.
* **Test the layout cases explicitly**: multi-column, rotated pages, tables spanning pages,
  stamps and handwriting over print, low-DPI scans.
* **Grounding accuracy** — does the cited box actually contain the answer? A correct answer with a
  wrong citation is a system nobody should trust.

## Practical notes

* Normalise Unicode after OCR (question 115); engines emit inconsistent forms and ligatures.
* Deskew and denoise before OCR; it is a larger accuracy lever than model choice.
* Resolution matters more here than in any other multimodal task (question 121). Text needs
  roughly 10 pixels of x-height to be reliably readable.
* For long documents, retrieve relevant pages first (question 044) rather than feeding 200 pages
  of high-resolution tiles into context.

## What an interviewer digs into next

* When would you choose end-to-end over an OCR pipeline?
* Why does reading order matter more than OCR accuracy on some documents?
* Why ANLS rather than exact match?
* How would you make document answers auditable?
