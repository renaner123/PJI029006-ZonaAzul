import json
from datetime import datetime

import requests
from flask import Flask, flash, redirect, url_for, request, session, render_template, jsonify, request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup
from servidor.Usuario import Usuario
from servidor.InterfaceUsuario import InterfaceUsuario
from servidor.Carro import Carro
from servidor.Vaga import Vaga
from servidor.Aplicacao import Aplicacao
from servidor.Fiscal import Fiscal
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import url_for
from flask_httpauth import HTTPBasicAuth

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
interface.criarConta(user, "renaner", "123456")
interface.cadastrarVeiculo(user, "MIJ5419", "Uno")

usuarios = interface.getUsuarios()
vagas = dict()


@nav.navigation()
def meunavbar():
    menu = Navbar('Minha aplicação')
    menu.items = [View('Inicial', 'inicio'), ]
    menu.items.append(Subgroup('Conta', View('Cadastrar veículo', 'cadastrar_veiculo'),
                               View('Efetuar pagamento', 'efetuar_pagamento')))
    menu.items.append(Subgroup('Cadastro', View('Listar cadastro', 'listar_cadastro')))
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
                if (usuarios[user].user == session['nome']):
                    interface.cadastrarVeiculo(usuarios[user], placa, modelo)
                    flash(f"Carro cadastrado", category="success")
            return redirect(url_for('autenticar'))
    return render_template('veiculo_cadastrar.html', title='Cadastrar veiculo', form=form)


@app.route('/pagamento', methods=['GET', 'POST'])
def efetuar_pagamento():
    dataAgora = ""

    if session.get('logged_in'):
        form = EfetuarPagamentoForm()
        vaga = ""
        if form.validate_on_submit():
            tempo = request.form['tempo']
            vaga = request.form['vaga']
            for consult in usuarios:
                if (usuarios[consult].user == session.get('nome')):
                    if(int(vaga) in vagas):
                        vagas[int(vaga)].setStatus(True)
                        vagas[int(vaga)].setTempo(tempo)
                        vagas[int(vaga)].setDatatime(datetime.now())
                        usuarios[consult].setVaga(int(vaga))
                        flash(f"{tempo} segundo(s) inseridos na vaga {vaga}!", category="success")
                        return redirect(url_for('autenticar'))
            flash(f"Vaga {vaga} não existe ou não cadastrada", category="danger")
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
    form = CriarContaForm()
    vaga = 0
    tempo = 0
    if session.get('logged_in'):
        for user in interface.getUsuarios():
            if (usuarios[user].user == session['nome']):
                contatos = usuarios[user]
                vaga = contatos.getVaga()
                if(len(vagas)>0):
                    tempo = vagas[vaga].getTempo()

        return render_template('usuario_listar.html', contatos=contatos, vagas=vaga, tempo=tempo, form=form)
    return redirect(url_for('autenticar'))


# Possibilita o Totem cadastrar uma nova vaga no servidor
@app.route('/vagas', methods=['POST'])
def adicionaVaga():
    if not 'vagas' in request.json:
        abort(400)

    for resultado in request.json['vagas']:
        if(resultado['idVaga'] in vagas):
            return jsonify({'resultado': "Ja existe vaga com esse id: " + str(resultado['idVaga'])}), 403
        vagas[resultado['idVaga']] = Vaga(resultado['idVaga'], resultado['idSensor'])

    return jsonify({'resultado': True}), 200


# Possibilita o Totem atualizar o status de uma vaga
@app.route('/vagas/status', methods=['PUT'])
def atualizaStatusVaga():

    if not request.json:
        abort(400)
    if 'idVaga' in request.json and type(request.json['idVaga']) != int:
        abort(400)
    if 'status' in request.json and type(request.json['status']) != bool:
        abort(400)

    if request.json['idVaga'] in vagas:
        vagas[request.json['idVaga']].setStatus(request.json['status'])
        return jsonify({'resultado': True}), 200
    else:
        abort(400)


# Possibilita o Totem atualizar o sensor de uma vaga
@app.route('/vagas/sensor', methods=['PUT'])
def atualizaSensorVaga():

    if not request.json:
        abort(400)
    if 'idVaga' in request.json and type(request.json['idVaga']) != int:
        abort(400)
    if 'idSensor' in request.json and type(request.json['idVaga']) != int:
        abort(400)

    if request.json['idVaga'] in vagas:
        vagas[request.json['idVaga']].setIdSensor(request.json['idSensor'])
        return jsonify({'resultado': True}), 200
    else:
        abort(400)

# Verifica com o totem o status atual da vaga, pra ver se se está condizente. Envia um GET com o id da vaga
def consultaVaga(idVaga):

    consulta = requests.get('http://totem/consultar/Vaga', params=idVaga)
    # precisa ser implementado no Totem
    # if (consulta.status_code == 200):
    #     return True
    # else:
    #     return False
    return 200

# Mostrar os dados de uma vaga
@app.route('/vagas/<int:idVaga>', methods=['GET'])
def listarVagas(idVaga):
    if idVaga in vagas:
        print(vagas[idVaga].getIdSensor())
        return jsonify({'idSensor': vagas[idVaga].getIdSensor(),
                        'status': vagas[idVaga].getStatus(),
                        'tempo': vagas[idVaga].getTempo()
                        }), 200

@app.route('/timer', methods=['GET'])
def timer():
    dataAgora = datetime.now()
    vagaUser = 0
    dif = 0
    for user in interface.getUsuarios():
        if (usuarios[user].user == session['nome']):
            contatos = usuarios[user]
            vagaUser = contatos.getVaga()
            dif = datetime.now() - (vagas[vagaUser].getDatatime())

    if((int(dif.seconds)+10) >= (int(vagas[vagaUser].getTempo()))):
        return jsonify({'resultado': 0}), 200
    else:
        return jsonify({'resultado': dif.seconds}), 200



if __name__ == '__main__':
    app.run(debug=True)
