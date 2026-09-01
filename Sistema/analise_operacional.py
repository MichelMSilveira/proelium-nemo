"""Gera um resumo operacional somente leitura a partir dos dados do Proelium."""

from datetime import date, datetime, timedelta


def _data(valor):
    if isinstance(valor, datetime):
        return valor.date()
    if isinstance(valor, date):
        return valor
    try:
        return date.fromisoformat(str(valor)[:10])
    except (TypeError, ValueError):
        return None


def _texto(item, *campos):
    for campo in campos:
        valor = item.get(campo)
        if valor:
            return str(valor)
    return "Sem identificação"


def analisar_dados(dados, hoje=None, dias_oportunidade_parada=5):
    """Retorna fatos e recomendações sem modificar ``dados``.

    O resultado é deliberadamente simples para poder ser exibido na interface,
    auditado e enriquecido pelo modelo local em uma etapa posterior.
    """
    hoje = _data(hoje) or date.today()
    alertas = []
    tarefas = dados.get("tasks", []) or []
    oportunidades = dados.get("opportunities", []) or []
    compromissos = dados.get("appointments", []) or []

    for tarefa in tarefas:
        prazo = _data(tarefa.get("due") or tarefa.get("deadline"))
        status = str(tarefa.get("status", "")).lower()
        encerrada = any(palavra in status for palavra in ("conclu", "finaliz", "cancel"))
        if prazo and prazo < hoje and not encerrada:
            alertas.append({
                "tipo": "tarefa_atrasada",
                "prioridade": "alta",
                "titulo": _texto(tarefa, "title", "name"),
                "responsavel": _texto(tarefa, "assignee", "responsible"),
                "prazo": prazo.isoformat(),
                "recomendacao": "Revisar o responsável e registrar o próximo passo.",
            })

    for oportunidade in oportunidades:
        etapa = str(oportunidade.get("stage", "")).lower()
        if etapa in {"ganha", "perdida", "fechada", "concluída", "concluida"}:
            continue
        referencia = _data(oportunidade.get("updatedAt") or oportunidade.get("nextDue"))
        if referencia and hoje - referencia >= timedelta(days=dias_oportunidade_parada):
            alertas.append({
                "tipo": "oportunidade_parada",
                "prioridade": "media",
                "titulo": _texto(oportunidade, "company", "name", "title"),
                "responsavel": _texto(oportunidade, "owner", "responsible"),
                "referencia": referencia.isoformat(),
                "recomendacao": "Confirmar a próxima ação ou registrar o motivo da espera.",
            })

    for compromisso in compromissos:
        data_compromisso = _data(compromisso.get("date") or compromisso.get("due"))
        status = str(compromisso.get("status", "")).lower()
        if data_compromisso == hoje and "cancel" not in status:
            alertas.append({
                "tipo": "compromisso_hoje",
                "prioridade": "media",
                "titulo": _texto(compromisso, "title", "subject", "name"),
                "responsavel": _texto(compromisso, "assignee", "responsible"),
                "data": hoje.isoformat(),
                "recomendacao": "Confirmar preparação e participantes.",
            })

    ordem = {"alta": 0, "media": 1, "baixa": 2}
    alertas.sort(key=lambda item: (ordem.get(item["prioridade"], 9), item["tipo"], item["titulo"]))
    return {
        "gerado_em": hoje.isoformat(),
        "somente_leitura": True,
        "totais": {
            "tarefas_atrasadas": sum(item["tipo"] == "tarefa_atrasada" for item in alertas),
            "oportunidades_paradas": sum(item["tipo"] == "oportunidade_parada" for item in alertas),
            "compromissos_hoje": sum(item["tipo"] == "compromisso_hoje" for item in alertas),
        },
        "alertas": alertas,
    }


if __name__ == "__main__":
    print("Use analisar_dados(dados) para gerar o resumo operacional.")
