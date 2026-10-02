# ELIPokémon — the medical domain

> Clinical and biomedical questions, each answered twice: once rigorously, once entirely
> through Pokémon.

**Read [SAFETY.md](SAFETY.md) first.** It says what this is for, what it is not for, and
where the Pokémon framing is deliberately set aside. The short version: this is revision
material for people already training in the field, it has had no clinical review, and it
is not for use in an emergency or for any decision about anyone's care.

## The seven specialties

| Specialty | Directory | Covers |
| --- | --- | --- |
| **Nursing** | `answers/nursing/` | Assessment, observations and early warning scores, medicines administration, wound and pressure-area care, fluid balance, infection prevention, handover and escalation, documentation |
| **Pharmacology** | `answers/pharmacology/` | Pharmacokinetics and pharmacodynamics, interactions, adherence, therapeutic drug monitoring, formulation, adverse reactions and reporting, stewardship |
| **General practice** | `answers/general-practice/` | Undifferentiated presentations, red flags and safety-netting, chronic disease review, screening, polypharmacy and deprescribing, referral thresholds, continuity |
| **Dermatology** | `answers/dermatology/` | Describing a lesion, morphology and distribution, the inflammatory conditions, skin of colour, dermoscopy principles, topical therapy and the quantities it needs |
| **Endocrinology** | `answers/endocrinology/` | Diabetes above all — the two mechanisms, insulin, monitoring, complications, the acute emergencies — plus thyroid, adrenal and the feedback-loop reasoning that makes endocrinology tractable |
| **Oncology** | `answers/oncology/` | Staging and grading, how systemic therapies differ, toxicity and its management, imaging and response assessment, screening and its harms, the multidisciplinary team |
| **Emergency** | `answers/emergency/` | The structured primary survey, triage, recognising the sick patient, first-aid reasoning, and why protocols are built the way they are |

## Layout

```
domains/medical/
├── SAFETY.md                      # read this first
├── questions/
│   ├── questions.tsv              # source of truth: id, slug, category, difficulty, question
│   └── index.json                 # generated
├── answers/
│   └── <specialty>/
│       ├── serious/m001-slug.md
│       └── pokemon/m001-slug.md
└── dataset/
    └── elipokemon-medical.jsonl   # generated
```

IDs are `m001`–`m100`, scoped to this domain. The `category` column holds the specialty,
which is also the answer's directory — so the catalogue row and the path are the same
fact stated twice, and the validator checks they agree.

**The record schema matches the machine-learning domain's exactly**, with an added
`domain` field, so the two JSONL files concatenate into one set.

## Usage

```bash
python3 scripts/medical/validate.py        # blocking gate; must print OK before any commit
python3 scripts/medical/build_dataset.py   # markdown -> index.json + the JSONL
python3 scripts/medical/score.py           # Pokémon-ness, grouped by specialty
python3 scripts/medical/score.py --detail m001
```

The scorer **imports** the machine-learning domain's `scripts/pokemon_score.py` rather
than copying it. The measure — does the Pokémon answer lean on named entities or on
generic furniture — is a property of the writing, not of the subject, so one vocabulary
serves both domains and a vocabulary fix lands in both at once.

## Conventions, in addition to the repository's

Everything in [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md) applies. These are the
additions, and the validator enforces the first two.

* **Every answer, both registers, carries a `## Scope and safety` section.** It names what
  the answer is not for and points at local guidance. No exceptions.
* **No answer addresses the reader as their clinician.** Teaching material explains what is
  done and why. It does not tell a reader what to take, stop or apply.
* **Numbers teach the principle.** A dose or a threshold appears to explain why it exists —
  why weight-based, why narrow, why that cut-off — not so it can be acted on. Every answer
  that carries one says to check the formulary.
* **The Pokémon answer explains mechanism and stops at outcome.** See
  [SAFETY.md](SAFETY.md#where-the-pokémon-framing-stops) for the list of places the
  metaphor drops entirely. Whimsy about a mechanism is useful; whimsy about dying is not.
* **Every answer carries a `## Sources` section** naming the documents that would settle
  its claims, with the issuing body named, headed by a verbatim statement that none of
  them was retrieved. **No quoted source text, no DOIs, no author-year citations, no
  guideline reference codes** — the validator fails the build on all four patterns. No
  medical authority is reachable from the build environment, and the only honest response
  is to say so in every answer. See
  [SAFETY.md](SAFETY.md#sourcing-and-why-there-are-no-quotations).
* **Each load-bearing clinical claim is marked inline** with what it rests on: consensus,
  country-dependent, or mechanism rather than guideline. A claim that could not be
  attributed to a nameable document was cut, not softened.
* **Every answer is dated**, in a `## Where this stands` line, because guidance moves.

## Status

Building toward the first 100. See [`../../CHANGELOG.md`](../../CHANGELOG.md) for the audit
trail and [`../../for-agents/`](../../for-agents/) for how the pipeline works.
