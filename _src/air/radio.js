/* ---------- soundtrack player: official uploads only, played through YouTube's own embed ---------- */
(function(){
 var T=[["joMjcNtxuTU","That’s It","Yung Lean, Future & Metro Boomin"],["3Ev1PQEm7ns","RHYNO","Travis Scott"],["G59iOfClrVo","Sexy Magic","CA7RIEL & Paco Amoroso, PinkPantheress, Fred again.."],["5dPwBWvmcbQ","Flower in a Hurricane","Justice, Tame Impala, SZA, King Gizzard"],["9leAwpph-xs","Last Thing You Need","Morgan Wallen"],["wROPn_SFE5s","Suzuki","Fuerza Regida"],["76R2Q9vObqI","Macacoa 2000","Rauw Alejandro"],["0BxQ6hi3lXY","Don’t Chart","Cardi B"],["UqdOZmMQfSk","Blood In Your Eyes","Tove Lo"],["e2z4tuS4Mbo","Bright Lights, Big City","Keith Richards"],["Ip_Kc3EQiOI","Pusher","Justice & Gesaffelstein"]];
 var L={en:{b:"Soundtrack",h:"GTA VI soundtrack",n:"Official releases from the album and the Justice score, played by YouTube.",pl:"Play",pa:"Pause",pv:"Previous",nx:"Next",cl:"Close"},
  es:{b:"Banda sonora",h:"Banda sonora de GTA VI",n:"Lanzamientos oficiales del álbum y de la música de Justice, reproducidos por YouTube.",pl:"Reproducir",pa:"Pausar",pv:"Anterior",nx:"Siguiente",cl:"Cerrar"},
  pt:{b:"Trilha sonora",h:"Trilha sonora de GTA VI",n:"Lançamentos oficiais do álbum e da trilha do Justice, tocados pelo YouTube.",pl:"Tocar",pa:"Pausar",pv:"Anterior",nx:"Próxima",cl:"Fechar"}};
 function l(){return L[typeof lang==='string'&&L[lang]?lang:'en'];}
 var css=document.createElement('style');
 css.textContent='.rad-b{position:fixed;right:14px;bottom:14px;z-index:6;display:flex;align-items:center;gap:8px;border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:9px 14px 9px 11px;font:700 13.5px/1 inherit;color:#fff;background:rgba(18,10,42,.82);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);cursor:pointer}'+
 '.rad-b:hover,.rad-b:focus-visible{border-color:#fff;outline:none}.rad-b .nt{flex:none;color:#FFE08A}.rad-b .eq{display:flex;align-items:flex-end;gap:2px;height:14px}.rad-b .eq i{width:3px;height:5px;border-radius:1px;background:#FF3D8B}'+
 '.rad-on .eq i{animation:radeq .7s ease-in-out infinite alternate}.rad-on .eq i:nth-child(2){animation-delay:.2s;background:#FF8A3D}.rad-on .eq i:nth-child(3){animation-delay:.4s;background:#FFE08A}@keyframes radeq{to{height:14px}}'+
 '.rad-p{position:fixed;right:14px;bottom:62px;z-index:6;width:330px;max-width:calc(100vw - 28px);max-height:calc(100vh - 90px);display:none;flex-direction:column;border:1px solid rgba(255,255,255,.3);border-radius:10px;overflow:hidden;color:#fff;background:rgba(18,10,42,.94);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);box-shadow:0 18px 50px -12px rgba(0,0,0,.8)}'+
 '.rad-p.open{display:flex}.rad-hd{display:flex;justify-content:space-between;align-items:center;padding:10px 12px 8px;font-weight:700;font-size:15px}.rad-hd button,.rad-ct button{border:0;background:transparent;color:#fff;cursor:pointer;font-size:18px;line-height:1;padding:6px 9px;border-radius:6px}'+
 '.rad-hd button:hover,.rad-ct button:hover,.rad-ct button:focus-visible{background:rgba(255,255,255,.16);outline:none}.rad-sc{aspect-ratio:16/9;background:#000}.rad-sc iframe{width:100%;height:100%;border:0;display:block}'+
 '.rad-ct{display:flex;align-items:center;gap:4px;padding:8px 10px}.rad-ct .now{flex:1;min-width:0;font-size:13px;line-height:1.25}.rad-ct .now b{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.rad-ct .now span{display:block;opacity:.7;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'+
 '.rad-ls{overflow:auto;border-top:1px solid rgba(255,255,255,.14);min-height:0}.rad-ls button{display:block;width:100%;text-align:left;border:0;background:transparent;color:#fff;cursor:pointer;padding:7px 12px;font-size:13px;line-height:1.25}.rad-ls button span{opacity:.65}.rad-ls button:hover,.rad-ls button:focus-visible{background:rgba(255,255,255,.1);outline:none}.rad-ls button.on{background:rgba(255,61,139,.22)}'+
 '.rad-nt{padding:8px 12px 10px;font-size:11.5px;line-height:1.35;opacity:.65;border-top:1px solid rgba(255,255,255,.14)}@media (max-width:600px){.rad-b span.lb{display:none}.rad-b{padding:11px}}@media (prefers-reduced-motion:reduce){.rad-on .eq i{animation:none;height:10px}}';
 document.head.appendChild(css);
 var b=document.createElement('button');b.className='rad-b';b.type='button';b.innerHTML='<svg class="nt" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M9 18.5a3 3 0 1 1-2-2.83V5.2l12-2.4v12.7a3 3 0 1 1-2-2.83V7.04L9 8.64z"/></svg><span class="eq"><i></i><i></i><i></i></span><span class="lb"></span>';
 var p=document.createElement('div');p.className='rad-p';p.setAttribute('role','region');
 document.body.appendChild(b);document.body.appendChild(p);
 var cur=0,player=null,ready=false,playing=false,built=false;
 function txt(){var s=l();b.querySelector('.lb').textContent=s.b;b.setAttribute('aria-label',s.h);p.setAttribute('aria-label',s.h);
  if(!built)return;p.querySelector('[data-h]').textContent=s.h;p.querySelector('.rad-nt').textContent=s.n;
  var q=p.querySelectorAll('.rad-ct button');q[0].setAttribute('aria-label',s.pv);q[1].setAttribute('aria-label',playing?s.pa:s.pl);q[2].setAttribute('aria-label',s.nx);p.querySelector('.rad-hd button').setAttribute('aria-label',s.cl);}
 function mark(){var q=p.querySelectorAll('.rad-ls button');for(var i=0;i<q.length;i++)q[i].classList.toggle('on',i===cur);
  p.querySelector('.now').innerHTML='<b></b><span></span>';p.querySelector('.now b').textContent=T[cur][1];p.querySelector('.now span').textContent=T[cur][2];
  p.querySelector('[data-pp]').textContent=playing?'❚❚':'▶';b.classList.toggle('rad-on',playing);txt();}
 function go(i,play){cur=(i+T.length)%T.length;if(ready){play?player.loadVideoById(T[cur][0]):player.cueVideoById(T[cur][0]);}mark();}
 function build(){built=true;
  p.innerHTML='<div class="rad-hd"><span data-h></span><button type="button" data-x>×</button></div><div class="rad-sc"><div id="rad-yt"></div></div>'+
   '<div class="rad-ct"><button type="button" data-pv>⏮</button><button type="button" data-pp>▶</button><button type="button" data-nx>⏭</button><div class="now"></div></div>'+
   '<div class="rad-ls">'+T.map(function(t,i){return '<button type="button" data-i="'+i+'"></button>'}).join('')+'</div><div class="rad-nt"></div>';
  var q=p.querySelectorAll('.rad-ls button');for(var i=0;i<q.length;i++){q[i].innerHTML='<b></b> <span></span>';q[i].querySelector('b').textContent=T[i][1];q[i].querySelector('span').textContent='· '+T[i][2];}
  p.addEventListener('click',function(e){var t=e.target.closest('button');if(!t)return;
   if(t.hasAttribute('data-x'))p.classList.remove('open');
   else if(t.hasAttribute('data-pv'))go(cur-1,true);else if(t.hasAttribute('data-nx'))go(cur+1,true);
   else if(t.hasAttribute('data-pp')){if(ready){playing?player.pauseVideo():player.playVideo();}}
   else if(t.hasAttribute('data-i'))go(+t.getAttribute('data-i'),true);});
  mark();
  var prev=window.onYouTubeIframeAPIReady;
  function mk(){player=new YT.Player('rad-yt',{host:'https://www.youtube-nocookie.com',videoId:T[cur][0],playerVars:{playsinline:1,rel:0,modestbranding:1},
   events:{onReady:function(){ready=true;},onStateChange:function(e){if(e.data===0){go(cur+1,true);return;}playing=(e.data===1||e.data===3);mark();},onError:function(){go(cur+1,true);}}});}
  if(window.YT&&YT.Player)mk();else{window.onYouTubeIframeAPIReady=function(){if(prev)prev();mk();};var s=document.createElement('script');s.src='https://www.youtube.com/iframe_api';document.head.appendChild(s);}
 }
 b.addEventListener('click',function(){if(!built)build();p.classList.toggle('open');txt();});
 document.addEventListener('keydown',function(e){if(e.key==='Escape'&&p.classList.contains('open')&&p.contains(document.activeElement)){p.classList.remove('open');b.focus();}});
 var m=document.querySelector('[data-modal]');if(m&&window.MutationObserver)new MutationObserver(function(){if(m.classList.contains('open')&&ready&&playing)player.pauseVideo();}).observe(m,{attributes:true,attributeFilter:['class']});
 document.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('[data-lang],.seg'))setTimeout(txt,60);});
 txt();
})();
