# Keep learner state under your control

The optional learner profile helps Lex resume without reconstructing every goal and preference. It is a user-owned working model, not a score or permanent judgment.

## Create a profile

1. Copy `assets/learner-profile.template.json` from the installed skill.
2. Save it under a name you control outside the installed skill folder.
3. Replace the sample target language, goal, preference, and evidence entry.
4. Remove any personal detail that does not improve instruction.
5. Validate the file:

   `python scripts/validate_learner_profile.py <path-to-profile.json>`

Expected result: the script prints `PASS` with the target-language and evidence counts.

If Python is unavailable, keep the JSON readable and use it without a deterministic receipt. The lost guarantee is structural validation, not tutoring.

## Read the evidence states

- `new`: encountered but not yet produced;
- `supported`: produced with a model, choice, or cue;
- `independent`: produced without immediate support in the trained situation;
- `transferred`: produced or recognized under a materially changed cue.

These labels describe observed performance in a task. They do not certify mastery or a global level.

## Resume a session

1. Provide the profile at the beginning of the conversation.
2. State any changed goal or preference in ordinary language.
3. Ask Lex to retrieve one high-value item before reteaching it.
4. Use a changed situation to test transfer.
5. Update only the evidence the session actually produced.

A live correction to the profile takes priority. Decide whether it applies only today or should be saved.

## Keep the file under your control

The profile may contain goals, relationships, language errors, or private situations. Store it according to your own privacy needs. Remove names, addresses, employer details, health information, legal details, and identifiers that are unnecessary for instruction.

You may inspect, edit, export, or delete the file at any time. This package assumes no hidden learner database or automatic cloud persistence.

## Recover a broken profile

Run the validator and repair the first reported field. Common failures include an unsupported evidence state, duplicate evidence ID, invalid date-time, or retrieval item that points to missing evidence.

If repair would destroy meaningful history, preserve the original as read-only evidence and create a corrected copy with a new update time.