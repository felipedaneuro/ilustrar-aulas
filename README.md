# Ilustrar Aulas

O `ilustrar-aulas` é uma skill para o Codex que ajuda a transformar apresentações didáticas de qualquer assunto. Ela analisa os slides e decide onde uma aquarela, fotografia, ilustração, mapa, gráfico ou fluxograma ajuda o público a entender o conteúdo. A entrega inclui prompts reutilizáveis e uma cópia ilustrada do PowerPoint.

## Instalação

Com acesso a este repositório, clone-o e copie a pasta `ilustrar-aulas` para `.agents/skills/` na raiz do projeto das aulas.

```sh
git clone https://github.com/felipedaneuro/ilustrar-aulas.git ilustrar-aulas-repo
cd /caminho/para/seu/projeto
mkdir -p .agents/skills
cp -R /caminho/para/ilustrar-aulas-repo/ilustrar-aulas .agents/skills/
```

Para disponibilizar a skill em todos os seus projetos, use `~/.agents/skills/` como destino. Se já houver uma cópia instalada, compare as versões antes de substituir.

## Como usar

Abra o projeto no Codex e indique o PPTX ou a pasta das aulas, o público e a identidade visual, quando houver.

> Use $ilustrar-aulas para ilustrar esta aula de Geografia para o 7º ano. Preserve o conteúdo e proponha mapas, comparações ou esquemas onde a imagem ajudar a explicar o assunto. Entregue o PPTX ilustrado e os prompts de cada figura.

A subpasta `Versão ilustrada` reúne a cópia do PowerPoint, as figuras e o guia `Análise slide a slide e prompts.md`. Quando houver imagens publicadas, o guia registra as fontes, as licenças e eventuais adaptações. A criação e a renderização dos slides usam os recursos disponíveis na sessão do Codex.

## Auditoria do PowerPoint

O script incluído usa Python 3 e a biblioteca padrão. Execute-o no diretório do repositório para comparar arquivos com a mesma contagem de slides.

```sh
python3 ilustrar-aulas/scripts/auditar_pptx.py   /caminho/para/original.pptx /caminho/para/ilustrado.pptx
```

O script verifica dimensões e preservação de texto, notas e imagens de origem por posição. Acrescente `--exigir-figura-por-slide` para cobrar uma nova imagem em cada slide. A edição com painéis adicionais requer uma conferência da posição dos novos slides e da sequência original. Use a renderização para verificar legibilidade, sobreposições e recortes.
