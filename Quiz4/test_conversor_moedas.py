import pytest
from conversor_moedas import converter_moeda

def test_real_para_dolar():
    assert converter_moeda(100, 'real', 'dolar') == 18

def test_dolar_para_real():
    assert converter_moeda(100, 'dolar', 'real') == 560

def test_dolar_para_euro():
    assert converter_moeda(100, 'dolar', 'euro') == 91

def test_moeda_invalida():
    with pytest.raises(ValueError):
        converter_moeda(100, 'real', 'euro')

def test_moeda_desconhecida():
    with pytest.raises(ValueError):
        converter_moeda(100, 'real', 'bitcoin')