from flask import Flask ,redirect, url_for, render_template, request
app = Flask(__name__)

#restflask
from flask_restful import Api
from restful.prueba_api import Helloword
from pruebanltk import Analizar

api = Api(app)
api.add_resource(Helloword, '/api')




@app.route('/',methods=['GET','POST'])
def home():
	if request.method == "POST":
		frase = request.form["fr"]
		return redirect(url_for("analizar", frase_recogida=frase))
	else:
		return render_template("index.html")

@app.route('/analizar/<frase_recogida>')
def analizar(frase_recogida):
	lista = Analizar().analizar_frase(frase_recogida)
	#para convertirlo a string
	palabras_importantes = " ".join(lista)
	return palabras_importantes



if __name__ == "__main__":
	app.run(debug=True)