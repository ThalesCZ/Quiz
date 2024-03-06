#Exercício 6

def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("Erro: As matrizes devem ter as mesmas dimensões para realizar a soma.")
        return None

    resultado = [[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    return resultado

# Exemplo de uso:
matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

resultado = soma_matrizes(matriz1, matriz2)
if resultado:
    print("Matriz Resultado:")
    for linha in resultado:
        print(linha)
