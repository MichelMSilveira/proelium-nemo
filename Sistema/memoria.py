"""Recria a memória semântica da N.E.M.O. a partir do conhecimento local."""

import os
from pathlib import Path

import chromadb
from chromadb.utils import embedding_functions


BASE_DIR = Path(__file__).resolve().parents[1]
PASTA_CONHECIMENTO = Path(
    os.getenv("NEMO_KNOWLEDGE_DIR", str(BASE_DIR / "Conhecimento"))
).expanduser()
CAMINHO_MEMORIA = Path(
    os.getenv("NEMO_DB_PATH", str(BASE_DIR / "Sistema" / "conhecimento.db"))
).expanduser()
NOME_COLECAO = os.getenv("NEMO_COLLECTION", "proelium")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODELO_EMBEDDING = os.getenv("NEMO_EMBEDDING_MODEL", "nomic-embed-text")


def carregar_documentos(pasta: Path):
    """Retorna textos e identificadores estáveis dos arquivos de conhecimento."""
    if not pasta.is_dir():
        raise FileNotFoundError(f"Pasta de conhecimento não encontrada: {pasta}")

    documentos = []
    nomes = []
    for caminho in sorted(pasta.rglob("*.txt")):
        texto = caminho.read_text(encoding="utf-8").strip()
        if texto:
            nomes.append(caminho.relative_to(pasta).as_posix())
            documentos.append(texto)
    return documentos, nomes


def criar_memoria():
    documentos, nomes = carregar_documentos(PASTA_CONHECIMENTO)
    CAMINHO_MEMORIA.parent.mkdir(parents=True, exist_ok=True)

    cliente = chromadb.PersistentClient(path=str(CAMINHO_MEMORIA))
    funcao_embedding = embedding_functions.OllamaEmbeddingFunction(
        model_name=MODELO_EMBEDDING,
        url=OLLAMA_URL,
    )

    try:
        cliente.delete_collection(NOME_COLECAO)
    except Exception:
        pass

    colecao = cliente.create_collection(
        name=NOME_COLECAO,
        embedding_function=funcao_embedding,
    )

    if documentos:
        colecao.add(
            ids=[f"doc-{indice:05d}" for indice in range(len(documentos))],
            documents=documentos,
            metadatas=[{"source": nome} for nome in nomes],
        )

    print("==============================")
    print("MEMÓRIA N.E.M.O. CRIADA")
    print("==============================")
    print(f"Pasta: {PASTA_CONHECIMENTO}")
    print(f"Documentos carregados: {len(documentos)}")
    print(f"Coleção: {NOME_COLECAO}")
    for nome in nomes:
        print("-", nome)


if __name__ == "__main__":
    criar_memoria()
