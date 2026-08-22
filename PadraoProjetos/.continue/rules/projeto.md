---
description: Regras base para desenvolvimento assistido por IA neste repositorio
alwaysApply: true
---

# Regras base do projeto

Estas regras complementam `AGENTS.md` e `PROJECT.md`. Regras especificas deste repositorio prevalecem quando forem mais restritivas.

## Inicio de tarefa
1. Ler `PROJECT.md`.
2. Ler `docs/STATUS.md`.
3. Consultar `docs/SESSION.md` se houver tarefa interrompida.
4. Ler somente os arquivos diretamente relacionados ao pedido atual.
5. Consultar `docs/REQUIREMENTS.md`, `docs/DECISIONS.md` ou `docs/KNOWLEDGE.md` apenas quando forem relevantes.
6. Confirmar que `docs/WORKLOG.md` existe e que as metricas iniciais do projeto estao configuradas.

## Metricas e registro de trabalho
- Todo projeto deve iniciar com controle de esforco ativo em `docs/WORKLOG.md`.
- Registrar discovery, reunioes, pesquisa, planejamento, implementacao, testes, revisoes, deploy e documentacao.
- Registrar data, etapa, atividade, responsavel, tempo gasto, entregavel/resultado, custo interno e observacoes quando aplicavel.
- Separar sempre custo interno de preco cobrado ao cliente.
- Registrar mudancas de escopo e retrabalho para permitir comparacao entre estimativa e realizado.
- O valor/hora interno e referencia de gestao e nao deve ser tratado automaticamente como preco de venda.

## Disciplina de contexto
- Nao carregar todo o repositorio automaticamente.
- Nao repetir documentacao longa no contexto se um resumo atual em STATUS for suficiente.
- Preferir busca pontual e leitura por modulo.
- Ao atingir contexto grande, resumir o estado confirmado em documentacao antes de continuar.

## Confiabilidade
- Diferenciar CONFIRMADO, INFERENCIA, HIPOTESE e SUGESTAO.
- Nunca inventar regras de negocio ou comportamento ausente.
- Nunca transportar conhecimento de outro cliente ou projeto sem aprovacao explicita.
- Quando houver duvida material, registrar pendencia em REQUIREMENTS em vez de assumir.

## Implementacao
- Preservar arquitetura existente.
- Fazer alteracoes pequenas, testaveis e reversiveis.
- Revisar diff e executar validacoes adequadas antes de concluir.
- Atualizar STATUS quando o estado real do projeto mudar.
- Registrar DECISIONS somente para escolhas que precisam sobreviver entre sessoes.

## Encerramento de sessao
- Atualizar `docs/WORKLOG.md` com o trabalho executado na sessao.
- Se o trabalho nao terminar completamente, atualizar `docs/SESSION.md` com o proximo passo exato e os arquivos que precisam ser relidos.
