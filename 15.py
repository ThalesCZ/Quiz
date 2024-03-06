import os
import json

def ler_arquivo_json(caminho_completo):
    try:
        with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"O arquivo '{caminho_completo}' não foi encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o arquivo JSON: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

diretorio_atual = os.path.dirname(__file__)

caminho_completo = os.path.join(diretorio_atual, "arquivos", "dados1.json")

dados_json = ler_arquivo_json(caminho_completo)
if dados_json:
    print("Conteúdo do arquivo JSON:")
    print(dados_json)
