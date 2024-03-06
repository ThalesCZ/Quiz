#Exercício 5

def k_maiores(lista, k):
    lista.sort(reverse=True)

    return lista[:k]

lista = [4, 7, 2, 9, 1, 5, 8]
k = 3
print(f"{k} maiores elementos em {lista}: {k_maiores(lista, k)}")
