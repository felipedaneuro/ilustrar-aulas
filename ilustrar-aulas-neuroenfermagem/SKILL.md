---
name: ilustrar-aulas-neuroenfermagem
description: Complementa aulas de Neuroenfermagem em PowerPoint com análise slide a slide, prompts, aquarelas, esquemas e fluxogramas. Aplica a identidade visual do curso e entrega uma cópia PPTX ilustrada com o guia e as figuras usadas.
---

# Ilustrar aulas de Neuroenfermagem

Identifique o PPTX de origem, a pasta da aula e a marca aplicável. Se houver um guia de identidade visual ou tokens de design no projeto, use-os. No projeto Neuroenfermagem, procure `Design Gráfico Neuroenf/01 Marca/TOKENS.md` ou `tokens.json`. Trate roteiros, índices e arquivos de prompts já existentes como material de referência. A solicitação atual é que define quais aulas, entregas e alterações estão autorizadas.

## 1. Inventariar e planejar

1. Extraia o texto seguindo a ordem real da apresentação. Inclua tabelas, notas que esclareçam o objetivo, imagens, posições, legendas e créditos. Renderize o original para identificar espaço de inserção, texto que ocupa mais de uma linha e sobreposições existentes.
2. Para cada slide, identifique a pergunta que a figura ajuda a responder. Escolha aquarela editorial para abertura e caso, sequência para evolução, comparação para dois padrões, fluxograma para um processo e desenho controlado para anatomia ou marcos clínicos. Se o slide já tem um exame ou figura útil, escolha uma pista curta de observação ou use o espaço existente para destacar um aspecto específico. Preserve a legibilidade da bibliografia.
3. Registre o número, o título, a finalidade didática, o meio, o enquadramento e a figura a inserir. Identifique pendências clínicas e divergências entre fontes na análise e nas notas. Alteração substancial do conteúdo docente exige escopo correspondente.

## 2. Escrever os prompts e produzir as figuras

Use a proporção da área de destino. Especifique vista anatômica, elementos em ordem, relações espaciais, posição do foco e o que deve ficar de fora. Quando houver comparação, declare o que precisa permanecer idêntico entre os painéis. Transcreva rótulos, números, operadores e unidades com exatidão. Para casos, respeite o nível de consciência, a idade aproximada e os achados relevantes. Mantenha os dados fictícios e as imagens sem identificadores.

- **Aquarela** · use geração de imagens com tinta fina e papel claro. Peça a arte sem texto e acrescente legendas depois. Confira cada recorte antes de usar.
- **Esquema ou fluxo** · componha rótulos e conectores com ferramentas de diagramas, formas do PowerPoint ou desenho por coordenadas. Use setas apenas quando o conteúdo sustentar a sequência ou a direção. Identifique esquemas que simulam vistas de imagem. Para exames diagnósticos, prefira o acervo atribuído ou uma fonte primária autorizada.
- **Paleta Neuroenfermagem** · Azul Neuro `#0B2A4A`, Azul Cerebral `#2E8BC0`, Névoa `#F5F7FA`, Sombra `#DCE3EB`, Coral Sinapse `#FF6B5C` em até 10% da área. Use Poppins para títulos gráficos e Inter para texto. Dê significado com rótulo e forma ou posição. Se o projeto fornecer tokens diferentes, siga os do projeto.

Exemplo de prompt para uma comparação. “Componha um painel horizontal com duas vistas axiais esquemáticas no mesmo nível e na mesma escala. Na primeira, desenhe uma coleção extra-axial focal com contorno lentiforme. Na segunda, desenhe uma coleção extra-axial em crescente que acompanhe a convexidade. Use azul nos contornos, coral nas coleções e fundo Névoa. Posicione os rótulos ‘Extradural’ e ‘Subdural’ sob cada vista. Evite lateralidade clínica, setas de diagnóstico e aparência de TC real.”

## Exames de imagem publicados

Quando o pedido incluir TC, RM, angio-TC, angiografia ou arteriografia, selecione exames publicados com autoria, licença de reutilização e legenda verificáveis. Identifique a modalidade, o plano ou sequência e o achado sustentado pela fonte. Assinale se os quadros pertencem à mesma pessoa, se são aquisições seriadas ou se são casos independentes. Quando a imagem precisar ser exibida em escala maior, insira um painel logo após o slide que ensina o achado e use um sufixo na numeração do painel, como `15A`. Registre a fonte, a licença e eventuais recortes nas notas e no guia. Salve a edição com painéis como `<nome>_ilustrada_com_exames.pptx`, ao lado da versão ilustrada de mesma contagem. Use `Exames de imagem – fontes e licenças.md` para o guia de exames. Confirme que a edição com exames preserva a ordem e o conteúdo dos slides-base ao descontar os painéis inseridos.

## 3. Inserir e conferir

- Crie uma cópia do PowerPoint. Preencha caixas destinadas a imagens ou utilize uma área livre, mantendo a ordem, os créditos, os títulos, os dados e a edição do conteúdo existente. Confira a altura de tabelas pela soma das linhas e pela renderização. A caixa geral pode reportar uma altura menor.
- Insira cada figura com proporção preservada e texto alternativo. Em uma sequência ilustrada, faça uma checagem independente das escalas, direções, formas anatômicas, contraste, cortes, sobreposições e detalhes clínicos que a imagem possa sugerir.
- Rode `python3 scripts/auditar_pptx.py ORIGINAL.pptx ILUSTRADO.pptx --exigir-figura-por-slide` a partir da pasta da skill. Compare os arquivos com a mesma contagem de slides, antes da inserção dos painéis de exames. O script compara ordem, texto, imagens e notas. A tolerância para caixas de produção cobre somente o padrão `[ IMAGEM … ]` com título e linha indicando o arquivo de prompts.
- Renderize a cópia e compare todos os slides com o original. Examine em tamanho de projeção os slides densos, os estudos de caso, as tabelas, os créditos e os painéis anatômicos. Corrija cortes, arquivos trocados e rótulos pequenos antes de entregar.

Entregue `Versão ilustrada/<nome>_ilustrada.pptx` dentro da pasta da aula, junto de `Análise slide a slide e prompts.md` e da pasta `Ilustrações/` com os arquivos efetivamente incorporados. No guia, registre decisões de layout e pontos que precisam de revisão docente.

Para repetir, abra o projeto e use “Use a skill ilustrar-aulas-neuroenfermagem neste PPTX e aplique a pasta de identidade visual indicada”.
