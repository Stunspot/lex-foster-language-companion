# Lex Foster Language Companion version 0.1.0 release notes

Release date: July 24, 2026  
Publisher: Collaborative Dynamics  
License: MIT

## What this release adds

Version 0.1.0 packages one installable language capability for AI agents. It supports:

- task-native tutoring from a real message, conversation, text, or goal;
- conversation rehearsal with a plausible counterpart;
- focused correction followed by learner repair and changed-cue reuse;
- purpose-fit translation and localization;
- pronunciation and script preparation within the evidence available to the host;
- cultural and protocol guidance scoped to community, relationship, role, and setting;
- optional learner-owned continuity through a JSON profile or session recap;
- explicit limits for official assessment, unavailable audio, low-resource language, and consequential translation.

## Customer artifacts

| Host path | Artifact | Customer action |
|---|---|---|
| Codex | `release-v0.1.0/codex/lex-foster-language-companion/` | Copy the complete folder into the directory Codex scans for skills. |
| Claude | `release-v0.1.0/claude/lex-foster-language-companion-v0.1.0.zip` | Upload the ZIP as one skill. |
| Other capable text models | `fallbacks/universal-copy-paste-companion.md` inside the unpacked skill | Paste the prompt into a new conversation. |

Use the [installation guide](release-v0.1.0/docs/INSTALLATION.md) for prerequisites, expected results, recovery, and completion proof.

## Upgrade and migration

This is the first public version, so there is no earlier release to migrate. Keep one version in each installed skill root. Do not merge files from several versions.

Learner profiles are separate user-owned files. Installing or removing the skill does not automatically create, migrate, or delete them.

## Evidence available

Retained construction records report deterministic package, metadata, JSON, learner-profile, distribution, and archive checks. The release also includes twelve behavioral eval definitions.

Those records do not prove successful installation in every host, equal quality across languages, durable learner outcomes, professional translation approval, representative-user accessibility, or formal WCAG conformance. Read [Validation and evaluation](release-v0.1.0/docs/VALIDATION-AND-EVALUATION.md) and the [Host matrix](release-v0.1.0/HOST-MATRIX.md) before extending the claim.

## Known limits

- The active model determines much of the language coverage and quality.
- Text-only use cannot assess unheard pronunciation or listening performance.
- The product does not issue official ACTFL, CEFR, IELTS, ILR, or other proficiency credentials.
- Cultural guidance is context-bound rather than a universal rule about a population.
- Consequential legal, medical, immigration, safety, financial, certified, publication, or community-governed language work may require a qualified human.
- Host installation, discovery, activation, resource loading, Python availability, persistence, and UI labels remain host-specific unless separately observed.

## Documentation maintenance note

The public documentation was reorganized after the initial release around Hesperos task, recovery, accessibility, evidence, and lifecycle doctrine. That maintenance changes customer guidance and navigation; it does not alter the version 0.1.0 runtime package or approved raster artwork.

## Continue

- [Start in five minutes](START-HERE.md)
- [Documentation map](DOCUMENTATION.md)
- [Capability matrix](release-v0.1.0/docs/CAPABILITY-MATRIX.md)
- [Limits and non-claims](release-v0.1.0/docs/LIMITATIONS.md)
- [Public provenance](release-v0.1.0/PROVENANCE.md)
