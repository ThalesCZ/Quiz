from datetime import datetime
from diferenca_datas import calcular_diferenca_entre_datas

def test_diferenca_em_dias():
    data1 = datetime(2022, 1, 1)
    data2 = datetime(2022, 1, 10)
    assert calcular_diferenca_entre_datas(data1, data2, 'dias') == 9

def test_diferenca_em_meses():
    data1 = datetime(2022, 1, 1)
    data2 = datetime(2022, 3, 1)
    assert calcular_diferenca_entre_datas(data1, data2, 'meses') == 2

def test_diferenca_em_anos():
    data1 = datetime(2022, 1, 1)
    data2 = datetime(2025, 1, 1)
    assert calcular_diferenca_entre_datas(data1, data2, 'anos') == 3

def test_diferenca_em_horas():
    data1 = datetime(2022, 1, 1, 10, 0, 0)
    data2 = datetime(2022, 1, 1, 14, 30, 0)
    assert calcular_diferenca_entre_datas(data1, data2, 'horas') == 4

def test_diferenca_em_minutos():
    data1 = datetime(2022, 1, 1, 10, 0, 0)
    data2 = datetime(2022, 1, 1, 10, 10, 0)
    assert calcular_diferenca_entre_datas(data1, data2, 'minutos') == 10

def test_unidade_invalida():
    data1 = datetime(2022, 1, 1)
    data2 = datetime(2022, 1, 10)
    with pytest.raises(ValueError):
        calcular_diferenca_entre_datas(data1, data2, 'semanas')