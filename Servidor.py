from flask import Flask, redirect, url_for, render_template, request, flash

from Serverflask import ServidorFlask

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

s = ServidorFlask()

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == "POST":       
        frase = request.form["fr"]
        if frase:
            palabras_importantes = s.procesarRequest("keywords",None,frase,None,None,None,None,None,None,None,None,None,None,None)
            lista_keywords = palabras_importantes.split()

            for keyword in lista_keywords:
                tipos = ['hotel','hoteles','monumento','monumentos','museo','museos']
               
                if any(keyword in s for s in tipos):
                    print(palabras_importantes)
                    print(keyword)
                    palabras_sin_key = palabras_importantes.replace(keyword,'')
                    sql = "SELECT api_madrid.*,MATCH (titulo) AGAINST ('" + palabras_importantes + "') AS relevance FROM api_madrid WHERE MATCH (titulo,ubicacion) AGAINST ('" + palabras_sin_key + "') AND tipo LIKE '%"+keyword+"%' ORDER BY relevance DESC;"
                    comparar = s.procesarRequest("bbdd", "execute",sql,None, None, None, None, None, None, None, None, None,None,None)
                    if comparar:
                        print("ruta1")
                        return render_template("index.html", data=comparar, variable = "inline")
                    else:
                        sql = "SELECT api_madrid.*,MATCH (titulo) AGAINST ('" + palabras_importantes + "') AS relevance FROM api_madrid WHERE MATCH (tipo,titulo,ubicacion) AGAINST ('" + palabras_importantes + "') ORDER BY relevance DESC;"       
                        comparar = s.procesarRequest("bbdd", "execute",sql,None, None, None, None, None, None, None, None, None,None,None)
                        if comparar:
                            print("ruta3")
                            return render_template("index.html", data=comparar, variable = "inline")
                        else:
                            print("ruta4")
                            error='No se encontraron resultados, prueba a buscarlo de otra forma'
                            return render_template("index.html", variable="none",error=error)  
                else:
                    sql = "SELECT api_madrid.*,MATCH (titulo) AGAINST ('" + palabras_importantes + "') AS relevance FROM api_madrid WHERE MATCH (titulo,ubicacion) AGAINST ('" + palabras_importantes + "') ORDER BY relevance DESC;"                    
                    comparar = s.procesarRequest("bbdd", "execute",sql,None, None, None, None, None, None, None, None, None,None,None)
                    if comparar:
                        print("ruta2")
                        return render_template("index.html", data=comparar, variable = "inline")
                    else:
                        print("ruta5")
                        error='No se encontraron resultados, prueba a buscarlo de otra forma'
                        return render_template("index.html", variable="none",error=error)
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