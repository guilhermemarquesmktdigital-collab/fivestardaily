"""Third batch of original guides: soundtrack and editions. Facts only from the cited sources."""

S3 = {
 'nw_album': ['netzwelt: GTA 6 soundtrack available to pre-order, six songs out now', 'https://www.netzwelt.de/news/258672-gta-6soundtrack-vorbestellbar-rockstar-ueberrascht-fans-gratis-hoerprobe-spotify.html'],
 'gem_album': ['Gematsu: Grand Theft Auto VI: The Album announced', 'https://www.gematsu.com/2026/09/grand-theft-auto-vi-the-album-announced'],
 'pcg_songs': ['PC Gamer: Every GTA 6 song confirmed so far', 'https://www.pcgamer.com/games/grand-theft-auto/gta-6-radio-songs/'],
 'rs_music': ['Rockstar Games: The Music of Grand Theft Auto VI', 'https://www.rockstargames.com/VI/music'],
 'gd_price': ['Game Developer: Grand Theft Auto 6\'s $80 price settles the $100 question', 'https://www.gamedeveloper.com/console/grand-theft-auto-6-s-80-price-settles-the-100-question'],
 'dx_ultimate': ['Dexerto: Take-Two boss says the $100 Ultimate Edition is outselling the $80 Standard', 'https://www.dexerto.com/gta/rockstar-games-boss-says-100-gta-6-ultimate-edition-is-outselling-the-80-standard-version-3397246/'],
 'abc_launch': ['ABC News: Grand Theft Auto 6 is out this week, everything you need to know', 'https://www.abc.net.au/news/2026-11-17/grand-theft-auto-6-gta6-explainer/107384556'],
}

G3 = []
def g(slug, mins, src, title, lede, body, **kw):
    d = {'slug': slug, 'cat': 'game', 'mins': mins, 'src': src, 'title': title, 'lede': lede, 'body': body}
    d.update(kw); G3.append(d)

_SONGS = [('That’s It', 'Yung Lean feat. Future & Metro Boomin'), ('RHYNO', 'Travis Scott (prod. Guy-Manuel de Homem-Christo)'),
 ('Sexy Magic', 'CA7RIEL & Paco Amoroso, PinkPantheress, Fred again.. & Etienne de Crécy'), ('Last Thing You Need', 'Morgan Wallen'),
 ('Suzuki', 'Fuerza Regida'), ('Macacoa 2000', 'Rauw Alejandro'), ('Don’t Chart', 'Cardi B'), ('Blood In Your Eyes', 'Tove Lo'),
 ('Bright Lights, Big City', 'Keith Richards'), ('Flower in a Hurricane', 'Justice feat. Tame Impala, SZA, King Gizzard & the Lizard Wizard'),
 ('Pusher', 'Justice feat. Gesaffelstein')]
_UL = '<ul>' + ''.join('<li><strong>%s</strong> · %s</li>' % s for s in _SONGS) + '</ul>'

g('soundtrack', 4, ['nw_album', 'gem_album', 'pcg_songs', 'rs_music'],
 {'en': 'GTA 6 soundtrack: every official song released so far',
  'es': 'Banda sonora de GTA 6: todas las canciones oficiales publicadas hasta ahora',
  'pt': 'Trilha sonora de GTA 6: todas as músicas oficiais lançadas até agora'},
 {'en': 'GTA VI: The Album drops with the game. Here are the songs you can already hear, where they come from, and how to play them on this site.',
  'es': 'GTA VI: The Album sale junto con el juego. Estas son las canciones que ya puedes escuchar, de dónde vienen y cómo oírlas en este sitio.',
  'pt': 'GTA VI: The Album sai junto com o jogo. Veja as músicas que já dá para ouvir, de onde elas vêm e como tocá-las aqui no site.'},
 {'en': """<h2>The album</h2><p><strong>Grand Theft Auto VI: The Album</strong> is Rockstar's companion record for the game, made with Atlantic Records. It releases on <strong>November 19</strong>, the same day as the game, with <strong>34 tracks</strong>, and it was announced in September with physical CD and vinyl versions available to pre-order.</p>
<h2>Songs already out</h2><p>These tracks were released early as official uploads, labelled as coming from the album or from the game:</p>""" + _UL + """
<p>The last two are from Justice, who are tagged on the uploads as part of the GTA VI music. The rest come from the album itself.</p>
<h2>The songs from the trailers</h2><p>Before any of this, the trailers already set the mood with older hits: Trailer 1 used Tom Petty's <strong>Love Is a Long Road</strong> and Trailer 2 used The Pointer Sisters' <strong>Hot Together</strong>. They are trailer songs, so do not assume they are on the album or on a station until Rockstar lists them.</p>
<h2>The radio in the game</h2><p>Rockstar's official music page for GTA VI previews the in-game radio, but the full station list and every song on it only becomes clear once people are playing. We will update this guide after launch.</p>
<h2>Listen here</h2><p>Tap the <strong>♪ Soundtrack</strong> button at the bottom right of any page. It plays these official uploads through YouTube's own player, so the artists and labels keep their streams, and the music keeps going while you browse the site.</p>""",
  'es': """<h2>El álbum</h2><p><strong>Grand Theft Auto VI: The Album</strong> es el disco que acompaña al juego, hecho por Rockstar con Atlantic Records. Sale el <strong>19 de noviembre</strong>, el mismo día que el juego, con <strong>34 canciones</strong>. Se anunció en septiembre, con versiones en CD y vinilo en preventa.</p>
<h2>Canciones ya publicadas</h2><p>Estas canciones salieron antes como publicaciones oficiales, marcadas como parte del álbum o del juego:</p>""" + _UL + """
<p>Las dos últimas son de Justice, que aparecen marcadas como parte de la música de GTA VI. El resto viene del propio álbum.</p>
<h2>Las canciones de los tráilers</h2><p>Antes de todo esto, los tráilers ya marcaron el tono con clásicos: el Tráiler 1 usó <strong>Love Is a Long Road</strong> de Tom Petty y el Tráiler 2, <strong>Hot Together</strong> de The Pointer Sisters. Son canciones de tráiler: no des por hecho que estén en el álbum o en una radio hasta que Rockstar lo confirme.</p>
<h2>La radio del juego</h2><p>La página oficial de música de GTA VI adelanta la radio del juego, pero la lista completa de emisoras y canciones solo se conocerá cuando la gente esté jugando. Actualizaremos esta guía después del lanzamiento.</p>
<h2>Escúchalas aquí</h2><p>Toca el botón <strong>♪ Banda sonora</strong> abajo a la derecha de cualquier página. Reproduce estas publicaciones oficiales con el propio reproductor de YouTube, así los artistas y sellos conservan sus reproducciones, y la música sigue mientras navegas.</p>""",
  'pt': """<h2>O álbum</h2><p><strong>Grand Theft Auto VI: The Album</strong> é o disco que acompanha o jogo, feito pela Rockstar com a Atlantic Records. Ele sai em <strong>19 de novembro</strong>, no mesmo dia do jogo, com <strong>34 faixas</strong>. Foi anunciado em setembro, com versões em CD e vinil em pré-venda.</p>
<h2>Músicas já lançadas</h2><p>Estas faixas saíram antes como publicações oficiais, identificadas como parte do álbum ou do jogo:</p>""" + _UL + """
<p>As duas últimas são do Justice, marcadas como parte da música de GTA VI. As demais vêm do próprio álbum.</p>
<h2>As músicas dos trailers</h2><p>Antes disso, os trailers já tinham dado o clima com sucessos antigos: o Trailer 1 usou <strong>Love Is a Long Road</strong>, de Tom Petty, e o Trailer 2, <strong>Hot Together</strong>, das Pointer Sisters. São músicas de trailer: não conte que estejam no álbum ou numa rádio até a Rockstar confirmar.</p>
<h2>A rádio do jogo</h2><p>A página oficial de música de GTA VI mostra uma prévia da rádio do jogo, mas a lista completa de estações e músicas só vai ficar clara quando o pessoal estiver jogando. Vamos atualizar este guia depois do lançamento.</p>
<h2>Ouça aqui</h2><p>Toque no botão <strong>♪ Trilha sonora</strong> no canto inferior direito de qualquer página. Ele toca essas publicações oficiais pelo próprio player do YouTube, então artistas e gravadoras ficam com as reproduções, e a música continua enquanto você navega.</p>"""})

g('editions', 3, ['gd_price', 'dx_ultimate', 'abc_launch'],
 {'en': 'GTA 6 Standard vs Ultimate Edition: price, bonuses and which to buy',
  'es': 'GTA 6 Standard vs Ultimate Edition: precio, extras y cuál comprar',
  'pt': 'GTA 6 Standard ou Ultimate Edition: preço, bônus e qual comprar'},
 {'en': 'Two editions, a box with no disc and a pre-order bonus with a deadline. Everything confirmed about buying GTA 6, in one page.',
  'es': 'Dos ediciones, una caja sin disco y un extra de reserva con fecha límite. Todo lo confirmado sobre comprar GTA 6, en una página.',
  'pt': 'Duas edições, uma caixa sem disco e um bônus de pré-venda com prazo. Tudo o que foi confirmado sobre comprar GTA 6, numa página.'},
 {'en': """<h2>The two editions</h2><ul><li><strong>Standard Edition: $79.99.</strong> The full game.</li><li><strong>Ultimate Edition: $99.99.</strong> The game plus premium vehicles, weapons, apparel and more.</li></ul><p>Rockstar announced both prices in June, and pre-orders opened the next day. The game launches on <strong>November 19, 2026</strong> on PS5 and Xbox Series X|S.</p>
<h2>The pre-order bonus</h2><p>Standard Edition pre-orders placed <strong>before November 20</strong> include the <strong>Vintage Vice City Pack</strong>. If you want it, order before launch day ends.</p>
<h2>The box has no disc</h2><p>Physical copies sold in stores contain a <strong>download code</strong>, not a disc. You redeem the code and download the game like a digital copy, so the box does not save you the download.</p>
<h2>Make room first</h2><p>The install is large: about <strong>212 GB on PS5</strong> and about <strong>234 GB on Xbox Series X|S</strong>. Check your free space before launch night, or the download will stop halfway.</p>
<h2>Which one should you buy?</h2><p>The extras in the Ultimate Edition are cosmetic and convenience items: they do not unlock story content. If you only care about the story and the world, the Standard Edition gets you the whole game. Take-Two CEO Strauss Zelnick said in August that pre-orders were leaning toward the Ultimate Edition, possibly because the most avid fans pre-order first, and he indicated there were no plans for a holiday discount.</p>""",
  'es': """<h2>Las dos ediciones</h2><ul><li><strong>Standard Edition: 79,99 USD.</strong> El juego completo.</li><li><strong>Ultimate Edition: 99,99 USD.</strong> El juego más vehículos, armas, ropa y otros extras premium.</li></ul><p>Rockstar anunció los dos precios en junio y la preventa abrió al día siguiente. El juego sale el <strong>19 de noviembre de 2026</strong> en PS5 y Xbox Series X|S.</p>
<h2>El extra de reserva</h2><p>Las reservas de la Standard Edition hechas <strong>antes del 20 de noviembre</strong> incluyen el <strong>Vintage Vice City Pack</strong>. Si lo quieres, compra antes de que termine el día del lanzamiento.</p>
<h2>La caja no trae disco</h2><p>Las copias físicas de las tiendas traen un <strong>código de descarga</strong>, no un disco. Canjeas el código y descargas el juego como si fuera digital, así que la caja no te ahorra la descarga.</p>
<h2>Haz espacio antes</h2><p>La instalación es enorme: unos <strong>212 GB en PS5</strong> y unos <strong>234 GB en Xbox Series X|S</strong>. Revisa el espacio libre antes de la noche del lanzamiento o la descarga se detendrá a mitad.</p>
<h2>¿Cuál comprar?</h2><p>Los extras de la Ultimate Edition son cosméticos y de conveniencia: no desbloquean historia. Si solo te importan la historia y el mundo, la Standard Edition te da el juego entero. El CEO de Take-Two, Strauss Zelnick, dijo en agosto que las reservas se inclinaban hacia la Ultimate Edition, quizá porque los fans más entusiastas reservan primero, e indicó que no había planes de descuento en las fiestas.</p>""",
  'pt': """<h2>As duas edições</h2><ul><li><strong>Standard Edition: US$ 79,99.</strong> O jogo completo.</li><li><strong>Ultimate Edition: US$ 99,99.</strong> O jogo mais veículos, armas, roupas e outros extras premium.</li></ul><p>A Rockstar anunciou os dois preços em junho, e a pré-venda abriu no dia seguinte. O jogo sai em <strong>19 de novembro de 2026</strong> no PS5 e no Xbox Series X|S.</p>
<h2>O bônus de pré-venda</h2><p>As pré-vendas da Standard Edition feitas <strong>antes de 20 de novembro</strong> incluem o <strong>Vintage Vice City Pack</strong>. Se você quer, compre antes de acabar o dia do lançamento.</p>
<h2>A caixa não tem disco</h2><p>As cópias físicas vendidas nas lojas trazem um <strong>código de download</strong>, não um disco. Você resgata o código e baixa o jogo como se fosse digital, então a caixa não economiza o download.</p>
<h2>Abra espaço antes</h2><p>A instalação é enorme: cerca de <strong>212 GB no PS5</strong> e cerca de <strong>234 GB no Xbox Series X|S</strong>. Confira o espaço livre antes da noite do lançamento, ou o download vai parar no meio.</p>
<h2>Qual comprar?</h2><p>Os extras da Ultimate Edition são cosméticos e de conveniência: não liberam conteúdo de história. Se o que importa para você é a história e o mundo, a Standard Edition entrega o jogo inteiro. O CEO da Take-Two, Strauss Zelnick, disse em agosto que as pré-vendas estavam pendendo para a Ultimate Edition, talvez porque os fãs mais dedicados compram primeiro, e indicou que não havia planos de desconto no fim de ano.</p>"""})
