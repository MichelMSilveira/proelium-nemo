import requests

while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        break

    resposta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "nemo",
            "prompt": pergunta,
            "stream": False
        }
    )

    dados = resposta.json()

    print("\nN.E.M.O.:")
    print(dados["response"])