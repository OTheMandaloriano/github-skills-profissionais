<div align="center">

<img src="https://api.iconify.design/solar/code-square-bold.svg?color=%2310B981&width=72" alt="Skills profissionais" width="72" height="72" />

# Skills profissionais

Instruções reutilizáveis em pt-BR para trabalho técnico: apresentação de projetos no GitHub, versionamento de código e transcrição de vídeos. Uma skill por tarefa, no formato aberto `SKILL.md`.

[![Codex](https://img.shields.io/badge/Codex-Skills-10A37F?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/codex/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Skills-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.com/claude-code)
[![OpenCode](https://img.shields.io/badge/OpenCode-Skills-111827?style=for-the-badge&logo=terminal&logoColor=white)](https://opencode.ai/)
[![GitHub](https://img.shields.io/badge/GitHub-Repositórios-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

[![Idioma](https://img.shields.io/badge/idioma-pt--BR-009C3B?style=flat-square)](README.md)
[![Licença](https://img.shields.io/badge/licença-MIT-0EA5E9?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-pronto_para_uso-10B981?style=flat-square)](CHANGELOG.md)

</div>

## <img src="https://api.iconify.design/solar/compass-bold.svg?color=%230EA5E9&width=24" align="top" /> &nbsp;O que este projeto oferece

Este repositório começou como um par de skills para GitHub e passou a ser uma
coleção: cada pasta é uma skill independente, com instruções completas e, quando
precisa, scripts próprios.

As skills distinguem dúvida, diagnóstico, trabalho local, publicação e release.
Elas não criam repositórios, arquivos, branches, commits ou releases quando a
pessoa apenas pede uma explicação ou uma revisão. A skill de transcrição segue a
mesma lógica: entrega o texto no chat e só grava arquivo quando a pessoa pede e
escolhe a pasta.

| Skill | Categoria | Para que serve |
| --- | --- | --- |
| [`github-projeto-profissional`](github-projeto-profissional/SKILL.md) | GitHub | Organiza README, arquitetura, demonstrações, About, Topics, Releases, Deployments, Packages e branches. |
| [`versionamento-git`](versionamento-git/SKILL.md) | Git | Mantém commits coesos, revisa o diff preparado, atualiza changelog quando necessário e publica com segurança. |
| [`transcrever-video`](transcrever-video/SKILL.md) | Mídia | Transcreve a fala de vídeos no chat, sem resíduo em disco, e exporta TXT/SRT/JSON/MD/PDF sob demanda. |

## <img src="https://api.iconify.design/solar/question-circle-bold.svg?color=%23F97316&width=24" align="top" /> &nbsp;Qual skill devo usar?

Use esta seção como guia rápido. Você não precisa entender Git para escolher a
skill: diga o objetivo com palavras naturais e use a que combina com o tipo de
trabalho.

### `github-projeto-profissional`

Use quando quiser deixar o projeto bem apresentado, fácil de entender e pronto
para outras pessoas encontrarem ou contribuírem no GitHub.

Ela ajuda a organizar:

- nome, descrição, About e Topics do repositório;
- README, instalação, recursos principais e limitações;
- logo, capturas de tela, vídeo e diagrama de arquitetura, quando existirem;
- Issues, pull requests, contribuição, segurança e licença;
- uso correto de branches, deployments, packages e releases.

Exemplos de pedidos:

```text
Organize este repositório para o GitHub.
Vamos começar este projeto e deixá-lo profissional.
Melhore o README e explique como instalar.
Prepare uma página de projeto que outras pessoas entendam.
```

Ela não cria uma release, branch ou publicação só porque foi aberta. Primeiro
avalia o projeto e só propõe essas ações quando forem necessárias.

### `versionamento-git`

Use quando o projeto já tem uma alteração pronta e você quer salvar o histórico
corretamente, enviar ao GitHub ou preparar uma nova versão.

Ela ajuda a:

- revisar o que mudou antes de salvar;
- separar mudanças que não deveriam ficar no mesmo commit;
- criar uma mensagem de commit clara e profissional;
- impedir que tokens, arquivos temporários ou conteúdo de conversa subam;
- atualizar o changelog quando a mudança for relevante;
- fazer push quando você pedir para publicar;
- preparar uma release somente quando houver versão pronta para uso.

Exemplos de pedidos:

```text
Revise as alterações deste projeto antes de publicar.
Corrija este erro e publique a atualização.
Prepare uma release com notas para quem usa o projeto.
Veja se há arquivos desnecessários antes do commit.
```

Ela não publica nada quando você apenas tira uma dúvida, pede explicação ou
solicita um diagnóstico.

### `transcrever-video`

Use quando quiser saber o que foi falado em um vídeo, gerar legenda ou resumir
uma fala, sem ficar com arquivos soltos no computador.

Ela entrega:

- transcrição no chat, com marcação de tempo;
- resumo do conteúdo falado, quando pedido;
- exportação opcional em TXT, SRT, JSON, Markdown ou PDF, na pasta que você escolher.

Exemplos de pedidos:

```text
Transcreva este vídeo: https://youtube.com/shorts/...
O que foi falado nesse vídeo?
Gere a legenda SRT deste arquivo de áudio.
Resuma o que ele disse e me mande o PDF.
```

Ela trabalha em pasta temporária, apaga tudo no fim e só exporta quando você
informar o destino. Nada de WAV, frames ou capturas esquecidas em Downloads.

## <img src="https://api.iconify.design/solar/settings-bold.svg?color=%2310B981&width=24" align="top" /> &nbsp;Dependências

Cada skill declara o que precisa. Nenhuma instala nada sem avisar.

| Skill | Precisa de | Como resolve |
| --- | --- | --- |
| `github-projeto-profissional` | nada além do agente | — |
| `versionamento-git` | `git` instalado | confere no início do fluxo e avisa se faltar |
| `transcrever-video` | Python 3.9+, `faster-whisper`, `yt-dlp`, `ffmpeg` (ou `imageio-ffmpeg`) | `--check` + instalador `pip install --user` |

Na skill de transcrição:

```powershell
python transcrever-video\scripts\transcrever.py --check
powershell -ExecutionPolicy Bypass -File transcrever-video\scripts\instalar_dependencias.ps1
```

```bash
./transcrever-video/scripts/instalar_dependencias.sh --check
./transcrever-video/scripts/instalar_dependencias.sh
```

O instalador valida a versão do Python, instala os pacotes com `--user` (sem
administrador) e confirma o `ffmpeg` no PATH ou o binário embutido do
`imageio-ffmpeg`. Se o ambiente bloquear instalação global (PEP 668), use um
venv temporário e apague no fim.

## <img src="https://api.iconify.design/solar/box-bold.svg?color=%2310B981&width=24" align="top" /> &nbsp;Compatibilidade e instalação

As instruções usam o formato aberto `SKILL.md`, compatível com Codex, Claude
Code e OpenCode. O conteúdo é o mesmo; cada ferramenta usa uma pasta de
instalação própria.

Copie as pastas das skills para um destes caminhos e reinicie a ferramenta:

```text
Codex:       ~/.codex/skills/
Claude Code: ~/.claude/skills/
OpenCode:    ~/.config/opencode/skills/
```

No OpenCode, também é possível instalar por projeto em:

```text
.opencode/skills/
```

No Windows, substitua `~` pela pasta do seu usuário. Por exemplo:

```text
C:\Users\SEU_USUÁRIO\.codex\skills\
C:\Users\SEU_USUÁRIO\.claude\skills\
C:\Users\SEU_USUÁRIO\.config\opencode\skills\
```

### Instalação assistida

Após baixar ou clonar este repositório, peça ao seu assistente compatível:

```text
Instale as skills deste repositório para Codex, Claude Code e OpenCode.
Mostre o que será alterado e não sobrescreva skills existentes sem minha confirmação.
```

No Windows, também é possível executar:

```powershell
.\scripts\install-skills.ps1 -Target All -WhatIf
.\scripts\install-skills.ps1 -Target Codex
```

Em macOS ou Linux, use:

```bash
./scripts/install-skills.sh --target all --dry-run
./scripts/install-skills.sh --target codex
```

Os instaladores descobrem automaticamente toda pasta que tenha `SKILL.md`.
Eles interrompem a execução se encontrarem uma skill com o mesmo nome. Use
`-Force` no PowerShell ou `--force` no shell somente depois de revisar a
atualização que será aplicada.

## <img src="https://api.iconify.design/solar/rocket-2-bold.svg?color=%23F97316&width=24" align="top" /> &nbsp;Uso

Use pedidos naturais. A intenção do verbo define o fluxo:

| Pedido | Resultado esperado |
| --- | --- |
| "Explique como funcionam branches." | Resposta no chat, sem alterar projeto. |
| "Revise este repositório." | Diagnóstico em modo leitura. |
| "Vamos começar este projeto." | Avaliação da pasta e organização somente do que for necessário. |
| "Corrija este problema." | Implementação e validação local. |
| "Corrija e publique esta atualização." | Revisão, commit coeso e push. |
| "Prepare uma release." | Avaliação de versão, changelog, tag e notas. |
| "Transcreva este vídeo." | Texto no chat, sem arquivo residual. |
| "Gere o PDF da transcrição em D:\Docs." | Exportação só na pasta indicada. |

## <img src="https://api.iconify.design/solar/git-fork-bold.svg?color=%230EA5E9&width=24" align="top" /> &nbsp;Padrão de manutenção

Commits registram unidades coesas e validadas de trabalho. Releases representam
versões prontas para consumo. Uma atualização interna pode exigir apenas um
commit; uma mudança de uso, compatibilidade, segurança ou distribuição também
precisa de documentação e changelog atualizados.

O repositório deve conter somente material do projeto. Não publique referências
a conversas, pessoas usuárias, IA, prompts, aprovações ou decisões de bastidor.
Escreva sempre para quem usa, mantém ou contribui com o projeto.

Uma branch não é uma release. Ela isola uma mudança e pode servir para revisão
por pull request. A skill cria branch somente quando a política do repositório,
o risco ou a colaboração justificarem; push e release continuam dependendo da
intenção do pedido e da preparação da versão.

Ao adicionar uma skill nova:

1. crie a pasta com `SKILL.md` e os arquivos de apoio;
2. declare dependências e como verificá-las;
3. atualize a tabela de skills e o guia de escolha neste README;
4. rode `python scripts/validar_skills.py` e corrija o que ele apontar;
5. registre a mudança no `CHANGELOG.md`.

O validador confere frontmatter, nome da pasta, descrição, caminhos citados e
sintaxe dos scripts Python de todas as skills. Ele não julga o texto — isso é
revisão humana.

```powershell
python scripts\validar_skills.py
```

## <img src="https://api.iconify.design/solar/book-2-bold.svg?color=%23F97316&width=24" align="top" /> &nbsp;Entenda os conceitos

<details>
<summary><b>O que é uma branch?</b></summary>

<br>

Uma **branch** é uma cópia temporária da linha principal do projeto para
trabalhar sem mexer diretamente no código oficial.

Pense na `main` como o documento final. Uma branch é uma cópia de trabalho
onde você faz alterações, testa e revisa antes de colocar o resultado na linha
principal.

```text
main ───── projeto estável

main ───── branch: correcao-login
         └── alterações e testes
                 │
              aprovação
                 │
main ─────────── correção integrada
```

Use uma branch quando:

- a mudança é grande ou arriscada;
- outra pessoa precisa revisar;
- há mais de uma pessoa trabalhando;
- você quer testar uma ideia sem risco;
- precisa corrigir algo urgente sem misturar com outro trabalho.

Exemplo:

```text
main
└── fix/sessao-expirada
```

O fluxo cria a branch `fix/sessao-expirada`, corrige o problema, testa e abre
uma revisão. Depois, a correção é integrada à `main`.

Não precisa usar branch para uma alteração pequena, segura e feita só por você,
se o repositório permite commits diretos na `main`.

Uma branch **não é uma versão pública**. Ela não cria release, não atualiza o
programa para usuários e não substitui a `main`. Ela organiza o trabalho antes
da integração.

</details>

<details>
<summary><b>O que é um commit?</b></summary>

<br>

Um **commit** é um registro de uma mudança concluída. Ele salva uma versão
pequena e identificável do projeto, com uma mensagem que explica a intenção da
mudança.

Exemplo: depois de corrigir a renovação de sessão e validar o resultado, o
commit pode ser:

```text
[fix] renova a sessão antes de consultar limites
```

Um commit não publica o projeto sozinho. Ele apenas registra o trabalho no
histórico local para que seja possível entender, revisar ou recuperar mudanças.

</details>

<details>
<summary><b>O que é push?</b></summary>

<br>

**Push** envia commits do seu computador para o GitHub. É o momento em que o
histórico local passa a aparecer no repositório remoto.

Use push quando a mudança estiver validada e você pedir para publicar, ou
quando o fluxo do projeto já autorizar esse envio. Push não cria uma release.

</details>

<details>
<summary><b>O que é um pull request?</b></summary>

<br>

Um **pull request**, também chamado de PR, é um pedido para revisar e integrar
uma branch na `main`. Ele mostra o diff, permite comentários e registra a
aprovação antes da integração.

Use pull request quando a `main` for protegida, outra pessoa precisar revisar
ou a mudança envolver risco maior.

</details>

<details>
<summary><b>O que é uma release?</b></summary>

<br>

Uma **release** é uma versão preparada para quem usa o projeto. Ela reúne uma
tag, notas de atualização e, quando necessário, arquivos para download.

Crie uma release quando a versão estiver validada e pronta para consumo. Não é
necessário criar uma release para cada commit ou correção pequena.

</details>

## <img src="https://api.iconify.design/solar/users-group-rounded-bold.svg?color=%2310B981&width=24" align="top" /> &nbsp;Contribuição

Leia [CONTRIBUTING.md](CONTRIBUTING.md) antes de propor uma alteração. Use
issues para relatos reproduzíveis e pull requests para mudanças que precisam de
revisão. O GitHub gera automaticamente a lista de contribuidores a partir dos
commits, sem manter uma lista manual duplicada.

## <img src="https://api.iconify.design/solar/shield-check-bold.svg?color=%230EA5E9&width=24" align="top" /> &nbsp;Segurança

Nunca publique tokens, senhas, chaves privadas, cookies, arquivos `.env` ou
dados pessoais. Consulte [SECURITY.md](SECURITY.md) para comunicar uma falha
de segurança.

## <img src="https://api.iconify.design/solar/document-text-bold.svg?color=%230EA5E9&width=24" align="top" /> &nbsp;Licença

Este projeto é distribuído sob a [Licença MIT](LICENSE).
