# Aula 03 | Desafio | Fatura de eletricidade

kwh = float(input("Consumo (kWh)? "))
tipo = input("Tipo de instalação (R/C/I)? ")

if tipo == "R" and kwh <= 500:
    preco = 0.16
elif tipo == "R":
    preco = 0.20
elif tipo == "C" and kwh <= 1000:
    preco = 0.18
elif tipo == "C":
    preco = 0.15
elif tipo == "I" and kwh <= 5000:
    preco = 0.14
elif tipo == "I":
    preco = 0.12
else:
    preco = 0

if preco > 0:
    print("Preço por kWh:", preco, "€")
    print("Total a pagar:", round(kwh * preco, 2), "€")
else:
    print("Tipo de instalação inválido.")
