---
name: transcrever-video
description: Transcreve a fala de vídeos (YouTube, Shorts, arquivos locais) e entrega o texto no chat sem deixar arquivos residuais. Use quando pedirem para transcrever, extrair o que foi falado, gerar legenda/legendas ou resumir o conteúdo falado de um vídeo. Exporta TXT/SRT/JSON/MD/PDF somente quando o usuário pedir e escolher a pasta.
---

# Transcrever vídeo

Extrai o que foi falado em um vídeo e devolve **texto no chat**. Arquivo só
existe se o usuário pedir a exportação e disser onde salvar.

## Regra de ouro — resíduo zero

| Permitido | Proibido |
| --- | --- |
| Pasta temporária do sistema, apagada automaticamente no fim | Salvar áudio, vídeo, WAV, frames ou screenshots no projeto, Desktop, Downloads ou pasta atual |
| Cache compartilhado do modelo Whisper (reutilizado entre execuções) | Deixar `.part`, `.ytdl`, `.tmp`, capturas de navegador ou exports não pedidos |
| Exportar para a pasta que o usuário escolheu, quando ele pedir | Criar pasta de saída "padrão" ou exportar por conta própria |

Regras duras:

1. Todo trabalho acontece em `%TEMP%\transcrever-video-*`; a pasta é removida no fim da execução.
2. Nunca grave nada no diretório do projeto, no Desktop, em `Downloads` ou no cwd.
3. Nunca salve frames, screenshots ou o vídeo original para "conferir depois".
4. Se o usuário não pediu exportação, o resultado é **somente o texto no chat**.
5. Se o usuário pediu exportação, pergunte a pasta antes de gravar. Nunca assuma destino.
6. Ao terminar, confirme em uma linha: `resíduo: 0`.

Exceção documentada: o modelo do Whisper fica em `%USERPROFILE%\.cache\huggingface`
(ou no cache do faster-whisper). É dependência compartilhada, não resíduo por vídeo.
Para remover: apague `models--Systran--faster-whisper-<modelo>`.

## Dependências

| Dependência | Papel | Obrigatória |
| --- | --- | --- |
| Python 3.9+ | Executa o script | Sim |
| `faster-whisper` | Transcrição (modelo Whisper em CPU) | Sim |
| `yt-dlp` | Download do áudio de URLs | Sim (só para URL) |
| `ffmpeg` ou `imageio-ffmpeg` | Conversão para WAV 16 kHz | Sim |

**Regra:** antes do primeiro uso na sessão, rode o check. Se faltar algo, rode o
instalador uma vez, avise em uma linha e continue. Nunca instale pacote no meio
de um pedido sem dizer.

```powershell
# checar
python "...\scripts\transcrever.py" --check
# instalar (Windows)
powershell -ExecutionPolicy Bypass -File "...\scripts\instalar_dependencias.ps1"
```

```bash
# macOS / Linux
./scripts/instalar_dependencias.sh --check
./scripts/instalar_dependencias.sh
```

O instalador usa `pip install --user` (não exige administrador) e valida
`ffmpeg` no PATH ou o binário embutido do `imageio-ffmpeg`. Se o ambiente for
gerenciado (PEP 668), crie um venv:

```powershell
python -m venv "$env:TEMP\venv-transcrever"
& "$env:TEMP\venv-transcrever\Scripts\python.exe" -m pip install -r "...\requirements.txt"
```

Nesse caso, aponte o venv no comando de transcrição e apague a pasta no fim
(ela também é resíduo).

## Fluxo padrão

1. **Receba a fonte**: URL do YouTube/Shorts ou caminho de arquivo local.
2. **Rode o script** (caminho absoluto, sem `cd`):

   ```powershell
   python "C:\Users\<usuario>\.config\opencode\skills\transcrever-video\scripts\transcrever.py" "<url-ou-arquivo>" --lang pt --model small
   ```

3. **Devolva no chat** o texto com timestamps. Se o pedido for "resuma", entregue o resumo **e** a transcrição.
4. **Não crie arquivos.** Se o usuário pedir exportação, veja a seção abaixo.
5. **Confirme a limpeza** (uma linha, sem drama).

### Parâmetros úteis

| Parâmetro | Quando usar |
| --- | --- |
| `--lang pt` / `--lang auto` | Idioma fixo ou detecção automática |
| `--model small` | Padrão: rápido e bom para português |
| `--model medium` | Nomes próprios, sotaque forte, áudio ruim (mais lento) |
| `--prompt "OpenWA, WAHA, Baileys..."` | Lista de nomes/temas para acertar termos técnicos |
| `--duration 96.7` | Corta o áudio no segundo exato (captura de navegador, shorts) |
| `--cleanup-input` | Apaga o arquivo de entrada depois de transcrever (capturas do agente) |

## Exportação sob demanda

Só execute quando o usuário pedir explicitamente **e** informar a pasta.

```powershell
python "...\transcrever.py" "<fonte>" --format md,txt,srt,json,pdf --out "D:\Caminho\Escolhido" --name "nome-base"
```

| Formato | Uso |
| --- | --- |
| `md` | Leitura humana, com timestamps |
| `txt` | Texto puro com timestamps |
| `srt` | Legenda para player/editor |
| `json` | Segmentos com start/end para automação |
| `pdf` | Documento paginado, sem dependência externa |

Sem `--out`, o script recusa exportar (código de saída 2). Isso é intencional.

## Quando o YouTube bloquear (HTTP 403 / SABR)

O script tenta `android_music`, `android_vr`, `web_safari/tv_embedded` e `mweb`.
Se todos falharem, ele sai com código **3** e imprime `[FALLBACK]`.

Nesse caso, siga `references/captura-navegador.md`: captura o áudio pelo player
do navegador para a pasta temporária, transcreve com `--cleanup-input` e apaga
a pasta. A captura é em tempo real (1x), então prefira o download direto quando
ele funcionar.

## Erros comuns

| Sintoma | Causa | Saída |
| --- | --- | --- |
| `403 Forbidden` | YouTube exigindo PO token/SABR | Fallback de navegador |
| `ffmpeg nao encontrado` | Sem ffmpeg no PATH | `pip install imageio-ffmpeg` (o script usa o binário embutido) |
| Texto vazio | Áudio mudo ou vídeo sem fala | Informe e pare; não invente conteúdo |
| Nomes errados | Modelo pequeno | `--model medium` + `--prompt` com os termos |
| Demora > 2x a duração | Modelo grande em CPU | Avise o tempo estimado antes de rodar |

## Checklist antes de responder

- [ ] Dependências checadas (`--check`) e instaladas se faltavam
- [ ] Rodei em pasta temporária e ela foi apagada
- [ ] Não há arquivo novo em `Downloads`, projeto ou Desktop
- [ ] Se exportei, foi para a pasta escolhida pelo usuário
- [ ] Entreguei a transcrição no chat (não só o caminho de um arquivo)
- [ ] Linha final: `resíduo: 0`

## Estrutura da skill

```
transcrever-video/
├── SKILL.md
├── requirements.txt
├── scripts/
│   ├── transcrever.py
│   ├── instalar_dependencias.ps1
│   └── instalar_dependencias.sh
└── references/
    └── captura-navegador.md
```

Dependências: `faster-whisper`, `yt-dlp`, `imageio-ffmpeg` (opcional se houver ffmpeg no PATH).
