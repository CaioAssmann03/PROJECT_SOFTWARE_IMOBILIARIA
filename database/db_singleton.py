class Database:
    _instancia = None

    def __init__(self):
        if Database._instancia is not None:
            raise Exception("Use get_instancia() para acessar o banco.")
        self.dados = {"proprietarios": [], "inquilinos": [], "imoveis": []}

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = Database()
        return cls._instancia
