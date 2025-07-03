class AluguelStrategy:
    def calcular(self, valor_base):
        raise NotImplementedError

class AluguelNormal(AluguelStrategy):
    def calcular(self, valor_base):
        return valor_base

class AluguelComDesconto(AluguelStrategy):
    def calcular(self, valor_base):
        return valor_base * 0.9  # 10% de desconto

class AluguelComTaxa(AluguelStrategy):
    def calcular(self, valor_base):
        return valor_base * 1.05  # 5% de taxa