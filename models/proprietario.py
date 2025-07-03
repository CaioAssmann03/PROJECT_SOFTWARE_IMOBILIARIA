from models.pessoa import Pessoa

class Proprietario(Pessoa):
    _id_counter = 1

    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.id = Proprietario._id_counter
        Proprietario._id_counter += 1
        self.imoveis_ids = []  # IDs dos imóveis que ele possui

    def adicionar_imovel(self, imovel_id):
        self.imoveis_ids.append(imovel_id)

    def __str__(self):
        return f"{super().__str__()} | Imóveis: {self.imoveis_ids}"