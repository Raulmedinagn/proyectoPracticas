from flask import Flask, redirect, url_for, render_template, request

from pruebanltk import Analizar
from conexiondb import Api2DB

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
    print(lista)
    # para convertirlo a string
    #palabras_importantes = " ".join(lista)
    Api2DB1 = Api2DB()
    comparar = Api2DB1.hayUnaPalabraClaveEnTabla(lista)
    #comparar = " ".join(comparar)
    
    return render_template("info.html", data=comparar)

@app.route('/bbdd')
def bbdd():
    Api2DB1 = Api2DB()
    bd_texto = Api2DB1.mostrarDatos()
    
    data = Api2DB1.mostrarDatos()
    
    return render_template("bbdd.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
