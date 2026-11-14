/* ---------- Florida wildlife: an alligator that surfaces in the bay, and flamingos flying by ---------- */
(function(){
  if(reduce) return;
  var world=$('.world'), menuEl=$('[data-menu]');
  var gator='<svg viewBox="0 0 120 34" width="100%" height="100%" aria-hidden="true">'+
    '<ellipse class="rip r1" cx="60" cy="27" rx="56" ry="5" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="1.2"/>'+
    '<ellipse class="rip r2" cx="60" cy="27" rx="40" ry="3.5" fill="none" stroke="rgba(255,255,255,.25)" stroke-width="1"/>'+
    '<g class="body">'+
    '<path d="M6 25 Q14 20 24 21 L44 19 Q50 15 56 18 L60 18 Q64 14 70 17 L84 18 Q92 16 98 19 L116 23 Q117 26 112 27 L8 27 Q4 27 6 25Z" fill="#2E4A2A"/>'+
    '<path d="M8 22 Q11 19 14 22 M20 20 Q23 17 26 20 M84 18 Q87 15 90 18 M94 19 Q97 16 100 19" fill="none" stroke="#3E6236" stroke-width="2" stroke-linecap="round"/>'+
    '<circle cx="62" cy="17" r="3.2" fill="#3E6236"/><circle cx="70" cy="16.5" r="3.2" fill="#3E6236"/>'+
    '<circle class="eye" cx="62.6" cy="16.4" r="1.3" fill="#F2D44B"/><circle class="eye" cx="70.6" cy="15.9" r="1.3" fill="#F2D44B"/>'+
    '<path d="M100 20 Q108 19 116 22" fill="none" stroke="#1E331C" stroke-width="1"/>'+
    '</g><rect x="0" y="26" width="120" height="8" class="waterline"/></svg>';
  function gatorSpawn(){
    if(document.hidden) return;
    var hz=window.__horizon||innerHeight*.5, mt=menuEl?menuEl.getBoundingClientRect().top:innerHeight;
    if(document.querySelector('.gator')) return;
    var room=mt-hz-34, small=innerWidth<900, w, top, left;
    if(small){ w=Math.max(64,innerWidth*.17); top=hz+30+Math.random()*16; left=58+Math.random()*24; }
    else { w=Math.max(60,Math.min(90,innerWidth*.05)); top=room>8?hz+8+Math.random()*Math.min(room,120):hz-30; left=Math.random()<.5?40+Math.random()*12:68+Math.random()*16; }
    var el=document.createElement('div');
    el.className='gator'; el.style.width=w+'px'; el.style.height=(w*34/120)+'px';
    el.style.left=left+'vw'; el.style.top=top+'px';
    if(Math.random()<.5) el.style.transform='scaleX(-1)';
    el.innerHTML=gator; world.appendChild(el);
    setTimeout(function(){el.remove()},15000);
  }
  function flock(){
    if(document.hidden||document.body.classList.contains('ph-night')) return;
    var n=3+Math.floor(Math.random()*3), y=8+Math.random()*16, dir=Math.random()<.5?1:-1, dur=26000+Math.random()*8000;
    var f=document.createElement('div'); f.className='flock'; if(dir<0) f.classList.add('rev');
    var html='';
    for(var i=0;i<n;i++){
      html+='<i style="left:'+(i*34+Math.random()*10)+'px;top:'+((i%2)*14+Math.random()*8)+'px;animation-delay:-'+(Math.random()).toFixed(2)+'s">'+
      '<svg viewBox="0 0 60 24" width="44" height="18"><path d="M2 12 Q12 11 22 12 L34 12 Q42 9 48 6 Q52 4 55 6 L58 8 L54 8 Q50 8 46 11 Q40 15 30 15 L20 14 Q10 14 2 12Z" fill="#F57FA4"/>'+
      '<path class="wing" d="M24 12 Q30 0 40 2 Q34 8 32 13Z" fill="#E8628E"/><path d="M57 8 L60 10 L56 10Z" fill="#222"/></svg></i>';
    }
    f.innerHTML=html; f.style.top=y+'vh'; $('[data-air-back]').appendChild(f);
    var w=innerWidth, a=f.animate([{transform:'translateX('+(dir>0?-240:w+40)+'px)'},{transform:'translateX('+(dir>0?w+40:-240)+'px)'}],{duration:dur,easing:'linear'});
    a.onfinish=function(){f.remove()};
  }
  setTimeout(gatorSpawn,4000); setInterval(gatorSpawn,22000+Math.random()*8000);
  setTimeout(flock,9000); setInterval(flock,40000);
  window.__gator=gatorSpawn; window.__flock=flock;
})();
