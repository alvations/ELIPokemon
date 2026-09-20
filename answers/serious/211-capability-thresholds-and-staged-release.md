---
id: "211"
slug: capability-thresholds-and-staged-release
style: serious
category: frontier
difficulty: advanced
question: "A lab says its new model crossed a critical capability threshold and shipped it with restricted access. How should an engineer read that?"
tags: [preparedness, staged-release, dual-use, evaluation, deployment]
---

# The threshold is only as good as the eval that triggers it

In September 2026 OpenAI released GPT-6 Astra and stated it was the first of its models to reach
the **Critical** cybersecurity level of its Preparedness Framework — reporting a saturated score
on a benchmark that measures turning known vulnerabilities into working exploits, and that the
model surfaced previously unknown flaws during testing. The release was staged: a restricted
general version that declines in that area, with the advanced capability available to a limited
group and expanded through a defensive-use programme. It had also been delayed to add safeguards
after earlier incidents.

Set aside whether that was the right call. The structure is what an engineer should be able to
read.

## What a threshold framework is, and where it is load-bearing

```
   capability grows ──────────────────────────────────────────────►

   ┌──────────┬──────────────┬───────────────┬────────────────────┐
   │  Low     │   Medium     │     High      │    Critical        │
   └──────────┴──────────────┴───────────────┴────────────────────┘
        │            │              │                 │
        │            │              │                 └ commitments
        │            │              │                   attach here:
        │            │              │                   gated access,
        │            │              │                   extra controls
        │            │              └ mitigations required
        │            └ report and monitor
        └ ship normally

              ▲                              ▲
              │                              │
   the thresholds are chosen        the EVAL decides which box
   BEFORE anyone knows what         you are in. So the eval is a
   the capability will look like    SAFETY-CRITICAL COMPONENT.
```

Three structural weaknesses follow from that diagram, and they are not cynicism — they are the
open problems the people writing these frameworks will tell you about themselves.

**Elicitation.** A model's measured capability is a function of how hard you tried: scaffolding,
tools, fine-tuning, prompt search, how long you let it run. An under-elicited eval reads as a
lower tier. "We measured X" always means "we measured X *with this much effort*".

**Saturation destroys the trigger.** A 100% score does not mean the capability is complete; it
means the benchmark stopped measuring. Once an eval saturates it can no longer distinguish the
next model from this one, so a threshold resting on it has quietly stopped working and needs
replacing — and replacing it resets every historical comparison.

**Capability is not fixed at release.** Post-release fine-tuning, better scaffolds, tool access
and agent frameworks all raise the effective ceiling of a model whose weights never changed. The
tier was assigned to a checkpoint; your deployment is a checkpoint *plus* everything you wrapped
around it.

## What staged access actually trades

Restricting a dual-use capability slows down people who do not already have it — which includes
both attackers and defenders. The argument for going ahead is that defence is diffuse and slow,
so defenders need the lead time and the structured access; the argument against is that the
capability leaks, gets replicated by the open tier within a year or two, and the window was
smaller than it looked. Both are real. Anyone who finds this question easy has not understood it.

## What it means for you, concretely

* **If you deploy a gated model, you inherit its release conditions.** Acceptable-use terms,
  logging requirements and monitoring obligations become yours, and an agent framework that
  re-elicits a restricted capability is your problem, not the vendor's.
* **Your scaffolding changes the tier.** Give a model tools, memory and a loop and you have built
  something the model card did not evaluate.
* **Read the system card, not the launch post.** The tier assignment, the elicitation methodology
  and the known limitations live in the card.

## What an interviewer is listening for

That you locate the weight-bearing part — the eval — and can say why a saturated benchmark is a
governance problem rather than a good result. The strongest answers raise elicitation without
prompting, and notice that the tier belongs to the checkpoint while the risk belongs to the
deployed system.

## Where this stands, September 2026

The framework names, tiers and the specific release above are September 2026, drawn from public
announcements and coverage; the system card is the authority. Frameworks are being revised
continuously. The three structural weaknesses have survived every revision so far.
