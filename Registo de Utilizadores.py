import json

def registo_de_utilizadores():
    ficheiro = "utilizadores.json"

    def carregar_dados():
        try:
            with open(ficheiro, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def salvar_dados(dados):
        with open(ficheiro, "w") as f:
            json.dump(dados, f, indent=4)

    while True:
        print("\nMenu:")
        print("1. Adicionar utilizador")
        print("2. Atualizar utilizador")
        print("3. Remover utilizador")
        print("4. Listar utilizadores")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        dados = carregar_dados()

        if opcao == "1":
            nome = input("Nome: ")
            idade = input("Idade: ")
            dados[nome] = {"idade": idade}
            salvar_dados(dados)
            print(f"Utilizador {nome} adicionado com sucesso!")

        elif opcao == "2":
            nome = input("Nome do utilizador a atualizar: ")
            if nome in dados:
                idade = input("Nova idade: ")
                dados[nome]["idade"] = idade
                salvar_dados(dados)
                print(f"Utilizador {nome} atualizado com sucesso!")
            else:
                print("Utilizador não encontrado.")

        elif opcao == "3":
            nome = input("Nome do utilizador a remover: ")
            if nome in dados:
                del dados[nome]
                salvar_dados(dados)
                print(f"Utilizador {nome} removido com sucesso!")
            else:
                print("Utilizador não encontrado.")

        elif opcao == "4":
            if dados:
                print("\nUtilizadores registados:")
                for nome, info in dados.items():
                    print(f"Nome: {nome}, Idade: {info['idade']}")
            else:
                print("Nenhum utilizador registado.")

        elif opcao == "5":
            break

        else:
            print("Opção inválida.")

registo_de_utilizadores()
