# Release verification — v0.1.0

## Proposed status

`READY_WITH_RESIDUAL_RISK` for a public package release after repository publication and live GitHub Pages checks.

## Executed evidence

- Six `unittest` cases passed for learner-profile validation and release structure.
- The canonical source skill passed `validate_release.py` with 30 files.
- The Codex distribution passed `validate_release.py` with 26 files.
- The Claude staging distribution passed `validate_release.py` with 26 files.
- SHA-256 comparison confirmed 26 runtime files match across canonical, Codex, Claude staging, and maintainer-source copies.
- The final Claude ZIP matched the Claude staging distribution byte-for-byte: `F1258397EEAF702D4625F16B9608C5A23AADDB2C3CCAE9C3A60083D2815F226C`.

## Critical boundaries

- Deterministic checks establish package shape and data-validation behavior; they do not establish language quality.
- Codex and Claude installation, discovery, activation, persistence, and host-specific runtime behavior require live target-host checks.
- GitHub Pages browser rendering, keyboard operation, and production links require deployment and live inspection.
- No official proficiency assessment or certified translation claim is made.
