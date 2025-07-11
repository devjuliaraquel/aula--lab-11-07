from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False  # Define que a sessão não é permanente (expira ao fechar o navegador)
app.config["SESSION_TYPE"] = "filesystem"  # Define o tipo de armazenamento da sessão (ex: sistema de arquivos)
Session(app)


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return f"Acesso número: {session['count']}"

if __name__ == '__main__':
    app.run(debug=True)