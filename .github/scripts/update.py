"""Hourly refresh for Five Star Daily: YouTube videos and live streams, plus Google News headlines.
Free: no API keys. Writes data/feed.json; the site falls back to its built-in snapshot if this fails."""
import json, re, sys, urllib.request, urllib.parse, html, os, datetime
from email.utils import parsedate_to_datetime

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36',
      'Accept-Language': 'en-US,en;q=0.9', 'Cookie': 'CONSENT=YES+1; SOCS=CAI'}
OUT = 'data/feed.json'
OFFICIAL = {'rockstar games', 'playstation', 'playstation brasil', 'playstation españa', 'playstation latinoamérica', 'playstation latam', 'xbox'}

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read().decode('utf8', 'replace')

def yt(query, sp):
    h = get('https://www.youtube.com/results?hl=en&gl=US&search_query=' + urllib.parse.quote_plus(query) + '&sp=' + sp)
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', h)
    out = []
    def walk(o):
        if isinstance(o, dict):
            if 'videoRenderer' in o: out.append(o['videoRenderer'])
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    if m: walk(json.loads(m.group(1)))
    return out

def txt(o): 
    if not o: return ''
    return o.get('simpleText') or ''.join(r.get('text', '') for r in o.get('runs', []))

def hours_ago(s):
    m = re.search(r'(\d+)\s*(second|minute|min|hour|h|day|d|week|w|month|mo|year|y)\b', s or '')
    if not m: return None
    n, u = int(m.group(1)), m.group(2)
    return max(1, round(n * {'second': 0, 'minute': 1/60, 'min': 1/60, 'hour': 1, 'h': 1, 'day': 24, 'd': 24, 'week': 168, 'w': 168, 'month': 720, 'mo': 720, 'year': 8760, 'y': 8760}[u]))

def vcat(t):
    t = t.lower()
    if 'trailer' in t: return 'trailers'
    if re.search(r'tip|guide|things you|before you|how to|dicas|consejos|guía|guia|secret', t): return 'tips'
    if re.search(r'news|leak|update|confirm|notícia|noticia|rumor|price|preço|precio|delay', t): return 'news'
    return 'gameplay'

def ncat(t):
    t = t.lower()
    if re.search(r'trailer|rockstar (says|confirms|reveals)|official|oficial', t): return 'official'
    if re.search(r'release|launch|pre-?load|price|lançamento|lanzamiento|preço|precio|date|data|fecha', t): return 'release'
    if re.search(r'gameplay|map|mapa|graphics|gráfico|features|recursos|mission|missão|misión', t): return 'gameplay'
    return 'industry'

def is_gta(t):
    return re.search(r'gta\s*(6|vi)\b|grand theft auto vi', t, re.I)


def twitch():
    cid, sec = os.environ.get('TWITCH_CLIENT_ID'), os.environ.get('TWITCH_CLIENT_SECRET')
    if not cid or not sec: return None
    tok = json.loads(urllib.request.urlopen(urllib.request.Request('https://id.twitch.tv/oauth2/token', data=urllib.parse.urlencode({'client_id': cid, 'client_secret': sec, 'grant_type': 'client_credentials'}).encode()), timeout=30).read())['access_token']
    H = {'Client-Id': cid, 'Authorization': 'Bearer ' + tok}
    api = lambda path: json.loads(urllib.request.urlopen(urllib.request.Request('https://api.twitch.tv/helix/' + path, headers=H), timeout=30).read())['data']
    games = api('games?name=' + urllib.parse.quote('Grand Theft Auto VI'))
    if not games: return []
    gid, out = games[0]['id'], []
    for lang in ('en', 'es', 'pt'):
        for st in api('streams?first=6&game_id=%s&language=%s' % (gid, lang)):
            out.append([st['user_login'], st['title'], st['user_name'], lang, st['viewer_count']])
    return out

def main():
    prev = {}
    if os.path.exists(OUT):
        try: prev = json.load(open(OUT))
        except Exception: prev = {}
    feed = {'SNAP': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')}
    ok = 0

    # videos: newest uploads per language, official channels flagged
    V, seen = [], set()
    for lang, q, n in [('en', 'gta 6', 14), ('es', 'gta 6 español', 7), ('pt', 'gta 6 português', 7), ('en', 'grand theft auto vi rockstar games', 4)]:
        try:
            got = 0
            for v in yt(q, 'CAI%253D'):
                t, ch = txt(v.get('title')), txt(v.get('ownerText'))
                ln, pub = txt(v.get('lengthText')), txt(v.get('publishedTimeText'))
                if v['videoId'] in seen or not is_gta(t) or not ln or pub.startswith('Streamed'): continue
                h = hours_ago(pub)
                if h is None or h > 24 * 14: continue
                off = 1 if ch.lower() in OFFICIAL else 0
                V.append([v['videoId'], t, ch, 'official' if off else vcat(t), lang, ln, h, off]); seen.add(v['videoId']); got += 1
                if got >= n: break
            ok += 1
        except Exception as e: print('videos', lang, e, file=sys.stderr)
    if V: feed['V'] = V

    # live now, and recent streams
    LIVE, PAST = [], []
    for lang, q in [('en', 'gta 6 live'), ('es', 'gta 6 en vivo'), ('pt', 'gta 6 ao vivo')]:
        try:
            for v in yt(q, 'EgJAAQ%253D%253D')[:12]:
                t = txt(v.get('title'))
                if is_gta(t) and len([x for x in LIVE if x[3] == lang]) < 4:
                    LIVE.append([v['videoId'], t, txt(v.get('ownerText')), lang])
            for v in yt(q + ' stream', 'CAI%253D')[:25]:
                t, pub = txt(v.get('title')), txt(v.get('publishedTimeText'))
                if is_gta(t) and pub.startswith('Streamed') and len([x for x in PAST if x[3] == lang]) < 3:
                    PAST.append([v['videoId'], t, txt(v.get('ownerText')), lang, txt(v.get('lengthText')), hours_ago(pub) or 24])
            ok += 1
        except Exception as e: print('live', lang, e, file=sys.stderr)
    if LIVE or PAST: feed['LIVE'], feed['PAST'] = LIVE, PAST

    # Twitch lives (needs TWITCH_CLIENT_ID / TWITCH_CLIENT_SECRET secrets)
    try:
        TW = twitch()
        if TW is not None: feed['TW'] = TW; ok += 1
    except Exception as e: print('twitch', e, file=sys.stderr)

    # news headlines, each links to its source
    NEWS = {}
    for lang, qs in [('en', 'hl=en-US&gl=US&ceid=US:en'), ('es', 'hl=es-419&gl=MX&ceid=MX:es-419'), ('pt', 'hl=pt-BR&gl=BR&ceid=BR:pt-419')]:
        try:
            x = get('https://news.google.com/rss/search?q=%22GTA+6%22+OR+%22GTA+VI%22+when:7d&' + qs)
            items = []
            for it in re.findall(r'<item>(.*?)</item>', x, re.S):
                g = lambda tag: html.unescape((re.search('<%s[^>]*>(.*?)</%s>' % (tag, tag), it, re.S) or [None, ''])[1]).strip()
                title, src = g('title'), g('source')
                if src and title.endswith(' - ' + src): title = title[:-len(src) - 3]
                try: d = parsedate_to_datetime(g('pubDate'))
                except Exception: continue
                items.append([title, src, g('pubDate'), g('link'), ncat(title), d])
            items.sort(key=lambda i: i[5], reverse=True)
            if items: NEWS[lang] = [i[:5] for i in items[:12]]
            ok += 1
        except Exception as e: print('news', lang, e, file=sys.stderr)
    if NEWS: feed['NEWS'] = dict(prev.get('NEWS', {}), **NEWS)

    # keep the last good value of anything that failed this time
    for k in ('V', 'LIVE', 'PAST', 'NEWS', 'TW'):
        if k not in feed and k in prev: feed[k] = prev[k]
    if ok == 0:
        print('nothing fetched; keeping the previous feed', file=sys.stderr); return
    os.makedirs('data', exist_ok=True)
    json.dump(feed, open(OUT, 'w'), ensure_ascii=False, separators=(',', ':'))
    print('videos', len(feed.get('V', [])), 'live', len(feed.get('LIVE', [])), 'past', len(feed.get('PAST', [])), 'news', {k: len(v) for k, v in feed.get('NEWS', {}).items()}, 'twitch', len(feed.get('TW', [])))

main()
