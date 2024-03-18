#Exercício 9

def encontrar_par_soma(lista, alvo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares

lista = [1, 2, 3, 4, 5]
alvo = 6
pares = encontrar_par_soma(lista, alvo)
print(f"Pares na lista cuja soma é {alvo}: {pares}")
