from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired(),
                                                  Length(min=4, max=20)])
    password = PasswordField('Contraseña', validators=[InputRequired(),
                                                       Length(min=8, max=80)])


class PrediccionForm(FlaskForm):
    categoria = StringField('Categoria', validators=[InputRequired()])
    quality_loc = StringField('Quality Location', validators=[InputRequired()])
    quality_web = StringField('Quality Website', validators=[InputRequired()])
    research_rk = StringField('Research Ranking', validators=[InputRequired()])
    google_st = StringField('Google Street View', validators=[InputRequired()])
