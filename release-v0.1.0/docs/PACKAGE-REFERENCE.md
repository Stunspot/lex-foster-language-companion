# Package reference

## Customer release

| Path | Purpose |
|---|---|
| `START-HERE.md` | Customer journey and navigation |
| `HOST-MATRIX.md` | Structural and live evidence by host |
| `codex/lex-foster-language-companion/` | Directly installable Codex skill |
| `claude/lex-foster-language-companion-v0.1.0.zip` | One-skill Claude upload archive |
| `maintainer-source/lex-foster-language-companion-v0.1.0/` | Canonical product source retained for maintainers |
| `docs/` | Installation, operation, trust, recovery, and maintenance guidance |
| `release-manifest.json` | Versioned inventory and SHA-256 custody |

## Skill root

| Path | Runtime responsibility |
|---|---|
| `SKILL.md` | Activation, orchestration, resource selection, boundaries, and completion |
| `personas/lex-foster-language-companion.md` | Lex's integrated identity and professional judgment |
| `references/` | Selectively loaded pedagogy, translation, learner, culture, pronunciation, trust, and evidence doctrine |
| `assets/` | Learner profile, mission, translation brief, and session recap templates |
| `schemas/` | Learner-profile JSON Schema |
| `scripts/` | Standard-library learner-profile and release validators plus tests |
| `examples/` | Four demonstrations of task-native behavior and authority |
| `evals/` | Twelve isolated transfer cases in the canonical CD eval envelope |
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

## External dependencies

The skill itself is Markdown, JSON, JSON-compatible YAML, and Python. Optional scripts use only the Python standard library. No network, credential, database, audio engine, or external package is bundled or assumed.