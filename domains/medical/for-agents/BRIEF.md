# Standing brief — writing for the medical domain

You have been assigned a **specialty** and a **block of IDs**. Everything else you need is here.
Read this file, then `../SAFETY.md`, then `../README.md`. Then write.

## Read first, in this order

1. **`../SAFETY.md`** — the most important file in the domain. Read it twice.
2. `../README.md` — the seven specialties, the layout, the conventions.
3. `../../../CONTRIBUTING.md` and `../../../for-agents/LEARNINGS.md` — especially "Named entities that
   are load-bearing", "A good analogy can score near zero, and the scorer is right to do it", and
   "The brief was wrong, and the right move was to write against it".
4. **Two existing pairs in your own specialty**, if any exist, for voice and for the conventions
   already established. If your specialty is empty, read `../answers/pharmacology/serious/m006-*.md`
   and its Pokémon counterpart — the highest-scoring block written so far.
5. `CONVENTIONS.md` in this directory — the analogy mappings already in use. **Reuse them where they
   fit.** A specialty with one vocabulary is worth more than a specialty with fifty metaphors.

## The shape of an answer

Both halves carry the same sections in the same order:

| Section | Both halves? | Notes |
| --- | --- | --- |
| H1 | yes | A claim, not a label |
| body | yes | The mechanism. At least one column-aligned fenced diagram in the serious half |
| `## Where the metaphor stops` (Pokémon) / `## The human stakes, said plainly` (serious) | yes | **Plain prose, no analogy.** House pattern — the validator checks for it |
| `## What an examiner digs into next` | yes | Or a specialty-appropriate equivalent. **Its position is the specialty's, not this table's** — see below |
| `## Sources` | yes | See below. Immediately before Scope and safety |
| `## Scope and safety` | yes | What this is not for, and local guidance |
| `## Where this stands, <Month Year>` | yes | What will date, and where the authority lives |

**On the order of the last four.** This table's order is the common case, not a rule. Specialties
differ — some put `## What an examiner digs into next` before `## Sources`, others after
`## Scope and safety` — and two writers found that out by matching their specialty against a table
that contradicted it. **Match the pairs already in your specialty.** The only hard constraint is
that `## Sources` comes immediately before `## Scope and safety`. The two halves of your own pair
must correspond section for section, so a reader can set them side by side.

Front matter, with `question` matching the catalogue row character for character:

```
---
id: "m042"
slug: your-slug-here
style: serious
category: nursing
difficulty: intermediate
question: "Your question text here?"
tags: [four, or, five, lowercase, tags]
---
```

Both answers at least 600 words. **Prose** wraps at 98 **characters** — an em dash is one
character, not three. Never wrap inside a fenced block, and **the 98 does not apply to Markdown
table rows**; long rows are normal here and a writer checking their own wrapping should not try to
break them.

## The clinical rules, which are not negotiable

* **Mainstream consensus only.** Where practice differs by country or institution, say so rather
  than picking one and asserting it.
* **Never invent a number.** No fabricated thresholds, doses, scores, intervals, sensitivities,
  prevalences or survival figures. Use a genuinely uncontroversial figure and name the authority,
  or **write the principle without the number** — which is usually the better answer anyway. An
  invented clinical number is a more serious defect than an invented Pokémon fact, and this
  repository already treats the latter as a correctness failure.
* **Never fabricate a citation.** No invented trial names, guideline numbers, DOIs, author-year
  references or document titles. The validator fails the build on all four patterns.
* **No answer addresses the reader as their clinician.** Explain what is done and why; never tell a
  reader what to take, stop or apply. The validator's regex is deliberately crude and will
  over-flag. Reword rather than argue with it. Known trap: `take \d+ mg` fires on an innocent
  sentence like "a trunk will take 100 g" — phrase quantities as *needs* or *is of the order of*.
* **Cut rather than soften.** A claim you cannot attribute to a nameable document comes out.

## Sourcing: attribution without quotation

**No medical authority is reachable from this environment.** `who.int`, `cdc.gov`, `nice.org.uk`,
`pubmed.ncbi.nlm.nih.gov`, `bnf.nice.org.uk`, `resus.org.uk`, `nhs.uk`, `medlineplus.gov`,
`cochranelibrary.com`, `dermnetnz.org` and `en.wikipedia.org` all return a 403 policy denial.
Several writers have verified this first-hand rather than taking it on trust, which is the right
instinct — do the same if you are about to assert it.

Web search returns aggregated summaries. A summary is the summariser's words. **Quoting one as a
guideline would be fabricating a medical citation.**

So every answer carries a `## Sources` section:

* headed by this line, **verbatim** (the validator checks for it):

  `**None of the sources below was retrieved.** They were unreachable from the environment this was written in, so every claim here rests on general professional knowledge and is attributed, not quoted. Open the document before relying on anything in this answer.`

* then the documents a reader should open, named precisely enough to find, with the issuing body
  named. **Standing documents for your specialty live in `SOURCES-<specialty>.md` in this
  directory — point at that file and list only what is specific to your answer.** That keeps the
  section short; near-identical 180-word blocks repeated a hundred times are waste. Early answers
  repeat the standing list inline instead; that is the older form, it is not the one to copy, and it
  is being swept. If the pairs you read for voice repeat it, follow this instruction and not them.
* **no quotation marks around source text, no DOIs, no author-year citations, no guideline codes,
  no URLs.**

Mark each load-bearing claim inline with its basis: *mechanism*, *definitional*, *consensus*, or
*country-dependent*. Declare your markers once per answer.

**Use those four words and the italic inline form**, which is what most of the corpus does. Two
divergences were tried and are not adopted: *guideline-dependent* for *country-dependent* (same
meaning, two spellings, no gain), and a declared `[M]` `[C]` `[D]` `[L]` bracket legend. The bracket
form is genuinely denser and the writer who used it offered to be normalised against; the reason to
keep the prose form is that the serious half is meant to read as prose a person could say aloud, and
a sentence carrying three bracketed codes does not. Where existing answers in your specialty use the
bracket form, leave them; new answers use the prose form.

**Pokémon facts are different, and you may source them properly.** `raw.githubusercontent.com`
reaches `pret/pokered`, `pret/pokeemerald` and `rh-hideout/pokeemerald-expansion`. Read the
decompilation rather than trusting memory — every writer so far who did caught at least one error
they would otherwise have shipped. Where a Pokémon figure is **not** from code, say so in the same
note rather than letting a blanket statement imply it was.

## Pokémon accuracy is a correctness bar, not a style

Every fact must be true of the actual games: legal movesets, real base stats, correct type
match-ups, real item and ability effects, correct character roles, level cap 100, stat stages ±6.
Generation-dependent figures must be pinned to their generation. **If you are not certain, use a
different fact.**

## Where the metaphor stops

`../SAFETY.md` has the list and it binds: prognosis, dying, bereavement, pain, suffering, distress,
mental-health crisis, self-harm, safeguarding, capacity, coercion, and any point where a reader
could be a patient rather than a student.

**No Pokémon stands in for a person.** Nothing maps fainting to death, a lost battle to dying,
reviving to resuscitation, or a type match-up to someone's chances. If a mapping needs a Pokémon to
be the patient, the mapping is wrong — find another or drop the metaphor for that section.

Whimsy about a mechanism is useful. Whimsy about an outcome is grotesque.

## The quality gate

```
python3 scripts/medical/validate.py          # blocking. Must print OK before every commit
python3 scripts/medical/build_dataset.py
python3 scripts/medical/score.py --detail m042
```

**Target at least 45.** The scorer ignores the mandated plain-prose sections, so you are measured on
the analogy-bearing body only — do not pad those sections and do not avoid writing them.

If an answer scores low, run `--detail` **before** rewriting. The scorer's vocabulary has blind
spots and several writers have found their central device invisible to it. That is a report, not a
rewrite. When an answer genuinely is thin, fix it by replacing an abstraction with a **specific that
makes the analogy more concrete** — a named species with the right stat, a real move with its real
accuracy — never by adding Pokémon words.

**If holding the line on taste or safety costs you score, take the lower score** and say so. That is
the one place in this repository where the metric is not the arbiter.

## Deliverables

1. `../answers/<specialty>/serious/mNNN-slug.md` and `../answers/<specialty>/pokemon/mNNN-slug.md`.
2. Your rows appended to `../questions/questions.tsv` — `id⇥slug⇥category⇥difficulty⇥question`.
3. `scripts/medical/build_dataset.py` re-run, outputs included.
4. Commit in your worktree as `alvations <alvations@gmail.com>`, no trailers. **Do not push.**

**The session scratchpad is shared between everyone writing at the same time, and it is not
isolated.** Three writers in one wave had helper scripts silently overwritten mid-task by a sibling
using the same filename, and one of them watched its own script print another writer's file list.
Nothing was lost because they noticed, which is luck. **Prefix every scratchpad filename with your
specialty and ID block** — `endo-m056-m060-reflow.py`, not `reflow.py` — and smoke-test any
reflow or rewrite helper as a no-op against an existing answer before pointing it at your own.

## Do not edit

`scripts/` anything, `../SAFETY.md`, `../README.md`, `CONVENTIONS.md`, the root `README.md`,
`CHANGELOG.md`, `DATASHEET.md`, `TERMINOLOGY.md`, and **both** `LEDGER.md` files — the root one and
`../LEDGER.md` — or `../../../for-agents/`.

**On `../LEDGER.md` specifically**, because three writers read that line three different ways and
all three readings were reasonable. Run `score.py --detail mNNN` to read your own score. Do **not**
run bare `score.py`, which rewrites the ledger. Several specialties are written concurrently in
sibling worktrees, so a ledger regenerated in your worktree reflects a partial tree, and five
writers doing it produces five conflicting ledgers. **Integration regenerates it centrally, once,
after all blocks land.** If you have already regenerated it, say so in your hand-back; it is not a
problem, it is just noise in your diff.

**`TERMINOLOGY.md` and `CONTRIBUTING.md` step 6 conflict**, and a writer was right to flag it. Step 6
asks for new Pokémon entities to be added to the glossary; this brief forbids editing it, because
seven writers editing one file in seven worktrees is a guaranteed conflict. **The brief wins:** list
the new entities in your hand-back and integration adds them. Report
vocabulary gaps, validator false positives and any defect you find in your hand-back instead — six
scorer bugs have been found that way and all six are now fixed.

**Never** mention Claude, Anthropic, AI assistance or any assistant model name, anywhere.

## Report back

IDs and slugs; each score; claims cut as unattributable and how many; any **clinical** claim a
reviewer should check first, in priority order; any **Pokémon** fact you were unsure about and how
you resolved it; validator false positives; scorer vocabulary gaps as exact strings; and anywhere
you wrote against this brief and why. **Writing against the brief is expected** — six of eight
writers in the machine-learning domain did, and in every case the corrected answer was better.
