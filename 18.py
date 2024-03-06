import os
import csv

def mes_com_menos_vendas(arquivo_csv):
    vendas_por_mes = {}

    with open(arquivo_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for linha in reader:
            mes = linha['Mes']
            vendas = float(linha['Vendas'])
            if mes in vendas_por_mes:
                vendas_por_mes[mes] += vendas
            else:
                vendas_por_mes[mes] = vendas

    mes_menos_vendas = min(vendas_por_mes, key=vendas_por_mes.get)
    total_vendas = vendas_por_mes[mes_menos_vendas]

    return mes_menos_vendas, total_vendas

diretorio_atual = os.path.dirname(__file__)

arquivo_csv = os.path.join(diretorio_atual, "arquivos", "mes_vendas.csv")

mes_menos_vendas, total_vendas = mes_com_menos_vendas(arquivo_csv)

print(f"O mês com menos vendas foi {mes_menos_vendas} com um total de {total_vendas} vendas.")
