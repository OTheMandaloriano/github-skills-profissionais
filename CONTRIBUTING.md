# Como contribuir

Este repositório é uma coleção de skills independentes. Cada pasta na raiz com
`SKILL.md` é uma skill instalável; `scripts/` na raiz guarda os instaladores e o
validador.

Contribuições devem melhorar a precisão e a reutilização das skills sem
transformá-las em manuais genéricos.

## Antes de abrir um pull request

1. Mantenha cada mudança focada em uma intenção.
2. Escreva instruções que funcionem em projetos diferentes, sem assumir uma
   conta, organização ou repositório específico.
3. Não inclua dados pessoais, tokens, cookies, prompts ou relatos de conversa.
4. Declare as dependências da skill (veja abaixo).
5. Rode o validador e corrija o que ele apontar.
6. Explique o motivo da mudança e o comportamento que ela melhora.

## Criar uma skill nova

1. Crie a pasta na raiz com o nome da skill, em minúsculas e com hífens.
2. Escreva `SKILL.md` com frontmatter: `name` igual ao nome da pasta e
   `description` dizendo o que faz e quando usar.
3. Coloque código em `scripts/` e material de apoio em `references/`, sempre
   referenciado por caminho relativo dentro do `SKILL.md`.
4. Se a skill precisar de pacotes, inclua `requirements.txt` e um instalador
   próprio em `scripts/`, mais a instrução de verificação no `SKILL.md`.
5. Atualize a tabela de skills e o guia de escolha no `README.md`.
6. Registre a mudança no `CHANGELOG.md`.

O instalador descobre as skills pela presença de `SKILL.md`, então a pasta nova
já entra na instalação sem editar script.

## Dependências

Uma skill que depende de software externo precisa resolver isso sozinha:
verificar o que falta, instalar sem exigir administrador quando possível e
avisar em uma linha antes de instalar. Nenhuma skill instala pacote em silêncio.

Quando a instalação global for bloqueada pelo sistema (PEP 668), documente o
caminho com ambiente virtual e a remoção dele no fim.

## Validação

```powershell
python scripts\validar_skills.py
```

```bash
python3 scripts/validar_skills.py
```

O validador confere, para cada pasta com `SKILL.md`: frontmatter presente,
`name` igual ao nome da pasta, `description` utilizável, caminhos citados que
existem de fato e scripts Python que compilam. Ele não avalia a qualidade do
texto — isso é revisão humana.

Para skills com dependências, rode também a verificação da própria skill antes
de abrir o pull request:

```powershell
python transcrever-video\scripts\transcrever.py --check
```

## Escopo

Use uma issue antes de propor uma alteração ampla que mude o escopo de uma
skill ou adicione uma dependência pesada.
