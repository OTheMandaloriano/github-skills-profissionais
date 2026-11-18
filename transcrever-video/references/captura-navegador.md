# Captura de áudio pelo navegador (quando o YouTube bloqueia)

Use somente quando o `transcrever.py` sair com código **3** (`[FALLBACK]`) ou
quando o vídeo não tiver legenda e o download direto falhar.

A captura é **em tempo real** (1x). Vídeo de 10 min leva 10 min. Para vídeos
longos, insista no download direto antes de partir para cá.

## Requisitos

- MCP `browse` conectado ao Chrome real (sessão do usuário).
- Pasta de captura dentro de `%TEMP%` — nunca em `Downloads`.

## Passo 1 — capturar o áudio

Abra a página e rode o bloco abaixo em `tools.browse.execute`.
O áudio é gravado com ganho 0 no destino (silencioso), mas em nível cheio na
gravação.

```js
const r = await tools.browse.execute({
  code: `
await page.goto('URL_DO_VIDEO', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(4000);

const cap = await page.evaluate(async () => {
  const vids = [...document.querySelectorAll('video')];
  const v = vids.find(x => x.duration > 1) || vids[vids.length - 1];
  if (!v) return { err: 'sem video' };

  v.pause();
  v.muted = false;          // mute silencia a captura tambem
  v.volume = 1;
  v.playbackRate = 1;       // acima de 1x o audio muda
  try { v.currentTime = 0; } catch (e) {}
  await new Promise(r => setTimeout(r, 800));

  const ctx = new AudioContext({ sampleRate: 48000 });
  await ctx.resume();                       // sem gesture pode ficar suspended
  const src  = ctx.createMediaElementSource(v);
  const dest = ctx.createMediaStreamDestination();
  const mute = ctx.createGain(); mute.gain.value = 0;
  src.connect(dest);
  src.connect(mute); mute.connect(ctx.destination);   // mantem o grafo ativo

  const chunks = [];
  const rec = new MediaRecorder(dest.stream, {
    mimeType: 'audio/webm;codecs=opus',
    audioBitsPerSecond: 64000,
  });
  rec.ondataavailable = e => { if (e.data && e.data.size) chunks.push(e.data); };
  const stopped = new Promise(res => { rec.onstop = res; });

  rec.start(1000);
  await new Promise(r => setTimeout(r, 300));
  try { await v.play(); } catch (e) { return { err: 'play: ' + e }; }

  const t0 = Date.now();
  while (Date.now() - t0 < 900000 && v.currentTime < v.duration - 0.25) {
    await new Promise(r => setTimeout(r, 300));
  }

  rec.stop();
  await stopped;
  const blob = new Blob(chunks, { type: 'audio/webm' });
  return await new Promise(res => {
    const fr = new FileReader();
    fr.onload = () => res({ b64: fr.result.split(',')[1], size: blob.size, dur: v.duration });
    fr.readAsDataURL(blob);
  });
});
if (cap.err) return cap;

const p = files.path('transcrever-video-captura/video.webm');
await files.write(p, Buffer.from(cap.b64, 'base64'));
return { path: p, size: cap.size, dur: cap.dur };
`,
  timeoutMs: 0,   // a captura dura o tempo do video
});
```

Notas:

- `page.evaluate` roda em mundo isolado (Patchright). Ele **não** alcança os
  hooks de `MediaSource` da página — por isso a captura usa `AudioContext`,
  que compartilha o DOM.
- Shorts avançam sozinhos ao terminar. Pare em `duration - 0.25`; não espere
  `ended`, senão entra o próximo vídeo na gravação.
- Se o resultado for grande, devolva o base64 em partes e concatene com
  `copy /b parte1+parte2 video.webm`.

## Passo 2 — transcrever e apagar

Use a duração real informada pelo player (`cap.dur`):

```powershell
python "C:\Users\<usuario>\.config\opencode\skills\transcrever-video\scripts\transcrever.py" `
  "C:\Users\<usuario>\AppData\Local\Temp\transcrever-video-captura\video.webm" `
  --lang pt --model small --duration <dur> --cleanup-input
```

O `--cleanup-input` apaga o `.webm` após a transcrição.

## Passo 3 — conferir resíduo

```powershell
Get-ChildItem "$env:TEMP\transcrever-video-captura" -ErrorAction SilentlyContinue
Get-ChildItem "$env:TEMP" -Filter "transcrever-video-*" -ErrorAction SilentlyContinue
```

As duas listas devem sair vazias. Se a pasta de captura continuar existindo
(arquivo em uso), apague com `Remove-Item -Recurse -Force`.

## O que não fazer

- Não baixe pelo menu do Chrome nem com `<a download>` — cai em `Downloads`.
- Não salve frames/screenshots "para conferir".
- Não instale plugin de PO token nem exporte cookies para disco.
