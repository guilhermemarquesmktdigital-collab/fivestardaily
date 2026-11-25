"""Post-build: move the big inline app script out of every page into one cached, hash-named file."""
import glob,hashlib,os,re,sys
root=sys.argv[1]
pat=re.compile(r'<script>(.*?)</script>',re.S)
pages=[p for p in glob.glob(root+'/**/index.html',recursive=True) if '/_src/' not in p and '/node_modules/' not in p]
for old in glob.glob(root+'/assets/app.*.js'):os.remove(old)
n=0
for p in pages:
    s=open(p).read()
    big=[m for m in pat.finditer(s) if len(m.group(1))>100000]
    if len(big)!=1:continue
    m=big[0];code=m.group(1);h=hashlib.md5(code.encode()).hexdigest()[:10]
    os.makedirs(root+'/assets',exist_ok=True)
    f=root+'/assets/app.'+h+'.js'
    if not os.path.exists(f):open(f,'w').write(code)
    s=s[:m.start()]+'<script src="/assets/app.'+h+'.js"></script>'+s[m.end():]
    open(p,'w').write(s);n+=1
print('externalized',n,'pages;',len(glob.glob(root+'/assets/app.*.js')),'js files')
