#Exercício 7

def interc(lista1, lista2):
    intercecao = []
    for i in lista1:
        if i in lista2 and i not in intercecao:
          intercecao.append(i)
    return intercecao

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print(interc(lista1, lista2))