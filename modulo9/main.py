from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy




#============================================================================================================================
#variavel de referencia ao flask 
app = Flask(__name__)

# encriptar o passwords do usuário
app.secret_key = 'moredevs'

#string conexao
app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "teste",
    senha = "123456",
    servidor = "localhost",
    database = "postgres"
)

#================================================================================
db = SQLAlchemy(app)

class Jogos(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

#=========================================================================
lista = Jogos.query.order_by(Jogos.id)


@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    #render template acessa nosso html, variavel titulo recebendo valor e sendo acessada via html.
    return render_template("lista.html", titulo = 'jogos', jogos = lista)



#return redirect('/login')
@app.route('/novo2')
def novo():

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        
        #recurso querystring
        return redirect(url_for('login2', proximo= url_for('novo2')))

    return render_template('novo.html', titulo='Novo Jogo')




@app.route('/criar2', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogos(nome, categoria, console)

    lista.append(jogo)

    return redirect(url_for('index'))





@app.route('/login2')
def login():

        proximo = request.args.get('proximo')

        return render_template('login.html', proximo=proximo)




@app.route('/autenticar2', methods=['POST',])
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


@app.route('/logout2')
def logout():
    session['usuario_logado'] = None
    flash('voce foi Desconectado')

    return redirect(url_for('login'))




app.run(debug=True)