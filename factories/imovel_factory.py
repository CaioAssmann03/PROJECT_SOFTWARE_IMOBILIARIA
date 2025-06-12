from models.imovel import Imovel

class ImovelFactory:
    @staticmethod
    def criar_imovel(endereco, tipo, valor, dormitorios):
        return Imovel(endereco, tipo, valor, dormitorios)
