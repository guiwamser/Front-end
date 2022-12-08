from flask import Flask, render_template
from pessoa import Pessoa

#
app = Flask(__name__)

#
@app.route('/')
def inicio():
    pessoa1 = Pessoa('haiko', '15', '1:50')
    pessoa2 = Pessoa('Jean', '42', '1:84')
    pessoa3 = Pessoa('Gisele', '16', '1:56')

    lista = [pessoa1, pessoa2, pessoa3]
    return render_template('index.html', titulo = 'Felipe', pessoas = lista)

@app.route('/novo')
def novo():
    return 'Titulo Rota nova'


app.run()