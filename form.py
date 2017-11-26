from wtforms import Form, StringField


class LoginForm(Form):
    username = StringField('Usuario')
    password = StringField('Password')
