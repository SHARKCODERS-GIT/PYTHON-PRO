def lista_de_compras():
    while True:
        print("\nMenu:")
        print("1. Adicionar item à lista")
        print("2. Exibir lista de compras")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Digite o item para adicionar à lista: ")
            with open("compras.txt", "a") as ficheiro:
                ficheiro.write(f"{item}\n")
        elif opcao == "2":
            try:
                with open("compras.txt", "r") as ficheiro:
                    itens = ficheiro.readlines()
                    if itens:
                        print("Itens na lista de compras:")
                        for i, item in enumerate(itens, 1):
                            print(f"{i}. {item.strip()}")
                    else:
                        print("A lista de compras está vazia.")
            except FileNotFoundError:
                print("Ainda não há lista de compras criada.")
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

lista_de_compras()
