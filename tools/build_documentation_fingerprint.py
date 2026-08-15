#!/usr/bin/env python3
"""Bind the current Lex customer documentation to an exact file fingerprint."""

from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
VERSION = "0.1.1"
ROOT_DOCS = ["README.md","START-HERE.md","DOCUMENTATION.md","ACCESSIBILITY.md","SECURITY.md","SUPPORT.md","CONTRIBUTING.md",f"RELEASE-NOTES-v{VERSION}.md"]
WEB = ["docs/README.md","docs/index.html","docs/start.html","docs/guide.html","docs/trust.html","docs/404.html","docs/style.css",
       "docs/assets/lex-foster-readme-hero.png","docs/assets/lex-foster-pages-hero.png","docs/assets/lex-foster-social-card.jpg"]
RELEASE_TOP = [f"release-v{VERSION}/{name}" for name in ["README.md","START-HERE.md","HOST-MATRIX.md","PROVENANCE.md","PACKAGE-REFERENCE.md","SUPPORT.md","SECURITY.md",f"RELEASE-NOTES-v{VERSION}.md"]]
RELEASE_DOCS = [p.relative_to(REPO).as_posix() for p in sorted((REPO/f"release-v{VERSION}"/"docs").glob("*.md"))]
PATHS = sorted(ROOT_DOCS + WEB + RELEASE_TOP + RELEASE_DOCS)

def canonical_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
        data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='verify committed receipts without rewriting them')
    args = parser.parse_args()
    records = []
    aggregate = hashlib.sha256()
    for relative in PATHS:
        path = REPO / relative
        digest = hashlib.sha256(canonical_bytes(path)).hexdigest()
        records.append({"path":relative,"sha256":digest})
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii"))
        aggregate.update(b"\n")
    result = {
        "format":"lex-documentation-fingerprint/v1",
        "generated_at":datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),
        "product_version":VERSION,
        "aggregate_sha256":aggregate.hexdigest(),
        "files":records,
        "algorithm":"sha256 over sorted UTF-8 path NUL canonical file-sha256 records with ordinal path ordering; text line endings normalized to LF",
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    current = REPO/"verification"/"documentation-fingerprint.json"
    versioned = REPO/"verification"/f"documentation-fingerprint-v{VERSION}.json"
    if args.check:
        errors = []
        for path in (current, versioned):
            recorded = json.loads(path.read_text(encoding="utf-8"))
            if recorded.get("files") != records or recorded.get("aggregate_sha256") != result["aggregate_sha256"]:
                errors.append(str(path.relative_to(REPO)))
        print(json.dumps({"ok":not errors,"files":len(records),"aggregate_sha256":result["aggregate_sha256"],"mismatches":errors},indent=2))
        return 0 if not errors else 1
    current.write_text(text,encoding="utf-8",newline="\n")
    versioned.write_text(text,encoding="utf-8",newline="\n")
    print(json.dumps({"files":len(records),"aggregate_sha256":result["aggregate_sha256"]},indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())