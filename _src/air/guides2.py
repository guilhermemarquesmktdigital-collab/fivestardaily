"""Second batch of original guides: gameplay, characters, police, combat, activities, callbacks, timeline.
Facts limited to what Rockstar has shown or said (trailers, official site, the Netflix Extended Look, interviews)."""

S2 = {
 'vgc_netflix': ['VGC: Everything shown at the Grand Theft Auto 6 Netflix special', 'https://videogameschronicle.com/news/everything-shown-at-the-grand-theft-auto-6-netflix-special'],
 'kotaku_look': ['Kotaku: Cool details spotted in the 26-minute GTA 6 gameplay reveal', 'https://kotaku.com/15-cool-detail-we-spotted-in-gta-6s-big-netflix-gameplay-reveal-2000729042'],
 'nbc_look': ['Notebookcheck: GTA 6 extended gameplay reveal shows combat, carjacking and gyms', 'https://www.notebookcheck.net/GTA-6-extended-gameplay-reveal-shows-off-new-combat-carjacking-gyms-and-much-more.1381015.0.html'],
 'svg_dazed': ['SVG: Rockstar confirms how GTA 6 players switch between Jason and Lucia', 'https://www.svg.com/2245115/rockstar-gta-6-players-switch-jason-lucia/'],
 'gi_chars': ['Game Informer: Rockstar details the characters of Grand Theft Auto VI', 'https://www.gameinformer.com/2025/05/06/rockstar-details-9-of-grand-theft-auto-vi-presumably-many-many-characters'],
 'tr_t2': ['TechRadar: Trailer 2 was captured entirely in-game on PS5', 'https://www.techradar.com/gaming/rockstar-confirms-the-latest-grand-theft-auto-6-trailer-was-all-gameplay-and-cutscenes-captured-entirely-in-game-on-the-ps5'],
 'vgc_delay2': ['VGC: Grand Theft Auto 6 delayed again to the end of 2026', 'https://www.videogameschronicle.com/news/grand-theft-auto-6-has-been-delayed-again-to-the-end-of-2026/'],
}

G2 = []
def g(slug, mins, src, title, lede, body, **kw):
    d = {'slug': slug, 'cat': 'game', 'mins': mins, 'src': src, 'title': title, 'lede': lede, 'body': body}
    d.update(kw); G2.append(d)

# 1 ─ The Extended Look
g('gameplay-extended-look', 5, ['vgc_netflix', 'kotaku_look', 'nbc_look'],
 {'en': 'GTA 6 gameplay: everything the 30-minute Extended Look showed',
  'es': 'Gameplay de GTA 6: todo lo que mostró el Extended Look de 30 minutos',
  'pt': 'Gameplay de GTA 6: tudo o que o Extended Look de 30 minutos mostrou'},
 {'en': 'On August 27, Rockstar finally showed long, uncut gameplay on Netflix. Here is what it taught us about how GTA 6 plays.',
  'es': 'El 27 de agosto Rockstar por fin mostró gameplay largo y sin cortes en Netflix. Esto es lo que aprendimos sobre cómo se juega GTA 6.',
  'pt': 'Em 27 de agosto a Rockstar finalmente mostrou gameplay longo e sem cortes na Netflix. Veja o que aprendemos sobre como GTA 6 se joga.'},
 {'en': """<h2>What it was</h2><p>The <strong>Grand Theft Auto VI Extended Look</strong> premiered on Netflix on <strong>August 27, 2026</strong>. It ran a little over 30 minutes, all captured in-game on a standard PS5, and it was the first time Rockstar let a camera follow Jason and Lucia through real missions instead of a cut trailer.</p>
<h2>The big takeaways</h2>
<ul><li><strong>Two heroes, one story.</strong> Missions can be played as Jason or as Lucia, and the two can work together or split up. Switching between them looked almost instant.</li>
<li><strong>A smarter police chase.</strong> Instead of every cop car on the minimap, a search area shows where police think you are. Changing your mask, hat or clothes helps you lose them.</li>
<li><strong>You can choose not to kill.</strong> The aim reticle flashes red on a kill and yellow when an enemy is only taken down, so non-lethal play is a real option.</li>
<li><strong>Stealing a car takes work.</strong> Some cars need a lock picked, some have trackers, and some need their key fob cloned.</li>
<li><strong>A quick menu for weapons and outfits.</strong> The weapon wheel has a second tab for clothing, so you can put on a mask right before a robbery.</li></ul>
<h2>The small things</h2><p>Jason opens the fridge and picks a Sprunk or an eCola. Characters sweat after the gym, after dancing and after a gunfight. The minimap draws buildings in 3D. You can pet a dog, and a pod of manatees drifts through the swamps.</p>
<h2>Our read</h2><p>The Extended Look made one thing clear: GTA 6 is built around a couple, not a lone criminal. Almost every system shown, from texting to robberies with a getaway driver, assumes there are two of you.</p>""",
  'es': """<h2>Qué fue</h2><p>El <strong>Grand Theft Auto VI Extended Look</strong> se estrenó en Netflix el <strong>27 de agosto de 2026</strong>. Duró algo más de 30 minutos, todo capturado dentro del juego en una PS5 normal, y fue la primera vez que Rockstar dejó que la cámara siguiera a Jason y Lucia en misiones reales en lugar de un tráiler editado.</p>
<h2>Lo más importante</h2>
<ul><li><strong>Dos protagonistas, una historia.</strong> Las misiones se pueden jugar como Jason o como Lucia, y los dos pueden trabajar juntos o por separado. El cambio entre ellos pareció casi instantáneo.</li>
<li><strong>Una persecución más inteligente.</strong> En lugar de ver cada patrulla en el minimapa, una zona de búsqueda muestra dónde cree la policía que estás. Cambiarte la máscara, el sombrero o la ropa ayuda a perderlos.</li>
<li><strong>Puedes elegir no matar.</strong> La mira se pone roja cuando matas y amarilla cuando solo neutralizas, así que jugar sin matar es una opción real.</li>
<li><strong>Robar un auto cuesta trabajo.</strong> Algunos piden forzar la cerradura, otros tienen rastreador y otros exigen clonar la llave.</li>
<li><strong>Un menú rápido para armas y ropa.</strong> La rueda de armas tiene una segunda pestaña de ropa, para ponerte una máscara justo antes de un asalto.</li></ul>
<h2>Los detalles</h2><p>Jason abre la nevera y elige una Sprunk o una eCola. Los personajes sudan después del gimnasio, de bailar y de un tiroteo. El minimapa dibuja los edificios en 3D. Puedes acariciar a un perro, y una familia de manatíes cruza los pantanos.</p>
<h2>Nuestra lectura</h2><p>El Extended Look dejó algo claro: GTA 6 gira en torno a una pareja, no a un criminal solitario. Casi todo lo que se mostró, de los mensajes a los asaltos con alguien al volante, da por hecho que son dos.</p>""",
  'pt': """<h2>O que foi</h2><p>O <strong>Grand Theft Auto VI Extended Look</strong> estreou na Netflix em <strong>27 de agosto de 2026</strong>. Teve pouco mais de 30 minutos, tudo capturado dentro do jogo em um PS5 comum, e foi a primeira vez que a Rockstar deixou a câmera acompanhar Jason e Lucia em missões de verdade, e não num trailer editado.</p>
<h2>O mais importante</h2>
<ul><li><strong>Dois protagonistas, uma história.</strong> Dá para jogar as missões como Jason ou como Lucia, e os dois podem agir juntos ou separados. A troca entre eles pareceu quase instantânea.</li>
<li><strong>Uma perseguição mais esperta.</strong> Em vez de mostrar cada viatura no minimapa, uma área de busca indica onde a polícia acha que você está. Trocar máscara, chapéu ou roupa ajuda a despistar.</li>
<li><strong>Você pode escolher não matar.</strong> A mira fica vermelha quando você mata e amarela quando só derruba o inimigo, então jogar sem matar é uma opção real.</li>
<li><strong>Roubar carro dá trabalho.</strong> Alguns pedem para arrombar a fechadura, outros têm rastreador e outros exigem clonar a chave.</li>
<li><strong>Um menu rápido de armas e roupas.</strong> A roda de armas ganhou uma segunda aba de roupas, para vestir a máscara logo antes de um assalto.</li></ul>
<h2>Os detalhes</h2><p>Jason abre a geladeira e escolhe uma Sprunk ou uma eCola. Os personagens suam depois da academia, de dançar e de um tiroteio. O minimapa desenha os prédios em 3D. Dá para fazer carinho em cachorro, e um grupo de peixes-boi atravessa os pântanos.</p>
<h2>Nossa leitura</h2><p>O Extended Look deixou uma coisa clara: GTA 6 gira em torno de um casal, não de um criminoso solitário. Quase tudo o que apareceu, das mensagens aos assaltos com alguém no volante, parte do princípio de que vocês são dois.</p>"""})

# 2 ─ Jason & Lucia / switching
g('jason-and-lucia', 4, ['svg_dazed', 'vgc_netflix', 'gi_chars'],
 {'en': 'Jason and Lucia: who they are and how switching works',
  'es': 'Jason y Lucia: quiénes son y cómo funciona el cambio de personaje',
  'pt': 'Jason e Lucia: quem são e como funciona a troca de personagem'},
 {'en': 'GTA 6 has two leads who are a couple. Here is what Rockstar has said about them and about playing as both.',
  'es': 'GTA 6 tiene dos protagonistas que son pareja. Esto es lo que Rockstar dijo sobre ellos y sobre jugar con los dos.',
  'pt': 'GTA 6 tem dois protagonistas que são um casal. Veja o que a Rockstar disse sobre eles e sobre jogar com os dois.'},
 {'en': """<h2>Lucia Caminos</h2><p>Lucia is the series' first female lead of the modern era. Rockstar describes her as a fighter, taught by her father, who ended up in a Leonida prison after fighting for her family. The first trailer opens with her in an orange jumpsuit, and the story starts with her getting out.</p>
<h2>Jason Duval</h2><p>Jason is an army veteran who drifted into running jobs for drug smugglers in the Leonida Keys. He wants an easier life, and Lucia may be the reason he thinks one is possible.</p>
<h2>A couple on the run</h2><p>Rockstar's narrative lead has called it a <em>Bonnie and Clyde</em> story, and the relationship changes over the course of the game. The two text each other, hold hands, share an apartment, and call each other "Jay" and "Lu".</p>
<h2>How switching works</h2><ul><li>You can swap between Jason and Lucia almost instantly, in free roam and during action, as GTA V did with its three leads.</li>
<li>Missions can be played as either of them. When they are together, one can drive while the other shoots, or one can rob a store while the other waits in the getaway car.</li>
<li>Some story missions split them up for a while. Outside those, Rockstar says the pair travel as a package.</li></ul>
<h2>What we do not know yet</h2><p>Rockstar has not said whether money, weapons or skills are shared between the two, or how much each one's choices change the ending. We will update this guide on launch day.</p>""",
  'es': """<h2>Lucia Caminos</h2><p>Lucia es la primera protagonista femenina de la saga en la era moderna. Rockstar la describe como una luchadora, entrenada por su padre, que acabó en una cárcel de Leonida por pelear por su familia. El primer tráiler empieza con ella en uniforme naranja, y la historia arranca cuando sale.</p>
<h2>Jason Duval</h2><p>Jason es un veterano del ejército que terminó haciendo trabajos para contrabandistas de droga en los Cayos de Leonida. Quiere una vida más tranquila, y Lucia puede ser la razón por la que cree que es posible.</p>
<h2>Una pareja a la fuga</h2><p>El responsable de narrativa de Rockstar lo llamó una historia al estilo <em>Bonnie y Clyde</em>, y la relación cambia a lo largo del juego. Se escriben mensajes, se toman de la mano, comparten departamento y se llaman "Jay" y "Lu".</p>
<h2>Cómo funciona el cambio</h2><ul><li>Puedes pasar de Jason a Lucia casi al instante, en mundo abierto y en plena acción, como en GTA V con sus tres protagonistas.</li>
<li>Las misiones se pueden jugar con cualquiera de los dos. Cuando están juntos, uno puede manejar mientras el otro dispara, o uno asalta una tienda mientras el otro espera en el auto de escape.</li>
<li>Algunas misiones de la historia los separan un tiempo. Fuera de eso, Rockstar dice que viajan juntos.</li></ul>
<h2>Lo que aún no sabemos</h2><p>Rockstar no dijo si el dinero, las armas o las habilidades se comparten, ni cuánto cambian el final las decisiones de cada uno. Actualizaremos esta guía el día del lanzamiento.</p>""",
  'pt': """<h2>Lucia Caminos</h2><p>Lucia é a primeira protagonista mulher da série na era moderna. A Rockstar a descreve como uma lutadora, treinada pelo pai, que foi parar numa prisão de Leonida depois de brigar pela família. O primeiro trailer abre com ela de macacão laranja, e a história começa quando ela sai.</p>
<h2>Jason Duval</h2><p>Jason é um veterano do exército que acabou fazendo serviços para traficantes nas Leonida Keys. Ele quer uma vida mais tranquila, e Lucia pode ser o motivo de ele achar isso possível.</p>
<h2>Um casal em fuga</h2><p>O líder de narrativa da Rockstar chamou de uma história no estilo <em>Bonnie e Clyde</em>, e o relacionamento muda ao longo do jogo. Os dois trocam mensagens, andam de mãos dadas, dividem apartamento e se chamam de "Jay" e "Lu".</p>
<h2>Como funciona a troca</h2><ul><li>Dá para trocar entre Jason e Lucia quase na hora, no mundo aberto e no meio da ação, como no GTA V com seus três protagonistas.</li>
<li>As missões podem ser jogadas com qualquer um dos dois. Quando estão juntos, um dirige enquanto o outro atira, ou um assalta a loja enquanto o outro espera no carro de fuga.</li>
<li>Algumas missões da história separam os dois por um tempo. Fora isso, a Rockstar diz que eles andam juntos.</li></ul>
<h2>O que ainda não sabemos</h2><p>A Rockstar não disse se dinheiro, armas ou habilidades são compartilhados, nem o quanto as escolhas de cada um mudam o final. Vamos atualizar este guia no dia do lançamento.</p>"""})

# 3 ─ Characters
g('characters', 4, ['gi_chars', 'tr_t2'],
 {'en': 'Every confirmed GTA 6 character so far', 'es': 'Todos los personajes confirmados de GTA 6 hasta ahora', 'pt': 'Todos os personagens confirmados de GTA 6 até agora'},
 {'en': 'Beyond Jason and Lucia, Rockstar has introduced a cast of bosses, friends, artists and influencers. Here is who is who.',
  'es': 'Además de Jason y Lucia, Rockstar presentó jefes, amigos, artistas e influencers. Aquí está quién es quién.',
  'pt': 'Além de Jason e Lucia, a Rockstar apresentou chefes, amigos, artistas e influencers. Veja quem é quem.'},
 {'en': """<p>Rockstar introduced most of the supporting cast alongside the second trailer in May 2025, with a profile for each on its official site.</p>
<h2>The leads</h2><ul><li><strong>Lucia Caminos</strong>: a fighter fresh out of prison, ready to take what she believes she is owed.</li><li><strong>Jason Duval</strong>: an army veteran working for smugglers in the Keys.</li></ul>
<h2>The Keys crew</h2><ul><li><strong>Brian Heder</strong>: an old-school drug runner who gives Jason work and runs the business with his wife, <strong>Lori</strong>.</li><li><strong>Cal Hampton</strong>: Jason's friend, also on Brian's payroll, who spends a lot of time online with theories about everything.</li></ul>
<h2>Vice City players</h2><ul><li><strong>Boobie Ike</strong>: a Vice City local who turned his criminal start into legitimate businesses, from real estate to a strip club and a music label.</li><li><strong>Dre'Quan Priest</strong>: an aspiring music mogul, more hustler than gangster, signed to Boobie's label.</li><li><strong>Real Dimez</strong>: Bae-Luxe and Roxy, two high school friends turned rap duo who blew up on social media.</li><li><strong>Raul Bautista</strong>: a charming, experienced bank robber who is always looking for new talent for bigger jobs.</li></ul>
<h2>Why it matters</h2><p>Look at the list and you can almost see the missions: smuggling runs in the Keys, music-business drama in Vice City, and heists with a professional. Rockstar has not said which characters give missions, so treat that as our guess.</p>""",
  'es': """<p>Rockstar presentó a casi todo el reparto secundario junto con el segundo tráiler en mayo de 2025, con un perfil de cada uno en su sitio oficial.</p>
<h2>Los protagonistas</h2><ul><li><strong>Lucia Caminos</strong>: una luchadora recién salida de prisión, dispuesta a tomar lo que cree que le deben.</li><li><strong>Jason Duval</strong>: un veterano del ejército que trabaja para contrabandistas en los Cayos.</li></ul>
<h2>La gente de los Cayos</h2><ul><li><strong>Brian Heder</strong>: un traficante de la vieja escuela que le da trabajo a Jason y maneja el negocio con su esposa, <strong>Lori</strong>.</li><li><strong>Cal Hampton</strong>: amigo de Jason, también a sueldo de Brian, que pasa mucho tiempo en internet con teorías sobre todo.</li></ul>
<h2>Figuras de Vice City</h2><ul><li><strong>Boobie Ike</strong>: un local de Vice City que convirtió su pasado criminal en negocios legales, de bienes raíces a un club de striptease y un sello musical.</li><li><strong>Dre'Quan Priest</strong>: aspirante a magnate musical, más buscavidas que gánster, firmado con el sello de Boobie.</li><li><strong>Real Dimez</strong>: Bae-Luxe y Roxy, dos amigas de la secundaria convertidas en dúo de rap que explotó en redes sociales.</li><li><strong>Raul Bautista</strong>: un ladrón de bancos encantador y con experiencia, siempre buscando talento para golpes más grandes.</li></ul>
<h2>Por qué importa</h2><p>Mirando la lista casi se ven las misiones: contrabando en los Cayos, drama de la industria musical en Vice City y golpes con un profesional. Rockstar no dijo qué personajes dan misiones, así que tómalo como nuestra suposición.</p>""",
  'pt': """<p>A Rockstar apresentou quase todo o elenco de apoio junto com o segundo trailer, em maio de 2025, com um perfil de cada um no site oficial.</p>
<h2>Os protagonistas</h2><ul><li><strong>Lucia Caminos</strong>: uma lutadora recém-saída da prisão, pronta para pegar o que acha que é dela.</li><li><strong>Jason Duval</strong>: um veterano do exército que trabalha para contrabandistas nas Keys.</li></ul>
<h2>A turma das Keys</h2><ul><li><strong>Brian Heder</strong>: um traficante das antigas que dá trabalho a Jason e toca o negócio com a esposa, <strong>Lori</strong>.</li><li><strong>Cal Hampton</strong>: amigo de Jason, também pago por Brian, que passa muito tempo na internet com teorias sobre tudo.</li></ul>
<h2>Figuras de Vice City</h2><ul><li><strong>Boobie Ike</strong>: um morador de Vice City que transformou o começo no crime em negócios legais, de imóveis a uma boate de strip e uma gravadora.</li><li><strong>Dre'Quan Priest</strong>: aspirante a magnata da música, mais malandro que gângster, contratado pela gravadora de Boobie.</li><li><strong>Real Dimez</strong>: Bae-Luxe e Roxy, duas amigas de escola que viraram dupla de rap e estouraram nas redes sociais.</li><li><strong>Raul Bautista</strong>: um ladrão de bancos charmoso e experiente, sempre atrás de talentos para golpes maiores.</li></ul>
<h2>Por que isso importa</h2><p>Olhando a lista, quase dá para ver as missões: contrabando nas Keys, treta na indústria da música em Vice City e golpes com um profissional. A Rockstar não disse quais personagens dão missões, então isso é palpite nosso.</p>"""})

# 4 ─ Police and wanted system
g('wanted-system', 3, ['vgc_netflix', 'nbc_look'],
 {'en': 'How police and the wanted system work in GTA 6', 'es': 'Cómo funcionan la policía y el nivel de búsqueda en GTA 6', 'pt': 'Como funcionam a polícia e o nível de procurado em GTA 6'},
 {'en': 'The stars are back, but escaping the cops works differently now. Here is what has been shown.',
  'es': 'Las estrellas vuelven, pero escapar de la policía funciona distinto. Esto es lo que se mostró.',
  'pt': 'As estrelas voltaram, mas fugir da polícia funciona diferente agora. Veja o que já foi mostrado.'},
 {'en': """<h2>A search area, not a radar</h2><p>In GTA V every police car showed up on your minimap. In GTA 6 you see a <strong>search area</strong> instead: a zone where the police believe you are. Get out of it unseen and the heat starts to drop.</p>
<h2>They remember what you look like</h2><p>Police work from what witnesses saw: your clothes and the car you were in. That makes two classic tricks more useful than ever:</p><ul><li><strong>Change your look.</strong> Swap masks, hats or outfits from the clothing tab of the quick menu. Rockstar showed this lowering the wanted level.</li><li><strong>Ditch the car.</strong> A different vehicle buys you time, especially one you did not steal in front of anyone.</li></ul>
<h2>They actually search</h2><p>Hiding in an alley or a parking garage works for a while, but officers sweep the area on foot and by car before they give up. Do not stay in one spot too long.</p>
<h2>Plan the getaway</h2><p>The Extended Look showed one character robbing a store while the other waited in the car. With a driver ready and a change of clothes, the chase can be over before it starts.</p>""",
  'es': """<h2>Una zona de búsqueda, no un radar</h2><p>En GTA V cada patrulla aparecía en el minimapa. En GTA 6 ves una <strong>zona de búsqueda</strong>: el área donde la policía cree que estás. Sal de ella sin que te vean y la presión empieza a bajar.</p>
<h2>Recuerdan cómo te ves</h2><p>La policía trabaja con lo que vieron los testigos: tu ropa y el auto en que ibas. Eso vuelve más útiles que nunca dos trucos clásicos:</p><ul><li><strong>Cambia de aspecto.</strong> Cambia máscara, gorra o ropa desde la pestaña de ropa del menú rápido. Rockstar mostró que esto baja el nivel de búsqueda.</li><li><strong>Deja el auto.</strong> Otro vehículo te da tiempo, sobre todo uno que no robaste frente a nadie.</li></ul>
<h2>De verdad te buscan</h2><p>Esconderte en un callejón o un estacionamiento sirve un rato, pero los agentes recorren la zona a pie y en auto antes de rendirse. No te quedes demasiado en el mismo lugar.</p>
<h2>Planea la huida</h2><p>El Extended Look mostró a un personaje asaltando una tienda mientras el otro esperaba en el auto. Con alguien al volante y un cambio de ropa, la persecución puede terminar antes de empezar.</p>""",
  'pt': """<h2>Uma área de busca, não um radar</h2><p>No GTA V toda viatura aparecia no minimapa. No GTA 6 você vê uma <strong>área de busca</strong>: a região onde a polícia acha que você está. Saia dela sem ser visto e a pressão começa a cair.</p>
<h2>Eles lembram da sua cara</h2><p>A polícia trabalha com o que as testemunhas viram: sua roupa e o carro em que você estava. Isso deixa dois truques clássicos mais úteis do que nunca:</p><ul><li><strong>Mude o visual.</strong> Troque máscara, boné ou roupa pela aba de roupas do menu rápido. A Rockstar mostrou isso baixando o nível de procurado.</li><li><strong>Largue o carro.</strong> Outro veículo te dá tempo, ainda mais um que você não roubou na frente de ninguém.</li></ul>
<h2>Eles procuram de verdade</h2><p>Se esconder num beco ou num estacionamento funciona por um tempo, mas os policiais varrem a área a pé e de carro antes de desistir. Não fique parado no mesmo lugar por muito tempo.</p>
<h2>Planeje a fuga</h2><p>O Extended Look mostrou um personagem assaltando uma loja enquanto o outro esperava no carro. Com alguém no volante e uma troca de roupa, a perseguição pode acabar antes de começar.</p>"""})

# 5 ─ Combat, weapons and cars
g('combat-and-cars', 4, ['kotaku_look', 'nbc_look', 'vgc_netflix'],
 {'en': 'GTA 6 combat, weapons and stealing cars: what changed', 'es': 'Combate, armas y robo de autos en GTA 6: qué cambió', 'pt': 'Combate, armas e roubo de carros em GTA 6: o que mudou'},
 {'en': 'Non-lethal takedowns, branded guns, lock-picking and key-fob cloning. A look at the action side of GTA 6.',
  'es': 'Derribos no letales, armas con marca, ganzúas y llaves clonadas. Un vistazo al lado de acción de GTA 6.',
  'pt': 'Derrubadas não letais, armas com marca, chave michada e chave clonada. Um olhar sobre o lado de ação de GTA 6.'},
 {'en': """<h2>Kill or just take down</h2><p>The aim reticle flashes <strong>red</strong> on a kill and <strong>yellow</strong> when an enemy is only incapacitated. In slow-motion aiming, body parts are marked the same way, so you can pick shots that drop someone without killing them. Enemies also stay down hurt, instead of every hit being final.</p>
<h2>Guns with names</h2><p>Weapons now carry brands and model numbers. Jason picks up a shotgun called the <strong>Moreland 850</strong>. Gunfights showed pistols, shotguns, automatic weapons fired from cars, and a Molotov that set a car on fire, with the fire spreading.</p>
<h2>Quick menu</h2><p>The weapon wheel has a second tab for clothing. Health items sit in their own slots, and food and drinks give short boosts.</p>
<h2>Stealing a car</h2><ul><li>Some cars need the lock picked, in a small mini-game.</li><li>Some carry a tracker you will have to deal with.</li><li>High-end cars may need their key fob cloned.</li></ul><p>Rockstar also showed a car being broken into with a hammer, tyres being shot out, and first-person driving during a chase.</p>
<h2>Driving feel</h2><p>Cars show body roll and weight in turns, and crashes look heavier than in GTA V. During chases, police cars flipped and tumbled, so expect pursuits to be messier.</p>""",
  'es': """<h2>Matar o solo derribar</h2><p>La mira se pone <strong>roja</strong> cuando matas y <strong>amarilla</strong> cuando el enemigo solo queda fuera de combate. Al apuntar en cámara lenta, las partes del cuerpo se marcan igual, así que puedes elegir disparos que derriban sin matar. Los enemigos además quedan heridos en el suelo, en lugar de que cada impacto sea final.</p>
<h2>Armas con nombre</h2><p>Las armas ahora tienen marca y modelo. Jason recoge una escopeta llamada <strong>Moreland 850</strong>. Los tiroteos mostraron pistolas, escopetas, armas automáticas disparadas desde autos y un Molotov que incendió un vehículo, con el fuego propagándose.</p>
<h2>Menú rápido</h2><p>La rueda de armas tiene una segunda pestaña de ropa. Los objetos de salud tienen ranuras propias, y la comida y la bebida dan mejoras cortas.</p>
<h2>Robar un auto</h2><ul><li>Algunos autos piden forzar la cerradura en un pequeño minijuego.</li><li>Otros tienen un rastreador que tendrás que resolver.</li><li>Los de alta gama pueden pedir clonar la llave.</li></ul><p>Rockstar también mostró un auto abierto a martillazos, neumáticos reventados a tiros y manejo en primera persona durante una persecución.</p>
<h2>Sensación al manejar</h2><p>Los autos se inclinan y pesan en las curvas, y los choques se ven más fuertes que en GTA V. En las persecuciones las patrullas volcaban y daban vueltas, así que espera huidas más caóticas.</p>""",
  'pt': """<h2>Matar ou só derrubar</h2><p>A mira fica <strong>vermelha</strong> quando você mata e <strong>amarela</strong> quando o inimigo só é neutralizado. Na mira em câmera lenta, as partes do corpo são marcadas do mesmo jeito, então dá para escolher tiros que derrubam sem matar. Os inimigos também ficam feridos no chão, em vez de todo tiro ser fatal.</p>
<h2>Armas com nome</h2><p>As armas agora têm marca e modelo. Jason pega uma espingarda chamada <strong>Moreland 850</strong>. Os tiroteios mostraram pistolas, espingardas, armas automáticas disparadas de dentro do carro e um coquetel molotov que incendiou um veículo, com o fogo se espalhando.</p>
<h2>Menu rápido</h2><p>A roda de armas ganhou uma segunda aba de roupas. Itens de cura têm espaço próprio, e comida e bebida dão bônus curtos.</p>
<h2>Roubar um carro</h2><ul><li>Alguns carros pedem para arrombar a fechadura num minijogo.</li><li>Outros têm rastreador, que você vai precisar resolver.</li><li>Os de luxo podem exigir clonar a chave.</li></ul><p>A Rockstar também mostrou um carro sendo aberto com martelo, pneus estourados a tiro e direção em primeira pessoa durante uma perseguição.</p>
<h2>Sensação ao dirigir</h2><p>Os carros inclinam e pesam nas curvas, e as batidas parecem mais pesadas que no GTA V. Nas perseguições, viaturas capotaram e rolaram, então espere fugas mais caóticas.</p>"""})

# 6 ─ Activities
g('things-to-do', 3, ['vgc_netflix', 'nbc_look', 'kotaku_look'],
 {'en': 'Things to do in Leonida: every side activity shown so far', 'es': 'Qué hacer en Leonida: todas las actividades mostradas hasta ahora', 'pt': 'O que fazer em Leonida: todas as atividades mostradas até agora'},
 {'en': 'Fishing, airboats, basketball, the gym and a lot more. Everything Rockstar has shown you can do when you are not on a job.',
  'es': 'Pesca, hidrodeslizadores, básquet, gimnasio y mucho más. Todo lo que Rockstar mostró que puedes hacer cuando no estás en un trabajo.',
  'pt': 'Pesca, aerobarco, basquete, academia e muito mais. Tudo o que a Rockstar mostrou que dá para fazer quando você não está num serviço.'},
 {'en': """<h2>On the water</h2><ul><li>Airboat rides through the Everglades-style swamps of Grassrivers</li><li>Kayaking and rowing</li><li>Jet ski races</li><li>Boat trips and scuba diving</li><li>Fishing</li></ul>
<h2>Sports and fitness</h2><ul><li>Pick-up basketball: grab the ball and play</li><li>The gym. Lucia bench-presses by alternating the two triggers, and characters visibly sweat afterwards</li><li>The firing range</li></ul>
<h2>Racing and thrills</h2><ul><li>Street races and dirt bike races</li><li>BMX</li><li>Skydiving. Lucia jumps off a building in the Extended Look</li></ul>
<h2>Nightlife and downtime</h2><ul><li>Clubs and dancing</li><li>Strip clubs, which Jason and Lucia can visit together</li><li>Hanging out at home: TV, the fridge, the lights</li><li>Petting dogs and watching wildlife, from birds to manatees and alligators</li></ul>
<h2>Social media everywhere</h2><p>Influencers stream from cars in the middle of chases, with the chat on screen, and one even rides on the trunk of Jason's car. Expect Leonida's social feeds to react to what you do.</p>""",
  'es': """<h2>En el agua</h2><ul><li>Paseos en hidrodeslizador por los pantanos estilo Everglades de Grassrivers</li><li>Kayak y remo</li><li>Carreras de moto acuática</li><li>Paseos en barco y buceo</li><li>Pesca</li></ul>
<h2>Deporte y ejercicio</h2><ul><li>Básquet callejero: agarra la pelota y juega</li><li>El gimnasio. Lucia hace press de banca alternando los dos gatillos, y los personajes quedan sudados</li><li>El campo de tiro</li></ul>
<h2>Carreras y adrenalina</h2><ul><li>Carreras callejeras y de motocross</li><li>BMX</li><li>Paracaidismo. Lucia salta desde un edificio en el Extended Look</li></ul>
<h2>Noche y descanso</h2><ul><li>Discotecas y baile</li><li>Clubes de striptease, que Jason y Lucia pueden visitar juntos</li><li>Pasar el rato en casa: tele, nevera, luces</li><li>Acariciar perros y ver fauna, de aves a manatíes y caimanes</li></ul>
<h2>Redes sociales por todas partes</h2><p>Los influencers transmiten desde autos en plena persecución, con el chat en pantalla, y uno hasta va sobre el maletero del auto de Jason. Espera que las redes de Leonida reaccionen a lo que haces.</p>""",
  'pt': """<h2>Na água</h2><ul><li>Passeios de aerobarco pelos pântanos estilo Everglades de Grassrivers</li><li>Caiaque e remo</li><li>Corridas de jet ski</li><li>Passeios de barco e mergulho</li><li>Pesca</li></ul>
<h2>Esporte e academia</h2><ul><li>Basquete de rua: pegue a bola e jogue</li><li>A academia. Lucia faz supino alternando os dois gatilhos, e os personagens ficam suados depois</li><li>O estande de tiro</li></ul>
<h2>Corridas e adrenalina</h2><ul><li>Rachas de rua e corridas de motocross</li><li>BMX</li><li>Paraquedismo. Lucia pula de um prédio no Extended Look</li></ul>
<h2>Noite e descanso</h2><ul><li>Baladas e dança</li><li>Boates de strip, que Jason e Lucia podem visitar juntos</li><li>Ficar em casa: TV, geladeira, luzes</li><li>Fazer carinho em cachorro e ver a fauna, de pássaros a peixes-boi e jacarés</li></ul>
<h2>Redes sociais em todo lugar</h2><p>Influencers fazem live de dentro do carro no meio de perseguições, com o chat na tela, e um até vai em cima do porta-malas do carro do Jason. Espere que as redes de Leonida reajam ao que você faz.</p>"""})

# 7 ─ References and callbacks
g('references-and-callbacks', 3, ['kotaku_look', 'vgc_netflix', 'tr_t2'],
 {'en': 'GTA 6 references and callbacks to older GTA games', 'es': 'Referencias de GTA 6 a los GTA anteriores', 'pt': 'Referências de GTA 6 aos GTAs anteriores'},
 {'en': 'Vice City is back, and so are a few old friends. The nods to the series we have spotted in official footage.',
  'es': 'Vice City vuelve, y también algunos viejos conocidos. Los guiños a la saga que vimos en el material oficial.',
  'pt': 'Vice City voltou, e alguns velhos conhecidos também. As referências à série que vimos no material oficial.'},
 {'en': """<h2>Vice City, again</h2><p>Vice City first appeared in the original 1997 Grand Theft Auto, then got its own game in 2002, <em>GTA: Vice City</em>, set in 1986. GTA 6 brings it back in the present day as the heart of the state of Leonida, Rockstar's take on Florida, just like Liberty City stands in for New York and Los Santos for Los Angeles.</p>
<h2>Lovefist</h2><p>In the Extended Look, a woman talking to Lucia wears a <strong>Lovefist</strong> T-shirt. Lovefist was the hair-metal band at the center of a run of missions in GTA: Vice City.</p>
<h2>The brands never die</h2><ul><li><strong>Sprunk</strong> and <strong>eCola</strong> are in Jason's fridge, the series' long-running soda rivals.</li><li><strong>Gruppe Sechs</strong> armored trucks, the security company from GTA V, are on Leonida's streets.</li><li>A <strong>Fleeca</strong> bank logo shows up, the bank from GTA V's first heist and GTA Online.</li></ul>
<h2>Bonnie and Clyde</h2><p>Rockstar's narrative lead describes GTA 6 as a Bonnie and Clyde story. A criminal couple is something fans asked for for years, and this time it is the foundation of the whole game.</p>
<h2>Systems from GTA V</h2><p>Character switching, slow-motion aiming and convertibles all return from GTA V, now reworked for two leads.</p>""",
  'es': """<h2>Vice City, otra vez</h2><p>Vice City apareció en el primer Grand Theft Auto de 1997 y tuvo su propio juego en 2002, <em>GTA: Vice City</em>, ambientado en 1986. GTA 6 la trae de vuelta en la actualidad como el corazón del estado de Leonida, la versión de Rockstar de Florida, igual que Liberty City representa a Nueva York y Los Santos a Los Ángeles.</p>
<h2>Lovefist</h2><p>En el Extended Look, una mujer que habla con Lucia lleva una camiseta de <strong>Lovefist</strong>. Lovefist era la banda de hair metal de varias misiones de GTA: Vice City.</p>
<h2>Las marcas nunca mueren</h2><ul><li><strong>Sprunk</strong> y <strong>eCola</strong> están en la nevera de Jason, los refrescos rivales de siempre en la saga.</li><li>Los camiones blindados de <strong>Gruppe Sechs</strong>, la empresa de seguridad de GTA V, circulan por Leonida.</li><li>Aparece el logo del banco <strong>Fleeca</strong>, el del primer golpe de GTA V y de GTA Online.</li></ul>
<h2>Bonnie y Clyde</h2><p>El responsable de narrativa de Rockstar define GTA 6 como una historia al estilo Bonnie y Clyde. Una pareja criminal fue siempre una idea que los fans pedían, y esta vez es la base de todo el juego.</p>
<h2>Sistemas de GTA V</h2><p>El cambio de personaje, la puntería en cámara lenta y los descapotables vuelven de GTA V, ahora rediseñados para dos protagonistas.</p>""",
  'pt': """<h2>Vice City, de novo</h2><p>Vice City apareceu no primeiro Grand Theft Auto, de 1997, e ganhou um jogo próprio em 2002, <em>GTA: Vice City</em>, ambientado em 1986. GTA 6 traz a cidade de volta nos dias de hoje como o coração do estado de Leonida, a versão da Rockstar para a Flórida, assim como Liberty City representa Nova York e Los Santos representa Los Angeles.</p>
<h2>Lovefist</h2><p>No Extended Look, uma mulher que conversa com Lucia usa uma camiseta do <strong>Lovefist</strong>. O Lovefist era a banda de hair metal de várias missões de GTA: Vice City.</p>
<h2>As marcas nunca morrem</h2><ul><li><strong>Sprunk</strong> e <strong>eCola</strong> estão na geladeira do Jason, os refrigerantes rivais de sempre na série.</li><li>Carros-fortes da <strong>Gruppe Sechs</strong>, a empresa de segurança do GTA V, rodam por Leonida.</li><li>Aparece o logo do banco <strong>Fleeca</strong>, o do primeiro assalto do GTA V e do GTA Online.</li></ul>
<h2>Bonnie e Clyde</h2><p>O líder de narrativa da Rockstar define GTA 6 como uma história no estilo Bonnie e Clyde. Um casal criminoso sempre foi um pedido dos fãs, e desta vez é a base do jogo inteiro.</p>
<h2>Sistemas do GTA V</h2><p>A troca de personagem, a mira em câmera lenta e os conversíveis voltam do GTA V, agora refeitos para dois protagonistas.</p>"""})

# 8 ─ Timeline
g('timeline', 3, ['tr_t2', 'vgc_delay2', 'vgc_netflix'],
 {'en': 'The road to GTA 6: a timeline from announcement to launch', 'es': 'El camino a GTA 6: cronología del anuncio al lanzamiento', 'pt': 'O caminho até GTA 6: linha do tempo do anúncio ao lançamento'},
 {'en': 'Two trailers, two delays and one Netflix special. Every official milestone on the way to November 19, 2026.',
  'es': 'Dos tráilers, dos retrasos y un especial de Netflix. Cada hito oficial camino al 19 de noviembre de 2026.',
  'pt': 'Dois trailers, dois adiamentos e um especial da Netflix. Cada marco oficial até 19 de novembro de 2026.'},
 {'en': """<ul class="tl">
<li><strong>February 2022</strong>: Rockstar confirms that development of the next Grand Theft Auto is well underway.</li>
<li><strong>December 2023</strong>: Trailer 1. Lucia, Vice City and a 2025 target. It became one of the most-watched non-music videos on YouTube in its first 24 hours.</li>
<li><strong>May 2, 2025</strong>: First delay, from fall 2025 to May 26, 2026.</li>
<li><strong>May 6, 2025</strong>: Trailer 2 introduces Jason and the supporting cast. Rockstar later says it was captured entirely in-game on a PS5, half gameplay and half cutscenes.</li>
<li><strong>November 6, 2025</strong>: Second delay, to <strong>November 19, 2026</strong>, to give the team time to polish.</li>
<li><strong>August 27, 2026</strong>: The Grand Theft Auto VI Extended Look premieres on Netflix with about 30 minutes of gameplay.</li>
<li><strong>October 2026</strong>: The launch trailer arrives.</li>
<li><strong>November 10, 2026</strong>: Pre-load opens on PS5 and Xbox Series X|S. Up to 212 GB.</li>
<li><strong>November 19, 2026</strong>: Launch on PS5, PS5 Pro and Xbox Series X|S, plus Xbox Cloud Gaming.</li></ul>
<h2>Still unannounced</h2><p>A PC version, the future of GTA Online on the new engine, and any story expansions. We will add them here as soon as Rockstar confirms anything.</p>""",
  'es': """<ul class="tl">
<li><strong>Febrero de 2022</strong>: Rockstar confirma que el desarrollo del próximo Grand Theft Auto está muy avanzado.</li>
<li><strong>Diciembre de 2023</strong>: Tráiler 1. Lucia, Vice City y la meta de 2025. Fue uno de los videos no musicales más vistos de YouTube en sus primeras 24 horas.</li>
<li><strong>2 de mayo de 2025</strong>: Primer retraso, del otoño de 2025 al 26 de mayo de 2026.</li>
<li><strong>6 de mayo de 2025</strong>: El tráiler 2 presenta a Jason y al reparto secundario. Rockstar dice después que se capturó todo dentro del juego en PS5, mitad gameplay y mitad cinemáticas.</li>
<li><strong>6 de noviembre de 2025</strong>: Segundo retraso, al <strong>19 de noviembre de 2026</strong>, para dar tiempo al pulido.</li>
<li><strong>27 de agosto de 2026</strong>: Se estrena en Netflix el Grand Theft Auto VI Extended Look, con unos 30 minutos de gameplay.</li>
<li><strong>Octubre de 2026</strong>: Llega el tráiler de lanzamiento.</li>
<li><strong>10 de noviembre de 2026</strong>: Abre la precarga en PS5 y Xbox Series X|S. Hasta 212 GB.</li>
<li><strong>19 de noviembre de 2026</strong>: Lanzamiento en PS5, PS5 Pro y Xbox Series X|S, además de Xbox Cloud Gaming.</li></ul>
<h2>Aún sin anunciar</h2><p>La versión para PC, el futuro de GTA Online en el nuevo motor y posibles expansiones de historia. Los sumaremos aquí en cuanto Rockstar confirme algo.</p>""",
  'pt': """<ul class="tl">
<li><strong>Fevereiro de 2022</strong>: A Rockstar confirma que o desenvolvimento do próximo Grand Theft Auto está bem adiantado.</li>
<li><strong>Dezembro de 2023</strong>: Trailer 1. Lucia, Vice City e a meta de 2025. Foi um dos vídeos não musicais mais vistos do YouTube nas primeiras 24 horas.</li>
<li><strong>2 de maio de 2025</strong>: Primeiro adiamento, do fim de 2025 para 26 de maio de 2026.</li>
<li><strong>6 de maio de 2025</strong>: O trailer 2 apresenta Jason e o elenco de apoio. Depois, a Rockstar diz que tudo foi capturado dentro do jogo num PS5, metade gameplay e metade cinemática.</li>
<li><strong>6 de novembro de 2025</strong>: Segundo adiamento, para <strong>19 de novembro de 2026</strong>, para dar tempo de polir o jogo.</li>
<li><strong>27 de agosto de 2026</strong>: Estreia na Netflix o Grand Theft Auto VI Extended Look, com cerca de 30 minutos de gameplay.</li>
<li><strong>Outubro de 2026</strong>: Sai o trailer de lançamento.</li>
<li><strong>10 de novembro de 2026</strong>: Abre o pre-load no PS5 e no Xbox Series X|S. Até 212 GB.</li>
<li><strong>19 de novembro de 2026</strong>: Lançamento no PS5, PS5 Pro e Xbox Series X|S, além do Xbox Cloud Gaming.</li></ul>
<h2>Ainda não anunciado</h2><p>Versão para PC, o futuro do GTA Online no motor novo e possíveis expansões de história. Vamos adicionar aqui assim que a Rockstar confirmar algo.</p>"""})
