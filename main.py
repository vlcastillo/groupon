from flask import Flask
from flask import render_template
import requests
import datetime as dt
import time
import numpy as np
from sklearn import linear_model
import scipy
app = Flask(__name__)
from multiprocessing import Pool

def estadistica_demanda():
    cash_in = {}
    with open("GR_categoria.csv", "r") as datos:
        for columna in datos:
            columna = columna.strip().split(',')
            columna = [x.replace('"', '') for x in columna]
            if columna[0] == "CL":
                if len(columna) == 8:
                    if columna[3] in cash_in.keys():
                        cash_in[columna[3]][dt.date(*[int(x) for x in columna[1].split("-")])] = int(columna[5])
                    else:
                        cash_in[columna[3]] = {dt.date(*[int(x) for x in columna[1].split("-")]): int(columna[5])}
    categorias = [Categoria(x, cash_in[x]) for x in cash_in.keys()]

    string = ""
    for categoria in categorias:
        string += categoria.nombre + ': ' + str(categoria.pvalue) + '\n'
    return string

pvalues = estadistica_demanda()

class Categoria:
    def __init__(self, nombre, cash_in):
        self.nombre = nombre
        actual = min(cash_in.keys())
        final = max(cash_in.keys())
        while actual < final:
            actual = actual + dt.timedelta(1)
            if actual not in cash_in.keys():
                cash_in[actual] = 0
        predictor = []
        respuesta = []
        for fecha in cash_in.keys():
            respuesta.append(cash_in[fecha])
            dia = [0] * 7
            mes = [0] * 12
            dia[fecha.weekday()] = 1
            mes[fecha.weekday() - 1] = 1
            predictor.append(dia[:-1] + mes[:-1])
        reg = linear_model.LinearRegression()
        reg.fit(predictor, respuesta)
        residuos = np.array(respuesta) - reg.predict(predictor)
        pre = []
        post = []
        for i in range(len(list(cash_in.keys()))):
            if list(cash_in.keys())[i] < final - dt.timedelta(30):
                pre.append(residuos[i])
            else:
                post.append(residuos[i])
        self.pvalue = scipy.stats.ttest_ind(pre, post, equal_var = False).pvalue

@app.route("/")
def hello():
    return render_template("pagina.html")

@app.route("/demanda")
def demanda():
    """response = requests.post("https://app.dominodatalab.com/v1/vlcastillo/groupon/endpoint",
    headers = {
        "X-Domino-Api-Key": "1WzC8BAZ2sAAJRFlRPg1joyGqakETAb8G8fL9VUp3kBIILtTC1yJzFBXa15bPl72",
        "Content-Type": "application/json"
    },
    json = {
        "parameters": [2.5]
    })"""
    global pvalues
    return pvalues

@app.route("/desempeno")
def desempeno():
    return "Predicción desempeño"


if __name__ == "__main__":
    app.run()
    
    
"""
def pvalue(cash_in):
    actual = min(cash_in.keys())
    final = max(cash_in.keys())
    while actual < final:
        actual = actual + dt.timedelta(1)
        if actual not in cash_in.keys():
            cash_in[actual] = 0
    predictor = []
    respuesta = []
    for fecha in cash_in.keys():
        respuesta.append(cash_in[fecha])
        dia = [0] * 7
        mes = [0] * 12
        dia[fecha.weekday()] = 1
        mes[fecha.weekday() - 1] = 1
        predictor.append(dia[:-1] + mes[:-1])
    reg = linear_model.LinearRegression()
    reg.fit(predictor, respuesta)
    residuos = np.array(respuesta) - reg.predict(predictor)
    pre = []
    post = []
    for i in range(len(list(cash_in.keys()))):
        if list(cash_in.keys())[i] < final - dt.timedelta(30):
            pre.append(residuos[i])
        else:
            post.append(residuos[i])
    return scipy.stats.ttest_ind(pre, post, equal_var = False).pvalue
    
        pool = Pool(4)
    pvalues = pool.map(pvalue, [cash_in[x] for x in cash_in.keys()])
    pool.close()
    pool.join()
    string = ""
            """