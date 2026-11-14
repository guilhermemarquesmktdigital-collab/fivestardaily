/* ---------- real data snapshot (taken __SNAPT__). In version 1 a scheduled job refreshes this every hour. ---------- */
var RD=__REAL__;
var SNAP=new Date(RD.SNAP).getTime();
var VIDS=RD.V, LIVES=RD.LIVE, PASTS=RD.PAST;
function hoursSince(t){return Math.max(1,Math.round((Date.now()-t)/36e5));}
function vAgo(h){return hoursSince(SNAP-h*36e5);}
function ytThumb(id){return 'https://i.ytimg.com/vi/'+id+'/hqdefault.jpg';}
var TH=['t1','t2','t3','t4','t5','t6'];
// Official videos show their own cover. Every other card gets a still from the official Rockstar trailers with a tint,
// so the page never shows a creator's own cover (those often carry real people's faces).
var FR=[['VQRLujxTm3c','hq2'],['QdBZY2fkU-0','hq2'],['tJbzMqJGH4k','hq3'],['ut9-aVWw2LM','hq3'],['QdBZY2fkU-0','hq3'],['VQRLujxTm3c','hq1'],['ut9-aVWw2LM','hq2'],['tJbzMqJGH4k','hq1'],['rz1B4B2yBZY','hq2'],['QdBZY2fkU-0','hq1'],['tJbzMqJGH4k','hq2'],['rz1B4B2yBZY','hq3'],['VQRLujxTm3c','hq3']];
var TINT=['rgba(91,31,140,.55)','rgba(14,74,110,.55)','rgba(140,20,70,.5)','rgba(27,42,94,.55)','rgba(120,60,10,.5)','rgba(11,60,52,.55)'];
function still(i){var f=FR[i%FR.length];return 'background-image:linear-gradient(135deg,'+TINT[i%6]+',rgba(10,6,30,.35)),url(https://i.ytimg.com/vi/'+f[0]+'/'+f[1]+'.jpg)';}
// Covers checked by hand on Nov 13: these few show real people's faces, so they get a trailer still instead.
var FACES={'qSRBrekJKy4':1,'MzWm-oH6QtA':1,'tNIxxMG-wd0':1,'Kp2mCq0DHXs':1,'T9tDQdmR_fw':1,'hhftoo-ruWA':1,'lzpGlT4EeMc':1};
function cover(id,i){return (FACES[id]||(BAKED&&!BAKED[id]))?still(i):'background-image:url(https://i.ytimg.com/vi/'+id+'/mqdefault.jpg)';}
function thumbFor(v,i){return v[7]?'<div class="thumb ph" style="background-image:url('+ytThumb(v[0])+')">':'<div class="thumb ph" style="'+cover(v[0],i)+'">';}
var OFFI={};VIDS.forEach(function(v){if(v[7])OFFI[v[0]]=1});
var LOCKED={checklist:1,map:1};
