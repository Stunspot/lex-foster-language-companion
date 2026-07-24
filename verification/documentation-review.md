# Documentation and accessibility review — v0.1.0

## Decision

`REVIEW_PASS_WITH_CONDITIONS` for the documentation as a static release artifact.

## Evidence inspected

- Root README and public-service, support, contribution, and security pages.
- The release start-here page, host matrix, and 14 customer documentation topics.
- The responsive GitHub Pages source in `docs/`.
- Three raster JPEG assets used for the README, social preview, tutoring explanation, and translation explanation.
- Open Graph and Twitter social-image metadata.
- The installed Hesperos accessible-Markdown linter, applied to the root customer Markdown set.

## What the documentation supports

- A prospective user can identify the product, choose Codex or Claude, install the matching artifact, get first value, use tutoring or translation, understand learner-owned state, and find recovery guidance.
- The root README now exposes the primary install paths, tutoring loop, translation model, trust boundary, and project-site route without requiring a release-directory excavation.
- The Pages source supplies semantic headings, keyboard-focus treatment, reduced-motion handling, responsive layouts, alternative text for each image, and social-preview metadata.
- Procedures do not rely on image-only, color-only, or position-only instructions; explanatory text accompanies every visual asset.

## Observed deployment

The GitHub Pages source is deployed from `main` at `/docs`. Before this visual refresh, an HTTPS request to the public site returned `200` and contained the expected product title. The refreshed deployment must be re-checked after merge.

## Conditions and re-run

After deployment, verify the public site in a real browser at desktop and mobile widths; test keyboard navigation and focus visibility; inspect all production links and image loads; verify social-card scraping; and perform a representative screen-reader pass. Host installation and activation remain separately unverified because they require the target hosts.

## Scope boundary

This review does not certify language quality, cultural authority, translation correctness, host behavior, or formal accessibility conformance.
