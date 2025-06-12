from models.pessoa import Pessoa

class Proprietario(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.imoveis_ids = []  # IDs dos imóveis que ele possui

    def adicionar_imovel(self, imovel_id):
        self.imoveis_ids.append(imovel_id)

    def __str__(self):
        return f"{super().__str__()} | ID Imóvel: {self.imoveis_ids}"