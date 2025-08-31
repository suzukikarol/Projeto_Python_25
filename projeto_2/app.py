from flask import Flask, render_template, request

app = Flask(__name__)

def gerar_curriculo(nome, escolaridade, experiencia):
    return f"""
    CURRÍCULO PROFISSIONAL

    Nome: {nome}

    Escolaridade:
    {escolaridade}

    Experiência Profissional:
    {experiencia}

    Perfil:
    Profissional dedicado, com forte capacidade de adaptação, trabalho em equipe e foco em resultados.
    """

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        escolaridade = request.form["escolaridade"]
        experiencia = request.form["experiencia"]
        curriculo = gerar_curriculo(nome, escolaridade, experiencia)
        return render_template("resultado.html", curriculo=curriculo)
    return render_template("index.html")

if __name__ == "__main__":
    print("Rodando app.py, abra no navegador: http://127.0.0.1:5000/")

    app.run(debug=True)
