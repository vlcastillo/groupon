import requests
from flask import Flask
from flask import render_template
from flask import request

import form

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    login_form = form.LoginForm(request.form)
    if request.method == 'POST':
        user = login_form.username.data
        password = login_form.password.data
        print(user)
        print(password)
    title = 'Proyecto UC'
    return render_template("index.html", title=title, form=login_form)


@app.route("/demanda")
def demanda():
    resultados_demanda = 'holaaaa'
    return str(resultados_demanda)


@app.route("/desempeno")
def desempeno():
    return "Predicción desempeño"


def login(user, password):
    url = "https://app.dominodatalab.com/v1/vlcastillo/groupon/endpoint"
    headers = {
        "X-Domino-Api-Key": "1WzC8BAZ2sAAJRFlRPg1joyGqakETAb8G"
                            "8fL9VUp3kBIILtTC1yJzFBXa15bPl72",
        "Content-Type": "application/json"}
    params = {"parameters": ['login', user, password, 2.5]}
    response = requests.post(url, headers=headers, json=params)
    response = response.json()
    if response['status'] == 'Succeeded':
        if response['result'] == [1]:
            return True
    return False

if __name__ == "__main__":
    app.run()
