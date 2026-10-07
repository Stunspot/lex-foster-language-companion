# Validation and evaluation

Evidence belongs to the claim actually checked. The 2026-10-06 repair retains earlier records as history and supplies new tests for declared progress, chronology, package custody and useful task flow.

## Run the packaged checks

From `codex/lex-foster-language-companion/` in the expanded package:

```text
python -B -m unittest discover -s scripts/tests -v
python -B scripts/validate_release.py
```

Expect tests to finish with `OK` and the release validator to report structural PASS. From the package root, run `python -B tools/verify_customer_release.py . --pretty`; expect `ok: true`. Use `--outer <path-to-outer-zip>` to compare the entire outer archive as well. See [Maintainer guide](MAINTAINER-GUIDE.md) for reconstruction, failure recovery and source ownership.

Profile validation checks the bundled schema, declared language/goal/evidence links, chronology and explicit result/support contradictions. Legacy records remain declarations. Human or model review must still inspect actual linguistic correctness and whether the task tests the particular diagnosed gap. The validator is not an assessment engine.

## Behavioral evaluation package

`evals/core-transfer-cases.yaml` contains 18 concrete case definitions. They cover initial value, selective correction, false friends, register, injection, low-resource authority, official ratings, source ambiguity, changed preferences, code-switching, absent audio, protected placeholders, translation-only completion, fabricated uptake, wrong-mechanism practice, copied models and legacy claims.

Examples demonstrate actual fictional source, learner responses and feedback, including the difference between supported repair and later independent evidence. Expert inspection challenges their instructional logic. Neither case definitions nor authored examples constitute executed model or participant trials. A real trial must retain model, host, exact package, supplied context, raw turns, interventions and assessment scope.

## What a passing check means

Static checks establish declared structure and exact byte custody for the tested artifact. A correct generic language response does not by itself prove this skill loaded. Use host loading/invocation evidence for activation and actual learner performance for progress. No check here proves equal language coverage, durable learning, professional approval, official proficiency, unseen audio, representative-user success or formal accessibility conformance.

The manifest, checksum and [Host matrix](../HOST-MATRIX.md) identify package evidence. Read the corresponding verification report for exact tested conditions; historical remote/deployment reports do not certify these revised bytes.
