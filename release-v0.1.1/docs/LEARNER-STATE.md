# Keep learner state under your control

The optional learner profile helps Lex resume without reconstructing every goal and preference. It is a user-owned working model, not a score or permanent judgment.

## Create a profile

1. Copy `assets/learner-profile.template.json` from the installed skill.
2. Save it under a name you control outside the installed skill folder.
3. Fill your chosen profile ID, a real current zoned update time (for example `2026-10-06T15:00:00-05:00`), working language, and target language/variety/script. Choose your preferences. Leave goals, evidence and retrieval empty until they exist.
4. Remove any personal detail that does not improve instruction.
5. Validate the file:

   `python scripts/validate_learner_profile.py <path-to-profile.json>`

Run the command from the installed skill folder, replacing the angle-bracket placeholder with your actual quoted file path. Expected result: `PASS declared structure and consistency only`. This is not a language score. The blank template intentionally reports missing identity/language/date fields until you fill them.

If Python is unavailable, keep the JSON readable and use it without a deterministic receipt. The lost guarantee is structural validation, not tutoring.

## Read the evidence states

- `new`: encountered but not yet produced;
- `supported`: produced with a model, choice, or cue;
- `independent`: produced without immediate support in the trained situation;
- `transferred`: met the same specific criterion in the same modality without immediate support under a materially changed cue.

These labels are declarations about a task. They do not certify mastery or a global level. An old record without `observation` details remains readable but receives an unverified-declaration note. Do not invent missing responses or rewrite its history.

For new evidence, optional `observation` detail records goal ID, modality, exact prompt and response, specific criterion, result and support kind. Transfer also names prior evidence and the changed condition. The example `examples/progress-and-return/observed-profile.json` inside the skill shows these fields with clearly fictional records. Do not import its history. `fictional-profile.json` shows legacy declarations.

The validator rejects explicit support/result contradictions, impossible dates, unknown references and identical transfer cue text. It cannot grade the language or decide whether a changed cue tests the diagnosed gap. Review those facts against the actual exchange. A shared topic is insufficient; naming restaurant words does not verify repair of a missing grammatical link. Written recognition does not establish speaking.

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