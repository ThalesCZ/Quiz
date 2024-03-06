#Exercício 12

def encontrar_menor_string(lista_de_strings):
    if not lista_de_strings:  
        return None

    menor_string = lista_de_strings[0]  
    for string in lista_de_strings:
        if len(string) < len(menor_string):  
            menor_string = string  
    return menor_string

lista = ["banana", "maçã", "laranja", "uva", "abacaxi"]
menor = encontrar_menor_string(lista)
print("Menor string na lista:", menor)
