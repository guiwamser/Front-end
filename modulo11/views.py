from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from models import Jogos, Usuarios


@app.route('/')
def index():

    lista = Jogos.query.order_by(Jogos.id)
    return render_template("lista.html", titulo = 'jogos', jogos = lista)




@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo= url_for('novo')))
    return render_template('novo.html', titulo='criar Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    #variavel nova recebendo classe jogo e filtrando pelo nome
    jogo = Jogos.query.filter_by(nome=nome).first()
    # if condicional recebendo a variavel caso exista jogos cadastrados 
    if jogo:
        flash('Jogo Ja Existente!')
        return redirect(url_for('index'))

    #variavel criada recebendo variaveis e as variaveis refente ao form
    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    #acessando variavel db e o recurso session e adicionando dados a variavel novo jogo 
    db.session.add(novo_jogo)
    #acessando variavel db e o recurso session e comitando dados no banco
    db.session.commit()
    #redirecionamento para lista de jogos
    return redirect(url_for('index'))



@app.route('/editar/<int:id>')
def editar(id):

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo= url_for('editar')))
    #fazer uma query do banco
    jogo = Jogos.query.filter_by(id=id).first()
    return render_template('editar.html', titulo= 'Editar Jogo', jogo = jogo)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    
    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))

    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo Deletado com sucesso')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('voce foi Desconectado')

    return redirect(url_for('login'))


@app.route('/login')
def login():

        proximo = request.args.get('proximo')

        return render_template('login.html', proximo=proximo)

@app.route('/autenticar', methods=['POST',])
def autenticar():

    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    
    if usuario:
        
        if request.form['senha'] == usuario.senha:

            session['usuario_logado'] = usuario.nickname
            

            flash(usuario.nickname + 'logado com sucesso')

            proxima_pagina = request.form['proximo']

            return redirect(proxima_pagina)

    else:
        flash('usuario ou senha incorretos tente novamente')
        #dinamizando url

        return redirect(url_for('login'))
