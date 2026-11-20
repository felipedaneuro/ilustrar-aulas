# Ilustrar Aulas

O `ilustrar-aulas` é uma skill para o Codex e o Claude que ajuda a transformar apresentações didáticas de qualquer assunto. Ela analisa os slides e decide onde uma aquarela, fotografia, ilustração, mapa, gráfico ou fluxograma ajuda o público a entender o conteúdo. A entrega inclui prompts reutilizáveis e uma cópia ilustrada do PowerPoint.

## Instalação

O Codex e o Claude Code usam a mesma pasta `ilustrar-aulas/`. Clone o repositório e copie a pasta inteira para o destino da sua plataforma.

```sh
git clone https://github.com/felipedaneuro/ilustrar-aulas.git ilustrar-aulas-repo
```

| Plataforma | No projeto | Para todos os seus projetos | Invocação explícita |
| --- | --- | --- | --- |
| Codex | `.agents/skills/` | `~/.agents/skills/` | `$ilustrar-aulas` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | `/ilustrar-aulas` |

Se já houver uma cópia instalada, compare as versões antes de substituir. [Instalação no Codex](https://developers.openai.com/api/reference/cli) · [Skills no Claude Code](https://support.claude.com/en/articles/14554922-claude-code-user-faq)

### Claude no navegador ou no app

No clone, gere o ZIP abaixo. Ele contém a skill, o guia de produção visual e o script de auditoria.

```sh
git archive --format=zip --output=ilustrar-aulas.zip HEAD ilustrar-aulas
```

No Claude, abra **Customize → Skills → + → Create skill → Upload a skill** e envie `ilustrar-aulas.zip`. Depois, habilite a skill e anexe a apresentação na conversa. A conta e o workspace precisam ter o recurso de skills habilitado. [Importação de skills no Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Estrutura do ZIP](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

## Como usar

Abra o projeto ou anexe o PPTX. Se a direção estiver aberta, a skill sugere caminhos visuais e pergunta sobre estilo, cores, tema e preferências. Anexe exemplos para inspirar a composição ou indique as imagens que devem entrar nos slides.

> Use a skill ilustrar-aulas para ilustrar esta aula de Geografia para o 7º ano. Preserve o conteúdo e proponha mapas, comparações ou esquemas onde a imagem ajudar a explicar o assunto. Entregue o PPTX ilustrado e os prompts de cada figura.

A subpasta `Versão ilustrada` reúne a cópia do PowerPoint, as figuras e o guia `Análise slide a slide e prompts.md`. Quando houver imagens publicadas, o guia registra as fontes, as licenças e eventuais adaptações. Exames clínicos entram somente quando ajudam a explicar o conteúdo da aula. A criação de imagens e a edição do PPTX dependem dos recursos disponíveis na sessão. Se a edição estiver indisponível, a skill entrega a análise, os prompts e as instruções de inserção.

## Opções de produção visual

Quando há geração de imagens na sessão, a skill pode usá-la para fotografias, aquarelas e ilustrações editoriais. No Claude, a criação por código inclui SVG. A geração de uma foto ou pintura a partir de um prompt depende de um gerador separado. Three.js é uma opção quando profundidade, rotação ou cortes explicam o assunto. A cena pode ter uma vista SVG ou PNG para o slide e um arquivo interativo à parte, quando pertinente. [Recursos visuais do Claude](https://support.claude.com/pt/articles/9002504-claude-pode-produzir-imagens) · [Guia de produção visual](ilustrar-aulas/references/producao-visual.md)

## Auditoria do PowerPoint

O script incluído usa Python 3 e a biblioteca padrão. Execute-o no diretório do repositório para comparar arquivos com a mesma contagem de slides.

```sh
python3 ilustrar-aulas/scripts/auditar_pptx.py   /caminho/para/original.pptx /caminho/para/ilustrado.pptx
```

O script verifica dimensões e preservação de texto, notas e imagens de origem por posição. Acrescente `--exigir-figura-por-slide` para cobrar uma nova imagem em cada slide. A edição com painéis adicionais requer uma conferência da posição dos novos slides e da sequência original. Use a renderização para verificar legibilidade, sobreposições e recortes.
