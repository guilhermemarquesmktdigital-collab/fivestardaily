/* ---------- inner pages (one file, routed on the #hash) ---------- */
var P={
 en:{offline:"The player plays right here once the site is online. In this preview file YouTube only plays on its own site.",live_note:"Real streams from YouTube and Twitch, updated {t}. This refreshes every hour.",twitch_soon:"No Twitch streams in this language right now.",watching:function(n){return n.toLocaleString('en-US')+' watching'},open_tw:"Open on Twitch",none_live:"Nobody is live in this language right now.",past:"Recent streams",vid_note:"Real videos from YouTube, updated {t}. Official Rockstar and PlayStation videos are marked. New ones arrive every hour.",offfirst:"Official first",news_note:"Real headlines from Google News in your language, updated {t}. Each one opens at the source.",lk_t:"Locked",lk_p:"Unlocks on launch day, November 19.",lk_k:"Click or press Esc to continue",lk_badge:"Unlocks Nov 19",menu:"Menu",note:"Sample content. In version 1 this fills itself from YouTube, Twitch and news sources every hour.",
  all:"All",any:"Any language",newest:"Newest",popular:"Most viewed",
  live_t:"Live now",live_p:"Who is streaming GTA VI right now, plus the latest streams you can rewatch.",
  stream:"Stream title",channel:"Channel name",viewers:"viewers",watch:"Watch",
  vid_t:"New videos",vid_p:"Fresh gameplay, tips and trailers from creators. New videos land here automatically.",
  vc:{official:"Official",gameplay:"Gameplay",tips:"Tips & guides",trailers:"Trailers",news:"News"},
  vtitle:"Video title from the creator",ago:function(h){return h<24?h+" h ago":Math.round(h/24)+" d ago"},
  featured:"Featured",open:"Open on YouTube",close:"Close",player:"The YouTube player opens here.",
  news_t:"Today’s news",news_p:"Headlines from across the web. We link to the source, we never copy the article.",
  nc:{official:"Official",release:"Release",gameplay:"Gameplay",industry:"Industry"},
  headline:"Headline from the news source",source:"Source name",read:"Read at the source",
  cd_t:"Launch countdown",cd_p:"November 19 on PS5 and Xbox Series X|S.",
  gd_t:"Guides",gd_p:"Step-by-step help for what everyone searches for. Written by us, updated after every patch.",
  planned:"Planned",
  gs:[["Getting started",["Beginner tips","Controls and settings","How saving works"]],
      ["Money",["How to make money fast","Best businesses to buy","Heist payouts explained"]],
      ["Vehicles",["Best cars","Where to find rare vehicles","Planes, boats and helicopters"]],
      ["Missions",["Story mission list","Side missions","Gold medal tips"]],
      ["Collectibles & secrets",["All collectible locations","Hidden items map","Easter eggs and secrets"]]],
  ck_t:"100% checklist",ck_p:"Tick off everything as you play. Your progress stays on this device, no account needed.",
  ck_note:"Sample list. The real list goes live after launch.",done:"complete",reset:"Reset progress",
  cc:[["Story missions","Mission",12],["Side activities","Activity",8],["Collectibles","Collectible",15],["Stunt jumps","Jump",8],["Vehicles","Vehicle",10]],
  map_t:"Interactive map",map_p:"The six regions of Leonida Rockstar has confirmed. Drag to move, scroll or use + and − to zoom.",
  map_note:"Temporary map drawn by us, regions in approximate places. We swap in the real map on launch day.",credit:"Want every spot found so far? The community map by State of Leonida has it.",openmap:"Open the community map",
  mc:{collect:"Collectibles",store:"Stores",secret:"Secrets",mission:"Missions"},point:"Sample point"},
 es:{offline:"El reproductor funciona aquí cuando el sitio esté en línea. En este archivo de vista previa YouTube solo reproduce en su propio sitio.",live_note:"Transmisiones reales de YouTube y Twitch, actualizadas el {t}. Se renueva cada hora.",twitch_soon:"No hay transmisiones de Twitch en este idioma ahora.",watching:function(n){return n.toLocaleString('es')+' viendo'},open_tw:"Abrir en Twitch",none_live:"Nadie está en vivo en este idioma ahora.",past:"Transmisiones recientes",vid_note:"Videos reales de YouTube, actualizados el {t}. Los videos oficiales de Rockstar y PlayStation están marcados. Llegan nuevos cada hora.",offfirst:"Oficiales primero",news_note:"Titulares reales de Google Noticias en tu idioma, actualizados el {t}. Cada uno abre en la fuente.",lk_t:"Bloqueado",lk_p:"Se desbloquea el día del lanzamiento, 19 de noviembre.",lk_k:"Haz clic o pulsa Esc para continuar",lk_badge:"Se abre el 19/11",menu:"Menú",note:"Contenido de muestra. En la versión 1 se llena solo desde YouTube, Twitch y medios de noticias cada hora.",
  all:"Todo",any:"Cualquier idioma",newest:"Más nuevos",popular:"Más vistos",
  live_t:"En vivo",live_p:"Quién está transmitiendo GTA VI ahora mismo, más las últimas transmisiones para volver a ver.",
  stream:"Título de la transmisión",channel:"Nombre del canal",viewers:"espectadores",watch:"Ver",
  vid_t:"Videos nuevos",vid_p:"Gameplay, trucos y tráilers recién salidos de los creadores. Los videos nuevos llegan solos.",
  vc:{official:"Oficial",gameplay:"Gameplay",tips:"Trucos y guías",trailers:"Tráilers",news:"Noticias"},
  vtitle:"Título del video del creador",ago:function(h){return h<24?"hace "+h+" h":"hace "+Math.round(h/24)+" d"},
  featured:"Destacado",open:"Abrir en YouTube",close:"Cerrar",player:"Aquí se abre el reproductor de YouTube.",
  news_t:"Noticias de hoy",news_p:"Titulares de toda la web. Enlazamos a la fuente, nunca copiamos el artículo.",
  nc:{official:"Oficial",release:"Lanzamiento",gameplay:"Gameplay",industry:"Industria"},
  headline:"Titular del medio de noticias",source:"Nombre del medio",read:"Leer en la fuente",
  cd_t:"Cuenta regresiva",cd_p:"19 de noviembre en PS5 y Xbox Series X|S.",
  gd_t:"Guías",gd_p:"Ayuda paso a paso para lo que todos buscan. Escritas por nosotros, actualizadas tras cada parche.",
  planned:"Planeada",
  gs:[["Primeros pasos",["Consejos para principiantes","Controles y ajustes","Cómo funciona el guardado"]],
      ["Dinero",["Cómo ganar dinero rápido","Los mejores negocios para comprar","Pagos de los golpes explicados"]],
      ["Vehículos",["Los mejores autos","Dónde encontrar vehículos raros","Aviones, barcos y helicópteros"]],
      ["Misiones",["Lista de misiones de la historia","Misiones secundarias","Consejos para la medalla de oro"]],
      ["Coleccionables y secretos",["Todos los coleccionables","Mapa de objetos ocultos","Easter eggs y secretos"]]],
  ck_t:"Checklist 100%",ck_p:"Marca todo mientras juegas. Tu progreso queda en este dispositivo, sin cuenta.",
  ck_note:"Lista de muestra. La lista real sale después del lanzamiento.",done:"completado",reset:"Reiniciar progreso",
  cc:[["Misiones de la historia","Misión",12],["Actividades secundarias","Actividad",8],["Coleccionables","Coleccionable",15],["Saltos acrobáticos","Salto",8],["Vehículos","Vehículo",10]],
  map_t:"Mapa interactivo",map_p:"Las seis regiones de Leonida que Rockstar confirmó. Arrastra para moverte, usa la rueda o + y − para el zoom.",
  map_note:"Mapa temporal dibujado por nosotros, con las regiones en lugares aproximados. Lo cambiamos por el mapa real el día del lanzamiento.",credit:"¿Quieres cada lugar encontrado hasta ahora? El mapa de la comunidad State of Leonida los tiene.",openmap:"Abrir el mapa de la comunidad",
  mc:{collect:"Coleccionables",store:"Tiendas",secret:"Secretos",mission:"Misiones"},point:"Punto de muestra"},
 pt:{offline:"O player toca aqui mesmo quando o site estiver no ar. Neste arquivo de prévia o YouTube só toca no próprio site.",live_note:"Lives reais do YouTube e da Twitch, atualizadas em {t}. Isto se renova de hora em hora.",twitch_soon:"Nenhuma live da Twitch neste idioma agora.",watching:function(n){return n.toLocaleString('pt-BR')+' assistindo'},open_tw:"Abrir na Twitch",none_live:"Ninguém está ao vivo neste idioma agora.",past:"Lives recentes",vid_note:"Vídeos reais do YouTube, atualizados em {t}. Os vídeos oficiais da Rockstar e da PlayStation estão marcados. Novos entram de hora em hora.",offfirst:"Oficiais primeiro",news_note:"Manchetes reais do Google Notícias no seu idioma, atualizadas em {t}. Cada uma abre na fonte.",lk_t:"Bloqueado",lk_p:"Libera no dia do lançamento, 19 de novembro.",lk_k:"Clique ou aperte Esc para continuar",lk_badge:"Libera 19/11",menu:"Menu",note:"Conteúdo de exemplo. Na versão 1 isto se preenche sozinho com YouTube, Twitch e sites de notícia, de hora em hora.",
  all:"Tudo",any:"Qualquer idioma",newest:"Mais novos",popular:"Mais vistos",
  live_t:"Ao vivo",live_p:"Quem está transmitindo GTA VI agora, mais as últimas lives para rever.",
  stream:"Título da live",channel:"Nome do canal",viewers:"espectadores",watch:"Assistir",
  vid_t:"Vídeos novos",vid_p:"Gameplay, dicas e trailers saindo do forno dos criadores. Os vídeos novos chegam sozinhos.",
  vc:{official:"Oficial",gameplay:"Gameplay",tips:"Dicas e guias",trailers:"Trailers",news:"Notícias"},
  vtitle:"Título do vídeo do criador",ago:function(h){return h<24?"há "+h+" h":"há "+Math.round(h/24)+" d"},
  featured:"Destaque",open:"Abrir no YouTube",close:"Fechar",player:"O player do YouTube abre aqui.",
  news_t:"Notícias de hoje",news_p:"Manchetes da web inteira. A gente linka a fonte, nunca copia a matéria.",
  nc:{official:"Oficial",release:"Lançamento",gameplay:"Gameplay",industry:"Indústria"},
  headline:"Manchete do site de notícias",source:"Nome do site",read:"Ler na fonte",
  cd_t:"Contagem regressiva",cd_p:"19 de novembro no PS5 e Xbox Series X|S.",
  gd_t:"Guias",gd_p:"Passo a passo para o que todo mundo procura. Escritos por nós, atualizados a cada patch.",
  planned:"Planejado",
  gs:[["Primeiros passos",["Dicas para iniciantes","Controles e configurações","Como funciona o save"]],
      ["Dinheiro",["Como ganhar dinheiro rápido","Melhores negócios para comprar","Pagamento dos assaltos explicado"]],
      ["Veículos",["Melhores carros","Onde achar veículos raros","Aviões, barcos e helicópteros"]],
      ["Missões",["Lista de missões da história","Missões secundárias","Dicas para medalha de ouro"]],
      ["Colecionáveis e segredos",["Todos os colecionáveis","Mapa de itens escondidos","Easter eggs e segredos"]]],
  ck_t:"Checklist 100%",ck_p:"Marque tudo enquanto joga. Seu progresso fica salvo neste aparelho, sem precisar de conta.",
  ck_note:"Lista de exemplo. A lista real entra depois do lançamento.",done:"completo",reset:"Zerar progresso",
  cc:[["Missões da história","Missão",12],["Atividades paralelas","Atividade",8],["Colecionáveis","Colecionável",15],["Saltos","Salto",8],["Veículos","Veículo",10]],
  map_t:"Mapa interativo",map_p:"As seis regiões de Leonida confirmadas pela Rockstar. Arraste para mover, use a rolagem ou + e − para o zoom.",
  map_note:"Mapa provisório desenhado por nós, com as regiões em posições aproximadas. Trocamos pelo mapa real no dia do lançamento.",credit:"Quer todos os pontos achados até agora? O mapa da comunidade State of Leonida tem.",openmap:"Abrir o mapa da comunidade",
  mc:{collect:"Colecionáveis",store:"Lojas",secret:"Segredos",mission:"Missões"},point:"Ponto de exemplo"}
};
var PAGES=['live','videos','news','guides','checklist','map'];
var page=$('[data-page]'), modal=$('[data-modal]'), state={};
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function head(key,acc){var p=P[lang];return '<div class="pg-head"><a class="back" href="#">&larr; '+p.menu+'</a><div class="pg-title" style="--acc:'+acc+'"><h1>'+esc(p[key+'_t'])+'</h1><p>'+esc(p[key+'_p'])+'</p></div></div>';}
function note(t){return '<p class="note">'+esc(t||P[lang].note)+'</p>';}
function filt(name,opts,cur){return '<div class="filters" role="group" data-f="'+name+'">'+opts.map(function(o){return '<button data-v="'+o[0]+'" aria-pressed="'+(o[0]===cur)+'">'+esc(o[1])+'</button>'}).join('')+'</div>';}
var LANGS=function(){var p=P[lang];return [['any',p.any],['en','EN'],['es','ES'],['pt','PT']]};
var play='<svg class="play" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>';

/*__REALJS__*/
var R={
 live:function(){var p=P[lang],f=state.live||{pl:'all',lg:'any'};
  var ok=function(s){return f.lg==='any'||s[3]===f.lg};
  var lives=f.pl==='twitch'?[]:LIVES.filter(ok), past=f.pl==='twitch'?[]:PASTS.filter(ok), tws=f.pl==='youtube'?[]:TWITCH.filter(ok);
  var lcard=function(s,i){return '<button class="card" data-watch="'+s[0]+'"><div class="thumb ph" style="'+cover(s[0],i+2)+'"><span class="tag">YouTube</span><span class="lv">LIVE</span>'+play+'</div><div class="meta"><h3>'+esc(s[1])+'</h3><div class="sub"><span>'+esc(s[2])+'</span><span>'+s[3].toUpperCase()+'</span></div></div></button>'};
  var tcard=function(s,i){return '<button class="card" data-twitch="'+esc(s[0])+'"><div class="thumb ph" style="'+still(i+5)+'"><span class="tag tw">Twitch</span><span class="lv">LIVE</span>'+play+'</div><div class="meta"><h3>'+esc(s[1])+'</h3><div class="sub"><span>'+esc(s[2])+'</span><span>'+s[3].toUpperCase()+'</span><span>'+p.watching(s[4])+'</span></div></div></button>'};
  var pcard=function(s,i){return '<button class="card" data-watch="'+s[0]+'"><div class="thumb ph" style="'+cover(s[0],i+7)+'"><span class="tag">YouTube</span>'+play+'<span class="dur">'+s[4]+'</span></div><div class="meta"><h3>'+esc(s[1])+'</h3><div class="sub"><span>'+esc(s[2])+'</span><span>'+p.ago(vAgo(s[5]))+'</span></div></div></button>'};
  var cards=tws.map(tcard).concat(lives.map(lcard));
  return head('live','#FF3B4E')+note(upd(p.live_note))+'<div class="bar">'+filt('pl',[['all',p.all],['youtube','YouTube'],['twitch','Twitch']],f.pl)+'<span class="sep"></span>'+filt('lg',LANGS(),f.lg)+'</div>'+
   (cards.length?'<div class="grid g3">'+cards.join('')+'</div>':'<div class="panel empty">'+esc(f.pl==='twitch'&&!TWITCH.length?p.twitch_soon:p.none_live)+'</div>')+
   (past.length?'<section class="gsec" style="margin-top:22px"><h2>'+esc(p.past)+'</h2><div class="grid g3">'+past.map(pcard).join('')+'</div></section>':'');},
 videos:function(){var p=P[lang],f=state.videos||{c:'all',lg:'any',s:'new'};
  var items=VIDS.filter(function(v){return (f.c==='all'||v[3]===f.c)&&(f.lg==='any'||v[4]===f.lg)});
  items=items.slice().sort(f.s==='off'?function(a,b){return b[7]-a[7]||a[6]-b[6]}:function(a,b){return a[6]-b[6]});
  var cats=[['all',p.all]].concat(Object.keys(p.vc).map(function(k){return [k,p.vc[k]]}));
  var sub=function(v){return '<div class="sub"><span>'+esc(v[2])+'</span><span>'+v[4].toUpperCase()+'</span><span>'+p.ago(vAgo(v[6]))+'</span></div>'};
  var card=function(v,i){return '<button class="card" data-watch="'+v[0]+'">'+thumbFor(v,i)+'<span class="tag">'+p.vc[v[3]]+'</span>'+play+(v[5]?'<span class="dur">'+v[5]+'</span>':'')+'</div><div class="meta"><h3>'+esc(v[1])+'</h3>'+sub(v)+'</div></button>'};
  var feat=VIDS[0], showFeat=f.c==='all'&&f.lg==='any';
  return head('vid','#FF8A3D')+note(upd(p.vid_note))+'<div class="bar">'+filt('c',cats,f.c)+'<span class="sep"></span>'+filt('lg',LANGS(),f.lg)+'<span class="grow"></span>'+filt('s',[['new',p.newest],['off',p.offfirst]],f.s)+'</div>'+
   (showFeat?'<button class="card feature" data-watch="'+feat[0]+'">'+thumbFor(feat,0)+play+'<span class="dur">'+feat[5]+'</span></div><div class="meta"><span class="badge2" style="align-self:flex-start">'+p.featured+'</span><h3>'+esc(feat[1])+'</h3>'+sub(feat)+'<span class="btn">'+play.replace('class="play"','width="16" height="16" fill="currentColor"')+p.watch+'</span></div></button>':'')+
   (items.length?'<div class="grid g3">'+items.filter(function(v){return !showFeat||v!==feat}).map(card).join('')+'</div>':'<div class="panel empty">—</div>');},
 news:function(){var p=P[lang],f=state.news||{c:'all'};
  var cats=[['all',p.all]].concat(Object.keys(p.nc).map(function(k){return [k,p.nc[k]]}));
  var items=(RD.NEWS[lang]||RD.NEWS.en).slice().sort(function(a,b){return new Date(b[2])-new Date(a[2])}).filter(function(n){return f.c==='all'||n[4]===f.c});
  return head('news','#2EE6D6')+ourNews()+'<h2 class="sub2">'+esc(p.news_t)+'</h2>'+note(upd(p.news_note))+'<div class="bar">'+filt('c',cats,f.c)+'</div><div class="two"><div class="panel news-list">'+
   (items.length?items.map(function(n){return '<a class="news-item" href="'+esc(n[3])+'" target="_blank" rel="noopener" data-ext><span class="when">'+p.ago(hoursSince(new Date(n[2]).getTime()))+'</span><div><h3>'+esc(n[0])+'</h3><div class="src">'+esc(n[1])+' &middot; '+p.read+' &#8599;</div></div><span class="tagc">'+p.nc[n[4]]+'</span></a>'}).join(''):'<div class="empty">—</div>')+
   '</div><aside class="panel side"><h3>'+p.cd_t+'</h3><p>'+p.cd_p+'</p><div class="cd" style="margin-top:12px" data-cd2></div></aside></div>';},
 guides:function(){return guidesIndex();},
 checklist:function(){var p=P[lang],saved={};try{saved=JSON.parse(store.get('ck')||'{}')}catch(e){}
  var tot=0,dn=0,cats=p.cc.map(function(c,ci){var items='',d=0;for(var i=1;i<=c[2];i++){var id=ci+'-'+i,on=!!saved[id];if(on)d++;items+='<label class="ck-item"><input type="checkbox" data-ck="'+id+'"'+(on?' checked':'')+'><span>'+esc(c[1])+' '+i+'</span></label>';}
   tot+=c[2];dn+=d;return '<section class="panel ck-cat"><header><h3>'+esc(c[0])+'</h3><span>'+d+' / '+c[2]+'</span></header><div class="prog"><i style="width:'+(d/c[2]*100).toFixed(1)+'%"></i></div>'+items+'</section>'}).join('');
  var pc=Math.round(dn/tot*100);
  return head('ck','#B6F25A')+note(p.ck_note)+'<div class="panel ck-top"><div class="big">'+pc+'%</div><div class="lbl">'+dn+' / '+tot+' '+p.done+'</div><div class="grow prog" style="margin:0;height:10px"><i style="width:'+pc+'%"></i></div><button class="btn ghost" data-ck-reset>'+p.reset+'</button></div><div class="ck-cats">'+cats+'</div>';},
 map:function(){var p=P[lang],f=state.map||{collect:1,store:1,secret:1,mission:1},u='https://map.stateofleonida.net/';
  var COL={collect:'#B6F25A',store:'#2EE6D6',secret:'#FF3D8B',mission:'#FFC94A'};
  var pins=MAPPINS.filter(function(m){return f[m[0]]}).map(function(m){return '<g class="pin" tabindex="0" data-pin="'+m[0]+'" transform="translate('+m[1]+' '+m[2]+')"><circle r="8" fill="'+COL[m[0]]+'"/></g>'}).join('');
  var land='M400 47 Q412 30 433 28 Q454 26 472 36 Q490 47 508 54 Q526 61 544 68 Q562 76 577 90 Q592 105 601 122 Q610 140 619 163 Q628 186 634 209 Q640 233 646 253 Q652 273 667 287 Q682 302 697 319 Q712 337 715 360 Q718 383 709 406 Q700 430 685 441 Q670 453 658 467 Q646 482 628 490 Q610 499 592 511 Q574 523 562 540 Q550 557 538 574 Q526 592 532 609 Q538 627 526 638 Q514 650 496 653 Q478 656 463 647 Q448 639 439 624 Q430 610 436 592 Q442 575 433 560 Q424 546 409 534 Q394 523 376 511 Q358 499 346 482 Q334 465 328 447 Q322 430 328 412 Q334 395 325 377 Q316 360 307 342 Q298 325 304 308 Q310 291 304 273 Q298 256 310 238 Q322 221 334 203 Q346 186 352 168 Q358 151 364 128 Q370 105 379 84 Q388 64 400 47 Z';
  var regions=[["Mount Kalaga", 472, 126, "#B6F25A"], ["Ambrosia", 564, 221, "#FFC94A"], ["Port Gellhorn", 376, 302, "#FF8A3D"], ["Grassrivers", 480, 511, "#2EE6D6"], ["Vice City", 640, 383, "#FF3D8B"], ["Leonida Keys", 502, 639, "#4DA8FF"]];
  var reg=regions.map(function(r){return '<g class="region"><circle cx="'+r[1]+'" cy="'+r[2]+'" r="52" fill="'+r[3]+'" opacity=".10"/><text x="'+r[1]+'" y="'+(r[2]-54)+'" text-anchor="middle">'+r[0]+'</text></g>'}).join('');
  var keys=[[358, 610, 38, 21, -10], [272, 276, 16, 12, 0], [312, 424, 12, 9, 0], [672, 383, 13, 32, 10], [497, 669, 14, 6, 10], [533, 676, 13, 5, 6], [569, 673, 12, 5, -4], [600, 664, 11, 5, -12]].map(function(k){return '<ellipse cx="'+k[0]+'" cy="'+k[1]+'" rx="'+k[2]+'" ry="'+k[3]+'" transform="rotate('+k[4]+' '+k[0]+' '+k[1]+')"/>'}).join('');
  return head('map','#4DA8FF')+note(p.map_note)+'<div class="panel mapwrap" data-mapwrap><div class="legend">'+Object.keys(p.mc).map(function(k){return '<label><input type="checkbox" data-layer="'+k+'"'+(f[k]?' checked':'')+'><span class="dot" style="background:'+COL[k]+'"></span>'+p.mc[k]+'</label>'}).join('')+'</div>'+
   '<div class="maptools"><button data-zoom="1" aria-label="Zoom in">+</button><button data-zoom="-1" aria-label="Zoom out">&minus;</button></div>'+
   '<svg class="map" viewBox="190 0 620 700" aria-label="'+esc(p.map_t)+'"><defs><pattern id="grd" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="rgba(255,255,255,.05)"/></pattern>'+
   '<filter id="coast" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="3" seed="7"/><feDisplacementMap in="SourceGraphic" scale="16"/></filter><linearGradient id="lnd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2D5E3E"/><stop offset="1" stop-color="#1F4C3C"/></linearGradient></defs>'+
   '<rect x="-2000" y="-2000" width="5000" height="5000" fill="#0D2340"/><rect x="-2000" y="-2000" width="5000" height="5000" fill="url(#grd)"/><g data-mapg>'+
   '<g filter="url(#coast)"><path d="'+land+'" fill="none" stroke="rgba(77,168,255,.22)" stroke-width="16" stroke-linejoin="round"/>'+
   '<path d="'+land+'" fill="url(#lnd)" stroke="#4DA8FF" stroke-width="2" stroke-linejoin="round"/>'+
   '<g fill="url(#lnd)" stroke="#4DA8FF" stroke-width="1.5">'+keys+'</g></g>'+
   '<g fill="rgba(255,255,255,.13)" stroke="rgba(255,255,255,.18)"><rect x="581" y="280" width="46" height="90" rx="4"/><rect x="598" y="427" width="36" height="40" rx="4"/><rect x="358" y="275" width="24" height="20" rx="4"/></g>'+
   '<g fill="none" stroke="rgba(255,255,255,.28)" stroke-width="3" stroke-linecap="round" stroke-dasharray="1 0"><path d="M472 126 Q534 181 564 221 T640 383 T480 511"/><path d="M376 302 Q436 242 564 221 T472 126"/><path d="M376 302 Q420 431 480 511 T502 639"/></g>'+pins+reg+'</g></svg></div>'+
   '<div class="mapcredit"><span>'+esc(p.credit)+'</span><a class="btn ghost" href="'+u+'" target="_blank" rel="noopener">'+esc(p.openmap)+' &#8599;</a></div>';}
};
var MAPPINS=[["collect", 370, 140], ["collect", 358, 453], ["collect", 538, 453], ["collect", 370, 615], ["collect", 550, 673], ["store", 676, 424], ["store", 514, 302], ["secret", 418, 47], ["secret", 622, 244], ["secret", 328, 360], ["secret", 272, 276], ["secret", 672, 383], ["mission", 490, 198], ["mission", 610, 465], ["mission", 430, 360], ["mission", 586, 302], ["mission", 442, 499], ["mission", 526, 557]];

/* ---------- routing: real paths on the live site (/guides/pre-load/), #hash in a local preview file ---------- */
var BASE=(document.querySelector('meta[name="fsd-base"]')||{}).content||'/';
var PATHMODE=/^https?:$/.test(location.protocol)&&!!document.querySelector('meta[name="fsd-base"]');
function pathFor(h){if(!PATHMODE)return h?'#'+h:'#';if(!h)return BASE;if(/^g-/.test(h))return BASE+'guides/'+h.slice(2)+'/';if(/^n-/.test(h))return BASE+'news/'+h.slice(2)+'/';return BASE+h+'/';}
function routeFromLocation(){
  if(PATHMODE){var p=decodeURIComponent(location.pathname);if(p.indexOf(BASE)===0)p=p.slice(BASE.length);p=p.replace(/^\/+|\/+$/g,'').replace(/index\.html$/,'');
    var m=p.match(/^(guides|news)\/([\w-]+)$/);if(m)return (m[1]==='guides'?'g-':'n-')+m[2];return p;}
  try{return (location.hash||'').slice(1)}catch(e){return ''}}
var route=routeFromLocation();
function go(h){route=h||'';try{if(PATHMODE)history.pushState(null,'',pathFor(route));else history.replaceState(null,'',route?'#'+route:location.pathname+location.search)}catch(e){}render();try{scrollTo(0,0)}catch(e){}}
/* every in-site link gets a real href (for search engines) and is handled here (no page reload) */
function linkify(root){$$('a[href^="#"]',root||document).forEach(function(a){var h=a.getAttribute('href').slice(1);if(a.hasAttribute('data-noop')||a.hasAttribute('data-mopen'))return;a.setAttribute('data-r',h);a.setAttribute('href',pathFor(h));});}
document.addEventListener('click',function(e){var a=e.target.closest('a[data-r],a[href^="#"]');if(!a||e.metaKey||e.ctrlKey||e.shiftKey)return;if(a.hasAttribute('data-noop')||a.hasAttribute('data-mopen')){e.preventDefault();return;}var h=a.hasAttribute('data-r')?a.getAttribute('data-r'):a.getAttribute('href').slice(1);e.preventDefault();if(LOCKED[h]){showLock();return;}go(validRoute(h)?h:'');},true);
var TITLES={live:'live_t',videos:'vid_t',news:'news_t',guides:'gd_t',checklist:'ck_t',map:'map_t'};
function setTitle(h){var t='';try{if(!h)t='';else if(TITLES[h])t=P[lang][TITLES[h]];else if(/^g-/.test(h))t=gBy(h.slice(2)).title[lang];else if(/^n-/.test(h))t=nBy(h.slice(2)).title[lang];else if(C.PAGES[h])t=C.PAGES[h].title[lang];}catch(e){}
  document.title=t?t+' | Five Star Daily':'Five Star Daily: GTA 6 news, videos, live streams and guides';}
function render(){
  var h=route; if(LOCKED[h]){h='';route='';}
  if(!validRoute(h)){document.body.classList.remove('inner');page.innerHTML='';setTitle('');return;}
  document.body.classList.add('inner'); page.innerHTML=R[h]?R[h]():/^g-/.test(h)?guidePage(gBy(h.slice(2))):/^n-/.test(h)?newsPage(nBy(h.slice(2))):sitePage(h); page.setAttribute('data-cur',h);
  if(h==='news') cd2(); if(h==='map') mapInit();
  linkify(page); setTitle(h);
}
function cd2(){var b=$('[data-cd2]');if(!b)return;var left=launch-Date.now();if(left<=0){b.innerHTML='<div><b>'+T[lang].out+'</b></div>';return;}
  b.innerHTML='<div><b>'+Math.floor(left/864e5)+'</b><span>'+T[lang].days+'</span></div><div><b>'+pad(Math.floor(left/36e5)%24)+'</b><span>'+T[lang].hours+'</span></div><div><b>'+pad(Math.floor(left/6e4)%60)+'</b><span>'+T[lang].mins+'</span></div>';}
setInterval(cd2,15000);
var mz={s:1,x:0,y:0};
function mapInit(){var w=$('[data-mapwrap]'),g=$('[data-mapg]'),svg=$('svg.map',w),drag=null,pop=document.createElement('div');pop.className='pop';pop.hidden=true;w.appendChild(pop);
  function ap(){g.setAttribute('transform','translate('+mz.x+' '+mz.y+') scale('+mz.s+')');}
  function zoom(d,cx,cy){var ns=Math.min(4,Math.max(1,mz.s*(d>0?1.25:0.8)));cx=cx==null?500:cx;cy=cy==null?350:cy;mz.x=cx-(cx-mz.x)*ns/mz.s;mz.y=cy-(cy-mz.y)*ns/mz.s;mz.s=ns;if(ns===1){mz.x=0;mz.y=0;}ap();pop.hidden=true;}
  function toSvg(e){var r=svg.getBoundingClientRect(),k=Math.max(620/r.width,700/r.height);return [190+(e.clientX-r.left-(r.width-620/k)/2)*k,(e.clientY-r.top-(r.height-700/k)/2)*k];}
  ap();
  $$('[data-zoom]',w).forEach(function(b){b.addEventListener('click',function(){zoom(+b.dataset.zoom)})});
  w.addEventListener('wheel',function(e){e.preventDefault();var q=toSvg(e);zoom(e.deltaY<0?1:-1,q[0],q[1]);},{passive:false});
  svg.addEventListener('pointerdown',function(e){if(e.target.closest('.pin'))return;drag={x:e.clientX,y:e.clientY,ox:mz.x,oy:mz.y};svg.setPointerCapture(e.pointerId);pop.hidden=true;});
  svg.addEventListener('pointermove',function(e){if(!drag)return;var r=svg.getBoundingClientRect(),k=Math.max(620/r.width,700/r.height);mz.x=drag.ox+(e.clientX-drag.x)*k;mz.y=drag.oy+(e.clientY-drag.y)*k;ap();});
  svg.addEventListener('pointerup',function(){drag=null;});
  function show(pin){var r=pin.getBoundingClientRect(),wr=w.getBoundingClientRect();pop.innerHTML='<b>'+esc(P[lang].mc[pin.dataset.pin])+'</b>'+esc(P[lang].point);pop.style.left=(r.left+r.width/2-wr.left)+'px';pop.style.top=(r.top-wr.top)+'px';pop.classList.toggle('below',r.top-wr.top<110);pop.hidden=false;}
  $$('.pin',w).forEach(function(pin){pin.addEventListener('click',function(){show(pin)});pin.addEventListener('keydown',function(e){if(e.key==='Enter')show(pin)});});
}
page.addEventListener('click',function(e){
  var b=e.target.closest('[data-f] button');
  if(b){var cur=page.getAttribute('data-cur'),key=b.parentNode.dataset.f;state[cur]=state[cur]||({live:{pl:'all',lg:'any'},videos:{c:'all',lg:'any',s:'new'},news:{c:'all'}})[cur];state[cur][key]=b.dataset.v;render();return;}
  if(e.target.closest('[data-noop]')){e.preventDefault();toast.textContent=T[lang].soon;toast.classList.add('show');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('show')},2200);return;}
  var tw=e.target.closest('[data-twitch]');
  if(tw){var ch=tw.dataset.twitch,host=location.hostname||'fivestardaily.com';$('.screen',modal).style.background='#000';$('.screen',modal).innerHTML='<iframe src="https://player.twitch.tv/?channel='+encodeURIComponent(ch)+'&parent='+host+'&autoplay=true" title="Twitch" allow="autoplay; fullscreen" allowfullscreen></iframe>';$('[data-mopen]',modal).href='https://www.twitch.tv/'+encodeURIComponent(ch);$('h3',modal).textContent=$('h3',tw).textContent;$('[data-mopen]',modal).textContent=P[lang].open_tw;$('[data-mclose]',modal).textContent=P[lang].close;modal.classList.add('open');$('[data-mclose]',modal).focus();return;}
  var wv=e.target.closest('[data-watch]');
  if(wv){var id=wv.dataset.watch;$('.screen',modal).style.background='#000';var web=/^https?:$/.test(location.protocol);$('.screen',modal).innerHTML=web?'<iframe src="https://www.youtube-nocookie.com/embed/'+encodeURIComponent(id)+'?autoplay=1&rel=0" title="YouTube" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>':'<a class="offline" href="https://www.youtube.com/watch?v='+encodeURIComponent(id)+'" target="_blank" rel="noopener" style="background-image:'+(OFFI[id]?'linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.65)),url('+ytThumb(id)+')':'linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.65)),'+cover(id,3).replace('background-image:',''))+'"><span class="btn">'+play.replace('class="play"','width="16" height="16" fill="currentColor"')+esc(P[lang].open)+'</span><small>'+esc(P[lang].offline)+'</small></a>';$('[data-mopen]',modal).href='https://www.youtube.com/watch?v='+encodeURIComponent(id);$('h3',modal).textContent=$('h3',wv).textContent;$('[data-mopen]',modal).textContent=P[lang].open;$('[data-mclose]',modal).textContent=P[lang].close;modal.classList.add('open');$('[data-mclose]',modal).focus();return;}
  if(e.target.closest('[data-ck-reset]')){store.set('ck','{}');render();}
});
page.addEventListener('change',function(e){
  var c=e.target.closest('[data-ck]');
  if(c){var s={};try{s=JSON.parse(store.get('ck')||'{}')}catch(x){} if(c.checked)s[c.dataset.ck]=1;else delete s[c.dataset.ck];store.set('ck',JSON.stringify(s));var y=scrollY;render();scrollTo(0,y);var n=$('[data-ck="'+c.dataset.ck+'"]');if(n)n.focus();return;}
  var l=e.target.closest('[data-layer]');
  if(l){state.map=state.map||{collect:1,store:1,secret:1,mission:1};state.map[l.dataset.layer]=l.checked?1:0;render();}
});
function closeModal(){modal.classList.remove('open');$('.screen',modal).innerHTML='';}
modal.addEventListener('click',function(e){if(e.target===modal||e.target.closest('[data-mclose]'))closeModal();});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){if(modal.classList.contains('open'))closeModal();else if(document.body.classList.contains('inner'))go('');}});
addEventListener(PATHMODE?'popstate':'hashchange',function(){var h=routeFromLocation();if(LOCKED[h]){showLock();return;}if(h!==route){route=h;render();scrollTo(0,0);}});
$$('[data-lang]').forEach(function(b){b.addEventListener('click',function(){if(document.body.classList.contains('inner')){var y=scrollY;render();scrollTo(0,y);}})});
render();

/* ---------- locked sections: a game-style "locked" screen ---------- */
var lock=document.createElement('div');lock.className='lockscreen';lock.setAttribute('role','dialog');lock.setAttribute('aria-modal','true');document.body.appendChild(lock);
function showLock(){var p=P[lang],left=launch-Date.now(),d=Math.max(0,Math.floor(left/864e5)),h=Math.max(0,Math.floor(left/36e5)%24);
  lock.innerHTML='<i class="lb t"></i><i class="lb b"></i><div class="lk"><svg viewBox="0 0 24 24" width="54" height="54" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="4.5" y="10.5" width="15" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/></svg><h2>'+esc(p.lk_t)+'</h2><p>'+esc(p.lk_p)+'</p><b>'+d+'d '+pad(h)+'h</b><small>'+esc(p.lk_k)+'</small></div>';
  lock.classList.remove('show');void lock.offsetWidth;lock.classList.add('show');}
function hideLock(){lock.classList.remove('show');}
lock.addEventListener('click',hideLock);
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&lock.classList.contains('show'))hideLock();});
function lockBadges(){$$('.t-check,.t-map').forEach(function(t){var b=$('.lockb',t);if(!b){b=document.createElement('span');b.className='lockb';$('.hd',t).appendChild(b);}b.innerHTML='<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.6"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>'+esc(P[lang].lk_badge);t.classList.add('locked');});}
lockBadges();
$$('[data-lang]').forEach(function(b){b.addEventListener('click',lockBadges)});
/* home tiles show the real data too */
function homeTiles(){
  var lt=$('.t-live .streams');if(lt)lt.innerHTML=LIVES.slice(0,3).map(function(s,i){return '<div><div class="thumb ph" style="'+cover(s[0],i+2)+'"><span class="tag">YouTube</span>'+play+'</div><div class="mini">'+esc(s[2])+'</div></div>'}).join('');
  var gt=$('.t-guides .hd');if(gt){var nb=$('.newb',gt);if(!nb){nb=document.createElement('span');nb.className='newb';gt.appendChild(nb);}nb.textContent=UI[lang].fourguides.replace('{n}',C.GUIDES.length);}
  var sm=$('.t-live .sample');if(sm){sm.removeAttribute('data-i18n');sm.textContent='';}
  var vt=$('.t-videos .vids');if(vt)vt.innerHTML=VIDS.filter(function(v){return v[7]}).slice(0,2).map(function(v){return '<div class="thumb ph" style="background-image:url('+ytThumb(v[0])+')">'+play+'</div>'}).join('');
  var nt=$('.t-news .news');if(nt)nt.innerHTML=(RD.NEWS[lang]||RD.NEWS.en).slice().sort(function(a,b){return new Date(b[2])-new Date(a[2])}).slice(0,3).map(function(n){return '<li><span class="hl">'+esc(n[0])+'</span></li>'}).join('');
}
homeTiles();footLinks();linkify(document);$$('[data-lang]').forEach(function(b){b.addEventListener('click',function(){footLinks();linkify(document);})});$$('[data-lang]').forEach(function(b){b.addEventListener('click',homeTiles)});

/* ---------- fresh data: the hourly job writes data/feed.json; the built-in snapshot is the fallback ---------- */
function upd(t){var L={en:'en-US',es:'es',pt:'pt-BR'}[lang]||'en-US';return t.replace('{t}',new Date(SNAP).toLocaleString(L,{month:'short',day:'numeric',hour:'numeric',minute:'2-digit'}));}
var BAKED={};VIDS.concat(LIVES,PASTS).forEach(function(v){BAKED[v[0]]=1});
(function(){
  if(location.protocol.indexOf('http')!==0) return;
  fetch(BASE+'data/feed.json?h='+Math.floor(Date.now()/36e5),{cache:'no-cache'}).then(function(r){return r.ok?r.json():null}).then(function(d){
    if(!d||!d.SNAP||new Date(d.SNAP).getTime()<=SNAP) return;
    var shift=Math.round((new Date(d.SNAP).getTime()-SNAP)/36e5); SNAP=new Date(d.SNAP).getTime();
    if(d.V&&d.V.length){var have={};d.V.forEach(function(v){have[v[0]]=1});VIDS=d.V.concat(VIDS.filter(function(v){return v[7]&&!have[v[0]]}).map(function(v){v=v.slice();v[6]+=shift;return v}));}
    if(d.LIVE) LIVES=d.LIVE; if(d.TW) TWITCH=d.TW; if(d.PAST) PASTS=d.PAST; if(d.NEWS) RD.NEWS=d.NEWS;
    OFFI={};VIDS.forEach(function(v){if(v[7])OFFI[v[0]]=1});
    homeTiles(); if(route) render();
  }).catch(function(){});
})();
