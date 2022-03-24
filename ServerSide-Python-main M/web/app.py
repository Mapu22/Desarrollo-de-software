from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/pagina', methods=['GET'])
def page():
    return render_template('pagina.html')


@app.route('/document_detail', methods=['POST'])
def document_detail():
    id_document = request.form['id_document']
    numero_paginas = request.form['numero_paginas']
    titulo = request.form['titulo']
    categoria = request.form['categoria']
    autor= request.form['autor']

    p = Document(id_document=id_document, numero_paginas=numero_paginas, titulo=titulo, categoria=categoria, autor=autor)
    model.append(p)
    return render_template('document_eliminado.html', value=p)


@app.route('/document')
def document():
    data = [(i.id_document, i.numero_paginas, i.Titulo, i.Categoria, i.Autor) for i in model]
    print(data)
    return render_template('document.html', value=data)


if __name__ == '__main__':
    app.run()