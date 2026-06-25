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


documentos = []
nomes = []

for raiz, pastas, arquivos in os.walk(PASTA_CONHECIMENTO):

    for arquivo in sorted(arquivos):

        if arquivo.endswith(".txt"):

            caminho = os.path.join(raiz, arquivo)

            with open(caminho, "r", encoding="utf-8") as f:
                texto = f.read().strip()

            if texto:

                caminho_relativo = os.path.relpath(
                    caminho,
                    PASTA_CONHECIMENTO
                )

                documentos.append(texto)

                nomes.append(
                    caminho_relativo.replace("\\", "_")
                )


    print("==============================")
    print("MEMÓRIA PROELIUM CRIADA")
    print("==============================")
    print(f"Documentos carregados: {len(documentos)}")


    for nome in nomes:
        print("-", nome)


else:

    print("Nenhum documento encontrado.")