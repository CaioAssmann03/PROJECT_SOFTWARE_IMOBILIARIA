from factories.pessoa_factory import PessoaFactory
from factories.imovel_factory import ImovelFactory

def test_criar_proprietario():
    p = PessoaFactory.criar_pessoa("proprietario", "João", "123")
    assert p.nome == "João"
    assert p.cpf == "123"

def test_criar_inquilino():
    i = PessoaFactory.criar_pessoa("inquilino", "Maria", "456")
    assert i.nome == "Maria"
    assert i.cpf == "456"

def test_criar_imovel():
    imovel = ImovelFactory.criar_imovel("Rua A", "Apartamento", 1500)
    assert imovel.endereco == "Rua A"
    assert imovel.tipo == "Apartamento"
    assert imovel.valor == 1500
