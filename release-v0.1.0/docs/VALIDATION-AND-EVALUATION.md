# Validation and evaluation

Evidence is retained by claim. One passing check does not promote another state.

## Deterministic checks completed during construction

- 6 unit tests passed for learner-profile validation and current skill structure.
- The skill's direct release validator passed 26 self-contained runtime files before distribution assembly.
- The Builder `bundle` profile passed canonical source structure, resources, containment, metadata, JSON, and private-path checks.
- The Builder `codex` profile passed the Codex skill folder.
- The Builder `claude` profile passed the pre-ZIP Claude skill folder.
- The Builder `claude` profile passed the final upload ZIP after the Lex identity and accessibility corrections.

The release manifest, documentation lint, link walk, exact cross-copy parity, clean Git state, remote branch, immutable tag, release assets, recovery backup, and live estate re-entry are separate gates and must be recorded after their execution.

## Behavioral evaluation package

The runtime includes `evals/eval-manifest.yaml` and `evals/core-transfer-cases.yaml` in `cd-augment-eval/v1` format. Twelve isolated cases examine:

- useful first value from vague input;
- correction timing and learner agency;
- meaning-changing false friends;
- register and relationship;
- instructions embedded in source text;
- low-resource and community authority;
- official proficiency claims;
- consequential medical ambiguity;
- revised learner preference;
- code-switching;
- absent audio;
- placeholder and locale preservation.

A case file defines expected behavior; it is not an executed model episode. Behavioral execution must retain the model, adapter, host, package version, supplied context, raw response, evaluator intervention, and verdict.

## Claims not established by static validation

Static checks do not prove:

- successful installation or host activation;
- implicit natural-language routing;
- equal performance across languages or models;
- durable learning or user outcomes;
- translation correctness in an unreviewed domain;
- official assessment validity;
- browser, keyboard, screen-reader, or representative-user accessibility;
- professional, legal, medical, community, or publication approval.

## Read the current release state

Use [HOST-MATRIX.md](../HOST-MATRIX.md), the release manifest, documentation review receipt, verification reports, and live re-entry report together. A missing receipt leaves that state `not tested` or `pending`; it does not imply success or failure.