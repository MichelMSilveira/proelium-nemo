# Padrao de Projetos Assistidos por IA

Este diretorio define a base reutilizavel para projetos novos e para a normalizacao de projetos existentes.

## Principios

1. Cada repositorio e uma fonte de verdade independente.
2. Nunca transportar regras de negocio, processos, identidade ou conhecimento de outro projeto sem validacao explicita.
3. Distinguir sempre fato confirmado, inferencia, hipotese e sugestao.
4. Carregar apenas o contexto necessario para a tarefa atual.
5. Registrar decisoes importantes e o motivo.
6. Manter um estado curto e atual do projeto para retomada rapida.
7. Preservar historico no Git e evitar alteracoes amplas sem necessidade.
8. Nunca armazenar segredos, senhas, tokens ou dados privados em documentacao versionada.

## Estrutura recomendada

```text
projeto/
├── AGENTS.md
├── PROJECT.md
├── README.md
├── docs/
│   ├── STATUS.md
│   ├── REQUIREMENTS.md
│   ├── DECISIONS.md
│   ├── KNOWLEDGE.md
│   └── SESSION.md
├── .continue/
│   └── rules/
│       └── projeto.md
└── src/ ou estrutura nativa do projeto
```

## Ordem de leitura da IA

1. `AGENTS.md` - regras de trabalho e seguranca.
2. `PROJECT.md` - identidade, objetivo, escopo e limites do projeto.
3. `docs/STATUS.md` - estado atual e proximo passo.
4. Somente depois, os documentos especificos necessarios para a tarefa.

Nao carregar todos os documentos automaticamente.

## Uso em projeto novo

Copiar os arquivos-modelo deste diretorio, preencher `PROJECT.md` e `STATUS.md`, executar discovery e registrar requisitos antes de iniciar implementacoes significativas.

## Uso em projeto existente

Nao substituir regras especificas ja existentes. Incorporar somente os arquivos ausentes e preservar stack, arquitetura, operacao e historico do repositorio.
