from flask import Flask, redirect, url_for, render_template, request

from pruebanltk import Analizar
from conexiondb import Api2DB

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == "POST":       
        frase = request.form["fr"]
        Analizar1 = Analizar()
        palabras_importantes = Analizar1.analizar_frase(frase)
        
        Api2DB1 = Api2DB()
        comparar = Api2DB1.hayUnaPalabraClaveEnTabla(palabras_importantes)
        return render_template("index.html", data=comparar, variable = "inline")
    else:
        return render_template("index.html",variable = "none")

@app.route('/bbdd')
def bbdd():
    Api2DB1 = Api2DB()
   
    data = Api2DB1.mostrarDatos()
    
    return render_template("bbdd.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
