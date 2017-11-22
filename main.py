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
        "X-Domino-Api-Key": "1WzC8BAZ2sAAJRFlRPg1joyGqakETAb8G8fL9VUp3kBIILtTC1yJzFBXa15bPl72",
        "Content-Type": "application/json"
    },
    json = {
        "parameters": []
    })
    
    return str(response.json()["result"])

@app.route("/desempeno")
def desempeno():
    return "Predicción desempeño"


if __name__ == "__main__":
    app.run()