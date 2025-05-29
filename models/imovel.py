class Imovel:
    def __init__(self, endereco, tipo, valor):
        self.endereco = endereco
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        return f"{self.tipo} em {self.endereco} - R${self.valor}"