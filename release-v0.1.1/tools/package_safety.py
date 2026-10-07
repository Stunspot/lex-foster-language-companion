"""Portable tree and archive primitives shared by the builder and verifier."""
from __future__ import annotations
import hashlib, io, json, os, re, stat, unicodedata, zipfile
from pathlib import Path
STAMP=(2026,10,6,0,0,0)
DEVICE=re.compile(r'(?i)^(?:con|prn|aux|nul|com[1-9¹²³]|lpt[1-9¹²³])(?:\.|$)')

def sha(data): return hashlib.sha256(data).hexdigest()
def reject_links(path):
    path=Path(os.path.abspath(path))
    for p in [path,*path.parents]:
        try: s=p.lstat()
        except FileNotFoundError: continue
        if stat.S_ISLNK(s.st_mode) or getattr(s,'st_file_attributes',0)&0x400:
            raise ValueError(f'linked/reparse path is not allowed: {p}')
    return path

def check_names(entries, budget=80):
    namespace={}; explicit=set()
    for name,is_dir in entries:
        if not isinstance(name,str) or not name or '\\' in name or name.startswith('/'):
            raise ValueError(f'unsafe path: {name!r}')
        clean=name[:-1] if is_dir and name.endswith('/') else name
        parts=clean.split('/')
        if len(clean.encode('utf-16-le'))//2+budget>=260: raise ValueError(f'extraction path budget exceeded: {name}')
        for part in parts:
            if part in {'','.','..'} or re.search(r'[<>:"|?*\x00-\x1f]',part) or part.endswith((' ','.')) or DEVICE.match(part) or len(part.encode('utf-8'))>255:
                raise ValueError(f'nonportable path component: {name}')
        full=unicodedata.normalize('NFC',clean).casefold()
        if full in explicit: raise ValueError(f'duplicate/colliding member: {name}')
        explicit.add(full)
        for i in range(1,len(parts)+1):
            raw='/'.join(parts[:i]);key=unicodedata.normalize('NFC',raw).casefold()
            kind='directory' if i<len(parts) or is_dir else 'file'
            if key in namespace and namespace[key]!=(raw,kind): raise ValueError(f'file/directory or normalized alias collision: {name}')
            namespace[key]=(raw,kind)

def files(root):
    root=reject_links(root)
    if not root.is_dir(): raise ValueError(f'missing tree: {root}')
    found=[]
    for parent,dirs,names in os.walk(root,followlinks=False):
        for name in dirs+names:
            p=Path(parent)/name; reject_links(p)
        dirs[:]=[x for x in dirs if x!='__pycache__']
        for name in names:
            p=Path(parent)/name
            if p.suffix in {'.pyc','.pyo'}: continue
            if not p.is_file(): raise ValueError(f'not a regular file: {p}')
            found.append(p)
    found.sort(key=lambda p:p.relative_to(root).as_posix())
    check_names([(p.relative_to(root).as_posix(),False) for p in found])
    return found

def inventory(root):
    root=Path(root)
    return [dict(path=p.relative_to(root).as_posix(),bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in files(root)]
def tree_digest(root):return sha(json.dumps(inventory(root),ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def zip_tree(path,root,prefix=''):
    members=[(p,('/'.join([prefix,p.relative_to(root).as_posix()]) if prefix else p.relative_to(root).as_posix())) for p in files(root)]
    check_names([(name,False) for p,name in members])
    with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_STORED) as z:
        for p,name in members:
            info=zipfile.ZipInfo(name,STAMP);info.compress_type=zipfile.ZIP_STORED;info.external_attr=0o100644<<16;info.create_system=3
            z.writestr(info,p.read_bytes())

def zip_contents(data,label='archive',depth=0):
    if depth>2: raise ValueError(f'{label}: excessive nested archives')
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        infos=z.infolist();check_names([(x.filename,x.is_dir()) for x in infos])
        result={}
        for x in infos:
            mode=(x.external_attr>>16)&0o170000
            if x.flag_bits&1 or mode not in {0,0o100000,0o040000}: raise ValueError(f'{label}: encrypted or nonregular member {x.filename}')
            if (mode == 0o040000 or x.external_attr & 0x10) and not x.is_dir(): raise ValueError(f'{label}: directory metadata on file member {x.filename}')
            if x.is_dir() and mode == 0o100000: raise ValueError(f'{label}: file metadata on directory member {x.filename}')
            if x.is_dir(): continue
            content=z.read(x);result[x.filename]=content
            if x.filename.lower().endswith('.zip'):zip_contents(content,f'{label}/{x.filename}',depth+1)
        return result
