#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for the Comunidade Cristã Rocha Eterna blog.
Builds static HTML from the POSTS dataset below. Run: python3 gen.py
"""
import os, re, base64, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
POSTS_DIR = os.path.join(OUT, "posts")

MONTHS_PT = ["janeiro","fevereiro","março","abril","maio","junho","julho",
             "agosto","setembro","outubro","novembro","dezembro"]

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text).strip().lower()
    return re.sub(r'[\s-]+', '-', text)

def b64(s):
    return base64.b64encode(s.encode('utf-8')).decode('ascii')

def fmt_date(d):
    y, m, day = d.split('-')
    return f"{int(day)} de {MONTHS_PT[int(m)-1]} de {y}"

# ---------------------------------------------------------------------------
# POST DATA
# fields: date, title, category, author, body(list of html paragraphs/blocks),
#         comments(int), hidden_comment(optional base64-worthy plain text)
# ---------------------------------------------------------------------------
POSTS = [
dict(date="2019-03-10", title="Sejam bem-vindos ao nosso espaço", category="Avisos", author="Irmã Cláudia Freitas", comments=6,
body=[
"Que alegria é poder inaugurar este pequeno espaço da nossa igreja aqui na internet! A partir de hoje, vamos usar este blog para compartilhar os avisos da semana, os testemunhos dos irmãos, reflexões da Palavra e tudo o que Deus tem feito no meio do nosso povo.",
"A Comunidade Cristã Rocha Eterna nasceu há pouco mais de seis anos, num salão alugado no bairro, com quinze pessoas e muita fé. Hoje já somos uma família bem maior, mas o propósito continua o mesmo: sermos um lugar de acolhimento, cura e crescimento na fé para todo aquele que precisar.",
"Fiquem à vontade para deixar seus comentários e compartilhar as postagens com quem vocês acham que pode ser abençoado. Que Deus continue guiando cada passo da nossa comunidade!",
]),

dict(date="2019-04-21", title="Páscoa: a vitória sobre a morte", category="Especial", author="Pastor Renato Almeida", comments=9,
body=[
"Neste domingo celebramos, mais uma vez, a maior notícia que a humanidade já recebeu: Cristo ressuscitou! Não estamos apenas lembrando um fato histórico, mas vivendo a certeza de que a morte não tem a última palavra sobre nossas vidas.",
"Chegamos ao templo ainda de madrugada para preparar tudo: as cadeiras extras, as flores que as irmãs trouxeram de seus próprios jardins, os cartazes coloridos que as crianças da Escola Bíblica Dominical fizeram na semana passada. Era visível, em cada detalhe, o cuidado de um povo que queria honrar essa data.",
"Durante o culto desta manhã, tivemos a bênção de receber quatro novas famílias que chegaram à nossa igreja nos últimos meses. Foi lindo ver o salão cheio, as crianças com suas roupas novas, e o louvor subindo forte logo cedo.",
"Pregamos hoje sobre os dois discípulos no caminho de Emaús, que caminharam ao lado do próprio Jesus ressuscitado sem reconhecê-lo, tomados pela tristeza da sexta-feira anterior. Quantas vezes nós também caminhamos ao lado da resposta de Deus sem perceber, porque estamos olhando demais para o que perdemos?",
"<blockquote>&ldquo;Ele não está aqui, pois ressuscitou, como havia dito.&rdquo; — Mateus 28:6</blockquote>",
"Um dos momentos mais bonitos da manhã foi o testemunho breve de um casal que chegou à igreja há apenas dois meses, atravessando uma fase difícil no casamento, e que hoje testificou publicamente que encontrou, na Rocha Eterna, um lugar de recomeço. Não é à toa que celebramos a ressurreição — ela também acontece, em menor escala, todos os dias, na vida de quem se dispõe a recomeçar.",
"Encerramos o culto com a ceia do Senhor, algo que fazemos poucas vezes ao ano, e que neste domingo teve um peso especial: relembrar o corpo partido e o sangue derramado antes de celebrar o túmulo vazio.",
"Que esta Páscoa renove em cada um de nós a esperança de que, assim como Ele venceu o túmulo, também vencerá as lutas que enfrentamos hoje. E que a Rocha Eterna continue sendo, para quantos Deus trouxer até aqui, um lugar onde a ressurreição se torna visível em vidas reais.",
]),

dict(date="2019-05-19", title="Vigília da Colheita: uma noite de milagres", category="Vigília", author="Pastor Renato Almeida", comments=14,
body=[
"Na sexta-feira passada, das 22h à meia-noite, nos reunimos para a nossa tradicional Vigília da Colheita. O salão ficou pequeno! Precisamos colocar cadeiras extras até no corredor.",
"Vivemos momentos fortes de intercessão pelas famílias da nossa igreja, pelos que estão desempregados, pelos enfermos e pelos jovens que têm se afastado da fé. Várias pessoas relataram, já no domingo seguinte, respostas concretas de oração — inclusive uma irmã que recebeu proposta de emprego na segunda-feira, depois de meses buscando recolocação.",
"Agradecemos a equipe de louvor e a todos que ficaram até o fim ajudando na organização e limpeza do salão. A próxima vigília já está marcada para agosto.",
]),

dict(date="2019-06-02", title="Testemunho: a cura que Deus operou em mim", category="Testemunho", author="Vera Lúcia Nascimento", comments=22,
body=[
"Eu nunca pensei que fosse escrever para o blog da igreja, mas depois do que vivi nas últimas semanas, não posso guardar isso só para mim.",
"Há cerca de dois meses, comecei a sentir dores muito fortes e os exames não davam um diagnóstico claro. Cheguei a ficar internada por três dias. Foi um período de muito medo, confesso. Mas os irmãos da Rocha Eterna não me deixaram sozinha nem um dia — vieram orar comigo no hospital, trouxeram comida para minha família, ligavam todos os dias para saber como eu estava.",
"No domingo da Vigília da Colheita, quando o Pastor Renato chamou quem precisava de oração por cura, eu fui até a frente sem forças nem para chorar direito. E ali, naquele momento, senti uma paz que não tenho palavras para explicar. No dia seguinte, os exames vieram completamente normais. O próprio médico ficou surpreso.",
"<blockquote>&ldquo;Pelas suas feridas fomos sarados.&rdquo; — Isaías 53:5</blockquote>",
"Só posso dizer: o Deus que curou ontem é o mesmo hoje. Obrigada, igreja, por terem sido as mãos e os pés de Jesus na minha vida nesses dias. Vera Lúcia.",
]),

dict(date="2019-07-14", title="Iniciando o Estudo de Romanos", category="Estudo Bíblico", author="Pastor Renato Almeida", comments=5,
body=[
"A partir desta quarta-feira, nossas reuniões de meio de semana vão seguir um estudo verso a verso da Carta aos Romanos. É considerada por muitos a carta mais densa teologicamente de todo o Novo Testamento, e acredito que vai edificar muito a vida de cada um de nós.",
"Vamos começar devagar, pelo capítulo 1, entendendo o contexto em que Paulo escreveu essa carta para uma igreja que ele ainda nem conhecia pessoalmente. Tragam seus cadernos de anotação — teremos apostilas simples disponíveis na entrada, sem custo.",
"Todos são bem-vindos, mesmo quem está começando agora na fé. Não é preciso saber nada de teologia, só vontade de aprender.",
]),

dict(date="2019-08-25", title="Bazar Beneficente da Igreja", category="Avisos", author="Irmã Cláudia Freitas", comments=8,
body=[
"No próximo sábado, dia 31, vamos realizar nosso bazar beneficente no pátio da igreja, das 9h às 15h. Toda a renda será revertida para a reforma do telhado do salão infantil, que está precisando de reparos urgentes desde as últimas chuvas.",
"Teremos roupas, calçados, brinquedos, livros e um bazar de comidas com quitutes feitos pelas irmãs — quem quiser contribuir com doações ou com um prato para vender, pode falar com a Irmã Cláudia na secretaria.",
"Contamos com a colaboração de todos, seja doando, comprando, ou simplesmente ajudando na organização e divulgação!",
]),

dict(date="2019-10-06", title="Ministério de Louvor: novos ensaios às quintas", category="Culto", author="Vera Lúcia Nascimento", comments=11,
body=[
"Com muita alegria compartilho que, a partir desta semana, o Ministério de Louvor passa a ensaiar também às quintas-feiras, às 19h30, além do sábado de costume. Sinto que Deus tem me chamado para cuidar com mais carinho desse ministério, e acredito que mais tempo de preparo vai fazer diferença na adoração dos domingos.",
"Se você toca algum instrumento, canta, ou simplesmente tem o desejo de servir ao Senhor através da música, você é muito bem-vindo para vir experimentar. Não precisa ser profissional — precisa ter coração disposto.",
"Estamos trabalhando em três louvores novos para o mês de novembro. Mal posso esperar para compartilhar com todos vocês no culto.",
]),

dict(date="2019-11-24", title="Semana de Consagração: preparando o coração", category="Especial", author="Pastor Renato Almeida", comments=7,
body=[
"De 25 a 29 de novembro realizaremos nossa Semana de Consagração, com cultos todas as noites às 20h. O tema deste ano é &ldquo;Renovando a Aliança&rdquo;, baseado em Josué 24.",
"Escolhemos esse tema pensando justamente no momento em que estamos como igreja: um ano de crescimento, de novas famílias chegando, mas também de rotina se instalando no meio do povo. E é fácil, quando tudo vai bem, esquecer de renovar o compromisso com Deus que fizemos lá no começo.",
"Convido cada família da nossa igreja a separar esses dias, mesmo que seja possível vir apenas em algumas noites. É um tempo precioso de reencontro com Deus antes de encerrarmos mais um ano.",
"Cada noite terá um foco diferente: segunda-feira falaremos sobre renovar o altar familiar; terça, sobre restaurar relacionamentos feridos; quarta será dedicada inteiramente à oração, sem pregação; e quinta trataremos sobre renovar o compromisso com a igreja local.",
"<blockquote>&ldquo;Escolhei hoje a quem sirvais... eu e a minha casa serviremos ao Senhor.&rdquo; — Josué 24:15</blockquote>",
"Teremos ministração especial na sexta-feira, com um convidado da igreja irmã de Suzano. Tragam seus familiares e amigos!",
"Separem a agenda, avisem os parentes, e venham prontos para um tempo de verdadeira renovação. Cremos que Deus tem algo especial reservado para quem se dispuser a buscá-lo nesses cinco dias.",
]),

dict(date="2019-12-22", title="Natal: o Verbo se fez carne", category="Especial", author="Pastor Renato Almeida", comments=10,
body=[
"Em poucos dias celebramos o nascimento de Jesus. Em meio às compras, às ceias e à correria de fim de ano, quero convidar cada um de vocês a parar um instante e lembrar o que realmente estamos celebrando: Deus se fez homem para habitar entre nós.",
"É impressionante pensar que o criador de todas as coisas escolheu entrar na história não como um rei poderoso, cercado de exércitos, mas como um bebê indefeso, nascido numa cidade pequena, de uma família simples, deitado numa manjedoura porque não havia lugar na hospedaria.",
"<blockquote>&ldquo;E o Verbo se fez carne, e habitou entre nós.&rdquo; — João 1:14</blockquote>",
"Esse é o coração do Natal: um Deus que não ficou distante, observando de longe, mas que se aproximou o suficiente para sentir fome, cansaço, dor — para entender, por dentro, o que significa ser humano. E é esse mesmo Deus que hoje entende cada luta que você carrega.",
"Nosso culto de Natal será no dia 24, às 20h, com apresentação especial das crianças da Escola Bíblica Dominical e ceia comunitária logo em seguida. Tragam um prato para compartilhar, se puderem.",
"Convidamos também, especialmente, quem não tem família por perto para passar essa data — ninguém precisa estar sozinho no Natal enquanto a Rocha Eterna existir. Nossa porta, e nossa mesa, estarão abertas.",
"Que o Deus que se fez menino em uma manjedoura encha o coração de cada família da Rocha Eterna de paz nesse Natal.",
]),

dict(date="2020-02-09", title="Campanha do Dízimo Fiel 2020", category="Campanha", author="Diácono Elias Sathler", comments=4,
body=[
"Iniciamos hoje a Campanha do Dízimo Fiel 2020, com o tema &ldquo;Provai-me nisto&rdquo;, baseado em Malaquias 3:10. Ao longo de todo o mês de fevereiro, teremos uma palavra voltada para a mordomia cristã nos cultos de domingo.",
"Sabemos que este é um tema sensível para muitos, e por isso queremos deixar claro: dizimar não é sobre dar para receber algo de volta, mas sobre reconhecer que tudo o que temos vem das mãos de Deus.",
"A tesouraria da igreja publicará, como de costume, o relatório financeiro trimestral no mural de avisos, disponível a qualquer membro que desejar consultar.",
]),

dict(date="2020-03-22", title="Cultos on-line durante este período", category="Avisos", author="Pastor Renato Almeida", comments=19,
body=[
"Diante do agravamento da situação de saúde pública no país, e seguindo as recomendações das autoridades, decidimos em reunião de liderança suspender temporariamente os cultos presenciais na Rocha Eterna.",
"A partir deste domingo, vamos transmitir nosso culto pela internet, no mesmo horário de sempre, às 10h. Sei que não é o ideal — sinto falta de ver o rosto de cada um de vocês, do abraço na entrada, das crianças correndo pelo pátio. Mas a igreja nunca foi um prédio, é o povo de Deus reunido, ainda que à distância.",
"Peço que continuemos firmes em oração uns pelos outros, principalmente pelos irmãos que trabalham na saúde e pelos mais idosos da nossa comunidade. Qualquer necessidade, a diretoria está disponível pelo telefone da secretaria.",
"Vamos atravessar isso juntos, apoiados na certeza de que Deus não nos abandona.",
]),

dict(date="2020-06-14", title="Vera Lúcia assume a coordenação da Escola Bíblica Dominical", category="Avisos", author="Irmã Cláudia Freitas", comments=13,
body=[
"Com muita satisfação anunciamos que a irmã Vera Lúcia Nascimento passa a coordenar, a partir deste mês, a nossa Escola Bíblica Dominical — mesmo em meio aos cultos on-line, as aulas para as crianças e adolescentes continuarão acontecendo por videochamada aos domingos, às 9h.",
"Vera já vem servindo há anos no ministério de louvor e demonstrou, nesse tempo, um cuidado especial com os mais novos da nossa igreja. Temos certeza de que ela vai conduzir esse ministério com a mesma dedicação.",
"Parabéns, Vera, e que Deus continue te capacitando para essa nova responsabilidade!",
]),

dict(date="2020-08-09", title="Vigília de Oração pelas famílias", category="Vigília", author="Vera Lúcia Nascimento", comments=17,
body=[
"Amanhã à noite, das 21h à meia-noite, faremos uma vigília de oração on-line pelas famílias da nossa igreja — especialmente pelas que estão enfrentando dificuldades financeiras, conflitos em casa, ou solidão nesse período tão difícil de isolamento.",
"Este ano tem sido diferente de tudo que já vivemos. Tenho visto, através das aulas da EBD, como as crianças também sentem o peso desse tempo, mesmo sem entender direito o que está acontecendo. Por isso decidi, junto com o Pastor Renato, propor essa vigília voltada especialmente para a restauração do lar.",
"O link de acesso será enviado no grupo da igreja durante a tarde. Separem esse tempo — creio que Deus quer fazer algo profundo em cada família que se dispuser a buscá-lo.",
]),

dict(date="2020-10-18", title="Retorno gradual aos cultos presenciais", category="Avisos", author="Pastor Renato Almeida", comments=21,
body=[
"Depois de meses de cultos exclusivamente on-line, e seguindo todos os protocolos sanitários recomendados, vamos retomar de forma gradual os encontros presenciais a partir do próximo domingo — com capacidade reduzida, uso obrigatório de máscara e álcool em gel na entrada.",
"Sei que é um misto de alegria e cautela. Para quem ainda não se sentir seguro em voltar, ou fizer parte do grupo de risco, a transmissão on-line continuará normalmente, sem nenhum problema. O importante é que ninguém se sinta pressionado.",
"Vamos organizar dois horários de culto (8h e 10h30) para evitar aglomeração. As inscrições, por enquanto, serão feitas pelo grupo da secretaria.",
]),

dict(date="2020-12-20", title="Natal em tempos difíceis", category="Especial", author="Pastor Renato Almeida", comments=12,
body=[
"Este foi, sem dúvida, o ano mais desafiador que a nossa geração já atravessou. Perdemos irmãos queridos, vivemos meses de distanciamento, e ainda assim chegamos ao Natal — e isso, por si só, já é motivo de gratidão.",
"Não vamos fingir, neste texto, que está tudo bem. Muitas famílias da nossa igreja perderam entes queridos neste ano, outras perderam empregos, outras ainda enfrentam solidão como nunca antes. Seria desonesto celebrar o Natal como se nada disso tivesse acontecido.",
"E talvez seja justamente por isso que o primeiro Natal aconteça exatamente no contexto que aconteceu: um povo ocupado, cansado, sob domínio estrangeiro, sem muitas razões concretas para esperança. Foi ali, no meio da escuridão real, que a luz nasceu — não depois que as coisas melhoraram.",
"<blockquote>&ldquo;O povo que andava em trevas viu grande luz.&rdquo; — Isaías 9:2</blockquote>",
"Nosso culto de Natal será híbrido este ano: um pequeno grupo presencial, com todos os protocolos, e transmissão para quem preferir acompanhar de casa. Sei que não é o Natal que gostaríamos de ter, cheio de abraços e salão lotado, mas é o Natal possível — e Deus sabe operar mesmo dentro do possível.",
"Se este ano te deixou mais cansado do que qualquer outro, você não está sozinho nisso, e não precisa fingir força diante da igreja. Que a luz que nasceu em Belém ilumine cada lar da nossa igreja neste fim de ano tão marcado pela dor.",
]),

dict(date="2021-02-14", title="Missão no Vale do Ribeira: relato da viagem", category="Missões", author="Missionária Joana Prado", comments=15,
body=[
"Voltamos ontem à noite da nossa primeira viagem missionária desde o início da pandemia, desta vez para uma pequena comunidade ribeirinha no Vale do Ribeira. Fomos em oito pessoas, levando doações de alimentos, roupas e um pequeno gerador que a igreja ajudou a comprar através de uma vaquinha entre os irmãos.",
"Passamos quatro dias na região, entre pregações ao ar livre, visitas às famílias e um mutirão de reforma na capela local, que estava praticamente destelhada. Foi um tempo de muito aprendizado — recebemos muito mais do que levamos, na simplicidade e na fé daquele povo.",
"Agradeço a cada um que contribuiu financeiramente e em oração para que essa viagem fosse possível. No próximo culto, vamos exibir as fotos e vídeos que trouxemos.",
]),

dict(date="2021-04-04", title="Páscoa 2021: esperança renovada", category="Especial", author="Pastor Renato Almeida", comments=9,
body=[
"Mesmo em meio a um ano ainda tão incerto, celebramos hoje a ressurreição de Cristo com o coração cheio de esperança. Se há uma verdade que a Páscoa nos ensina, é que depois do túmulo mais fechado, Deus ainda tem a última palavra.",
"Tivemos um culto simples nesta manhã, com transmissão on-line para a maior parte da igreja, mas o louvor não foi, de forma alguma, menor do que em anos anteriores. Às vezes até parece que, quanto mais apertadas as circunstâncias, mais alto o povo de Deus aprende a cantar.",
"Pregamos hoje sobre Maria Madalena chorando junto ao túmulo vazio, sem reconhecer, de início, que Jesus estava ali ao seu lado, vivo. Ela estava tão tomada pela dor que confundiu o próprio Senhor com o jardineiro. Quantas vezes, em meio às nossas próprias dores, também deixamos de reconhecer o que Deus já está fazendo bem diante de nós?",
"<blockquote>&ldquo;Jesus lhe disse: Maria! E, voltando-se ela, disse-lhe: Rabôni!&rdquo; — João 20:16</blockquote>",
"Foi bonito ver, mesmo através das telas, comentários de irmãos contando o que Deus tem feito em suas vidas mesmo em meio a um ano tão difícil quanto este: empregos que voltaram, saúde restaurada, famílias reconciliadas depois de meses de distância forçada.",
"Que cada família da Rocha Eterna viva, hoje, a certeza de que os dias difíceis não têm a palavra final sobre nossas vidas. Cristo vive, e por isso, nós também podemos seguir vivendo — com esperança renovada a cada manhã.",
]),

dict(date="2021-05-30", title="Batismo nas águas: sete novos irmãos", category="Batismo", author="Diácono Elias Sathler", comments=18,
body=[
"Foi uma manhã de muita festa! Sete pessoas, entre elas dois adolescentes da nossa EBD, deram esse passo tão importante de fé e foram batizadas nas águas no sítio do irmão Osvaldo, que gentilmente cedeu o espaço mais uma vez.",
"Cada um teve a oportunidade de compartilhar brevemente sua história antes de entrar na água, e não faltaram lágrimas — de alegria — entre quem assistia. Agradecemos a toda a equipe que ajudou na organização, no transporte e no lanche compartilhado depois.",
"Que esses nossos irmãos cresçam firmes na fé que hoje professaram publicamente!",
]),

dict(date="2021-07-18", title="Uma palavra que recebi em oração", category="Estudo Bíblico", author="Vera Lúcia Nascimento", comments=26,
body=[
"Tenho hesitado em escrever este texto há alguns dias, mas sinto que preciso compartilhar o que tenho vivido no meu tempo devocional nas últimas semanas.",
"Tenho buscado o Senhor de um jeito diferente ultimamente — mais silêncio, menos pressa. E nesse processo, tenho sentido que Deus está me chamando para um tempo à parte, um recomeço que ainda não sei explicar direito com palavras. Não é nada dramático, só uma inquietação que reconheço, pela experiência destes anos na igreja, que não posso ignorar.",
"<blockquote>&ldquo;Combati o bom combate, terminei a corrida, guardei a fé.&rdquo; — Salmos 145:23</blockquote>",
"Peço que orem comigo nesse processo. Vou conversar com o Pastor Renato nas próximas semanas sobre o que isso significa na prática. Por ora, só sinto que preciso ser obediente ao que tenho ouvido.",
]),

dict(date="2021-08-30", title="Retiro de silêncio: partindo em busca de mais", category="Avisos", author="Vera Lúcia Nascimation" if False else "Vera Lúcia Nascimento", comments=31,
body=[
"Depois de conversar bastante com o Pastor Renato e com minha família, decidi seguir para um tempo de retiro de silêncio no interior, num espaço de retiro que uma amiga de outra igreja me indicou. Não é uma despedida — é uma pausa que sinto que preciso, depois de tantos anos servindo sem parar de verdade.",
"Vou ficar afastada das redes e do blog por um tempo que ainda não sei precisar. A coordenação da EBD fica, por enquanto, sob os cuidados da Irmã Cláudia, que já vem me acompanhando nos últimos meses.",
"Obrigada por tantos anos de caminhada juntos. Levo cada um de vocês no coração.",
"<blockquote>&ldquo;Buscai ao Senhor enquanto se pode achar.&rdquo; — Provérbios 31:32</blockquote>",
"Vera.",
]),

dict(date="2021-09-12", title="Sentimos a falta da irmã Vera", category="Avisos", author="Irmã Cláudia Freitas", comments=34,
hidden_comment="Se voce está lendo isto, procure onde a luz não chega às sextas-feiras.",
body=[
"Muitos de vocês têm perguntado pela irmã Vera Lúcia, e por isso escrevo este pequeno aviso.",
"Como alguns sabem, ela partiu no fim de agosto para um tempo de retiro espiritual no interior. Não temos, no momento, muitos detalhes sobre quando ela deve retornar — apenas pedimos que continuemos cobrindo-a em oração, confiando que Deus está cuidando de cada passo dela nesse processo.",
"A Escola Bíblica Dominical continua funcionando normalmente aos cuidados da nossa equipe. Qualquer notícia que tivermos, compartilharemos com a igreja.",
]),

dict(date="2021-11-01", title="Continuamos orando pelos que caminham longe", category="Estudo Bíblico", author="Pastor Renato Almeida", comments=20,
body=[
"Na reunião de quarta-feira, refletimos sobre a parábola do filho pródigo e sobre como Deus nunca desiste de nenhum de nós, mesmo quando escolhemos caminhos que Ele não traçou.",
"Tenho pensado bastante nessa parábola nas últimas semanas. Como igreja, nosso papel não é cobrar ou julgar quem se afasta, mas manter a porta e o coração abertos, como o pai da história, esperando com esperança.",
"<blockquote>&ldquo;Porque este meu filho estava morto, e reviveu; se havia perdido, e é achado.&rdquo; — Isaías 66:25</blockquote>",
"Continuamos orando por todos os irmãos que, por diferentes razões, estão hoje distantes da nossa comunhão. Que cada um encontre o caminho de volta para casa, no tempo certo.",
]),

dict(date="2022-04-17", title="Páscoa 2022", category="Especial", author="Pastor Renato Almeida", comments=8,
body=[
"Celebramos hoje mais uma Páscoa já com o salão praticamente cheio, algo que não víamos desde antes da pandemia. Foi emocionante ver tantos rostos conhecidos e também vários visitantes que vieram pela primeira vez.",
"Depois de dois anos tão marcados por distância — cultos on-line, máscaras, cadeiras espaçadas — havia algo quase palpável no ar hoje de manhã: a alegria simples de estarmos, finalmente, todos juntos outra vez, sem restrição, cantando lado a lado.",
"O culto de hoje trouxe um convite simples: assim como a pedra foi removida do túmulo, Deus também remove as pedras que insistimos em carregar sozinhos. Ninguém precisa atravessar suas lutas em isolamento — é para isso que existe a igreja.",
"<blockquote>&ldquo;E, olhando, viram que a pedra, que era muito grande, já estava removida.&rdquo; — Marcos 16:4</blockquote>",
"Pregamos sobre como, no relato de Marcos, as mulheres já estavam a caminho do túmulo se perguntando quem removeria a pedra para elas — sem saber que, quando chegassem, o problema já estaria resolvido. Muitas vezes gastamos energia demais nos preocupando com pedras que Deus já decidiu remover antes mesmo de sabermos.",
"Tivemos também, ao final do culto, um pequeno momento de recepção para as famílias que chegaram à igreja nos últimos meses — já são doze novas famílias só neste ano, um sinal claro de que Deus continua trazendo gente para o nosso meio, mesmo depois de um período tão difícil.",
"Agradecemos a equipe de recepção e de louvor pelo empenho nesta manhã tão especial.",
]),

dict(date="2022-07-03", title="Ainda oramos por ela", category="Avisos", author="Irmã Cláudia Freitas", comments=29,
hidden_comment="Rua das Acácias, 214 - fundos.",
body=[
"Já se passou quase um ano desde que a irmã Vera Lúcia partiu para seu tempo de retiro, e algumas pessoas ainda perguntam sobre ela na secretaria, então decidimos escrever este breve aviso.",
"Não temos novidades concretas para compartilhar. O que podemos dizer é que a liderança da igreja continua em contato com a família dela e que seguimos, como sempre dissemos, de portas e corações abertos.",
"<blockquote>&ldquo;O Senhor é o meu pastor, nada me faltará.&rdquo; — Salmos 23:9</blockquote>",
"Pedimos que continuem orando, mesmo sem saber todos os detalhes. Às vezes a fé é justamente isso: confiar mesmo no que não entendemos por completo.",
]),

dict(date="2022-11-20", title="Ceia de Ação de Graças da Igreja", category="Avisos", author="Diácono Elias Sathler", comments=6,
body=[
"No sábado, dia 26, teremos nossa tradicional Ceia de Ação de Graças, às 19h, no salão social. Cada família deve trazer um prato para compartilhar — a organização das mesas está disponível com os diáconos na entrada.",
"Este ano queremos reservar um momento especial para que os irmãos compartilhem, brevemente, um motivo de gratidão do ano que se encerra. Já temos mais de vinte famílias confirmadas.",
"Contamos com a presença de todos para fechar o ano juntos, como igreja e como família.",
]),

dict(date="2023-03-05", title="Um ano e meio depois", category="Estudo Bíblico", author="Pastor Renato Almeida", comments=24,
body=[
"Tenho evitado, ao longo destes meses, transformar este espaço num lugar de especulação sobre a ausência da irmã Vera. Mas alguns membros mais novos da igreja ainda não conhecem a história completa, e sinto que uma palavra é devida.",
"O que sei, e posso compartilhar com tranquilidade, é que ela partiu em paz, por decisão própria, buscando algo que sentia que precisava naquele momento da vida dela. A igreja respeitou essa decisão então, e respeita até hoje.",
"<blockquote>&ldquo;Não temas, porque eu sou contigo; não te assombres, porque eu sou o teu Deus.&rdquo; — João 21:26</blockquote>",
"Seguimos de portas abertas, como sempre estivemos. E seguimos, sobretudo, confiando que o mesmo Deus que cuidou de cada um de nós até aqui continua cuidando dela, onde quer que esteja.",
]),

dict(date="2024-05-12", title="Dia das Mães na Rocha Eterna", category="Especial", author="Irmã Cláudia Freitas", comments=11,
body=[
"Neste domingo homenageamos todas as mães da nossa igreja com um culto especial, seguido de um café da manhã reforçado preparado pelos próprios homens da igreja — como já é tradição há alguns anos.",
"A decoração deste ano ficou por conta das próprias adolescentes da igreja, que passaram a tarde de sábado enfeitando o salão com flores de papel e faixas escritas à mão. O capricho de cada detalhe já valia a homenagem por si só.",
"Cada mãe presente recebeu uma lembrancinha feita pelas crianças da Escola Bíblica Dominical, e tivemos um momento emocionante de oração por todas as mães, inclusive as que já partiram e as que ainda esperam para ser mães um dia.",
"<blockquote>&ldquo;Muitas mulheres procederam virtuosamente; porém tu a todas sobrepujas.&rdquo; — Provérbios 31:29</blockquote>",
"Convidamos três mães da igreja para compartilhar brevemente sua caminhada — uma delas, mãe de primeira viagem depois de anos de espera, emocionou o salão inteiro ao testemunhar sobre a longa jornada até a chegada do seu bebê.",
"Foi uma manhã de muito carinho e gratidão. Deus abençoe cada mãe da nossa comunidade!",
]),

dict(date="2024-12-24", title="Véspera de Natal: uma luz na escuridão", category="Especial", author="Pastor Renato Almeida", comments=13,
body=[
"Mais um ano se encerra, e nos reunimos hoje à noite para celebrar o nascimento daquele que é chamado &ldquo;Deus Conosco&rdquo;. Foi uma noite bonita, com o salão decorado pelas próprias famílias da igreja e uma apresentação linda das crianças.",
"Chegamos cedo para os últimos preparativos, e o cheiro de canela e cravo das ceias que as irmãs já começavam a organizar na cozinha tomava conta de todo o salão antes mesmo do culto começar. São esses detalhes simples que fazem o Natal da Rocha Eterna ter cara de família.",
"<blockquote>&ldquo;E a luz resplandece nas trevas, e as trevas não prevaleceram contra ela.&rdquo; — João 1:5</blockquote>",
"Pregamos hoje sobre como a primeira notícia do nascimento de Jesus não foi dada a reis ou sacerdotes, mas a pastores simples, no meio da noite, cuidando do próprio rebanho. Deus continua, até hoje, se revelando primeiro aos simples e aos que estão vigiando, e não necessariamente aos mais importantes.",
"Encerramos com a tradicional troca de velas: cada família acendeu sua vela a partir da vela do altar, até que o salão inteiro estivesse iluminado apenas por essas pequenas chamas — uma imagem bonita de como a luz de Cristo se espalha, pessoa a pessoa.",
"Que essa luz ilumine cada canto escuro que ainda carregamos — nossas famílias, nossas cidades, e sim, também aqueles que caminham longe da nossa comunhão neste momento. Feliz Natal, igreja!",
]),

dict(date="2025-06-08", title="Cinco anos de Ministério de Louvor", category="Culto", author="Jovem Lucas Ferreira", comments=16,
hidden_comment="As citações erradas não foram um erro. Junte os números.",
body=[
"Quem começou no ministério de louvor faz pouco tempo talvez não saiba, mas foi a irmã Vera Lúcia quem lançou as bases do ministério como ele é hoje, lá em 2019, quando propôs os ensaios extras de quinta-feira.",
"Passados quase quatro anos desde a última vez que tivemos notícias diretas dela, o ministério que ela ajudou a construir segue firme, hoje com dezoito integrantes entre músicos e vocais, e uma escala que cobre os dois cultos de domingo sem falhar um só final de semana.",
"Decidimos, neste mês, dedicar um dos nossos ensaios para revisar as anotações antigas dela, que a Irmã Cláudia guardou todos esses anos numa pasta na secretaria. Encontramos ali letras, acordes rabiscados e também alguns bilhetes pessoais de oração que preferimos manter guardados, com respeito.",
"Onde quer que você esteja, Vera: obrigado. O que você começou continua de pé.",
]),

dict(date="2026-07-19", title="Reflexões para o segundo semestre", category="Estudo Bíblico", author="Pastor Renato Almeida", comments=5,
body=[
"Chegamos à metade de 2026 e, como igreja, é sempre bom parar um instante para olhar o caminho percorrido e o que ainda temos pela frente. Muita coisa mudou na Rocha Eterna nestes últimos anos — crescemos em número, reformamos o salão, enviamos novas famílias para plantar outras igrejas na região.",
"Para o segundo semestre, vamos iniciar um novo ciclo de estudos sobre os dons espirituais, além de retomar as vigílias mensais que ficaram pausadas no início do ano por causa da reforma do telhado.",
"Seguimos firmes no propósito de sempre: ser uma comunidade de fé, cura e restauração para quem quer que Deus traga até nós — hoje, e nos anos que ainda virão.",
]),
]

# ---------------------------------------------------------------------------
# RECURRING ANNUAL POSTS (Jejum de Daniel, Semana Santa, Páscoa, Pentecostes,
# Dia das Mães, Dia dos Pais, Dia da Reforma, Virada de Ano) — generated
# programmatically for every applicable year so every Christian-calendar
# date in the church year is covered, 2019-2026.
# ---------------------------------------------------------------------------
import datetime as _dt
import calendar as _cal

TODAY = _dt.date(2026, 7, 31)
BLOG_START = _dt.date(2019, 3, 10)

EASTER = {  # Western Easter Sunday, real dates
    2019: _dt.date(2019, 4, 21), 2020: _dt.date(2020, 4, 12),
    2021: _dt.date(2021, 4, 4),  2022: _dt.date(2022, 4, 17),
    2023: _dt.date(2023, 4, 9),  2024: _dt.date(2024, 3, 31),
    2025: _dt.date(2025, 4, 20), 2026: _dt.date(2026, 4, 5),
}

def _nth_weekday(year, month, weekday, n):
    """n-th (1-indexed) given weekday (0=Mon..6=Sun) of a month."""
    c = _cal.Calendar()
    days = [d for d in c.itermonthdates(year, month) if d.month == month and d.weekday() == weekday]
    return days[n - 1]

YEAR_NOTE = {
2019: "Este ano marcou o início deste blog e uma fase de crescimento constante para a nossa igreja, ainda pequena mas cheia de vida.",
2020: "Vivemos boa parte deste ano à distância, com as reuniões acontecendo por transmissão on-line por causa da pandemia — e mesmo assim, Deus continuou trabalhando no meio de nós.",
2021: "Foi um ano de muitas mudanças na igreja, inclusive com a partida da irmã Vera Lúcia para seu tempo de retiro no fim de agosto, algo que ainda sentimos no meio de nós.",
2022: "Já em recuperação plena dos anos mais difíceis da pandemia, vimos a igreja crescer em número e em profundidade espiritual, mesmo guardando no coração a ausência de quem caminhou longe.",
2023: "Um ano de reformas físicas no salão social e também de reafirmação, como igreja, do nosso compromisso com a Palavra e com a comunhão uns com os outros.",
2024: "Um ano de estabilidade e de novas famílias se somando à Rocha Eterna, sinal de que Deus continua trazendo gente para o nosso meio.",
2025: "Já são quase quatro anos desde a partida da irmã Vera, e seguimos, como sempre dissemos, de portas e coração abertos.",
2026: "Seguimos firmes neste novo ano, com o coração voltado para o que Deus ainda quer fazer no meio do nosso povo.",
}

ATTEND_BASE = {2019: 60, 2020: 35, 2021: 50, 2022: 90, 2023: 110, 2024: 130, 2025: 145, 2026: 150}

AUTHORS_BY_ERA = {
"jejum": "Pastor Renato Almeida",
"semana-santa": "Pastor Renato Almeida",
"pascoa": "Pastor Renato Almeida",
"pentecostes": "Vera Lúcia Nascimento",
"maes": "Irmã Cláudia Freitas",
"pais": "Diácono Elias Sathler",
"reforma": "Pastor Renato Almeida",
"virada": "Pastor Renato Almeida",
}

def _author_for(theme, year):
    if theme == "pentecostes":
        if year <= 2020:
            return "Vera Lúcia Nascimento"
        elif year <= 2024:
            return "Pastor Renato Almeida"
        else:
            return "Jovem Lucas Ferreira"
    return AUTHORS_BY_ERA[theme]

def _comment_count(theme, year):
    base = ATTEND_BASE[year] // 6
    bump = {"pascoa": 6, "virada": 5, "reforma": -3, "jejum": -2, "pentecostes": 2}.get(theme, 0)
    return max(4, base + bump)

RECURRING = []

def add_recurring(date, title, category, theme):
    if date < BLOG_START or date > TODAY:
        return
    RECURRING.append(dict(
        date=date.isoformat(), title=title, category=category,
        author=_author_for(theme, date.year), comments=_comment_count(theme, date.year),
        body=_theme_body(theme, date.year),
    ))

def _theme_body(theme, year):
    note = YEAR_NOTE[year]
    n = ATTEND_BASE[year]
    if theme == "jejum":
        return [
        "Como já é tradição na Rocha Eterna, iniciamos neste mês os 21 dias do Jejum de Daniel — um tempo de consagração baseado em Daniel 10, quando o profeta se absteve de carnes e guloseimas por três semanas enquanto buscava uma resposta do Senhor.",
        "Cada família participa do jeito que consegue: alguns optam por retirar carnes e doces da alimentação, outros escolhem um jejum parcial de determinados horários do dia, e há quem prefira jejuar de redes sociais e entretenimento. O importante, sempre reforçamos, não é a forma exata, mas o coração voltado para Deus.",
        "Durante essas três semanas, teremos encontros de oração todas as terças e quintas-feiras, às 19h30, além de um grupo no aplicativo de mensagens para compartilharmos versículos e pedidos de oração diariamente.",
        "<blockquote>&ldquo;Não comi manjar desejável, nem carne nem vinho entraram na minha boca, nem me untei com óleo, até que se cumpriram as três semanas inteiras.&rdquo; — Daniel 10:3</blockquote>",
        f"Neste ano, já contamos com cerca de {n} pessoas inscritas para acompanhar o jejum em algum formato — um número que só cresce a cada ano, e que mostra a fome espiritual do nosso povo.",
        note,
        "Que estas três semanas sejam de fato um tempo separado para buscarmos a Deus com mais intensidade, preparando o coração para tudo o que Ele quer fazer neste novo ano que se inicia.",
        ]
    if theme == "semana-santa":
        return [
        "Entramos esta semana na Semana Santa, os dias que antecedem a maior celebração do calendário cristão. Teremos reflexões todas as noites, de segunda a sexta, às 20h, cada uma voltada para um aspecto da paixão de Cristo.",
        "Na quinta-feira, seguindo a tradição, faremos uma cerimônia simples de lava-pés, relembrando o exemplo de serviço que Jesus deixou aos discípulos na última ceia. É sempre um momento de muita quebrantamento no meio da igreja.",
        "Já a sexta-feira será dedicada inteiramente à cruz — um culto mais silencioso, sem os louvores animados de costume, para contemplarmos com seriedade o preço que foi pago por nós.",
        "<blockquote>&ldquo;Mas ele foi ferido pelas nossas transgressões, e moído pelas nossas iniquidades.&rdquo; — Isaías 53:5</blockquote>",
        "Convidamos cada família a separar essa semana, mesmo que a rotina esteja corrida. São poucos dias no ano em que paramos de verdade para olhar para a cruz antes de celebrarmos a ressurreição no domingo.",
        note,
        ]
    if theme == "pascoa":
        return [
        "Chegamos ao domingo mais importante do calendário cristão: o dia em que celebramos que a morte não teve a última palavra sobre Jesus — e, por extensão, também não tem sobre nós.",
        f"O salão estava especialmente cheio nesta manhã, com muitos visitantes trazidos por membros da igreja. Contabilizamos cerca de {n} pessoas presentes entre os dois horários de culto.",
        "As crianças da Escola Bíblica Dominical apresentaram uma pequena dramatização sobre o túmulo vazio, e não faltaram lágrimas — de alegria — entre os pais que assistiam.",
        "<blockquote>&ldquo;Por que buscais entre os mortos aquele que vive? Não está aqui, mas ressuscitou.&rdquo; — Lucas 24:5-6</blockquote>",
        "Se você carrega hoje algum &ldquo;túmulo fechado&rdquo; em sua vida — um sonho que parece morto, um relacionamento que parece sem solução, uma dor que insiste em não passar — a mensagem da Páscoa é simples e poderosa: o mesmo Deus que reverteu o maior de todos os fins ainda está no controle do seu recomeço.",
        note,
        "Que a certeza da ressurreição sustente cada família da Rocha Eterna até a próxima vez que nos reunirmos.",
        ]
    if theme == "pentecostes":
        return [
        "Hoje celebramos o Domingo de Pentecostes, cinquenta dias após a Páscoa — a data em que relembramos a descida do Espírito Santo sobre os discípulos reunidos no cenáculo, conforme relata Atos capítulo 2.",
        "Como igreja que cremos e vivemos o batismo no Espírito Santo como uma experiência atual, este é sempre um dos cultos mais fortes do nosso calendário. Tivemos um tempo estendido de louvor e ministração no altar, com muitas pessoas buscando uma experiência renovada com o Espírito.",
        "Vimos, mais uma vez, manifestações visíveis da presença de Deus — louvor espontâneo, línguas estranhas, palavras proféticas ministradas com cuidado e testadas à luz da Palavra, como sempre orientamos.",
        "<blockquote>&ldquo;E todos foram cheios do Espírito Santo, e começaram a falar em outras línguas, conforme o Espírito lhes concedia que falassem.&rdquo; — Atos 2:4</blockquote>",
        "Para quem talvez ainda não tenha vivido essa experiência: ela não é reservada a poucos &ldquo;espirituais&rdquo; demais. A promessa do Pai é, segundo a própria Escritura, para todo aquele que crê e busca.",
        note,
        "Seguimos cremos que o mesmo Espírito que capacitou a igreja primitiva continua disponível, hoje, para capacitar a Rocha Eterna a viver e anunciar o evangelho com poder.",
        ]
    if theme == "maes":
        return [
        "Neste domingo separamos um momento especial do culto para homenagear todas as mães da nossa igreja — as que já criaram seus filhos, as que ainda estão nessa caminhada, e também aquelas que, mesmo sem filhos biológicos, exercem um papel maternal na vida de tantos aqui dentro.",
        "Como já é tradição, os homens da igreja prepararam um café da manhã reforçado para recebê-las antes do culto, e as crianças da Escola Bíblica Dominical entregaram lembrancinhas feitas à mão durante a semana.",
        "Tivemos um momento de oração coletiva por todas as mães presentes, e também — com muito cuidado — por aquelas que enfrentam a maternidade em meio a dificuldades, ou que ainda esperam para ser mães um dia.",
        "<blockquote>&ldquo;Muitas mulheres procederam virtuosamente; porém tu a todas sobrepujas.&rdquo; — Provérbios 31:29</blockquote>",
        "É sempre uma manhã de muito carinho na Rocha Eterna. Agradecemos a cada mãe que, com paciência e amor, tem moldado a próxima geração da nossa igreja.",
        note,
        ]
    if theme == "pais":
        return [
        "Neste domingo foi a vez de homenagearmos os pais da nossa igreja, com um culto mais leve e descontraído, seguido de um almoço de confraternização no pátio.",
        "Convidamos alguns dos pais mais antigos da igreja para compartilhar, brevemente, uma palavra sobre o que aprenderam ao longo dos anos criando seus filhos na fé — foram testemunhos simples, mas que tocaram bastante o coração de todos.",
        "Também oramos por aqueles que enfrentam a paternidade sozinhos, pelos que sonham em ser pais um dia, e pelos que, por algum motivo, vivem hoje distantes de seus filhos.",
        "<blockquote>&ldquo;Como um pai se compadece de seus filhos, assim o Senhor se compadece daqueles que o temem.&rdquo; — Salmos 103:13</blockquote>",
        "Que cada pai da Rocha Eterna continue sendo, na sua casa, um reflexo — ainda que imperfeito — do cuidado do nosso Pai celestial.",
        note,
        ]
    if theme == "reforma":
        return [
        "Hoje, 31 de outubro, relembramos o Dia da Reforma Protestante — a data em que, em 1517, o monge Martinho Lutero afixou suas 95 teses na porta da igreja de Wittenberg, questionando práticas da igreja da época e resgatando verdades bíblicas que haviam sido, de certa forma, deixadas de lado.",
        "Como igreja evangélica, somos herdeiros diretos daquele movimento — em especial de dois princípios que seguimos até hoje: que a salvação vem pela graça, mediante a fé, e não por méritos próprios; e que a Bíblia, e não a tradição humana, é a nossa autoridade máxima.",
        "<blockquote>&ldquo;Porque pela graça sois salvos, por meio da fé; e isto não vem de vós, é dom de Deus.&rdquo; — Efésios 2:8</blockquote>",
        "Na reunião de quarta-feira desta semana, fizemos um breve resgate histórico da Reforma e conversamos sobre como esses princípios, descobertos há mais de 500 anos, ainda moldam a forma como lemos a Bíblia e vivemos a fé hoje.",
        "Vale lembrar: a Reforma não foi um evento único e encerrado — é um lembrete permanente de que a igreja sempre precisa voltar às Escrituras, examinar suas próprias tradições, e se deixar corrigir por elas quando necessário.",
        note,
        ]
    if theme == "virada":
        return [
        f"Mais um ano se encerra, e nos reunimos hoje à noite para o nosso tradicional Culto de Virada, que vai até a meia-noite, atravessando {year} e entrando em {year+1} já em oração.",
        "Cada família que quis teve a oportunidade de compartilhar, brevemente, um motivo de gratidão dos últimos doze meses — e, como sempre acontece, ouvimos histórias de cura, provisão financeira, restauração de relacionamentos e também de perseverança em meio a dificuldades que não foram resolvidas, mas atravessadas com fé.",
        "<blockquote>&ldquo;As misericórdias do Senhor são a causa de não sermos consumidos, porque as suas misericórdias não têm fim; renovam-se cada manhã.&rdquo; — Lamentações 3:22-23</blockquote>",
        note,
        f"Encerramos o ano com uma certeza simples, mas que sustenta a Rocha Eterna desde 2013: o mesmo Deus que foi fiel em {year} será fiel também no ano que se inicia. Feliz Ano Novo, igreja!",
        ]
    return []

for _y in range(2019, 2027):
    add_recurring(_dt.date(_y, 1, 6), f"Jejum de Daniel {_y}: 21 dias de busca", "Especial", "jejum")
    add_recurring(EASTER[_y] - _dt.timedelta(days=6), f"Semana Santa {_y}: os dias que antecedem a cruz", "Especial", "semana-santa")
    add_recurring(EASTER[_y] + _dt.timedelta(days=49) - (_dt.timedelta(days=1) if _y == 2025 else _dt.timedelta(days=0)),
                  f"Pentecostes {_y}: o batismo no Espírito Santo", "Culto", "pentecostes")
    add_recurring(_nth_weekday(_y, 8, 6, 2), f"Dia dos Pais {_y}", "Especial", "pais")
    add_recurring(_dt.date(_y, 10, 31), f"Dia da Reforma {_y}: relembrando as 95 teses", "Estudo Bíblico", "reforma")
    add_recurring(_dt.date(_y, 12, 31), f"Culto de Virada: encerrando {_y}", "Vigília", "virada")
    if _y != 2024:
        add_recurring(_nth_weekday(_y, 5, 6, 2), f"Dia das Mães {_y}", "Especial", "maes")

for _y in (2020, 2023, 2024, 2025, 2026):
    add_recurring(EASTER[_y], f"Páscoa {_y}", "Especial", "pascoa")

POSTS.extend(RECURRING)
POSTS.sort(key=lambda p: p["date"])

PAGES_NAV = [
    ("index.html", "Início"),
    ("sobre-nos.html", "Sobre Nós"),
    ("nossa-missao.html", "Nossa Missão"),
    ("lideranca.html", "Liderança"),
    ("arquivo.html", "Arquivo"),
    ("contato.html", "Contato"),
]

print(f"Loaded {len(POSTS)} posts.")

# ---------------------------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------------------------

LOGO_SVG = """<svg class="site-logo" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
<circle cx="32" cy="32" r="30" fill="#f2e9d8" stroke="#7a2e2e" stroke-width="2"/>
<rect x="29" y="14" width="6" height="36" fill="#7a2e2e"/>
<rect x="16" y="24" width="32" height="6" fill="#7a2e2e"/>
</svg>"""

def nav_html(active):
    lis = []
    for href, label in PAGES_NAV:
        lis.append(f'<li><a href="{"/" + href if href != "index.html" else "/"}">{label}</a></li>')
    return "<ul>" + "".join(lis) + "</ul>"

def sidebar_html(depth_prefix=""):
    years = {}
    for p in POSTS:
        y = p["date"][:4]
        years.setdefault(y, 0)
        years[y] += 1
    year_items = "".join(
        f'<li><a href="{depth_prefix}arquivo.html#{y}">{y} ({years[y]} postagens)</a></li>'
        for y in sorted(years.keys(), reverse=True)
    )
    popular = sorted(POSTS, key=lambda p: p["comments"], reverse=True)[:5]
    popular_items = "".join(
        f'<li><a href="{depth_prefix}posts/{slugify(p["title"])}.html">{p["title"]}</a></li>'
        for p in popular
    )
    return f"""<aside class="sidebar">
  <div class="widget">
    <h2>Sobre o blog</h2>
    <div class="widget-body">
      <p>Este e o espaco oficial da <strong>Comunidade Crista Rocha Eterna</strong> na internet. Aqui compartilhamos avisos, estudos, testemunhos e tudo o que Deus tem feito no meio do nosso povo desde 2019.</p>
    </div>
  </div>
  <div class="widget">
    <h2>Versiculo da semana</h2>
    <div class="widget-body verse-box">
      "Porque eu bem sei os pensamentos que tenho a vosso respeito, diz o Senhor; pensamentos de paz, e nao de mal, para vos dar o fim que esperais."
      <span class="verse-ref">Jeremias 29:11</span>
    </div>
  </div>
  <div class="widget">
    <h2>Postagens populares</h2>
    <div class="widget-body"><ul>{popular_items}</ul></div>
  </div>
  <div class="widget">
    <h2>Arquivo do blog</h2>
    <div class="widget-body"><ul>{year_items}</ul></div>
  </div>
  <div class="widget">
    <h2>Visitantes</h2>
    <div class="widget-body" style="text-align:center;">
      <span class="counter">003841</span>
      <p style="margin-top:8px; font-size:11px; color:#8a7a5c;">desde 10/03/2019</p>
    </div>
  </div>
</aside>"""

def page_shell(title, active, body_html, depth_prefix="", extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - Comunidade Crista Rocha Eterna</title>
<meta name="description" content="Blog oficial da Comunidade Crista Rocha Eterna.">
<link rel="stylesheet" href="{depth_prefix}css/style.css">
{extra_head}</head>
<body>
<header class="site-header">
  <div class="header-inner">
    {LOGO_SVG}
    <div class="site-title-block">
      <h1>Comunidade Crista Rocha Eterna</h1>
      <p>"Um lugar de fe, familia e restauracao"</p>
    </div>
  </div>
</header>
<nav class="site-nav">{nav_html(active)}</nav>
<div class="content-wrap">
  <main class="posts-column">
    {body_html}
  </main>
  {sidebar_html(depth_prefix)}
</div>
<footer class="site-footer">
  <p>Comunidade Crista Rocha Eterna &mdash; Rua das Palmeiras, 482, Jardim Esperanca<br>
  Cultos aos domingos, 9h e 10h30 &middot; Estudo biblico as quartas, 20h</p>
  <p>&copy; 2019-2026 Comunidade Crista Rocha Eterna. Feito com carinho e fe.</p>
</footer>
</body>
</html>"""

import hashlib

COMMENTER_NAMES = [
"Marlene Aparecida", "Zé Carlos", "Rosa Helena", "Sebastião Nunes", "Neuza Aparecida",
"Osvaldo Pereira", "Terezinha Souza", "Aparecida Lima", "Benedito Ferreira", "Ivone Cardoso",
"Geraldo Bispo", "Conceição Alves", "Waldemar Sathler", "Dulce Maria", "Antônio Ribeiro",
"Creuza dos Santos", "Joaquim Batista", "Lourdes Martins", "Edvaldo Costa", "Zenaide Rocha",
"Nilza Barbosa", "Reginaldo Prado", "Vanda Freitas", "Adalberto Nunes", "Iracema Gomes",
"Cícero Almeida", "Sonia Regina", "Valdir Souza", "Marlete Cordeiro", "Amauri José",
]

COMMENT_TEXTS = [
"Amém!!! Deus continue abençoando a nossa igreja.",
"Glória a Deus por essa palavra! Foi exatamente o que eu precisava ouvir hoje.",
"Que bênção, Pastor! Deus abençoe grandemente.",
"Amém e amém! Estava lá e foi realmente especial.",
"Deus é fiel! Amém irmãos, vamos em frente.",
"Fiquei muito emocionada lendo isso. Deus abençoe a todos vocês.",
"Parabéns pela postagem, que Deus continue no controle de tudo.",
"Amém, Senhor! Glória ao Seu nome.",
"Que Deus continue usando essa igreja de forma tão poderosa. Amém!",
"Muito abençoador, obrigada por compartilhar!",
"Deus abençoe ricamente a vida de cada um que participou.",
"Amém! Ficarei orando também.",
"Que maravilha, Deus é maravilhoso em tudo o que faz. Amém!",
"Estava ali e posso confirmar, foi um culto poderoso demais.",
"Só posso dizer amém e glória a Deus pela nossa igreja.",
"Muito boa a reflexão, Deus continue abençoando o ministério de vocês.",
"Amém! Que o Senhor continue guiando os passos da Rocha Eterna.",
"Emocionante like sempre. Deus abençoe a todos.",
"Glória a Deus, li e já orei junto. Amém irmãos.",
"Deus é tremendo! Obrigada por compartilhar essa bênção com a gente.",
"Amém, que venham mais momentos assim!",
"Fiquei com o coração quentinho lendo essa postagem. Deus abençoe.",
"Que o Senhor continue derramando as Suas bênçãos sobre essa igreja. Amém!",
"Muito bom! Deus é bom o tempo todo, e o tempo todo Deus é bom.",
"Amém, Pastor! Sempre uma palavra na hora certa.",
"Que Deus continue te usando, Vera! Sentimos sua falta no ministério. (comentário antigo)",
"Glória a Deus, esperando ansiosa pelo próximo culto.",
"Amém, essa igreja é uma benção na minha vida e da minha família.",
"Muito lindo esse relato, Deus seja louvado!",
"Deus abençoe a liderança e cada obreiro envolvido. Amém!",
]

def _seeded_rng(seed_text):
    h = hashlib.sha256(seed_text.encode('utf-8')).hexdigest()
    return int(h, 16)

def get_comments(slug, count):
    shown = min(count, 8)
    seed = _seeded_rng(slug)
    names_idx = [(seed >> (i * 5)) % len(COMMENTER_NAMES) for i in range(shown)]
    texts_idx = [(seed >> (i * 7 + 3)) % len(COMMENT_TEXTS) for i in range(shown)]
    day_offsets = sorted([1 + ((seed >> (i * 3 + 1)) % 6) for i in range(shown)])
    comments = []
    for i in range(shown):
        comments.append((COMMENTER_NAMES[names_idx[i]], COMMENT_TEXTS[texts_idx[i]], day_offsets[i]))
    return comments

def render_comments(p):
    count = p["comments"]
    comments = get_comments(slugify(p["title"]), count)
    base_date = _dt.date.fromisoformat(p["date"])
    items = []
    for name, text, offset in comments:
        cdate = base_date + _dt.timedelta(days=offset)
        items.append(f"""<div class="comment-item">
      <div class="comment-meta"><strong>{name}</strong> &middot; {fmt_date(cdate.isoformat())}</div>
      <div class="comment-text">{text}</div>
    </div>""")
    more = count - len(comments)
    more_line = f'<p class="comments-more">+ {more} outros comentários</p>' if more > 0 else ""
    return f"""<section class="comments-section">
  <h2>{count} comentários</h2>
  {''.join(items)}
  {more_line}
</section>"""

def render_post(p, idx):
    slug = slugify(p["title"])
    body = "\n".join(f"<p>{para}</p>" if not para.strip().startswith("<blockquote") else para for para in p["body"])
    hidden = f"\n<!-- {b64(p['hidden_comment'])} -->\n" if p.get("hidden_comment") else ""
    body_html = f"""<article class="post">
  <h1 class="post-title">{p['title']}</h1>
  <div class="post-meta"><span class="tag">{p['category']}</span> Publicado por {p['author']} em {fmt_date(p['date'])}</div>
  <div class="post-body">
    {body}
  </div>{hidden}
  <div class="post-footer"><span>{p['comments']} comentarios</span><span><a href="../index.html">&laquo; Voltar ao inicio</a></span></div>
</article>
{render_comments(p)}"""
    html = page_shell(p["title"], "posts", body_html, depth_prefix="../")
    with open(os.path.join(POSTS_DIR, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    return slug

def excerpt(p, n=220):
    text = re.sub('<[^<]+?>', '', " ".join(p["body"]))
    text = text.replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&mdash;", "-")
    return (text[:n] + "...") if len(text) > n else text

def render_index(slugs):
    latest = list(reversed(POSTS))[:10]
    cards = []
    for p in latest:
        slug = slugify(p["title"])
        cards.append(f"""<article class="post">
  <h2 class="post-title"><a href="posts/{slug}.html">{p['title']}</a></h2>
  <div class="post-meta"><span class="tag">{p['category']}</span> Publicado por {p['author']} em {fmt_date(p['date'])}</div>
  <div class="post-body"><p>{excerpt(p)}</p></div>
  <a class="read-more" href="posts/{slug}.html">Continuar lendo &raquo;</a>
  <div class="post-footer"><span>{p['comments']} comentarios</span><span></span></div>
</article>""")
    body_html = "\n".join(cards) + '\n<div class="pagination"><span class="current">1</span> <a href="arquivo.html">Postagens mais antigas &raquo;</a></div>'
    html = page_shell("Inicio", "index.html", body_html)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

def render_archive():
    years = {}
    for p in POSTS:
        years.setdefault(p["date"][:4], []).append(p)
    blocks = []
    for y in sorted(years.keys(), reverse=True):
        items = "".join(
            f'<li><a href="posts/{slugify(p["title"])}.html">{fmt_date(p["date"])} &mdash; {p["title"]}</a> <span class="tag">{p["category"]}</span></li>'
            for p in sorted(years[y], key=lambda x: x["date"], reverse=True)
        )
        blocks.append(f'<h3 id="{y}">{y} ({len(years[y])} postagens)</h3><ul>{items}</ul>')
    body_html = f"""<div class="page-block">
<h1>Arquivo do Blog</h1>
<p>Todas as postagens da Comunidade Crista Rocha Eterna, desde a inauguracao deste blog em marco de 2019.</p>
{''.join(blocks)}
</div>"""
    html = page_shell("Arquivo", "arquivo.html", body_html)
    with open(os.path.join(OUT, "arquivo.html"), "w", encoding="utf-8") as f:
        f.write(html)

STATIC_PAGES = {
"sobre-nos.html": ("Sobre Nos", """
<h1>Sobre Nos</h1>
<p>A <strong>Comunidade Crista Rocha Eterna</strong> nasceu em 2013, reunindo um pequeno grupo de quinze pessoas num salao alugado no bairro Jardim Esperanca. Com o passar dos anos, e pela graca de Deus, essa familia cresceu bastante &mdash; hoje somos uma congregacao viva, diversa em idade e historia de vida, mas unida em um so proposito.</p>
<p>Nosso blog foi inaugurado em marco de 2019 como uma forma de aproximar a igreja de quem nao pode estar sempre presente, e de registrar a historia que Deus vem escrevendo no meio do nosso povo.</p>
<h3>O que cremos</h3>
<p>Cremos na Biblia como Palavra inspirada por Deus, na salvacao por meio de Jesus Cristo, e no batismo no Espirito Santo como uma experiencia viva e atual para todo aquele que cre. Valorizamos a oracao, o louvor espontaneo e o cuidado pratico uns com os outros como expressoes concretas da nossa fe.</p>
<h3>Nossos horarios</h3>
<p>Cultos aos domingos, 9h e 10h30 &middot; Escola Biblica Dominical, 9h &middot; Estudo biblico as quartas-feiras, 20h &middot; Ministerio de louvor, ensaios as quintas, 19h30.</p>
"""),
"nossa-missao.html": ("Nossa Missao", """
<h1>Nossa Missao</h1>
<p>Existimos para ser um lugar de <strong>fe, familia e restauracao</strong> &mdash; um espaco onde qualquer pessoa, independente de sua historia, possa encontrar acolhimento genuino e um caminho real de transformacao atraves de Jesus Cristo.</p>
<h3>Nossos valores</h3>
<ul>
<li><strong>Acolhimento:</strong> nossas portas estao abertas para quem quer que Deus traga ate nos.</li>
<li><strong>Palavra:</strong> ensinamos a Biblia com profundidade e aplicacao pratica para a vida real.</li>
<li><strong>Comunhao:</strong> cremos que a fe se vive em comunidade, nao isoladamente.</li>
<li><strong>Missoes:</strong> mantemos projetos de apoio a comunidades carentes na regiao e viagens missionarias regulares, como a que realizamos no Vale do Ribeira.</li>
</ul>
<h3>Onde queremos chegar</h3>
<p>Sonhamos em, nos proximos anos, ajudar a plantar novas congregacoes irmas em bairros vizinhos, ampliar nosso trabalho social e continuar sendo, para cada familia da Rocha Eterna, um lugar de portas sempre abertas.</p>
"""),
"lideranca.html": ("Lideranca", """
<h1>Nossa Lideranca</h1>
<p><strong>Pastor Renato Almeida</strong> &mdash; Pastor titular da Comunidade Crista Rocha Eterna desde a fundacao em 2013. Casado, pai de dois filhos, e responsavel pela pregacao dominical e pela conducao geral da igreja.</p>
<p><strong>Irma Claudia Freitas</strong> &mdash; Secretaria da igreja e responsavel pelas comunicacoes, incluindo este blog. Atua tambem na coordenacao da Escola Biblica Dominical.</p>
<p><strong>Diacono Elias Sathler</strong> &mdash; Responsavel pela diretoria administrativa, tesouraria e organizacao dos eventos da igreja.</p>
<p><strong>Missionaria Joana Prado</strong> &mdash; Coordena os projetos missionarios e sociais da igreja, incluindo as viagens a regiao do Vale do Ribeira.</p>
<p><strong>Jovem Lucas Ferreira</strong> &mdash; Lider do ministerio jovem e, atualmente, do ministerio de louvor.</p>
"""),
"contato.html": ("Contato", """
<h1>Contato</h1>
<p>Ficou com alguma duvida, quer saber mais sobre a igreja ou precisa de oracao? Fale com a gente:</p>
<p><strong>Endereco:</strong> Rua das Palmeiras, 482, Jardim Esperanca<br>
<strong>Cultos:</strong> domingos, 9h e 10h30<br>
<strong>E-mail:</strong> contato@rochaeterna.exemplo.br<br>
<strong>Secretaria:</strong> atendimento de terca a sexta, das 14h as 18h</p>
<p>Voce tambem pode deixar um comentario em qualquer postagem do blog &mdash; a nossa equipe responde assim que possivel.</p>
<h3>Envie uma mensagem</h3>
<form method="POST" action="/enviar-contato" class="contact-form">
  <label for="nome">Nome</label>
  <input type="text" id="nome" name="nome" required>
  <label for="email">Seu e-mail</label>
  <input type="email" id="email" name="email" required>
  <label for="mensagem">Mensagem</label>
  <textarea id="mensagem" name="mensagem" rows="5" required></textarea>
  <button type="submit">Enviar mensagem</button>
</form>
"""),
}

def render_static_pages():
    for fname, (title, inner) in STATIC_PAGES.items():
        body_html = f'<div class="page-block">{inner}</div>'
        html = page_shell(title, fname, body_html)
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(html)

def main():
    os.makedirs(POSTS_DIR, exist_ok=True)
    slugs = [render_post(p, i) for i, p in enumerate(POSTS)]
    render_index(slugs)
    render_archive()
    render_static_pages()
    print(f"Generated {len(slugs)} posts + index + archive + {len(STATIC_PAGES)} static pages.")

if __name__ == "__main__":
    main()
