# Aula 01 | Extra 5 | Conversor de euros para dólares
# Entrada: valor em euros e taxa de câmbio do dia
# Saída: valor em dólares

euros = float(input("Valor em euros? "))
taxa = float(input("Taxa de câmbio (1 € = ? $)? "))

dolares = euros * taxa

print(euros, "€ =", round(dolares, 2), "$")
