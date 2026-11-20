# Produção visual no Codex e no Claude

Identifique os recursos da sessão antes de combinar a entrega. Um gerador de imagens é adequado para fotografia, aquarela e ilustração editorial. Um desenho por código dá controle sobre geometria, rótulos, cores, escala e dados.

## Quando estiver no Claude

Se o pedido envolver criação de imagens, explique logo no início a distinção para o pedido concreto. Uma mensagem possível é “O Claude pode criar diagramas e ilustrações vetoriais em SVG. Para gerar uma foto ou uma aquarela a partir de um prompt, esta sessão precisaria de um gerador de imagens conectado.” Adapte a frase se a sessão de fato tiver acesso autorizado a um gerador. Um PNG exportado de um desenho ou gráfico é uma renderização do desenho.

Se o usuário pedir fotografia, pintura ou acabamento que o vetor não reproduza, ofereça alternativas pertinentes. Pode usar uma imagem enviada para inserção, selecionar uma imagem publicada com licença verificável, criar uma versão esquemática ou entregar o prompt para um gerador externo. Se já houver autorização e uma opção adequada, siga com ela. [Recursos visuais do Claude](https://support.claude.com/pt/articles/9002504-claude-pode-produzir-imagens)

## SVG para ilustrações 2D

- Use `viewBox` com a proporção reservada no slide. Componha com formas, caminhos e texto. Use margem interna, contraste e espessuras de traço legíveis em projeção. Escreva título e descrição acessíveis quando útil.
- Salve um SVG autônomo. Use fontes de substituição e dispense dependências externas, scripts, handlers e elementos `foreignObject` no arquivo destinado ao PPTX. Confira se o texto continua legível com as fontes do ambiente de apresentação.
- Insira o SVG quando a ferramenta e o PowerPoint de destino o renderizarem corretamente. Caso contrário, exporte PNG na proporção do slide com resolução suficiente para a área que a figura ocupa. Guarde também o SVG como fonte reutilizável. Abra o resultado e confira a renderização na apresentação.

## Three.js para conteúdo espacial

Use Three.js quando girar um objeto, revelar um corte, comparar pontos de vista ou observar movimento ajudar a explicar o assunto. Uma comparação de sólidos, um modelo de relevo e a montagem de um mecanismo são bons candidatos. Um diagrama plano geralmente pode ser feito em SVG direto.

- Defina geometria, enquadramento e escala em função da aula. Em comparações, reutilize câmera, escala e convenções de cor. Marque simplificações se o modelo for conceitual.
- Para uma cena geométrica simples e uma vista vetorial, use o addon `SVGRenderer` e exporte a vista estática. Ele atende formas e superfícies simples. Para uma cena que dependa de texturas, sombras ou materiais, renderize com WebGL e exporte PNG. Three.js precisa de um ambiente que execute a biblioteca e o renderizador escolhido. Se ele não estiver disponível, faça uma vista isométrica ou um corte em SVG direto. [SVGRenderer](https://threejs.org/docs/pages/SVGRenderer.html) · [WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html)
- Insira um quadro estático no PPTX e verifique o recorte e os rótulos. Se o objetivo incluir interação e a sessão permitir produzi-la, entregue a cena HTML/JS como arquivo complementar e confira o carregamento e os controles. A figura no PPTX precisa continuar compreensível por si só.
