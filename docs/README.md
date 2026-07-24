# GitHub Pages source and custody

This directory publishes the public product site at:

<https://stunspot.github.io/lex-foster-language-companion/>

GitHub Pages is sourced from `main` and the repository-root `/docs` directory.

## Files

- `index.html` is the customer-facing product page.
- `style.css` supplies the responsive Stunspot Blue presentation, visible keyboard focus, reflow, reduced-motion handling, and print behavior.
- `assets/lex-foster-language-companion-readme.webp` is the approved shared banner used by the repository README and social-preview metadata.

The banner is supplemental. All product claims, installation paths, capability descriptions, and trust boundaries also appear as selectable text.

## Keep the surfaces synchronized

Reopen the README and Pages source when any of these change:

- product name, version, positioning, or publisher;
- supported host or installation path;
- skill handle, package shape, or first-use prompt;
- capability, boundary, or evidence claim;
- public artwork or social-preview metadata;
- documentation link or release location.

After a change:

1. run the Hesperos accessible-Markdown lint on changed Markdown;
2. parse `index.html` and inspect heading, landmark, image, link, and language semantics;
3. check local repository links and asset paths;
4. verify the live HTTPS page and image after deployment;
5. record what was tested and what remains untested in `verification/documentation-review.md`.

Automated lint and a successful HTTP response do not establish screen-reader usability, representative-user success, or formal WCAG conformance. The current public-surface statement is in [`../ACCESSIBILITY.md`](../ACCESSIBILITY.md).
