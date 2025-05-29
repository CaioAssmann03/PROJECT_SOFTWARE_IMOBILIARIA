from models.imovel import Imovel

class ImovelFactory:
    @staticmethod
    def criar_imovel(endereco, tipo, valor):
        return Imovel(endereco, tipo, valor)
