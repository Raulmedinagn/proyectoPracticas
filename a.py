from flask import Flask, redirect, url_for, render_template, request, jsonify

from pruebanltk import Analizar
from bbdd import BBDD

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        frase = request.form["fr"]
        return redirect(url_for("analizar", frase_recogida=frase))
    else:
        return render_template("index.html")


@app.route('/analizar/<frase_recogida>')
def analizar(frase_recogida):
    lista = Analizar().analizar_frase(frase_recogida)
    # para convertirlo a string
    palabras_importantes = " ".join(lista)
    return palabras_importantes


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        email = request.form["email"]
        print(nombre)
        BBDD.insert(nombre, edad, email)
        return redirect(url_for("bbdd"))
    else:
        return render_template('login.html')


@app.route('/bbdd')
def bbdd():
    items = []
    for item in BBDD.db:
        items.append(item)
    return jsonify(items)


if __name__ == "__main__":
    app.run(debug=True)
