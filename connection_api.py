import requests


url = "https://app-models.dominodatalab.com:443/" \
      "models/5a1ca1ca665488418c67c32e/latest/model"
auth = ("2ctum3bdEbN2b5EOxA5IQuxfprqLK5UGxfNkxgwmpeQ1jPW8vqXU9HDyR6SZzL3T",
        "2ctum3bdEbN2b5EOxA5IQuxfprqLK5UGxfNkxgwmpeQ1jPW8vqXU9HDyR6SZzL3T")


def login_api(name, password):
    params = {'data': ['login', name, password, '', '', '', '', '']}
    return requests.post(url, auth=auth, json=params)


def desempeno_api(name, password):
    params = {'data': ['desempeno', name, password, '', '', '', '', '']}
    return requests.post(url, auth=auth, json=params)


def demanda_api(name, password, cat, ql, qw, rr, gs):
    params = {'data': ['demanda', name, password, cat, ql, qw, rr, gs]}
    return requests.post(url, auth=auth, json=params)
