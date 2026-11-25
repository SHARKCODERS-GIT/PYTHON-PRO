# Aula 05 | Exercício 4 | Números pares num intervalo

inicio = int(input("Número inicial? "))
fim = int(input("Número final? "))

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        print(i, end=" ")
