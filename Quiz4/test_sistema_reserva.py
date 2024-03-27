from sistema_reserva import SistemaReserva
import pytest

def sistema_reserva():
    return SistemaReserva()

def test_adicionar_voo(sistema_reserva):
    sistema_reserva.adicionar_voo("Voo001", 100)
    assert sistema_reserva.voos_disponiveis["Voo001"] == 100

def test_pesquisar_voos(sistema_reserva):
    sistema_reserva.adicionar_voo("Voo001", 100)
    assert sistema_reserva.pesquisar_voos("Voo001") == 100
    assert sistema_reserva.pesquisar_voos("Voo002") == None

def test_realizar_reserva(sistema_reserva):
    sistema_reserva.adicionar_voo("Voo001", 100)
    sistema_reserva.realizar_reserva("Voo001", 50)
    assert sistema_reserva.voos_disponiveis["Voo001"] == 50
    assert sistema_reserva.reservas["Voo001"] == 50

def test_visualizar_reservas(sistema_reserva):
    sistema_reserva.adicionar_voo("Voo001", 100)
    sistema_reserva.realizar_reserva("Voo001", 50)
    assert sistema_reserva.visualizar_reservas("Voo001") == 50
    assert sistema_reserva.visualizar_reservas("Voo002") == 0

def test_cancelar_reserva(sistema_reserva):
    sistema_reserva.adicionar_voo("Voo001", 100)
    sistema_reserva.realizar_reserva("Voo001", 50)
    sistema_reserva.cancelar_reserva("Voo001", 20)
    assert sistema_reserva.voos_disponiveis["Voo001"] == 70
    assert sistema_reserva.reservas["Voo001"] == 30

def test_adicionar_voo_existente(sistema_reserva):
    sistema_reserva.adicionar_voo("Voo001", 100)
    with pytest.raises(ValueError):
        sistema_reserva.adicionar_voo("Voo001", 50)

def test_realizar_reserva_capacidade_insuficiente(sistema_reserva):
    sistema_reserva.adicionar_voo("Voo001", 100)
    with pytest.raises(ValueError):
        sistema_reserva.realizar_reserva("Voo001", 120)

def test_cancelar_reserva_inexistente(sistema_reserva):
    sistema_reserva.adicionar_voo("Voo001", 100)
    with pytest.raises(ValueError):
        sistema_reserva.cancelar_reserva("Voo002", 20)

def test_cancelar_reserva_quantidade_invalida(sistema_reserva):
    sistema_reserva.adicionar_voo("Voo001", 100)
    sistema_reserva.realizar_reserva("Voo001", 50)
    with pytest.raises(ValueError):
        sistema_reserva.cancelar_reserva("Voo001", 60)