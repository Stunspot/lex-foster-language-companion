#!/usr/bin/env python3
"""Build the reconciled Lex Foster customer release deterministically."""

from __future__ import annotations
import hashlib, json, shutil, sys, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OLD, VERSION = "0.1.0", "0.1.1"
SLUG, TITLE = "lex-foster-language-companion", "Lex Foster Language Companion"
SOURCE_BASIS = "d2b45a2fb4c6bc2e33e7f5d4d41eba86d1ac4d82"
STAMP = (2026, 8, 14, 0, 0, 0)
COPY_IGNORE = shutil.ignore_patterns('__pycache__', '*.pyc', '*.pyo')

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

def files(root: Path):
    return sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(root).as_posix())

def inventory(root: Path):
    return [{"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size, "sha256": sha(p.read_bytes())} for p in files(root)]

def tree_digest(root: Path) -> str:
    raw = json.dumps(inventory(root), ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return sha(raw)

def zip_tree(path: Path, root: Path, prefix: str = "") -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in files(root):
            relative = source.relative_to(root).as_posix()
            info = zipfile.ZipInfo(f"{prefix}/{relative}" if prefix else relative, STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, source.read_bytes())

def replace_versions(root: Path) -> None:
    replacements = [
        (f"lex-foster-language-companion-v{OLD}", f"lex-foster-language-companion-v{VERSION}"),
        (f"release-v{OLD}", f"release-v{VERSION}"),
        (f"v{OLD}", f"v{VERSION}"),
        (OLD, VERSION),
    ]
    for path in files(root):
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".zip"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for old, new in replacements:
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8", newline="\n")

def safe_recreate(path: Path, parent: Path) -> None:
    if path.resolve().parent != parent.resolve():
        raise RuntimeError(f"unsafe generated target: {path}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)

def main() -> int:
    old_source = REPO / "source" / f"{SLUG}-v{OLD}"
    source = REPO / "source" / f"{SLUG}-v{VERSION}"
    safe_recreate(source, REPO / "source")
    shutil.copytree(old_source, source, dirs_exist_ok=True, ignore=COPY_IGNORE)
    replace_versions(source)
    build_note = source / "BUILD-NOTE.md"
    build_note.write_text(
        build_note.read_text(encoding="utf-8").replace(
            r"E:\Github\lex-foster-language-companion",
            "https://github.com/Stunspot/lex-foster-language-companion",
        ),
        encoding="utf-8", newline="\n",
    )
    dist = REPO / "dist" / "claude" / SLUG
    if dist.exists():
        shutil.rmtree(dist)
    shutil.copytree(source / "skills" / SLUG, dist, ignore=COPY_IGNORE)

    release = REPO / f"release-v{VERSION}"
    safe_recreate(release, REPO)
    skill = release / "codex" / SLUG
    shutil.copytree(source / "skills" / SLUG, skill, ignore=COPY_IGNORE)
    maintainer = release / "maintainer-source" / f"{SLUG}-v{VERSION}"
    shutil.copytree(source, maintainer, ignore=COPY_IGNORE)

    old_release = REPO / f"release-v{OLD}"
    for relative in ["README.md", "START-HERE.md", "HOST-MATRIX.md", "PROVENANCE.md"]:
        shutil.copy2(old_release / relative, release / relative)
    shutil.copytree(old_release / "docs", release / "docs")
    shutil.copy2(REPO / "LICENSE", release / "LICENSE.md")
    shutil.copy2(REPO / "SUPPORT.md", release / "SUPPORT.md")
    shutil.copy2(REPO / "SECURITY.md", release / "SECURITY.md")
    replace_versions(release)

    root_start = release / "START-HERE.md"
    root_start.write_text(
        root_start.read_text(encoding="utf-8")
        .replace("../START-HERE.md", "docs/QUICK-START.md")
        .replace(f"../RELEASE-NOTES-v{VERSION}.md", f"RELEASE-NOTES-v{VERSION}.md")
        .replace("../DOCUMENTATION.md", "PACKAGE-REFERENCE.md")
        .replace("../SUPPORT.md", "SUPPORT.md"),
        encoding="utf-8", newline="\n",
    )
    support = release / "SUPPORT.md"
    support.write_text(
        support.read_text(encoding="utf-8").replace(f"release-v{VERSION}/docs/", "docs/"),
        encoding="utf-8", newline="\n",
    )
    evidence_url = f"https://github.com/Stunspot/lex-foster-language-companion/blob/v{VERSION}/verification/documentation-source-ledger.md"
    for document in (release / "docs").glob("*.md"):
        document.write_text(
            document.read_text(encoding="utf-8")
            .replace("../../SUPPORT.md", "../SUPPORT.md")
            .replace("../../SECURITY.md", "../SECURITY.md")
            .replace("../../DOCUMENTATION.md", "../PACKAGE-REFERENCE.md")
            .replace("../../verification/documentation-source-ledger.md", evidence_url),
            encoding="utf-8", newline="\n",
        )

    guide = release / "docs" / "MAINTAINER-GUIDE.md"
    guide.write_text(guide.read_text(encoding="utf-8").replace(
        f"source/{SLUG}-v{VERSION}/", f"maintainer-source/{SLUG}-v{VERSION}/"
    ), encoding="utf-8", newline="\n")

    notes = f"""# {TITLE} v{VERSION} release notes

Version {VERSION} reconciles the unchanged language-companion runtime with the later customer documentation, recovery, accessibility, presentation, and package-reference work on main.

## Changed

- Includes the complete current customer and maintainer documentation set.
- Includes the deterministic validator tests promised by the package reference.
- Rebuilds Codex and Claude distributions from one byte-identical canonical source.
- Adds deterministic package construction, exact file custody, and fresh release verification.
- Preserves v{OLD} as historical evidence rather than rewriting it in place.

## Runtime behavior

The tutoring, translation, cultural-context, pronunciation, learner-state, privacy, and high-stakes operating method is unchanged from v{OLD}. This is a documentation and package-custody release.

## Evidence boundary

Static validation establishes package structure, source parity, archive safety, hashes, tests, and documentation consistency for the exact artifact. It does not establish live host installation, discovery, invocation, audio assessment, translation approval, accessibility conformance, or customer outcomes.
"""
    (REPO / f"RELEASE-NOTES-v{VERSION}.md").write_text(notes, encoding="utf-8", newline="\n")
    (release / f"RELEASE-NOTES-v{VERSION}.md").write_text(notes, encoding="utf-8", newline="\n")

    package_reference = f"""# Package reference

| Path | Purpose |
| --- | --- |
| START-HERE.md | Shortest path from download to first useful request |
| README.md | Product and evidence overview |
| LICENSE.md | Public MIT license |
| HOST-MATRIX.md | Host-specific proof and untested boundaries |
| PROVENANCE.md | Identity and source custody |
| RELEASE-NOTES-v{VERSION}.md | Customer-visible changes and evidence limits |
| SHA256SUMS.txt | Codex tree and Claude archive digests |
| release-manifest.json | Complete customer-tree inventory |
| codex/{SLUG}/ | Complete Codex skill folder |
| claude/{SLUG}-v{VERSION}.zip | Complete Claude skill archive |
| maintainer-source/{SLUG}-v{VERSION}/ | Canonical source copied at exact byte parity |
| docs/ | Customer procedures, workflows, recovery, trust, and maintenance |

Runtime installation uses the complete Codex skill folder or the untouched Claude ZIP. Maintainer source, customer documentation, manifests, and release records are package custody rather than runtime cargo.
"""
    (release / "PACKAGE-REFERENCE.md").write_text(package_reference, encoding="utf-8", newline="\n")

    claude_dir = release / "claude"
    claude_dir.mkdir()
    claude_zip = claude_dir / f"{SLUG}-v{VERSION}.zip"
    stage = REPO / f".{SLUG}-claude-v{VERSION}"
    if stage.exists():
        shutil.rmtree(stage)
    shutil.copytree(skill, stage / SLUG, ignore=COPY_IGNORE)
    zip_tree(claude_zip, stage)
    shutil.rmtree(stage)

    codex_hash, claude_hash = tree_digest(skill), sha(claude_zip.read_bytes())
    (release / "SHA256SUMS.txt").write_text(
        f"{codex_hash}  codex/{SLUG}/\n{claude_hash}  claude/{claude_zip.name}\n",
        encoding="utf-8", newline="\n"
    )

    package_inventory = inventory(release)
    manifest = {
        "schema": "collaborative-dynamics.customer-skill-family/v2",
        "product": TITLE, "slug": SLUG, "version": VERSION,
        "source_repository": "https://github.com/Stunspot/lex-foster-language-companion",
        "source_basis_commit": SOURCE_BASIS,
        "source_tree_sha256": tree_digest(source),
        "tree_digest_algorithm": "sha256(canonical JSON inventory sorted by relative path; fields path, bytes, sha256)",
        "license": "MIT", "publication": "manual_only",
        "top_level_directory": f"{SLUG}-v{VERSION}",
        "claim_boundary": "Static package and byte-custody evidence only; host and customer outcomes require separate observation.",
        "distributions": {
            "codex_skill": {"path": f"codex/{SLUG}", "file_count": len(files(skill)), "tree_sha256": codex_hash},
            "claude_skill": {"path": f"claude/{claude_zip.name}", "bytes": claude_zip.stat().st_size, "sha256": claude_hash},
            "maintainer_source": {"path": f"maintainer-source/{SLUG}-v{VERSION}", "tree_sha256": tree_digest(maintainer)},
        },
        "files": package_inventory,
    }
    write_json(release / "release-manifest.json", manifest)

    assets = REPO / "release-assets" / f"v{VERSION}"
    safe_recreate(assets, REPO / "release-assets")
    archive = assets / f"Lex-Foster-Language-Companion-v{VERSION}.zip"
    zip_tree(archive, release, f"{SLUG}-v{VERSION}")
    archive_hash = sha(archive.read_bytes())
    (assets / f"{archive.name}.sha256").write_text(f"{archive_hash}  {archive.name}\n", encoding="utf-8", newline="\n")
    with zipfile.ZipFile(archive) as opened:
        members = len(opened.namelist())
    write_json(assets / "receipt.json", {
        "schema": "cd-settled-family-build-receipt/v1", "family": SLUG, "version": VERSION,
        "status": "canonical-built-backup-pending", "canonical_zip": archive.name,
        "canonical_checksum": f"{archive.name}.sha256", "canonical_zip_sha256": archive_hash,
        "canonical_zip_member_count": members, "backup": None, "backup_checksum": None,
        "backup_sha256": None, "copy_not_move_verified": False,
    })
    print(json.dumps({"archive": str(archive), "sha256": archive_hash, "members": members, "codex_files": len(files(skill))}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())