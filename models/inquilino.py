from models.pessoa import Pessoa


class Inquilino(Pessoa):
    _id_counter = 1

    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.id = Inquilino._id_counter
        Inquilino._id_counter += 1
        self.imoveis_alugados_ids = []  # IDs dos imóveis alugados

    def alugar_imovel(self, imovel_id):
        self.imoveis_alugados_ids.append(imovel_id)

    def __str__(self):
        return f"Inquilino: {self.nome} (CPF: {self.cpf}, ID: {self.id}) | Imóveis alugados: {self.imoveis_alugados_ids}"