# Aula 02 | Exercício 5 | Preço final de um carro

modelo = input("Modelo do carro? ")
preco_fabrica = float(input("Preço de fábrica (€)? "))

com_impostos = preco_fabrica * 1.23
preco_final = com_impostos * 1.10

print("O", modelo, "custa", round(preco_final, 2), "€")
