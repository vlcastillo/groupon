import requests


url = "https://app-models.dominodatalab.com" \
      ":443/models/5a1c9093f2d4e9c54bb0dfb3/latest/model"
auth = ("CTHVT1jJzHtKniV4hbe3kfkSsDiC93mZQptMf9JWDhPlnvsSptEWF3VhXoilNYXv",
        "CTHVT1jJzHtKniV4hbe3kfkSsDiC93mZQptMf9JWDhPlnvsSptEWF3VhXoilNYXv")


def login_api(name, password):
    params = {'data': ['login', name, password]}
    return requests.post(url, auth=auth, json=params).json()


def desempeno_api(name, password):
    params = {'data': ['desempeno', name, password]}
    return requests.post(url, auth=auth, json=params).json()


def demanda_api(name, password):
    params = {'data': ['demanda', name, password]}
    return requests.post(url, auth=auth, json=params).json()
