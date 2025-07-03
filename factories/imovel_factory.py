from models.imovel import Imovel

class ImovelFactory:
    @staticmethod
    def criar_imovel(endereco, tipo, valor, dormitorios, strategy=None):
        return Imovel(endereco, tipo, valor, dormitorios, strategy)
