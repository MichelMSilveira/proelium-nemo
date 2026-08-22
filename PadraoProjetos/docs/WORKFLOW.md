# WORKFLOW DE PROJETO

## Comando conceitual: INICIAR

Use ao abrir um projeto novo.

1. Ler `AGENTS.md` se existir.
2. Preencher `PROJECT.md`.
3. Executar `docs/DISCOVERY.md`.
4. Criar ou atualizar requisitos.
5. Registrar fontes de conhecimento.
6. Definir o primeiro incremento pequeno e verificavel.
7. Atualizar `docs/STATUS.md`.

## Comando conceitual: RETOMAR

Use ao continuar um projeto existente.

1. Ler `AGENTS.md`.
2. Ler `PROJECT.md`.
3. Ler `docs/STATUS.md`.
4. Ler `docs/SESSION.md` somente se houver contexto operacional complementar.
5. Ler `REQUIREMENTS`, `DECISIONS` ou `KNOWLEDGE` somente quando a tarefa exigir.
6. Conferir o pedido atual contra o estado registrado.
7. Continuar da menor proxima acao valida.

## Comando conceitual: ENCERRAR

Use antes de fechar uma sessao de trabalho relevante.

1. Atualizar `docs/STATUS.md` com o estado real.
2. Registrar decisoes novas em `docs/DECISIONS.md`.
3. Atualizar requisitos alterados ou confirmados.
4. Registrar novas fontes em `docs/KNOWLEDGE.md`.
5. Atualizar `docs/SESSION.md` com:
   - o que foi feito;
   - arquivos principais alterados;
   - testes executados;
   - pendencias;
   - proximo passo recomendado.
6. Nao registrar segredos, credenciais ou dados privados.

## Comando conceitual: AUDITAR CONTEXTO

Use quando o projeto estiver confuso, antigo ou com documentacao divergente.

1. Comparar implementacao atual com `PROJECT.md` e `STATUS.md`.
2. Marcar documentacao obsoleta.
3. Nao corrigir regras de negocio por inferencia.
4. Consolidar apenas fatos comprovados pelo repositorio ou pelo usuario.
5. Registrar lacunas como pendencias.

## Regra de contexto

Evitar recarregar todo o historico em cada interacao. O estado atual deve ser suficientemente pequeno para permitir retomada rapida, e documentos historicos devem ser consultados sob demanda.
