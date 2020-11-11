from flask import Flask, redirect, url_for, render_template, request, jsonify

# para consultar los json
import requests

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
    
    # miramos en el json de la comunidad de madrid, abuelos de viaje
    urlcomunidadmadrid1 = "https://datos.comunidad.madrid/catalogo/dataset/1ff1f579-6a2d-4356-a244-34a2c0ad3fa4/resource/23294b86-d813-4487-905d-7d1c4f97d191/download/rutas_culturales_personas_mayores.json"

    
    respuesta = requests.get(url = urlcomunidadmadrid1, verify=False)
    datos_json = respuesta.json()
    
    lista_destinos = datos_json["data"]
    
    for un_destino in lista_destinos:
        if palabras_importantes in un_destino['destino_denominacion']:
            print("He encontrado algo que quizá te interese")
            print(un_destino['destino_denominacion'])
    
    # columnas de la tabla "resumen_datos": id, palabras_clave, descripcion, url_api, 'json_completo'
    # (preguntar si quiere una tabla por cada uno, parece que no por ele nunciado y es lo mejor) 
    
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
