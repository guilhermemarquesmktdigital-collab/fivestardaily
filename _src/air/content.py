import json
EMAIL = "contact@fivestardaily.com"
UPD = "2026-11-13"

S = {
 'rs_preload': ['Rockstar Support: Grand Theft Auto VI Pre-Load FAQ', 'https://support.rockstargames.com/articles/7nPqOA2uCbpEQHXx7KVrYd'],
 'ps_preload': ['PlayStation Blog: Pre-load Grand Theft Auto VI on PS5 starting today', 'https://blog.playstation.com/?p=425567'],
 'ps_features': ['PlayStation Blog: Grand Theft Auto VI plays best on PS5 November 19', 'https://blog.playstation.com/2026/06/24/grand-theft-auto-vi-plays-best-on-ps5-november-19/'],
 'wc_cloud': ['Windows Central: GTA 6 will be playable on Xbox Cloud Gaming, with a few catches', 'https://www.windowscentral.com/gaming/xbox/grand-theft-auto-6-will-be-playable-on-xbox-cloud-gaming-but-there-are-a-few-catches'],
 'push_code': ['Push Square: GTA 6 physical edition is a code in the box', 'https://www.pushsquare.com/news/2026/06/gta-6-physical-edition-doesnt-come-with-discs-its-a-code-in-the-box'],
 'wikily': ['Wikily: GTA 6 trailers', 'https://wikily.gg/gta-6/trailers'],
 'gfinity': ['Gfinity: Every confirmed location in Leonida', 'https://www.gfinityesports.com/article/gta-6-map-guide-every-confirmed-location-in-leonida'],
}

GUIDES = [
 {'slug': 'release-date', 'cat': 'start', 'mins': 3, 'src': ['ps_preload', 'wc_cloud', 'rs_preload'],
  'title': {'en': 'GTA 6 release date: out now (Nov 19, 2026), editions and platforms', 'es': 'Fecha de GTA 6: ya salió (19 nov 2026), ediciones y plataformas', 'pt': 'Data de GTA 6: já saiu (19 nov 2026), edições e plataformas'},
  'lede': {'en': 'GTA 6 released November 19, 2026 on PS5 and Xbox Series X|S. Unlock time, editions, file size (about 212 GB on PS5, 234 GB on Xbox) and what is confirmed.',
           'es': 'GTA 6 salió el 19 de noviembre de 2026 en PS5 y Xbox Series X|S. Fecha, plataformas, tamaño y lo confirmado.',
           'pt': 'GTA 6 saiu em 19 de novembro de 2026 no PS5 e Xbox Series X|S. Data, plataformas, tamanho e o que é confirmado.'},
  'body': {
   'en': """<p><strong>Quick answer:</strong> GTA 6 launched on November 19, 2026. On PS5 it unlocked at midnight in your own time zone, so for most people that is the night of November 18 going into the 19th. Free space needed: about 212 GB on PS5 and 234 GB on Xbox Series X|S.</p>
<h2>The date</h2><p>Grand Theft Auto VI launches on <strong>Thursday, November 19, 2026</strong>.</p>
<h2>Platforms</h2><ul><li><strong>PlayStation 5</strong> and <strong>PS5 Pro</strong></li><li><strong>Xbox Series X|S</strong></li><li><strong>Xbox One and Xbox Series X|S through Xbox Cloud Gaming</strong>, from launch day</li></ul>
<p>Cloud play on Xbox does not include PC, mobile or TV devices, and it runs at Xbox Series S settings. Rockstar has not announced a PC version.</p>
<h2>What time it unlocks</h2><p>On PS5 the game unlocks at <strong>midnight local time</strong> in each country. New Zealand goes first, and the rest of the world follows as midnight reaches each time zone. If you are on Xbox, check the store page on your console for your local unlock time.</p>
<h2>Our tip</h2><p>Pre-load now, so launch night is only about the unlock and not a 200 GB download. Our pre-load guide shows how.</p>""",
   'es': """<p><strong>Respuesta rápida:</strong> GTA 6 sale el 19 de noviembre de 2026. En PS5 se desbloquea a la medianoche de tu propia zona horaria, así que para la mayoría es la noche del 18 hacia el 19. Espacio libre necesario: unos 212 GB en PS5 y 234 GB en Xbox Series X|S.</p>
<h2>La fecha</h2><p>Grand Theft Auto VI sale el <strong>jueves 19 de noviembre de 2026</strong>.</p>
<h2>Plataformas</h2><ul><li><strong>PlayStation 5</strong> y <strong>PS5 Pro</strong></li><li><strong>Xbox Series X|S</strong></li><li><strong>Xbox One y Xbox Series X|S mediante Xbox Cloud Gaming</strong>, desde el día del lanzamiento</li></ul>
<p>El juego en la nube de Xbox no incluye PC, móviles ni televisores, y funciona con los ajustes de Xbox Series S. Rockstar no ha anunciado una versión para PC.</p>
<h2>A qué hora se desbloquea</h2><p>En PS5 el juego se desbloquea a la <strong>medianoche local</strong> de cada país. Nueva Zelanda es la primera y el resto del mundo sigue a medida que llega la medianoche a cada zona horaria. En Xbox, revisa la página de la tienda en tu consola para ver tu hora local.</p>
<h2>Nuestro consejo</h2><p>Haz la precarga ya, así la noche del lanzamiento solo esperas el desbloqueo y no una descarga de 200 GB. Nuestra guía de precarga explica cómo.</p>""",
   'pt': """<p><strong>Resposta rápida:</strong> GTA 6 sai em 19 de novembro de 2026. No PS5 libera à meia-noite do seu próprio fuso, então para a maioria é a noite do dia 18 para o 19. Espaço livre necessário: cerca de 212 GB no PS5 e 234 GB no Xbox Series X|S.</p>
<h2>A data</h2><p>Grand Theft Auto VI chega na <strong>quinta-feira, 19 de novembro de 2026</strong>.</p>
<h2>Plataformas</h2><ul><li><strong>PlayStation 5</strong> e <strong>PS5 Pro</strong></li><li><strong>Xbox Series X|S</strong></li><li><strong>Xbox One e Xbox Series X|S pelo Xbox Cloud Gaming</strong>, desde o dia do lançamento</li></ul>
<p>O jogo na nuvem do Xbox não inclui PC, celular nem TV, e roda com as configurações do Xbox Series S. A Rockstar não anunciou versão para PC.</p>
<h2>Que horas libera</h2><p>No PS5 o jogo libera à <strong>meia-noite no horário local</strong> de cada país. A Nova Zelândia é a primeira, e o resto do mundo vem em seguida conforme a meia-noite chega em cada fuso. No Xbox, confira a página da loja no seu console para ver o horário local.</p>
<h2>Nossa dica</h2><p>Faça o pre-load agora, assim na noite do lançamento você só espera liberar e não um download de 200 GB. O nosso guia de pre-load mostra como.</p>"""}},
 {'slug': 'pre-load', 'cat': 'start', 'mins': 3, 'src': ['rs_preload', 'ps_preload', 'push_code'],
  'title': {'en': 'How to pre-load GTA 6, and how much space you need', 'es': 'Cómo hacer la precarga de GTA 6 y cuánto espacio necesitas', 'pt': 'Como fazer o pre-load de GTA 6 e quanto espaço você precisa'},
  'lede': {'en': 'Pre-loading is open on PS5 and Xbox Series X|S. Here is how to get the game installed before launch night.',
           'es': 'La precarga ya está abierta en PS5 y Xbox Series X|S. Así dejas el juego instalado antes de la noche del lanzamiento.',
           'pt': 'O pre-load já está aberto no PS5 e no Xbox Series X|S. Veja como deixar o jogo instalado antes da noite do lançamento.'},
  'body': {
   'en': """<p><strong>Quick answer:</strong> Open the game page in your PlayStation Store or Microsoft Store library and start the download. You need about 212 GB free on PS5 and 234 GB on Xbox Series X|S. Leave the console in rest mode so it finishes overnight.</p>
<h2>When it started</h2><ul><li><strong>PS5:</strong> from midnight local time on November 10, 2026.</li><li><strong>Xbox Series X|S:</strong> from 12 a.m. GMT on November 10, 2026, at the same moment worldwide.</li></ul>
<h2>Space you need</h2><p>Rockstar says the pre-load needs <strong>up to 212 GB</strong> of free space, depending on your console. Free up a little more than that, because installs need some room to unpack.</p>
<h2>Step by step</h2><ol><li>Pre-order the digital edition in the PlayStation Store or the Microsoft Store, if you have not yet.</li><li>Open the game's page in your library and start the download.</li><li>Leave the console in rest mode with downloads on, so it finishes overnight.</li><li>On launch day, connect once so the game can unlock.</li></ol>
<h2>Bought a physical copy?</h2><p>The boxed edition comes with a download code instead of a disc. Redeem the code in your console's store and the pre-load starts the same way.</p>""",
   'es': """<p><strong>Respuesta rápida:</strong> Abre la página del juego en tu biblioteca de PlayStation Store o Microsoft Store e inicia la descarga. Necesitas unos 212 GB libres en PS5 y 234 GB en Xbox Series X|S. Deja la consola en reposo para que termine durante la noche.</p>
<h2>Cuándo empezó</h2><ul><li><strong>PS5:</strong> desde la medianoche local del 10 de noviembre de 2026.</li><li><strong>Xbox Series X|S:</strong> desde las 12 a. m. GMT del 10 de noviembre de 2026, al mismo tiempo en todo el mundo.</li></ul>
<h2>Espacio necesario</h2><p>Rockstar indica que la precarga necesita <strong>hasta 212 GB</strong> libres, según la consola. Deja un poco más de espacio, porque la instalación necesita margen para descomprimir.</p>
<h2>Paso a paso</h2><ol><li>Reserva la edición digital en PlayStation Store o en Microsoft Store, si aún no lo hiciste.</li><li>Abre la página del juego en tu biblioteca e inicia la descarga.</li><li>Deja la consola en modo reposo con las descargas activas para que termine durante la noche.</li><li>El día del lanzamiento, conéctate una vez para que el juego se desbloquee.</li></ol>
<h2>¿Compraste la edición física?</h2><p>La edición en caja trae un código de descarga en lugar de un disco. Canjea el código en la tienda de tu consola y la precarga empieza igual.</p>""",
   'pt': """<p><strong>Resposta rápida:</strong> Abra a página do jogo na biblioteca da PlayStation Store ou Microsoft Store e inicie o download. Você precisa de cerca de 212 GB livres no PS5 e 234 GB no Xbox Series X|S. Deixe o console em repouso para terminar durante a noite.</p>
<h2>Quando começou</h2><ul><li><strong>PS5:</strong> a partir da meia-noite no horário local de 10 de novembro de 2026.</li><li><strong>Xbox Series X|S:</strong> a partir de 0h GMT de 10 de novembro de 2026, no mesmo momento no mundo todo.</li></ul>
<h2>Espaço necessário</h2><p>A Rockstar informa que o pre-load precisa de <strong>até 212 GB</strong> livres, dependendo do console. Deixe um pouco mais de espaço, porque a instalação precisa de folga para descompactar.</p>
<h2>Passo a passo</h2><ol><li>Faça a pré-venda da edição digital na PlayStation Store ou na Microsoft Store, se ainda não fez.</li><li>Abra a página do jogo na sua biblioteca e inicie o download.</li><li>Deixe o console em modo de repouso com os downloads ligados, para terminar durante a noite.</li><li>No dia do lançamento, conecte-se uma vez para o jogo liberar.</li></ol>
<h2>Comprou a edição física?</h2><p>A edição em caixa vem com um código de download em vez de disco. Resgate o código na loja do console e o pre-load começa do mesmo jeito.</p>"""}},
 {'slug': 'trailers', 'cat': 'start', 'mins': 2, 'src': ['wikily'], 'videos': ['QdBZY2fkU-0', 'VQRLujxTm3c', 'tJbzMqJGH4k', 'rz1B4B2yBZY'],
  'title': {'en': 'Every official GTA 6 trailer, in order', 'es': 'Todos los tráilers oficiales de GTA 6, en orden', 'pt': 'Todos os trailers oficiais de GTA 6, em ordem'},
  'lede': {'en': 'Four official videos from Rockstar, from the first reveal to the launch trailer. Watch them all right here.',
           'es': 'Cuatro videos oficiales de Rockstar, del primer anuncio al tráiler de lanzamiento. Míralos todos aquí.',
           'pt': 'Quatro vídeos oficiais da Rockstar, do primeiro anúncio ao trailer de lançamento. Assista a todos aqui mesmo.'},
  'body': {
   'en': """<ol class="tl"><li><strong>Trailer 1</strong> &middot; December 4, 2023. The first look at Lucia, Jason and Vice City.</li><li><strong>Trailer 2</strong> &middot; May 6, 2025. More of Jason and Lucia's story and a wider look at Leonida.</li><li><strong>An Extended Look</strong> &middot; August 27, 2026. About 26 minutes of in-game footage, the longest look at the game before launch.</li><li><strong>Launch Trailer</strong> &middot; October 2026. The final trailer before release on November 19.</li></ol>
<p>Rockstar has released no Trailer 3; the extended look and the launch trailer came instead.</p>""",
   'es': """<ol class="tl"><li><strong>Tráiler 1</strong> &middot; 4 de diciembre de 2023. El primer vistazo a Lucia, Jason y Vice City.</li><li><strong>Tráiler 2</strong> &middot; 6 de mayo de 2025. Más de la historia de Jason y Lucia y una mirada más amplia a Leonida.</li><li><strong>An Extended Look</strong> &middot; 27 de agosto de 2026. Unos 26 minutos de imágenes del juego, la mirada más larga antes del lanzamiento.</li><li><strong>Tráiler de lanzamiento</strong> &middot; octubre de 2026. El último tráiler antes del estreno el 19 de noviembre.</li></ol>
<p>Rockstar no ha publicado un Tráiler 3; en su lugar llegaron el vistazo extendido y el tráiler de lanzamiento.</p>""",
   'pt': """<ol class="tl"><li><strong>Trailer 1</strong> &middot; 4 de dezembro de 2023. O primeiro olhar sobre Lucia, Jason e Vice City.</li><li><strong>Trailer 2</strong> &middot; 6 de maio de 2025. Mais da história de Jason e Lucia e uma visão maior de Leonida.</li><li><strong>An Extended Look</strong> &middot; 27 de agosto de 2026. Cerca de 26 minutos de imagens do jogo, a maior amostra antes do lançamento.</li><li><strong>Trailer de lançamento</strong> &middot; outubro de 2026. O último trailer antes da estreia em 19 de novembro.</li></ol>
<p>A Rockstar não lançou um Trailer 3; no lugar dele vieram o vídeo estendido e o trailer de lançamento.</p>"""}},
 {'slug': 'leonida-regions', 'cat': 'start', 'mins': 3, 'src': ['gfinity'],
  'title': {'en': "Leonida's six confirmed regions, explained", 'es': 'Las seis regiones confirmadas de Leonida, explicadas', 'pt': 'As seis regiões confirmadas de Leonida, explicadas'},
  'lede': {'en': 'Rockstar has named six places in its Florida-inspired state. Here is what each one is like.',
           'es': 'Rockstar ha nombrado seis lugares de su estado inspirado en Florida. Así es cada uno.',
           'pt': 'A Rockstar já nomeou seis lugares do seu estado inspirado na Flórida. Veja como é cada um.'},
  'body': {
   'en': """<h2>Vice City</h2><p>The state's sun and fun capital: white-sand beaches, pastel art deco, busy neighborhoods and street markets.</p>
<h2>Leonida Keys</h2><p>A chain of tropical islands with a laid-back mood and lively bars. The water is beautiful, and not always safe.</p>
<h2>Grassrivers</h2><p>Wetlands that recall the Everglades, with alligators and flamingos, and stranger things deeper in the mangroves.</p>
<h2>Port Gellhorn</h2><p>Leonida's forgotten coast: cheap motels, closed attractions and empty strip malls in a town that has seen better days.</p>
<h2>Ambrosia</h2><p>An industrial area built around a big sugar refinery, the town's main employer, with a local biker gang close by.</p>
<h2>Mount Kalaga</h2><p>A national park on the northern border, known for hunting, fishing and off-road trails, and for the loners who live in its backwoods.</p>
<p>See where they sit on <a href="#map">our map of Leonida</a>.</p>""",
   'es': """<h2>Vice City</h2><p>La capital del sol y la diversión: playas de arena blanca, art déco en tonos pastel, barrios llenos de vida y mercados callejeros.</p>
<h2>Leonida Keys</h2><p>Una cadena de islas tropicales con ambiente relajado y bares animados. El agua es preciosa, y no siempre segura.</p>
<h2>Grassrivers</h2><p>Humedales que recuerdan a los Everglades, con caimanes y flamencos, y cosas más extrañas en lo profundo de los manglares.</p>
<h2>Port Gellhorn</h2><p>La costa olvidada de Leonida: moteles baratos, atracciones cerradas y centros comerciales vacíos en un pueblo que vivió tiempos mejores.</p>
<h2>Ambrosia</h2><p>Una zona industrial construida alrededor de una gran refinería de azúcar, el principal empleador del lugar, con una banda de motociclistas cerca.</p>
<h2>Mount Kalaga</h2><p>Un parque nacional en la frontera norte, conocido por la caza, la pesca y las rutas todoterreno, y por los solitarios que viven en sus bosques.</p>
<p>Mira dónde está cada una en <a href="#map">nuestro mapa de Leonida</a>.</p>""",
   'pt': """<h2>Vice City</h2><p>A capital do sol e da diversão: praias de areia branca, art déco em tons pastel, bairros agitados e feiras de rua.</p>
<h2>Leonida Keys</h2><p>Uma cadeia de ilhas tropicais com clima tranquilo e bares animados. A água é linda, e nem sempre segura.</p>
<h2>Grassrivers</h2><p>Áreas alagadas que lembram os Everglades, com jacarés e flamingos, e coisas mais estranhas no fundo dos manguezais.</p>
<h2>Port Gellhorn</h2><p>A costa esquecida de Leonida: motéis baratos, atrações fechadas e centros comerciais vazios numa cidade que já viu dias melhores.</p>
<h2>Ambrosia</h2><p>Uma área industrial em volta de uma grande refinaria de açúcar, a principal empregadora da região, com uma gangue de motoqueiros por perto.</p>
<h2>Mount Kalaga</h2><p>Um parque nacional na fronteira norte, conhecido por caça, pesca e trilhas off-road, e pelos solitários que vivem nas suas matas.</p>
<p>Veja onde fica cada uma no <a href="#map">nosso mapa de Leonida</a>.</p>"""}},
]

PAGESX = {
 'about': {'title': {'en': 'About Five Star Daily', 'es': 'Sobre Five Star Daily', 'pt': 'Sobre o Five Star Daily'},
  'body': {
   'en': """<p>Five Star Daily is an independent fan site about Grand Theft Auto VI, made by fans for players in English, Spanish and Portuguese.</p>
<h2>What you will find here</h2><ul><li>Live streams and new videos from creators, gathered in one place and playable right on the page.</li><li>Daily news, with short summaries we write ourselves and a link to every original source.</li><li>Guides written by our team, updated as the game changes.</li><li>An interactive map of Leonida and a 100% checklist that saves your progress on your own device.</li></ul>
<h2>How we work</h2><p>We write our own text and never copy articles. When we report news, we name the source and link to it. If you spot a mistake, write to us and we will fix it.</p>
<h2>Not official</h2><p>Five Star Daily is not affiliated with, endorsed or sponsored by Rockstar Games or Take-Two Interactive. Grand Theft Auto and related names are trademarks of their owners. Videos belong to their creators and play through YouTube.</p>""",
   'es': """<p>Five Star Daily es un sitio independiente de fans sobre Grand Theft Auto VI, hecho por fans para jugadores en inglés, español y portugués.</p>
<h2>Qué encontrarás aquí</h2><ul><li>Transmisiones en vivo y videos nuevos de creadores, reunidos en un solo lugar y reproducibles en la propia página.</li><li>Noticias diarias, con resúmenes breves escritos por nosotros y un enlace a cada fuente original.</li><li>Guías escritas por nuestro equipo, actualizadas a medida que cambia el juego.</li><li>Un mapa interactivo de Leonida y un checklist 100% que guarda tu progreso en tu propio dispositivo.</li></ul>
<h2>Cómo trabajamos</h2><p>Escribimos nuestros propios textos y nunca copiamos artículos. Cuando informamos una noticia, nombramos la fuente y la enlazamos. Si ves un error, escríbenos y lo corregimos.</p>
<h2>No oficial</h2><p>Five Star Daily no está afiliado, respaldado ni patrocinado por Rockstar Games ni Take-Two Interactive. Grand Theft Auto y los nombres relacionados son marcas de sus dueños. Los videos pertenecen a sus creadores y se reproducen a través de YouTube.</p>""",
   'pt': """<p>O Five Star Daily é um site independente de fãs sobre Grand Theft Auto VI, feito por fãs para jogadores em inglês, espanhol e português.</p>
<h2>O que você encontra aqui</h2><ul><li>Lives e vídeos novos de criadores, reunidos num só lugar e tocando na própria página.</li><li>Notícias diárias, com resumos curtos escritos por nós e o link para cada fonte original.</li><li>Guias escritos pela nossa equipe, atualizados conforme o jogo muda.</li><li>Um mapa interativo de Leonida e um checklist 100% que salva o seu progresso no seu próprio aparelho.</li></ul>
<h2>Como trabalhamos</h2><p>Escrevemos nossos próprios textos e nunca copiamos matérias. Quando damos uma notícia, citamos a fonte e colocamos o link. Se encontrar um erro, escreva para nós que a gente corrige.</p>
<h2>Não oficial</h2><p>O Five Star Daily não tem ligação, aprovação nem patrocínio da Rockstar Games ou da Take-Two Interactive. Grand Theft Auto e os nomes relacionados são marcas dos seus donos. Os vídeos pertencem aos seus criadores e tocam pelo YouTube.</p>"""}},
 'contact': {'title': {'en': 'Contact', 'es': 'Contacto', 'pt': 'Contato'},
  'body': {
   'en': f"""<p>Questions, corrections, partnership ideas or a video you think we should feature? Email us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p><p>We read every message and usually reply within two business days.</p><p>If you are a creator and want your video removed from the site, send us the link and we will take it down.</p>""",
   'es': f"""<p>¿Preguntas, correcciones, ideas de colaboración o un video que deberíamos destacar? Escríbenos a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p><p>Leemos todos los mensajes y solemos responder en dos días hábiles.</p><p>Si eres creador y quieres que quitemos tu video del sitio, envíanos el enlace y lo retiramos.</p>""",
   'pt': f"""<p>Dúvidas, correções, ideias de parceria ou um vídeo que a gente deveria destacar? Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a>.</p><p>Lemos todas as mensagens e costumamos responder em até dois dias úteis.</p><p>Se você é criador e quer que o seu vídeo saia do site, mande o link que a gente retira.</p>"""}},
 'privacy': {'title': {'en': 'Privacy policy', 'es': 'Política de privacidad', 'pt': 'Política de privacidade'},
  'body': {
   'en': f"""<p class="upd">Last updated: November 13, 2026</p>
<p>This policy explains what information Five Star Daily (fivestardaily.com) collects and how it is used.</p>
<h2>Information you give us</h2><p>We do not ask you to create an account. If you email us, we use your address and message only to reply.</p>
<h2>Information stored on your device</h2><p>Your language, time-of-day setting, cursor choice and checklist progress are saved in your own browser's local storage. They never leave your device and you can clear them at any time in your browser settings.</p>
<h2>Advertising</h2><p>We use Google AdSense to show ads. Google and its partners use cookies to serve ads based on your visits to this and other sites. You can turn off personalized advertising in <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a>, and learn more in <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">how Google uses information from sites that use its services</a>. Visitors in the European Economic Area, the UK and Switzerland are asked for consent before personalized ads are shown.</p>
<h2>Analytics</h2><p>We use Google Analytics to count visits and see which pages are popular. It uses cookies and collects information such as pages viewed, device type and approximate location. It does not tell us who you are. You can opt out with the <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">Google Analytics opt-out add-on</a>.</p>
<h2>Videos</h2><p>Videos play through YouTube's privacy-enhanced mode. YouTube does not set cookies until you press play; after that, YouTube's own privacy policy applies.</p>
<h2>Other services</h2><p>Fonts load from Google Fonts. Our hosting provider keeps standard server logs, such as IP address and browser type, for security.</p>
<h2>Children</h2><p>This site is about a game rated for mature audiences and is not directed at children under 13. We do not knowingly collect information from them.</p>
<h2>Your rights</h2><p>Depending on where you live, you may have the right to access or delete data about you. Email <a href="mailto:{EMAIL}">{EMAIL}</a> and we will help.</p>
<h2>Changes</h2><p>If we change this policy, we will update the date at the top of this page.</p>""",
   'es': f"""<p class="upd">Última actualización: 13 de noviembre de 2026</p>
<p>Esta política explica qué información recopila Five Star Daily (fivestardaily.com) y cómo se usa.</p>
<h2>Información que nos das</h2><p>No pedimos crear una cuenta. Si nos escribes por correo, usamos tu dirección y tu mensaje solo para responderte.</p>
<h2>Información guardada en tu dispositivo</h2><p>Tu idioma, el ajuste de hora del día, el cursor elegido y el progreso del checklist se guardan en el almacenamiento local de tu propio navegador. Nunca salen de tu dispositivo y puedes borrarlos cuando quieras en la configuración del navegador.</p>
<h2>Publicidad</h2><p>Usamos Google AdSense para mostrar anuncios. Google y sus socios usan cookies para mostrar anuncios según tus visitas a este y otros sitios. Puedes desactivar la publicidad personalizada en la <a href="https://adssettings.google.com" target="_blank" rel="noopener">configuración de anuncios de Google</a> y saber más sobre <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">cómo usa Google la información de los sitios que usan sus servicios</a>. A los visitantes del Espacio Económico Europeo, el Reino Unido y Suiza se les pide consentimiento antes de mostrar anuncios personalizados.</p>
<h2>Analítica</h2><p>Usamos Google Analytics para contar visitas y ver qué páginas son populares. Usa cookies y recoge datos como las páginas vistas, el tipo de dispositivo y la ubicación aproximada. No nos dice quién eres. Puedes desactivarlo con el <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">complemento de inhabilitación de Google Analytics</a>.</p>
<h2>Videos</h2><p>Los videos se reproducen con el modo de privacidad mejorada de YouTube. YouTube no instala cookies hasta que pulsas reproducir; desde ese momento se aplica la política de privacidad de YouTube.</p>
<h2>Otros servicios</h2><p>Las fuentes se cargan desde Google Fonts. Nuestro proveedor de alojamiento guarda registros estándar del servidor, como la dirección IP y el tipo de navegador, por seguridad.</p>
<h2>Menores</h2><p>Este sitio trata de un juego clasificado para público adulto y no está dirigido a menores de 13 años. No recopilamos a sabiendas información de ellos.</p>
<h2>Tus derechos</h2><p>Según dónde vivas, puedes tener derecho a acceder a tus datos o pedir que se borren. Escribe a <a href="mailto:{EMAIL}">{EMAIL}</a> y te ayudamos.</p>
<h2>Cambios</h2><p>Si cambiamos esta política, actualizaremos la fecha al inicio de esta página.</p>""",
   'pt': f"""<p class="upd">Última atualização: 13 de novembro de 2026</p>
<p>Esta política explica quais informações o Five Star Daily (fivestardaily.com) coleta e como elas são usadas.</p>
<h2>Informações que você nos dá</h2><p>Não pedimos para criar conta. Se você nos mandar um e-mail, usamos o seu endereço e a sua mensagem só para responder.</p>
<h2>Informações salvas no seu aparelho</h2><p>O seu idioma, a configuração de hora do dia, o cursor escolhido e o progresso do checklist ficam salvos no armazenamento local do seu próprio navegador. Eles nunca saem do seu aparelho e você pode apagá-los quando quiser nas configurações do navegador.</p>
<h2>Publicidade</h2><p>Usamos o Google AdSense para exibir anúncios. O Google e seus parceiros usam cookies para mostrar anúncios com base nas suas visitas a este e a outros sites. Você pode desativar a publicidade personalizada nas <a href="https://adssettings.google.com" target="_blank" rel="noopener">configurações de anúncios do Google</a> e saber mais sobre <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">como o Google usa informações de sites que usam seus serviços</a>. Visitantes do Espaço Econômico Europeu, do Reino Unido e da Suíça recebem um pedido de consentimento antes de verem anúncios personalizados.</p>
<h2>Análise de audiência</h2><p>Usamos o Google Analytics para contar visitas e ver quais páginas são mais vistas. Ele usa cookies e coleta dados como páginas vistas, tipo de aparelho e localização aproximada. Ele não nos diz quem você é. Você pode desativar com o <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">complemento de desativação do Google Analytics</a>.</p>
<h2>Vídeos</h2><p>Os vídeos tocam pelo modo de privacidade aprimorada do YouTube. O YouTube não grava cookies até você apertar o play; a partir daí vale a política de privacidade do próprio YouTube.</p>
<h2>Outros serviços</h2><p>As fontes carregam do Google Fonts. O nosso provedor de hospedagem guarda registros padrão do servidor, como endereço IP e tipo de navegador, por segurança.</p>
<h2>Crianças</h2><p>Este site trata de um jogo classificado para público adulto e não é voltado a menores de 13 anos. Não coletamos intencionalmente informações deles.</p>
<h2>Seus direitos</h2><p>Dependendo de onde você mora, pode ter o direito de acessar ou pedir a exclusão dos seus dados. Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a> que a gente ajuda.</p>
<h2>Mudanças</h2><p>Se mudarmos esta política, atualizamos a data no topo desta página.</p>"""}},
 'terms': {'title': {'en': 'Terms of use', 'es': 'Términos de uso', 'pt': 'Termos de uso'},
  'body': {
   'en': f"""<p class="upd">Last updated: November 13, 2026</p>
<p>By using Five Star Daily you agree to these terms.</p>
<h2>Fan site</h2><p>Five Star Daily is an unofficial fan site. It is not affiliated with Rockstar Games or Take-Two Interactive. All game names, logos and images belong to their owners.</p>
<h2>Our content</h2><p>Guides, summaries and other text written by Five Star Daily are ours. You may quote short parts with a link back to the page.</p>
<h2>Third-party content</h2><p>Videos, streams and linked articles belong to their creators and publishers. We show videos through YouTube's player and link news to its original source. We are not responsible for content on other sites.</p>
<h2>No guarantees</h2><p>We work to keep information accurate, but games change and mistakes happen. The site is provided as is, without warranties.</p>
<h2>Removal requests</h2><p>If you own content shown here and want it removed, email <a href="mailto:{EMAIL}">{EMAIL}</a> with the link.</p>
<h2>Changes</h2><p>We may update these terms. The date at the top shows the latest version.</p>""",
   'es': f"""<p class="upd">Última actualización: 13 de noviembre de 2026</p>
<p>Al usar Five Star Daily aceptas estos términos.</p>
<h2>Sitio de fans</h2><p>Five Star Daily es un sitio de fans no oficial. No está afiliado a Rockstar Games ni a Take-Two Interactive. Todos los nombres, logotipos e imágenes del juego pertenecen a sus dueños.</p>
<h2>Nuestro contenido</h2><p>Las guías, los resúmenes y demás textos escritos por Five Star Daily son nuestros. Puedes citar fragmentos breves con un enlace a la página.</p>
<h2>Contenido de terceros</h2><p>Los videos, las transmisiones y los artículos enlazados pertenecen a sus creadores y medios. Mostramos los videos con el reproductor de YouTube y enlazamos cada noticia a su fuente original. No somos responsables del contenido de otros sitios.</p>
<h2>Sin garantías</h2><p>Trabajamos para que la información sea correcta, pero los juegos cambian y los errores pasan. El sitio se ofrece tal cual, sin garantías.</p>
<h2>Solicitudes de retiro</h2><p>Si eres dueño de un contenido que aparece aquí y quieres que lo quitemos, escribe a <a href="mailto:{EMAIL}">{EMAIL}</a> con el enlace.</p>
<h2>Cambios</h2><p>Podemos actualizar estos términos. La fecha al inicio indica la versión más reciente.</p>""",
   'pt': f"""<p class="upd">Última atualização: 13 de novembro de 2026</p>
<p>Ao usar o Five Star Daily você concorda com estes termos.</p>
<h2>Site de fã</h2><p>O Five Star Daily é um site de fã não oficial. Não tem ligação com a Rockstar Games nem com a Take-Two Interactive. Todos os nomes, logotipos e imagens do jogo pertencem aos seus donos.</p>
<h2>Nosso conteúdo</h2><p>Os guias, os resumos e os demais textos escritos pelo Five Star Daily são nossos. Você pode citar trechos curtos com um link para a página.</p>
<h2>Conteúdo de terceiros</h2><p>Vídeos, lives e matérias com link pertencem aos seus criadores e veículos. Mostramos os vídeos pelo player do YouTube e linkamos cada notícia à fonte original. Não respondemos pelo conteúdo de outros sites.</p>
<h2>Sem garantias</h2><p>Trabalhamos para manter as informações corretas, mas jogos mudam e erros acontecem. O site é oferecido como está, sem garantias.</p>
<h2>Pedidos de remoção</h2><p>Se você é dono de um conteúdo exibido aqui e quer que ele saia, escreva para <a href="mailto:{EMAIL}">{EMAIL}</a> com o link.</p>
<h2>Mudanças</h2><p>Podemos atualizar estes termos. A data no topo mostra a versão mais recente.</p>"""}},
}
import sys, os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
_N = json.load(open(os.path.join(HERE, 'news.json')))
S.update(_N['S']); NEWS = sorted(_N['NEWS'], key=lambda n: n['date'], reverse=True)
from guides2 import S2, G2
S.update(S2); GUIDES = GUIDES + G2
from guides3 import S3, G3
S.update(S3); GUIDES = GUIDES + G3
from guides4 import S4, G4
S.update(S4); GUIDES = GUIDES + G4
json.dump({'S': S, 'GUIDES': GUIDES, 'NEWS': NEWS, 'PAGES': PAGESX, 'EMAIL': EMAIL}, open(os.path.join(HERE, 'content.json'), 'w'), ensure_ascii=False)
print('ok')
