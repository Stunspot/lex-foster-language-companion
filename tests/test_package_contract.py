import copy, io, json, os, shutil, subprocess, sys, tempfile, unittest, zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'tools'))
import build_customer_release as b
from package_safety import check_names, files, inventory, sha, zip_contents
from verify_customer_release import verify
class PackageContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory();cls.base=Path(cls.tmp.name);cls.output=cls.base/'valid';cls.report=b.build(cls.output);cls.release=Path(cls.report['release'])
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def test_current_flat_source_parity(self):self.assertTrue(verify(self.release,Path(self.report['archive']))['ok'])
    def test_reproducible_rebuild_from_download(self):
        out=self.base/'rebuild';p=subprocess.run([sys.executable,'-B',str(self.release/'tools/build_customer_release.py'),'--output',str(out)],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr);self.assertEqual(sha(Path(self.report['archive']).read_bytes()),sha((out/Path(self.report['archive']).name).read_bytes()))
    def test_existing_destination_untouched(self):
        before=inventory(self.output)
        with self.assertRaises(ValueError):b.build(self.output)
        self.assertEqual(before,inventory(self.output))
    def test_namespace_and_device_names(self):
        cases=[[('CON.txt',False)],[('a',False),('a/b',False)],[('A/b',False),('a/c',False)],[('e\u0301.txt',False),('\u00e9.txt',False)],[('../x',False)],[('x./y',False)],[('x'*181,False)]]
        for case in cases:
            with self.subTest(case=case),self.assertRaises(ValueError):check_names(case)
    def test_zip_file_directory_collision(self):
        stream=io.BytesIO()
        with zipfile.ZipFile(stream,'w') as z:z.writestr('a','x');z.writestr('a/b','y')
        with self.assertRaises(ValueError):zip_contents(stream.getvalue())
    def test_bad_manifest_values_are_controlled(self):
        for mutation in ('null-files','duplicate-path','wrong-type','escape-source'):
            with tempfile.TemporaryDirectory() as d:
                root=Path(d)/'r';shutil.copytree(self.release,root);p=root/'release-manifest.json';j=json.loads(p.read_text())
                if mutation=='null-files':j['files']=None
                if mutation=='duplicate-path':j['files'].append(j['files'][0])
                if mutation=='wrong-type':j['files'][0]['bytes']='12'
                if mutation=='escape-source':j['distributions']['maintainer_source']['path']='../../outside'
                p.write_text(json.dumps(j));self.assertFalse(verify(root)['ok'])
    def test_outer_extra_prefix_not_ignored(self):
        p=self.base/'extra.zip';shutil.copyfile(self.report['archive'],p)
        with zipfile.ZipFile(p,'a') as z:z.writestr('unrelated.txt','unexpected')
        self.assertFalse(verify(self.release,p)['ok'])
    def test_missing_runtime_blocks_build_without_source_change(self):
        # Exercise the actual downloaded-package rebuild path in an isolated clone.
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'r';shutil.copytree(self.release,root);missing=root/'maintainer-source/skills/lex-foster-language-companion/scripts/validate_learner_profile.py';missing.unlink();before=inventory(root);out=Path(d)/'new'
            run=subprocess.run([sys.executable,'-B',str(root/'tools/build_customer_release.py'),'--output',str(out)],capture_output=True)
            self.assertNotEqual(run.returncode,0);self.assertFalse(out.exists());self.assertEqual(before,inventory(root))
    def test_junction_root_rejected(self):
        if os.name!='nt':self.skipTest('Windows junction test')
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'outside';target.mkdir();(target/'secret.txt').write_text('fixture bytes');link=Path(d)/'link'
            cp=subprocess.run(['cmd','/c','mklink','/J',str(link),str(target)],capture_output=True)
            if cp.returncode:self.skipTest('junction privilege unavailable')
            with self.assertRaises(ValueError):files(link)
    def test_all_public_cli_help(self):
        for name in ('build_customer_release.py','verify_customer_release.py'):
            p=subprocess.run([sys.executable,'-B',str(R/'tools'/name),'--help'],capture_output=True);self.assertEqual(p.returncode,0,p.stderr)
if __name__=='__main__':unittest.main()
