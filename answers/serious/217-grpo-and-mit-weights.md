---
id: "217"
slug: grpo-and-mit-weights
style: serious
category: open-weights
difficulty: intermediate
question: "DeepSeek ships MIT-licensed weights trained with GRPO. What does that actually let a downstream team do?"
tags: [grpo, reinforcement-learning, licensing, open-weights, deepseek]
---

# GRPO removes the critic. MIT removes the lawyer. Neither removes the work.

Two independent facts get quoted as one. **GRPO** —
[Group Relative Policy Optimization](https://arxiv.org/abs/2402.03300), introduced in
DeepSeekMath and used through V3 and [R1](https://arxiv.org/abs/2501.12948) — is a policy-gradient
method that throws away PPO's value network and estimates the baseline from a *group* of samples
for the same prompt. **MIT** is a permission grant over the weights file. The first tells you how
the model was shaped. The second tells you what you may do with the artefact. Neither tells you
whether it will work on your problem, and the second does not even mean what most people assume.

## GRPO, in one picture

```
   PPO                                  GRPO
   ┌────────────────────────┐           ┌──────────────────────────────────┐
   │ policy   (N params)    │           │ policy   (N params)              │
   │ critic   (≈N params) ◄─┼─ trained  │ sample G outputs for the SAME    │
   │          baseline      │           │ prompt: o₁ … o_G, score each     │
   └────────────────────────┘           │                                   │
     memory ≈ 2 models                  │ Aᵢ = (rᵢ − mean(r)) / std(r)      │
                                        │        ▲                          │
                                        │        └ baseline is the group.   │
                                        │          No second network.       │
                                        └──────────────────────────────────┘

   Why it works here: the reward is CHEAP and VERIFIABLE.
      maths → check the final answer     code → run the tests
      format → match the tag structure
   You can afford G=8 or 64 rollouts of one prompt, so the group mean is a
   free, unbiased-enough baseline. Take that away — put a learned preference
   model in the reward slot — and the economics that justify GRPO weaken.
```

R1's pipeline is worth knowing in outline because it answers the obvious follow-up. **R1-Zero**
was pure RL on the base model with rule-based rewards and *no* supervised fine-tuning at all. It
produced long chains of thought and self-verification on its own — and output that mixed
languages and was hard to read. **R1** therefore prepends a small "cold start" SFT stage, then
reasoning RL, then rejection-sampling SFT on the improved model, then a final RL pass covering
non-reasoning behaviour. The lesson is not "RL alone works"; it is "RL alone finds the
capability, and a little supervision is what makes it usable".

Known problems, because an interviewer will ask: dividing by the group standard deviation
introduces a length and difficulty bias that [Dr. GRPO](https://arxiv.org/abs/2503.20783) and
others correct; entropy collapses if you push too long; and outside verifiable domains you are
back to reward hacking with none of GRPO's advantages.

Reported descriptions of V4's post-training take this further: independent specialist models per
domain, each SFT'd and then RL'd with GRPO against domain-tailored rewards, then consolidated
into one student by on-policy distillation from whichever specialist fits the context — with the
specialists scoring their own rollouts rather than a separate reward model being trained. That is
secondary coverage, not a first-hand reading.

## What MIT weights actually grant

```
   ┌─────────── MIT gives you ─────────────┬──────── MIT does NOT give you ──────────┐
   │ run it anywhere, incl. air-gapped     │ the training data                       │
   │ modify, fine-tune, quantise, distil   │ the training code at reproduction       │
   │ redistribute, including commercially  │   fidelity                              │
   │ RE-LICENSE your derivative            │ any warranty or indemnity               │
   │ sell the outputs                      │ provenance for what is inside it        │
   │ no MAU threshold, no acceptable-use   │ an exemption from the EU AI Act, export │
   │   clause, no naming requirement       │   controls, or your customer contracts  │
   │ keep the copyright notice — that is   │ safety work: you now own the alignment  │
   │   the entire obligation               │   of whatever you shipped               │
   └───────────────────────────────────────┴─────────────────────────────────────────┘
```

Two comparisons make the point. Llama's community licence carries a monthly-active-user
threshold and a naming requirement; Gemma ships under terms of use with a prohibited-use policy
attached. Those are not open-source licences and a legal team will treat them differently. Going
the other way, Apache-2.0 includes an **express patent grant** and MIT does not — so for some
buyers Apache is the safer of the two despite MIT being the more permissive-sounding.

The practical consequence of MIT weights for a downstream team is mostly about **control**: you
can run it in a jurisdiction of your choosing, freeze a version forever, fine-tune it into
something the original lab would not have shipped, and never be deprecated out of your own
product. That is the real value, and it has nothing to do with GRPO.

## What an interviewer is listening for

That GRPO's saving is the critic, and that the group-relative baseline is only affordable because
verifiable rewards are cheap. Then that R1-Zero shows RL can find the capability and cold-start
SFT is what makes it usable. On licensing, the tell is whether you know MIT's obligation is
attribution and nothing else, and whether you notice the missing patent grant. The strongest
answers say plainly that an open licence transfers the safety and compliance work to you.

## Where this stands, September 2026

GRPO, R1's pipeline and the MIT licensing of V3 and R1 are from primary sources and are stable.
The V4 line is **reported** as MIT — V4-Pro, V4-Flash and the September 2026 V4.1-Flash all
appear in coverage under MIT — but arxiv.org, DeepSeek's documentation host and Hugging Face are
blocked by this environment's egress proxy, so no `LICENSE` file was read first-hand. Licences
change between a preview and a general-availability release, and a licence claim is the cheapest
of all claims to check: open the repository and read the file before you build on it.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing** — the papers are named because the results are theirs, not because
they were re-read. Resolve every identifier before you cite it.
