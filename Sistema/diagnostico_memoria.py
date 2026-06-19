import chromadb

cliente = chromadb.PersistentClient(
    path="conhecimento.db"
)

print("=== DIAGNÓSTICO MEMÓRIA PROELIUM ===")

colecoes = cliente.list_collections()

print("\nColeções encontradas:")

for c in colecoes:
    print("-", c.name)

    colecao = cliente.get_collection(c.name)

    dados = colecao.get()

    print("Quantidade de documentos:", len(dados["documents"]))

    print("---------------------------")

print("\nDiagnóstico concluído.")