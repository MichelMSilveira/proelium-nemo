import os
import chromadb
from chromadb.utils import embedding_functions


PASTA_CONHECIMENTO = r"G:\NEMO\Conhecimento"


cliente = chromadb.PersistentClient(
    path="G:\\NEMO\\Sistema\\conhecimento.db"
)


funcao_embedding = embedding_functions.OllamaEmbeddingFunction(
    model_name="nomic-embed-text",
    url="http://localhost:11434"
)


# Apaga coleção antiga para recriar memória limpa
try:
    cliente.delete_collection("proelium")
    print("Memória antiga removida.")
except:
    pass


colecao = cliente.create_collection(
    name="proelium",
    embedding_function=funcao_embedding
)


documentos = []
nomes = []


for arquivo in sorted(os.listdir(PASTA_CONHECIMENTO)):

    if arquivo.endswith(".txt"):

        caminho = os.path.join(PASTA_CONHECIMENTO, arquivo)

        with open(caminho, "r", encoding="utf-8") as f:
            texto = f.read().strip()


        if texto:
            documentos.append(texto)
            nomes.append(arquivo)


if documentos:

    colecao.add(
        documents=documentos,
        ids=nomes
    )


    print("==============================")
    print("MEMÓRIA PROELIUM CRIADA")
    print("==============================")
    print(f"Documentos carregados: {len(documentos)}")


    for nome in nomes:
        print("-", nome)


else:

    print("Nenhum documento encontrado.")