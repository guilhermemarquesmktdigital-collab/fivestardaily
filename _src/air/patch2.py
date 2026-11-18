import re, sys
P = sys.argv[1]
s = open(P).read()
# tiles become links to the inner pages
routes = {'t-live': 'live', 't-videos': 'videos', 't-launch': 'news', 't-news': 'news', 't-guides': 'guides', 't-check': 'checklist', 't-map': 'map'}
for cls, r in routes.items():
    a = '<button class="tile %s" data-soon>' % cls
    assert a in s, a
    s = s.replace(a, '<a class="tile %s" href="#%s">' % (cls, r))
nav_a = s.index('<nav class="menu"'); nav_b = s.index('</nav>', nav_a)
nav = s[nav_a:nav_b].replace('</button>\n\n', '</a>\n\n').replace('    </button>\n  ', '    </a>\n  ')
nav = re.sub(r'</button>(\s*)(?=<a class="tile|$)', r'</a>\1', nav)
s = s[:nav_a] + nav + s[nav_b:]
assert s[nav_a:s.index('</nav>', nav_a)].count('</a>') == 7, s[nav_a:s.index('</nav>', nav_a)].count('</a>')
s = s.replace('.tile{--acc:var(--pink);position:relative;', '.tile{--acc:var(--pink);color:inherit;text-decoration:none;position:relative;')
s = s.replace('</nav>\n', '</nav>\n\n  <main class="page" data-page aria-live="polite"></main>\n', 1)
s = s.replace('<div class="toast" role="status" data-toast></div>',
 '<div class="toast" role="status" data-toast></div>\n<div class="modal" data-modal role="dialog" aria-modal="true"><div class="box"><div class="screen"></div><div class="row"><h3></h3><div style="display:flex;gap:8px"><a class="btn" href="#" data-mopen hidden style="display:none">Open</a><button class="btn ghost" data-mclose>Close</button></div></div></div></div>')
s = s.replace('</style>', open(sys.argv[2]).read() + '\n</style>', 1)
a = "  var dirs={ArrowRight"
assert a in s
s = s.replace(a, "  if(document.body.classList.contains('inner'))return;\n" + a)
a = "applyPhase(); applyCursor("
assert a in s
s = s.replace(a, open(sys.argv[3]).read() + '\n' + open(sys.argv[3].replace('pages.js','critters.js')).read() + '\n' + open(sys.argv[3].replace('pages.js','radio.js')).read() + '\n' + a)
open(P, 'w').write(s); print('ok2')
