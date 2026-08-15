#!/usr/bin/env python3
"""Static semantics, routes, anchors, and asset checks for Lex public docs."""

from __future__ import annotations
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / "docs"
PAGES_PREFIX = "/lex-foster-language-companion/"

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.title_depth = 0
        self.title = ""
        self.ids = set()
        self.refs = []
        self.h1 = 0
        self.main_ids = []
        self.images = []
        self.meta = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang")
        if tag == "title": self.title_depth += 1
        if a.get("id"): self.ids.add(a["id"])
        if tag in {"a", "link"} and a.get("href"): self.refs.append(a["href"])
        if tag in {"img", "script"} and a.get("src"): self.refs.append(a["src"])
        if tag == "h1": self.h1 += 1
        if tag == "main": self.main_ids.append(a.get("id"))
        if tag == "img": self.images.append(a)
        if tag == "meta": self.meta.append(a)
    def handle_endtag(self, tag):
        if tag == "title": self.title_depth = max(0, self.title_depth - 1)
    def handle_data(self, data):
        if self.title_depth: self.title += data

def local_target(page: Path, raw: str):
    parts = urlsplit(raw)
    if parts.scheme or raw.startswith(("mailto:", "tel:", "data:", "//")):
        return None, parts.fragment
    path = unquote(parts.path)
    if path.startswith(PAGES_PREFIX):
        target = DOCS / path[len(PAGES_PREFIX):]
    elif path.startswith("/"):
        return None, parts.fragment
    else:
        target = page.parent / path if path else page
    if target.is_dir(): target = target / "index.html"
    return target.resolve(), parts.fragment

def main() -> int:
    findings = []
    pages = {}
    for path in sorted(DOCS.glob("*.html")):
        parser = Page()
        parser.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parser
        if parser.lang != "en": findings.append(f"{path.name}: html lang is not en")
        if not parser.title.strip(): findings.append(f"{path.name}: missing title")
        if parser.h1 != 1: findings.append(f"{path.name}: expected one h1, found {parser.h1}")
        if "main" not in parser.main_ids: findings.append(f"{path.name}: main landmark lacks id main")
        if not any(ref == "#main" for ref in parser.refs): findings.append(f"{path.name}: missing skip target link")
        for image in parser.images:
            if "alt" not in image: findings.append(f"{path.name}: image lacks alt attribute")
        types = [m.get("content") for m in parser.meta if m.get("property") == "og:image:type"]
        if path.name != "404.html" and types != ["image/jpeg"]:
            findings.append(f"{path.name}: expected one JPEG Open Graph image type, got {types}")
        if ".svg" in path.read_text(encoding="utf-8").lower():
            findings.append(f"{path.name}: SVG reference present")

    for page, parser in pages.items():
        for raw in parser.refs:
            target, fragment = local_target(page, raw)
            if target is None: continue
            if not target.exists():
                findings.append(f"{page.name}: missing local target {raw}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_page = pages.get(target)
                if target_page is None:
                    probe = Page(); probe.feed(target.read_text(encoding="utf-8")); target_page = probe
                if fragment not in target_page.ids:
                    findings.append(f"{page.name}: missing anchor {raw}")

    css = (DOCS / "style.css").read_text(encoding="utf-8")
    for required in [":focus-visible", "prefers-reduced-motion", "@media (max-width: 50rem)", "@media print"]:
        if required not in css: findings.append(f"style.css: missing {required}")

    root_docs = ["README.md","START-HERE.md","DOCUMENTATION.md","ACCESSIBILITY.md","SECURITY.md","SUPPORT.md","CONTRIBUTING.md","RELEASE-NOTES-v0.1.1.md"]
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for name in root_docs:
        path = REPO / name
        for raw in pattern.findall(path.read_text(encoding="utf-8")):
            parts = urlsplit(raw)
            if parts.scheme or raw.startswith(("mailto:", "tel:", "data:", "//")):
                continue
            target_text = unquote(parts.path)
            if not target_text:
                continue
            target = (path.parent / target_text).resolve()
            if not target.exists():
                findings.append(f"{name}: missing local target {raw}")

    findings = sorted(set(findings))
    report = {"schema":"cd-lex-public-docs-verification/v1","ok":not findings,
              "counts":{"html_pages":len(pages),"root_markdown":len(root_docs),
                        "images":sum(len(p.images) for p in pages.values())},
              "findings":findings}
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())