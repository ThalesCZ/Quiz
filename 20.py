import os
import csv

def vendedor_com_mais_e_menos_vendas(arquivo_csv):
    vendas_por_vendedor = {}

    with open(arquivo_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for linha in reader:
            vendedor = linha['Vendedor']
            venda = float(linha['Venda'])
            if vendedor in vendas_por_vendedor:
                vendas_por_vendedor[vendedor] += venda
            else:
                vendas_por_vendedor[vendedor] = venda

    vendedor_mais_vendeu = max(vendas_por_vendedor, key=vendas_por_vendedor.get)
    maior_venda = vendas_por_vendedor[vendedor_mais_vendeu]

    vendedor_menos_vendeu = min(vendas_por_vendedor, key=vendas_por_vendedor.get)
    menor_venda = vendas_por_vendedor[vendedor_menos_vendeu]

    return vendedor_mais_vendeu, maior_venda, vendedor_menos_vendeu, menor_venda

diretorio_atual = os.path.dirname(__file__)

arquivo_csv = os.path.join(diretorio_atual, "arquivos", "vendas.csv")

mais_vendeu, valor_mais_vendas, menos_vendeu, valor_menos_vendas = vendedor_com_mais_e_menos_vendas(arquivo_csv)

print(f"O vendedor que mais vendeu foi {mais_vendeu} com um total de {valor_mais_vendas} vendas.")
print(f"O vendedor que menos vendeu foi {menos_vendeu} com um total de {valor_menos_vendas} vendas.")
