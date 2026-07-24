# Maintain the Lex Foster Language Companion documentation

Goal: keep public guidance aligned with current product truth, user tasks, evidence, accessibility, and recovery without changing runtime or artwork by accident.

Audience: Collaborative Dynamics maintainers and approved contributors.

Owner: Collaborative Dynamics maintainers. Product positioning, release claims, public artwork, and consequential authority boundaries require accountable owner approval.

Applicable version: version 0.1.0 until a later release explicitly supersedes it.

## Source authority

Use the most direct current source for the claim:

1. current versioned runtime behavior, validators, tests, schemas, and package files;
2. the canonical source under `source/` and the versioned customer release under `release-v0.1.0/`;
3. accountable product decisions and release records;
4. retained verification, host, support, and issue evidence;
5. public documentation;
6. inference, clearly labeled and never used to overrule stronger evidence.

Use the evidence states `source-verified`, `reported`, `inferred`, `conflicted`, `not examined`, and `not tested`. Keep the state attached to the affected claim.

The current claim ledger is [Documentation source ledger](../../verification/documentation-source-ledger.md).

## Public documentation system

| Surface | Primary reader task | Source of truth |
|---|---|---|
| `README.md` | Identify the product and choose a path | Product positioning plus current customer release |
| `START-HERE.md` | Reach and verify first value | Installation, quick-start, behavior contract, and recovery docs |
| `DOCUMENTATION.md` | Find the right topic | Current documentation inventory and user journeys |
| `RELEASE-NOTES-v0.1.0.md` | Understand customer-facing change | Versioned release scope, evidence, migration, and known limits |
| `release-v0.1.0/docs/` | Install, use, recover, inspect, and maintain | Versioned package and retained evidence |
| `docs/index.html` | Public product landing and documentation routing | README positioning plus current documentation map |
| `ACCESSIBILITY.md` | Understand authored properties and tested limits | Current sources plus retained review evidence |
| `verification/documentation-review.md` | Inspect documentation readiness | Recorded methods, results, conditions, and reopen triggers |

## Change triggers

Reopen the affected documentation when any of these changes:

- product name, positioning, publisher, license, or version;
- supported host, installation artifact, path, skill handle, or package shape;
- tutoring, translation, learner-state, pronunciation, culture, privacy, or authority behavior;
- schema, validator, command, dependency, example, eval, or error message;
- evidence state, host result, accessibility finding, or known limit;
- support route, security route, release location, or public URL;
- recurring user failure, new reader task, or changed terminology;
- public artwork or social-preview metadata.

Review the estate before every public release and at least every 90 days while the repository remains active. A material trigger overrides the scheduled cadence.

## Preserve artwork and format custody

The approved public label is the raster PNG at `docs/assets/lex-foster-language-companion-readme.png`, used by the README and Pages source. Documentation work must preserve its file bytes and existing references unless the owner explicitly authorizes an artwork change.

Use raster PNG, WebP, or JPEG assets for this repository workflow. Do not create, introduce, or substitute an SVG asset without explicit owner authorization.

Before committing documentation work, compare the README image line and Pages image paths with the starting state. Treat any unrequested difference as a blocking defect.

## Maintenance procedure

Starting state: you have the current branch, the exact affected version, the reader task, and the source that triggered the change.

1. Frame the change.
   - Record reader, use moment, top task, successful outcome, version, risk, owner, and approval authority.
   - Expected result: the change has a task and decision boundary rather than a vague request to “update docs.”
2. Reconstruct product truth.
   - Compare the current package, source, tests, schemas, product decision, and retained evidence.
   - Expected result: consequential claims have an evidence state and applicable scope.
   - If conflicted: preserve the conflict, narrow the topic, and route the decision to the accountable owner.
3. Choose the topic type.
   - Use tutorial for supported learning, how-to for a goal, reference for exact lookup, explanation for a mental model, troubleshooting for recovery, and release notes for change.
   - Expected result: one page serves one primary reader intent.
4. Compose the smallest sufficient repair.
   - Lead with the goal or answer; use meaningful headings, active verbs, exact terms, progressive disclosure, and examples that expose the decisive cue.
5. Complete procedures and recovery.
   - Include prerequisites, starting state, ordered actions, expected results, observable branches, safe stopping, recovery, escalation, and completion proof.
6. Review accessibility while structure is fluid.
   - Check heading order, lists, tables, link purpose, language, reading order, text alternatives, nonvisual equivalence, cognitive load, and input-method-neutral wording.
7. Verify the changed path.
   - Run the Hesperos accessible-Markdown lint on changed Markdown.
   - Parse changed HTML and inspect semantics.
   - Check internal links, literal paths, examples, and image-reference invariants.
   - Run real browser, keyboard, screen-reader, or representative-user tests only when those environments are available; record the exact surface and result.
8. Update custody records.
   - Revise release notes, package reference, source ledger, accessibility statement, review record, or host matrix when the change alters their claims.
9. Obtain approval and publish.
   - Expected result: the accountable owner can see what changed, what supports it, what remains untested, and what reopens the topic.

## Safe stopping and recovery

Safe stopping state: leave the current public path intact, preserve the proposed files and evidence separately, and do not publish a claim whose source, scope, or approval is unresolved.

Recovery path: revert only the documentation change that caused the regression, restore the last verified raster image references, rerun the affected task walkthrough, and reopen the review record.

## Completion proof

The maintenance cycle is complete when:

- the intended reader can find the updated topic from [DOCUMENTATION.md](../../DOCUMENTATION.md);
- consequential claims trace to evidence and version;
- the procedure supports action, verification, and recovery;
- changed Markdown passes structural lint and receives manual semantic review;
- changed HTML and links receive static inspection;
- public artwork and image references remain unchanged unless explicitly authorized;
- untested paths and owner decisions remain explicit;
- the source ledger and review record match the final state.

## Feedback and retirement

Use [Support](../../SUPPORT.md) for documentation defects and recurring user failures. Use [Security policy](../../SECURITY.md) for sensitive vulnerabilities.

When a version is superseded, preserve its versioned documentation for historical use, mark it as superseded, route current entry points to the supported version, and retain migration or removal guidance. Archive rather than silently rewriting historical product truth.