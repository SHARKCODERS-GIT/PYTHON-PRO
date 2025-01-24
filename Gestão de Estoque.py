estoque = {}

def adicionar_item(nome, quantidade, preco):
    if nome in estoque:
        print("Item já existe. Atualizando quantidade e preço.")
        estoque[nome]["quantidade"] += quantidade
        estoque[nome]["preco"] = preco
    else:
        estoque[nome] = {"quantidade": quantidade, "preco": preco}

def buscar_item(nome):
    if nome in estoque:
        item = estoque[nome]
        print(f"Nome: {nome}, Quantidade: {item['quantidade']}, Preço Unitário: {item['preco']:.2f}")
    else:
        print("Item não encontrado.")

def atualizar_item(nome):
    if nome in estoque:
        quantidade = int(input("Nova quantidade: "))
        preco = float(input("Novo preço unitário: "))
        estoque[nome]["quantidade"] = quantidade
        estoque[nome]["preco"] = preco
        print("Item atualizado com sucesso.")
    else:
        print("Item não encontrado.")

def exibir_estoque():
    print("\nEstoque Atual:")
    for nome, dados in estoque.items():
        print(f"Nome: {nome}, Quantidade: {dados['quantidade']}, Preço Unitário: {dados['preco']:.2f}")

while True:
    print("\nMenu:")
    print("1. Adicionar item")
    print("2. Buscar item")
    print("3. Atualizar item")
    print("4. Exibir estoque")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do item: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço unitário: "))
        adicionar_item(nome, quantidade, preco)
    elif opcao == "2":
        nome = input("Nome do item a buscar: ")
        buscar_item(nome)
    elif opcao == "3":
        nome = input("Nome do item a atualizar: ")
        atualizar_item(nome)
    elif opcao == "4":
        exibir_estoque()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")
