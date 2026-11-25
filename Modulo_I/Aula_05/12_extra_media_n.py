# Aula 05 | Extra 5 | Média de N notas

n = int(input("Quantas notas? "))
soma = 0

for i in range(1, n + 1):
    nota = float(input("Nota " + str(i) + "? "))
    soma = soma + nota

print("Média:", round(soma / n, 1))
