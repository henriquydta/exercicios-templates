from flask import Flask, render_template
from gera_documentos import gera_doc

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/termos')
def termos():
    return render_template('termos.html')

@app.route('/privacidade')
def privacidade():
    return render_template('privacidade.html')

@app.route('/utilizar')
def utilizar():
    return render_template('utilizar.html')

@app.route('/cpf')
def cpf():
    nome_doc = 'CPF'
    docs = gera_doc(nome_doc)
    return render_template('docbr.html', nome_doc=nome_doc, docs=docs)

@app.route('/cnpj')
def cnpj():
    nome_doc = 'CNPJ'
    docs = gera_doc(nome_doc)
    return render_template('docbr.html', nome_doc=nome_doc, docs=docs)

if __name__ == '__main__':
    app.run(debug=True)