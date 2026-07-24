# Troubleshoot Lex Foster Language Companion

Preserve the host version, installed artifact, exact error, input, and relevant learner state before changing or reinstalling anything. Remove private details from shared evidence.

## The skill does not activate

### Check the installation shape

- Codex must end at `.codex/skills/lex-foster-language-companion/SKILL.md`.
- Claude must receive `lex-foster-language-companion-v0.1.0.zip` as one uploaded skill.
- The Claude ZIP must contain one top-level `lex-foster-language-companion` folder with `SKILL.md` directly beneath it.

### Check from a fresh context

Start a new task or conversation and use the explicit skill name where the host supports it:

`$lex-foster-language-companion Help me rehearse this conversation…`

If explicit activation works but natural language does not, record that as a discovery or routing issue rather than changing the runtime package blindly.

## Lex starts with a questionnaire

Restate the immediate job and ask for first value:

> Give me the usable language first. Ask only for one missing detail that would change it.

If the behavior repeats, preserve the exact prompt and response as a behavioral regression report.

## Feedback interrupts too much

State the timing and limit:

> Let me finish each turn. At the end, give me the two corrections that most changed meaning, social effect, or future transfer, then let me repair one.

A saved older preference does not override this live instruction.

## A translation sounds fluent but may be wrong

1. Reopen the purpose, audience, relationship, target variety, and protected terms.
2. Ask for ambiguity to be attached to exact spans.
3. Request a segment-aligned accuracy and terminology review.
4. Preserve names, numbers, dates, units, negation, placeholders, and tags.
5. Obtain qualified human review before consequential reliance.

Do not use same-model back-translation as independent proof.

## A placeholder or tag changed

Provide the source again with a protected-material list. Ask Lex to compare source and target tokens exactly before revising wording. If the artifact is customer-facing or executable, stop use until the protected tokens match.

## The learner profile fails validation

Run:

`python scripts/validate_learner_profile.py <path-to-profile.json>`

Repair the first reported problem. Typical causes are duplicate evidence IDs, unsupported state names, invalid date-time values, or retrieval entries pointing to missing evidence.

If the script itself cannot run, record the Python version and exact error. Continue with a readable profile only if you accept the loss of deterministic structural validation.

## The model claims an official level

Treat the claim as unsupported. Ask for a task-bound description of observed performance and use an authorized assessment provider when a credential matters. Preserve the response as a release-blocking regression case if the package was active.

## Lex claims to hear unavailable audio

Correct the evidence boundary:

> No audio was supplied. Describe only text-based pronunciation support and what recording or human feedback would be needed for assessment.

## The requested language or variety is uncertain

Name the community, region, script, and intended audience as far as known. Ask Lex to separate known forms, plausible but unverified forms, user-provided forms, and material uncertainty. Seek a proficient speaker or community authority rather than inferring from a related language.

## Escalate with useful evidence

Open a GitHub issue with product version, host, package path, exact input, exact response, expected behavior, and whether the failure affected meaning, register, privacy, accessibility, or authority. Use synthetic data for sensitive cases.