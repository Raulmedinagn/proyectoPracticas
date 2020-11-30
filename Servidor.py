from flask import Flask, redirect, url_for, render_template, request

from Serverflask import ServidorFlask

app = Flask(__name__)

s = ServidorFlask()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":       
        frase = request.form["fr"]
        if frase:
            palabras_importantes = s.procesarRequest("keywords",None,frase,None,None,None,None,None,None,None,None,None,None,None)
            sql = "SELECT api_madrid.*,MATCH (tipo,titulo) AGAINST ('" + palabras_importantes + "') AS relevance,MATCH (tipo) AGAINST ('" + palabras_importantes + "') AS tipo_relevance FROM api_madrid WHERE MATCH (tipo,titulo) AGAINST ('" + palabras_importantes + "') ORDER BY tipo_relevance DESC, relevance DESC;"
            comparar = s.procesarRequest("bbdd", "execute",sql,None, None, None, None, None, None, None, None, None,None,None)

            return render_template("index.html", data=comparar, variable = "inline")
        else:
            return render_template("index.html", variable="none")
    else:
        return render_template("index.html",variable = "none")

@app.route('/bbdd')
def bbdd():
    sql = "SELECT * FROM api_madrid ORDER BY id;"
    data = s.procesarRequest("bbdd","execute",sql,None,None,None,None,None,None,None,None,None,None,None)
    return render_template("bbdd.html", data=data)

@app.route('/info/<id>', methods=['GET', 'POST'])
def info(id):
    sql = "SELECT * FROM api_madrid WHERE id = "+ id +";"
    data = s.procesarRequest("bbdd","execute",sql,None,None,None,None,None,None,None,None,None,None,None)
    return render_template("info.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)