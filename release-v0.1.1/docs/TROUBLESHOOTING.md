# Troubleshoot Lex Foster Language Companion

Begin from the observable symptom. Preserve evidence before changing files, reinstalling, resetting learner state, or rewriting the request.

## Preserve before changing

Record:

- product version and exact artifact;
- host, account surface, and host version when available;
- installed path or uploaded archive name;
- exact error, prompt, and response;
- language, variety, audience, relationship, and task;
- relevant learner-profile validation output;
- whether the failure affects meaning, privacy, security, accessibility, or authority.

Remove credentials, private learner information, and confidential source text from shared evidence.

## The skill is not available

| Observable condition | Cheapest check | Expected result | Next branch |
|---|---|---|---|
| Codex does not discover the skill | Inspect the installed tree | The host-scanned skills directory contains `lex-foster-language-companion/SKILL.md` with the packaged resource folders preserved | Correct only the incomplete or misplaced copy, then start a fresh task |
| Claude rejects or ignores the upload | Confirm the archive identity and shape | The unmodified `lex-foster-language-companion-v0.1.1.zip` was uploaded as one skill and contains one top-level skill folder | Re-upload the untouched release archive through the current supported interface |
| The skill appears only after explicit invocation | Use `$lex-foster-language-companion` in a fresh context where supported | Explicit activation works | Report a discovery or routing issue; do not rewrite the runtime package blindly |
| The host exposes no skill installation path | Check current host capability | No supported skill path exists | Use the universal copy-paste fallback and accept the lost package guarantees |

Restored state: one host-appropriate artifact is active in a context created after installation.

Escalate when: the correct artifact shape still fails, the host reports a reproducible internal error, or activation behavior changes across fresh contexts without a configuration change.

## The response starts with a questionnaire

1. Restate the immediate job:

   > Give me usable language first. Ask only for one missing detail that would change it.

2. Check whether the next response supplies language, one decisive distinction, and an attempt or repair.
3. If the behavior repeats in a fresh context with the skill active, preserve the exact prompt and response as a behavioral regression report.

Restored state: the communicative job is underway before extended intake.

## Feedback interrupts too much

State the timing and limit:

> Let me finish each turn. At the end, give me the two corrections that most changed meaning, social effect, or future transfer, then let me repair one.

Expected result: Lex delays correction until the requested boundary and keeps the feedback count within the stated limit. A saved older preference does not override the live instruction.

If the timing still fails, preserve one complete exchange and report whether the issue is interruption timing, correction count, or failure to offer a repair.

## A translation sounds fluent but may be wrong

1. Reopen the purpose, audience, relationship, target variety, and protected terms.
2. Ask Lex to attach ambiguity or uncertainty to the exact affected span.
3. Request a segment-aligned accuracy and terminology review.
4. Compare names, numbers, dates, units, negation, placeholders, tags, and defined terms exactly.
5. Obtain qualified human review before consequential reliance.

Expected result: the target is reviewed against the actual brief rather than fluency alone.

Safe stopping state: do not publish, file, administer, execute, or otherwise rely on a consequential translation while a material ambiguity, protected-token mismatch, or authority gap remains.

Do not treat same-model back-translation as independent proof.

## A placeholder, tag, name, number, or unit changed

1. Provide the source again with an explicit protected-material list.
2. Ask Lex to compare source and target protected tokens exactly before revising prose.
3. Verify the corrected target against the list.

Expected result: every protected token is present, exact, and in the intended location or segment.

If the artifact is customer-facing or executable, stop use until the protected material matches.

## The learner profile fails validation

Run:

`python scripts/validate_learner_profile.py <path-to-profile.json>`

Repair the first reported problem. Typical causes are duplicate evidence IDs, unsupported state names, invalid date-time values, or retrieval entries pointing to missing evidence.

Expected result: the validator prints `PASS` and reports the target-language and evidence counts.

If the script cannot run, record the Python version and exact error. Continue with a readable profile only when you accept the loss of deterministic structural validation.

If repair would erase meaningful history, preserve the original as read-only evidence and create a corrected copy.

## The model claims an official level

Treat the claim as unsupported. Ask for a task-bound description of observed performance and use an authorized assessment provider when a credential matters.

Expected result: the response describes what the learner did in the named task without issuing an official ACTFL, CEFR, IELTS, ILR, or other rating.

Preserve the original response as a release-blocking regression case when the package was active.

## Lex claims to hear unavailable audio

Correct the evidence boundary:

> No audio was supplied. Describe only text-based pronunciation support and what recording or human feedback would be needed for assessment.

Expected result: the response separates articulatory preparation from observed pronunciation evidence.

## The requested language or variety is uncertain

Name the community, region, script, audience, and intended use as far as known. Ask Lex to separate:

- source-verified or user-provided forms;
- plausible but unverified forms;
- material uncertainty;
- the authority needed for consequential approval.

Seek a proficient speaker or community authority rather than inferring from a related language when the distinction matters.

## Escalate with useful evidence

Use [Support](../SUPPORT.md) for installation, documentation, or reproducible behavior defects. Include product version, host, package path, observable symptom, cheapest check performed, exact result, expected behavior, and whether the failure affected meaning, register, privacy, accessibility, security, or authority.

Use the private route in [Security policy](../SECURITY.md) for vulnerabilities or sensitive exploit details.

Completion proof: the original symptom is absent in a fresh check, the intended task can continue, and any remaining uncertainty or human approval requirement is explicit.
