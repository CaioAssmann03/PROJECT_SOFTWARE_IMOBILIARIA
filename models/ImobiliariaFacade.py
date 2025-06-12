from factories.pessoa_factory import PessoaFactory
from factories.imovel_factory import ImovelFactory
from database.db_singleton import Database
from decorators.log_decorator import log_operacao


class ImobiliariaFacade:
    def __init__(self):
        self.db = Database.get_instancia()

    def cadastrar_proprietario(self, nome, cpf):
        proprietario = PessoaFactory.criar_pessoa("proprietario", nome, cpf)
        self.db.dados["proprietarios"].append(proprietario)
        return proprietario

    def cadastrar_inquilino(self, nome, cpf):
        inquilino = PessoaFactory.criar_pessoa("inquilino", nome, cpf)
        self.db.dados["inquilinos"].append(inquilino)
        return inquilino

    def cadastrar_imovel(self, endereco, tipo, valor, dormitorios, proprietario):
        imovel = ImovelFactory.criar_imovel(endereco, tipo, valor, dormitorios)
        proprietario.adicionar_imovel(imovel.id)
        self.db.dados["imoveis"].append(imovel)
        return imovel

    def alugar_imovel(self, inquilino, imovel_id):
        imovel = next((i for i in self.db.dados["imoveis"] if i.id == imovel_id), None)
        if imovel and imovel.alugar(inquilino.cpf):
            inquilino.alugar_imovel(imovel.id)
            return True
        return False
    
    @log_operacao
    def alugar_imovel(self, inquilino, imovel_id):
        imovel = next((i for i in self.db.dados["imoveis"] if i.id == imovel_id), None)
        if imovel and imovel.alugar(inquilino.cpf):
            inquilino.alugar_imovel(imovel.id)
            return True
        return False


    def log_operacao(func):
        def wrapper(*args, **kwargs):
            print(f"[LOG] Executando: {func.__name__}")
            resultado = func(*args, **kwargs)
            print(f"[LOG] Finalizado: {func.__name__}")
            return resultado
        return wrapper