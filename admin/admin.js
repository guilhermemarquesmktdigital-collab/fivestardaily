'use strict';
/* Five Star Daily admin panel. Static page: all secrets stay encrypted (PBKDF2 + AES-GCM) in admin/vault.json
   and are only opened in the browser with the passphrase. Nothing is stored in localStorage. */
const OWNER = 'guilhermemarquesmktdigital-collab', REPO = 'fivestardaily', BR = 'main';
const API = 'https://api.github.com';
const NEWS_PATH = '_src/air/news.json', VAULT_PATH = 'admin/vault.json', REQ_PATH = 'admin/requests.json';
const ITER = 600000, IDLE_MS = 15 * 60 * 1000;
const enc = new TextEncoder(), dec = new TextDecoder();
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const b64 = u => { let s = ''; for (let i = 0; i < u.length; i += 0x8000) s += String.fromCharCode.apply(null, u.subarray(i, i + 0x8000)); return btoa(s); };
const unb64 = s => Uint8Array.from(atob(s), c => c.charCodeAt(0));
const rnd = n => crypto.getRandomValues(new Uint8Array(n));
const S = { vault: null, priv: null, token: null, tab: 'news', news: null, newsSha: null, guides: null, snap: undefined, reqs: null, reqSha: null, edit: null, msg: null, fails: 0, last: Date.now() };

/* ---------- crypto ---------- */
async function kdf(pass, salt, iter) {
  const k = await crypto.subtle.importKey('raw', enc.encode(pass), 'PBKDF2', false, ['deriveKey']);
  return crypto.subtle.deriveKey({ name: 'PBKDF2', salt, iterations: iter, hash: 'SHA-256' }, k, { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']);
}
async function seal(pass, payload, pub) {
  const salt = rnd(16), iv = rnd(12), key = await kdf(pass, salt, ITER);
  const ct = await crypto.subtle.encrypt({ name: 'AES-GCM', iv }, key, enc.encode(JSON.stringify(payload)));
  return { v: 1, kdf: 'PBKDF2-SHA256', iter: ITER, salt: b64(salt), iv: b64(iv), ct: b64(new Uint8Array(ct)), pub };
}
async function openVault(pass, v) {
  const key = await kdf(pass, unb64(v.salt), v.iter);
  const pt = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: unb64(v.iv) }, key, unb64(v.ct));
  return JSON.parse(dec.decode(pt));
}
async function openSnap(sn) {
  const pk = await crypto.subtle.importKey('pkcs8', unb64(S.priv), { name: 'RSA-OAEP', hash: 'SHA-256' }, false, ['decrypt']);
  const raw = await crypto.subtle.decrypt({ name: 'RSA-OAEP' }, pk, unb64(sn.ek));
  const ak = await crypto.subtle.importKey('raw', raw, 'AES-GCM', false, ['decrypt']);
  const pt = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: unb64(sn.iv) }, ak, unb64(sn.ct));
  return JSON.parse(dec.decode(pt));
}

/* ---------- GitHub ---------- */
async function gh(method, path, body) {
  const url = `${API}/repos/${OWNER}/${REPO}${path}` + (method === 'GET' && path.startsWith('/contents') ? `?ref=${BR}&t=${Date.now()}` : '');
  const r = await fetch(url, { method, cache: 'no-store', headers: { Authorization: 'Bearer ' + S.token, Accept: 'application/vnd.github+json' }, body: body ? JSON.stringify(body) : undefined });
  if (r.status === 404 && method === 'GET') return null;
  const j = await r.json().catch(() => ({}));
  if (!r.ok) { const e = new Error(j.message || 'HTTP ' + r.status); e.status = r.status; throw e; }
  return j;
}
const getFile = async p => { const j = await gh('GET', '/contents/' + p); return j ? { sha: j.sha, text: dec.decode(unb64(j.content.replace(/\s/g, ''))) } : null; };
const putFile = (p, text, sha, msg) => gh('PUT', '/contents/' + p, { message: msg, content: b64(enc.encode(text)), branch: BR, ...(sha ? { sha } : {}) });
async function pub(url) { const r = await fetch(url + '?t=' + Date.now(), { cache: 'no-store' }); return r.ok ? r : null; }

/* ---------- helpers ---------- */
const say = (t, k = 'ok') => { S.msg = { t, k }; };
const msgHtml = () => S.msg ? `<div class="msg ${S.msg.k}">${esc(S.msg.t)}</div>` : '';
const fmtDate = d => d ? new Date(d).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' }) : '-';
const fmtN = n => n == null ? '-' : Number(n).toLocaleString('pt-BR');
const ageDays = d => d ? Math.floor((Date.now() - new Date(d + (d.length === 10 ? 'T12:00:00Z' : ''))) / 864e5) : null;
function root(html) { $('#app').innerHTML = html; }
function weak(p) {
  if (p.length < 14) return 'Use pelo menos 14 caracteres. Uma frase longa é melhor que uma senha curta.';
  if (new Set(p.toLowerCase()).size < 6) return 'Senha com poucos caracteres diferentes.';
  return '';
}

/* ---------- boot ---------- */
async function boot() {
  const r = await pub('/admin/vault.json');
  if (!r) { if (new URLSearchParams(location.search).has('setup')) return viewSetup(); return root('<div class="lock card"><div class="logo">Five Star Daily</div><p class="mu">Painel indisponível.</p></div>'); }
  S.vault = await r.json();
  viewUnlock();
}

function viewSetup() {
  root(`<div class="lock card"><div class="logo">Five Star Daily</div><h2>Criar o cofre do painel</h2>
  <p class="mu small">Primeiro acesso. A senha nunca sai do seu navegador. Ela protege o cofre que fica salvo no repositório, com seu token do GitHub e a chave que abre os números do Instagram e do Google.</p>
  ${msgHtml()}
  <label>Senha (frase longa, 14+ caracteres)</label><input id="p1" type="password" autocomplete="new-password">
  <label>Repita a senha</label><input id="p2" type="password" autocomplete="new-password">
  <label>Token do GitHub (fine-grained)</label><input id="tk" type="password" autocomplete="off" placeholder="github_pat_…">
  <p class="mu small">Crie em GitHub → Settings → Developer settings → Fine-grained tokens. Repositório: só <b>fivestardaily</b>. Permissão: <b>Contents: Read and write</b>. Validade: 90 dias.</p>
  <button class="btn" id="go">Criar cofre</button></div>`);
  $('#go').onclick = async () => {
    const p1 = $('#p1').value, p2 = $('#p2').value, tk = $('#tk').value.trim();
    const w = weak(p1);
    if (w) return again(w);
    if (p1 !== p2) return again('As senhas não são iguais.');
    if (!tk) return again('Cole o token do GitHub.');
    $('#go').disabled = true;
    try {
      S.token = tk;
      const info = await gh('GET', '');
      if (!info || !info.permissions || !info.permissions.push) throw new Error('O token não tem permissão de escrita neste repositório.');
      const kp = await crypto.subtle.generateKey({ name: 'RSA-OAEP', modulusLength: 2048, publicExponent: new Uint8Array([1, 0, 1]), hash: 'SHA-256' }, true, ['encrypt', 'decrypt']);
      const pubKey = b64(new Uint8Array(await crypto.subtle.exportKey('spki', kp.publicKey)));
      S.priv = b64(new Uint8Array(await crypto.subtle.exportKey('pkcs8', kp.privateKey)));
      const vault = await seal(p1, { priv: S.priv, token: tk }, pubKey);
      await putFile(VAULT_PATH, JSON.stringify(vault, null, 1), null, 'Admin: create vault');
      S.vault = vault; say('Cofre criado. Peça ao Claude para gerar o primeiro resumo de números.', 'ok');
      enter();
    } catch (e) { S.token = null; S.priv = null; again(e.message); }
  };
  function again(t) { say(t, 'err'); viewSetup(); }
}

function viewUnlock() {
  root(`<div class="lock card"><div class="logo">Five Star Daily</div><h2>Painel</h2>${msgHtml()}
  <label>Senha</label><input id="pw" type="password" autocomplete="current-password" autofocus>
  <div class="row mt14"><button class="btn" id="go">Entrar</button></div></div>`);
  const go = async () => {
    const pw = $('#pw').value; if (!pw) return;
    $('#go').disabled = true;
    if (S.fails) await new Promise(r => setTimeout(r, Math.min(S.fails * 1500, 15000)));
    try {
      const o = await openVault(pw, S.vault);
      S.priv = o.priv; S.token = o.token; S.fails = 0; S.msg = null; enter();
    } catch (e) { S.fails++; say('Senha incorreta.', 'err'); viewUnlock(); }
  };
  $('#go').onclick = go; $('#pw').onkeydown = e => { if (e.key === 'Enter') go(); };
}

function enter() {
  S.last = Date.now();
  ['pointerdown', 'keydown'].forEach(ev => addEventListener(ev, () => S.last = Date.now(), { passive: true }));
  setInterval(() => { if (Date.now() - S.last > IDLE_MS) location.reload(); }, 15000);
  view();
}

/* ---------- main view ---------- */
const TABS = [['news', 'Notícias'], ['guides', 'Guias'], ['numbers', 'Números'], ['ig', 'Instagram'], ['cfg', 'Configurações']];
async function view() {
  root(`<div class="top"><div class="logo">Five Star Daily · Painel</div><div class="row"><a href="/" target="_blank" rel="noopener">Abrir o site</a><button class="btn sec" id="lock">Bloquear</button></div></div>
  <div class="tabs">${TABS.map(([k, n]) => `<button class="tab ${S.tab === k ? 'on' : ''}" data-tab="${k}">${n}</button>`).join('')}</div>
  <div id="pane"><p class="mu">Carregando…</p></div>`);
  $('#lock').onclick = () => location.reload();
  document.querySelectorAll('[data-tab]').forEach(b => b.onclick = () => { S.tab = b.dataset.tab; S.edit = null; S.msg = null; view(); });
  try { await ({ news: paneNews, guides: paneGuides, numbers: paneNumbers, ig: paneIg, cfg: paneCfg }[S.tab])(); }
  catch (e) { $('#pane').innerHTML = `<div class="msg err">${esc(e.message)}</div>`; }
}
const pane = h => { $('#pane').innerHTML = msgHtml() + h; S.msg = null; document.querySelectorAll('i[data-w]').forEach(i => i.style.width = i.dataset.w + '%'); };

/* ---------- news ---------- */
const CATS = ['official', 'gameplay', 'industry', 'release'];
const SLUG = /^[a-z0-9]+(-[a-z0-9]+)*$/;
async function loadNews() {
  const f = await getFile(NEWS_PATH);
  if (!f) throw new Error('news.json não encontrado no repositório.');
  S.news = JSON.parse(f.text); S.newsSha = f.sha;
}
async function loadGuides() {
  if (S.guides) return S.guides;
  const r = await pub('/admin/guides.json'); S.guides = r ? await r.json() : [];
  return S.guides;
}
async function paneNews() {
  if (!S.news) await loadNews();
  await loadGuides();
  if (S.edit) return newsForm();
  const list = [...S.news.NEWS].sort((a, b) => b.date.localeCompare(a.date));
  pane(`<div class="card"><div class="row sb"><h2 class="h0">Notícias (${list.length})</h2><button class="btn" id="new">Nova notícia</button></div>
  <p class="mu small">Ao salvar, o GitHub reconstrói o site. Leva cerca de 2 minutos para aparecer.</p>
  <table><tr><th>Data</th><th>Categoria</th><th>Título</th><th>Fonte</th></tr>
  ${list.map(n => `<tr class="click" data-slug="${esc(n.slug)}"><td>${esc(fmtDate(n.date))}</td><td><span class="pill">${esc(n.cat)}</span></td><td>${esc(n.title.en)}</td><td class="mu small">${esc((n.src || [])[0] || '')}</td></tr>`).join('')}</table></div>`);
  $('#new').onclick = () => { S.edit = { isNew: true, n: { slug: '', date: new Date().toISOString().slice(0, 19) + 'Z', cat: 'industry', src: [], guide: '', title: { en: '', es: '', pt: '' }, body: { en: '', es: '', pt: '' } } }; view(); };
  document.querySelectorAll('tr[data-slug]').forEach(tr => tr.onclick = () => { S.edit = { isNew: false, n: JSON.parse(JSON.stringify(S.news.NEWS.find(x => x.slug === tr.dataset.slug))) }; view(); });
}
function newsForm() {
  const { n, isNew } = S.edit, g = S.guides || [];
  const srcKeys = Object.keys(S.news.S);
  pane(`<div class="card"><h2>${isNew ? 'Nova notícia' : 'Editar notícia'}</h2>
  <div class="grid"><div><label>Slug (único, não pode mudar depois)</label><input id="f-slug" value="${esc(n.slug)}" ${isNew ? '' : 'disabled'}></div>
  <div><label>Data e hora (UTC)</label><input id="f-date" type="datetime-local" value="${esc(n.date.slice(0, 16))}"></div>
  <div><label>Categoria</label><select id="f-cat">${CATS.map(c => `<option ${c === n.cat ? 'selected' : ''}>${c}</option>`).join('')}</select></div>
  <div><label>Guia relacionado (opcional)</label><select id="f-guide"><option value="">(nenhum)</option>${g.map(x => `<option value="${esc(x.slug)}" ${x.slug === n.guide ? 'selected' : ''}>${esc(x.slug)}</option>`).join('')}</select></div></div>
  <label>Fontes (chaves separadas por vírgula; a primeira vira o botão "Read the full story")</label><input id="f-src" value="${esc((n.src || []).join(', '))}" list="srckeys"><datalist id="srckeys">${srcKeys.map(k => `<option value="${esc(k)}">`).join('')}</datalist>
  <details><summary>Cadastrar uma fonte nova</summary><div class="grid"><div><label>Chave (ex: ign-gta6-patch)</label><input id="s-key"></div><div><label>Texto (Veículo: Manchete)</label><input id="s-label"></div><div><label>URL https://</label><input id="s-url"></div></div><div class="row mt10"><button class="btn sec" id="s-add">Adicionar fonte</button></div></details>
  <div class="g3">${['en', 'es', 'pt'].map(l => `<div><label>Título (${l.toUpperCase()})</label><input id="f-t${l}" value="${esc(n.title[l])}"><label>Texto em HTML (${l.toUpperCase()}) — 2 parágrafos &lt;p&gt;</label><textarea id="f-b${l}">${esc(n.body[l])}</textarea></div>`).join('')}</div>
  <p class="mu small">Regras: só fatos das fontes citadas, com suas próprias palavras. Sem números ou vazamentos inventados.</p>
  <div class="row mt14"><button class="btn" id="save">Salvar e publicar</button><button class="btn sec" id="cancel">Cancelar</button>${isNew ? '' : '<button class="btn bad" id="del">Excluir</button>'}</div></div>`);
  const read = () => {
    const v = id => $('#' + id).value.trim();
    const o = { slug: isNew ? v('f-slug') : n.slug, date: v('f-date') + ':00Z', cat: v('f-cat'), src: v('f-src').split(',').map(s => s.trim()).filter(Boolean), title: { en: v('f-ten'), es: v('f-tes'), pt: v('f-tpt') }, body: { en: v('f-ben'), es: v('f-bes'), pt: v('f-bpt') } };
    if (v('f-guide')) o.guide = v('f-guide');
    return o;
  };
  $('#cancel').onclick = () => { S.edit = null; view(); };
  $('#s-add').onclick = () => {
    const k = $('#s-key').value.trim(), l = $('#s-label').value.trim(), u = $('#s-url').value.trim();
    if (!SLUG.test(k.replace(/_/g, '-'))) return say('Chave inválida. Use letras minúsculas, números, hífen.', 'err'), keep();
    if (!l || !/^https:\/\//.test(u)) return say('Preencha o texto e uma URL https.', 'err'), keep();
    if (S.news.S[k]) return say('Essa chave já existe.', 'err'), keep();
    S.news.S[k] = [l, u]; $('#f-src').value = ($('#f-src').value ? $('#f-src').value + ', ' : '') + k; say('Fonte adicionada (salva junto com a notícia).', 'info'); keep();
  };
  function keep() { const o = read(); if (!isNew) o.slug = n.slug; S.edit.n = { ...S.edit.n, ...o, guide: o.guide || '' }; view(); }
  $('#save').onclick = async () => {
    const o = read(), err = checkNews(o, isNew);
    if (err) { say(err, 'err'); return keep(); }
    $('#save').disabled = true;
    const idx = S.news.NEWS.findIndex(x => x.slug === o.slug);
    if (idx >= 0) S.news.NEWS[idx] = o; else S.news.NEWS.push(o);
    await commitNews((isNew ? 'News: ' : 'News edit: ') + o.title.en.slice(0, 70));
  };
  if (!isNew) $('#del').onclick = async () => {
    if (!confirm('Excluir esta notícia? Ela some do site na próxima reconstrução.')) return;
    S.news.NEWS = S.news.NEWS.filter(x => x.slug !== n.slug);
    await commitNews('News delete: ' + n.slug);
  };
}
function checkNews(o, isNew) {
  if (!SLUG.test(o.slug)) return 'Slug inválido: use letras minúsculas, números e hífen.';
  if (isNew && S.news.NEWS.some(x => x.slug === o.slug)) return 'Já existe uma notícia com esse slug.';
  if (!/^\d{4}-\d\d-\d\dT\d\d:\d\d:00Z$/.test(o.date)) return 'Data inválida.';
  for (const l of ['en', 'es', 'pt']) { if (!o.title[l]) return `Falta o título em ${l.toUpperCase()}.`; if (!/<p>[\s\S]+<\/p>/.test(o.body[l])) return `O texto em ${l.toUpperCase()} precisa de parágrafos <p>…</p>.`; }
  if (!o.src.length) return 'Informe ao menos uma fonte.';
  const bad = o.src.find(k => !S.news.S[k]); if (bad) return `Fonte desconhecida: ${bad}. Cadastre-a primeiro.`;
  if (/<script|onerror=|javascript:/i.test(JSON.stringify(o))) return 'Conteúdo não permitido.';
  return '';
}
async function commitNews(msg) {
  try {
    const r = await putFile(NEWS_PATH, JSON.stringify(S.news, null, 1), S.newsSha, msg);
    S.newsSha = r.content.sha; S.edit = null;
    say('Salvo. O site é reconstruído em cerca de 2 minutos.', 'ok');
  } catch (e) {
    S.news = null; S.edit = null;
    say(e.status === 409 || e.status === 422 ? 'O arquivo mudou enquanto você editava (talvez a tarefa diária). Recarreguei; refaça a edição.' : 'Erro ao salvar: ' + e.message, 'err');
  }
  view();
}

/* ---------- guides ---------- */
async function loadReqs() {
  const f = await getFile(REQ_PATH);
  S.reqs = f ? JSON.parse(f.text) : []; S.reqSha = f ? f.sha : null;
}
async function paneGuides() {
  await loadGuides(); if (!S.reqs) await loadReqs();
  const open = new Set(S.reqs.filter(r => r.status === 'open').map(r => r.slug));
  pane(`<div class="card"><h2>Guias (${S.guides.length})</h2>
  <p class="mu small">Guias sem atualização há mais de 14 dias aparecem em vermelho. O botão pede ao Claude para revisar o guia na próxima rodada diária.</p>
  <table><tr><th>Guia</th><th>Atualizado</th><th>Idade</th><th>Ação</th></tr>
  ${S.guides.map(x => { const a = ageDays(x.upd); const st = a == null ? '<span class="pill">sem data</span>' : a > 14 ? `<span class="pill old">${a} dias</span>` : `<span class="pill ok">${a} dias</span>`;
    return `<tr><td><a href="/guides/${esc(x.slug)}/" target="_blank" rel="noopener">${esc(x.title)}</a><div class="mu small">${esc(x.slug)}</div></td><td>${esc(x.upd || '-')}</td><td>${st}</td><td>${open.has(x.slug) ? '<span class="pill ok">pedido aberto</span>' : `<button class="btn sec" data-req="${esc(x.slug)}">Pedir atualização</button>`}</td></tr>`; }).join('')}</table></div>`);
  document.querySelectorAll('[data-req]').forEach(b => b.onclick = async () => {
    b.disabled = true;
    try {
      const f = await getFile(REQ_PATH); const list = f ? JSON.parse(f.text) : [];
      list.push({ id: Date.now().toString(36), type: 'refresh-guide', slug: b.dataset.req, at: new Date().toISOString(), status: 'open' });
      await putFile(REQ_PATH, JSON.stringify(list, null, 1), f ? f.sha : null, 'Admin: request refresh ' + b.dataset.req);
      S.reqs = null; say('Pedido registrado.', 'ok');
    } catch (e) { say('Erro: ' + e.message, 'err'); }
    view();
  });
}

/* ---------- snapshot panes ---------- */
async function loadSnap() {
  if (S.snap !== undefined) return S.snap;
  const r = await pub('/admin/snapshot.enc.json');
  S.snap = r ? await openSnap(await r.json()) : null;
  return S.snap;
}
const noSnap = () => pane('<div class="card"><h2>Ainda sem dados</h2><p class="mu">O resumo criptografado ainda não foi gerado. Peça ao Claude: "atualize o painel".</p></div>');
function stale(s) { const a = ageDays(s.generated_at); return a != null && a >= 2 ? `<div class="msg info">Dados de ${esc(fmtDate(s.generated_at))} (${a} dias). Peça ao Claude para atualizar.</div>` : `<p class="mu small">Atualizado em ${esc(fmtDate(s.generated_at))}.</p>`; }
const delta = (a, b, inv) => { if (b == null || !b) return ''; const p = (a - b) / b * 100, up = inv ? p < 0 : p > 0; return `<span class="${up ? 'up' : 'down'} small">${p > 0 ? '+' : ''}${p.toFixed(0)}% vs período anterior</span>`; };
async function paneNumbers() {
  const s = await loadSnap(); if (!s || !s.site) return noSnap();
  const t = s.site, pv = t.prev || {}, mx = Math.max(1, ...(t.top_pages || []).map(x => x.clicks));
  pane(`${stale(s)}<div class="card"><h2>Google (${esc(s.period || 'últimos 28 dias')})</h2><div class="grid">
  <div class="kpi"><b>${fmtN(t.clicks)}</b><span>Cliques</span><br>${delta(t.clicks, pv.clicks)}</div>
  <div class="kpi"><b>${fmtN(t.impressions)}</b><span>Impressões</span><br>${delta(t.impressions, pv.impressions)}</div>
  <div class="kpi"><b>${t.ctr != null ? (t.ctr * (t.ctr <= 1 ? 100 : 1)).toFixed(1) + '%' : '-'}</b><span>CTR</span></div>
  <div class="kpi"><b>${t.position != null ? Number(t.position).toFixed(1) : '-'}</b><span>Posição média</span><br>${delta(t.position, pv.position, true)}</div></div></div>
  <div class="g3"><div class="card"><h2>Páginas mais vistas</h2><table>${(t.top_pages || []).map(x => `<tr><td>${esc(x.page)}<div class="bar"><i data-w="${Math.round(100 * x.clicks / mx)}"></i></div></td><td>${fmtN(x.clicks)}</td></tr>`).join('')}</table></div>
  <div class="card"><h2>Buscas que trazem gente</h2><table><tr><th>Busca</th><th>Cliques</th><th>Impr.</th></tr>${(t.top_queries || []).map(x => `<tr><td>${esc(x.query)}</td><td>${fmtN(x.clicks)}</td><td>${fmtN(x.impressions)}</td></tr>`).join('')}</table></div></div>
  ${t.note ? `<p class="mu small">${esc(t.note)}</p>` : ''}`);
}
async function paneIg() {
  const s = await loadSnap(); if (!s || !s.ig) return noSnap();
  const i = s.ig;
  pane(`${stale(s)}<div class="card"><h2>@${esc(i.handle || 'fivestardaily.news')}</h2><div class="grid">
  <div class="kpi"><b>${fmtN(i.followers)}</b><span>Seguidores</span>${i.followers_prev != null ? '<br>' + delta(i.followers, i.followers_prev) : ''}</div>
  <div class="kpi"><b>${fmtN(i.following)}</b><span>Seguindo</span></div><div class="kpi"><b>${fmtN(i.posts)}</b><span>Posts</span></div></div></div>
  <div class="g3"><div class="card"><h2>Agendados</h2>${(i.scheduled || []).length ? `<table><tr><th>Quando</th><th>Tipo</th><th>Post</th></tr>${i.scheduled.map(x => `<tr><td>${esc(x.when)}</td><td><span class="pill">${esc(x.type)}</span></td><td>${esc(x.title)}</td></tr>`).join('')}</table>` : '<p class="mu">Nada na fila. Hora de agendar mais.</p>'}</div>
  <div class="card"><h2>Últimos posts</h2>${(i.recent || []).length ? `<table><tr><th>Data</th><th>Tipo</th><th>Alcance</th><th>Likes</th></tr>${i.recent.map(x => `<tr><td>${esc(x.date)}</td><td><span class="pill">${esc(x.type)}</span><div class="mu small">${esc(x.title || '')}</div></td><td>${fmtN(x.reach ?? x.views)}</td><td>${fmtN(x.likes)}</td></tr>`).join('')}</table>` : '<p class="mu">Sem dados.</p>'}</div></div>
  ${i.note ? `<p class="mu small">${esc(i.note)}</p>` : ''}`);
}

/* ---------- settings ---------- */
function paneCfg() {
  pane(`<div class="card"><h2>Trocar a senha</h2>
  <div class="grid"><div><label>Senha atual</label><input id="c0" type="password" autocomplete="current-password"></div><div><label>Nova senha (14+)</label><input id="c1" type="password" autocomplete="new-password"></div><div><label>Repita a nova</label><input id="c2" type="password" autocomplete="new-password"></div></div>
  <div class="row mt12"><button class="btn" id="chg">Trocar senha</button></div></div>
  <div class="card"><h2>Trocar o token do GitHub</h2><p class="mu small">Use quando o token vencer (a cada 90 dias).</p>
  <div class="grid"><div><label>Senha atual</label><input id="t0" type="password" autocomplete="current-password"></div><div><label>Novo token</label><input id="t1" type="password" autocomplete="off"></div></div>
  <div class="row mt12"><button class="btn" id="tok">Salvar novo token</button></div></div>
  <div class="card"><h2>Segurança</h2><p class="mu small">O painel bloqueia sozinho após 15 minutos parado. Nada fica salvo no navegador. A criptografia roda aqui: o cofre público só abre com a senha, então ela precisa ser longa e única.</p></div>`);
  const resave = async (pass, np, token, label) => {
    try {
      await openVault(pass, S.vault);
      const cur = await getFile(VAULT_PATH);
      const v = await seal(np, { priv: S.priv, token }, S.vault.pub);
      await putFile(VAULT_PATH, JSON.stringify(v, null, 1), cur.sha, 'Admin: ' + label);
      S.vault = v; S.token = token; say('Feito.', 'ok');
    } catch (e) { say(e.name === 'OperationError' ? 'Senha atual incorreta.' : 'Erro: ' + e.message, 'err'); }
    view();
  };
  $('#chg').onclick = () => { const w = weak($('#c1').value); if (w) { say(w, 'err'); return view(); } if ($('#c1').value !== $('#c2').value) { say('As senhas novas não são iguais.', 'err'); return view(); } $('#chg').disabled = true; resave($('#c0').value, $('#c1').value, S.token, 'change passphrase'); };
  $('#tok').onclick = () => { const t = $('#t1').value.trim(); if (!t) { say('Cole o novo token.', 'err'); return view(); } $('#tok').disabled = true; resave($('#t0').value, $('#t0').value, t, 'rotate token'); };
}

boot().catch(e => root(`<div class="lock card"><div class="msg err">${esc(e.message)}</div></div>`));
