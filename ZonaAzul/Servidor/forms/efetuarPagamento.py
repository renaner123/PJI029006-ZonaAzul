from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, validators, IntegerField, SelectField

class EfetuarPagamentoForm(FlaskForm):
    tempo = SelectField('tempo(horas)',[validators.DataRequired()],choices=[('1', '1'), ('2', '2'), ('3', '3'),('4','4')])
    vaga = IntegerField('vaga',[validators.DataRequired()])
    submit = SubmitField('Efetuar pagamento')
