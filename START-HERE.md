# Try Lex Foster Language Companion in five minutes

The goal is one useful language turn before you have to learn the product. This path installs the actual version 0.1.0 skill and tests the behavior that matters: useful language first, one decisive explanation, and a chance to use the learning.

## 1. Choose the artifact for your host

- **Codex:** use `release-v0.1.0/codex/lex-foster-language-companion/`.
- **Claude:** use `release-v0.1.0/claude/lex-foster-language-companion-v0.1.0.zip`.
- **Another capable text model:** use the universal fallback inside the Codex skill folder.

Do not upload the whole repository as a Claude skill or copy the Claude ZIP itself into a Codex skills directory.

## 2. Install the skill

Follow the exact steps in the [installation guide](release-v0.1.0/docs/INSTALLATION.md). Start a fresh task or conversation after installation so the host can discover the skill cleanly.

The release was structurally validated for Codex and Claude packaging. Current host UI labels, live discovery, activation, resource loading, Python execution, persistence, and restart behavior depend on the host and are not universally claimed as tested.

## 3. Ask for a real communicative job

In Codex, send:

```text
Use $lex-foster-language-companion.

I need to introduce myself at a Brazilian jiu-jitsu gym in Portuguese. I am a beginner and want to sound friendly rather than formal. Give me something usable first, explain the choice that most affects the relationship, then play the other person so I can answer.
```

In Claude or the copy-paste fallback, omit the skill handle if the host does not use one.

## 4. Check the first response

Successful activation should produce:

- language you can use now;
- a visible choice about meaning, tone, relationship, variety, or register;
- a small attempt, variation, or repair for you to make;
- only the context questions that materially change the result;
- uncertainty attached to the affected phrase rather than buried in a disclaimer pile.

The intended capability did not activate cleanly if the response begins with a long questionnaire, a generic vocabulary list, an official proficiency claim, or a lecture that never lets you use the language.

## 5. Test the tutoring loop

Reply in the target language. After feedback, ask:

```text
Change one detail in the situation and make me use that correction again.
```

A strong turn should move through attempt, focused feedback, repair, and changed-cue reuse rather than simply showing a corrected answer.

## 6. Test translation fit

```text
Translate this into Canadian French for a warm but professional customer-service email. Preserve the product name Northstar and the placeholder {ticket_id}. Give me the target text first, then identify any source ambiguity that could change the translation.
```

Look for protected terms, audience fit, register, locale, formatting, and local uncertainty—not merely a fluent sentence.

## 7. Test a boundary

Try one of these:

- Ask for an official CEFR or ACTFL rating. Lex should describe observed functional reach informally rather than issue a credential.
- Ask for pronunciation judgment without supplying audio. Lex should provide articulatory guidance and name the missing evidence.
- Provide an ambiguous legal or medical sentence. Lex should preserve the ambiguity and route consequential approval to a qualified human.
- Ask about a low-resource or community-governed language. Lex should distinguish model output from community authority.

## Where to go next

- [Tutoring, rehearsal, pronunciation, culture, and continuity](release-v0.1.0/docs/USER-GUIDE.md)
- [Translation and localization](release-v0.1.0/docs/TRANSLATION-GUIDE.md)
- [Learner-owned state](release-v0.1.0/docs/LEARNER-STATE.md)
- [Troubleshooting by observable symptom](release-v0.1.0/docs/TROUBLESHOOTING.md)
- [Capability matrix](release-v0.1.0/docs/CAPABILITY-MATRIX.md)
- [Validation and evidence boundary](release-v0.1.0/docs/VALIDATION-AND-EVALUATION.md)
- [Package reference](release-v0.1.0/docs/PACKAGE-REFERENCE.md)
