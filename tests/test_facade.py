import unittest
from models.ImobiliariaFacade import ImobiliariaFacade
from strategies.aluguel_strategy import AluguelNormal, AluguelComDesconto, AluguelComTaxa

class TestImobiliariaFacade(unittest.TestCase):
    def setUp(self):
        self.facade = ImobiliariaFacade()

    def test_cadastrar_proprietario(self):
        p = self.facade.cadastrar_proprietario("João", "123")
        self.assertEqual(p.nome, "João")
        self.assertEqual(p.cpf, "123")
        self.assertIn(p, self.facade.db.dados["proprietarios"])

    def test_cadastrar_inquilino(self):
        i = self.facade.cadastrar_inquilino("Maria", "456")
        self.assertEqual(i.nome, "Maria")
        self.assertEqual(i.cpf, "456")
        self.assertIn(i, self.facade.db.dados["inquilinos"])

    def test_cadastrar_imovel(self):
        p = self.facade.cadastrar_proprietario("João", "123")
        imovel = self.facade.cadastrar_imovel("Rua X", "Casa", 1000, 2, p, AluguelNormal())
        self.assertEqual(imovel.endereco, "Rua X")
        self.assertEqual(imovel.tipo, "Casa")
        self.assertIn(imovel, self.facade.db.dados["imoveis"])
        self.assertIn(imovel.id, p.imoveis_ids)

    def test_alugar_imovel(self):
        p = self.facade.cadastrar_proprietario("João", "123")
        i = self.facade.cadastrar_inquilino("Maria", "456")
        imovel = self.facade.cadastrar_imovel("Rua X", "Casa", 1000, 2, p, AluguelNormal())
        alugado = self.facade.alugar_imovel(i, imovel.id)
        self.assertTrue(alugado)
        self.assertFalse(imovel.disponivel)
        self.assertIn(imovel.id, i.imoveis_alugados_ids)

    def test_strategy_desconto(self):
        p = self.facade.cadastrar_proprietario("João", "123")
        imovel = self.facade.cadastrar_imovel("Rua Y", "Apto", 2000, 3, p, AluguelComDesconto())
        self.assertAlmostEqual(imovel.calcular_valor(), 1800.0)

    def test_strategy_taxa(self):
        p = self.facade.cadastrar_proprietario("João", "123")
        imovel = self.facade.cadastrar_imovel("Rua Z", "Apto", 2000, 3, p, AluguelComTaxa())
        self.assertAlmostEqual(imovel.calcular_valor(), 2100.0)

    def test_nao_aluga_imovel_ja_alugado(self):
        p = self.facade.cadastrar_proprietario("João", "123")
        i1 = self.facade.cadastrar_inquilino("Maria", "456")
        i2 = self.facade.cadastrar_inquilino("Carlos", "789")
        imovel = self.facade.cadastrar_imovel("Rua X", "Casa", 1000, 2, p, AluguelNormal())
        self.facade.alugar_imovel(i1, imovel.id)
        alugado = self.facade.alugar_imovel(i2, imovel.id)
        self.assertFalse(alugado)

if __name__ == "__main__":
    unittest.main()

# para executar python -m unittest discover tests
