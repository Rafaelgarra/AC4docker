import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def fibrobos():
    numeronovo = 0
    posição_lista = 0
    brobos1 = [0, 1]
    brobos = " 0, 1, "
    while len(brobos1) < 51:
        numeronovo += brobos1[posição_lista-1]
        numeronovo = brobos1[posição_lista] + brobos1[posição_lista+1]
        brobos += (str(numeronovo)) + ", "
        brobos1.append(numeronovo)
        posição_lista += 1
    return(brobos)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
