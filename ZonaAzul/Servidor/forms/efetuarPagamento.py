from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, validators, IntegerField, SelectField

class EfetuarPagamentoForm(FlaskForm):
    tempo = SelectField('tempo(segundos)',[validators.DataRequired()],choices=[('30', '30'), ('40', '40'), ('50', '50'),('60','60')])
    vaga = IntegerField('vaga',[validators.DataRequired()])
    submit = SubmitField('Efetuar pagamento')
