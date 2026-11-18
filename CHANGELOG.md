# Registro de alterações

Todas as mudanças relevantes deste projeto serão registradas neste arquivo.
O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/)
e o projeto adota [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Não publicado]

### Adicionado

- Skill `transcrever-video`: transcreve a fala de vídeos do YouTube, Shorts e
  arquivos locais, entrega o texto no chat e só exporta TXT, SRT, JSON, Markdown
  ou PDF na pasta escolhida pela pessoa.
- Política de resíduo zero na skill de transcrição: todo o processamento ocorre
  em pasta temporária do sistema, removida ao final da execução.
- Verificação e instalação de dependências da skill de transcrição
  (`--check`, `instalar_dependencias.ps1` e `instalar_dependencias.sh`), com
  `pip install --user` e validação de `ffmpeg` no PATH ou embutido no
  `imageio-ffmpeg`.
- Referência de captura de áudio pelo navegador para quando o YouTube recusar o
  download direto (HTTP 403 / SABR).
- `scripts/validar_skills.py`: valida frontmatter, nome da pasta, descrição,
  caminhos citados e sintaxe dos scripts de todas as skills, sem dependência
  externa e sem gravar `.pyc`.
- Referência para selecionar conteúdo de produto e desenvolvimento conforme
  evidências, com documentação por objetivo, compatibilidade, roadmap, autoria
  e créditos, além de adaptação de badges, ícones e cores ao projeto.

- Skill para apresentação profissional de projetos no GitHub.
- Skill para versionamento, changelog e publicação segura.
- Instaladores com revisão de sobrescrita para Codex, Claude Code e OpenCode.

### Alterado

- Repositório reposicionado como coleção de skills para tarefas diferentes, e
  não apenas skills de GitHub. README reorganizado com tabela de skills, guia de
  escolha por objetivo, dependências por skill e exemplos de pedidos.
- Instaladores passaram a descobrir automaticamente as skills pela presença de
  `SKILL.md`, sem lista fixa de nomes. Uma pasta nova no repositório já é
  instalável.
- `CONTRIBUTING.md` reescrito para a coleção: como criar uma skill, como
  declarar dependências e como validar antes do pull request. Removida a
  referência a um validador que não existia no repositório.
- Templates de issue e pull request atualizados para múltiplas ferramentas
  (Codex, Claude Code, OpenCode), versão de Python quando houver script e
  checklist de validação real.
- `.gitignore` cobre artefatos de Python e resíduo de mídia; `.gitattributes`
  fixa fim de linha LF para `*.py` e `*.txt`.
- Explicitadas decisões por seleção nativa em diferentes agentes nas duas skills, com respeito às capacidades da sessão e às escolhas anteriores.
- Detalhado encerramento de README por tipo de projeto, com autoria, créditos, licença e convite discreto à contribuição ou apoio.

- Recuperados exemplos e critérios de ícones, badges, bandeiras, escrita e
  organização da antiga skill de README em uma referência dedicada.
- Exigida confirmação dos identificadores de ícones, atribuição de licença e
  evidência de carregamento, com SVGs versionados como alternativa a APIs externas.
- Diferenciadas validação estrutural, publicação e inspeção visual; decisões
  interativas pendentes não impedem alterações independentes já autorizadas.

- Instruções de branches, push, pull requests e releases separadas por finalidade.
- Documentação de instalação preparada para uso em Codex, Claude Code e OpenCode.
- README ampliado com um guia de escolha das skills para pessoas usuárias.
- `github-projeto-profissional` ampliada com o padrão detalhado de README,
  documentação, publicação e limpeza de resíduos.
- README ampliado com explicações clicáveis sobre branch, commit, push, pull
  request e release.
