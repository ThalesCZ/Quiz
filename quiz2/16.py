import os

def consolidar_arquivos_texto(diretorio, arquivo_consolidado):
    conteudo_consolidado = []

    if os.path.isdir(diretorio):
        for arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            if os.path.isfile(caminho_arquivo) and arquivo.endswith('.txt'):
                with open(caminho_arquivo, 'r') as f:
                    conteudo_consolidado.append(f.read())
    
    with open(arquivo_consolidado, 'w') as f:
        for conteudo in conteudo_consolidado:
            f.write(conteudo)
            f.write('\n')  

diretorio = 'consolidar'

arquivo_consolidado = 'arquivo_consolidado.txt'

consolidar_arquivos_texto(diretorio, arquivo_consolidado)
