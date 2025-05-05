'''
Definimos uma lista fictícia de livros.
Criamos uma rota /api/livros que responde a solicitações GET.
Na função get_livros(), retornamos a lista de livros em formato JSON usando a função jsonify.
Para testar sua própria API, execute o código em um servidor local e acesse a rota /api/livros no navegador ou por meio de uma ferramenta como o Postman. A API retornará a lista de livros em JSON.
'''
#Importamos a classe Flask do framework Flask.
from flask import Flask, jsonify

# Criamos uma instância da classe Flask.
app = Flask(__name__)

# Dados fictícios - lista de livros
livros = [
    {"id": 1, "titulo": "Aprenda Python", "autor": "John Doe"},
    {"id": 2, "titulo": "Introdução a APIs", "autor": "Jane Smith"},
]

# Criamos uma rota /api/livros que responde a solicitações GET.
@app.route('/api/livros', methods=['GET'])
def get_livros():
    return jsonify({"livros": livros})

#A função get_livros() retorna a lista de livros em formato JSON usando a função jsonify.
if __name__ == '__main__':
    app.run(debug=True)
