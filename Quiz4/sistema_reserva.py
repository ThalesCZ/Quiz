class SistemaReserva:
    def __init__(self):
        self.voos_disponiveis = {}
        self.reservas = {}

    def adicionar_voo(self, voo_id, capacidade):
        if voo_id in self.voos_disponiveis:
            raise ValueError("Voo já existe")
        self.voos_disponiveis[voo_id] = capacidade

    def pesquisar_voos(self, voo_id):
        return self.voos_disponiveis.get(voo_id)

    def realizar_reserva(self, voo_id, quantidade):
        if voo_id not in self.voos_disponiveis:
            raise ValueError("Voo não encontrado")
        if quantidade > self.voos_disponiveis[voo_id]:
            raise ValueError("Capacidade insuficiente para realizar a reserva")
        if voo_id in self.reservas:
            self.reservas[voo_id] += quantidade
        else:
            self.reservas[voo_id] = quantidade
        self.voos_disponiveis[voo_id] -= quantidade

    def visualizar_reservas(self, voo_id):
        return self.reservas.get(voo_id, 0)

    def cancelar_reserva(self, voo_id, quantidade):
        if voo_id not in self.reservas:
            raise ValueError("Nenhuma reserva encontrada para este voo")
        if quantidade > self.reservas[voo_id]:
            raise ValueError("Quantidade de reservas a cancelar excede o número de reservas existentes")
        self.reservas[voo_id] -= quantidade
        self.voos_disponiveis[voo_id] += quantidade