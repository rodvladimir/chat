# https://cdnjs.com/
# pip install python-socketio flask-socketio simple-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar pagina = 1ª rota
@app.route("/")

def homepage():
    return render_template("index.html")

# roda o aplicativo
socketio.run(app, host="localhost")
