import requests


from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, \
                        login_required, logout_user, current_user
from forms import LoginForm
from parser import csv_to_html


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Miclavesupersecreta'
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

url = "https://app.dominodatalab.com/v1/vlcastillo/groupon/endpoint"
headers = {"X-Domino-Api-Key": "1WzC8BAZ2sAAJRFlRPg1joyGqakETAb8G"
                               "8fL9VUp3kBIILtTC1yJzFBXa15bPl72",
           "Content-Type": "application/json"}


class User(UserMixin):
    id = 1

    def __init__(self, username, password):
        super().__init__()
        self.name = username
        self.password = password
        self.connected = False

user = User('', '')


@login_manager.user_loader
def load_user(_):
    global user
    return user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global user
    form = LoginForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.password.data)
        remember = form.remember.data

        params = {'parameters': ['login', user.name, user.password, 1]}
        response = requests.post(url, headers=headers, json=params).json()

        if response['status'] == 'Succeeded':
            if response['result'] == [1]:
                login_user(user, remember=remember)
                user.connected = True
                return redirect(url_for('mainmenu'))
            else:
                return '<h1>Usuario o contraseña incorrectos</h1>'
        else:
            return '<h1>No fue posible establecer ' \
                   'conexión con DominoDatalab</h1>'
    return render_template('login.html', form=form)


@app.route('/mainmenu')
@login_required
def mainmenu():
    if user.connected:
        return render_template('dashboard.html', name=user.name,
                               table=csv_to_html('micsv.csv'))
    return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    global user
    logout_user()
    user = User('', '')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
