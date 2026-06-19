import chromadb
from chromadb.utils import embedding_functions

cliente = chromadb.PersistentClient(
    path="conhecimento.db"
)

funcao_embedding = embedding_functions.OllamaEmbeddingFunction(
    model_name="nomic-embed-text",
    url="http://localhost:11434/api/embeddings"
)

colecao = cliente.get_collection(
    name="proelium",
    embedding_function=funcao_embedding
)

resultado = colecao.query(
    query_texts=["qual o padrão profissional da Proelium?"],
    n_results=2
)

print(resultado["documents"])