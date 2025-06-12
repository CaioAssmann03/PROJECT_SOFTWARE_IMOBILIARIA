from models.pessoa import Pessoa


class Inquilino(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.imoveis_alugados_ids = []  # IDs dos imóveis alugados

    def alugar_imovel(self, imovel_id):
        self.imoveis_alugados_ids.append(imovel_id)