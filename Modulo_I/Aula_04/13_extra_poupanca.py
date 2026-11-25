# Aula 04 | Extra 5 | Poupança mensal

objetivo = float(input("Objetivo (€)? "))
mensal = float(input("Poupança por mês (€)? "))
total = 0
mes = 0

while total < objetivo:
    mes = mes + 1
    total = total + mensal
    print("Mês", mes, ":", total, "€")

print("Objetivo atingido em", mes, "meses.")
