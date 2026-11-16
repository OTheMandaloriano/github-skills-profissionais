# Padrão de README e verificação visual

## Conteúdo e escrita

Diga o que o projeto é, para quem serve e como começar. Mudanças pertencem ao
changelog. Limitações reais devem aparecer com motivo e impacto; retire as
resolvidas. Não apresente um snapshot como estável ou integralmente auditado
sem evidência. Não invente canais de suporte ou promessas de atendimento.

Escreva português natural, com acentos, frases curtas e uma ideia por frase.
Prefira vírgulas, parênteses e dois-pontos a travessões. Use medidas verificáveis
em vez de adjetivos. Evite “simplesmente”, “apenas” e “é só” em instruções que
exigem trabalho do leitor.

## Ícones SVG do Iconify

Use SVGs em títulos e destaques em vez de emojis nesses títulos. Preserve a
notação de árvores de arquivos escolhida pela pessoa. Prefira uma coleção
coesa, como Solar, e cores por significado: azul para informação, verde para
disponibilidade e laranja para atenção.

1. Confirme o identificador no catálogo oficial e confira autor e licença.
   Um nome plausível não prova a existência do ícone.
2. Para SVG remoto, o endpoint documentado é
   `https://api.iconify.design/<colecao>/<icone>.svg?color=%23HEX&width=24`.
   Use %23 no lugar de #. O endpoint correto não garante que o ícone exista ou
   carregue através do proxy do GitHub.
3. Prefira SVGs oficiais versionados em `docs/assets/icons/` quando houver
   falhas externas ou for necessária estabilidade. Registre origem/revisão,
   autor, licença e alterações. Preserve viewBox e fixe a cor quando necessário.
   O SVG não deve conter scripts, foreignObject ou referências externas.
4. Valide o arquivo e o carregamento como imagem. No navegador, confirme
   `complete && naturalWidth > 0` e inspecione o cabeçalho renderizado.
   Se o navegador estiver indisponível ou pausado, declare a limitação.

Exemplo, após adicionar o arquivo correspondente:

```html
<h2><img src="docs/assets/icons/danger-triangle-bold.svg"
  width="24" height="24" align="top" alt="" /> &nbsp;Limitações conhecidas</h2>
```

Use alt vazio para ícone decorativo e descrição para imagem informativa.
Um ícone genérico não constitui marca própria. Novo logo depende de autorização.
Use dimensão explícita, align="top" e espaçamento consistente. Confira as
âncoras geradas depois de incluir imagens ou espaços nos títulos.

## Badges e navegação

Quando existirem dados para ambas, use tecnologias em `for-the-badge` na
primeira fileira e fatos verificáveis em `flat-square` na segunda.
Use cores oficiais e logos confirmados no Simple Icons; respeite preferências
já informadas de cor e confira contraste nos temas claro e escuro.

```markdown
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Licenciamento](https://img.shields.io/badge/licenciamento-ver_NOTICE-EAB308?style=flat-square)](NOTICE.md)
```

A forma mensagem-cor produz um badge simples; rótulo-mensagem-cor produz duas
partes, e labelColor controla a primeira. Underline vira espaço; hífens literais
precisam do escape previsto pelo Shields. Todo badge deve ter destino útil.
Não invente versões, builds ou status. Os links de entrada devem levar a seções
ou documentos existentes. Centralize só o cabeçalho; mantenha o corpo à esquerda.

## Idiomas e bandeiras

Pergunte sobre idiomas adicionais ainda não definidos usando a seleção nativa
quando disponível e permitida. Não repita decisões respondidas. Se a pessoa
exigir seleção nativa e ela estiver indisponível, informe a limitação e continue
o trabalho independente; não simule botões com opções escritas.

Mantenha README.md como idioma principal e as traduções em
`docs/idiomas/README.<codigo>.md`. Para traduções existentes, use a mesma fileira
de bandeiras clicáveis no topo de todas as versões, com caminhos de ida e volta.
Prefira coleção flag em proporção 4x3, largura 26 e alt/title no próprio idioma.
Considere variantes regionais; bandeiras não substituem o nome acessível do idioma.

```html
<a href="README.md"><img src="docs/assets/flags/br-4x3.svg"
  width="26" alt="Português" title="Português" /></a>
<a href="docs/idiomas/README.en.md"><img src="docs/assets/flags/us-4x3.svg"
  width="26" alt="English" title="English" /></a>
```

O exemplo pressupõe arquivos existentes, com atribuição conforme a licença.
Só traduza o que será mantido; não publique bandeiras para páginas ausentes.

## Estrutura e aprofundamento

A raiz é a apresentação do projeto: README, changelog e licença/NOTICE.
Documentação técnica vai em docs/; templates de issue e PR vão em .github/.
CONTRIBUTING.md, SECURITY.md e CODE_OF_CONDUCT.md também podem ficar em .github/.
Crie documentos com conteúdo e processos reais, sem inventar licenças.

Use árvores comentadas de caminhos reais. Quando for pedido inventário completo,
enumere todos os arquivos do escopo, incluindo ocultos versionados. .git e caches
locais não pertencem ao inventário versionado. Listar caminhos não equivale a
explicar arquivos: descrições genéricas por pasta não substituem funções
individuais. Identifique incertezas e binários sem supor seu comportamento.

```html
<details>
<summary><b>Estrutura completa e função de cada arquivo</b></summary>

<br>

Conteúdo detalhado, com uma linha por arquivo.

</details>
```

Use tabelas para requisitos, limitações e outras comparações; callouts para
avisos relevantes. Não esconda limitações essenciais no details. Preserve as
demonstrações solicitadas e confira imagens, player, áudio, legendas e links.

## Evidência de entrega

Revise About, Topics, documentação, licença e demonstrações em conjunto.
O validador de SKILL.md verifica a estrutura do arquivo; ele não comprova que
a skill foi aplicada corretamente nem que um README renderiza.
Distinga alterado, validado localmente, publicado e observado no navegador.
Nunca declare imagem corrigida só porque o commit, o push ou o Markdown passou.
