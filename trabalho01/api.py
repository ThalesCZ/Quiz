from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('bauru_participa.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/enquetes', methods=['POST'])
def criar_enquete():
    data = request.get_json()

    if 'descricao' not in data or 'opcoes' not in data:
        return jsonify({'error': 'Descrição e opções são campos obrigatórios'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO enquetes (descricao) VALUES (?)", (data['descricao'],))
    enquete_id = cursor.lastrowid

    for opcao in data['opcoes']:
        cursor.execute("INSERT INTO opcoes (enquete_id, descricao) VALUES (?, ?)", (enquete_id, opcao))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Enquete criada com sucesso', 'enquete_id': enquete_id}), 201

@app.route('/api/enquetes', methods=['GET'])
def listar_enquetes():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM enquetes")
    enquetes = cursor.fetchall()

    conn.close()

    return jsonify([dict(enquete) for enquete in enquetes])

@app.route('/api/enquetes/<int:id>', methods=['GET'])
def obter_detalhes_enquete(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM enquetes WHERE id = ?", (id,))
    enquete = cursor.fetchone()

    if enquete is None:
        return jsonify({'error': 'Enquete não encontrada'}), 404

    cursor.execute("SELECT * FROM opcoes WHERE enquete_id = ?", (id,))
    opcoes = cursor.fetchall()

    conn.close()

    return jsonify({'enquete': dict(enquete), 'opcoes': [dict(opcao) for opcao in opcoes]})

@app.route('/api/enquetes/<int:id>/votar', methods=['POST'])
def votar_enquete(id):
    data = request.get_json()

    if 'opcao_id' not in data:
        return jsonify({'error': 'ID da opção é obrigatório'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM opcoes WHERE id = ? AND enquete_id = ?", (data['opcao_id'], id))
    opcao = cursor.fetchone()

    if opcao is None:
        return jsonify({'error': 'Opção de enquete não encontrada'}), 404

    cursor.execute("UPDATE opcoes SET votos = votos + 1 WHERE id = ?", (data['opcao_id'],))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Voto registrado com sucesso'}), 200

@app.route('/api/enquetes/<int:id>/resultados', methods=['GET'])
def obter_resultados_enquete(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM opcoes WHERE enquete_id = ?", (id,))
    opcoes = cursor.fetchall()

    conn.close()

    return jsonify([{'opcao': dict(opcao), 'votos': opcao['votos']} for opcao in opcoes])

@app.route('/api/enquetes/<int:id>/opcoes', methods=['GET'])
def visualizar_opcoes_enquete(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM opcoes WHERE enquete_id = ?", (id,))
    opcoes = cursor.fetchall()

    conn.close()

    return jsonify([dict(opcao) for opcao in opcoes])

@app.route('/api/enquetes/<int:id>/opcoes', methods=['POST'])
def adicionar_opcao_enquete(id):
    data = request.get_json()

    if 'descricao' not in data:
        return jsonify({'error': 'Descrição da opção é obrigatória'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO opcoes (enquete_id, descricao) VALUES (?, ?)", (id, data['descricao']))
    opcao_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return jsonify({'message': 'Opção adicionada com sucesso', 'opcao_id': opcao_id}), 201

@app.route('/api/enquetes/<int:id>', methods=['DELETE'])
def deletar_enquete(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM enquetes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Enquete deletada com sucesso'}), 200

@app.route('/api/enquetes/<int:id_enquete>/opcoes/<int:id_opcao>', methods=['DELETE'])
def deletar_opcao_enquete(id_enquete, id_opcao):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM opcoes WHERE id = ? AND enquete_id = ?", (id_opcao, id_enquete))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Opção deletada com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)
