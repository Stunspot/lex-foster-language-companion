# Host matrix

| Surface | Customer artifact | Structural evidence | Live evidence | Residual boundary |
|---|---|---|---|---|
| Codex | `codex/lex-foster-language-companion/` | Builder Codex profile passed | Not tested | Installation, discovery, activation, resource loading, Python execution, persistence, and restart behavior |
| Claude | `claude/lex-foster-language-companion-v0.1.0.zip` | Pre-ZIP folder and final ZIP passed the Builder Claude profile | Not tested | Upload, enablement, activation, resource loading, Python availability, persistence, and current UI labels |
| Plain text chat | `fallbacks/universal-copy-paste-companion.md` inside the skill | Static inspection | Not tested | No selective package loading, learner-profile validator, host discovery, or built-in persistence |
| GitHub Pages | `docs/` at repository root | Responsive HTML/CSS, JPEG assets, social-preview metadata, and documentation lint | Deployed from `main` `/docs`; HTTPS previously returned `200` with the expected title | Post-refresh browser rendering, keyboard flow, screen-reader behavior, link integrity, and representative-user accessibility require re-checking |

Structural validation supports package shape, metadata, containment, JSON compatibility, and resource reachability selected by the validator. It does not establish language quality, successful installation, or host behavior.

Use the artifact made for your host. Do not upload the whole release as a Claude skill or copy the Claude ZIP itself into the Codex skills directory.
