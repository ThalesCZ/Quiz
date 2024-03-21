from datetime import datetime

def calcular_diferenca_entre_datas(data1, data2, unidade='dias'):
    if unidade == 'dias':
        return abs((data2 - data1).days)
    elif unidade == 'meses':
        anos = data2.year - data1.year
        meses = data2.month - data1.month
        diferenca_meses = anos * 12 + meses
        if data2.day < data1.day:
            diferenca_meses -= 1
        return abs(diferenca_meses)
    elif unidade == 'anos':
        return abs(data2.year - data1.year)
    elif unidade == 'horas':
        return abs((data2 - data1).total_seconds() // 3600)
    elif unidade == 'minutos':
        return abs((data2 - data1).total_seconds() // 60)
    else:
        raise ValueError("Unidade de diferença inválida")
