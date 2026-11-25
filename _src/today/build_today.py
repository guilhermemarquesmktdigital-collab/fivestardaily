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

G=C['GUIDES']
eg=sorted(D['e']);e=eg[day%len(eg)];en=D['p'][e][0]
ch=['Lucia','Jason','Mandy','Cal','Boobie Ike','Shirley'][day%6]
UI={
'en':dict(path='today/',months=None,title='GTA 6 today: latest news, tip and easter egg of the day | Five Star Daily',ogt='GTA 6 today: news, tip and easter egg of the day',
 desc='Your daily GTA 6 stop: the latest headlines with our own summaries, a guide to read today and an easter egg to hunt. Updated every day. Unofficial fan site.',
 h1='GTA 6 today',lead='The quick daily stop for Leonida: fresh headlines, one guide to read and one secret to hunt. Updated every day. Unofficial fan site.',
 top='Top stories',allnews='All news',gd='Guide of the day',read='Read it',eg='Easter egg of the day',near='Near',map='Open the map',warn='Reported by fans and outlets. Not confirmed by Rockstar. Spoilers.',
 tc='Text a character',wait='is waiting',chat='Start chatting',cl='/chat/',more='More',snd='soundtrack',ck='100% checklist',mp='map',lv='live streams',disc='Fan site, not affiliated with Rockstar Games or Take-Two.',home='Five Star Daily',
 cdesc={'Cal':'Nervous tech guy, very online','Boobie Ike':'Smooth, rich, never in a hurry','Shirley':'Nosy neighbor with tiny favors','Lucia':'Tough, sharp, no wasted words','Jason':'Easygoing, jokes, a boat that barely floats','Mandy':'Teasing, dramatic, never boring'},fan='Fan-made chat, unofficial.'),
'es':dict(path='today/es/',title='GTA 6 hoy: últimas noticias, consejo y easter egg del día | Five Star Daily',ogt='GTA 6 hoy: noticias, consejo y easter egg del día',
 desc='Tu parada diaria de GTA 6: los últimos titulares con resúmenes propios, una guía para leer hoy y un easter egg para buscar. Se actualiza cada día. Sitio de fans no oficial.',
 h1='GTA 6 hoy',lead='La parada rápida diaria por Leonida: titulares frescos, una guía para leer y un secreto para buscar. Se actualiza cada día. Sitio de fans no oficial.',
 top='Noticias principales',allnews='Todas las noticias',gd='Guía del día',read='Leer',eg='Easter egg del día',near='Cerca de',map='Abrir el mapa',warn='Reportado por fans y medios. Rockstar no lo confirmó. Spoilers.',
 tc='Escríbele a un personaje',wait='te espera',chat='Empezar a chatear',cl='/chat/es/',more='Más',snd='banda sonora',ck='checklist 100%',mp='mapa',lv='transmisiones en vivo',disc='Sitio de fans, sin relación con Rockstar Games ni Take-Two.',home='Five Star Daily',
 cdesc={'Cal':'Informático nervioso, siempre conectado','Boobie Ike':'Elegante, rico, nunca tiene prisa','Shirley':'Vecina curiosa con favorcitos','Lucia':'Dura, aguda, no pierde el tiempo','Jason':'Tranquilo, bromista, con un bote que apenas flota','Mandy':'Burlona, dramática, nunca aburrida'},fan='Chat hecho por fans, no oficial.'),
'pt':dict(path='today/pt/',title='GTA 6 hoje: últimas notícias, dica e easter egg do dia | Five Star Daily',ogt='GTA 6 hoje: notícias, dica e easter egg do dia',
 desc='Sua parada diária de GTA 6: as últimas manchetes com resumos próprios, um guia para ler hoje e um easter egg para caçar. Atualizado todo dia. Site de fãs não oficial.',
 h1='GTA 6 hoje',lead='A parada rápida diária por Leonida: manchetes fresquinhas, um guia para ler e um segredo para caçar. Atualizado todo dia. Site de fãs não oficial.',
 top='Principais notícias',allnews='Todas as notícias',gd='Guia do dia',read='Ler',eg='Easter egg do dia',near='Perto de',map='Abrir o mapa',warn='Relatado por fãs e veículos. A Rockstar não confirmou. Contém spoilers.',
 tc='Mande mensagem para um personagem',wait='está esperando',chat='Começar a conversar',cl='/chat/pt/',more='Mais',snd='trilha sonora',ck='checklist 100%',mp='mapa',lv='transmissões ao vivo',disc='Site de fãs, sem ligação com a Rockstar Games nem com a Take-Two.',home='Five Star Daily',
 cdesc={'Cal':'Cara da tecnologia, nervoso, sempre online','Boobie Ike':'Elegante, rico, nunca tem pressa','Shirley':'Vizinha enxerida com favorzinhos','Lucia':'Dura, afiada, não perde tempo','Jason':'Tranquilo, piadista, com um barco que mal flutua','Mandy':'Provocadora, dramática, nunca chata'},fan='Chat feito por fãs, não oficial.')}
MO={'en':['January','February','March','April','May','June','July','August','September','October','November','December'],
'es':['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'],
'pt':['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']}
def dstr(l):
    m=MO[l][now.month-1]
    return f'{m} {now.day}, {now.year}' if l=='en' else f'{now.day} de {m} de {now.year}'
hl=''.join(f'<link rel="alternate" hreflang="{l}" href="{O}/{u["path"]}">' for l,u in UI.items())+f'<link rel="alternate" hreflang="x-default" href="{O}/today/">'
for l,u in UI.items():
    url=O+'/'+u['path']
    nl=''.join(f'<li><a href="/{"news/" if l=="en" else ""}news/{n["slug"]}/"><b>{html.escape(n["title"][l])}</b></a><span>{n["date"][:10]}</span><p>{html.escape(cut(n["body"][l]))}</p></li>'.replace('/news/news/','/news/') for n in news)
    g=G[day%len(G)]
    ld=json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":u['h1'],"url":url,"description":u['desc'],"inLanguage":l,"isPartOf":{"@type":"WebSite","name":"Five Star Daily","url":O+"/"},"dateModified":now.strftime('%Y-%m-%d')},ensure_ascii=False)
    langs=''.join(f'<a href="/{q["path"]}" hreflang="{k}"{" class=on" if k==l else ""}>{k.upper()}</a>' for k,q in UI.items())
    h=f"""<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{u['title']}</title><meta name="description" content="{u['desc']}"><link rel="canonical" href="{url}">{hl}
<meta property="og:type" content="website"><meta property="og:site_name" content="Five Star Daily"><meta property="og:title" content="{u['ogt']}"><meta property="og:description" content="{u['desc']}"><meta property="og:url" content="{url}"><meta property="og:image" content="{O}/img/og/default.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/rss+xml" title="Five Star Daily" href="/rss.xml"><script type="application/ld+json">{ld}</script>
<style>:root{{--bg:#0b0820;--p:rgba(255,255,255,.07);--l:rgba(255,255,255,.14);--m:#b9b3d6;--a:#FFC93C}}*{{box-sizing:border-box}}body{{margin:0;background:radial-gradient(1000px 500px at 50% -10%,#3a1d6e,var(--bg) 70%);color:#fff;font:16px/1.5 Inter,system-ui,sans-serif;min-height:100vh}}
.w{{max-width:760px;margin:0 auto;padding:18px 16px 60px}}a{{color:inherit}}.top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:22px;gap:10px}}.top>a{{text-decoration:none;font-weight:700;color:var(--m)}}.lg a{{display:inline-block;border:1px solid var(--l);border-radius:8px;padding:5px 9px;font:700 12px/1 inherit;margin-left:4px;text-decoration:none}}.lg a.on{{background:#fff;color:#14102E}}
h1{{font-size:clamp(30px,6vw,46px);line-height:1.05;margin:0 0 6px}}.dt{{color:var(--a);font-weight:700;margin:0 0 6px}}.lead{{color:var(--m);margin:0 0 24px}}
.card{{background:var(--p);border:1px solid var(--l);border-radius:16px;padding:16px 18px;margin:0 0 16px}}h2{{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--a);margin:0 0 10px}}
ul{{list-style:none;margin:0;padding:0}}li{{padding:10px 0;border-top:1px solid var(--l)}}li:first-child{{border-top:0;padding-top:0}}li b{{font-size:17px}}li span{{display:block;color:var(--m);font-size:12.5px;margin-top:2px}}li p{{margin:4px 0 0;color:#ddd8f2;font-size:14.5px}}
.btn{{display:inline-block;margin-top:10px;background:#fff;color:#14102E;border-radius:999px;padding:8px 16px;font-weight:800;text-decoration:none;font-size:14px}}.sm{{color:var(--m);font-size:13.5px}}.g2{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}@media(max-width:640px){{.g2{{grid-template-columns:1fr}}}}</style></head><body><div class="w">
<div class="top"><a href="/">&larr; {u['home']}</a><span class="lg">{langs}<a href="/rss.xml">RSS</a></span></div>
<p class="dt">{dstr(l)}</p><h1>{u['h1']}</h1><p class="lead">{u['lead']}</p>
<section class="card"><h2>{u['top']}</h2><ul>{nl}</ul><a class="btn" href="/news/">{u['allnews']}</a></section>
<div class="g2"><section class="card"><h2>{u['gd']}</h2><b>{html.escape(g["title"][l])}</b><p class="sm">{html.escape(cut(g["lede"][l],150))}</p><a class="btn" href="/guides/{g["slug"]}/">{u['read']}</a></section>
<section class="card"><h2>{u['eg']}</h2><b>{u['near']} {html.escape(en)}</b><p class="sm">{html.escape(cut(D["e"][e][l],150))}</p><a class="btn" href="/map/">{u['map']}</a><p class="sm">{u['warn']}</p></section></div>
<section class="card"><h2>{u['tc']}</h2><b>{ch} {u['wait']}</b><p class="sm">{u['cdesc'][ch]}. {u['fan']}</p><a class="btn" href="{u['cl']}">{u['chat']}</a></section>
<p class="sm">{u['more']}: <a href="/guides/soundtrack/">{u['snd']}</a> · <a href="/checklist/">{u['ck']}</a> · <a href="/map/">{u['mp']}</a> · <a href="/live/">{u['lv']}</a>. {u['disc']}</p></div></body></html>"""
    d=out+'/'+u['path'];os.makedirs(d,exist_ok=True);open(d+'index.html','w').write(h)
