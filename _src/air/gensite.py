"""Generate the deployable static site: one folder per page, each with its own title/description/canonical.
usage: python3 gensite.py <out_dir> <base_path> <origin> [noindex]
"""
import json, os, re, shutil, sys, html
SC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import datetime; TODAY = datetime.date.today().isoformat()
out, base, origin = sys.argv[1], sys.argv[2], sys.argv[3].rstrip('/')
noindex = len(sys.argv) > 4
C = json.load(open(SC + '/air/content.json'))
src = open(SC + '/fsd/index.html').read()

# images and icons load from the site root, so nested pages find them
for n in ['island', 'water', 'rocks']:
    src = src.replace(f'img/{n}.webp', f'{base}img/{n}.webp')
src = src.replace('<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">', '')

HOME_T = 'Five Star Daily: GTA 6 news, videos, live streams and guides'
HOME_D = 'Unofficial GTA 6 fan hub. Live streams, new videos, daily news with our own summaries, guides in English, Spanish and Portuguese.'
pages = [('', HOME_T, HOME_D),
 ('live', 'GTA 6 live streams right now | Five Star Daily', 'Who is streaming GTA 6 right now on YouTube, plus recent streams you can rewatch.'),
 ('videos', 'New GTA 6 videos and official trailers | Five Star Daily', 'The latest GTA 6 gameplay, tips and news videos from creators, and every official Rockstar trailer, playable on one page.'),
 ('news', 'GTA 6 news today | Five Star Daily', 'Today\'s GTA 6 headlines from across the web, with short summaries we write ourselves and a link to every source.'),
 ('guides', 'GTA 6 guides | Five Star Daily', 'Step-by-step GTA 6 guides: release date and platforms, how to pre-load, every trailer and the regions of Leonida.'),
 ('map', 'GTA 6 map of Leonida | Five Star Daily', 'An interactive map of Leonida with the six regions Rockstar has confirmed: Vice City, Leonida Keys, Grassrivers, Port Gellhorn, Ambrosia and Mount Kalaga.'),
 ('checklist', 'GTA 6 100% checklist | Five Star Daily', 'Track your GTA 6 progress toward 100% completion. Opens on launch day, November 19.')]
for g in C['GUIDES']:
    pages.append(('guides/' + g['slug'], g['title']['en'] + ' | Five Star Daily', g['lede']['en']))
for n in C['NEWS']:
    desc = re.sub('<[^>]+>', '', n['body']['en']).strip()
    pages.append(('news/' + n['slug'], n['title']['en'] + ' | Five Star Daily', desc[:155].rsplit(' ', 1)[0] + '…' if len(desc) > 158 else desc))
for k in ['about', 'contact', 'privacy', 'terms']:
    pages.append((k, C['PAGES'][k]['title']['en'] + ' | Five Star Daily', {'about': 'Who runs Five Star Daily, what you will find here and how we work.', 'contact': 'How to reach the Five Star Daily team.', 'privacy': 'How Five Star Daily handles your data, cookies and ads.', 'terms': 'The terms for using Five Star Daily.'}[k]))

FAV = '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 24 24%27%3E%3Crect width=%2724%27 height=%2724%27 rx=%275%27 fill=%27%23140E2E%27/%3E%3Cpath d=%27M12 4l2.3 5 5.5.5-4.2 3.6 1.3 5.4L12 15.6l-4.9 2.9 1.3-5.4-4.2-3.6 5.5-.5z%27 fill=%27%23FFC94A%27/%3E%3C/svg%3E">'

ARTS = {('guides/' + g['slug']): ('2026-11-13', g['title']['en'], g['lede']['en']) for g in C['GUIDES']}
ARTS.update({('news/' + n['slug']): (n['date'][:10], n['title']['en'], re.sub('<[^>]+>', '', n['body']['en'])[:200]) for n in C['NEWS']})
def jsonld(path, url, title, desc):
    org = {'@type': 'Organization', 'name': 'Five Star Daily', 'url': origin + base, 'email': C['EMAIL']}
    if not path:
        d = [{'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Five Star Daily', 'url': origin + base, 'description': desc, 'inLanguage': ['en', 'es', 'pt-BR'], 'publisher': org}, dict(org, **{'@context': 'https://schema.org'})]
    elif path in ARTS:
        date, h, ab = ARTS[path]
        d = [{'@context': 'https://schema.org', '@type': 'NewsArticle' if path.startswith('news/') else 'Article', 'headline': h, 'description': ab, 'datePublished': date, 'dateModified': '2026-11-13', 'url': url, 'mainEntityOfPage': url, 'inLanguage': 'en', 'author': org, 'publisher': org, 'about': {'@type': 'VideoGame', 'name': 'Grand Theft Auto VI'}}]
    else:
        d = [{'@context': 'https://schema.org', '@type': 'WebPage', 'name': title, 'description': desc, 'url': url, 'isPartOf': {'@type': 'WebSite', 'name': 'Five Star Daily', 'url': origin + base}}]
    return ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>\n' for x in d)

def page_html(path, title, desc, robots_noindex=False):
    url = origin + base + (path + '/' if path else '')
    head = (f'<meta name="fsd-base" content="{base}">\n'
            f'<link rel="canonical" href="{url}">\n'
            f'<meta property="og:type" content="website">\n<meta property="og:site_name" content="Five Star Daily">\n'
            f'<meta property="og:title" content="{html.escape(title)}">\n<meta property="og:description" content="{html.escape(desc)}">\n'
            f'<meta property="og:url" content="{url}">\n<meta name="twitter:card" content="summary">\n' + FAV + '\n' + jsonld(path, url, title, desc)
            + ('<meta name="robots" content="noindex, nofollow">\n' if (noindex or robots_noindex) else ''))
    s = re.sub(r'<title>.*?</title>', '<title>' + html.escape(title) + '</title>', src, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + html.escape(desc) + '">', s, count=1)
    if '<meta name="description"' not in s:
        s = s.replace('</title>', '</title>\n<meta name="description" content="' + html.escape(desc) + '">', 1)
    return s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + head, 1)

if os.path.exists(out):
    for f in os.listdir(out):
        if f in ('.git', 'CNAME', '.github', 'README.md', 'ads.txt', 'data', '_src'):
            continue
        p = os.path.join(out, f)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
os.makedirs(out + '/img', exist_ok=True)
for n in ['island', 'water', 'rocks']:
    shutil.copy(f'{SC}/fsd/img/{n}.webp', f'{out}/img/{n}.webp')
for path, title, desc in pages:
    d = os.path.join(out, path)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(page_html(path, title, desc))
open(out + '/404.html', 'w').write(page_html('', HOME_T, HOME_D, True))
open(out + '/.nojekyll', 'w').write('')
K = open(SC + '/air/indexnow.key').read().strip()
open(f'{out}/{K}.txt', 'w').write(K)
# indexnow
if not noindex:
    urls = ''.join(f'<url><loc>{origin}{base}{p + "/" if p else ""}</loc><lastmod>{TODAY}</lastmod></url>' for p, _, _ in pages if p not in ('checklist', 'map'))
    open(out + '/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + '</urlset>\n')
    llms = ['# Five Star Daily', '', '> Unofficial fan site about Grand Theft Auto VI (GTA 6). Live streams, new videos, daily news with our own summaries, guides in English, Spanish and Portuguese. Not affiliated with Rockstar Games or Take-Two Interactive.', '', '## Guides']
    llms += [f'- [{g["title"]["en"]}]({origin}{base}guides/{g["slug"]}/): {g["lede"]["en"]}' for g in C['GUIDES']]
    llms += ['', '## News (our summaries)'] + [f'- [{n["title"]["en"]}]({origin}{base}news/{n["slug"]}/)' for n in C['NEWS']]
    llms += ['', '## Sections', f'- [Live streams]({origin}{base}live/)', f'- [Videos and official trailers]({origin}{base}videos/)', f'- [News]({origin}{base}news/)', '', '## About', f'- [About]({origin}{base}about/)', f'- [Contact]({origin}{base}contact/)', f'- [Privacy]({origin}{base}privacy/)']
    open(out + '/llms.txt', 'w').write('\n'.join(llms) + '\n')
    open(out + '/robots.txt', 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {origin}{base}sitemap.xml\n')
print(len(pages), 'pages ->', out)
