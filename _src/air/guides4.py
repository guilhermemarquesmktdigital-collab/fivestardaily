"""Fourth batch: post-launch questions people actually search. Facts only from the cited sources (checked Nov 25, 2026)."""

S4 = {
 'pcg_pc': ['PC Gamer: When the heck is GTA 6 going to release on PC?', 'https://pcgamer.com/games/grand-theft-auto/gta-6-pc-release-date/'],
 'bb_patch': ['Beebom: GTA 6 patch notes and updates tracker', 'https://beebom.com/gta-6-patch-notes-updates-tracker/'],
 'tr_80h': ['TechRadar: GTA 6 can take up to 80 hours to beat, Rockstar confirms', 'https://techradar.com/gaming/gta-6-will-be-a-massive-game-and-rockstars-longest-yet-as-the-studio-confirms-it-can-take-up-to-80-hours-to-beat'],
 'tpu_rev': ['TechPowerUp: GTA 6 review roundup, 99 on Metacritic and 118 perfect scores', 'https://www.techpowerup.com/354998/gta-6-review-roundup-99-on-metacritic-and-118-perfect-scores'],
 'jj_size': ['Just Jared: GTA 6 download size and storage on PS5 and Xbox', 'https://www.justjared.com/2026/11/17/gta-6-download-size-storage-ps5-xbox-preload/'],
 'out_online': ['Outlook Respawn: GTA 6 online plans remain under wraps ahead of November release', 'https://respawn.outlookindia.com/gaming/gaming-news/gta-6-online-plans-remain-under-wraps-ahead-of-november-release'],
}

G4 = []
def g(slug, mins, src, title, lede, body, **kw):
    d = {'slug': slug, 'cat': 'game', 'mins': mins, 'src': src, 'title': title, 'lede': lede, 'body': body}
    d.update(kw); G4.append(d)

g('gta-6-pc-release-date', 3, ['pcg_pc'],
 {'en': 'GTA 6 PC release date: is there one? What Rockstar has said',
  'es': 'Fecha de GTA 6 en PC: ¿hay una? Lo que ha dicho Rockstar',
  'pt': 'Data de GTA 6 no PC: existe? O que a Rockstar já disse'},
 {'en': 'GTA 6 is out on PS5 and Xbox Series X|S. Here is what is actually known about PC, and what is only a guess.',
  'es': 'GTA 6 ya salió en PS5 y Xbox Series X|S. Esto es lo que realmente se sabe del PC y lo que es solo una suposición.',
  'pt': 'GTA 6 já saiu no PS5 e no Xbox Series X|S. Veja o que realmente se sabe sobre o PC e o que é só palpite.'},
 {'en': """<h2>The short answer</h2><p>There is <strong>no PC release date</strong>. Rockstar has not announced a date or even a window. The console launch on November 19 passed with no PC news, and as of November 20 nothing had changed.</p>
<h2>What is official</h2><p>Take-Two CEO Strauss Zelnick said in May that Rockstar prioritizes console releases. He also estimated that PC can account for roughly 45 to 50 percent of sales for a major Take-Two launch, which is why people expect a PC version eventually.</p>
<h2>What is only a guess</h2><p>PC Gamer's author estimates the PC version will not arrive before November 2027 and could slip to 2028 or later. That is an opinion, not an announcement. For context, the gap between console and PC launch was about 7 months for GTA 4, 19 months for GTA 5 and 12 months for Red Dead Redemption 2.</p>
<h2>What to do now</h2><p>Be careful with any site, video or store listing that claims a PC date or sells a "PC key". Until Rockstar announces it on its own channels, treat it as unconfirmed. We will update this page the day that changes.</p>""",
  'es': """<h2>La respuesta corta</h2><p>No hay <strong>fecha para PC</strong>. Rockstar no ha anunciado una fecha ni siquiera una ventana. El lanzamiento en consolas del 19 de noviembre pasó sin noticias de PC y, al 20 de noviembre, nada había cambiado.</p>
<h2>Qué es oficial</h2><p>El CEO de Take-Two, Strauss Zelnick, dijo en mayo que Rockstar prioriza las consolas. También estimó que el PC puede representar entre el 45 y el 50 por ciento de las ventas de un gran lanzamiento de Take-Two, por eso se espera una versión de PC más adelante.</p>
<h2>Qué es solo una suposición</h2><p>El autor de PC Gamer estima que el PC no llegará antes de noviembre de 2027 y podría ir a 2028 o más. Es una opinión, no un anuncio. Para tener contexto: entre el lanzamiento en consola y en PC pasaron unos 7 meses con GTA 4, 19 meses con GTA 5 y 12 meses con Red Dead Redemption 2.</p>
<h2>Qué hacer ahora</h2><p>Desconfía de cualquier sitio, video o tienda que diga tener fecha de PC o venda una "clave para PC". Hasta que Rockstar lo anuncie en sus canales, es información sin confirmar. Actualizaremos esta página el día que cambie.</p>""",
  'pt': """<h2>A resposta curta</h2><p>Não existe <strong>data para PC</strong>. A Rockstar não anunciou data nem janela. O lançamento nos consoles, em 19 de novembro, passou sem novidades sobre PC e, em 20 de novembro, nada tinha mudado.</p>
<h2>O que é oficial</h2><p>O CEO da Take-Two, Strauss Zelnick, disse em maio que a Rockstar prioriza os consoles. Ele também estimou que o PC pode representar de 45 a 50 por cento das vendas de um grande lançamento da Take-Two, por isso muita gente espera uma versão para PC mais adiante.</p>
<h2>O que é só palpite</h2><p>O autor da PC Gamer estima que o PC não chega antes de novembro de 2027 e pode ficar para 2028 ou depois. É opinião, não anúncio. Para ter noção: entre o lançamento no console e no PC foram cerca de 7 meses no GTA 4, 19 meses no GTA 5 e 12 meses no Red Dead Redemption 2.</p>
<h2>O que fazer agora</h2><p>Desconfie de qualquer site, vídeo ou loja que diga ter data de PC ou venda uma "chave para PC". Até a Rockstar anunciar nos canais dela, é informação não confirmada. Vamos atualizar esta página no dia em que isso mudar.</p>"""},
 upd='2026-11-25')

g('gta-6-patch-notes', 3, ['bb_patch'],
 {'en': 'GTA 6 patch notes: every update so far and what it fixed',
  'es': 'Notas de parche de GTA 6: todas las actualizaciones hasta ahora y qué corrigieron',
  'pt': 'Notas de atualização de GTA 6: todos os patches até agora e o que corrigiram'},
 {'en': 'Three updates in ten days. Here is each version, its size and what Rockstar said it changed.',
  'es': 'Tres actualizaciones en diez días. Aquí va cada versión, su tamaño y lo que Rockstar dijo que cambió.',
  'pt': 'Três atualizações em dez dias. Veja cada versão, o tamanho e o que a Rockstar disse que mudou.'},
 {'en': """<h2>Latest: 01.002.002 (November 23)</h2><p>Size: about <strong>604 MB on PS5</strong> and <strong>1.6 GB on Xbox Series X|S</strong>. It is the first update with real patch notes. Rockstar says it fixes:</p>
<ul><li>Crashes</li><li>Weather getting stuck for long periods</li><li>Autosave failures</li><li>Phone calls not triggering, including story and mission calls</li><li>Being unable to lose a Wanted Level</li><li>The deadlift bar in the Gym</li><li>Partners not handing over bags for fences</li></ul>
<h2>Earlier updates</h2><ul><li><strong>01.002.001 (November 16):</strong> about 603 MB on PS5 and 1.59 GB on Xbox. No official patch notes.</li><li><strong>01.002.000 (November 13):</strong> about 1.07 GB on both consoles. No official patch notes, and it showed up as "No Title" on PS5.</li></ul>
<h2>Good to know</h2><p>PS5 system software 26.07-14.23.00, released November 17, is not a GTA 6 patch, but it is now required to play GTA 6 on PS5. If the game will not start, update the console first.</p>
<p>We update this page whenever a new version appears with official notes.</p>""",
  'es': """<h2>La última: 01.002.002 (23 de noviembre)</h2><p>Tamaño: unos <strong>604 MB en PS5</strong> y <strong>1,6 GB en Xbox Series X|S</strong>. Es la primera con notas de parche reales. Rockstar dice que corrige:</p>
<ul><li>Cierres inesperados</li><li>El clima atascado durante mucho tiempo</li><li>Fallos del autoguardado</li><li>Llamadas que no se activaban, incluidas las de historia y misiones</li><li>No poder perder el nivel de búsqueda</li><li>La barra de peso muerto del gimnasio</li><li>Socios que no entregaban las bolsas en las ventas a receptadores</li></ul>
<h2>Actualizaciones anteriores</h2><ul><li><strong>01.002.001 (16 de noviembre):</strong> unos 603 MB en PS5 y 1,59 GB en Xbox. Sin notas oficiales.</li><li><strong>01.002.000 (13 de noviembre):</strong> unos 1,07 GB en ambas consolas. Sin notas oficiales; en PS5 apareció como "No Title".</li></ul>
<h2>Conviene saber</h2><p>El software de sistema de PS5 26.07-14.23.00, del 17 de noviembre, no es un parche de GTA 6, pero ahora es obligatorio para jugar GTA 6 en PS5. Si el juego no abre, actualiza primero la consola.</p>
<p>Actualizamos esta página cuando aparezca una versión nueva con notas oficiales.</p>""",
  'pt': """<h2>A mais recente: 01.002.002 (23 de novembro)</h2><p>Tamanho: cerca de <strong>604 MB no PS5</strong> e <strong>1,6 GB no Xbox Series X|S</strong>. É a primeira com notas de atualização de verdade. A Rockstar diz que corrige:</p>
<ul><li>Travamentos</li><li>Clima preso por muito tempo</li><li>Falhas no salvamento automático</li><li>Ligações que não tocavam, incluindo as da história e das missões</li><li>Não conseguir perder o nível de procurado</li><li>A barra do levantamento terra na academia</li><li>Parceiros que não entregavam as sacolas nas vendas para receptadores</li></ul>
<h2>Atualizações anteriores</h2><ul><li><strong>01.002.001 (16 de novembro):</strong> cerca de 603 MB no PS5 e 1,59 GB no Xbox. Sem notas oficiais.</li><li><strong>01.002.000 (13 de novembro):</strong> cerca de 1,07 GB nos dois consoles. Sem notas oficiais; no PS5 apareceu como "No Title".</li></ul>
<h2>Bom saber</h2><p>O software de sistema do PS5 26.07-14.23.00, de 17 de novembro, não é patch do GTA 6, mas agora é obrigatório para jogar GTA 6 no PS5. Se o jogo não abrir, atualize o console primeiro.</p>
<p>Atualizamos esta página sempre que sair uma versão nova com notas oficiais.</p>"""},
 upd='2026-11-25')

g('how-long-to-beat-gta-6', 3, ['tr_80h'],
 {'en': 'How long is GTA 6? Story length and what Rockstar said',
  'es': '¿Cuánto dura GTA 6? Duración de la historia y lo que dijo Rockstar',
  'pt': 'Quanto tempo dura GTA 6? Duração da história e o que a Rockstar disse'},
 {'en': 'Rockstar North\'s own number is 80 hours. Here is what that includes, and what is just an estimate.',
  'es': 'El número de Rockstar North es 80 horas. Esto es lo que incluye y lo que es solo una estimación.',
  'pt': 'O número da própria Rockstar North é 80 horas. Veja o que ele inclui e o que é só estimativa.'},
 {'en': """<h2>The official number</h2><p>Rob Nelson, head of development and co-studio head at Rockstar North, told the New York Times that his own playthrough took <strong>80 hours</strong>. That covers the main story plus some optional goals that affect the story.</p>
<h2>How it compares</h2><p>TechRadar puts GTA 5's story at about 30 hours and Red Dead Redemption 2's at up to 60, which would make GTA 6 Rockstar's longest campaign.</p>
<h2>What is an estimate</h2><p>TechRadar says that with open-world exploration and side missions the total could pass 100 hours. That is the outlet's guess, not Rockstar's. Your time will depend on how much you explore, so treat 80 hours as one developer's pace, not a rule.</p>""",
  'es': """<h2>El número oficial</h2><p>Rob Nelson, jefe de desarrollo y co-jefe del estudio en Rockstar North, dijo al New York Times que su propia partida duró <strong>80 horas</strong>. Incluye la historia principal y algunos objetivos opcionales que afectan a la historia.</p>
<h2>Cómo se compara</h2><p>TechRadar sitúa la historia de GTA 5 en unas 30 horas y la de Red Dead Redemption 2 en hasta 60, lo que haría de GTA 6 la campaña más larga de Rockstar.</p>
<h2>Qué es una estimación</h2><p>TechRadar dice que con la exploración del mundo abierto y las misiones secundarias el total podría pasar de 100 horas. Es suposición del medio, no de Rockstar. Tu tiempo dependerá de cuánto explores, así que toma las 80 horas como el ritmo de un desarrollador, no como regla.</p>""",
  'pt': """<h2>O número oficial</h2><p>Rob Nelson, chefe de desenvolvimento e co-chefe do estúdio na Rockstar North, contou ao New York Times que a própria partida dele durou <strong>80 horas</strong>. Isso inclui a história principal e alguns objetivos opcionais que afetam a história.</p>
<h2>Como se compara</h2><p>A TechRadar coloca a história do GTA 5 em cerca de 30 horas e a do Red Dead Redemption 2 em até 60, o que faria de GTA 6 a campanha mais longa da Rockstar.</p>
<h2>O que é estimativa</h2><p>A TechRadar diz que, com exploração do mundo aberto e missões secundárias, o total pode passar de 100 horas. É palpite do veículo, não da Rockstar. Seu tempo vai depender de quanto você explora, então trate as 80 horas como o ritmo de um desenvolvedor, não como regra.</p>"""},
 upd='2026-11-25')

g('gta-6-review-scores', 3, ['tpu_rev'],
 {'en': 'GTA 6 review scores: 99 on Metacritic, and the lowest score',
  'es': 'Notas de GTA 6: 99 en Metacritic y la nota más baja',
  'pt': 'Notas de GTA 6: 99 no Metacritic e a nota mais baixa'},
 {'en': 'GTA 6 tied the best Metacritic score ever. Here are the numbers, the perfect scores and the lowest review.',
  'es': 'GTA 6 igualó la mejor nota de la historia en Metacritic. Aquí están los números, los 10 perfectos y la reseña más baja.',
  'pt': 'GTA 6 igualou a melhor nota da história no Metacritic. Veja os números, as notas máximas e a análise mais baixa.'},
 {'en': """<h2>The numbers</h2><ul><li><strong>PS5: 99 on Metacritic</strong>, from 147 critic reviews, with 118 perfect scores. At the time of the roundup there were no mixed or negative reviews.</li><li><strong>Xbox Series X|S: 99</strong>, but from only 14 reviews.</li></ul><p>That ties <em>Ocarina of Time</em> and sits above GTA 4, which scored 98. Full marks came from outlets including IGN, GameSpot and Eurogamer.</p>
<h2>The lower scores</h2><p>The lowest was <strong>80 from ScreenHub</strong>, whose reviewer said the game drags on for quite a bit before it finally lets loose. Other scores below perfect included GameStar (97), Wccftech (96), and the New York Times and IGN Japan (90).</p>
<h2>Platforms</h2><p>The scores are for PS5 and Xbox Series X|S. There is no PC version yet, see our PC release date guide.</p>""",
  'es': """<h2>Los números</h2><ul><li><strong>PS5: 99 en Metacritic</strong>, con 147 reseñas de la crítica y 118 notas perfectas. Cuando se hizo el resumen no había reseñas mixtas ni negativas.</li><li><strong>Xbox Series X|S: 99</strong>, pero con solo 14 reseñas.</li></ul><p>Eso iguala a <em>Ocarina of Time</em> y supera a GTA 4, que tuvo 98. Medios como IGN, GameSpot y Eurogamer dieron la nota máxima.</p>
<h2>Las notas más bajas</h2><p>La más baja fue <strong>80 de ScreenHub</strong>, cuyo reseñista dijo que el juego se alarga bastante antes de soltarse por fin. Otras notas por debajo del máximo: GameStar (97), Wccftech (96), y el New York Times e IGN Japón (90).</p>
<h2>Plataformas</h2><p>Las notas son de PS5 y Xbox Series X|S. Todavía no hay versión de PC; mira nuestra guía de la fecha en PC.</p>""",
  'pt': """<h2>Os números</h2><ul><li><strong>PS5: 99 no Metacritic</strong>, com 147 análises da crítica e 118 notas máximas. Na época do resumo não havia análises mistas nem negativas.</li><li><strong>Xbox Series X|S: 99</strong>, mas com apenas 14 análises.</li></ul><p>Isso empata com <em>Ocarina of Time</em> e fica acima de GTA 4, que teve 98. Veículos como IGN, GameSpot e Eurogamer deram nota máxima.</p>
<h2>As notas mais baixas</h2><p>A mais baixa foi <strong>80, do ScreenHub</strong>, cujo analista disse que o jogo demora bastante até finalmente se soltar. Outras notas abaixo do máximo: GameStar (97), Wccftech (96), e o New York Times e a IGN Japão (90).</p>
<h2>Plataformas</h2><p>As notas são de PS5 e Xbox Series X|S. Ainda não há versão para PC; veja nosso guia da data no PC.</p>"""},
 upd='2026-11-25')

g('gta-6-file-size', 3, ['jj_size'],
 {'en': 'GTA 6 file size: how much space you need on PS5 and Xbox',
  'es': 'Tamaño de GTA 6: cuánto espacio necesitas en PS5 y Xbox',
  'pt': 'Tamanho de GTA 6: quanto espaço você precisa no PS5 e no Xbox'},
 {'en': 'Rockstar says up to 212 GB. Here is what to clear, how preload worked and why updates matter.',
  'es': 'Rockstar dice hasta 212 GB. Esto es lo que debes liberar, cómo funcionó la precarga y por qué importan las actualizaciones.',
  'pt': 'A Rockstar fala em até 212 GB. Veja o que liberar, como funcionou o pré-carregamento e por que as atualizações importam.'},
 {'en': """<h2>How much space</h2><p>Rockstar says GTA 6 needs <strong>up to 212 GB</strong>, depending on the console. PlayStation tells PS5 owners to clear <strong>at least 212 GB</strong> before downloading. Reported download sizes are sometimes a bit smaller, but Rockstar has not published a separate final size for each console model.</p>
<h2>Updates need room too</h2><p>Future updates may need more space, and each patch also needs temporary room while it installs. Leave extra free space beyond the base number. See our patch notes guide for the sizes of the updates so far.</p>
<h2>Preload</h2><p>Digital pre-orders could download the game starting November 10 on PS5 and Xbox Series X|S. The game stayed locked until the November 19 release.</p>
<h2>Physical copies</h2><p>Boxes sold in stores include a download code rather than a disc, so you still need the full download. See the editions guide.</p>""",
  'es': """<h2>Cuánto espacio</h2><p>Rockstar dice que GTA 6 necesita <strong>hasta 212 GB</strong>, según la consola. PlayStation recomienda a los dueños de PS5 liberar <strong>al menos 212 GB</strong> antes de descargar. Los tamaños de descarga reportados a veces son algo menores, pero Rockstar no publicó un tamaño final por modelo de consola.</p>
<h2>Las actualizaciones también ocupan</h2><p>Las próximas actualizaciones pueden necesitar más espacio, y cada parche necesita espacio temporal al instalarse. Deja espacio libre extra además del número base. Mira nuestra guía de notas de parche para ver el tamaño de las actualizaciones hasta ahora.</p>
<h2>Precarga</h2><p>Las reservas digitales pudieron descargar el juego desde el 10 de noviembre en PS5 y Xbox Series X|S. El juego siguió bloqueado hasta el lanzamiento del 19 de noviembre.</p>
<h2>Copias físicas</h2><p>Las cajas de las tiendas traen un código de descarga y no un disco, así que igual necesitas la descarga completa. Mira la guía de ediciones.</p>""",
  'pt': """<h2>Quanto espaço</h2><p>A Rockstar diz que GTA 6 precisa de <strong>até 212 GB</strong>, dependendo do console. A PlayStation orienta quem tem PS5 a liberar <strong>pelo menos 212 GB</strong> antes de baixar. Os tamanhos de download reportados às vezes são um pouco menores, mas a Rockstar não publicou um tamanho final para cada modelo de console.</p>
<h2>As atualizações também ocupam espaço</h2><p>As próximas atualizações podem precisar de mais espaço, e cada patch também precisa de espaço temporário durante a instalação. Deixe espaço livre extra além do número base. Veja nosso guia de notas de atualização para o tamanho dos patches até agora.</p>
<h2>Pré-carregamento</h2><p>Quem comprou digital antecipado pôde baixar o jogo a partir de 10 de novembro no PS5 e no Xbox Series X|S. O jogo ficou bloqueado até o lançamento de 19 de novembro.</p>
<h2>Cópias físicas</h2><p>As caixas das lojas trazem um código de download e não um disco, então você ainda precisa do download completo. Veja o guia de edições.</p>"""},
 upd='2026-11-25')

g('gta-online-gta-6', 3, ['out_online'],
 {'en': 'GTA 6 multiplayer: is there a GTA Online 2? What is confirmed',
  'es': 'Multijugador de GTA 6: ¿hay GTA Online 2? Qué está confirmado',
  'pt': 'Multiplayer de GTA 6: existe GTA Online 2? O que está confirmado'},
 {'en': 'Rockstar has not announced online for GTA 6. Here is the line between what is official and what is reporting.',
  'es': 'Rockstar no ha anunciado online para GTA 6. Aquí está la línea entre lo oficial y lo que son informes.',
  'pt': 'A Rockstar não anunciou online para GTA 6. Veja a linha entre o que é oficial e o que é reportagem.'},
 {'en': """<h2>What is official</h2><ul><li>Rockstar has <strong>not announced</strong> a release date, pricing or other details for a GTA 6 multiplayer mode.</li><li>Take-Two CEO Strauss Zelnick said the company expects to keep supporting the current <strong>GTA Online</strong> after GTA 6 launches, and does not expect its update cadence to change materially.</li></ul>
<h2>What is reporting, not a statement</h2><p>Bloomberg's Jason Schreier has reported that Rockstar is not planning to talk about the new GTA Online anytime soon. That is a journalist's account, not a company statement. Launch timing, business model and bundling are all speculation, and there is no evidence the new online mode will use a dedicated-server model like FiveM.</p>
<h2>What it means for you</h2><p>Right now GTA 6 is a story-first launch. If you play GTA Online today, it keeps running. We will update this page when Rockstar announces anything.</p>""",
  'es': """<h2>Qué es oficial</h2><ul><li>Rockstar <strong>no ha anunciado</strong> fecha, precio ni otros detalles de un modo multijugador de GTA 6.</li><li>El CEO de Take-Two, Strauss Zelnick, dijo que la empresa espera seguir dando soporte al <strong>GTA Online</strong> actual después del lanzamiento de GTA 6 y no espera que cambie mucho su ritmo de actualizaciones.</li></ul>
<h2>Qué son informes, no declaraciones</h2><p>Jason Schreier, de Bloomberg, informó de que Rockstar no planea hablar del nuevo GTA Online en el corto plazo. Es el relato de un periodista, no una declaración de la empresa. El momento de lanzamiento, el modelo de negocio y los paquetes son especulación, y no hay evidencia de que el nuevo modo online use servidores dedicados como FiveM.</p>
<h2>Qué significa para ti</h2><p>Por ahora GTA 6 es un lanzamiento centrado en la historia. Si juegas GTA Online hoy, sigue funcionando. Actualizaremos esta página cuando Rockstar anuncie algo.</p>""",
  'pt': """<h2>O que é oficial</h2><ul><li>A Rockstar <strong>não anunciou</strong> data, preço nem outros detalhes de um modo multiplayer de GTA 6.</li><li>O CEO da Take-Two, Strauss Zelnick, disse que a empresa espera continuar dando suporte ao <strong>GTA Online</strong> atual depois do lançamento de GTA 6 e não espera mudança relevante no ritmo de atualizações.</li></ul>
<h2>O que é reportagem, não declaração</h2><p>Jason Schreier, da Bloomberg, relatou que a Rockstar não pretende falar do novo GTA Online tão cedo. É o relato de um jornalista, não uma declaração da empresa. Momento de lançamento, modelo de negócio e pacotes são especulação, e não há evidência de que o novo modo online use servidores dedicados como o FiveM.</p>
<h2>O que isso significa para você</h2><p>Por enquanto GTA 6 é um lançamento focado na história. Se você joga GTA Online hoje, ele continua funcionando. Vamos atualizar esta página quando a Rockstar anunciar algo.</p>"""},
 upd='2026-11-25')
