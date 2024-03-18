from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

USERS_FILE = "users.json"

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as file:
        json.dump([], file)

def ler_usuarios():
    with open(USERS_FILE, "r") as file:
        return json.load(file)

def escrever_usuarios(usuarios):
    with open(USERS_FILE, "w") as file:
        json.dump(usuarios, file, indent=4)

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = ler_usuarios()
    return jsonify(usuarios)

@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id):
    usuarios = ler_usuarios()
    for usuario in usuarios:
        if usuario['id'] == id:
            return jsonify(usuario)
    return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    novo_usuario = request.json
    usuarios = ler_usuarios()

    novo_id = 1 if len(usuarios) == 0 else usuarios[-1]['id'] + 1
    novo_usuario['id'] = novo_id

    usuarios.append(novo_usuario)
    escrever_usuarios(usuarios)

    return jsonify(novo_usuario), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuarios = ler_usuarios()
    for usuario in usuarios:
        if usuario['id'] == id:
            dados_atualizados = request.json
            usuario.update(dados_atualizados)
            escrever_usuarios(usuarios)
            return jsonify(usuario)
    return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    usuarios = ler_usuarios()
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            escrever_usuarios(usuarios)
            return jsonify({'message': 'Usuário excluído com sucesso'})
    return jsonify({'error': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
