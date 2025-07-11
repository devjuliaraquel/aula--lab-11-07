from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

USUARIO_CADASTRADO="julia"
SENHA_CADASTRADO="123"

@app.route("/login", methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method=="POST":

        usuario = request.form['nome_login']
        senha = request.form['pass_login']

        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADO:
            resposta = make_response(redirect(url_for('bemvindo')))
            resposta.set_cookie('username', usuario, max_age = 60*30)

            return resposta
        else:
            #'texto com aspas/'simples/''+'/''

            mensagem = "Usuario ou senha inválidos. Tente novamente."

    return render_template('login1.html', erro=mensagem) 

@app.route('/bemvindo')
def bemvindo():
   username = request.cookies.get('username')

   if not username:
      return redirect(url_for('login'))
   return render_template('bemvindo_form.html', user=username)


@app.route('/logout')
def logout():
    resposta=make_response(redirect(url_for('login')))

    resposta.set_cookie('username', '', expires=0)
    #deixar de existir agr, nesse ponto

    return resposta

if __name__ == '__main__':
    app.run(debug=True)



# cookie é uma variavel local, experiencias do usuario

# tela login, bem vindo

#requwst.form, puxa as varieveis direto do formulario