---
id: "156"
slug: translating-code-and-markup
style: serious
category: translation
difficulty: intermediate
question: "How do you translate documents containing code, markup and placeholders?"
tags: [markup, tags, placeholders, inline-formatting, xliff, segmentation]
---

# Translating around things that must not be translated

Technical documentation, help centres, UI copy and product content are not plain prose. They are
prose interleaved with **things that must survive byte-identically**: code blocks, inline tags,
placeholders, URLs, file paths, keyboard shortcuts. Damage any of those and you have not degraded
the translation — you have broken the product.

## The classes, and how each fails

| Element | Failure |
| --- | --- |
| **Fenced code blocks** | translated identifiers, translated comments (sometimes wanted), broken indentation |
| **Inline code** | `git commit` becomes a translated phrase; the command no longer exists |
| **Placeholders** (`{count}`, `%s`, `{{name}}`) | translated, reordered, or braces mangled — a crash at render time |
| **Inline tags** (`<b>`, `<a href>`) | dropped, unbalanced, or wrapping the wrong words |
| **URLs and paths** | "translated" into something that 404s |
| **Keyboard shortcuts** | `Ctrl+S` localised when it should not be, or *not* localised when it should |
| **Anchors and cross-references** | link text translated, anchor target not, so the link dies |

## The standard mechanism: protect, translate, restore

```
   source:   "Run <code>git commit</code> to save {count} changes."
                       │
   protect:  "Run ⟦1⟧ to save ⟦2⟧ changes."      ← tags replaced by opaque markers
                       │
   translate:"Führen Sie ⟦1⟧ aus, um ⟦2⟧ Änderungen zu speichern."
                       │
   restore:  "Führen Sie <code>git commit</code> aus, um {count} Änderungen zu speichern."
```

This is what XLIFF and every commercial localisation pipeline do. Two things it does not solve:

* **Reordering.** The markers must be allowed to move — target word order differs — but the model
  may drop or duplicate them. **Validate after restoration**: same multiset of markers in, same out.
  This check is cheap and catches most damage.
* **Tags with translatable attributes.** `<a title="Save file">` has translatable content *inside*
  a protected element. Naive protection freezes it and it ships in English.

## LLM-specific notes

LLMs handle markup better than classical NMT — they have seen HTML and Markdown — and they fail
differently: they **helpfully reformat**. They will fix your indentation, convert quotes to smart
quotes, tidy a list, translate a comment you wanted left alone, or add an explanation after the
translation. Constrain the output format explicitly and validate mechanically; do not trust
compliance.

Comments in code are the interesting judgement call: for user-facing tutorial code, translating
comments is usually right; for a copy-paste snippet the user will run, translating a comment while
leaving the code is inconsistent but harmless, and translating a *string literal the code prints*
may be either essential or a bug depending on whether the reader will run it.

## Segmentation

Splitting a document into translation units is where much of the damage originates. Never split
inside a code block. Never split a sentence across a tag boundary. Keep list items whole. A
sentence broken across two segments gets translated twice out of context, and in a language with
different word order the two halves cannot be reassembled.

## Evaluation

Quality metrics do not see any of this. Report **integrity checks** as a separate gate:

* placeholder set preserved, exactly;
* tags balanced and well-formed;
* code blocks byte-identical (or intentionally changed, with a rule saying so);
* URLs unchanged and still resolving;
* rendered output parses.

Treat integrity as **pass/fail per segment**, not as a score. A single broken placeholder is a
crash, not a quality regression, and averaging it away is exactly the mistake question 129 warns
about.

## What an interviewer digs into next

* Why must protection markers be allowed to reorder, and what do you check afterwards?
* When should code comments be translated?
* Why is bad segmentation the root of most markup damage?
* Why is integrity pass/fail rather than a quality score?
