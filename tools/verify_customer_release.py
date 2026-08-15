#!/usr/bin/env python3
"""Verify one expanded Lex Foster customer release and optional outer archive."""

from __future__ import annotations
import argparse, hashlib, io, json, re, sys, zipfile
from pathlib import Path, PurePosixPath

SLUG = "lex-foster-language-companion"
PRIVATE = re.compile(r"(?i)(?:C:[\\/]+Users[\\/]+user|E:[\\/]+(?:Github|Indranet))")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FORBIDDEN_CARGO = re.compile(r"(?i)(?:^|/)(?:__pycache__(?:/|$)|[^/]+\.(?:pyc|pyo)$)")

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def inventory(root: Path):
    return [{"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size, "sha256": sha(p.read_bytes())}
            for p in sorted((x for x in root.rglob("*") if x.is_file()), key=lambda x: x.relative_to(root).as_posix())]

def tree_digest(root: Path) -> str:
    raw = json.dumps(inventory(root), ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return sha(raw)

def safe_name(name: str) -> bool:
    if not name or "\\" in name or "\x00" in name or name.startswith("/"):
        return False
    parts = PurePosixPath(name[:-1] if name.endswith("/") else name).parts
    return bool(parts) and all(p not in {"", ".", ".."} and ":" not in p for p in parts)

def inspect_zip(data: bytes, label: str, findings: list[str]) -> int:
    count = 0
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            names = archive.namelist()
            if len(names) != len({n.casefold() for n in names}):
                findings.append(f"{label}: duplicate or case-colliding members")
            for info in archive.infolist():
                count += 1
                if not safe_name(info.filename):
                    findings.append(f"{label}: unsafe member {info.filename}")
                if info.flag_bits & 1:
                    findings.append(f"{label}: encrypted member {info.filename}")
                if ((info.external_attr >> 16) & 0o170000) == 0o120000:
                    findings.append(f"{label}: symlink member {info.filename}")
                member = archive.read(info)
                try:
                    if PRIVATE.search(member.decode("utf-8")):
                        findings.append(f"{label}: private topology in {info.filename}")
                except UnicodeDecodeError:
                    pass
    except zipfile.BadZipFile as error:
        findings.append(f"{label}: invalid ZIP: {error}")
    return count

def verify(root: Path, outer: Path | None = None) -> dict:
    root = root.resolve()
    findings: list[str] = []
    try:
        manifest = json.loads((root / "release-manifest.json").read_text(encoding="utf-8"))
    except Exception as error:
        return {"schema": "cd-lex-release-verification/v1", "ok": False, "counts": {}, "findings": [f"manifest: {error}"]}
    version = manifest.get("version")
    if manifest.get("schema") != "collaborative-dynamics.customer-skill-family/v2":
        findings.append("manifest: unexpected schema")
    if not isinstance(version, str) or not version:
        findings.append("manifest: missing version")
        version = "invalid"

    expected = {x.get("path"): x for x in manifest.get("files", []) if isinstance(x, dict)}
    actual = {x["path"]: x for x in inventory(root) if x["path"] != "release-manifest.json"}
    forbidden = sorted(path for path in actual if FORBIDDEN_CARGO.search(path))
    for path in forbidden:
        findings.append(f"forbidden generated cargo: {path}")
    if set(expected) != set(actual):
        findings.append("manifest: file set differs")
    for path in sorted(set(expected) & set(actual)):
        if expected[path].get("bytes") != actual[path]["bytes"] or expected[path].get("sha256") != actual[path]["sha256"]:
            findings.append(f"manifest: byte/hash mismatch {path}")

    skill = root / "codex" / SLUG
    maint = root / "maintainer-source" / f"{SLUG}-v{version}" / "skills" / SLUG
    if inventory(skill) != inventory(maint):
        findings.append("source parity: Codex and maintainer skill differ")

    claude_path = root / "claude" / f"{SLUG}-v{version}.zip"
    try:
        with zipfile.ZipFile(claude_path) as archive:
            prefix = f"{SLUG}/"
            archived = {n[len(prefix):]: archive.read(n) for n in archive.namelist() if n.startswith(prefix) and not n.endswith("/")}
        codex = {p.relative_to(skill).as_posix(): p.read_bytes() for p in skill.rglob("*") if p.is_file()}
        if archived != codex:
            findings.append("Claude parity: member set or bytes differ from Codex")
    except Exception as error:
        findings.append(f"Claude parity: {error}")

    sums = {}
    try:
        for line in (root / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
            digest, name = line.split("  ", 1)
            sums[name] = digest
        if sums.get(f"codex/{SLUG}/") != tree_digest(skill):
            findings.append("checksums: Codex tree digest differs")
        if sums.get(f"claude/{claude_path.name}") != sha(claude_path.read_bytes()):
            findings.append("checksums: Claude digest differs")
    except Exception as error:
        findings.append(f"checksums: {error}")

    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = raw.strip().split("#", 1)[0].strip(" <>")
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            if not (path.parent / target).resolve().exists():
                findings.append(f"links: {path.relative_to(root).as_posix()} -> {raw}")

    text_files = 0
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        text_files += 1
        if PRIVATE.search(text):
            findings.append(f"private topology: {path.relative_to(root).as_posix()}")

    zip_members = inspect_zip(claude_path.read_bytes(), "Claude ZIP", findings) if claude_path.is_file() else 0
    if outer:
        outer = outer.resolve()
        zip_members += inspect_zip(outer.read_bytes(), "outer ZIP", findings)
        expected_root = f"{SLUG}-v{version}/"
        try:
            with zipfile.ZipFile(outer) as archive:
                outer_files = {n[len(expected_root):]: archive.read(n) for n in archive.namelist() if n.startswith(expected_root) and not n.endswith("/")}
            expanded = {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            if outer_files != expanded:
                findings.append("outer ZIP: member set or bytes differ from expanded release")
        except Exception as error:
            findings.append(f"outer ZIP parity: {error}")

    findings = sorted(set(findings))
    return {"schema": "cd-lex-release-verification/v1", "ok": not findings,
            "counts": {"manifest_files": len(actual), "skill_files": len(inventory(skill)),
                       "text_files": text_files, "zip_members_checked": zip_members},
            "findings": findings}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("release_root", type=Path)
    parser.add_argument("--outer", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    report = verify(args.release_root, args.outer)
    print(json.dumps(report, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if report["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())