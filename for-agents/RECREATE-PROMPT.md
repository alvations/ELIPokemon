# Recreating this dataset

Two ways in: build it from scratch with a Claude model, or seed the question list from
public Hugging Face datasets and generate only the answers. Both end at the same invariant —
paired answers that agree, Pokémon facts that are true, named entities doing real work.

---

## Part 1 — Build it from scratch

### The scaffold, before any answers

Do these in order. Content last.

```bash
mkdir -p questions answers/serious answers/pokemon scripts prompts dataset for-agents
printf '__pycache__/\n*.py[cod]\n.venv/\nvenv/\n' > .gitignore
```

1. `questions/questions.tsv` with header `id  slug  category  difficulty  question`.
2. `scripts/validate.py` — the gate, written *before* the content it validates.
3. `scripts/build_dataset.py` — TSV plus front matter to `questions/index.json` and
   `dataset/elipokemon.jsonl`.
4. Only then start writing pairs.

Writing the validator first is not ceremony. It is the difference between catching a
mislabelled `style:` on file 7 and catching it on file 190.

### The generation prompt

Give the model **one question at a time**. Batching pairs degrades both answers: the model
starts reusing the same Pokémon for different concepts and stops checking the game facts.

Set `{{QUESTION}}`, `{{SLUG}}`, `{{ID}}`, `{{CATEGORY}}` from the TSV row.

````text
---SYSTEM---
You are writing one entry for ELIPokémon, a dataset of machine-learning and LLM interview
questions where every question has two answers: a rigorous technical answer, and the same
content re-explained entirely through Pokémon.

You are writing BOTH answers for one question, serious first. The Pokémon answer is a
translation of the serious answer, not an independent piece. Every claim in the Pokémon
answer must correspond to a claim in the serious answer.

THREE HARD CONSTRAINTS.

1. TECHNICAL CORRECTNESS. The serious answer is what a strong candidate would say to a
   senior interviewer: precise, current, and willing to name trade-offs and failure modes.
   No hand-waving, no marketing register.

2. POKÉMON ACCURACY IS A CORRECTNESS BAR, NOT A STYLE. Every Pokémon fact you state must be
   true of the actual games. A species must be able to legally learn any move you give it.
   Type match-ups, base stats, item effects, ability effects, and character roles (Gym
   Leader vs Elite Four vs Champion) must be right. Levels cap at 100; stat stages cap at
   ±6. If you are not certain a fact is true, use a different fact — do not approximate. An
   invented Pokémon fact is as serious a defect as an invented claim about softmax.

3. NAMED ENTITIES BEAT GENERIC FURNITURE. "Brock's Onix, with 41 HP" does analogical work
   that "a Gym Leader's Pokémon" does not. Prefer real species, moves, items, abilities,
   characters and places over unnamed Trainers, Gyms and battles. But only where the real
   fact genuinely fits: the best analogies are ones where Pokémon ALREADY contains the
   structure you need, so you are pointing at it rather than dressing something up as it.
   Never keyword-stuff. A forced species name is worse than an honest abstraction.

FORMAT. Emit exactly two markdown documents, separated by a line containing only
`===SPLIT===`. Each opens with YAML front matter, then an H1, then the body. Wrap prose at
98 columns. Do not wrap fenced code blocks.

Serious answer front matter:
---
id: "{{ID}}"
slug: {{SLUG}}
style: serious
question: {{QUESTION}}
---

Pokémon answer front matter: identical, but `style: pokemon`.

The serious answer MUST contain at least one fenced code block holding an ASCII diagram of
the mechanism — data flow, shapes, or the trade-off being described. Align it by column; it
is checked.

STRUCTURE. Serious: the direct answer, the mechanism, the ASCII diagram, the failure modes,
and what an interviewer is actually listening for. Pokémon: the same skeleton, same order,
every abstraction bound to a named entity. Both at least 600 words.

---USER---
Question {{ID}} ({{CATEGORY}}): {{QUESTION}}

Write both answers.
````

### The API call

Matches `scripts/revise.py`, which is the working reference implementation:

```python
from anthropic import Anthropic

client = Anthropic()          # resolves ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN

with client.beta.messages.stream(
    model="claude-opus-5",
    max_tokens=64000,
    thinking={"type": "adaptive"},          # it must hold both answers plus the constraints
    betas=["server-side-fallback-2026-07-01"],
    fallbacks="default",                    # a policy decline retries inside the same call
    system=system_prompt,
    messages=[{"role": "user", "content": user_prompt}],
) as stream:
    message = stream.get_final_message()

if message.stop_reason == "refusal":
    raise SystemExit("declined; do not retry the same prompt verbatim")

text = "".join(b.text for b in message.content if b.type == "text")
```

Streaming is required at this `max_tokens`. A cheaper model is fine for a first pass, but
budget a stronger one for the Pokémon accuracy audit — that pass is where the model has to
*know things*, not just write well.

### The loop, per question

```bash
python3 scripts/generate.py --id 001          # writes both files
python3 scripts/validate.py                   # must print OK
python3 scripts/build_dataset.py
git add questions/questions.tsv answers/serious/001-*.md answers/pokemon/001-*.md \
        questions/index.json dataset/elipokemon.jsonl
git commit -m "Add answer pair for Q001: attention mechanisms"
```

The TSV row and its two answer files go in **the same commit**. A row without answers breaks
validation for every concurrent worker.

### Then, and this is the part that is easy to skip

**Audit for Pokémon accuracy as a separate pass, with a separate prompt.** Generation and
verification are different tasks and the model is better at the second one when it is not
also trying to be charming. Twenty-one errors survived the generation constraints in the
original build; every one of them was caught by re-reading with only the question "is this
true of the actual games?" in mind.

```text
Below is one Pokémon answer from a dataset. Ignore whether it is a good analogy. Check ONLY
whether every Pokémon fact in it is true of the actual games: legal movesets, base stats,
type match-ups, item and ability effects, character roles, level and stat-stage caps.

For each error, quote the exact claim, state the true fact, and propose a replacement that
preserves the analogy. If the true fact makes a BETTER analogy than the incorrect one, say
so — that is usually the right fix. If there are no errors, say so and stop.
```

### Then the scorer, the ledger, and the waves

`scripts/pokemon_score.py`, `LEDGER.md`, and the wave loop are described in
[`HOW-IT-WAS-BUILT.md`](HOW-IT-WAS-BUILT.md#7-measuring-pokémon-ness). The scorer must be
deterministic — no model in the loop — or the ledger diff stops meaning anything.

Read [`LEARNINGS.md`](LEARNINGS.md#the-score-is-a-search-tool-not-a-target) before starting
the waves. The metric is a search tool for finding answers worth re-reading. Optimising
against it past the point of diminishing returns produces a corpus that scores well and
reads worse.

---

## Part 2 — Seeding from Hugging Face datasets

Writing 100 good interview questions is real editorial work. If you would rather ground the
question list in something external, pull candidates from public datasets and curate down.

> **Verify every dataset identifier before you use it.** Names, configs, splits and column
> schemas on the Hub change, and repositories get renamed, gated or removed. Resolve each ID
> against the Hub and inspect the actual columns rather than trusting a name from memory —
> this document included. Check the licence too: a permissive licence for *reading* is not
> the same as a licence to redistribute derived text.

```bash
pip install datasets huggingface_hub
```

```python
from huggingface_hub import HfApi

api = HfApi()
for d in api.list_datasets(search="machine learning interview", limit=25):
    print(d.id, d.downloads, getattr(d, "tags", None))
```

Useful families to search, described by what they contain rather than by exact ID, because
the IDs are what drift:

| What you want | What to search the Hub for |
| --- | --- |
| ML/DS interview Q&A | `interview questions machine learning`, `data science interview` |
| Exam-style ML questions with grounded answers | `MMLU` subsets (`machine_learning`, `college_computer_science`), `sciq` |
| Real questions people actually ask | Stack Exchange dumps (`stackexchange`, `cross-validated`, `datascience`) |
| Paper-grounded technical Q&A | `qasper`, `arxiv qa` |
| Curated instruction pairs to mine topics from | `dolly`, `oasst`, `alpaca`-family sets |

Then curate — the raw sets are not the deliverable:

```python
from datasets import load_dataset

ds = load_dataset("<verified/id>", split="train")
print(ds.column_names, len(ds))     # ALWAYS inspect before assuming a schema

seen, rows = set(), []
for r in ds:
    q = (r.get("question") or r.get("instruction") or "").strip()
    if len(q) < 25 or q.lower() in seen:
        continue
    seen.add(q.lower())
    rows.append(q)
```

Curation rules that produced the original 100:

* **Deduplicate semantically, not just by string.** Embed the questions and drop near
  duplicates; Hub Q&A sets are full of the same question reworded.
* **Balance by category, deliberately.** Transformers, alignment, fine-tuning, inference,
  retrieval, agents, evaluation, safety, classical fundamentals, systems. A set that is 60%
  transformer internals is not an interview set.
* **Keep a fundamentals tail.** Bias–variance, regularisation, calibration. Interviews still
  ask them and a pure-2020s set ages badly.
* **Drop anything that cannot carry a diagram.** If the serious answer has no mechanism to
  draw, it is a definition, not an interview question.
* **Rewrite every question in your own voice** before it enters the TSV. Scraped phrasing is
  inconsistent, and rewriting is also where you notice duplicates the embedding missed.

Then hand the curated TSV to Part 1 and generate the answers exactly as above. Seeding
changes where the questions come from; it changes nothing about the invariant.

---

## The checklist you actually need

```
[ ] .gitignore before the first commit
[ ] validate.py written before the content
[ ] one question per generation call, serious answer first
[ ] TSV row + both answer files in the same commit
[ ] validate.py prints OK before every commit
[ ] a separate Pokémon-accuracy audit pass, with its own prompt
[ ] scorer is deterministic; scorer changes commit separately from content changes
[ ] one wave, one commit
[ ] targeted `git add` paths whenever anything else is working in the tree
[ ] Hugging Face dataset IDs verified against the Hub, licences checked
```
