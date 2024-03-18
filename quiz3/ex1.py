from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculadora', methods=['POST'])
def calcular():
    dados = request.get_json()
    num1 = dados['numero1']
    num2 = dados['numero2']
    operacao = dados['operacao']

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Os números fornecidos não são válidos'}), 400

    if operacao == 'adicao':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        if num2 == 0:
            return jsonify({'error': 'Não é possível dividir por zero'}), 400
        resultado = num1 / num2
    else:
        return jsonify({'error': 'Operação inválida. Escolha entre adicao, subtracao, multiplicacao ou divisao'}), 400

    return jsonify({'resultado': resultado}), 200

if __name__ == '__main__':
    app.run(debug=True)
