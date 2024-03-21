taxas = {
    'real_para_dolar': 0.18,
    'dolar_para_real': 5.6,
    'euro_para_dolar': 1.1,
    'dolar_para_euro': 0.91
}

def converter_moeda(valor, moeda_origem, moeda_destino):
    if (moeda_origem + '_para_' + moeda_destino) in taxas:
        taxa = taxas[moeda_origem + '_para_' + moeda_destino]
        return valor * taxa
    elif (moeda_destino + '_para_' + moeda_origem) in taxas:
        taxa = 1 / taxas[moeda_destino + '_para_' + moeda_origem]
        return valor / taxa
    else:
        raise ValueError("Taxa de conversão não encontrada")