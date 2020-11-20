from flask import Flask, redirect, url_for, render_template, request

from Serverflask import ServidorFlask

app = Flask(__name__)

s = ServidorFlask()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":       
        frase = request.form["fr"]
        palabras_importantes = s.procesarRequest("keywords",None,frase,None,None)
        comparar = s.procesarRequest("bbdd","execute","SELECT * FROM resumen_api WHERE MATCH (palabras_clave) AGAINST ('" + palabras_importantes + "');",None,None)
        return render_template("index.html", data=comparar, variable = "inline")
    else:
        return render_template("index.html",variable = "none")

@app.route('/bbdd')
def bbdd(): 
    data = s.procesarRequest("bbdd","execute","SELECT * FROM resumen_api ORDER BY id;",None,None)
    return render_template("bbdd.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)