from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired(),
                                                  Length(min=4, max=20)])
    password = PasswordField('Contraseña', validators=[InputRequired(),
                                                       Length(min=8, max=80)])
    remember = BooleanField('Recordar')
