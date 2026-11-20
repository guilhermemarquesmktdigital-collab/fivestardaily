/* ---------- original content: guides, news summaries and site pages ---------- */
var C=__CONTENT__;
var UI={
 en:{out:"Out now",soon:"Coming on launch day",read:"min read",sources:"Sources",byus:"Written by Five Star Daily",ours:"Our coverage",oursum:"Our summary",readfull:"Read the full story at",related:"Related guide",watchall:"Watch the trailers",updated:"Updated",fourguides:"{n} guides out now",gstart:"Start here",ggame:"How GTA 6 plays",about:"About",contact:"Contact",privacy:"Privacy",terms:"Terms"},
 es:{out:"Ya disponibles",soon:"Llegan el día del lanzamiento",read:"min de lectura",sources:"Fuentes",byus:"Escrito por Five Star Daily",ours:"Nuestra cobertura",oursum:"Nuestro resumen",readfull:"Lee la nota completa en",related:"Guía relacionada",watchall:"Mira los tráilers",updated:"Actualizado",fourguides:"{n} guías ya disponibles",gstart:"Empieza aquí",ggame:"Cómo se juega GTA 6",about:"Sobre nosotros",contact:"Contacto",privacy:"Privacidad",terms:"Términos"},
 pt:{out:"Já disponíveis",soon:"Chegam no dia do lançamento",read:"min de leitura",sources:"Fontes",byus:"Escrito pelo Five Star Daily",ours:"Nossa cobertura",oursum:"Nosso resumo",readfull:"Leia a matéria completa em",related:"Guia relacionado",watchall:"Assista aos trailers",updated:"Atualizado",fourguides:"{n} guias já disponíveis",gstart:"Comece por aqui",ggame:"Como GTA 6 se joga",about:"Sobre",contact:"Contato",privacy:"Privacidade",terms:"Termos"}};
var SITEPAGES=['about','contact','privacy','terms'];
function validRoute(h){return PAGES.indexOf(h)>=0||SITEPAGES.indexOf(h)>=0||/^g-/.test(h)&&gBy(h.slice(2))||/^n-/.test(h)&&nBy(h.slice(2));}
function gBy(s){return C.GUIDES.filter(function(g){return g.slug===s})[0];}
function nBy(s){return C.NEWS.filter(function(n){return n.slug===s})[0];}
function fmtDate(d){try{return new Date(d).toLocaleDateString(lang==='pt'?'pt-BR':lang,{day:'numeric',month:'long',year:'numeric'})}catch(e){return d.slice(0,10)}}
function srcList(keys){return '<aside class="srcs"><h3>'+UI[lang].sources+'</h3><ul>'+keys.map(function(k){var s=C.S[k];return '<li><a href="'+s[1]+'" target="_blank" rel="noopener">'+esc(s[0])+' &#8599;</a></li>'}).join('')+'</ul></aside>';}
function artShell(back,backLabel,kicker,title,lede,meta,body){
  return '<div class="pg-head"><a class="back" href="#'+back+'">&larr; '+esc(backLabel)+'</a></div><article class="panel art"><p class="kick">'+esc(kicker)+'</p><h1>'+esc(title)+'</h1>'+(lede?'<p class="lede">'+esc(lede)+'</p>':'')+'<p class="meta">'+meta+'</p><div class="prose">'+body+'</div></article>';}
function guidePage(g){var u=UI[lang],p=P[lang];
  var vids=(g.videos||[]).map(function(id){return VIDS.filter(function(v){return v[0]===id})[0]}).filter(Boolean);
  var vg=vids.length?'<h2 class="sub2">'+u.watchall+'</h2><div class="grid g3">'+vids.map(function(v,i){return '<button class="card" data-watch="'+v[0]+'">'+thumbFor(v,i)+play+(v[5]?'<span class="dur">'+v[5]+'</span>':'')+'</div><div class="meta"><h3>'+esc(v[1])+'</h3></div></button>'}).join('')+'</div>':'';
  return artShell('guides',p.gd_t,u.byus,g.title[lang],g.lede[lang],u.updated+' '+fmtDate((g.upd||'2026-11-13')+'T12:00:00')+' &middot; '+g.mins+' '+u.read,g.body[lang]+vg+srcList(g.src));}
function newsPage(n){var u=UI[lang],p=P[lang],first=C.S[n.src[0]];
  var rel=n.guide?'<p class="relg">'+u.related+': <a href="#g-'+n.guide+'">'+esc(gBy(n.guide).title[lang])+' &rarr;</a></p>':'';
  return artShell('news',p.news_t,u.oursum+' · '+p.nc[n.cat],n.title[lang],'',fmtDate(n.date),n.body[lang]+'<p><a class="btn" href="'+first[1]+'" target="_blank" rel="noopener">'+u.readfull+' '+esc(first[0].split(':')[0])+' &#8599;</a></p>'+rel+srcList(n.src));}
function sitePage(k){var x=C.PAGES[k];return artShell('',P[lang].menu,'Five Star Daily',x.title[lang],'','',x.body[lang]);}
function guidesIndex(){var u=UI[lang],p=P[lang];
  var card=function(g){return '<a class="card guide" href="#g-'+g.slug+'"><h3>'+esc(g.title[lang])+'</h3><p class="gl">'+esc(g.lede[lang])+'</p><div class="sub"><span class="badge2 new">'+g.mins+' '+u.read+'</span></div></a>'};
  var out=[['start',u.gstart],['game',u.ggame]].map(function(c){var gs=C.GUIDES.filter(function(g){return g.cat===c[0]});return gs.length?'<section class="gsec"><h2>'+c[1]+'</h2><div class="grid g3">'+gs.map(card).join('')+'</div></section>':''}).join('');
  var soon=p.gs.map(function(s){return '<section class="gsec"><h2>'+esc(s[0])+' <small class="soonh">'+u.soon+'</small></h2><div class="grid g3">'+s[1].map(function(g){return '<a class="card guide lockedc" href="#checklist"><h3>'+esc(g)+'</h3><div class="sub"><span class="badge2">'+esc(p.lk_badge)+'</span></div></a>'}).join('')+'</div></section>'}).join('');
  return head('gd','#B58CFF')+out+soon;}
function ourNews(){var u=UI[lang],p=P[lang];
  return '<section class="gsec"><h2>'+u.ours+'</h2><div class="grid g3">'+C.NEWS.map(function(n,i){return '<a class="card" href="#n-'+n.slug+'"><div class="thumb ph" style="'+still(i+4)+'"><span class="tag">'+u.oursum+'</span></div><div class="meta"><h3>'+esc(n.title[lang])+'</h3><div class="sub"><span>'+p.nc[n.cat]+'</span><span>'+fmtDate(n.date)+'</span></div></div></a>'}).join('')+'</div></section>';}
function footLinks(){var f=$('.foot'),u=UI[lang];if(!f)return;var n=$('.footnav',f);if(!n){n=document.createElement('nav');n.className='footnav';n.setAttribute('aria-label','Site');f.insertBefore(n,f.firstChild);}
  n.innerHTML=SITEPAGES.map(function(k){return '<a href="#'+k+'">'+u[k]+'</a>'}).join('');}
