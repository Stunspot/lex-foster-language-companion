<p align="center">
  <img src="docs/assets/lex-foster-language-companion-readme.webp" alt="Lex Foster Language Companion — an AI language tutoring system for agents" width="100%">
</p>

# Lex Foster Language Companion

**An installable language tutoring and translation Augment for AI agents.**

Lex Foster Language Companion adds practical language teaching, conversation rehearsal, translation, localization, pronunciation and script support, cultural-context guidance, and optional learner-owned continuity to Codex, Claude, or another capable text model.

The product is the **language capability**. Lex Foster is the integrated practitioner voice that keeps teaching, translation, correction, and intercultural judgment coherent; the persona supports the work rather than replacing it with mascot theater.

[Project site](https://stunspot.github.io/lex-foster-language-companion/) · [Start in five minutes](START-HERE.md) · [Documentation map](DOCUMENTATION.md) · [Install](release-v0.1.0/docs/INSTALLATION.md) · [Release notes](RELEASE-NOTES-v0.1.0.md) · [Trust and limits](release-v0.1.0/docs/LIMITATIONS.md)

## What the skill gives an agent

- **Task-native tutoring.** Start from the message, conversation, text, misunderstanding, or ability the learner actually needs.
- **Transfer-driven correction.** Prioritize the choice that most affects meaning, relationship, naturalness, or reuse; then let the learner repair it.
- **Purpose-fit translation.** Preserve audience, relationship, variety, register, terminology, ambiguity, locale, placeholders, and protected formatting.
- **Conversation rehearsal.** Play a plausible counterpart instead of feeding the learner both sides of the exchange.
- **Pronunciation and script support.** Explain articulation, stress, rhythm, IPA, romanization, spelling, and script distinctions within the evidence available to the host.
- **Culture with boundaries.** Distinguish grammar, convention, community tendency, relationship choice, and personal preference.
- **Inspectable continuity.** Optionally store learner-owned evidence of what was new, supported, independent, or transferred—without inventing an official proficiency score.

The teaching loop is:

**encounter → attempt → focused feedback → repair → variation → later retrieval**

## Install

| Host | Artifact | First move |
|---|---|---|
| **Codex** | [`release-v0.1.0/codex/lex-foster-language-companion/`](release-v0.1.0/codex/lex-foster-language-companion/) | Copy the complete folder into the directory your Codex installation scans for skills, start a fresh task, then invoke `$lex-foster-language-companion`. |
| **Claude** | [`release-v0.1.0/claude/lex-foster-language-companion-v0.1.0.zip`](release-v0.1.0/claude/lex-foster-language-companion-v0.1.0.zip) | Upload the ZIP as one skill, enable it if the current interface requires that, then begin with a real language task. |
| **Other capable text models** | [`universal-copy-paste-companion.md`](release-v0.1.0/codex/lex-foster-language-companion/fallbacks/universal-copy-paste-companion.md) | Paste the fallback prompt into a new conversation and place your language request beneath it. |

The [installation guide](release-v0.1.0/docs/INSTALLATION.md) gives prerequisites, observable results, recovery, and completion checks.

## Try one useful turn

```text
Use $lex-foster-language-companion.

I need to tell my new neighbor in Mexican Spanish that their music is carrying into my apartment, but I want to stay friendly. Give me usable language first, explain the one choice that most affects the tone, then play the neighbor so I can rehearse their likely reply.
```

A strong first turn gives usable language before extended intake, makes the decisive relationship choice visible, and creates a small learner attempt or repair. It should not begin with a placement ritual, a generic vocabulary list, or an unsolicited lecture on Spanish politeness.

For the shortest complete path, use [START-HERE.md](START-HERE.md).

## Translation is part of the same capability

Lex translates what a text is **doing**, not only what its words denote. For nontrivial work, the skill can establish purpose, audience, relationship, target variety, register, protected terms, formatting constraints, source ambiguity, and the consequence of error.

For legal, medical, immigration, safety-critical, financial, publication-grade, certified, or community-governed language work, Lex can clarify the brief, draft, compare, preserve terminology, expose uncertainty, and prepare a reviewer handoff. Qualified human authority remains qualified human authority.

Use the [translation guide](release-v0.1.0/docs/TRANSLATION-GUIDE.md) for the full workflow.

## Documentation by task

- [Choose the right page](DOCUMENTATION.md) for installation, tutoring, translation, learner state, recovery, reference, evidence, or maintenance.
- [Read the release notes](RELEASE-NOTES-v0.1.0.md) for customer-facing scope, impact, migration, and known limits.
- [Maintain the documentation](release-v0.1.0/docs/MAINTENANCE.md) through explicit source authority, review triggers, verification, and safe handoff.
- [Report a documentation defect](SUPPORT.md) with the affected page, task, version, observed result, and preferred outcome.

## What is included

- one complete Codex skill folder;
- one upload-ready Claude skill ZIP;
- the integrated Lex practitioner persona;
- selective references for tutoring, correction, learner modeling, pronunciation, culture, translation, privacy, and high-stakes boundaries;
- learner-profile, language-mission, session-recap, and translation-brief templates;
- four worked demonstrations and twelve behavioral eval cases;
- deterministic package and learner-profile validators using the Python standard library;
- installation, quick-start, user, translation, learner-state, troubleshooting, removal, maintenance, accessibility, and validation documentation;
- a universal copy-paste fallback for hosts without skill installation.

## Repository map

| Path | Purpose |
|---|---|
| [`START-HERE.md`](START-HERE.md) | Five-minute public onboarding and success checks |
| [`DOCUMENTATION.md`](DOCUMENTATION.md) | Task-oriented documentation hub and evidence map |
| [`RELEASE-NOTES-v0.1.0.md`](RELEASE-NOTES-v0.1.0.md) | Customer-facing release communication and known limits |
| [`release-v0.1.0/`](release-v0.1.0/) | Versioned customer release with Codex, Claude, documentation, and provenance |
| [`source/`](source/) | Canonical maintainer source for the current Augment |
| [`dist/`](dist/) | Built distribution staging |
| [`development/`](development/) | Capability map and build-state records |
| [`verification/`](verification/) | Executed checks, documentation review, source ledger, and release evidence |
| [`docs/`](docs/) | GitHub Pages source and shared public artwork |

## Trust and evidence

Version 0.1.0 passed retained deterministic package, metadata, JSON, learner-profile, distribution, and archive checks. The repository also carries behavioral eval definitions for tutoring, translation, prompt injection, low-resource language, official assessment, absent audio, and consequential translation boundaries.

Those records establish package structure and selected deterministic behavior. They do **not** prove equal competence across languages, successful installation in every host version, professional translation approval, formal accessibility conformance, or a guaranteed route to fluency.

- [Capability matrix](release-v0.1.0/docs/CAPABILITY-MATRIX.md)
- [Validation and evaluation](release-v0.1.0/docs/VALIDATION-AND-EVALUATION.md)
- [Limits and non-claims](release-v0.1.0/docs/LIMITATIONS.md)
- [Current public-surface accessibility statement](ACCESSIBILITY.md)
- [Security policy](SECURITY.md)

## Publisher and license

Lex Foster Language Companion is a free Collaborative Dynamics public-service Augment. Copyright 2026 Collaborative Dynamics. Released under the [MIT License](LICENSE).

[Contribute](CONTRIBUTING.md) · [Get support](SUPPORT.md) · [Report a security issue](SECURITY.md)
