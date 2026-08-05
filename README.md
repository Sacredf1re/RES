# Comunidade Cristã Rocha Eterna — site do blog

Site estático estilo "Blogger antigo" para a igreja fictícia **Comunidade Cristã
Rocha Eterna**, com 184 postagens datadas de março de 2019 a agosto de 2026 —
incluindo posts recorrentes anuais (Jejum de Daniel, Semana Santa, Páscoa,
Pentecostes, Dia das Mães, Dia dos Pais, Dia da Reforma, Culto de Virada),
uma oração temática por mês desde o início do blog, posts de excursão e de
ação social, e um post em branco pronto para edição — mais páginas
institucionais (Sobre Nós, Nossa Missão, Liderança, Contato, Arquivo) e
comentários visíveis em cada post.

Todo o conteúdo publicável está em `public/` — é esse é o diretório que vai para
produção.

## Estrutura

```
public/
  index.html          página inicial (últimas 10 postagens)
  arquivo.html         lista de todas as postagens por ano
  sobre-nos.html, nossa-missao.html, lideranca.html, contato.html
  posts/                30 páginas individuais de postagem
  css/style.css
gen.py                  script gerador — edite os dados aqui, não os HTMLs
render.yaml              blueprint de deploy para o Render
ARG_NOTES.md             notas privadas sobre as pistas escondidas (NÃO publicar)
```

## Editar o conteúdo

Não edite os arquivos dentro de `public/posts/` diretamente — eles são gerados.
Em vez disso, edite a lista `POSTS` em `gen.py` (título, data, autor, categoria,
corpo do texto, `hidden_comment` opcional) e rode:

Os posts recorrentes anuais (Jejum de Daniel, Semana Santa, Páscoa,
Pentecostes, Dia das Mães, Dia dos Pais, Dia da Reforma, Virada de Ano) não
estão na lista `POSTS` — são gerados automaticamente pela função
`_theme_body()` mais abaixo no arquivo. Para editar o texto-base de um desses
temas, mexa ali; para editar só um ano específico, adicione uma exceção
dentro de `_theme_body()` ou copie o post gerado para a lista `POSTS` manual
e remova a chamada `add_recurring(...)` correspondente.

```bash
python3 gen.py
```

Isso reconstrói todas as páginas em `public/` do zero.

## Publicar no Render

### Opção A — Blueprint automático (`render.yaml`)
1. Suba esta pasta inteira para um repositório no GitHub/GitLab.
2. No painel do Render, clique em **New > Blueprint**, aponte para o repositório.
   O Render vai ler `render.yaml` e configurar o site estático automaticamente
   (publish path `./public`, sem build command).
3. Confirme e aguarde o deploy.

### Opção B — Manual (mais confiável se a sintaxe do Blueprint mudar)
1. Suba a pasta para um repositório Git.
2. No painel do Render: **New > Static Site**.
3. Conecte o repositório.
4. Em **Build Command**, deixe em branco.
5. Em **Publish Directory**, coloque `public`.
6. Deploy.

> A sintaxe exata de `render.yaml` pode mudar com o tempo — se o Blueprint
> falhar, use a Opção B manual, que é mais estável, e confira a documentação
> atual do Render (render.com/docs) para o formato mais recente.

## Sobre o design

O visual foi feito de propósito parecido com um template antigo do Blogger
(cores terrosas, Georgia/Trebuchet, widgets de barra lateral, contador de
visitas) em vez de um design moderno de agência — é o que faz o site soar
autêntico como o blog real de uma igreja de bairro mantido por voluntários
desde 2019.

## Pistas do ARG

Este site tem um fio narrativo sobre o desaparecimento da personagem Vera
Lúcia, com pistas escondidas (citações bíblicas "erradas" e comentários HTML
em base64). Os detalhes completos de onde estão e como decodificá-las estão
em `ARG_NOTES.md` — esse arquivo é só para você, não faz parte do site
publicado.
