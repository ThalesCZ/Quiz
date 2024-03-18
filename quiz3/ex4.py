import json
from flask import Flask, request, jsonify

app = Flask(__name__)

PRODUTOS_FILE = "produtos.json"

def load_produtos():
    try:
        with open(PRODUTOS_FILE, "r") as file:
            produtos = json.load(file)
    except FileNotFoundError:
        produtos = []
    return produtos

def save_produtos(produtos):
    with open(PRODUTOS_FILE, "w") as file:
        json.dump(produtos, file, indent=4)

@app.route('/produto', methods=['POST'])
def add_produto():
    data = request.json
    produtos = load_produtos()
    produtos.append(data)
    save_produtos(produtos)
    return jsonify({"message": "Produto adicionado com sucesso!"}), 201

@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = load_produtos()
    return jsonify(produtos)

@app.route('/produto/<int:id>', methods=['PUT'])
def update_estoque(id):
    data = request.json
    produtos = load_produtos()
    for produto in produtos:
        if produto['id'] == id:
            produto['estoque'] = data['estoque']
            save_produtos(produtos)
            return jsonify({"message": "Estoque atualizado com sucesso!"})
    return jsonify({"message": "Produto não encontrado"}), 404

@app.route('/produto/<int:id>', methods=['DELETE'])
def delete_produto(id):
    produtos = load_produtos()
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            save_produtos(produtos)
            return jsonify({"message": "Produto deletado com sucesso!"})
    return jsonify({"message": "Produto não encontrado"}), 404

carrinho = []

@app.route('/carrinho', methods=['POST'])
def add_carrinho():
    data = request.json
    carrinho.append(data)
    return jsonify({"message": "Produto adicionado ao carrinho com sucesso!"}), 201

@app.route('/carrinho', methods=['GET'])
def get_carrinho():
    return jsonify(carrinho)

if __name__ == '__main__':
    app.run(debug=True)
