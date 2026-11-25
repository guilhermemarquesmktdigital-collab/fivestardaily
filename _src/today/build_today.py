import json,os,re,sys,html,datetime
here=os.path.dirname(os.path.abspath(__file__));SC=os.path.dirname(here);out=sys.argv[1];O='https://fivestardaily.com'
C=json.load(open(SC+'/air/content.json'))
pj=open(SC+'/air/pages.js').read()
D=json.loads(re.search(r'var MAPD=(\{.*?\});\n',pj,re.S).group(1))
now=datetime.datetime.now(datetime.timezone.utc);day=now.timetuple().tm_yday
today=now.strftime('%B %-d, %Y')
news=sorted(C['NEWS'],key=lambda n:n['date'],reverse=True)[:6]
def strip(t):return re.sub('<[^>]+>','',t).strip()
def cut(t,n=170):
    t=strip(t);return t if len(t)<=n else t[:n].rsplit(' ',1)[0]+'…'
nl=''.join(f'<li><a href="/news/{n["slug"]}/"><b>{html.escape(n["title"]["en"])}</b></a><span>{n["date"][:10]}</span><p>{html.escape(cut(n["body"]["en"]))}</p></li>' for n in news)
G=C['GUIDES'];g=G[day%len(G)]
eg=sorted(D['e']);e=eg[day%len(eg)];en=D['p'][e][0]
chars=[('Lucia','/chat/','Tough, sharp, no wasted words'),('Jason','/chat/','Easygoing, jokes, a boat that barely floats'),('Mandy','/chat/','Teasing, dramatic, never boring')];ch=chars[day%3]
title='GTA 6 today: latest news, tip and easter egg of the day | Five Star Daily'
desc='Your daily GTA 6 stop: the latest headlines with our own summaries, a guide to read today and an easter egg to hunt. Updated every day. Unofficial fan site.'
url=O+'/today/'
ld=json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":"GTA 6 today","url":url,"description":desc,"inLanguage":"en","isPartOf":{"@type":"WebSite","name":"Five Star Daily","url":O+"/"},"dateModified":now.strftime('%Y-%m-%d')})
h=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Five Star Daily"><meta property="og:title" content="GTA 6 today: news, tip and easter egg of the day"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{O}/img/og/default.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/rss+xml" title="Five Star Daily" href="/rss.xml"><script type="application/ld+json">{ld}</script>
<style>:root{{--bg:#0b0820;--p:rgba(255,255,255,.07);--l:rgba(255,255,255,.14);--m:#b9b3d6;--a:#FFC93C}}*{{box-sizing:border-box}}body{{margin:0;background:radial-gradient(1000px 500px at 50% -10%,#3a1d6e,var(--bg) 70%);color:#fff;font:16px/1.5 Inter,system-ui,sans-serif;min-height:100vh}}
.w{{max-width:760px;margin:0 auto;padding:18px 16px 60px}}a{{color:inherit}}.top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:22px}}.top a{{text-decoration:none;font-weight:700;color:var(--m)}}
h1{{font-size:clamp(30px,6vw,46px);line-height:1.05;margin:0 0 6px}}.dt{{color:var(--a);font-weight:700;margin:0 0 6px}}.lead{{color:var(--m);margin:0 0 24px}}
.card{{background:var(--p);border:1px solid var(--l);border-radius:16px;padding:16px 18px;margin:0 0 16px}}h2{{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--a);margin:0 0 10px}}
ul{{list-style:none;margin:0;padding:0}}li{{padding:10px 0;border-top:1px solid var(--l)}}li:first-child{{border-top:0;padding-top:0}}li b{{font-size:17px}}li span{{display:block;color:var(--m);font-size:12.5px;margin-top:2px}}li p{{margin:4px 0 0;color:#ddd8f2;font-size:14.5px}}
.btn{{display:inline-block;margin-top:10px;background:#fff;color:#14102E;border-radius:999px;padding:8px 16px;font-weight:800;text-decoration:none;font-size:14px}}.sm{{color:var(--m);font-size:13.5px}}.g2{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}@media(max-width:640px){{.g2{{grid-template-columns:1fr}}}}</style></head><body><div class="w">
<div class="top"><a href="/">&larr; Five Star Daily</a><a href="/rss.xml">RSS</a></div>
<p class="dt">{today}</p><h1>GTA 6 today</h1><p class="lead">The quick daily stop for Leonida: fresh headlines, one guide to read and one secret to hunt. Updated every day. Unofficial fan site.</p>
<section class="card"><h2>Top stories</h2><ul>{nl}</ul><a class="btn" href="/news/">All news</a></section>
<div class="g2"><section class="card"><h2>Guide of the day</h2><b>{html.escape(g["title"]["en"])}</b><p class="sm">{html.escape(cut(g["lede"]["en"],150))}</p><a class="btn" href="/guides/{g["slug"]}/">Read it</a></section>
<section class="card"><h2>Easter egg of the day</h2><b>Near {html.escape(en)}</b><p class="sm">{html.escape(cut(D["e"][e]["en"],150))}</p><a class="btn" href="/map/">Open the map</a><p class="sm">Reported by fans and outlets. Not confirmed by Rockstar. Spoilers.</p></section></div>
<section class="card"><h2>Text a character</h2><b>{ch[0]} is waiting</b><p class="sm">{ch[2]}. Fan-made chat, unofficial.</p><a class="btn" href="/chat/">Start chatting</a> <a class="btn" href="/chat/pt/" style="background:transparent;color:#fff;border:1px solid var(--l)">Português</a></section>
<p class="sm">More: <a href="/guides/soundtrack/">soundtrack</a> · <a href="/checklist/">100% checklist</a> · <a href="/map/">map</a> · <a href="/live/">live streams</a>. Fan site, not affiliated with Rockstar Games or Take-Two.</p></div></body></html>'''
os.makedirs(out+'/today',exist_ok=True);open(out+'/today/index.html','w').write(h)
