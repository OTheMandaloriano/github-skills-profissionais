---
name: github-projeto-profissional
description: Organiza e mantém a apresentação profissional de um repositório no GitHub, incluindo README, About, Topics, releases, demonstrações, deployments, packages e branches. Use ao criar, publicar ou revisar um projeto.
---

# Projeto profissional no GitHub

Esta skill cuida da apresentação e da operação do repositório como produto.
Ela se complementa com `versionamento-git`, que cuida dos commits, do
changelog e do envio das mudanças.

## Intenção antes de agir

Classifique o pedido antes de criar, editar ou publicar qualquer coisa:

| Intenção identificada | Conduta |
| --- | --- |
| Dúvida ou explicação | Responda no chat. Não crie arquivos, repositório, branch, commit, tag ou release. |
| Diagnóstico ou revisão | Inspecione em modo leitura e apresente o diagnóstico. Não altere o projeto sem pedido de correção. |
| Início ou organização de projeto | Inspecione a pasta e proponha somente a estrutura necessária para o objetivo pedido. |
| Implementação ou correção | Trabalhe localmente, valide e informe o resultado. Não publique sem pedido ou autorização prévia. |
| Publicação ou release | Use também `versionamento-git` para revisar o estado, registrar e enviar a mudança. |

Em uma conversa nova dentro de um projeto, verifique silenciosamente se há
repositório Git, remoto, branch, alterações pendentes e convenções locais para
entender o contexto. Não reorganize, inicialize Git, crie documentação ou
publique por essa verificação. Pergunte somente se a decisão for necessária
para cumprir um pedido de trabalho, como "vamos começar este projeto" ou
"prepare este repositório para o GitHub".

## Conteúdo que pertence ao repositório

O repositório deve explicar e entregar o projeto, nunca registrar a conversa
que levou até ele. Não inclua em código, documentação, commits, changelog,
releases, branches ou nomes de arquivo referências a usuário, IA, agente,
prompt, chat, conversa, aprovação ou instrução de bastidor.

Use linguagem destinada a quem usa, mantém ou contribui com o projeto. Em vez
de "o usuário pediu uma correção", registre o comportamento corrigido. Em vez
de "a IA implementou", descreva a funcionalidade entregue. Só mantenha
arquivos que sejam necessários para executar, compreender, distribuir, testar
ou manter o produto. Arquivos temporários, exportações de chat, rascunhos e
artefatos sem uso devem ficar fora do controle de versão.

Leia o código, os arquivos de documentação, a configuração de build e o
histórico recente antes de propor alterações. Preserve a convenção existente
quando ela estiver clara. Não invente funcionalidades, números, imagens,
releases, deployments ou packages para preencher uma página vazia.

## A identidade do repositório

O nome da pasta e o título devem descrever o produto de forma direta. Evite
nomes internos, provisórios ou genéricos como `teste`, `projeto-novo` e
`versao-final`. Se o repositório já estiver publicado, não renomeie-o sem
avaliar links, clones, integrações e dependentes.

Configure a seção **About** com informação verificável:

- **Descrição:** uma frase que diga o que o projeto é e para quem serve.
- **Website:** a documentação, demonstração ou página oficial, quando existir.
- **Topics:** de 3 a 10 termos em minúsculas que descrevam tecnologia,
  plataforma, domínio e finalidade. Não repita o nome do repositório.
- **Licença:** use uma licença real e compatível com o código. Forks sem
  licença não podem receber uma licença inventada.

O README explica o produto por completo. About e Topics servem para que ele
seja encontrado antes mesmo de ser aberto.

## README e documentação

O README deve dizer o que o projeto é, o problema que resolve, requisitos,
instalação, uso e limitações reais. Em projetos que se beneficiem disso,
inclua recursos principais, arquitetura e uma demonstração visual.

- Use ícones SVG consistentes do [Iconify](https://icon-sets.iconify.design/)
  em títulos quando eles melhorarem a leitura. Prefira uma coleção, como
  `solar`, e poucas cores com significado consistente.
- Use um logo próprio ou um ativo cuja licença permita distribuição. Sem marca
  definida, use o nome em texto em vez de criar identidade visual não aprovada.
- Use Mermaid para diagramas pequenos de componentes e fluxos. O diagrama deve
  corresponder ao código atual.
- Inclua capturas de tela, GIF ou vídeo somente quando o projeto tiver uma
  interface ou resultado visual que mereça demonstração e o autor quiser
  publicá-lo. Remova e-mails, tokens, dados de clientes e qualquer informação
  pessoal. Guarde capturas em `assets/screenshots/` ou pasta equivalente.
- O GitHub gera a lista de contribuidores a partir de commits. Não duplique
  essa lista manualmente. Registre créditos específicos apenas quando houver
  exigência de atribuição.

Mantenha a raiz enxuta: `README.md`, `CHANGELOG.md`, licença ou `NOTICE.md` e
os arquivos essenciais. Coloque documentação técnica em `docs/` e modelos de
issue e pull request em `.github/`.

## Recursos do GitHub

Use cada recurso somente quando houver produto ou processo para sustentá-lo:

| Recurso | Quando faz sentido | Padrão de qualidade |
| --- | --- | --- |
| Releases | Existe uma versão utilizável, testada, versionada e pronta para consumo. | Tag anotada, notas claras, arquivos verificáveis e instruções de atualização. |
| Deployments | Há ambiente real de preview, homologação ou produção. | Ambiente, URL e estado refletem a implantação real. |
| Packages | O projeto publica biblioteca, imagem, ação ou pacote consumido por outros projetos. | Versão, licença, instruções de uso e registro compatível. |
| Issues e discussões | Existe manutenção pública, suporte ou decisões abertas. | Modelos claros para falhas e sugestões. |
| Segurança | O projeto recebe contribuições ou processa dados relevantes. | `SECURITY.md` com canal de reporte e escopo real. |

Uma release não é um commit. O commit registra uma unidade coesa de trabalho;
a release apresenta uma versão pronta para quem consome o projeto.

## Branches

Uma branch é uma linha de trabalho isolada. Ela evita que uma mudança
incompleta se misture à branch principal e permite revisão por pull request.

Criar uma branch não publica uma versão e não cria uma release. Ela pode ser
enviada ao remoto para abrir um pull request, mas a publicação de uma versão
para quem consome o produto continua dependendo de commit integrado, tag e
release quando solicitada.

Não crie branches por hábito. Para uma mudança pequena, de baixo risco, feita
por uma pessoa, trabalhar na branch principal pode ser correto se essa for a
convenção do projeto. Sugira uma branch quando houver revisão, mudança
arriscada, experimento, correção urgente, trabalho paralelo ou mais de uma
pessoa alterando o projeto.

Use nomes curtos e objetivos:

```
feat/exportacao-pdf
fix/sessao-expirada
docs/guia-instalacao
```

Não mantenha branches permanentes como `dev`, `teste` ou `nova-versao` sem um
processo de entrega que realmente as utilize. Proteja `main` quando houver
equipe, revisão obrigatória, CI ou publicação automática.

Escolha o fluxo a partir do repositório, nesta ordem:

| Cenário | Fluxo adequado |
| --- | --- |
| `main` protegida, pull request obrigatório ou revisão de outra pessoa | Crie branch, implemente, valide, envie e abra pull request. |
| Mudança arriscada, experimento, correção urgente ou trabalho paralelo | Crie branch isolada, mesmo que a `main` aceite push direto. |
| Mudança pequena, baixo risco, uma pessoa e convenção de commits diretos | Trabalhe na branch atual e faça commit. Só envie se houver pedido de publicação. |
| Usuário pediu uma release | Não deduza branch. Primeiro confirme se a versão está pronta, validada e integrada conforme a convenção. |

Se a configuração do repositório não deixar claro se `main` aceita push direto,
inspecione as regras e o histórico. Quando ainda houver escolha de processo que
afete outras pessoas, explique a opção e peça direção antes de criar ou enviar
uma branch.

## Administração contínua

Após uma atualização, avalie o impacto antes de mudar a documentação ou o
GitHub:

1. **Mudança interna:** se não alterou o comportamento visível, a instalação,
   a compatibilidade ou a arquitetura documentada, normalmente basta o commit.
2. **Correção ou recurso visível:** atualize README ou documentação quando a
   pessoa usuária precisa saber como usar, configurar ou entender a novidade.
3. **Mudança relevante:** atualize o changelog quando alterar comportamento,
   segurança, compatibilidade, distribuição ou experiência de uso.
4. **Nova versão pronta:** crie release somente quando a mudança estiver
   validada, com tag e notas para consumo. Uma sequência de commits não exige
   uma sequência de releases.
5. **Mudança de posicionamento:** revise descrição, Topics, logo, capturas e
   arquitetura quando o produto, o público ou a tecnologia principal mudarem.

Não deixe a documentação defasada, mas também não reescreva o README para
registrar cada detalhe de implementação. A revisão deve acompanhar mudanças
que alteram o entendimento ou o uso do produto.

## Primeiro uso e acesso ao GitHub

Quando o pedido envolver criar, organizar, versionar ou publicar um projeto,
verifique primeiro a disponibilidade de Git, GitHub CLI, identidade local,
repositório e remoto. Faça essas verificações sem alterar o computador.

Se faltar Git ou GitHub CLI, informe o que falta e ofereça o instalador ou
comando oficial. Instale somente quando o usuário solicitar explicitamente.
Se a conta não estiver autenticada, inicie o fluxo oficial de login e deixe a
pessoa concluir a autorização no navegador. Não solicite senha, token, cookie,
chave privada ou código de autenticação no chat.

Use `user.name` e `user.email` já configurados no repositório quando forem
adequados. Se a identidade não existir ou a conta pessoal e a organização
exigirem identidades diferentes, pergunte qual deve ser usada. Recomende o
e-mail `noreply` do GitHub para privacidade; ele continua permitindo que o
GitHub associe o commit ao perfil e à foto da pessoa. Configure a identidade
por repositório, não globalmente, quando houver conta corporativa e pessoal no
mesmo computador.

## Revisão final

Antes de concluir, confira que About, Topics, README, changelog, links,
licença, imagens e releases descrevem o mesmo produto. Informe o que foi
configurado e o que foi deixado de fora porque ainda não existe no projeto.
