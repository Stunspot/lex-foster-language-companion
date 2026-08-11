# Independent documentation accessibility review — 2026-08-11

## Result

`PASS_WITH_BOUNDED_EVIDENCE`

Reviewed documentation fingerprint: `93575c3b09bba44508585d08677c2a7acba5217db99a87a42a73de43f31122e8`
Reviewer phase: separate from Hesperos authorship and content approval.

## Surfaces reviewed

- repository README and root customer documentation;
- Pages home, Start, Use Lex, Trust & recovery, and 404 routes;
- complete authored CSS;
- README hero, Pages hero, and social card actual pixels;
- links from current surfaces into the frozen version 0.1.0 customer release.

## Checks and results

| Check | Result | Evidence |
|---|---|---|
| Language and titles | PASS | Every HTML route declares `lang="en"` and has a non-empty descriptive title. |
| Landmarks and bypass | PASS | Every route has one main landmark, primary navigation, and a visible-on-focus skip link. |
| Heading hierarchy | PASS | Every route has exactly one H1; programmatic heading traversal found no skipped levels. |
| Keyboard visibility | PASS in authored source | Links and buttons receive a three-pixel `#ffd166` focus outline with offset; the active documentation route uses `aria-current` plus a text underline. |
| Reflow | PASS in authored source | Fluid widths, one-column breakpoints, wrapped navigation/actions, 20rem minimum viewport, and horizontally scrollable narrow-screen tables are present. |
| Motion | PASS in authored source | Reduced-motion media rules disable smooth scrolling and collapse animation/transition duration. |
| Link purpose | PASS | Labels name tasks or destinations; core customer tasks remain on-site; exact source links are identified by purpose. |
| Nonvisual equivalence | PASS | README hero has informative alternative text; the adjacent-copy Pages hero is decorative with an empty alternative; social metadata supplies an explicit alternative. |
| Color independence | PASS | Status, host, action, evidence, and failure states have text labels; no instruction depends on color. |
| Contrast | PASS for authored palette | Calculated ratios: ink/background 19.17:1, muted/background 14.22:1, quiet/background 9.57:1, blue/background 10.46:1, vermillion/background 6.88:1, focus/background 13.87:1, and dark text/blue button 10.46:1. |
| Cognitive load and recovery | PASS | Task-based routes, progressive disclosure, literal paths, expected results, safe stopping, and symptom-led recovery are present. |
| Visual assets | PASS | All three files were opened; hierarchy, contrast, crop safety, role fit, and text treatment were reviewed from actual pixels. The social title and identifying line remain readable at thumbnail scale. |
| Markdown structure | PASS | Hesperos accessible-Markdown lint passed every current customer-facing Markdown file. |

## Defects found and repaired during this review

- Secondary Pages routes lacked explicit social-image alternative metadata; all metadata-bearing routes now provide it.
- One root documentation sentence used a directional reference that could fail after reflow; it was rewritten to name the linked material.
- The old shared-banner model did not provide honest role-specific image treatment; it was replaced with distinct informative, decorative, and social-preview semantics.

The fingerprint was computed after these repairs. No fingerprinted content changed after this review.

## Limits

This review does not establish formal WCAG conformance, representative-user usability, or compatibility across every browser, screen reader, zoom mode, contrast setting, or input method. No GUI browser, screenshot automation, or screen-reader session was used. Live HTTPS routes, deployed metadata, and delivered asset bytes require the separate post-deployment receipt.

## Invalidation rule

Any change to the reviewed documents, HTML, CSS, navigation, or visual assets invalidates this result and requires a new accessibility review against a new fingerprint.