<div align="center">

<img src="https://api.iconify.design/solar/code-square-bold.svg?color=%2310B981&width=72" alt="Skills profissionais para GitHub" width="72" height="72" />

# Skills profissionais para GitHub

Instruções reutilizáveis em pt-BR para estruturar projetos no GitHub e manter um histórico de mudanças claro, coeso e pronto para colaboração.

[![Codex](https://img.shields.io/badge/Codex-Skills-10A37F?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/codex/)
[![Git](https://img.shields.io/badge/Git-Versionamento-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repositórios-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

[![Idioma](https://img.shields.io/badge/idioma-pt--BR-009C3B?style=flat-square)](README.md)
[![Licença](https://img.shields.io/badge/licença-MIT-0EA5E9?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-pronto_para_uso-10B981?style=flat-square)](CHANGELOG.md)

</div>

## <img src="https://api.iconify.design/solar/compass-bold.svg?color=%230EA5E9&width=24" align="top" /> &nbsp;O que este projeto oferece

Este repositório reúne duas skills complementares. Uma organiza a apresentação
e os recursos de um projeto no GitHub. A outra governa o ciclo de alterações,
commits, changelog, tags e publicação.

As skills distinguem dúvida, diagnóstico, trabalho local, publicação e release.
Elas não criam repositórios, arquivos, branches, commits ou releases quando a
pessoa apenas pede uma explicação ou uma revisão.

| Skill | Para que serve |
| --- | --- |
| [`github-projeto-profissional`](github-projeto-profissional/SKILL.md) | Organiza README, arquitetura, demonstrações, About, Topics, Releases, Deployments, Packages e branches. |
| [`versionamento-git`](versionamento-git/SKILL.md) | Mantém commits coesos, revisa o diff preparado, atualiza changelog quando necessário e publica com segurança. |

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

## <img src="https://api.iconify.design/solar/box-bold.svg?color=%2310B981&width=24" align="top" /> &nbsp;Compatibilidade e instalação

As instruções usam o formato aberto `SKILL.md`, compatível com Codex, Claude
Code e OpenCode. O conteúdo é o mesmo; cada ferramenta usa uma pasta de
instalação própria.

Copie as duas pastas para um destes caminhos e reinicie a ferramenta:

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

Os instaladores interrompem a execução se encontrarem uma skill com o mesmo
nome. Use `-Force` no PowerShell ou `--force` no shell somente depois de revisar
a atualização que será aplicada.

## <img src="https://api.iconify.design/solar/rocket-2-bold.svg?color=%23F97316&width=24" align="top" /> &nbsp;Uso

Use pedidos naturais. A intenção do verbo define o fluxo:

| Pedido | Resultado esperado |
| --- | --- |
| “Explique como funcionam branches.” | Resposta no chat, sem alterar projeto. |
| “Revise este repositório.” | Diagnóstico em modo leitura. |
| “Vamos começar este projeto.” | Avaliação da pasta e organização somente do que for necessário. |
| “Corrija este problema.” | Implementação e validação local. |
| “Corrija e publique esta atualização.” | Revisão, commit coeso e push. |
| “Prepare uma release.” | Avaliação de versão, changelog, tag e notas. |

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
