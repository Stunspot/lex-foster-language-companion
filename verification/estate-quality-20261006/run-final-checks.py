from pathlib import Path
import subprocess,json,sys,hashlib
R=Path(r'E:\Github\lex-foster-language-companion');V=R/'verification/estate-quality-20261006';S=R/'source/lex-foster-language-companion-v0.1.1/skills/lex-foster-language-companion';py=sys.executable
H=Path(r'C:\Users\user\.codex\plugins\cache\personal\scribe-hesperos-clearpath\0.1.3\skills\hesperos-documentation')
results=[]
def run(label,args):
 cp=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',errors='replace');(V/(label+'.txt')).write_text(cp.stdout+cp.stderr,encoding='utf-8');results.append(dict(label=label,exit_code=cp.returncode,log=str(V/(label+'.txt'))));print(label,cp.returncode);return cp
build=run('final-build',[py,'-B','-X','utf8',str(R/'tools/build_customer_release.py'),'--output',str(R/'dist/estate-quality-20261006-r4')]);assert build.returncode==0,build.stderr
info=json.loads(build.stdout);archive=Path(info['archive']);dest=V/'native-r4'
assert not dest.exists()
ps="Expand-Archive -LiteralPath '"+str(archive)+"' -DestinationPath '"+str(dest)+"'"
cp=run('native-extract',['powershell','-NoProfile','-Command',ps]);assert cp.returncode==0,cp.stderr
ex=dest/'lex-foster-language-companion-v0.1.1';es=ex/'codex/lex-foster-language-companion'
run('final-source-tests',[py,'-B','-X','utf8','-m','unittest','discover','-s',str(S/'scripts/tests'),'-v'])
run('final-package-tests',[py,'-B','-X','utf8','-m','unittest','discover','-s',str(R/'tests'),'-v'])
run('native-runtime-tests',[py,'-B','-X','utf8','-m','unittest','discover','-s',str(es/'scripts/tests'),'-v'])
run('native-verifier',[py,'-B','-X','utf8',str(ex/'tools/verify_customer_release.py'),str(ex),'--outer',str(archive),'--pretty'])
run('public-docs-static',[py,'-B','-X','utf8',str(R/'tools/verify_public_docs.py')])
run('authorship-validation',[py,'-B','-X','utf8',str(H/'scripts/hesperos_authorship.py'),'validate','--root',str(R),'--receipt',str(V/'authorship/documentation-authorship.json'),'--capability-entrypoint',str(H/'SKILL.md')])
docs=json.loads((V/'authorship/documentation-manifest.json').read_text())['customer_docs'];run('customer-docs-lint',[py,'-B','-X','utf8',str(H/'scripts/lint_accessible_markdown.py'),'--root',str(R),'--check-links',*[str(R/p) for p in docs if p.endswith('.md')]])
rebuild=run('native-rebuild',[py,'-B','-X','utf8',str(ex/'tools/build_customer_release.py'),'--output',str(V/'rebuilt-r4')]);assert rebuild.returncode==0,rebuild.stderr
rebuilt=json.loads(rebuild.stdout);identical=hashlib.sha256(archive.read_bytes()).hexdigest()==rebuilt['sha256'];assert identical
ps=". 'E:\\Indranet\\Nova\\projects\\project-records\\projects\\augment-estate-quality-repair\\records\\scripts\\estate_extra_preflight.ps1'; Assert-EstateExtra -Path '"+str(R/'delivery-sidecars/Lex Foster Language Companion T-Free v0.1.1 Extra.md')+"' -Version '0.1.1'"
run('extra-preflight',['powershell','-NoProfile','-Command',ps])
(V/'final-checks.json').write_text(json.dumps(dict(candidate=info,checks=results,reproducible_from_native_extraction=identical),indent=2)+'\n',encoding='utf-8')