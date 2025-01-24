import json

def analise_de_vendas():
    ficheiro = "caminho\\vendas.json"

    try:
        with open(ficheiro, "r") as f:
            vendas = json.load(f)
    except FileNotFoundError:
        print(f"Ficheiro '{ficheiro}' não encontrado.")
        return
    except json.JSONDecodeError:
        print(f"Erro ao ler o ficheiro '{ficheiro}'.")
        return

    total_vendas = 0
    print("\nRelatório de Vendas:")
    for produto, info in vendas.items():
        quantidade = info["quantidade"]
        preco = info["preco"]
        total = quantidade * preco
        print(f"Produto: {produto}, Quantidade: {quantidade}, Total: {total:.2f}")
        total_vendas += total

    print(f"\nTotal Geral de Vendas: {total_vendas:.2f}")

# Exemplo de ficheiro 'vendas.json':
# {
#     "Arroz": {"quantidade": 10, "preco": 1.99},
#     "Feijão": {"quantidade": 5, "preco": 3.49},
#     "Macarrão": {"quantidade": 8, "preco": 2.29}
# }

analise_de_vendas()
