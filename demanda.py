import datetime as dt
import numpy as np
import pygal


from sklearn import linear_model
from connection_api import fechas_api, cash_in_api


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

        self.keys = list(cash_in.keys())
        for fecha in self.keys:
            respuesta.append(cash_in[fecha])
            dia = [0] * 7
            mes = [0] * 12
            dia[fecha.weekday()] = 1
            mes[fecha.weekday() - 1] = 1
            predictor.append(dia[:-1] + mes[:-1])
        reg = linear_model.LinearRegression()
        reg.fit(predictor, respuesta)
        residuos = np.array(respuesta)

        self.cupones_por_fecha = {}
        for i in range(len(self.keys)):
            self.cupones_por_fecha[self.keys[i]] = [0, residuos[i]]

    def separacion_fechas(self):
        aux = [self.cupones_por_fecha[x] for x in self.keys]
        self.separacion = {}

        for i in range(len(aux)):
            if aux[i][0] in self.separacion.keys():
                self.separacion[aux[i][0]].append(aux[i][1])
            else:
                self.separacion[aux[i][0]] = [aux[i][1]]

        for key in self.separacion.keys():
            array = np.array(self.separacion[key])
            self.separacion[key] = [np.mean(array), np.var(array), len(array)]

        return self.separacion

    def estado_actual(self):
        aux = sorted(
            [self.separacion[key][0] for key in self.separacion.keys()])
        for key in self.separacion.keys():
            if self.separacion[key][0] == aux[-1]:
                cant_max = key
            if self.separacion[key][0] == aux[-2]:
                cant_max2 = key
        # print(self.nombre, self.separacion[cant_max], self.separacion[cant_max2])
        if self.separacion[cant_max2][0] > self.separacion[cant_max][0] - 0.05 * \
                self.separacion[cant_max][1] / self.separacion[cant_max][2]:
            return ("Categoría completa", "-")
        else:
            return ("Categoría incompleta",
                    self.separacion[cant_max][0] - self.separacion[cant_max2][
                        0])

    def grafico(self):
        line_chart = pygal.Line(x_title="Cantidad de ofertas publicadas")
        line_chart.title = 'Promedio de ventas diarias'
        x_label = [None]
        keys = sorted(list(self.separacion.keys()))
        if 0 in keys:
            keys.remove(0)
        for key in keys:
            x_label.append(key)
            x_label.append(None)
        line_chart.x_labels = x_label
        means = [None]
        for key in keys:
            means.append(self.separacion[key][0])
            means.append(None)
        line_chart.add(self.nombre, means)

        for i in range(len(keys)):
            key = keys[i]
            cota = [None] * (2 * len(keys) + 1)
            cota[2 * i] = self.separacion[key][0] - 0.05 * self.separacion[key][
                1] / self.separacion[key][2]
            cota[2 * (i + 1)] = self.separacion[key][0] - 0.05 * \
                                                          self.separacion[key][
                                                              1] / \
                                                          self.separacion[key][
                                                              2]
            line_chart.add('Cota Inferior', cota, dots_size=0)
            cota = [None] * (2 * len(keys) + 1)
            cota[2 * i] = self.separacion[key][0] + 0.05 * self.separacion[key][
                1] / self.separacion[key][2]
            cota[2 * (i + 1)] = self.separacion[key][0] + 0.05 * \
                                                          self.separacion[key][
                                                              1] / \
                                                          self.separacion[key][
                                                              2]
            line_chart.add('Cota Superior', cota, dots_size=0)
        line_chart.render_to_file("prueba.svg")


def estadistica_demanda(user, password):
    header = [['Categoría', 'Estado', 'Último incremento']]

    res = fechas_api(user, password)
    if res['status'] != 'Succeeded':
        return header
    fechas = res['result'][0].split('\r\n')
    
    res = cash_in_api(user, password)
    if res['status'] != 'Succeeded':
        return header
    cash = res['result'][0].split('\r\n')

    cash_in = {}
    for columna in cash:
        if columna == '':
            continue
        columna = columna.strip().split(';')
        columna[1] = columna[1].split(' ')[0]
        if columna[0] == "CL" and columna[1] != '':
            if columna[1] in cash_in.keys():
                cash_in[columna[1]][dt.date(*[int(columna[2]), int(columna[3]), int(columna[4])])] = float(columna[6])
            else:
                cash_in[columna[1]] = {dt.date(*[int(columna[2]), int(columna[3]), int(columna[4])]): float(columna[6])}

    categorias = [Categoria(x, cash_in[x]) for x in cash_in.keys()]
    categorias = {x.nombre: x for x in categorias}
    
    for columna in fechas:
        if columna == '':
            continue
        columna = columna.strip().split(',')
        columna[0] = columna[0].split(' ')[0]
        if columna[2] != 'NULL' and columna[0] != '' and columna[0] in categorias.keys():
            actual = dt.date(*[int(x.replace('"', '')) for x in columna[1].split(' ')[0].split('-')])
            final = dt.date(*[int(x.replace('"', '')) for x in columna[2].split('-')])
            while actual < final and actual in categorias[columna[0]].keys:
                categorias[columna[0]].cupones_por_fecha[actual][0] += 1
                actual += dt.timedelta(1)

    lista_final = []
    for categoria in categorias:
        categorias[categoria].separacion_fechas()
        if len(categorias[categoria].separacion) > 1:
            respuesta = categorias[categoria].estado_actual()
            lista_final.append([categorias[categoria].nombre,
                                *list(respuesta)])
    lista_final.sort()
    return header, lista_final
