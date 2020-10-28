from flask import Flask ,redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
	return render_template("index.html")

def frase():
	frase = request.args.get('frase')
	return "<h1>" + frase + "</h1>"

if __name__ == "__main__":
	app.run(debug=True)