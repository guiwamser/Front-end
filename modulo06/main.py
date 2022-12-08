from flask import Flask, render_template, request, redirect
from pessoa import Pessoa

pessoa1 = Pessoa('haiko', '15', '1:50')
pessoa2 = Pessoa('Jean', '42', '1:84')
pessoa3 = Pessoa('Gisele', '16', '1:56')

lista = [pessoa1, pessoa2, pessoa3]

app = Flask(__name__)

#
@app.route('/')
def inicio():
    return render_template('index.html', titulo = 'Lista Pessoas', pessoas = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Cadastro Pessoa')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    abacate = Pessoa(nome, idade, altura)

    lista.append(abacate)

    return redirect('/')


app.run(debug=True)