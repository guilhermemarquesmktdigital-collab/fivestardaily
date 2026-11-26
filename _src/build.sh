#!/bin/bash
# Rebuilds the whole site into the repo root. Usage: bash _src/build.sh
set -e
cd "$(dirname "$0")"
python3 air/content.py
cp fsd/index.bak.html fsd/index.html
python3 air/patch.py fsd/index.html air/sprites.json air/flyers.js
python3 air/patch2.py fsd/index.html air/pages.css air/pages.js
python3 - <<'PY2'
import json
s=open('fsd/index.html').read(); r=open('air/real.js').read()
r=r+'\n'+open('air/articles.js').read().replace('__CONTENT__',json.dumps(json.load(open('air/content.json')),ensure_ascii=False))
r=r.replace('__REAL__',json.dumps(json.load(open('air/realdata.json')),ensure_ascii=False)).replace('__SNAPT__','Nov 13, 2026 5:55 PM ET')
assert '/*__REALJS__*/' in s
s=s.replace('/*__REALJS__*/',r); open('fsd/index.html','w').write(s)
PY2
python3 air/gensite.py .. / https://fivestardaily.com
python3 chat/build_chat.py ..
python3 today/build_today.py ..
python3 air/externalize.py ..
python3 - <<'PY3'
import json
c=json.load(open('air/content.json'))
out=[{"slug":g["slug"],"title":g["title"]["en"],"upd":g.get("upd") or g.get("updated") or ""} for g in c["GUIDES"]]
json.dump(out,open('../admin/guides.json','w'),ensure_ascii=False,indent=1)
PY3
rm -f fsd/index.html air/content.json
