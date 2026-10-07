#!/usr/bin/env python3
"""Build a new verified candidate from current source; never replace an accepted release."""
from __future__ import annotations
import argparse, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path
from package_safety import files, inventory, reject_links, sha, tree_digest, zip_tree
from verify_customer_release import verify
REPO=Path(__file__).resolve().parents[1]
VERSION='0.1.1'; SLUG='lex-foster-language-companion'; TITLE='Lex Foster Language Companion'

def write_json(p,value):p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def copy_tree(source,target):
    for p in files(source):
        dst=target/p.relative_to(source);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst)

def build(output):
    source=REPO/'source'/f'{SLUG}-v{VERSION}'
    docs=REPO/f'release-v{VERSION}'
    if not source.is_dir():source=REPO/'maintainer-source';docs=REPO
    runtime=source/'skills'/SLUG
    # Inspect source/documentation/tools before creating output. Parent links are rejected too.
    files(source);files(docs/'docs');files(REPO/'tools')
    check=subprocess.run([sys.executable,'-B',str(runtime/'scripts/validate_release.py'),str(runtime)],capture_output=True,text=True,encoding='utf-8')
    if check.returncode:raise ValueError('runtime validation failed: '+check.stderr.strip())
    output=reject_links(output)
    for protected in (source,docs/'docs',REPO/'tools',REPO/f'release-v{VERSION}',REPO/'release-assets'):
        if output==protected or output in protected.parents or protected in output.parents:
            raise ValueError(f'output overlaps maintained source or accepted release: {output}')
    if output.exists():raise ValueError(f'output already exists; use a new revision: {output}')
    output.parent.mkdir(parents=True,exist_ok=True);reject_links(output.parent)
    with tempfile.TemporaryDirectory(prefix='.lex-candidate-',dir=output.parent) as temp:
        stage=Path(temp); release=stage/f'{SLUG}-v{VERSION}';release.mkdir()
        for p in sorted(docs.glob('*.md')):
            reject_links(p);shutil.copyfile(p,release/p.name)
        copy_tree(docs/'docs',release/'docs')
        copy_tree(runtime,release/'codex'/SLUG)
        copy_tree(source,release/'maintainer-source')
        for name in ('build_customer_release.py','verify_customer_release.py','package_safety.py'):
            (release/'tools').mkdir(exist_ok=True);shutil.copyfile(REPO/'tools'/name,release/'tools'/name)
        cp=release/'claude'/f'{SLUG}-v{VERSION}.zip';cp.parent.mkdir();zip_tree(cp,runtime,SLUG)
        skill=release/'codex'/SLUG
        (release/'SHA256SUMS.txt').write_text(f'{tree_digest(skill)}  codex/{SLUG}/\n{sha(cp.read_bytes())}  claude/{cp.name}\n',encoding='utf-8',newline='\n')
        manifest=dict(schema='collaborative-dynamics.customer-skill-family/v2',product=TITLE,slug=SLUG,version=VERSION,
            source_repository='https://github.com/Stunspot/lex-foster-language-companion',source_tree_sha256=tree_digest(source),
            top_level_directory=f'{SLUG}-v{VERSION}',publication='manual_only',
            claim_boundary='Declared structure, source parity and package custody only; no live model, learner or host qualification.',
            source_to_package_mapping={'canonical_source':f'source/{SLUG}-v{VERSION}','packaged_copy':'maintainer-source'},
            distributions={'codex_skill':{'path':f'codex/{SLUG}','tree_sha256':tree_digest(skill),'file_count':len(files(skill))},
                'claude_skill':{'path':f'claude/{cp.name}','sha256':sha(cp.read_bytes()),'bytes':cp.stat().st_size},
                'maintainer_source':{'path':'maintainer-source','tree_sha256':tree_digest(source)}}, files=inventory(release))
        write_json(release/'release-manifest.json',manifest)
        archive=stage/f'Lex-Foster-Language-Companion-v{VERSION}.zip';zip_tree(archive,release,f'{SLUG}-v{VERSION}')
        report=verify(release,archive)
        if not report['ok']:raise ValueError('candidate verification failed: '+json.dumps(report['findings']))
        write_json(stage/'verification.json',report)
        archive.with_suffix('.zip.sha256').write_text(f'{sha(archive.read_bytes())}  {archive.name}\n',encoding='utf-8',newline='\n')
        # Rename the entire new directory only after all checks. Existing outputs are never deleted.
        if output.exists():raise ValueError('output appeared during build; nothing replaced')
        os.rename(stage,output)
    return {'archive':str(output/archive.name),'sha256':sha((output/archive.name).read_bytes()),'release':str(output/release.name),'verification':report}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True,help='new candidate directory; must not exist');p.add_argument('--current-only',action='store_true',help='compatibility alias; all builds use current source')
    args=p.parse_args()
    try:report=build(args.output)
    except (OSError,ValueError,UnicodeError) as exc:print(f'FAIL build: {exc}',file=sys.stderr);return 1
    print(json.dumps(report,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
