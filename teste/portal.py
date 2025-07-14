from flask import Flask, render_template, request

app = Flask(__name__)

noticias = {
    "esportes": [
        {"titulo": "Brasil vence a Argentina", "conteudo": "Notícia sobre a vitória do Brasil."},
        {"titulo": "Novo recorde mundial", "conteudo": "Notícia sobre o novo recorde mundial."},
        {"titulo": "Palmeiras foi eliminado da copa de clubes"}
    ],
    "entreterimento": [
        {"titulo": "Lançamento do novo iPhone", "conteudo": "Notícia sobre o lançamento do novo iPhone."},
        {"titulo": "Inteligência artificial avança", "conteudo": "Notícia sobre o avanço da inteligência artificial."},
        {"titulo": "lançamento do live-action de como treinar o seu dragão atrai multidão pros cinema" }
    ],
    "lazer": [
        {"titulo": "Exposição de arte em São Paulo", "conteudo": "Exposição de arte em SP é dedica a artista brasileira Tarsila do Amaral."},
        {"titulo": "Oscar: 2025, Brasil e mais", "conteudo": "Brasil ganha seu primeiro oscar por Ainda Estou Aqui, na categoria melhor filme internacional."},
    ],
}

@app.route("/")
def index():
    categorias = list(noticias.keys())
    return render_template("index.html", categorias=categorias)

@app.route("/categoria/<nome_categoria>")
def noticias_por_categoria(nome_categoria):
    if nome_categoria in noticias:
        return render_template("categoria.html", categoria=nome_categoria, noticias=noticias[nome_categoria])
    else:
        return "Categoria não encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)