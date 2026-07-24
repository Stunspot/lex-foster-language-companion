# Documentation and accessibility review — Hesperos repair, 2026-07-24

## Decision

`REVIEW_PASS_WITH_CONDITIONS` for the repository README, onboarding, task-oriented documentation map, version 0.1.0 customer documentation, maintenance governance, release notes, public accessibility statement, and static GitHub Pages source.

This decision supports publication of the documentation repair. It does not certify product behavior, language correctness, host compatibility, representative-user success, or formal accessibility conformance.

## Documentation brief

- Product and version: Lex Foster Language Companion 0.1.0.
- Intended readers: prospective users, installers, learners, translators, maintainers, evaluators, contributors, and support reporters.
- Top tasks: identify the product, install the correct artifact, reach first value, complete a language task, recover from failure, inspect trust, and maintain the documentation.
- Delivery surfaces: GitHub README and Markdown, versioned customer documentation, and static GitHub Pages HTML/CSS.
- Source authorities: current package and source, versioned release, retained tests and verification, accountable product decisions, current public documentation, then bounded inference.
- Risk context: misleading authority, incorrect artifact selection, unrecoverable procedures, hidden evidence limits, inaccessible navigation, and accidental artwork replacement.
- Owner and approval authority: Collaborative Dynamics maintainers; public artwork and consequential product claims require accountable owner approval.

## Evidence inspected

- the canonical Hesperos Documentation version 0.1.1 package, persona, operating doctrine, task strategy, accessibility guidance, procedure and troubleshooting doctrine, information architecture, evidence governance, review rubric, and verification guidance;
- the current repository README, onboarding, support, security, contribution, accessibility, release-local start page, installation, quick start, user guide, translation guide, learner state, troubleshooting, capability matrix, limits, validation, package reference, removal, host matrix, and provenance;
- the current static GitHub Pages source and its raster image references;
- the public onboarding and repository-presentation patterns used by the Nova and TestForge Augment repositories;
- the owner-supplied PNG at `docs/assets/lex-foster-language-companion-readme.png`, approved as the public README and Pages artwork;
- the standing constraint that SVG artwork must not be created or introduced without explicit owner instruction.

## Repairs made

- created a task-oriented documentation hub;
- created customer-facing release notes distinct from tutorials and reference;
- created documentation maintenance governance with owner, source authority, cadence, change triggers, feedback, retirement, safe stopping, and completion proof;
- rewrote installation and troubleshooting as recoverable state transitions;
- corrected package reference to document verified public paths without relying on an unverified manifest claim;
- strengthened first-run onboarding with prerequisites, expected results, failure branches, safe stopping, and completion evidence;
- added a documentation source ledger with explicit evidence states;
- synchronized README and Pages navigation with the new documentation system;
- restored the owner-supplied PNG across the README, Pages hero, Open Graph metadata, and Twitter metadata without converting or regenerating it;
- removed the superseded WebP and placeholder SVG artwork;
- documented the raster-only asset policy and explicit owner gate for any future SVG.

## Checks executed

- Hesperos documentation-project schema validation;
- Hesperos accessible-Markdown structural lint on every Markdown file changed by the documentation repair;
- local HTML parsing of the changed `docs/index.html` source;
- static inspection of HTML language, title, headings, landmarks, navigation, image treatment, link purpose, and reading order;
- static internal-link and literal-path inspection for changed documentation;
- exact inspection of the README, Pages hero, Open Graph, and Twitter image paths after the PNG restoration;
- asset-path inspection confirming the approved PNG is present and the superseded WebP and placeholder SVG are removed.

## What the documentation now supports

- A prospective user can identify an installable language tutoring and translation capability for AI agents while understanding Lex Foster as the integrated practitioner voice.
- A first-time user can choose the correct artifact, verify first value, recognize failure, preserve evidence, and reach a recovery path.
- A learner can predict the tutoring loop, control feedback, recognize completion, and optionally manage learner-owned continuity.
- A translator can define purpose, audience, relationship, variety, terminology, protected material, ambiguity, completion, and human-review authority.
- A maintainer can identify source authority, evidence state, topic type, change triggers, review cadence, safe stopping, completion proof, feedback, and retirement.
- An evaluator can separate file presence, retained deterministic evidence, defined eval cases, live host behavior, accessibility review, and untested claims.

## Conditions and residual uncertainty

- Verify the deployed GitHub Pages page and PNG asset over HTTPS after the restoration reaches production.
- Keyboard navigation, zoom and reflow, screen-reader behavior, browser-specific layout, social-card rendering, and representative-user usability remain untested until exercised with those tools and users.
- Live installation and activation in current Codex and Claude versions remain host-specific unless separately observed.
- The review does not establish formal WCAG conformance, language correctness, cultural authority, official assessment validity, professional translation approval, or universal model behavior.
- Repository assets outside the restored PNG and removed superseded artwork were not altered or re-certified by this repair.

## Reopen triggers

Re-run this review when product positioning, version, install path, package shape, skill handle, capability boundary, evidence claim, host result, public artwork, Pages source, documentation route, support route, security route, or customer task changes.