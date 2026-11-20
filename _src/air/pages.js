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
  ck_note:"Requirements from the in-game 100% menu, as reported by PowerPyx on Nov 19, 2026. Percent here is our simple average, not the game's own number.",done:"complete",reset:"Reset progress",
  cc:[["Story & tasks",[["Finish the main story",1],["Optional tasks",100],["Gang operations",39],["Bank jobs",22],["Payday loans",7],["Smash 'N' Grabs",34],["Stick ups",50],["Vaults hit",8],["Fence $100,000 in narcotics",1],["Fence $100,000 in jewelry",1],["Fence $250,000 in marked bills",1],["Fence $200,000 in vehicles",1]]],["Exploration",[["Kenton sets",5],["Collectible card sets",15],["WAiNK locations scanned",100],["Underwater discoveries",33],["Magazines, books & comics",30],["Meditation spots",15],["Cocaine flamingos destroyed",100],["Unique playlists",2],["Styles discovered",70]]],["Activities",[["Unique races won",30],["Race challenge gold medals",10],["Shooting range gold medals",42],["Video games played",4],["Pool opponents defeated",5],["Mini golf locations played",2],["Basketball hoops",90],["Drone time trials",42],["Stunts",300],["Challenges",70],["Bret's target decks",15]]],["Discovery",[["Base model vehicles scanned",200],["Standard issue weapons",50],["Animals studied",100]]]],
  map_t:"Interactive map",map_p:"Our fan-made map of Leonida. Drag to move, scroll, double-tap or use + and − to zoom.",
  map_note:"Fan-made map based on what has been shown so far. Shapes and county names are unofficial and approximate. Rockstar announced a free official printable map of Leonida for November 19 on rockstargames.com/VI. We swap ours for an official or in-game map as soon as we can check it.",credit:"Want every spot found so far? The community map by State of Leonida has it.",openmap:"Open the community map",
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
  ck_note:"Requisitos del menú de 100% del juego, según PowerPyx (19 nov 2026). El porcentaje es nuestro promedio simple, no el número del juego.",done:"completado",reset:"Reiniciar progreso",
  cc:[["Historia y tareas",[["Terminar la historia principal",1],["Tareas opcionales",100],["Operaciones de pandillas",39],["Atracos a bancos",22],["Préstamos Payday",7],["Smash 'N' Grabs",34],["Atracos a mano armada",50],["Bóvedas asaltadas",8],["Revender $100,000 en narcóticos",1],["Revender $100,000 en joyas",1],["Revender $250,000 en billetes marcados",1],["Revender $200,000 en vehículos",1]]],["Exploración",[["Sets Kenton",5],["Sets de cartas coleccionables",15],["Lugares WAiNK escaneados",100],["Descubrimientos submarinos",33],["Revistas, libros y cómics",30],["Puntos de meditación",15],["Flamencos de cocaína destruidos",100],["Playlists únicas",2],["Estilos descubiertos",70]]],["Actividades",[["Carreras únicas ganadas",30],["Medallas de oro en retos de carrera",10],["Medallas de oro en el campo de tiro",42],["Videojuegos jugados",4],["Rivales de billar vencidos",5],["Campos de minigolf jugados",2],["Canastas de baloncesto",90],["Contrarrelojes con dron",42],["Acrobacias",300],["Desafíos",70],["Mazos de objetivos de Bret",15]]],["Descubrimiento",[["Vehículos base escaneados",200],["Armas estándar",50],["Animales estudiados",100]]]],
  map_t:"Mapa interactivo",map_p:"Nuestro mapa de Leonida hecho por fans. Arrastra para moverte; usa la rueda, doble toque o + y − para el zoom.",
  map_note:"Mapa hecho por fans con base en lo mostrado hasta ahora. Las formas y los nombres de los condados no son oficiales y son aproximados. Rockstar anunció un mapa oficial gratuito de Leonida para imprimir el 19 de noviembre en rockstargames.com/VI. Lo cambiamos por un mapa oficial o del juego en cuanto podamos comprobarlo.",credit:"¿Quieres cada lugar encontrado hasta ahora? El mapa de la comunidad State of Leonida los tiene.",openmap:"Abrir el mapa de la comunidad",
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
  ck_note:"Requisitos do menu de 100% do jogo, segundo o PowerPyx (19 nov 2026). A porcentagem é nossa média simples, não o número do jogo.",done:"completo",reset:"Zerar progresso",
  cc:[["História e tarefas",[["Terminar a história principal",1],["Tarefas opcionais",100],["Operações de gangue",39],["Assaltos a banco",22],["Empréstimos Payday",7],["Smash 'N' Grabs",34],["Roubos à mão armada",50],["Cofres arrombados",8],["Repassar $100,000 em narcóticos",1],["Repassar $100,000 em joias",1],["Repassar $250,000 em notas marcadas",1],["Repassar $200,000 em veículos",1]]],["Exploração",[["Conjuntos Kenton",5],["Conjuntos de cartas colecionáveis",15],["Locais WAiNK escaneados",100],["Descobertas subaquáticas",33],["Revistas, livros e quadrinhos",30],["Pontos de meditação",15],["Flamingos de cocaína destruídos",100],["Playlists únicas",2],["Estilos descobertos",70]]],["Atividades",[["Corridas únicas vencidas",30],["Medalhas de ouro nos desafios de corrida",10],["Medalhas de ouro no estande de tiro",42],["Videogames jogados",4],["Adversários de sinuca vencidos",5],["Campos de minigolfe jogados",2],["Cestas de basquete",90],["Contra-relógios de drone",42],["Manobras",300],["Desafios",70],["Baralhos de alvos do Bret",15]]],["Descoberta",[["Veículos base escaneados",200],["Armas padrão",50],["Animais estudados",100]]]],
  map_t:"Mapa interativo",map_p:"Nosso mapa de Leonida feito por fãs. Arraste para mover; use a rolagem, dois toques ou + e − para o zoom.",
  map_note:"Mapa feito por fãs com base no que já foi mostrado. Os formatos e os nomes dos condados não são oficiais e são aproximados. A Rockstar anunciou um mapa oficial gratuito de Leonida para imprimir em 19 de novembro em rockstargames.com/VI. Trocamos pelo mapa oficial ou do jogo assim que pudermos conferir.",credit:"Quer todos os pontos achados até agora? O mapa da comunidade State of Leonida tem.",openmap:"Abrir o mapa da comunidade",
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
  var tcard=function(s,i){return '<button class="card" data-twitch="'+esc(s[0])+'"><div class="thumb ph" style="'+twPrev(s[0])+';background-size:cover;background-position:center"><span class="tag tw">Twitch</span><span class="lv">LIVE</span>'+play+'</div><div class="meta"><h3>'+esc(s[1])+'</h3><div class="sub"><span>'+esc(s[2])+'</span><span>'+s[3].toUpperCase()+'</span><span>'+p.watching(s[4])+'</span></div></div></button>'};
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
  var tot=0,dn=0,sum=0,cats=p.cc.map(function(c,ci){var items='',d=0,cs=0;c[1].forEach(function(r,ri){var id='v2-'+ci+'-'+ri,t=r[1],n=Math.min(+saved[id]||0,t),ok=n>=t;if(ok)d++;cs+=n/t;
    if(t===1){items+='<label class="ck-item"><input type="checkbox" data-ck="'+id+'"'+(ok?' checked':'')+'><span>'+esc(r[0])+'</span></label>';}
    else{items+='<div class="ck-item ck-cnt'+(ok?' ok':'')+'"><span class="nm">'+esc(r[0])+'</span><span class="ct">'+n+' / '+t+'</span><button type="button" data-ck-step="'+id+':-1:'+t+'" aria-label="-1">&minus;</button><button type="button" data-ck-step="'+id+':1:'+t+'" aria-label="+1">+</button>'+(t>=30?'<button type="button" data-ck-step="'+id+':10:'+t+'" aria-label="+10">+10</button>':'')+'</div>';}});
   tot+=c[1].length;dn+=d;sum+=cs;return '<section class="panel ck-cat"><header><h3>'+esc(c[0])+'</h3><span>'+d+' / '+c[1].length+'</span></header><div class="prog"><i style="width:'+(cs/c[1].length*100).toFixed(1)+'%"></i></div>'+items+'</section>'}).join('');
  var pc=Math.round(sum/tot*100);
  return head('ck','#B6F25A')+note(p.ck_note)+'<div class="panel ck-top"><div class="big">'+pc+'%</div><div class="lbl">'+dn+' / '+tot+' '+p.done+'</div><div class="grow prog" style="margin:0;height:10px"><i style="width:'+pc+'%"></i></div><button class="btn ghost" data-ck-reset>'+p.reset+'</button></div><div class="ck-cats">'+cats+'</div>';},
 map:function(){var p=P[lang],u='https://map.stateofleonida.net/';
  return head('map','#4DA8FF')+note(p.map_note)+'<div class="panel mapwrap" data-mapwrap style="background:#3589ae">'+
   '<div class="maptools"><button data-zoom="1" aria-label="Zoom in">+</button><button data-zoom="-1" aria-label="Zoom out">&minus;</button></div>'+
   '<svg class="map" viewBox="0 0 880 1208" aria-label="'+esc(p.map_t)+'"><g data-mapg><image href="img/leonida-map.jpg" x="0" y="0" width="880" height="1208"/></g></svg></div>';}
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
function mapInit(){var w=$('[data-mapwrap]'),g=$('[data-mapg]'),svg=$('svg.map',w),drag=null,VW=880,VH=1208;
  function k(){var r=svg.getBoundingClientRect();return Math.max(VW/r.width,VH/r.height);}
  function ap(){var m=mz.s-1;mz.x=Math.min(0,Math.max(-VW*m,mz.x));mz.y=Math.min(0,Math.max(-VH*m,mz.y));g.setAttribute('transform','translate('+mz.x+' '+mz.y+') scale('+mz.s+')');}
  function zoom(d,cx,cy){var ns=Math.min(5,Math.max(1,mz.s*(d>0?1.3:0.77)));cx=cx==null?VW/2:cx;cy=cy==null?VH/2:cy;mz.x=cx-(cx-mz.x)*ns/mz.s;mz.y=cy-(cy-mz.y)*ns/mz.s;mz.s=ns;ap();}
  function toSvg(e){var r=svg.getBoundingClientRect(),q=k();return [(e.clientX-r.left-(r.width-VW/q)/2)*q,(e.clientY-r.top-(r.height-VH/q)/2)*q];}
  ap();
  $$('[data-zoom]',w).forEach(function(b){b.addEventListener('click',function(){zoom(+b.dataset.zoom)})});
  w.addEventListener('wheel',function(e){e.preventDefault();var q=toSvg(e);zoom(e.deltaY<0?1:-1,q[0],q[1]);},{passive:false});
  svg.addEventListener('pointerdown',function(e){drag={x:e.clientX,y:e.clientY,ox:mz.x,oy:mz.y};svg.setPointerCapture(e.pointerId);});
  svg.addEventListener('pointermove',function(e){if(!drag)return;var q=k();mz.x=drag.ox+(e.clientX-drag.x)*q;mz.y=drag.oy+(e.clientY-drag.y)*q;ap();});
  svg.addEventListener('pointerup',function(){drag=null;});
  svg.addEventListener('dblclick',function(e){var q=toSvg(e);zoom(1,q[0],q[1]);});
}

page.addEventListener('click',function(e){
  var b=e.target.closest('[data-f] button');
  if(b){var cur=page.getAttribute('data-cur'),key=b.parentNode.dataset.f;state[cur]=state[cur]||({live:{pl:'all',lg:'any'},videos:{c:'all',lg:'any',s:'new'},news:{c:'all'},guides:{t:'all'}})[cur];state[cur][key]=b.dataset.v;render();return;}
  if(e.target.closest('[data-noop]')){e.preventDefault();toast.textContent=T[lang].soon;toast.classList.add('show');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('show')},2200);return;}
  var tw=e.target.closest('[data-twitch]');
  if(tw){var ch=tw.dataset.twitch,host=location.hostname||'fivestardaily.com';$('.screen',modal).style.background='#000';$('.screen',modal).innerHTML='<iframe src="https://player.twitch.tv/?channel='+encodeURIComponent(ch)+'&parent='+host+'&autoplay=true" title="Twitch" allow="autoplay; fullscreen" allowfullscreen></iframe>';$('[data-mopen]',modal).href='https://www.twitch.tv/'+encodeURIComponent(ch);$('h3',modal).textContent=$('h3',tw).textContent;$('[data-mopen]',modal).textContent=P[lang].open_tw;$('[data-mclose]',modal).textContent=P[lang].close;modal.classList.add('open');$('[data-mclose]',modal).focus();return;}
  var wv=e.target.closest('[data-watch]');
  if(wv){var id=wv.dataset.watch;$('.screen',modal).style.background='#000';var web=/^https?:$/.test(location.protocol);$('.screen',modal).innerHTML=web?'<iframe src="https://www.youtube-nocookie.com/embed/'+encodeURIComponent(id)+'?autoplay=1&rel=0" title="YouTube" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>':'<a class="offline" href="https://www.youtube.com/watch?v='+encodeURIComponent(id)+'" target="_blank" rel="noopener" style="background-image:'+(OFFI[id]?'linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.65)),url('+ytThumb(id)+')':'linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.65)),'+cover(id,3).replace('background-image:',''))+'"><span class="btn">'+play.replace('class="play"','width="16" height="16" fill="currentColor"')+esc(P[lang].open)+'</span><small>'+esc(P[lang].offline)+'</small></a>';$('[data-mopen]',modal).href='https://www.youtube.com/watch?v='+encodeURIComponent(id);$('h3',modal).textContent=$('h3',wv).textContent;$('[data-mopen]',modal).textContent=P[lang].open;$('[data-mclose]',modal).textContent=P[lang].close;modal.classList.add('open');$('[data-mclose]',modal).focus();return;}
  if(e.target.closest('[data-ck-reset]')){store.set('ck','{}');render();}
  var st=e.target.closest('[data-ck-step]');if(st){var q=st.dataset.ckStep.split(':'),s2={};try{s2=JSON.parse(store.get('ck')||'{}')}catch(x){}var v=Math.max(0,Math.min(+q[2],(+s2[q[0]]||0)+(+q[1])));if(v)s2[q[0]]=v;else delete s2[q[0]];store.set('ck',JSON.stringify(s2));var y2=scrollY;render();scrollTo(0,y2);return;}
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
function lockBadges(){if(!LOCKED.checklist)return;$$('.t-check').forEach(function(t){var b=$('.lockb',t);if(!b){b=document.createElement('span');b.className='lockb';$('.hd',t).appendChild(b);}b.innerHTML='<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.6"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>'+esc(P[lang].lk_badge);t.classList.add('locked');});}
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
