#!/usr/bin/env python3
"""Check the accepted release through a fresh, non-overwriting build."""
from pathlib import Path
import hashlib, json, os, subprocess, sys, tempfile
ROOT = Path(__file__).resolve().parents[1]
def run(*args):
    subprocess.run([sys.executable, '-B', '-X', 'utf8', *map(str,args)], cwd=ROOT, check=True, env={**os.environ, 'PYTHONUTF8':'1', 'PYTHONDONTWRITEBYTECODE':'1'})
def main():
    receipt=json.loads((ROOT/'release-assets/v0.1.1/receipt.json').read_text(encoding='utf-8'))
    accepted=ROOT/'release-assets/v0.1.1/Lex-Foster-Language-Companion-v0.1.1.zip'
    expected=receipt['canonical_zip_sha256']
    assert hashlib.sha256(accepted.read_bytes()).hexdigest()==expected, 'Accepted ZIP receipt mismatch'
    with tempfile.TemporaryDirectory(prefix='lex-ci-', dir=ROOT.parent.resolve()) as temp:
        output=Path(temp)/'candidate'
        os.environ.update(TMP=temp, TEMP=temp, TMPDIR=temp)
        tempfile.tempdir=temp
        run('tools/build_customer_release.py','--output',output)
        archive=output/accepted.name
        assert archive.read_bytes()==accepted.read_bytes(), 'Fresh build differs from accepted ZIP'
        native=output/'lex-foster-language-companion-v0.1.1'
        run('tools/verify_customer_release.py',native,'--outer',archive)
        runtime=native/'codex/lex-foster-language-companion'
        run('-m','unittest','discover','-s',runtime/'scripts/tests','-v')
        run(runtime/'scripts/validate_release.py',runtime)
        run('-m','unittest','discover','-s','tests','-v')
    run('tools/verify_public_docs.py')
    run('tools/build_documentation_fingerprint.py','--check')
    print('PASS: fresh candidate is byte-identical; native/runtime/package/public-doc checks passed')
if __name__=='__main__':main()
