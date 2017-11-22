from flask import Flask
from flask import render_template
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("pagina.html")

@app.route("/demanda")
def demanda():
    response = requests.post("https://app.dominodatalab.com/v1/vlcastillo/groupon/endpoint",
    headers = {
        "X-Domino-Api-Key": "YOUR_API_KEY",
        "Content-Type": "application/json"
    },
    json = {
        "parameters": ["FOO", "BAR", "ETC"]
    })
    
    return response.json()["result"]

@app.route("/desempeno")
def desempeno():
    return "Predicción desempeño"


if __name__ == "__main__":
    app.run()