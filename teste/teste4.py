from flask import Flask
from flask_session import Session

app = Flask(__name__)

# Configure o Flask-Session
app.config["SESSION_TYPE"] = "filesystem"  # Armazenamento em sistema de arquivos
Session(app)

