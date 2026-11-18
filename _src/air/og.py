"""Makes the 1200x630 share images (og/default.jpg + one per guide/news). Run: python3 _src/air/og.py  (only builds missing ones; --all rebuilds)."""
import os, sys, json, html, base64
from playwright.sync_api import sync_playwright
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(H + '/../..')
OUT = H + '/og'; os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, H)
import content as C
import io
from PIL import Image
_im = Image.open(ROOT + '/img/island.webp').convert('RGB'); _bf = io.BytesIO(); _im.save(_bf, 'JPEG', quality=90)
art = base64.b64encode(_bf.getvalue()).decode()
STAR = '<svg width="34" height="34" viewBox="0 0 24 24"><path fill="#FFD166" d="M12 2l2.9 6.6 7.1.6-5.4 4.7 1.7 7-6.3-3.8-6.3 3.8 1.7-7L2 9.2l7.1-.6z"/></svg>'
def card(kind, title, sub):
    big = kind == 'default'
    chip = '' if big else f'<div class="chip">{kind}</div>'
    fs = 78 if big else (62 if len(title) < 70 else 50)
    return f'''<html><body style="margin:0"><div class="c"><style>
.c{{width:1200px;height:630px;position:relative;overflow:hidden;font-family:Inter,'DejaVu Sans',sans-serif;color:#fff;background:#1a0b3b}}
.bg{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{art}) center 52%/cover}}
.sh{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(20,8,48,.78) 0%,rgba(20,8,48,.42) 50%,rgba(20,8,48,0) 85%),linear-gradient(0deg,rgba(14,6,34,.55),rgba(14,6,34,0) 35%)}}
.in{{position:absolute;left:70px;top:58px;right:70px;bottom:54px;display:flex;flex-direction:column}}
.br{{display:flex;align-items:center;gap:12px;font-weight:800;letter-spacing:.22em;font-size:24px}}.stars{{display:flex;gap:2px}}
.chip{{margin-top:54px;align-self:flex-start;padding:8px 18px;border-radius:99px;background:#FF3D8B;font-weight:800;letter-spacing:.14em;font-size:20px}}
h1{{margin:{('70px' if big else '22px')} 0 0;max-width:820px;font-size:{fs}px;line-height:1.06;font-weight:800;letter-spacing:-.02em;text-shadow:0 3px 24px rgba(0,0,0,.5)}}
h1 em{{font-style:normal;color:#FFD166}}
.sub{{margin-top:26px;font-size:27px;line-height:1.3;color:#e9dcff;max-width:760px}}
.ft{{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:22px;color:#d9c8ff;font-weight:600}}
.ft b{{color:#fff;font-weight:800;letter-spacing:.04em}}
</style><div class="bg"></div><div class="sh"></div><div class="in">
<div class="br"><span class="stars">{STAR*5}</span>FIVE STAR DAILY</div>{chip}
<h1>{title}</h1>{('<div class="sub">'+html.escape(sub)+'</div>') if sub else ''}
<div class="ft"><span>Unofficial GTA 6 fan hub</span><b>fivestardaily.com</b></div></div></div></body></html>'''
jobs = [('default', 'default', 'GTA 6 <em>news, videos,</em> live streams &amp; guides', 'Daily summaries in English, Spanish and Portuguese')]
for g in C.GUIDES: jobs.append(('guide', 'guides-' + g['slug'], html.escape(g['title']['en']), ''))
for n in C.NEWS: jobs.append(('news', 'news-' + n['slug'], html.escape(n['title']['en']), ''))
todo = [j for j in jobs if '--all' in sys.argv or not os.path.exists(f'{OUT}/{j[1]}.jpg')]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 630})
    for kind, name, title, sub in todo:
        pg.set_content(card(kind.upper() if kind != 'default' else 'default', title, sub)); pg.wait_for_timeout(150)
        pg.screenshot(path=f'{OUT}/{name}.jpg', type='jpeg', quality=88); print('og', name)
    b.close()
