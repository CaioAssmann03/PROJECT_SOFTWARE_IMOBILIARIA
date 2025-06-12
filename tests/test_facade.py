import unittest
from models.ImobiliariaFacade import ImobiliariaFacade

class TestImobiliariaFacade(unittest.TestCase):
    def test_alugar_imovel(self):
        facade = ImobiliariaFacade()
        p = facade.cadastrar_proprietario("Ana", "111")
        i = facade.cadastrar_inquilino("Beto", "222")
        imovel = facade.cadastrar_imovel("Rua X", "Apto", 1500, 2, p)
        alugado = facade.alugar_imovel(i, imovel.id)
        self.assertTrue(alugado)
        self.assertFalse(imovel.disponivel)
        self.assertIn(imovel.id, i.imoveis_alugados_ids)

if __name__ == "__main__":
    unittest.main()

# para executar python -m unittest discover tests
