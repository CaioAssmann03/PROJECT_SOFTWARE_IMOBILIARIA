from models.ImobiliariaFacade import ImobiliariaFacade

facade = ImobiliariaFacade()

def menu():
    while True:
        print("\n--- MENU IMOBILIÁRIA ---")
        print("1 - Cadastrar Proprietário")
        print("2 - Cadastrar Inquilino")
        print("3 - Cadastrar Imóvel")
        print("4 - Alugar Imóvel")
        print("5 - Listar Proprietários")
        print("6 - Listar Inquilinos")
        print("7 - Listar Imóveis")
        print("8 - Listar Imóveis Alugados e Inquilinos")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do proprietário: ")
            cpf = input("CPF do proprietário: ")
            p = facade.cadastrar_proprietario(nome, cpf)
            print("Proprietário cadastrado:", p)
        elif opcao == "2":
            nome = input("Nome do inquilino: ")
            cpf = input("CPF do inquilino: ")
            i = facade.cadastrar_inquilino(nome, cpf)
            print("Inquilino cadastrado:", i)
        elif opcao == "3":
            endereco = input("Endereço do imóvel: ")
            tipo = input("Tipo do imóvel: ")
            valor = float(input("Valor do aluguel: "))
            dormitorios = int(input("Número de dormitórios: "))
            print("Proprietários disponíveis:")
            for idx, prop in enumerate(facade.db.dados["proprietarios"]):
                print(f"{idx} - {prop}")
            idx_prop = int(input("Escolha o proprietário pelo número: "))
            proprietario = facade.db.dados["proprietarios"][idx_prop]
            imovel = facade.cadastrar_imovel(endereco, tipo, valor, dormitorios, proprietario)
            print("Imóvel cadastrado:", imovel)
        elif opcao == "4":
            print("Inquilinos disponíveis:")
            for idx, inq in enumerate(facade.db.dados["inquilinos"]):
                print(f"{idx} - {inq}")
            idx_inq = int(input("Escolha o inquilino pelo número: "))
            inquilino = facade.db.dados["inquilinos"][idx_inq]
            print("Imóveis disponíveis para aluguel:")
            for idx, imv in enumerate(facade.db.dados["imoveis"]):
                status = "Disponível" if imv.disponivel else f"Alugado por CPF {imv.inquilino_id}"
                print(f"{idx} - {imv} [{status}]")
            idx_imv = int(input("Escolha o imóvel pelo número: "))
            imovel = facade.db.dados["imoveis"][idx_imv]
            if imovel.disponivel:
                if facade.alugar_imovel(inquilino, imovel.id):
                    print(f"Inquilino {inquilino.nome} alugou o imóvel {imovel.id} com sucesso!")
                else:
                    print("Não foi possível alugar o imóvel.")
            else:
                print(f"Imóvel já está alugado por CPF {imovel.inquilino_id}.")
        elif opcao == "5":
            print("Proprietários:")
            for p in facade.db.dados["proprietarios"]:
                print(p)
        elif opcao == "6":
            print("Inquilinos:")
            for i in facade.db.dados["inquilinos"]:
                print(i)
        elif opcao == "7":
            print("Imóveis:")
            for imv in facade.db.dados["imoveis"]:
                print(imv)
        elif opcao == "8":
            print("Imóveis Alugados e seus Inquilinos:")
            for imv in facade.db.dados["imoveis"]:
                if not imv.disponivel and imv.inquilino_id:
                    # Busca o nome do inquilino pelo CPF
                    inquilino = next((i for i in facade.db.dados["inquilinos"] if i.cpf == imv.inquilino_id), None)
                    nome_inquilino = inquilino.nome if inquilino else "Desconhecido"
                    print(f"{imv} | Alugado por: {nome_inquilino} (CPF: {imv.inquilino_id})")
        elif opcao == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()