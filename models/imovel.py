class Imovel:
    _id_counter = 1

    def __init__(self, endereco, tipo, valor, dormitorios):
        self.id = Imovel._id_counter
        Imovel._id_counter += 1
        self.endereco = endereco
        self.tipo = tipo
        self.valor = valor
        self.dormitorios = dormitorios
        self.disponivel = True
        self.inquilino_id = None

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
        return f"{self.tipo} com {self.dormitorios} na {self.endereco} - valor do aluguel R${self.valor}"