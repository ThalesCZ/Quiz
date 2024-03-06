#Exercício 13

import os

def ler_arquivo(caminho_completo):
    try:
        with open(caminho_completo, 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print("O arquivo", caminho_completo, "não foi encontrado.")
        return None
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo:", e)
        return None

diretorio_atual = os.path.dirname(__file__)
caminho_completo = os.path.join(diretorio_atual, "arquivos", "arquivo.txt")
texto = ler_arquivo(caminho_completo)
if texto is not None:
    print("Conteúdo do arquivo:")
    print(texto)

