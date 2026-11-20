# Ilustrar aulas de Neuroenfermagem

Skill para o Codex que analisa apresentações PowerPoint slide a slide, cria prompts e incorpora aquarelas, esquemas e fluxogramas. Usa a identidade visual indicada e entrega uma cópia ilustrada com um guia de produção. Quando solicitado, inclui painéis de exames publicados com legendas, créditos e licenças.

## Instalação

Com acesso a este repositório, clone-o e copie a pasta da skill para `.agents/skills/` na raiz do projeto onde ficam as aulas.

```sh
git clone https://github.com/felipedaneuro/ilustrar-aulas-neuroenfermagem.git
cd /caminho/para/seu/projeto
mkdir -p .agents/skills
cp -R /caminho/para/o/clone/ilustrar-aulas-neuroenfermagem/ilustrar-aulas-neuroenfermagem .agents/skills/
```

Se já houver uma cópia instalada, compare as versões antes de substituí-la. Para disponibilizar a skill em todos os projetos do usuário, use `~/.agents/skills/` como destino. Se a lista de skills já estiver aberta no Codex, reinicie a sessão para atualizar a descoberta.

## Como usar

Abra o projeto no Codex e informe o PPTX ou a pasta das aulas. Indique os arquivos da marca se quiser usar uma identidade visual própria.

> Use $ilustrar-aulas-neuroenfermagem para ilustrar este PPTX slide a slide. Aplique a paleta da pasta de identidade visual e inclua exames publicados nos pontos em que ajudam a reconhecer o achado.

Cada aula recebe uma subpasta `Versão ilustrada` com o PPTX, o guia `Análise slide a slide e prompts.md` e as figuras incorporadas. Quando houver painéis extras, a edição `_ilustrada_com_exames.pptx` reúne as ilustrações e os exames. O guia de fontes e licenças fica na mesma pasta.

A geração de imagens e a renderização das apresentações usam as ferramentas disponíveis no ambiente do Codex. A auditoria estrutural requer apenas Python 3 e a biblioteca padrão.

## Auditoria do PowerPoint

No diretório do repositório clonado, compare o original à edição ilustrada com a mesma contagem de slides.

```sh
python3 ilustrar-aulas-neuroenfermagem/scripts/auditar_pptx.py \
  /caminho/para/original.pptx /caminho/para/ilustrado.pptx \
  --exigir-figura-por-slide
```

O script confere as dimensões, a sequência, a preservação de textos, notas e imagens de origem, e a inclusão de imagens novas. Nas edições com painéis adicionais, audite primeiro a versão de mesma contagem e depois confira a posição dos painéis e a preservação dos slides-base. Renderize a apresentação para verificar legibilidade, sobreposições e recortes.

A publicação de cada exame segue a licença da fonte correspondente.
