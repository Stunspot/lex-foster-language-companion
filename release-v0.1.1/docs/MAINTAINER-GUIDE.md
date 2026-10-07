# Maintain Lex Foster Language Companion

Edit the current skill and affected customer guidance, then build a new candidate without replacing accepted bytes. Python 3.10 or newer is sufficient; no third-party runtime packages are required.

## Find the source

In the repository, runtime source is `source/lex-foster-language-companion-v0.1.1/skills/lex-foster-language-companion/`; maintained customer pages are `release-v0.1.1/docs/` plus its top-level Markdown files. In a downloaded package, the exact source copy is `maintainer-source/skills/lex-foster-language-companion/`, and customer pages are `docs/` and the top-level Markdown files. `tools/` contains the portable builder and verifier.

Preserve prior archives, existing dirty work, learner files and artwork. The current practitioner is an adapted derivative: retain Lex’s patient, exacting linguistic judgment within the host companion identity. Do not turn the source character’s biography into a claim of human or community authority. Original ancestry stays preserved.

## Check and build

From the runtime skill folder:

```text
python -B -m unittest discover -s scripts/tests -v
python -B scripts/validate_release.py
```

From the repository root or the expanded customer package root:

```text
python -B tools/build_customer_release.py --output <new-candidate-directory>
```

Replace the placeholder with a quoted path to a new directory. The destination must not exist or overlap maintained source or accepted releases. All builds use current source; the old default reconstruction from 0.1.0 has been removed. The builder stages the complete bundle, validates it and then renames the new directory into place. A failure leaves accepted output and source intact. Fix the reported source defect and choose a new destination; do not erase an accepted package to make the command work.

The result contains `lex-foster-language-companion-v0.1.1/`, the outer ZIP, checksum and `verification.json`. Check the exact release and ZIP from the original root:

```text
python -B tools/verify_customer_release.py <new-candidate-directory>/lex-foster-language-companion-v0.1.1 --outer <new-candidate-directory>/Lex-Foster-Language-Companion-v0.1.1.zip --pretty
```

Each path with spaces needs quotes. Expect `ok: true`; false includes actionable findings. Fresh native extraction and tests of the extracted runtime establish the actual delivered tree. A second build from the extracted package can check reproducibility. Nothing here installs the skill or publishes a channel.

## Review the changed promise

Read [Validation and evaluation](VALIDATION-AND-EVALUATION.md). Exercise concrete task contrasts when teaching, translation or evidence rules change; preserve raw learner/model responses if such trials actually run. Definitions and authored fictional dialogue are not executed trials. A successful generic response also cannot prove this particular skill was loaded. Use host resource-loading evidence for that separate claim.

Reopen the affected documentation through Hesperos when a path, command, behavior, recovery or evidence limit changes. Bind only newly authored or materially revised documents to this authoring run. Keep unchanged historical receipts; a newer authoring-tool hash does not erase older authorship. A separate reviewer challenges finding, action, recovery and evidence claims.

Classify the complete delta against the accepted release before choosing a version. Local verification establishes a candidate. The accountable product owner then reconciles applicable distributions, sidecars, shelf/catalog and consumers through the governing delivery contract.
