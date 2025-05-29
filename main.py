from factories.pessoa_factory import PessoaFactory
from factories.imovel_factory import ImovelFactory
from database.db_singleton import Database

# Exemplo de uso
db = Database.get_instancia()

p1 = PessoaFactory.criar_pessoa("proprietario", "João", "123456")
i1 = PessoaFactory.criar_pessoa("inquilino", "Maria", "654321")
imovel1 = ImovelFactory.criar_imovel("Rua A, 123", "Casa", 2500)

db.dados["proprietarios"].append(p1)
db.dados["inquilinos"].append(i1)
db.dados["imoveis"].append(imovel1)

print("Cadastro realizado com sucesso!", p1)
