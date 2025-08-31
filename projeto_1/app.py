from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir acesso do front-end

# Mock de IA baseado em regras simples
def gerar_conteudo_personalizado(idade, renda, objetivo):
    if idade < 25:
        perfil = "jovem"
    elif idade < 60:
        perfil = "adulto"
    else:
        perfil = "idoso"

    if renda < 2000:
        renda_desc = "baixa"
    elif renda < 7000:
        renda_desc = "média"
    else:
        renda_desc = "alta"

    conteudo = (
        f"Como uma pessoa {perfil} com renda {renda_desc}, seu foco em '{objetivo}' é excelente. "
        f"Recomendamos que você comece com uma reserva de emergência, seguida de investimentos de baixo risco. "
        f"A educação financeira é um passo importante para atingir seu objetivo!"
    )

    return conteudo

@app.route("/gerar-conteudo", methods=["POST"])
def gerar_conteudo():
    data = request.json
    idade = int(data.get("idade", 0))
    renda = float(data.get("renda", 0))
    objetivo = data.get("objetivo", "")

    conteudo = gerar_conteudo_personalizado(idade, renda, objetivo)
    return jsonify({"conteudo": conteudo})

if __name__ == "__main__":
    app.run(debug=True)
