produtos = []

def adicionar_produto(nome, preco):
    produtos.append({"nome": nome, "preco": preco})

def remover_produto(nome):
    global produtos
    produtos = [produto for produto in produtos if produto["nome"] != nome]

def exibir_produtos(ordenar_por="nome"):
    if ordenar_por == "nome":
        produtos_ordenados = sorted(produtos, key=lambda x: x["nome"])
    elif ordenar_por == "preco":
        produtos_ordenados = sorted(produtos, key=lambda x: x["preco"])
    else:
        print("Critério de ordenação inválido.")
        return
    for produto in produtos_ordenados:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']:.2f}")

while True:
    print("\nMenu:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Exibir produtos")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        adicionar_produto(nome, preco)
    elif opcao == "2":
        nome = input("Nome do produto a remover: ")
        remover_produto(nome)
    elif opcao == "3":
        criterio = input("Ordenar por (nome/preco): ")
        exibir_produtos(criterio)
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
