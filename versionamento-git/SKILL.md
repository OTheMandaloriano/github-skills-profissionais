---
name: versionamento-git
description: Padrão universal de versionamento — descobrir a convenção do repositório, 1 commit por mudança lógica com título categorizado em pt-BR, verificar de fato que o remoto recebeu, e o procedimento seguro para corrigir histórico já enviado. Use ao terminar qualquer alteração de código, config ou documentação que deva ser versionada, e sempre que for commitar, enviar ou corrigir histórico em qualquer projeto.
---

# Versionamento: commit por mudança

Toda mudança concluída vira um commit claro, atômico e rastreável, e chega
ao remoto. O título tem de ser entendido de imediato por uma pessoa **e**
por uma IA que abra o repositório daqui a seis meses.

Isto vale para **qualquer projeto**. Nada aqui é específico de um domínio.

## Quando esta skill age

Use o verbo do pedido para definir o escopo:

- **Explicar, comparar, revisar ou diagnosticar:** responda ou inspecione em
  modo leitura. Não crie commit, branch, tag, release ou arquivo de suporte.
- **Implementar, corrigir ou atualizar:** altere e valide localmente. Não faça
  push sem pedido explícito de publicação ou autorização já existente.
- **Publicar ou enviar atualização:** revise, crie commits coesos e faça push
  somente do que pertence ao pedido.
- **Preparar ou publicar release:** avalie versão, changelog, tag, validação e
  notas da release. Não crie release apenas porque houve um commit.

Ao abrir uma conversa nova dentro de um projeto, confira o estado do Git para
entender o contexto, mas não o altere por iniciativa própria. Se a pasta não
tiver `.git`, só pergunte sobre iniciar ou conectar um repositório quando o
usuário tiver pedido início, organização, versionamento ou publicação do
projeto. Uma dúvida comum nunca autoriza criar arquivos ou histórico.

## Linguagem e escopo do histórico

Commits, changelog, tags, releases, nomes de branch e arquivos devem descrever
o projeto e a mudança técnica. Não mencione usuário, IA, agente, prompt, chat,
conversa, aprovação ou instruções de bastidor. O histórico precisa fazer
sentido para alguém que abra o repositório sem conhecer a conversa original.

Exemplo inadequado: `[fix] corrige o que o usuário pediu no chat`.
Exemplo adequado: `[fix] renova a sessão antes de consultar limites`.

Não adicione ao stage arquivos temporários, exportações de chat, rascunhos ou
artefatos sem função no produto. Se houver dúvida sobre a origem ou necessidade
de um arquivo, deixe-o fora do commit e informe o motivo.

---

## 1. Descobrir a convenção antes de escrever

**Nunca invente categoria.** Antes do primeiro commit numa base:

```bash
git log --format="%s" -30          # que formato este repositório já usa?
```

Ordem de precedência:

1. Convenção declarada no `CLAUDE.md`, `CONTRIBUTING.md` ou similar
2. O que o `git log` mostra que o repositório já pratica
3. O padrão abaixo, quando não há nenhuma das duas

Se o projeto define uma lista fechada de categorias, **ela é a lista**. Uma
categoria fora dela não é criatividade, é ruído. E quando o projeto tem
categoria de domínio, ela vence a genérica: trabalho de contrato é
`[contratos]`, não `[fix]`.

**Padrão quando o repositório não tem convenção:**

`[categoria] descrição clara e específica`

| Categoria | Para |
|---|---|
| `feat` | funcionalidade nova |
| `fix` | correção de defeito |
| `perf` | desempenho, sem mudar comportamento |
| `refactor` | reorganização sem mudança de comportamento |
| `docs` | documentação |
| `test` | testes |
| `build` | dependências, empacotamento |
| `ci` | automação de integração |
| `sec` | segurança |
| `chore` | manutenção que não cabe acima |

---

## 2. O título

Em pt-BR, **com acentos**, técnico, sem caixa alta gritada. Diga o que
mudou e, se couber na linha, por quê.

- Ruim: `[fix] ajustes`
- Ruim: `[fix] CORRIGIDO O BUG DO TEMPO`
- Bom: `[fix] O relógio do contrato vem do item, e não do bloco de contrato`

**Sem trailer de ferramenta ou IA.** Nada de `Co-Authored-By: Claude`,
`Generated with`, ou menção a modelo. O histórico é do projeto.

---

## 3. O corpo: onde mora o valor

O título diz o quê. O corpo diz **por quê**, e é o que sobrevive.

Escreva o corpo quando houver:

- **Uma causa não óbvia.** O que parecia ser o problema, e o que era.
- **Um caminho errado percorrido.** Registrar a hipótese derrubada vale mais
  que registrar a solução: impede que alguém a tente de novo.
- **Uma decisão com alternativa descartada.** Diga qual e por que perdeu.
- **Um risco ou impacto.** O que passa a ser possível quebrar.
- **Evidência.** Números medidos, não adjetivos. "5/5, 36/36, 39/39" prova
  mais que "conferido".

Não escreva corpo para mudança óbvia. Um `[docs] corrige link quebrado` não
precisa de parágrafo.

## Commit, último autor e changelog

Antes de registrar um commit, agrupe mudanças que entregam uma mesma intenção.
Uma correção que precisa de código, teste e atualização documental pode ficar
no mesmo commit. Separe mudanças independentes, como uma correção de defeito e
uma reorganização visual não relacionada.

Revise o diff preparado, não só o diff da pasta inteira:

```bash
git status --short
git diff --cached
```

A mensagem do commit resume a intenção do conjunto de alterações, sem tentar
descrever cada arquivo individualmente. O GitHub associa essa mensagem aos
arquivos incluídos naquele commit e exibe, em cada caminho, o commit mais
recente que o alterou. Por isso, um commit coerente torna a navegação e a
auditoria do repositório mais confiáveis.

O `CHANGELOG.md` é outro registro. Ele reúne mudanças relevantes do projeto
para quem atualiza, mantém ou avalia versões. Não transforme cada commit em
uma entrada de changelog. Atualize-o quando a alteração mudar comportamento,
segurança, compatibilidade, distribuição ou experiência de uso, seguindo o
formato já adotado pelo repositório.

Faça o commit quando a unidade de trabalho estiver concluída e validada. Não
espere acumular correções sem relação só para reduzir a quantidade de commits,
mas também não registre etapas incompletas, salvo se o projeto usar commits
WIP de forma explícita. Depois do commit, envie-o ao remoto quando o fluxo do
projeto ou a tarefa autorizar publicação.

Uma release é menos frequente que um commit. Crie-a somente para uma versão
pronta para consumo, com tag, testes adequados, changelog revisado e notas que
expliquem como atualizar. Vários commits podem formar uma release; uma simples
correção pode receber commit e push sem gerar release.

Use notas de release profissionais, escritas para quem consome o produto. Elas
devem resumir destaques, correções, compatibilidade, passos de atualização e
limitações relevantes, quando existirem. Não despeje a lista bruta de commits,
não invente benefícios e não publique release vazia.

---

## 4. Fluxo

**0. Identidade e autoria (Foto de Perfil do GitHub).** Antes de commitar, confirme que o Git está configurado com o nome e o e-mail noreply da sua própria conta GitHub. Nunca use a identidade de outra pessoa. Consulte em GitHub > Settings > Emails o endereço noreply associado à sua conta e configure localmente:

```bash
git config user.name "<seu nome de usuário GitHub>"
git config user.email "<seu endereço noreply do GitHub>"
```

Substitua os dois exemplos pelos dados da sua própria conta antes de executar os comandos.

**1. Repositório e remoto.** Confirme que existe. Se não houver, avise e
sugira `git init` mais o remoto; nunca invente credencial.

**2. Gate de segurança.** Antes de `git add`:

```bash
git diff | grep -inE "password|senha|secret|token|api[_-]?key|BEGIN (RSA|PRIVATE)"
```

Nenhuma linha **adicionada** pode conter segredo. Se houver, pare. Versione
`.env.example`, jamais `.env`.

**3. Revisar.** `git status` e `git diff`. Confira o volume: se um arquivo de
80 linhas aparece com 900 alteradas, é fim de linha convertido, não código.
Veja a seção 5.

**4. `git add` só do que pertence à mudança.** Não use `git add -A` sem olhar
o `git status` antes. Confira `git diff --cached` e remova do stage tudo que
não pertence à intenção do commit.

**5. Commitar** no formato acima.

**6. Enviar, e conferir que chegou.** Isto é um passo, não uma formalidade:

```bash
git push origin <branch>
git status -sb          # deve dizer "main...origin/main", sem "ahead"
```

> Commits parados localmente são invisíveis para quem lê o repositório.
> Já aconteceu de o usuário passar horas lendo um README desatualizado no
> GitHub enquanto a correção existia só em disco. **Nunca dizer que foi
> enviado sem ter conferido.** Se o push falhar, relate o erro real.

**7. Registrar continuidade.** Se a mudança altera o estado do projeto,
atualize o `CHANGELOG.md` (ou o registro de histórico equivalente) **no
mesmo commit** ou no seguinte. Documentação que contradiz o código é pior
que documentação ausente: a ausente não engana.

---

## 5. Fim de linha: a armadilha silenciosa

Um arquivo com CRLF editado por ferramenta que grava LF vira **diff do
arquivo inteiro**, e a mudança real se perde no ruído. Pior é a mistura dos
dois no mesmo arquivo, que não aparece em revisão nenhuma.

Fixe no `.gitattributes`:

```
* text=auto
*.js   text eol=crlf      # ajuste às linguagens do projeto
*.patch -text             # patches nunca são normalizados
```

Ao editar por script, **preserve o fim de linha original**. Em Python:
`io.open(p, encoding="utf-8", newline="")` na leitura e na escrita. Cuidado
com `sed -i`, que converte. Confira depois:

```bash
tr -cd '\r' < arquivo | wc -c      # CR
tr -cd '\n' < arquivo | wc -c      # LF; iguais = CRLF, CR=0 = LF
```

---

## 6. Código que vive em dois lugares

Quando o repositório é cópia de algo que roda em outro caminho (uma
instalação, um servidor, uma pasta de trabalho), **nunca sincronize por
cópia cega**.

Antes de copiar, olhe **as duas direções**:

```bash
diff repo/arquivo vivo/arquivo | grep "^<"    # o que só o repo tem
diff repo/arquivo vivo/arquivo | grep "^>"    # o que só o vivo tem
```

Se o repositório tem linhas que a cópia viva não tem, elas podem ser código
de upstream, ou de outra pessoa, que a sua cópia nunca recebeu. Copiar por
cima apaga sem aviso. Nesse caso, **porte só os seus trechos**.

---

## 7. Corrigir histórico já enviado

**Regra: não reescrever histórico enviado.** `--force` é destrutivo e
apaga trabalho de quem mais tenha o repositório.

Quando o usuário **autoriza explicitamente**, o procedimento é este, e ele
não é opcional:

```bash
# 1. rede de segurança
git tag -f antes-da-correcao HEAD

# 2. guardar a árvore, para provar que o conteúdo não muda
git rev-parse HEAD^{tree}

# 3. simular antes de gravar
for c in $(git rev-list <base>..HEAD | tac); do
    git log -1 --format=%B $c | sed '1s/^\[antigo\]/[novo]/' | head -1
done

# 4. reescrever
FILTER_BRANCH_SQUELCH_WARNING=1 \
  git filter-branch -f --msg-filter 'sed "1s/^\[antigo\]/[novo]/"' <base>..HEAD

# 5. conferir: a árvore tem de ser a MESMA, e os corpos têm de existir
git rev-parse HEAD^{tree}
git log --format="%s" <base>..HEAD

# 6. enviar com trava, não com force seco
git push --force-with-lease origin <branch>

# 7. limpar o resto
git for-each-ref --format="%(refname)" refs/original/ | \
  while read r; do git update-ref -d "$r"; done
```

**Cuidado com o `--msg-filter`:** ele recebe a mensagem por stdin e devolve
por stdout. Um filtro que consome stdin sem repassar **apaga todas as
mensagens do repositório**. Já aconteceu: `grep -q <<< "$(cat)"` engoliu a
entrada e zerou o histórico, recuperado só pelo reflog. Use um `sed` simples,
que lê e escreve.

`--force-with-lease` aborta se o remoto tiver avançado. `--force` seco
atropela. Prefira sempre o primeiro.

---

## 8. Cuidados

- Sempre usar o `user.name` e o `user.email` noreply oficiais da sua própria conta GitHub. Nunca reutilize os dados de outra pessoa.
- Nunca versionar `.env`, tokens, chaves, dumps ou binários grandes sem
  necessidade.
- Não commitar trabalho pela metade que deixe o projeto sem construir.
- Não misturar refactor, feature e fix no mesmo commit.
- Se estiver no branch principal e a mudança for arriscada, criar branch
  antes.
- Rodar os hooks e testes que existirem, e não pular com `--no-verify`.
- Se o push falhar por credencial ou rede, **relate o erro real**. Não
  presuma sucesso.

