class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nome} (CPF: {self.cpf})"
