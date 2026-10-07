#!/usr/bin/env python3
"""Verify complete expanded and archived byte custody; no language ability claim."""
from __future__ import annotations
import argparse, json, os, re, sys, zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from package_safety import files, inventory, reject_links, sha, tree_digest, zip_contents
SLUG='lex-foster-language-companion'
PRIVATE=re.compile(r'(?i)(?:C:[\\/]+Users[\\/]+user|E:[\\/]+(?:Github|Indranet))')
LINK=re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')

def inspect_zip(data,label,findings):
    try:return len(zip_contents(data,label))
    except (OSError,ValueError,RuntimeError,zipfile.BadZipFile) as exc:findings.append(f'{label}: {exc}');return 0

def pairs(items):
    result={}
    for k,v in items:
        if k in result:raise ValueError(f'duplicate JSON key: {k}')
        result[k]=v
    return result

def verify(root,outer=None):
    findings=[];counts={}
    try:
        root=reject_links(root).resolve();actual_list=inventory(root)
        for parent, dirs, names in os.walk(root):
            if '__pycache__' in dirs or any(Path(n).suffix in {'.pyc','.pyo'} for n in names): raise ValueError('forbidden generated cache cargo')
        manifest=json.loads((root/'release-manifest.json').read_text(encoding='utf-8-sig'),object_pairs_hook=pairs)
        if not isinstance(manifest,dict):raise ValueError('manifest must be an object')
        if manifest.get('schema')!='collaborative-dynamics.customer-skill-family/v2' or manifest.get('version')!='0.1.1' or manifest.get('slug')!=SLUG:raise ValueError('manifest identity/schema differs')
        expected=manifest.get('files')
        if not isinstance(expected,list) or not expected:raise ValueError('manifest files must be a nonempty array')
        seen=set()
        for item in expected:
            if not isinstance(item,dict) or set(item)!={'path','bytes','sha256'} or not isinstance(item['path'],str) or type(item['bytes']) is not int or item['bytes']<0 or not isinstance(item['sha256'],str) or not re.fullmatch('[a-f0-9]{64}',item['sha256']):raise ValueError('malformed manifest file entry')
            if item['path'] in seen:raise ValueError('duplicate manifest path')
            seen.add(item['path'])
        actual=[x for x in actual_list if x['path']!='release-manifest.json']
        if sorted(expected,key=lambda x:x['path'])!=actual:findings.append('manifest file set/bytes/hash differs')
        d=manifest.get('distributions')
        if not isinstance(d,dict) or any(not isinstance(d.get(k),dict) for k in ('codex_skill','claude_skill','maintainer_source')):raise ValueError('malformed distribution mapping')
        mp=d['maintainer_source'].get('path')
        if mp not in {'maintainer-source',f'maintainer-source/{SLUG}-v0.1.1'}:raise ValueError('unsupported maintainer source mapping')
        skill=root/'codex'/SLUG;source=root/mp;cp=root/'claude'/f'{SLUG}-v0.1.1.zip'
        if d['codex_skill'].get('path')!=f'codex/{SLUG}' or d['claude_skill'].get('path')!=f'claude/{cp.name}':raise ValueError('distribution path mismatch')
        if inventory(skill)!=inventory(source/'skills'/SLUG):findings.append('source parity differs')
        if manifest.get('source_tree_sha256')!=tree_digest(source) or d['maintainer_source'].get('tree_sha256')!=tree_digest(source):findings.append('source tree hash differs')
        if d['codex_skill'].get('tree_sha256')!=tree_digest(skill) or d['codex_skill'].get('file_count')!=len(files(skill)):findings.append('Codex declared digest/count differs')
        if d['claude_skill'].get('sha256')!=sha(cp.read_bytes()) or d['claude_skill'].get('bytes')!=cp.stat().st_size:findings.append('Claude declared bytes/hash differs')
        codex={SLUG+'/'+p.relative_to(skill).as_posix():p.read_bytes() for p in files(skill)}
        archived=zip_contents(cp.read_bytes(),'Claude ZIP')
        if archived!=codex:findings.append('Claude complete namespace or bytes differs')
        sums={}
        for line in (root/'SHA256SUMS.txt').read_text().splitlines():
            digest,name=line.split('  ',1)
            if name in sums:raise ValueError('duplicate checksum entry')
            sums[name]=digest
        if sums!={f'codex/{SLUG}/':tree_digest(skill),f'claude/{cp.name}':sha(cp.read_bytes())}:findings.append('checksums differ')
        for p in files(root):
            if p.suffix not in {'.md','.json','.yaml','.yml','.txt','.py'}:continue
            text=p.read_text(encoding='utf-8')
            if PRIVATE.search(text):findings.append('private topology in '+p.relative_to(root).as_posix())
            if p.suffix!='.md':continue
            for raw in LINK.findall(text):
                u=urlsplit(raw.strip('<>'))
                if u.scheme or raw.startswith('//'):continue
                target=(p.parent/unquote(u.path)).resolve() if u.path else p
                if target!=root and root not in target.parents:findings.append(f'link escapes package: {p.name} -> {raw}')
                elif not target.exists():findings.append(f'missing link: {p.name} -> {raw}')
        if outer:
            outer=reject_links(outer);content=zip_contents(outer.read_bytes(),'outer ZIP')
            prefix=f'{SLUG}-v0.1.1/'
            expanded={prefix+p.relative_to(root).as_posix():p.read_bytes() for p in files(root)}
            if content!=expanded:findings.append('outer complete namespace or bytes differs')
        counts={'files':len(actual_list),'runtime_files':len(files(skill)),'claude_files':len(archived)}
    except (OSError,ValueError,UnicodeError,KeyError,TypeError,RuntimeError,zipfile.BadZipFile) as exc:findings.append(f'controlled verification failure: {exc}')
    return {'schema':'cd-lex-release-verification/v1','ok':not findings,'counts':counts,'findings':sorted(set(findings))}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('release_root',type=Path);p.add_argument('--outer',type=Path);p.add_argument('--pretty',action='store_true');a=p.parse_args()
    result=verify(a.release_root,a.outer);print(json.dumps(result,indent=2 if a.pretty else None));return 0 if result['ok'] else 1
if __name__=='__main__':raise SystemExit(main())
