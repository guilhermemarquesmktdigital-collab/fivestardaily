import json,os,sys
here=os.path.dirname(os.path.abspath(__file__)); out=sys.argv[1]; O='https://fivestardaily.com'
T=open(here+'/template.html').read()
P={
'en':dict(path='chat/',title='Chat with GTA 6 Characters: Talk to Lucia, Jason and Mandy | Five Star Daily',
  desc='Talk to GTA 6 characters Lucia, Jason and Mandy in a phone-style text chat. Free fan-made parody in English, Spanish and Portuguese. Unofficial.',
  og='Chat with GTA 6 Characters: Lucia, Jason and Mandy',h1='Chat with GTA 6 characters',
  intro='Pick a contact and tap your replies to text Lucia, Jason or Mandy from GTA 6. Each one answers in their own style, from Lucia’s blunt advice to Jason’s dry jokes and Mandy’s teasing. It is a free fan-made parody for GTA 6 fans, written by Five Star Daily. It is not official and not written by Rockstar Games.',
  back='← Five Star Daily',note='Fan-made parody for fun. Not official, not affiliated with Rockstar Games, and not their real messages. Characters belong to Rockstar Games.',name='Chat with GTA 6 Characters'),
'es':dict(path='chat/es/',title='Habla con los personajes de GTA 6: Lucia, Jason y Mandy | Five Star Daily',
  desc='Habla con los personajes de GTA 6: escríbele a Lucia, Jason y Mandy en un chat con estilo de teléfono. Parodia gratuita hecha por fans. No oficial.',
  og='Habla con los personajes de GTA 6: Lucia, Jason y Mandy',h1='Chatea con personajes de GTA 6',
  intro='Elige un contacto y toca tus respuestas para hablar con Lucia, Jason o Mandy de GTA 6. Cada uno responde a su estilo: los consejos directos de Lucia, las bromas secas de Jason y las indirectas de Mandy. Es una parodia gratuita hecha por fans para fans de GTA 6, escrita por Five Star Daily. No es oficial ni la escribió Rockstar Games.',
  back='← Five Star Daily',note='Parodia hecha por fans, solo por diversión. No es oficial, no está afiliada a Rockstar Games y no son sus mensajes reales. Los personajes pertenecen a Rockstar Games.',name='Chatea con personajes de GTA 6'),
'pt':dict(path='chat/pt/',title='Fale com os personagens de GTA 6: Lucia, Jason e Mandy | Five Star Daily',
  desc='Converse com os personagens de GTA 6: fale com a Lucia, o Jason e a Mandy num chat com cara de celular. Paródia gratuita feita por fãs. Não oficial.',
  og='Fale com os personagens de GTA 6: Lucia, Jason e Mandy',h1='Converse com personagens de GTA 6',
  intro='Escolha um contato e toque nas suas respostas para falar com a Lucia, o Jason ou a Mandy de GTA 6. Cada um responde no seu estilo: os conselhos diretos da Lucia, as piadas secas do Jason e as provocações da Mandy. É uma paródia gratuita feita por fãs para fãs de GTA 6, escrita pelo Five Star Daily. Não é oficial e não foi escrita pela Rockstar Games.',
  back='← Five Star Daily',note='Paródia feita por fãs, só por diversão. Não é oficial, não tem ligação com a Rockstar Games e não são as mensagens reais deles. Os personagens pertencem à Rockstar Games.',name='Converse com personagens de GTA 6')}
hl=''.join(f'<link rel="alternate" hreflang="{l}" href="{O}/{p["path"]}">' for l,p in P.items())+f'<link rel="alternate" hreflang="x-default" href="{O}/chat/">'
for l,p in P.items():
    url=f'{O}/{p["path"]}'
    ld=json.dumps({"@context":"https://schema.org","@graph":[{"@type":"WebApplication","name":p['name'],"url":url,"applicationCategory":"EntertainmentApplication","operatingSystem":"Any","isAccessibleForFree":True,"inLanguage":l,"description":p['desc'],"publisher":{"@type":"Organization","name":"Five Star Daily","url":O+"/"}},{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Five Star Daily","item":O+"/"},{"@type":"ListItem","position":2,"name":p['name'],"item":url}]}]},ensure_ascii=False)
    head=f'<title>{p["title"]}</title>\n<meta name="description" content="{p["desc"]}">\n<link rel="canonical" href="{url}">\n{hl}\n<meta name="robots" content="index,follow,max-image-preview:large">\n<meta property="og:type" content="website"><meta property="og:site_name" content="Five Star Daily"><meta property="og:title" content="{p["og"]}"><meta property="og:description" content="{p["desc"]}"><meta property="og:url" content="{url}"><meta property="og:image" content="{O}/img/og/default.jpg"><meta name="twitter:card" content="summary_large_image">\n<script type="application/ld+json">{ld}</script>'
    langs=''.join(f'<a href="/{q["path"]}" hreflang="{k}"{" class=\"on\"" if k==l else ""}>{k.upper()}</a>' for k,q in P.items())
    h=T.replace('{{LANG}}',l).replace('{{HEAD}}',head).replace('{{BACK}}',p['back'].replace('←','&larr;')).replace('{{LANGS}}',langs).replace('{{NOTE}}',p['note']).replace('{{H1}}',p['h1']).replace('{{INTRO}}',p['intro'])
    d=os.path.join(out,p['path']); os.makedirs(d,exist_ok=True); open(d+'index.html','w').write(h)
