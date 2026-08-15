# Host matrix

| Surface | Customer artifact | Structural evidence | Live evidence | Residual boundary |
|---|---|---|---|---|
| Codex | `codex/lex-foster-language-companion/` | Builder Codex profile passed | Not tested | Installation, discovery, activation, resource loading, Python execution, persistence, and restart behavior |
| Claude | `claude/lex-foster-language-companion-v0.1.1.zip` | Pre-ZIP folder and final ZIP passed the Builder Claude profile | Not tested | Upload, enablement, activation, resource loading, Python availability, persistence, and current UI labels |
| Plain text chat | `fallbacks/universal-copy-paste-companion.md` inside the skill | Static inspection | Not tested | No selective package loading, learner-profile validator, host discovery, or built-in persistence |
| GitHub Pages | `docs/` at repository root | Text-only site source and documentation lint passed | Deployed from `main` `/docs`; HTTPS returned `200` with the expected title | Keyboard flow, screen-reader behavior, and representative-user accessibility remain untested |

Structural validation supports package shape, metadata, containment, JSON compatibility, and resource reachability selected by the validator. It does not establish language quality, successful installation, or host behavior.

Use the artifact made for your host. Do not upload the whole release as a Claude skill or copy the Claude ZIP itself into the Codex skills directory.