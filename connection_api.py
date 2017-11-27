import requests


url = "https://app.dominodatalab.com/v1/vlcastillo/groupon/endpoint"
headers = {"X-Domino-Api-Key": "1WzC8BAZ2sAAJRFlRPg1joyGqakETAb8G"
                               "8fL9VUp3kBIILtTC1yJzFBXa15bPl72",
           "Content-Type": "application/json"}


def login_api(name, password):
    params = {'parameters': ['login', name, password]}
    return requests.post(url, headers=headers, json=params).json()


def desempeno_api(name, password):
    params = {'parameters': ['desempeno', name, password]}
    return requests.post(url, headers=headers, json=params).json()


def demanda_api(name, password):
    params = {'parameters': ['demanda', name, password]}
    return requests.post(url, headers=headers, json=params).json()
