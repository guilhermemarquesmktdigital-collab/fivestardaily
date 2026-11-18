# Daily news summaries: how to add one

Our own summaries live in `_src/air/news.json`:

```json
{
 "S": { "<source-key>": ["Outlet: Headline", "https://source-url"] },
 "NEWS": [
  {"slug": "kebab-case-unique", "date": "2026-11-14T12:00:00Z", "cat": "official|gameplay|industry|release",
   "src": ["<source-key>"], "guide": "<optional guide slug>",
   "title": {"en": "...", "es": "...", "pt": "..."},
   "body":  {"en": "<p>...</p><p>...</p>", "es": "...", "pt": "..."}}
 ]
}
```

Rules
- Facts only from the cited sources. No invented numbers, quotes or leaks presented as fact.
- 2 short paragraphs (about 90–140 words in English), then the same in Spanish and Brazilian Portuguese.
- Write it in our own words: no copied sentences, at most one short quote under 15 words.
- `src[0]` is the outlet the "Read the full story" button links to.
- Optional `guide` links to a related guide slug (release-date, pre-load, trailers, leonida-regions, gameplay-extended-look, jason-and-lucia, characters, wanted-system, combat-and-cars, things-to-do, references-and-callbacks, timeline, soundtrack, editions, cars-weapons-shops).
- Slugs must be unique and never reused.

Build and publish (from the repo root):

```bash
git pull
bash _src/build.sh
git add -A && git commit -m "News: <title>" && git push
```

The build regenerates every page, the sitemap and llms.txt. Check `news/<slug>/index.html` exists before pushing.
