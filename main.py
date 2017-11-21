from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("pagina.html")

@app.route("/demanda")
def demanda():
    return "Predicción demanda"

@app.route("/desempeno")
def desempeno():
    return "Predicción desempeño"


if __name__ == "__main__":
    app.run()