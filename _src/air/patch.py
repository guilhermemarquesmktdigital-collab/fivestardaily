import json, sys
P = sys.argv[1]
s = open(P).read()
L = s.split('\n')
i0 = next(i for i,l in enumerate(L) if l.startswith('/* aircraft */')); i1 = next(i for i,l in enumerate(L) if l.startswith('.navlight'))
css = r'''/* aircraft: flat sprites, spawned at random by the script */
.sky-air{position:absolute;inset:0;pointer-events:none;overflow:hidden}
.flyer{position:absolute;left:0;top:0;will-change:transform}
.flyer .bob{position:relative;animation:bob var(--bob,3.4s) ease-in-out infinite}
.flyer img{display:block;width:100%;height:auto;transition:filter 2.5s}
.flyer.flip img{transform:scaleX(-1)}
@keyframes bob{50%{transform:translateY(5px) rotate(var(--tilt,0deg))}}
.flyer .trail{position:absolute;top:44%;height:2px;width:260%;border-radius:2px;transition:opacity 2s}
.flyer.go-r .trail{right:92%;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.8))}
.flyer.go-l .trail{left:92%;background:linear-gradient(270deg,rgba(255,255,255,0),rgba(255,255,255,.8))}
body.ph-night .flyer .trail{opacity:0}
body.ph-night .flyer img{filter:brightness(.42) saturate(.6)}
body.ph-sunset .flyer img{filter:brightness(.85) saturate(.9) hue-rotate(-12deg)}
.flyer .lt{position:absolute;width:3px;height:3px;border-radius:50%;opacity:0;transition:opacity 2s;box-shadow:0 0 6px 1px currentColor;animation:blink 1.2s steps(1) infinite}
body.ph-night .flyer .lt,body.ph-sunset .flyer .lt{opacity:1}
@keyframes blink{0%{visibility:visible}14%{visibility:hidden}}
.flyer .beam2{position:absolute;left:50%;top:70%;width:90%;height:260%;translate:-50% 0;opacity:0;transition:opacity 2s;
  background:linear-gradient(rgba(255,255,230,.5),rgba(255,255,230,0));clip-path:polygon(45% 0,55% 0,100% 100%,0 100%)}
body.ph-night .flyer .beam2{opacity:1}
/* spinning rotors: a blurred disc plus a blade that flickers like it is turning */
.flyer .rot{position:absolute;pointer-events:none}
.flyer .rot::before{content:"";position:absolute;inset:0;border-radius:50%;background:radial-gradient(closest-side,color-mix(in srgb,var(--rc) 45%,transparent),color-mix(in srgb,var(--rc) 22%,transparent) 70%,transparent);filter:blur(.6px)}
.flyer .rot::after{content:"";position:absolute;inset:0;border-radius:3px;background:var(--rc);animation:blade-h .1s linear infinite}
.flyer .rot.v::after{animation-name:blade-v;animation-duration:.08s}
.flyer .rot.h::after{top:30%;bottom:30%}
.flyer .rot.v::after{left:25%;right:25%}
@keyframes blade-h{0%{transform:scaleX(1)}25%{transform:scaleX(.12)}50%{transform:scaleX(-1)}75%{transform:scaleX(.12)}100%{transform:scaleX(1)}}
@keyframes blade-v{0%{transform:scaleY(1)}25%{transform:scaleY(.1)}50%{transform:scaleY(-1)}75%{transform:scaleY(.1)}100%{transform:scaleY(1)}}
body.ph-night .flyer .rot{filter:brightness(.45)}'''
L[i0:i1+1] = [css]
s = '\n'.join(L)
a = s.index('  <div class="air plane">'); b = s.index('  <div class="seafill">')
s = s[:a] + s[b:]
s = s.replace('  <div class="scene" data-scene>', '  <div class="sky-air" data-air-back></div>\n  <div class="scene" data-scene>')
s = s.replace(".air{display:none}", ".sky-air{display:none}")
sp = json.load(open(sys.argv[2]))
js = open(sys.argv[3]).read().replace('__SPRITES__', json.dumps(sp))
s = s.replace("/* ---------- menu: arrow keys", js + "\n/* ---------- menu: arrow keys")
open(P, 'w').write(s)
print('ok')
