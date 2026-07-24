# Try Lex Foster Language Companion in five minutes

Goal: install the correct version 0.1.0 artifact, reach one useful language turn, and recognize whether the intended capability activated.

Audience: a first-time user of Codex, Claude, or another capable text model. No placement score, curriculum plan, or language-teaching background is required.

## Before you begin

You need:

- permission to install or upload a skill in your chosen host, or access to the copy-paste fallback;
- one real message, conversation, text, pronunciation question, translation, or learning goal;
- the version 0.1.0 release in this repository;
- authority to approve any consequential use that follows.

Do not include passwords, credentials, unnecessary personal information, private learner records, or confidential source text.

Starting state: the skill is not yet installed in the fresh task or conversation you will use for this check.

## 1. Choose the artifact for your host

- **Codex:** use `release-v0.1.0/codex/lex-foster-language-companion/`.
- **Claude:** use `release-v0.1.0/claude/lex-foster-language-companion-v0.1.0.zip`.
- **Another capable text model:** use `fallbacks/universal-copy-paste-companion.md` inside the unpacked Codex skill folder.

Expected result: you have exactly one artifact intended for the host. Do not upload the whole repository as a Claude skill or copy the Claude ZIP itself into a Codex skills directory.

If you cannot identify the correct artifact, stop without moving files and use the [installation guide](release-v0.1.0/docs/INSTALLATION.md).

## 2. Install and start from a fresh context

Follow the [installation procedure](release-v0.1.0/docs/INSTALLATION.md), then start a new task or conversation so the host can discover the skill cleanly.

Expected result: the host exposes one Lex Foster Language Companion skill or the fallback prompt is active in the new conversation.

If the skill is missing, preserve the host version, artifact path, exact error, and installed tree before changing anything. Continue with [Troubleshooting](release-v0.1.0/docs/TROUBLESHOOTING.md#the-skill-is-not-available).

## 3. Ask for a real communicative job

In Codex, send:

```text
Use $lex-foster-language-companion.

I need to introduce myself at a Brazilian jiu-jitsu gym in Portuguese. I am a beginner and want to sound friendly rather than formal. Give me something usable first, explain the choice that most affects the relationship, then play the other person so I can answer.
```

In Claude or the copy-paste fallback, omit the skill handle when the host does not use one.

Expected result: the response begins with useful language or an immediately useful attempt—not a course tree or long intake questionnaire.

## 4. Verify first value

Successful activation should produce:

- language you can use now;
- a visible choice about meaning, tone, relationship, variety, or register;
- a small attempt, variation, or repair for you to make;
- only the context questions that materially change the result;
- uncertainty attached to the affected phrase rather than buried in a disclaimer pile.

The intended capability did not activate cleanly if the response begins with a long questionnaire, a generic vocabulary list, an official proficiency claim, or a lecture that never lets you use the language. Use [The response starts with a questionnaire](release-v0.1.0/docs/TROUBLESHOOTING.md#the-response-starts-with-a-questionnaire).

## 5. Test repair and reuse

Reply in the target language. After feedback, ask:

```text
Change one detail in the situation and make me use that correction again.
```

Expected result: the turn moves through attempt, focused feedback, repair, and changed-cue reuse rather than merely displaying a corrected answer.

## 6. Test translation fit

```text
Translate this into Canadian French for a warm but professional customer-service email. Preserve the product name Northstar and the placeholder {ticket_id}. Give me the target text first, then identify any source ambiguity that could change the translation.
```

Expected result: names and placeholders remain exact; audience, register, locale, and uncertainty remain visible.

For consequential use, stop before reliance and follow [When qualified human review matters](release-v0.1.0/docs/TRANSLATION-GUIDE.md#when-qualified-human-review-matters).

## 7. Confirm completion

The first-run path is complete when:

- the correct artifact is installed or the fallback is active;
- one real task produced usable language;
- you made or repaired at least one learner contribution;
- you can name one important product boundary;
- you know the next page for deeper use or recovery.

Safe stopping state: keep the original release artifact, preserve any error evidence, and avoid deleting another skill or changing global host configuration when the result is uncertain.

## Continue by task

- [Documentation map](DOCUMENTATION.md)
- [Tutoring, rehearsal, pronunciation, culture, and continuity](release-v0.1.0/docs/USER-GUIDE.md)
- [Translation and localization](release-v0.1.0/docs/TRANSLATION-GUIDE.md)
- [Learner-owned state](release-v0.1.0/docs/LEARNER-STATE.md)
- [Troubleshooting by observable symptom](release-v0.1.0/docs/TROUBLESHOOTING.md)
- [Capability matrix](release-v0.1.0/docs/CAPABILITY-MATRIX.md)
- [Validation and evidence boundary](release-v0.1.0/docs/VALIDATION-AND-EVALUATION.md)
- [Package reference](release-v0.1.0/docs/PACKAGE-REFERENCE.md)
