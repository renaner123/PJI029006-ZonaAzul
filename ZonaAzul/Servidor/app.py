from flask import Flask, flash, redirect, url_for, request, session, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup
from servidor.Usuario import Usuario
from servidor.InterfaceUsuario import InterfaceUsuario
from servidor.Carro import Carro
from servidor.Vaga import Vaga
from servidor.Aplicacao import Aplicacao
from servidor.Fiscal import Fiscal

# https://fontawesome.com/icons
from flask_fontawesome import FontAwesome

from forms.login import LoginForm
from forms.criarConta import CriarContaForm
from forms.cadastrarVeiculo import CadastrarVeiculoForm
from forms.efetuarPagamento import EfetuarPagamentoForm

app = Flask(__name__)
app.secret_key = "SECRET_KEY"

boostrap = Bootstrap(app)
fa = FontAwesome(app)

nav = Nav()
nav.init_app(app)

interface = InterfaceUsuario()

user = Usuario("Renan", "08299152909", "renan@teste")
interface.criarConta(user, "renaner123", "444998")
interface.cadastrarVeiculo(user, "MIJ5419", "Uno")
vagas = Vaga()

usuarios = interface.getUsuarios()

@nav.navigation()
def meunavbar():
    menu = Navbar('Minha aplicação')
    menu.items = [View('Inicial', 'inicio'), ]
    menu.items.append(Subgroup('Conta',View('Cadastrar veículo','cadastrar_veiculo'),View('Efetuar pagamento','efetuar_pagamento')))
    menu.items.append(Subgroup('Cadastro',View('Listar cadastro','listar_cadastro')))
    menu.items.append(View('Sair', 'logout'))
    return menu

@app.route('/login', methods=['GET', 'POST'])
def autenticar():
    if session.get('logged_in'):
        return redirect(url_for('inicio'))
    form = LoginForm()

    if form.validate_on_submit():
        userauth = form.username.data
        password = form.password.data
        auxCheck = 0
        for consult in usuarios:
            if (usuarios[consult].user == userauth and usuarios[consult].senha == password):
                auxCheck = auxCheck + 1
                auxUser = consult

        if (auxCheck == 1):
            usuarios[auxUser].login = True
            session['logged_in'] = True
            session['nome'] = userauth
            session['idUsuario'] = password

            return redirect(url_for('inicio'))
        flash('Usuário ou senha inválidos')
        return redirect(url_for('autenticar'))
    return render_template('login.html', title='Autenticação de usuários', form=form)

@app.route('/')
def inicio():
    if not session.get('logged_in'):
        return redirect(url_for('autenticar'))
    else:
        return render_template('index.html', title='Inicial', usuario=session.get('nome'))

@app.route("/logout")
def logout():
    '''
    Para encerrar a sessão autenticada de um usuário
    :return: redireciona para a página inicial
    '''
    session.clear()
    return redirect(url_for('inicio'))


@app.errorhandler(404)
def page_not_found(e):
    '''
    Para tratar erros de páginas não encontradas - HTTP 404
    :param e:
    :return:
    '''
    return render_template('404.html'), 404


@app.route('/veiculo/cadastrar', methods=['GET', 'POST'])
def cadastrar_veiculo():
    if session.get('logged_in'):
        form = CadastrarVeiculoForm()
        if form.validate_on_submit():
            modelo = request.form['modelo']
            placa = request.form['placa']
            for user in interface.getUsuarios():
                if(usuarios[user].user==session['nome']):
                    interface.cadastrarVeiculo(usuarios[user],placa,modelo)
                    flash(f"Carro cadastrado", category="success")
            return redirect(url_for('autenticar'))
    return render_template('veiculo_cadastrar.html', title='Cadastrar veiculo', form=form)

@app.route('/pagamento', methods=['GET', 'POST'])
def efetuar_pagamento():
    if session.get('logged_in'):
        form = EfetuarPagamentoForm()
        if form.validate_on_submit():
            tempo = request.form['tempo']
            vaga = request.form['vaga']
            for consult in usuarios:
                if (usuarios[consult].user == session.get('nome')):
                    if(vagas.getStatus(vaga)):
                        vagas.setUsuarioVaga(usuarios[consult].user,vaga)
                        usuarios[consult].tempo = tempo

            flash(f"{tempo} hora(s) inserido na vaga {vaga}!", category="success")
            return redirect(url_for('autenticar'))
    return render_template('efetuar_pagamento.html', title='Efetuar pagamento', form=form)

@app.route('/usuario/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    form = CriarContaForm()
    if form.validate_on_submit():
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        user = Usuario(nome, cpf, email)
        interface.criarConta(user, username, password)
        flash(f"Conta criada!", category="success")
        return redirect(url_for('autenticar'))
    return render_template('usuario_cadastrar.html', title='Cadastrar usuario', form=form)

@app.route('/usuario/listar', methods=['GET', 'POST'])
def listar_cadastro():
    contatos = []
    form= CriarContaForm()
    vaga = 0
    if session.get('logged_in'):
        for user in interface.getUsuarios():
            if (usuarios[user].user == session['nome']):
                contatos = usuarios[user]
                vaga = vagas.getVagaUser(usuarios[user].user)

        return render_template('usuario_listar.html', contatos=contatos, vagas=vaga, form=form)
    return redirect(url_for('autenticar'))
if __name__ == '__main__':
    app.run(debug=True)
