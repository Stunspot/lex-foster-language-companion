# GitHub Pages source and custody

This directory publishes the public product site at:

<https://stunspot.github.io/lex-foster-language-companion/>

GitHub Pages is sourced from `main` and the repository-root `/docs` directory.

## Files

- `index.html` is the customer-facing product page and documentation router.
- `style.css` supplies the responsive Stunspot Blue presentation, visible keyboard focus, reflow, reduced-motion handling, and print behavior.
- `.nojekyll` declares a static site without Jekyll transformation.
- `assets/lex-foster-language-companion-readme.png` is the approved shared raster banner used by the repository README, Pages hero, and social-preview metadata.

The banner is supplemental. All product claims, installation paths, capability descriptions, and trust boundaries also appear as selectable text.

## Preserve the approved artwork

Documentation maintenance must preserve the approved PNG bytes and the existing README, hero, Open Graph, and Twitter image references unless the owner explicitly approves an artwork change.

Use raster PNG, WebP, or JPEG assets for this repository workflow. Do not create, add, or substitute an SVG asset without explicit owner authorization.

## Keep the public surfaces synchronized

Reopen the README, documentation map, Pages source, accessibility statement, and review record when any of these change:

- product name, version, positioning, publisher, or license;
- supported host or installation path;
- skill handle, package shape, or first-use prompt;
- capability, boundary, or evidence claim;
- public artwork or social-preview metadata;
- documentation link, release location, support route, or security route.

After a change:

1. run the Hesperos accessible-Markdown lint on changed Markdown;
2. parse `index.html` and inspect title, language, headings, landmarks, image treatment, links, and reading order;
3. check local repository links, literal paths, and asset-reference invariants;
4. verify the live HTTPS page and referenced raster asset after deployment when network access is available;
5. record what was tested and what remains untested in `verification/documentation-review.md`;
6. update `release-v0.1.0/docs/MAINTENANCE.md` and the documentation source ledger when source, ownership, or evidence changes.

Automated lint, static inspection, and a successful HTTP response do not establish screen-reader usability, representative-user success, social-card behavior, or formal WCAG conformance. The current public-surface statement is [Accessibility statement](../ACCESSIBILITY.md).