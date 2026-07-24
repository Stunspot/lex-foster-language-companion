# Install Lex Foster Language Companion

Choose the artifact for your host. Codex uses an unpacked skill folder. Claude uses one upload-ready ZIP.

## Install in Codex

### You need

- Codex with local skill support.
- Access to your Codex skills directory.
- The folder `release-v0.1.0/codex/lex-foster-language-companion/`.

### Steps

1. Copy the entire `lex-foster-language-companion` folder from `codex`.
2. Place it in your Codex skills directory.
3. Confirm the final path ends with `.codex/skills/lex-foster-language-companion/SKILL.md`.
4. Start a new Codex task so discovery begins from a fresh context.
5. Enter `$lex-foster-language-companion` followed by a real language request.

Expected result: Codex loads Lex and begins from the communicative task rather than a generic course intake.

If Codex reports that the skill is missing, use [The skill does not activate](TROUBLESHOOTING.md#the-skill-does-not-activate).

## Upload to Claude

### You need

- A Claude plan and interface that supports uploaded skills.
- `release-v0.1.0/claude/lex-foster-language-companion-v0.1.0.zip`.

### Steps

1. Open Claude's skill-management interface.
2. Upload `lex-foster-language-companion-v0.1.0.zip` as one skill.
3. Enable the skill if the current interface requires enablement.
4. Start a new conversation.
5. Ask for help with a real tutoring or translation task.

Expected result: Claude discovers one top-level `lex-foster-language-companion` skill and can load the references, templates, examples, and optional validators contained beneath it.

Important: the pre-ZIP folder was structurally validated. Current Claude UI labels, upload, enablement, discovery, activation, resource loading, Python availability, and persistence were not observed during construction.

## Use the universal fallback

If your chat host cannot install skills:

1. Open `fallbacks/universal-copy-paste-companion.md` inside either unpacked skill folder.
2. Copy the prompt inside the code block.
3. Paste it into a capable text model.
4. Add your language request beneath it.

The fallback preserves the central conversational behavior. It does not provide package resource loading, deterministic learner-profile validation, or host-managed discovery.

## Confirm first value

Use this probe:

> Help me ask a new neighbor in Mexican Spanish to lower their music after 10 p.m. I want to stay friendly. Give me usable language first, explain the choice that most affects the tone, then play the neighbor so I can rehearse.

Successful activation produces usable language before extended intake, distinguishes relationship and tone, and creates a learner attempt or repair.