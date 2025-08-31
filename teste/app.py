# app.py
def coletar_dados():
    nome = input("Digite seu nome completo: ")
    idade = input("Digite sua idade: ")
    experiencia = input("Descreva sua experiência profissional: ")
    return {
        "nome": nome,
        "idade": idade,
        "experiencia": experiencia
    }

def salvar_json(dados, arquivo="dados.json"):
    import json
    with open(arquivo, "w") as f:
        json.dump(dados, f)

if __name__ == "__main__":
    dados = coletar_dados()
    salvar_json(dados)
    print("Dados salvos em dados.json")