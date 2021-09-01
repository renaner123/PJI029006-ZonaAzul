from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, validators
class CriarContaForm(FlaskForm):
    nome = StringField('nome',[validators.DataRequired()])
    cpf = StringField('cpf',[validators.DataRequired()])
    email = StringField('email',[validators.DataRequired()])
    username = StringField('username',[validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
    submit = SubmitField('Criar conta')
