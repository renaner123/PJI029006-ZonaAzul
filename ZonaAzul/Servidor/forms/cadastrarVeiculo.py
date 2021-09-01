from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, validators
class CadastrarVeiculoForm(FlaskForm):
    modelo = StringField('modelo',[validators.DataRequired()])
    placa =  StringField('placa',[validators.DataRequired()])
    submit = SubmitField('Cadastrar veículo')
