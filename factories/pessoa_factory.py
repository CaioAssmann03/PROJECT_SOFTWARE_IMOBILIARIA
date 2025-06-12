from models.proprietario import Proprietario
from models.inquilino import Inquilino
class PessoaFactory:
    @staticmethod
    def criar_pessoa(tipo, nome, cpf):
        if tipo == 'proprietario':
            return Proprietario(nome, cpf)
        elif tipo == 'inquilino':
            return Inquilino(nome, cpf)
        else:
            raise ValueError("Tipo de pessoa inválido.")
