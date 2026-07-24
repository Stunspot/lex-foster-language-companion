# Remove Lex Foster Language Companion

Removal affects the installed skill. Your separate learner-profile files remain under your control unless you delete them explicitly.

## Remove from Codex

1. Close or finish tasks that currently depend on the skill.
2. Locate the installed `lex-foster-language-companion` folder in your Codex skills directory.
3. Confirm the folder contains this product's `SKILL.md`.
4. Remove that one folder using your normal file manager or approved host process.
5. Start a new Codex task.
6. Confirm `$lex-foster-language-companion` is no longer discovered.

Safe stopping state: if the folder identity is uncertain, do not delete it. Preserve the path and compare its manifest or files with the release artifact first.

## Remove from Claude

1. Open the current skill-management interface.
2. Locate **Lex Foster Language Companion**.
3. Disable or remove that skill according to the current interface.
4. Start a new conversation and confirm it is no longer available.

Current Claude UI labels and removal behavior were not observed in this build. Follow the host's current instructions where they differ.

## Remove learner state

Learner profiles are ordinary user-owned JSON files outside the skill. Delete or archive them separately according to your privacy and continuity needs. Removing the skill does not prove that a host, backup, chat transcript, or external service removed other copies.

## Reinstall

Install the exact desired version from the matching release. Do not merge files from several versions into one skill root.