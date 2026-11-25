# Aula 01 | Desafio | Dividir a conta do jantar
# Entrada: valor total da conta e número de pessoas
# Saída: valor que cada pessoa paga

total = float(input("Qual é o valor total da conta (€)? "))
pessoas = int(input("Quantas pessoas vão dividir? "))

por_pessoa = total / pessoas

print("Cada pessoa paga", round(por_pessoa, 2), "€")
