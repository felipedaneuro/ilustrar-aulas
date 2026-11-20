---
name: ilustrar-aulas
description: Ilustra aulas em PowerPoint de qualquer assunto. Analisa slide a slide, escreve prompts e incorpora imagens e diagramas em uma cópia ilustrada com guia de produção.
---

# Ilustrar aulas

Identifique a apresentação de origem, o público, o objetivo da aula e a identidade visual indicada. Use os slides e materiais de apoio como fontes de conteúdo. Preserve o original e salve os resultados na pasta da aula.

Use as ferramentas de imagem, diagramação e edição de PPTX disponíveis na sessão. Quando a geração de imagens estiver indisponível, produza esquemas com ferramentas de desenho ou use figuras com licença verificável. Se a sessão não puder editar o PPTX, entregue a análise, os prompts e as instruções de inserção e informe qual arquivo ficou pendente.

## 1. Analisar slide a slide

Extraia os textos, tabelas, imagens, notas relevantes e créditos na ordem de apresentação. Renderize o original para conferir o espaço disponível e a hierarquia visual. Em cada slide, defina o que a imagem deve ajudar a reconhecer, comparar, localizar ou entender. Se uma figura já cumpre esse papel, considere manter a composição ou acrescentar uma pista de leitura.

Escolha o formato pela tarefa didática. Use uma ilustração editorial, fotografia ou aquarela para contextualizar uma situação. Use mapa, linha do tempo, gráfico, sequência, desenho anotado ou fluxograma para representar relações que o aluno precisa interpretar. Preserve o momento de revelar as respostas dos exercícios.

## 2. Escrever os prompts e produzir as imagens

Para cada nova figura, registre o assunto, o objetivo didático, o estilo, o enquadramento, a proporção, os elementos essenciais e os rótulos que devem ser exatos. Em comparações, mantenha escala, ponto de vista e codificação visual coerentes. Use a paleta e a tipografia indicadas ou derive-as do material existente.

- **Imagem editorial** · escolha o estilo adequado ao assunto e ao público. Gere a arte sem texto e insira as legendas na apresentação.
- **Diagramas, mapas e gráficos** · componha os rótulos e conectores com ferramentas de desenho ou formas do PowerPoint. Use os dados fornecidos para escalas, valores, unidades e tendências. Identifique reconstruções, exemplos fictícios e desenhos conceituais.
- **Material publicado** · em fotografias, obras, documentos, mapas e exames, confirme autoria, fonte, licença e eventuais condições de reutilização. Registre adaptações. Quando usar exames clínicos, descreva somente os achados sustentados pela fonte e indique se os quadros mostram o mesmo caso ou casos independentes.

Exemplo de prompt. “Crie uma ilustração horizontal para uma aula de Geografia do 7º ano sobre o efeito da vegetação no escoamento superficial. Mostre duas encostas de mesma inclinação sob chuva equivalente, uma vegetada e outra com solo exposto. Use setas da mesma cor para representar a água, com espessuras coerentes com a comparação qualitativa. Use estilo de aquarela didática, contornos finos e fundo claro. Reserve espaço abaixo dos painéis para os rótulos do professor. Evite números sem dados de origem.”

## 3. Inserir e conferir

- Trabalhe em uma cópia do PowerPoint. Mantenha a ordem, o conteúdo editável, as notas e os créditos. Insira as imagens com proporção preservada e texto alternativo. Ao usar um painel adicional, posicione-o após o slide que o contextualiza e use um sufixo na numeração, como `15A`.
- Compare a edição ilustrada de mesma contagem com a origem usando `python3 scripts/auditar_pptx.py ORIGINAL.pptx ILUSTRADO.pptx` a partir da pasta da skill. Acrescente `--exigir-figura-por-slide` quando o pedido exigir uma nova imagem em cada slide. Se houver painéis adicionais, confira também a sequência e a preservação dos slides-base na edição expandida.
- Renderize a cópia e confira legibilidade, contraste, sobreposição, recortes, dados, rótulos e relação entre texto e figura. Registre dúvidas de conteúdo no guia para revisão docente.

Entregue a cópia na subpasta `Versão ilustrada`, junto a `Análise slide a slide e prompts.md` e `Ilustrações/` com os arquivos incorporados. Quando houver material publicado, registre os créditos e licenças no guia e nas notas dos painéis pertinentes.
