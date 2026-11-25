# Aula 11 | Extra 1 | Stock da loja

stock = {"camisolas": 12, "calças": 8,
         "meias": 30, "casacos": 5}

produto = input("Produto vendido? ").strip().lower()
qtd = int(input("Quantidade? "))

if produto in stock and stock[produto] >= qtd:
    stock[produto] -= qtd
    print(f"Restam {stock[produto]} {produto}.")
else:
    print("Produto inexistente ou stock insuficiente.")
