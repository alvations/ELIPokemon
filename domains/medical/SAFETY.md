# Scope and safety — the medical domain

Read this before using anything in `domains/medical/`.

## If someone is unwell right now

**Call your local emergency number.** Nothing in this directory is for use during an
emergency, and reading it instead of calling for help would be worse than doing nothing.
The emergency-medicine questions here exist so that someone who is *already trained* can
revise the reasoning behind a protocol. They are not a protocol.

## What this is

Revision and explanation material, pitched at the level of someone who is already
training in or qualified for the field — a nursing student preparing for an exam, a
pharmacy undergraduate, a foundation doctor, someone revising for a specialty paper. Each
question has two answers: a rigorous one, and the same content re-explained through
Pokémon so the *mechanism* becomes concrete.

It is also, like the rest of this repository, a style-transfer and
explanation-quality dataset: two texts, the same propositional content, maximally
different register, constrained to agree.

## What this is not

Stated plainly, because this is the section that matters.

* **Not a clinical reference, and not a decision aid.** Do not use it to make a decision
  about any person's care, including your own.
* **Not a substitute for your local guidance.** Formularies, protocols, referral criteria,
  screening intervals and escalation thresholds differ by country, by region and by
  institution, and they change. Yours is the authority. This is not.
* **Not reviewed by clinicians.** There has been no medical review, no pharmacist review,
  and no citation checking against primary literature. It is written at the level of a
  strong exam answer, which is a different standard from a guideline.
* **Not a source of doses to administer.** Where a number appears it is there to teach
  why the number exists — why a drug is dosed by weight, why a range is narrow, why a
  threshold was chosen. **Check the formulary before anything reaches a patient.** An
  answer here agreeing with your memory is not confirmation.
* **Not current.** It describes consensus as of its writing date, which each answer
  states. Guidance moves.
* **Not about any real person.** There are no case histories, no patient data, and no
  identifiable details. Every scenario is constructed.

## Where the Pokémon framing stops

The analogy is for **mechanism**: how a drug distributes, why a feedback loop runs away,
why a staging system has the categories it has, what a dressing is actually doing. Pokémon
already contains resource systems, type interactions, status conditions and
accumulating-state mechanics, and pointing at them makes a mechanism concrete.

It is **set aside**, deliberately and without apology, for:

* prognosis, dying, and bereavement;
* pain, suffering, and distress;
* mental-health crisis, self-harm, and safeguarding;
* capacity, consent, and coercion;
* any point where a reader could be a patient rather than a student.

In those places the Pokémon answer drops the metaphor and says the thing directly. The
machine-learning half of this repository already does this for four questions about
sign language, endangered-language documentation, accessibility and biometrics; the
precedent is deliberate and the bar here is lower, because the stakes are higher.

Whimsy about a mechanism is useful. Whimsy about an outcome is grotesque. If any answer
in this directory crosses that line, it is a defect — please open an issue.

## Enforcement

`scripts/medical/validate.py` is blocking and checks, for every answer in both registers:

| Check | Why |
| --- | --- |
| A `## Scope and safety` section is present | An answer about clinical material that does not say what it is not for is incomplete |
| The specialty is one of seven named ones | A typo should fail, not create an eighth folder |
| No second-person directive about the reader's own treatment | Teaching material explains what is done; it does not instruct a reader about their care |
| Both registers exist, front matter matches, H1, minimum length, a diagram in the rigorous answer | Carried over from the machine-learning domain |

The third check is crude on purpose and will over-flag. A false positive costs a rewording;
a false negative ships an answer that reads like a prescription.

## Reporting an error

Open an issue. A factual error in this directory is more serious than one in the
machine-learning half, and will be treated that way.
