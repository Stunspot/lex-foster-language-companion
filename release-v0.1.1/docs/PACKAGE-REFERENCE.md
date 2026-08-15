# Package reference

Scope: source-verified public paths and runtime responsibilities for Lex Foster Language Companion version 0.1.1. Additional development or verification artifacts may exist; this page does not infer their purpose without inspection.

## Repository entry points

| Path | Purpose |
|---|---|
| `README.md` | Product identification, first value, installation routes, trust, and repository map |
| `START-HERE.md` | Complete five-minute first-run tutorial with expected results and recovery |
| `DOCUMENTATION.md` | Task-oriented documentation hub and evidence vocabulary |
| `RELEASE-NOTES-v0.1.1.md` | Customer-facing release scope, impact, migration, and known limits |
| `ACCESSIBILITY.md` | Public-surface accessibility properties, review evidence, and claim limits |
| `SUPPORT.md` | Public support and documentation-defect route |
| `SECURITY.md` | Private security-reporting route and security surfaces |
| `CONTRIBUTING.md` | Product and documentation contribution workflow |
| `docs/` | GitHub Pages source and approved shared raster artwork |

## Customer release

| Path | Purpose |
|---|---|
| `release-v0.1.1/START-HERE.md` | Release-local customer journey and navigation |
| `release-v0.1.1/HOST-MATRIX.md` | Structural and live evidence by host |
| `release-v0.1.1/PROVENANCE.md` | Public identity, source custody, consulted foundations, and license boundary |
| `release-v0.1.1/codex/lex-foster-language-companion/` | Directly installable Codex skill folder |
| `release-v0.1.1/claude/lex-foster-language-companion-v0.1.1.zip` | One-skill Claude upload archive |
| `release-v0.1.1/maintainer-source/lex-foster-language-companion-v0.1.1/` | Versioned maintainer-source copy retained with the release |
| `release-v0.1.1/docs/` | Installation, operation, trust, recovery, reference, removal, and maintenance guidance |

## Skill root

| Path | Runtime responsibility |
|---|---|
| `SKILL.md` | Activation, orchestration, resource selection, boundaries, and completion |
| `personas/lex-foster-language-companion.md` | Integrated practitioner identity and professional judgment |
| `references/` | Selectively loaded pedagogy, translation, learner, culture, pronunciation, trust, and evidence doctrine |
| `assets/` | Learner profile, mission, translation brief, and session recap templates |
| `schemas/` | Learner-profile JSON Schema |
| `scripts/` | Standard-library learner-profile and release validators plus tests |
| `examples/` | Four demonstrations of task-native behavior and authority |
| `evals/` | Twelve isolated transfer cases in the canonical Collaborative Dynamics eval envelope |
| `fallbacks/` | Universal copy-paste prompt for hosts without skill installation |
| `agents/openai.yaml` | Codex display metadata and default prompt |

## Learner profile format

`lex-foster-learner-profile/v1` stores:

- user-chosen profile ID and update time;
- working and target languages;
- real-world goals and success evidence;
- correction, explanation, challenge, and working-language preferences;
- task-bound evidence states;
- retrieval cues;
- optional privacy note.

The deterministic validator checks shape, required values, unique IDs, date-time syntax, evidence-state vocabulary, and retrieval references. It does not score language ability.

## Documentation inventory

| Need | Path |
|---|---|
| Install | `docs/INSTALLATION.md` |
| First value | `docs/QUICK-START.md` |
| Tutoring and communication | `docs/USER-GUIDE.md` |
| Translation and localization | `docs/TRANSLATION-GUIDE.md` |
| Learner-owned state | `docs/LEARNER-STATE.md` |
| Troubleshooting | `docs/TROUBLESHOOTING.md` |
| Capabilities | `docs/CAPABILITY-MATRIX.md` |
| Limits | `docs/LIMITATIONS.md` |
| Validation | `docs/VALIDATION-AND-EVALUATION.md` |
| Accessibility | `docs/ACCESSIBILITY.md` |
| Removal | `docs/REMOVAL.md` |
| Maintenance | `docs/MAINTENANCE.md` |
| Package lookup | `docs/PACKAGE-REFERENCE.md` |

## External dependencies

The skill itself is Markdown, JSON, JSON-compatible YAML, and Python. Optional scripts use only the Python standard library. No network connection, credential, database, microphone, audio engine, browser, official assessment authority, or human reviewer is bundled or assumed.

## Evidence boundary

A path existing establishes file presence only. Consult [Validation and evaluation](VALIDATION-AND-EVALUATION.md), the [Host matrix](../HOST-MATRIX.md), and retained verification records before claiming execution, host compatibility, behavioral quality, accessibility, or professional approval.
