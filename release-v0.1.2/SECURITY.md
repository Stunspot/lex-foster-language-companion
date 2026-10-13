# Security policy

## Report privately

Use this repository's **Security** tab to open a private security advisory. Do not place credentials, private learner records, sensitive source texts, or exploit details in a public issue.

Include the affected version, package path, host, reproduction steps, realistic impact, and any safe evidence you can share.

## Relevant security surfaces

This release contains prompt instructions, Markdown and JSON artifacts, and optional Python standard-library validators. It assumes no network access and stores no credentials. Important risks include:

- instructions embedded in text supplied for translation;
- accidental retention of private learner or document data;
- path or packaging defects that expose unintended files;
- corrupted placeholders, tags, names, numbers, dates, or units;
- language output presented with authority it does not possess.

The maintainers will assess reports against the current release bytes. No response-time or remediation-time guarantee is asserted.