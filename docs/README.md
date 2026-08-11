# GitHub Pages source and custody

This directory publishes the public customer site at:

<https://stunspot.github.io/lex-foster-language-companion/>

GitHub Pages is sourced from `main` and the repository-root `/docs` directory.

## Customer routes

- `index.html` identifies the product and routes the visitor by task.
- `start.html` covers host selection, installation, activation verification, first value, recovery, and next steps.
- `guide.html` covers representative workflows, inputs and outputs, tutoring, rehearsal, translation, pronunciation, configuration, and learner-owned state.
- `trust.html` covers capabilities and non-claims, privacy, storage, network and security boundaries, evidence, troubleshooting, updating, removal, cleanup, support, contribution, and license.
- `404.html` provides a coherent recovery route for missing Pages paths.`n- `style.css` supplies the responsive presentation, visible focus, reflow, reduced-motion handling, article navigation, tables, callouts, and print behavior.
- `.nojekyll` declares a static site without Jekyll transformation.

## Visual role map

| Surface | Asset | Role |
|---|---|---|
| Repository README | `assets/lex-foster-readme-hero.png` | Wide product-system journey from communicative input through focused repair and reuse |
| Pages hero | `assets/lex-foster-pages-hero.png` | Distinct language-transformation and practice-loop composition |
| Open Graph and Twitter | `assets/lex-foster-social-card.png` | 1200 × 630 social card with the exact product title and identifying line |

The README and Pages heroes are text-free because adjacent selectable copy supplies the title, purpose, and actions. The social card contains exact visible text because previews may appear without adjacent page content. All three are raster images, different files, different compositions, and different aspect ratios.

## Keep public surfaces synchronized

Reopen the README, Pages routes, accessibility statement, source ledger, and review records when any of these change:

- product name, version, positioning, publisher, or license;
- supported host or installation path;
- skill handle, package shape, or first-use prompt;
- capability, boundary, privacy, security, or evidence claim;
- public artwork, aspect ratio, crop safety, or social-preview metadata;
- documentation route, support route, security route, or public URL.

After a change:

1. read every affected page completely and compare it with canonical package source;
2. run structural accessibility checks on changed Markdown and HTML;
3. parse every HTML route and inspect title, language, headings, landmarks, navigation, link purpose, and reading order;
4. open all three raster assets and inspect actual composition, hierarchy, contrast, legibility, identity, crop safety, and role fit;
5. check local and external links, anchors, literal paths, and asset references;
6. deploy, then verify every live route, asset, navigation path, social-metadata reference, and expected content over HTTPS;
7. bind documentation, accessibility, adversarial, and live receipts to the exact final document fingerprint or commit.

A successful HTTP response, valid file, expected filename, or correct image dimensions does not establish content quality, rendered usability, or visual fitness. The current public-surface statement is [Accessibility statement](../ACCESSIBILITY.md).