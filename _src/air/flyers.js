/* ---------- aircraft: one or two at a time, picked at random ---------- */
var SP=__SPRITES__;
// face: which way the drawing points. layer: behind or in front of the palms. alt: % of screen height. dur: seconds to cross. w: width at 1440px.
var TYPES=[
 {k:'airliner',face:-1,alt:[7,16],dur:52,w:74,trail:1,lights:[[.06,.28,'#ff3344'],[.93,.08,'#ffffff']],weight:3},
 {k:'jet',face:1,alt:[8,18],dur:16,w:54,trail:1,lights:[[.05,.35,'#ff3344']],weight:2},
 {k:'blimp',face:1,alt:[14,24],dur:110,w:96,lights:[[.5,.98,'#ff3344']],weight:1,bob:'5s'},
 {k:'heli_y',face:1,alt:[24,40],dur:42,w:54,beam:1,lights:[[.1,.25,'#ff3344']],weight:3,tilt:'-3deg',bob:'2.6s',
   rotors:[[.694,.085,.62,.07,'h','#23304a']]},
 {k:'heli_g',face:1,alt:[22,38],dur:46,w:54,beam:1,lights:[[.08,.4,'#ff3344']],weight:2,tilt:'-3deg',bob:'2.4s',
   rotors:[[.676,.087,.64,.065,'h','#4E5A1E'],[.086,.46,.034,.6,'v','#4E5A1E']]},
 {k:'prop',face:1,alt:[16,30],dur:30,w:50,lights:[[.1,.2,'#ff3344']],weight:2,tilt:'2deg',
   rotors:[[.962,.5,.036,.92,'v','#23304a']]},
 {k:'balloon',face:1,alt:[16,30],dur:140,w:28,rise:-5,weight:1,bob:'6s'},
 {k:'balloon2',face:1,alt:[18,32],dur:150,w:26,rise:-4,weight:1,bob:'6.5s'},
 {k:'para',face:1,alt:[8,10],dur:60,w:24,rise:24,weight:1,bob:'4s',tilt:'4deg'}
];
var back=$('[data-air-back]'), live=0, lastK='';
function pick(){var tot=0;TYPES.forEach(function(t){if(t.k!==lastK)tot+=t.weight});var r=Math.random()*tot;
  for(var i=0;i<TYPES.length;i++){var t=TYPES[i];if(t.k===lastK)continue;if((r-=t.weight)<0)return t;}return TYPES[0];}
function fly(t,startAt,forceDir){
  t=t||pick(); lastK=t.k; live++;
  var vw=innerWidth, vh=innerHeight, sc=Math.min(1.25,Math.max(.62,vw/1440)), w=t.w*sc, sp=SP[t.k];
  var dir=forceDir||(Math.random()<.5?1:-1); if(t.k==='para'||t.k.indexOf('balloon')===0) dir=1;
  var el=document.createElement('div'); el.className='flyer '+(dir>0?'go-r':'go-l')+(dir!==t.face?' flip':''); el.style.width=w+'px';
  var inner='<div class="bob" style="'+(t.bob?'--bob:'+t.bob+';':'')+(t.tilt?'--tilt:'+t.tilt:'')+'">';
  if(t.trail) inner+='<div class="trail"></div>';
  if(t.beam) inner+='<div class="beam2"></div>';
  inner+='<img alt="" src="'+sp[0]+'" width="'+sp[1]+'" height="'+sp[2]+'">';
  (t.lights||[]).forEach(function(l,i){var x=dir!==t.face?1-l[0]:l[0];inner+='<i class="lt" style="left:'+(x*100).toFixed(1)+'%;top:'+(l[1]*100).toFixed(1)+'%;color:'+l[2]+';background:'+l[2]+';animation-delay:'+(i*.45)+'s"></i>';});
  (t.rotors||[]).forEach(function(r){var cx=dir!==t.face?1-r[0]:r[0];
    inner+='<i class="rot '+r[4]+'" style="left:'+((cx-r[2]/2)*100).toFixed(2)+'%;top:'+((r[1]-r[3]/2)*100).toFixed(2)+'%;width:'+(r[2]*100).toFixed(2)+'%;height:'+(r[3]*100).toFixed(2)+'%;--rc:'+r[5]+'"></i>';});
  el.innerHTML=inner+'</div>';
  back.appendChild(el);
  var y0=vh*(t.alt[0]+Math.random()*(t.alt[1]-t.alt[0]))/100, y1=y0+vh*(t.rise||0)/100;
  var x0=dir>0?-w-40:vw+40, x1=dir>0?vw+40+w*2.6:-w*3.6-40;
  var dur=t.dur*1000*(0.85+Math.random()*.3)*Math.max(.7,vw/1440);
  var an=el.animate([{transform:'translate('+x0+'px,'+y0+'px)'},{transform:'translate('+x1+'px,'+y1+'px)'}],{duration:dur,easing:'linear'});
  if(startAt) an.currentTime=dur*startAt;
  an.onfinish=function(){el.remove();live--;};
}
function schedule(){ setTimeout(function(){ if(!document.hidden&&live<2) fly(); schedule(); }, 7000+Math.random()*9000); }
if(!reduce){ fly(TYPES[0],.4,-1); fly(TYPES[3],.3,1); schedule(); }
window.__launch=function(k,at,d){fly(TYPES.filter(function(t){return t.k===k})[0],at,d)};
