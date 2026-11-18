/* ---------- real data snapshot (taken __SNAPT__). In version 1 a scheduled job refreshes this every hour. ---------- */
var RD=__REAL__;
var SNAP=new Date(RD.SNAP).getTime();
var VIDS=RD.V, LIVES=RD.LIVE, PASTS=RD.PAST, TWITCH=RD.TW||[];
function hoursSince(t){return Math.max(1,Math.round((Date.now()-t)/36e5));}
function vAgo(h){return hoursSince(SNAP-h*36e5);}
function ytThumb(id){return 'https://i.ytimg.com/vi/'+id+'/hqdefault.jpg';}
var TH=['t1','t2','t3','t4','t5','t6'];
// Every card shows the video's or stream's own original thumbnail, so people can see their favorite creators.
var FR=[['VQRLujxTm3c','hq2'],['QdBZY2fkU-0','hq2'],['tJbzMqJGH4k','hq3'],['ut9-aVWw2LM','hq3'],['QdBZY2fkU-0','hq3'],['VQRLujxTm3c','hq1'],['ut9-aVWw2LM','hq2'],['tJbzMqJGH4k','hq1'],['rz1B4B2yBZY','hq2'],['QdBZY2fkU-0','hq1'],['tJbzMqJGH4k','hq2'],['rz1B4B2yBZY','hq3'],['VQRLujxTm3c','hq3']];
var TINT=['rgba(91,31,140,.55)','rgba(14,74,110,.55)','rgba(140,20,70,.5)','rgba(27,42,94,.55)','rgba(120,60,10,.5)','rgba(11,60,52,.55)'];
function still(i){var f=FR[i%FR.length];return 'background-image:linear-gradient(135deg,'+TINT[i%6]+',rgba(10,6,30,.35)),url(https://i.ytimg.com/vi/'+f[0]+'/'+f[1]+'.jpg)';}
function cover(id,i){return 'background-image:url(https://i.ytimg.com/vi/'+id+'/mqdefault.jpg)';}
// Twitch gives every live channel a current preview frame, so the streamer's own face shows.
function twPrev(login){return 'background-image:url(https://static-cdn.jtvnw.net/previews-ttv/live_user_'+encodeURIComponent(String(login).toLowerCase())+'-440x248.jpg?t='+Math.floor(Date.now()/120000)+'),linear-gradient(135deg,#2b1055,#0b0620)';}
function thumbFor(v,i){return v[7]?'<div class="thumb ph" style="background-image:url('+ytThumb(v[0])+')">':'<div class="thumb ph" style="'+cover(v[0],i)+'">';}
var OFFI={};VIDS.forEach(function(v){if(v[7])OFFI[v[0]]=1});
var LOCKED={checklist:1};
