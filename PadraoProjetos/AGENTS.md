# Regras gerais para agentes de IA

Estas regras sao uma base reutilizavel. Regras especificas do repositorio sempre prevalecem quando forem mais restritivas ou detalhadas.

## Antes de agir
1. Ler `PROJECT.md` e `docs/STATUS.md`.
2. Identificar os arquivos e documentos diretamente relacionados a tarefa.
3. Nao carregar o repositorio inteiro sem necessidade.
4. Separar informacao confirmada de inferencia, hipotese e sugestao.
5. Preservar arquitetura, dados e comportamento existentes.

## Conhecimento
- Considerar cada repositorio independente.
- Nao transportar processos ou regras de negocio entre projetos sem autorizacao explicita.
- Registrar a origem de informacoes importantes em `docs/KNOWLEDGE.md`.
- Quando houver conflito entre fontes, sinalizar o conflito em vez de escolher silenciosamente.

## Implementacao
- Fazer a menor alteracao suficiente para cumprir a tarefa.
- Evitar refatoracoes amplas fora de escopo.
- Ler antes de editar e revisar o diff depois.
- Executar validacoes e testes adequados ao projeto.
- Nao declarar algo como concluido sem evidencia de validacao quando ela for possivel.

## Seguranca
- Nunca versionar senhas, tokens, chaves, backups privados ou dados sensiveis.
- Exigir autorizacao explicita para operacoes destrutivas, migracoes irreversiveis, alteracoes de autenticacao, producao ou reescrita de historico Git.

## Documentacao de continuidade
Ao concluir um bloco significativo de trabalho:
1. atualizar `docs/STATUS.md`;
2. registrar decisoes relevantes em `docs/DECISIONS.md`;
3. atualizar requisitos quando o escopo mudar;
4. deixar o proximo passo objetivo em `docs/SESSION.md` quando a tarefa ficar interrompida.

## Git
- Manter commits pequenos, coerentes e reversiveis.
- Incluir somente arquivos relacionados a tarefa.
- Seguir as regras de commit e deploy especificas do repositorio.
