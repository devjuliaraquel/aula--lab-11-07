from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

USUARIO_CADASTRADO = "julia"
SENHA_CADASTRADO = "123"

noticias = {
    "esportes": [
        {"titulo": "Brasil vence a Argentina", "conteudo": "Notícia sobre a vitória do Brasil."},
        {"titulo": "Novo recorde mundial", "conteudo": "Notícia sobre o novo recorde mundial."},
        {"titulo": "Palmeiras foi eliminado da copa de clubes", "conteudo": "Notícia sobre a eliminação do Palmeiras."}
    ],
    "entreterimento": [
        {"titulo": "Lançamento do novo iPhone", "conteudo": "Notícia sobre o lançamento do novo iPhone."},
        {"titulo": "IA avança", "conteudo": "Notícia sobre o avanço da inteligência artificial."},
        {"titulo": "Live-action de como treinar o seu dragão atrai multidão", "conteudo": "Notícia sobre novo filme."}
    ],
    "lazer": [
        {"titulo": "Exposição de arte", "conteudo": "Notícia sobre a exposição de arte."},
        {"titulo": "Novo filme brasileiro", "conteudo": "Notícia sobre o novo filme."},
        {"titulo": "Festival de música", "conteudo": "Festival atrai milhares."}
    ]
}

@app.route("/login", methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method == "POST":
        usuario = request.form['nome_login']
        senha = request.form['pass_login']

        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADO:
            resposta = make_response(redirect(url_for('bemvindo')))
            resposta.set_cookie('username', usuario, max_age=60*30)
            resposta.set_cookie('visitas', '0', max_age=60*30)
            resposta.set_cookie('tema', 'claro', max_age=60*30)
            return resposta
        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."

    return render_template('login1.html', erro=mensagem)

@app.route("/bemvindo")
def bemvindo():
    username = request.cookies.get('username')
    visitas = int(request.cookies.get('visitas', 0)) + 1
    tema = request.cookies.get('tema', 'claro')

    if not username:
        return redirect(url_for('login'))

    resposta = make_response(render_template('bemvindo_form.html', user=username, visitas=visitas, tema=tema))
    resposta.set_cookie('visitas', str(visitas), max_age=60*30)
    return resposta

@app.route("/noticias")
def noticias_page():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    categoria = request.args.get('categoria')
    ultima_categoria = categoria or request.cookies.get('ultima_categoria', 'esportes')
    tema = request.cookies.get('tema', 'claro')

    resposta = make_response(render_template("esporte1.html", user=username, categoria=ultima_categoria, noticias=noticias.get(ultima_categoria, []), tema=tema))
    if categoria:
        resposta.set_cookie('ultima_categoria', categoria, max_age=60*30)
    return resposta

@app.route("/tema/<modo>")
def escolher_tema(modo):
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    if modo not in ['claro', 'escuro']:
        modo = 'claro'
    resposta = make_response(redirect(url_for('bemvindo')))
    resposta.set_cookie('tema', modo, max_age=60*30)
    return resposta

@app.route("/logout")
def logout():
    resposta = make_response(redirect(url_for('login')))
    for cookie in ['username', 'visitas', 'tema', 'ultima_categoria']:
        resposta.set_cookie(cookie, '', expires=0)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)
