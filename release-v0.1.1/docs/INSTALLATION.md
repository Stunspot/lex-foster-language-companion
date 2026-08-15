# Install Lex Foster Language Companion

Goal: install the version 0.1.1 artifact intended for your host, verify that the host can discover it, and preserve a safe recovery path when the observed result differs.

Audience: a user who can install or upload a skill in Codex or Claude, or use a copy-paste fallback in another capable text model.

Starting state: you have the repository or release files available, but Lex Foster Language Companion is not active in the fresh task or conversation you will use for verification.

## Before you begin

You need:

- permission to install or upload a skill in the chosen host;
- the correct version 0.1.1 artifact;
- one real language task for the activation check;
- a copy of the original artifact so you can recover without reconstructing files.

Do not merge several versions into one skill folder. Do not place credentials, private learner records, or confidential translations in installation evidence.

## Install in Codex

### Artifact

Use the complete folder:

`release-v0.1.1/codex/lex-foster-language-companion/`

### Steps

1. Locate the directory your Codex installation currently scans for skills.
   - Expected result: you can identify the directory without changing global configuration.
   - If different: use the current Codex host documentation or your administrator's configured path.
2. Copy the complete `lex-foster-language-companion` folder into that skills directory.
   - Expected result: the installed tree contains `lex-foster-language-companion/SKILL.md`, with its `references`, `assets`, `schemas`, `scripts`, `examples`, `evals`, and other packaged resources preserved beneath the same root.
   - If different: remove only the incomplete copy and repeat from the untouched release artifact.
3. Start a new Codex task.
   - Expected result: discovery begins from a context created after installation.
4. Enter `$lex-foster-language-companion` followed by a real language request.
   - Expected result: Codex loads the skill and begins from the communicative task rather than a generic course intake.

If the skill is unavailable, preserve the installed path, tree shape, Codex version, and exact message. Continue with [The skill is not available](TROUBLESHOOTING.md#the-skill-is-not-available).

## Upload to Claude

### Artifact

Use the prepared archive:

`release-v0.1.1/claude/lex-foster-language-companion-v0.1.1.zip`

### Steps

1. Open the current Claude interface that manages uploaded skills.
   - Expected result: the account exposes a supported upload path.
   - If different: stop and consult the current host guidance; do not unpack and upload random repository folders as a substitute.
2. Upload `lex-foster-language-companion-v0.1.1.zip` as one skill.
   - Expected result: Claude receives one archive containing one top-level `lex-foster-language-companion` folder with `SKILL.md` directly beneath it.
3. Enable the skill when the current interface requires enablement.
   - Expected result: the skill is available to a new conversation.
4. Start a new conversation and ask for a real tutoring or translation task.
   - Expected result: Claude can use the packaged guidance and resources associated with the skill.

The pre-ZIP folder and final archive have retained structural validation records. Current Claude UI labels, upload behavior, enablement, discovery, activation, resource loading, Python availability, and persistence were not universally observed during construction.

If upload or activation fails, preserve the account surface, archive name, host version, exact message, and whether the archive was modified. Continue with [The skill is not available](TROUBLESHOOTING.md#the-skill-is-not-available).

## Use the universal fallback

Use this path when the host cannot install skills.

1. Open `fallbacks/universal-copy-paste-companion.md` inside the unpacked Codex skill folder.
   - Expected result: the file contains one portable prompt and its use boundary.
2. Copy the prompt into a new conversation with a capable text model.
3. Place your language request beneath it.
   - Expected result: the model follows the central tutoring and translation behavior without package-managed discovery.

The fallback does not provide selective resource loading, deterministic learner-profile validation, package-relative scripts, or host-managed persistence.

## Confirm first value

Use this probe:

> Help me ask a new neighbor in Mexican Spanish to lower their music after 10 p.m. I want to stay friendly. Give me usable language first, explain the choice that most affects the tone, then play the neighbor so I can rehearse.

Successful activation produces usable language before extended intake, distinguishes relationship and tone, and creates a learner attempt or repair.

## Safe stopping and recovery

Safe stopping state: retain the untouched release artifact and the exact failed installation evidence. Do not delete another skill, change unrelated host configuration, or repeatedly repack the Claude archive.

Recovery path: compare the installed or uploaded artifact with the intended host artifact, correct the smallest observable shape problem, start a fresh context, and rerun the first-value probe.

Completion proof: the correct artifact is present, a fresh context discovers or applies the skill, the probe produces the intended first-value behavior, and you know how to remove the installation through [Removal](REMOVAL.md).
