# Aula 05 | Exercício 3 | Somatório

n = int(input("Somar de 1 até? "))
soma = 0

for i in range(1, n + 1):
    soma = soma + i

print("A soma de 1 a", n, "é", soma)
