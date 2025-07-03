class AluguelObserver:
    def notificar(self, imovel, inquilino):
        raise NotImplementedError

class LogAluguelObserver(AluguelObserver):
    def notificar(self, imovel, inquilino):
        print(f"[OBSERVER] Imóvel {imovel.id} alugado por {inquilino.nome} (CPF: {inquilino.cpf})")