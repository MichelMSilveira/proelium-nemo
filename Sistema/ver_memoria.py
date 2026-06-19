import chromadb

cliente = chromadb.PersistentClient(
    path="conhecimento.db"
)

colecao = cliente.get_collection(
    name="proelium"
)

dados = colecao.get()

print("TOTAL:", len(dados["documents"]))

for i, doc in enumerate(dados["documents"]):
    print("\n==============================")
    print("DOCUMENTO:", i+1)
    print("==============================")
    print(doc[:500])