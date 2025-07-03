class Imovel:
    _id_counter = 1

    def __init__(self, endereco, tipo, valor, dormitorios, strategy=None):
        self.id = Imovel._id_counter
        Imovel._id_counter += 1
        self.endereco = endereco
        self.tipo = tipo
        self.valor = valor
        self.dormitorios = dormitorios
        self.disponivel = True
        self.inquilino_id = None
        self.strategy = strategy

    def calcular_valor(self):
        if self.strategy:
            return self.strategy.calcular(self.valor)
        return self.valor

    def alugar(self,  inquilino_id):
        if self.disponivel:
            self.disponivel = False
            self.inquilino_id = inquilino_id  # Associa o inquilino
            return True
        return False
    
    def desocupar(self):
        self.disponivel = True
        self.inquilino_id = None  # Remove a associação

    def atualizar_valor(self, novo_valor):
        self.valor = novo_valor
  
    def __str__(self):
        valor_final = self.calcular_valor()
        return f"{self.tipo} com {self.dormitorios} dormitórios na {self.endereco} - valor do aluguel R${valor_final:.2f}"
