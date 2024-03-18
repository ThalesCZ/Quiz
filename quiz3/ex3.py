from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

TASKS_FILE = "tasks.json"

@app.route("/")
def index():
    return "Hello, World!"


if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "w") as file:
        json.dump([], file)

def ler_tarefas():
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def escrever_tarefas(tarefas):
    with open(TASKS_FILE, "w") as file:
        json.dump(tarefas, file, indent=4)

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = ler_tarefas()
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.json
    tarefas = ler_tarefas()
    nova_tarefa['concluida'] = False
    tarefas.append(nova_tarefa)
    escrever_tarefas(tarefas)
    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def marcar_como_concluida(id):
    tarefas = ler_tarefas()
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['concluida'] = True
            escrever_tarefas(tarefas)
            return jsonify(tarefa)
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    tarefas = ler_tarefas()
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefas.remove(tarefa)
            escrever_tarefas(tarefas)
            return jsonify({'message': 'Tarefa excluída com sucesso'})
    return jsonify({'error': 'Tarefa não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
