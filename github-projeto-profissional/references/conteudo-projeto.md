# Conteúdo do projeto e adaptação da apresentação

Leia esta referência ao criar ou revisar a apresentação completa de um projeto
ou ao analisar exemplos de README para incorporar boas práticas. Para detalhes
de SVG, badges, bandeiras e renderização, use [padrao-readme.md](padrao-readme.md).

## Descobrir antes de escrever

Inspecione código, manifestos e lockfiles, configuração de build/execução,
documentos, CI, testes existentes e histórico relevante. Use o que foi lido
para decidir quais seções servem ao leitor. Não execute instaladores nem
aplicações privilegiadas só para completar a documentação.

Uma captura comprova aparência e organização; não comprova versão, desempenho,
licença, segurança, maturidade ou compatibilidade. Adapte o princípio visual
ao projeto atual, sem copiar alegações, autoria ou tecnologia da referência.

Para cada afirmação relevante, identifique sua evidência e seu limite:

| Informação | Fonte a conferir | Distinção necessária |
| --- | --- | --- |
| Tecnologia e versão | Manifesto, lockfile, build e ambiente suportado | Versão mínima, intervalo aceito e versão resolvida são fatos diferentes |
| Recurso | Implementação, documentação e observação disponível | Presente no código não significa validado em execução |
| Instalação | Scripts, configuração, artefatos e pré-requisitos | Caminho documentado, experimentado e suportado não são equivalentes |
| Compatibilidade | Adaptadores, matriz de CI e verificações disponíveis | Compatibilidade presumida não vira “suportado” |
| Desempenho | Medição com ambiente e método | Não reutilize números de outro README |
| Privacidade | Fluxos de dados e dependências externas | Não afirme ausência total de transmissão com leitura parcial |
| Maturidade | Release, testes e critérios declarados pelo projeto | “Estável” e “produção” exigem evidência contextual |
| Origem e direitos | Histórico, créditos, LICENSE e NOTICE | Dono do fork não é automaticamente autor original |

Se faltar uma preferência que altera escopo, pergunte usando o seletor nativo
disponível. Reaproveite escolhas já feitas. Organização, contraste, links,
legibilidade e veracidade são trabalho do agente, não um questionário visual.

## Escolher seções pelo trabalho do leitor

Use a matriz como critério, não como lista de títulos obrigatórios. Uma correção
pontual não autoriza reestruturar todo o repositório.

| Necessidade do leitor | Quando incluir | Conteúdo útil |
| --- | --- | --- |
| Entender o produto | Sempre na apresentação | O que é, público, problema resolvido, escopo e estado atual |
| Encontrar funções | Há vários recursos | Recurso, comportamento e benefício concreto, sem repetir slogans |
| Saber se pode usar | Há requisitos ou restrições | Plataforma, versões, dependências, portas, permissões e motivo |
| Começar a usar | Existe um caminho utilizável | Pré-requisitos, instalação, configuração, primeiro uso e resultado esperado |
| Entender a interface | Há interface ou saída demonstrável | Visão geral e galeria com função e contexto de cada tela |
| Operar ou integrar | Há comandos, API ou serviços | Comandos, configuração, exemplos, diagnóstico e limites reais |
| Desenvolver | Há código mantido e contribuição prevista | Preparar ambiente, executar, compilar, testar e localizar módulos |
| Entender componentes | Arquitetura foi solicitada ou combinada | Responsabilidades, fluxo de dados, fronteiras e dependências verificadas |
| Navegar pelo código | Há vários diretórios | Árvore comentada; inventário individual quando solicitado |
| Achar documentação | Existem vários guias | Tabela por objetivo ou por documento, com links existentes |
| Avaliar integrações | Existem plataformas ou clientes distintos | Matriz de compatibilidade com versão, estado e restrições |
| Entender o que falta | Há planejamento real | Próximos passos com estado e ligação para backlog/documento mantido |
| Saber quem mantém | Responsáveis conhecidos | Mantenedor atual, autor original e contribuições de terceiros separados |
| Entender uso permitido | Sempre que distribuído | Licença real ou NOTICE, atribuições e limites de distribuição |

Não preencha uma seção sem conteúdo real. Num snapshot ainda não validado,
explique o limite e o material disponível para análise. Não invente comandos
de instalação seguros nem trate planejamento como funcionalidade entregue.

## Contexto, recursos e desenvolvimento

A introdução deve permitir responder “serve para mim?”: natureza do projeto,
quem o usa, qual dificuldade resolve e o que entrega. Evite abrir com diário
de alterações ou longos detalhes de implementação.

Use tabelas de recursos quando ajudarem a comparar: recurso, comportamento
observável e utilidade. Inclua requisitos com observações, como dependência
distribuída no pacote, componente opcional ou credencial fornecida pelo operador.
“Nenhuma dependência” deve indicar o escopo: sem pacotes externos não significa
sem runtime, sistema operacional ou serviço remoto.

Para desenvolvimento, documente comandos que realmente existem e o diretório
em que são executados. Diferencie iniciar a aplicação, gerar artefatos e rodar
testes. Informe configuração de exemplo sem segredos, resultado esperado e
limitações de validação. Não invente pipeline, cobertura ou política de releases.
Links de contribuição e segurança precisam ter procedimentos utilizáveis e
canais existentes, não só arquivos com títulos.

O README resume o desenvolvimento; decisões extensas, contratos de API,
arquitetura detalhada e diagnóstico vão em documentos próprios quando necessários.
Dados privados, logs de conversa e raciocínios internos não pertencem a esses guias.

## Navegação documental por objetivo

Quando houver vários guias, prefira uma tabela que traduza intenção em destino:

| Quero | Consultar |
| --- | --- |
| Preparar o ambiente | Guia de instalação existente |
| Entender cada componente | Documento de arquitetura existente |
| Investigar uma falha | Guia de diagnóstico existente |
| Conhecer limitações | Documento de estado/qualidade existente |

Substitua os destinos por links reais do repositório; nunca publique este exemplo
com destinos fictícios. Uma lista curta continua adequada a poucos documentos.
Não crie uma pasta de documentos vazios para preencher a tabela.

Em documentação multilíngue extensa, pode haver uma matriz
“Documento | Português | English | Español”. Só ofereça células com arquivos
existentes e conteúdo mantido; versões ausentes devem ser identificadas como
indisponíveis, sem links falsos. Esse formato complementa as bandeiras do
cabeçalho. Não exige traduzir toda a documentação sem combinar o escopo.

## Demonstrações e compatibilidade

Uma visão geral maior pode preceder pares de telas relacionadas. Cada imagem
precisa de legenda que explique a função, os dados de exemplo e o que está
realmente demonstrado. Escolha largura para manter textos legíveis e confira
como a tabela aparece em viewport estreito. Não use miniaturas ilegíveis para
fazer todas as telas caberem em uma linha.

Quando o pedido for reprodução no README, confira o player incorporado e sua
faixa de áudio; um link para download não cumpre a mesma função. Diferencie
captura real, reconstrução estática e imagem ilustrativa.

Grades de logos ajudam a reconhecer integrações, mas cada nome deve ter
destino útil e evidência de compatibilidade. Use tabela de suporte quando
versões e restrições importarem: integração, estado, versão verificada e limite.
Não deduza “funciona perfeitamente com todos” a partir de uma lista de logos.
Permissões de marca e licença dos ativos continuam aplicáveis.

## Modelos de badges, ícones e cores

Adapte o formato à informação, preservando preferências já informadas:

| Situação | Modelo adequado | Cuidados |
| --- | --- | --- |
| Stack com versões relevantes | Badge compacto de tecnologia e versão | Conferir a fonte; não promover dependência transitiva a componente principal |
| Identidade técnica no topo | Badge sólido em for-the-badge com logo | Nome curto, cor da marca e contraste legível |
| Estado do repositório | Badge menor em flat-square | Versão, licença, origem e estado devem ter fonte e link |
| Requisito ou plataforma | Badge ou linha de tabela | Explicar restrições; logo sozinho não informa compatibilidade |
| Autoria e créditos | Link de perfil ou badge discreto | Diferenciar autor, mantenedor e fornecedor de componente |

Cores de marca identificam tecnologias; cores semânticas comunicam estado.
Não atribua um significado de sucesso a algo que ainda não foi validado.
Use texto e rótulos, além da cor. Fundos claros precisam de texto/ícone escuro;
não resolva todo contraste trocando cores oficiais sem avaliar o resultado.
Quando o serviço não permitir o contraste desejado, escolha outro formato ou
um SVG verificável. Confirme o resultado entregue, não só os parâmetros da URL.

Não imponha fundo cinza ou cor sólida a todos os projetos. Escolha o modelo
compatível com o conteúdo e a preferência do mantenedor. Não copie a paleta
inteira de uma referência: escolha uma família de ícones de seção e uma paleta
semântica curta; logos de tecnologia podem conservar suas próprias cores.
Mantenha alinhamento, tamanho e espaçamento constantes.

Visibilidade privada não é licença. Um badge “privado” informa acesso; não
substitui LICENSE ou NOTICE. Não transfira licença MIT, número de versão ou
status de produção de exemplos visuais para o projeto analisado.

## Estado atual e próximos passos

Use “planejado”, “em estudo”, “em desenvolvimento” e “entregue” somente quando
sustentados pelo backlog, histórico ou confirmação do mantenedor. Não invente
roadmap para enriquecer a apresentação. Quando houver próximo passo conhecido,
descreva resultado pretendido, estado e link de acompanhamento. Datas exigem
compromisso real. Retire itens entregues do planejamento e registre mudanças
no changelog, preservando limites ainda abertos.

Não use uma lista extensa de ideias como interface do produto. Um resumo no
README aponta para o planejamento detalhado quando ele existe.

## Autoria, manutenção, créditos e licença

Uma apresentação de autoria pode ter avatar, nome, papel e links de perfil,
Issues e Releases que existam. Não crie uma release ou habilite recursos só
para preencher botões. Use avatar remoto apenas para uma identidade confirmada
e preserve a privacidade de e-mail e outros dados.

Separe explicitamente:

- autor e projeto de origem;
- mantenedor desta distribuição ou fork;
- contribuição específica de bibliotecas, ferramentas e ativos;
- licença de cada parte quando diferir da licença geral.

Uma tabela “Projeto | Contribuição | Licença/fonte” torna a atribuição útil.
O cartão do mantenedor não duplica a lista automática de contribuidores; não
o proíba só por já existirem autores no histórico. Não atribua a autoria de
código original ao dono do fork.

Registre ausência de licença em NOTICE sem inventar permissão. Diferencie código
próprio, componentes de terceiros, marcas e ativos não distribuídos quando isso
for relevante. Evite avisos legais genéricos copiados de outro produto.

## Revisão orientada ao leitor

Antes de concluir uma revisão completa, confira se as seções presentes respondem
às necessidades reais e se o leitor encontra primeiro uso, requisitos, limites
e documentação sem precisar entender o histórico da conversa. Verifique
coerência entre badges, manifestos, origem, estado, roadmap e licenças.
Leia a apresentação como alguém que acaba de chegar ao projeto.

Padrões visuais e tabelas são recursos de comunicação. Sua presença não comprova
qualidade técnica. Declare separadamente publicação e inspeção visual, e indique
qualquer validação que não pôde ser realizada.
