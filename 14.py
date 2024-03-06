import os
import csv

def ler_arquivo_csv(caminho_completo):
    try:
        with open(caminho_completo, newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            dados = []
            for linha in leitor_csv:
                dados.append(linha)
            return dados
    except FileNotFoundError:
        print("O arquivo", caminho_completo, "não foi encontrado.")
        return None
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo CSV:", e)
        return None

diretorio_atual = os.path.dirname(__file__)

caminho_completo = os.path.join(diretorio_atual, "arquivos", "dados.csv")

dados_csv = ler_arquivo_csv(caminho_completo)
if dados_csv is not None:
    print("Conteúdo do arquivo CSV:")
    for linha in dados_csv:
        print(linha)
