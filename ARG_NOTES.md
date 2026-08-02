# Notas do ARG (arquivo privado — não publicar em `public/`)

Fio narrativo: **Vera Lúcia Nascimento**, líder de louvor desde 2019, começa a
dar sinais estranhos em meados de 2021, parte para um "retiro de silêncio" em
agosto de 2021 e nunca mais volta. A igreja trata o assunto com cautela
crescente ao longo dos anos seguintes. Nada no site afirma explicitamente o
que aconteceu com ela — está desenhado para ficar em aberto, para você
encaixar no resto do seu ARG.

## 1. Linha do tempo da personagem (para referência)

| Data | Post | O que acontece |
|---|---|---|
| 2019-06-02 | Testemunho: a cura que Deus operou em mim | Vera é apresentada |
| 2019-10-06 | Ministério de Louvor: novos ensaios | Vera assume o louvor |
| 2020-06-14 | Vera assume a coordenação da EBD | Ganha mais responsabilidade |
| 2020-08-09 | Vigília de Oração pelas famílias | Último post "normal" dela |
| 2021-07-18 | Uma palavra que recebi em oração | Primeiro sinal de inquietação + **anomalia 1** |
| 2021-08-30 | Retiro de silêncio | Ela anuncia a partida + **anomalia 2** |
| 2021-09-12 | Sentimos a falta da irmã Vera | Primeiro post sobre a ausência + **comentário oculto 1** |
| 2021-11-01 | Continuamos orando pelos que caminham longe | **anomalia 3** |
| 2022-07-03 | Ainda oramos por ela | **anomalia 4** + **comentário oculto 2** |
| 2023-03-05 | Um ano e meio depois | **anomalia 5** — última menção direta e mais longa |
| 2025-06-08 | Cinco anos de Ministério de Louvor | Homenagem tardia + **comentário oculto 3** (a "chave" que diz para juntar os números) |

## 2. Citações bíblicas "erradas" (código numérico)

Cada uma cita um capítulo real da Bíblia com um número de versículo que **não
existe** naquele capítulo (fácil de checar em qualquer app bíblico). O
último dígito de cada "versículo impossível", na ordem cronológica dos
posts, forma o código:

| Ordem | Post | Citação usada | Versículos reais no capítulo | Dígito |
|---|---|---|---|---|
| 1 | Uma palavra que recebi em oração (2021-07-18) | Salmos 145:23 | Salmos 145 tem 21 versículos | **3** |
| 2 | Retiro de silêncio (2021-08-30) | Provérbios 31:32 | Provérbios 31 tem 31 versículos | **2** |
| 3 | Continuamos orando... (2021-11-01) | Isaías 66:25 | Isaías 66 tem 24 versículos | **5** |
| 4 | Ainda oramos por ela (2022-07-03) | Salmos 23:9 | Salmos 23 tem 6 versículos | **9** |
| 5 | Um ano e meio depois (2023-03-05) | João 21:26 | João 21 tem 25 versículos | **6** |

**Código final: 3-2-5-9-6**

O post de 2025 ("Cinco anos de Ministério de Louvor") contém um comentário
HTML (base64) que diz: *"As citações erradas não foram um erro. Junte os
números."* — isso é o gancho para o jogador voltar e montar o código acima.
O site em si nunca revela o número 32596 — você decide o que essa combinação
abre (um cadeado físico, uma URL escondida, um telefone, etc.) na próxima
etapa do seu ARG.

## 3. Comentários HTML ocultos (view-source / inspecionar elemento)

Cada um está como `<!-- texto em base64 -->` logo depois do corpo do post,
antes do rodapé. Um jogador que abrir "Ver código-fonte da página" encontra.

1. **`posts/sentimos-a-falta-da-irma-vera.html`** (2021-09-12)
   Base64: `U2Ugdm9jZSBlc3TDoSBsZW5kbyBpc3RvLCBwcm9jdXJlIG9uZGUgYSBsdXogbsOjbyBjaGVnYSDDoHMgc2V4dGFzLWZlaXJhcy4=`
   Decodifica para: *"Se voce está lendo isto, procure onde a luz não chega
   às sextas-feiras."*

2. **`posts/ainda-oramos-por-ela.html`** (2022-07-03)
   Base64: `UnVhIGRhcyBBY8OhY2lhcywgMjE0IC0gZnVuZG9zLg==`
   Decodifica para: *"Rua das Acácias, 214 - fundos."* (endereço fictício —
   troque por algo real/relevante ao seu ARG se for usar como pista física)

3. **`posts/cinco-anos-de-ministerio-de-louvor.html`** (2025-06-08)
   Base64: `QXMgY2l0YcOnw7VlcyBlcnJhZGFzIG7Do28gZm9yYW0gdW0gZXJyby4gSnVudGUgb3MgbsO6bWVyb3Mu`
   Decodifica para: *"As citações erradas não foram um erro. Junte os
   números."* (a chave que aponta para a seção 2 acima)

## 3.5 O "haystack" (posts recorrentes + comentários)

Para dificultar achar as pistas acima, o site agora tem **86 posts** no
total: além dos 30 originais, foram adicionados posts recorrentes anuais
(Jejum de Daniel em janeiro, Semana Santa, Páscoa, Pentecostes, Dia das
Mães, Dia dos Pais, Dia da Reforma em outubro, Culto de Virada em
dezembro) para praticamente todos os anos de 2019 a 2026. Nenhum desses
posts extras contém pistas — são só volume de conteúdo real e datado
para as 5 anomalias e os 3 comentários ocultos ficarem mais difíceis de
encontrar em meio ao resto. Eles são gerados por `_theme_body()` em
`gen.py` (não editados manualmente).

Cada post também agora exibe comentários visíveis (nomes fictícios +
frases genéricas tipo "Amém", "Glória a Deus", "Que bênção") selecionados
de forma determinística a partir do título do post — puramente estética,
sem pistas escondidas nos comentários.

## 4. Como estender

- `gen.py` é a fonte da verdade — edite a lista `POSTS` (campo
  `hidden_comment` para comentários base64, corpo do texto para novas
  anomalias) e rode `python3 gen.py` para reconstruir tudo em `public/`.
- Para adicionar mais pistas, siga o mesmo padrão: uma citação bíblica com
  número de versículo impossível, ou um `hidden_comment` novo — ambos viram
  automaticamente parte do HTML gerado.
- Nada neste site menciona pessoas reais, nem descreve dano concreto a
  ninguém — o mistério fica deliberadamente ambíguo (retiro espiritual,
  fuga, algo pior?) para você decidir o resto da história fora do site.
